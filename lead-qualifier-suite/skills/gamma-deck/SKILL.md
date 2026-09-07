---
name: gamma-deck
description: Generate a personalized 3-video-idea Gamma deck for each qualified lead, pitching the YouTube mini-course offer, and write the deck link back to the Google Sheet. Reads qualified rows directly via Composio MCP (no n8n). Requires collaborative approval of the cover-line/video-brief wording contract before generating any decks.
---

# Gamma Deck

Third skill in the `lead-qualifier-suite` pipeline. Depends on the `qualification` skill having already run on this sheet — it only reads rows that already have `qualification_label` and `research_status` filled in, to know which rows qualify and which to skip. Independent of the `personalization` skill; either can run first. All row reads and all writes go through Composio MCP; deck creation goes through the Gamma MCP.

Unlike `personalization`, this skill does **not** reuse `company_description` / `evidence_summary` from the sheet as its research source — it re-visits each qualifying lead's website itself to gather fresh detail for the video ideas (current product surface, features, services, positioning, who they serve). Those sheet columns are only used to confirm the row already qualified and to get the normalized website/domain to visit; they are not treated as sufficient evidence on their own for what goes into the deck.

Read `references/gamma-deck-spec.md` before generating any deck content.

## What this produces

For each qualifying lead, a Gamma deck built from the fixed template `2bvn38zphijx223` ("Copy of Company Presentation Template - Primer"):

- **Cover card**: `{{COMPANY NAME}}` placeholder replaced with the lead's normalized company name, plus a personalized one-line framing (`gamma_cover_line`) replacing the template's placeholder body text.
- **3 video-idea cards**, one per video: a "How To…" style title and a "What can be covered" brief. The brief is not a topic outline — it states the problem the lead's target audience faces, and how a video demonstrating the lead's own product addresses it.

This deck is meant to be linked in Email 2 of the outreach sequence (a separate step, not handled by this skill).

## Stage 1: Approve the wording contract

1. Ask for the Google Sheet URL or ID (reuse the same sheet the qualification skill was run on).
2. Use Composio MCP to read the sheet headers and confirm the qualification columns exist (`qualification_label`, `normalized_company_name`, `normalized_website`, `research_status`, at minimum). If they don't exist, tell the user to run the `qualification` skill first — do not proceed.
3. Collaborate to lock the cover-line pattern and video-brief pattern per `references/gamma-deck-spec.md`. Show one fully worked example (cover line + 3 video ideas) for a real qualifying row on the sheet, and wait for explicit approval.
4. Create the approved JSON spec, then register it:

```powershell
python "${CLAUDE_PLUGIN_ROOT}\scripts\company_qualifier.py" init-gamma --output-dir "<workspace>\outputs" --spec "<approved-spec.json>"
```

`init-gamma` validates the spec against the existing run state (created by the `qualification` skill in the same `--output-dir`) and prints the full `output_columns` list including the gamma columns (`gamma_cover_line`, `gamma_video_1_title`, `gamma_video_1_brief`, `gamma_video_2_title`, `gamma_video_2_brief`, `gamma_video_3_title`, `gamma_video_3_brief`, `gamma_deck_status`, `gamma_deck_failure_reason`, `gamma_deck_url`). Before adding any column, diff against the sheet's current headers via Composio — only create columns that are actually missing.

If `--output-dir` has no `run-state.json` yet, the qualification skill hasn't been initialized for this sheet — stop and run it first.

## Stage 2: Generate decks

1. Read all rows from the sheet via Composio where `research_status = success` and `gamma_deck_status` is blank. Process them in manageable batches (e.g. 5-10 rows at a time — Gamma generation is heavier than text generation, keep batches smaller than the personalization skill's).
2. For rows where `qualification_label = skip`: set `gamma_deck_status = skipped`, leave every other gamma field blank, and write that back — do not call Gamma for these.
3. For every other row:
   a. **Dedup check first — this is the expensive step to skip.** A deck is company-level content (cover line + video ideas about the company, not the contact), so rows sharing a company (same `normalized_domain`) must reuse one deck instead of each triggering its own paid Gamma generation. Before doing anything else, check the cross-row cache using the row's `normalized_domain` column value (already on the sheet from the `qualification` skill):

   ```powershell
   python "${CLAUDE_PLUGIN_ROOT}\scripts\company_qualifier.py" lookup-domain --output-dir "<workspace>\outputs" --domain "<row's normalized_domain>" --stage gamma
   ```

   If `cached: true`, skip the site visit and the Gamma call entirely — take the returned `sheet_row` (includes `gamma_deck_url`), write it to this row via Composio, and move to the next row. Within a single batch processed in parallel, do this check for every row *before* visiting any site, so two rows for the same new (not-yet-cached) company don't both trigger a Gamma generation — pick one to do the real work and have the other wait for that result.
   b. For rows not found in the cache, visit the row's `normalized_website` fresh (homepage first, then product/features/pricing/blog as needed) — do not skip this because the sheet already has `company_description`/`evidence_summary` from qualification; those were gathered for fit-scoring, not for video-idea material, and may be stale or too thin for this purpose. Fall back to Exa MCP if direct access is unreliable; if the site still cannot be verified, treat this row like a failure (step 3g) instead of falling back to the old qualification evidence.
   c. From that fresh research, draft the cover line and 3 video ideas (title + brief) per the approved contract. Ground every claim only in what you just found on the site — no invented features, launches, or metrics, and do not backfill gaps from `company_description`/`evidence_summary`. Titles must pass the title quality bar in `references/gamma-deck-spec.md`: grounded in a real, specific capability of the site (not generic enough to fit any competitor), broad enough that a real audience searches for the underlying problem (not so niche it only means something to existing users), and phrased with a curiosity/viral hook. Redraft any title that fails either side of that balance.
   d. Call `generate_from_template` (Gamma MCP) with `gammaId: "2bvn38zphijx223"` and a `prompt` that explicitly instructs, in this order:
      - Replace `{{COMPANY NAME}}` on the cover card with the row's `normalized_company_name`.
      - Replace the cover card's body paragraph with the drafted `gamma_cover_line`.
      - On card 2 ("Video Idea #1"): set the `How To…` heading to `gamma_video_1_title` and the "What can be covered" text to `gamma_video_1_brief`.
      - Same pattern for cards 3 and 4 with video 2 and video 3 fields.
      - Preserve the template's layout, labels, and image — only replace text content.
   e. If `generate_from_template` succeeds, take its returned deck URL and set `gamma_deck_status = success`, `gamma_deck_url = <that URL>`, `gamma_deck_failure_reason = ""`. If it fails or the deck is not accessible, set `gamma_deck_status = failed`, `gamma_deck_url = ""`, `gamma_deck_failure_reason = <what went wrong>`.
   f. Build the result JSON with all 7 gamma text fields, the actual `gamma_deck_status`/`gamma_deck_url`/`gamma_deck_failure_reason` from step e, `_qualification_label`, and `_normalized_domain` (the row's `normalized_domain` — required so the result can be cached for other rows at the same company), then validate it:

   ```powershell
   python "${CLAUDE_PLUGIN_ROOT}\scripts\company_qualifier.py" validate-gamma-result --output-dir "<workspace>\outputs" --result "<result.json>"
   ```

   On success, the helper also stores the result in the cross-row domain cache so later rows at the same company can reuse it via step 3a.
4. Use Composio MCP to write the final `sheet_row` from the validator into the exact sheet row number — do not wait for the full batch to finish before writing, and do not look up the row by matching values.

## Notes

- Do not alter the approved wording contract mid-run; if the user changes it, treat it as a new spec and re-run `init-gamma` (existing decks for previously-processed rows are not regenerated automatically).
- This skill never reads from or writes to the n8n webhook — that belongs solely to the `qualification` skill.
- This skill does not draft Email 2 copy — it only produces `gamma_deck_url` for the sheet. Referencing that link in an email is a separate step outside this skill.
- Template ID `2bvn38zphijx223` is fixed for this offer's 3-video-idea format. If the user wants a different deck structure, that requires a new approved template and template ID, not a change to this skill's prompt logic alone.
- Deck reuse is per `normalized_domain` for the lifetime of one `--output-dir`'s cache — if the wording contract changes mid-run, previously cached decks still reflect the old contract; start a new output directory to force full regeneration under a new contract.
