---
name: orchestrator
description: Run the full lead-qualifier-suite pipeline in one pass per company — qualify, and only if the lead qualifies, immediately write personalization lines and draft the Gamma deck from the same website visit. Use this when the user wants the whole pipeline run efficiently (one site visit per company) rather than three separate sweeps over the sheet.
date_created: 2026-07-18
date_modified: 2026-07-18
status: reference
---

# Orchestrator

Master skill for `lead-qualifier-suite`. Unlike a simple "run these three skills back to back," this skill owns the n8n research loop itself so that **each company's website is visited exactly once**, and qualification, personalization, and gamma-deck content are all produced from that single visit for rows that qualify. Rows that don't qualify never get a second look — no personalization, no gamma content, no Gamma API call.

Use this skill when the user asks to run the whole pipeline (e.g. "qualify this sheet and get me decks for everyone" or "run the full thing efficiently"). If the user only wants one stage in isolation (e.g. "just qualify this sheet," "regenerate the Gamma decks with a new spec," "backfill personalization for rows I already qualified"), use the dedicated `qualification`, `personalization`, or `gamma-deck` skill instead — those still do their own independent sweeps (and, for `gamma-deck`, its own fresh site visit) and are the right tool for touching up or re-running a single stage after the fact.

Read `skills/qualification/references/default-target-profile.md`, `skills/personalization/references/personalization-spec.md`, and `skills/gamma-deck/references/gamma-deck-spec.md` before running — this skill reuses all three contracts but does not duplicate their content here.

## Stage 1: Setup (no site visits yet)

1. Ask for the Google Sheet URL or ID. Use Composio MCP to read the headers and identify the website column and optional company-name column, same as the `qualification` skill's Stage 1.
2. Collaborate on and lock the **personalization** wording contract (template, custom fields, wording pattern, max length, prohibited claims) per `personalization-spec.md`. Show a worked example and wait for explicit approval.
3. Collaborate on and lock the **gamma-deck** wording contract (cover-line pattern, video-brief pattern, max length) per `gamma-deck-spec.md`. Show a worked example and wait for explicit approval.
4. Initialize all three stages against one shared output directory, in order:

```powershell
python "${CLAUDE_PLUGIN_ROOT}\scripts\company_qualifier.py" init --sheet-id "<sheet-id>" --website-column "<column>" [--company-column "<column>"] --output-dir "<workspace>\outputs"
python "${CLAUDE_PLUGIN_ROOT}\scripts\company_qualifier.py" init-personalization --output-dir "<workspace>\outputs" --spec "<approved-personalization-spec.json>"
python "${CLAUDE_PLUGIN_ROOT}\scripts\company_qualifier.py" init-gamma --output-dir "<workspace>\outputs" --spec "<approved-gamma-spec.json>"
```

5. Take the final `output_columns` list (from the `init-gamma` response — it's cumulative) and diff it against the sheet's current headers via Composio. Create only the columns that are actually missing; never recreate an existing one.
6. Remind the user to confirm the n8n workflow's **Sheet Column Config** node is pointed at this sheet's actual website/company headers before Stage 2 begins — this skill does not configure that node itself.

Do not skip either approval gate to save time. Both must be locked before any row is processed, since the whole point of one-visit-per-company is that there's no second pass to fix wording later without a full re-run.

## Stage 2: Combined research loop (one visit per company)

"One visit per company" here means two separate things, both required: (a) within a single row, one site visit covers qualification, personalization, and gamma material — never three separate visits for the same row; and (b) across rows that share a company, the second and later rows must reuse the first row's output instead of visiting the site or calling Gamma again. Point (b) is the cross-row dedup described in step 2 below — without it, a sheet with several contacts per company would still redo the research and, worse, call the paid Gamma API once per contact for identical decks.

Repeat until n8n reports no rows left:

1. Call the n8n webhook to get the next batch (same contract as the `qualification` skill):

```
GET https://n8n-acx-v2-clone-u40987.vm.elestio.app/webhook/bdc80d7d-0f32-4dd5-9d77-c658660aedc9
Body (JSON): { "googleSheetUrl": "<sheet-url>", "batchNumber": <n> }
```

   Start at `batchNumber=1`, increment per call. Empty `rows` array means done.

2. **Dedup check before any research.** For every row in the batch, normalize its raw website into a domain and check the cross-row cache for a prior qualification result:

```powershell
python "${CLAUDE_PLUGIN_ROOT}\scripts\company_qualifier.py" lookup-domain --output-dir "<workspace>\outputs" --website "<row's raw website value>" --stage qualification
```

   Split the batch: rows with `cached: true` skip straight to step 5 using the cached `sheet_row` (plus, if that domain also has cached `personalization`/`gamma` entries — check both stages the same way — reuse those too instead of drafting or calling Gamma again). Rows with `cached: false` proceed through steps 3-4 for a fresh visit. If two uncached rows in the same batch share a domain, only one of them should actually do the research/draft/Gamma-call work — the other should wait for that result and then reuse it, exactly as if it had been cache-hit.

3. Research the remaining (uncached, non-duplicate) rows in parallel — visit every website simultaneously, **once each**, then process each row independently through the steps below using only that one visit's findings.

For each uncached row:

1. Visit the normalized website (homepage first, then product/features/pricing/about/blog as needed to cover qualification, personalization, and video-idea material in one pass). Fall back to Exa MCP if direct access is unreliable; mark `failed` if the site still cannot be verified.
2. Qualify: choose a label per the target profile, write company description, qualification reason, evidence summary, and source URL. Build the qualification result JSON (with `_raw_website`/`_raw_company`) and validate it:

```powershell
python "${CLAUDE_PLUGIN_ROOT}\scripts\company_qualifier.py" validate-qualification-result --output-dir "<workspace>\outputs" --result "<qual-result.json>"
```

   The validator's response includes `normalized_domain` and also caches this `sheet_row` under it — note this domain, it's needed for the personalization/gamma `_normalized_domain` fields below.
3. **If `research_status = failed` or `qualification_label = skip`**: the row is done. Take the `sheet_row` from the validator as-is (personalization and gamma fields stay blank/default), set `gamma_deck_status = skipped` if the label was `skip` (leave blank if it was a research failure), and go to step 5. Do not draft personalization lines or gamma content, and do not call Gamma.
4. **Otherwise (qualifying, successful row)** — from the same visit's findings, not a fresh one:
   a. Draft the approved personalization custom field(s). Build a result JSON with those fields plus `_qualification_label` and `_normalized_domain` (from step 2 above), then validate:

   ```powershell
   python "${CLAUDE_PLUGIN_ROOT}\scripts\company_qualifier.py" validate-personalization-result --output-dir "<workspace>\outputs" --result "<personalization-result.json>"
   ```

   b. Draft the gamma cover line and 3 video ideas (title + brief per the approved contract, grounded only in this visit's findings). Titles must pass the title quality bar in `skills/gamma-deck/references/gamma-deck-spec.md`: grounded in a specific real capability (not generic enough to fit any competitor), broad enough that a real audience searches for the underlying problem (not so niche it only means something to existing users), and phrased with a curiosity/viral hook. Redraft any title that fails either side of that balance.
   c. Call `generate_from_template` (Gamma MCP) with `gammaId: "2bvn38zphijx223"` and a prompt that replaces `{{COMPANY NAME}}` with `normalized_company_name`, the cover body with the drafted `gamma_cover_line`, and each video card's heading/brief with the corresponding `gamma_video_N_title`/`gamma_video_N_brief` — same substitution pattern as the standalone `gamma-deck` skill.
   d. On success, set `gamma_deck_status = success`, `gamma_deck_url = <returned URL>`. On failure, set `gamma_deck_status = failed`, `gamma_deck_url = ""`, `gamma_deck_failure_reason = <reason>`.
   e. Build the gamma result JSON with the 7 gamma text fields, the actual `gamma_deck_status`/`gamma_deck_url`/`gamma_deck_failure_reason` from step d, `_qualification_label`, and `_normalized_domain`, then validate (this also caches the result for other rows at the same company):

   ```powershell
   python "${CLAUDE_PLUGIN_ROOT}\scripts\company_qualifier.py" validate-gamma-result --output-dir "<workspace>\outputs" --result "<gamma-result.json>"
   ```
5. Merge the qualification `sheet_row`, the personalization `sheet_row`, and the gamma `sheet_row` (whether freshly produced or reused from the cache in step 2) into a single combined row object.
6. Use Composio MCP to write that combined row into the exact sheet row number given by the webhook response's `row` field — one write per row, after all applicable stages for that row are done. Do not wait for the full batch to finish before writing, and do not look up the row by matching values.

## Resuming an interrupted run

- Restart at `batchNumber=1`; n8n skips rows whose `research_status` is already filled in, same as the standalone `qualification` skill.
- Because this skill writes each row only once (after qualification and, if applicable, personalization and gamma are all done), a row interrupted mid-processing will have no `research_status` yet and will simply be re-visited and redone from scratch on resume — this is the one acceptable case where a company's site might be visited more than once.
- The cross-row domain cache lives in the same `--output-dir` and persists across resumes, so a resumed run still benefits from dedup against rows completed in an earlier session.
- Do not resume a run using different personalization/gamma specs than the ones originally approved for this output directory — that changes the wording contract for already-written rows inconsistently. Start a new output directory instead if the contract changes.

## Notes

- This skill visits each company's website exactly once **across the whole run**, regardless of whether the row ends up qualifying and regardless of how many contact rows share that company — that's the whole point of routing full-pipeline runs through it instead of chaining the three standalone skills, which would otherwise re-visit qualifying companies for personalization and gamma-deck (and, worse, call Gamma once per contact).
- It does not draft Email 1 or Email 2 copy beyond the sheet columns `personalization` and `gamma-deck` already define.
- It does not touch the n8n webhook for anything other than the row-batch contract already used by `qualification`.
