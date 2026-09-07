---
name: qualification
description: Qualify companies from a Google Sheet against the GTM target profile. Reads row batches from a dedicated n8n workflow, researches each website, labels priority_now/good_fit/maybe/skip, and writes qualification data back via Composio MCP. First stage of the lead-qualifier-suite pipeline — run this before personalization or gamma-deck.
---

# Qualification

First skill in the `lead-qualifier-suite` pipeline. Produces qualification data only (no outreach copy, no Gamma decks) — those are separate skills (`personalization`, `gamma-deck`) that read this skill's output back out of the sheet.

Read `references/default-target-profile.md` for qualification logic.

## Stage 1: Inspect and initialize

1. Ask the user for their Google Sheet URL or ID.
2. Use Composio MCP to read the sheet headers. Identify the website column and optional company-name column. Use the most obvious candidate automatically; ask the user to confirm if ambiguous.
3. Initialize the run:

```powershell
python "${CLAUDE_PLUGIN_ROOT}\scripts\company_qualifier.py" init --sheet-id "<sheet-id>" --website-column "<column>" [--company-column "<column>"] --output-dir "<workspace>\outputs"
```

`init` validates inputs, saves run state, and prints the list of `output_columns` that must exist in the sheet. Before adding any column, use Composio to read the current headers and diff them against `output_columns` — only create columns that are actually missing. Never create a column that already exists under the same name.

4. Remind the user to confirm the n8n workflow's **Sheet Column Config** node is pointed at this sheet's actual website/company headers before Stage 2 begins (see "n8n dependency" below) — this skill does not configure that node itself.

## Stage 2: Research loop

Row batches come from n8n. Repeat until n8n reports no rows left:

1. Call the n8n webhook to get the next batch:

```
GET https://n8n-acx-v2-clone-u40987.vm.elestio.app/webhook/bdc80d7d-0f32-4dd5-9d77-c658660aedc9
Body (JSON): { "googleSheetUrl": "<sheet-url>", "batchNumber": <n> }
```

   Start `batchNumber` at `1` and increment by 1 on each subsequent call for this sheet. n8n internally filters out rows whose `research_status` is already filled in, then returns the next slice — resuming a run just means starting again at `batchNumber=1`.

   Example (curl):
   ```bash
   curl -s -X GET "https://n8n-acx-v2-clone-u40987.vm.elestio.app/webhook/bdc80d7d-0f32-4dd5-9d77-c658660aedc9" \
     -H "Content-Type: application/json" \
     -d '{"googleSheetUrl":"<sheet-url>","batchNumber":1}'
   ```

2. The response is `{ "rows": [ { "row": <sheet_row_number>, "website": "<value>", "company": "<value>" }, ... ] }`. An empty `rows` array means the run is complete — stop the loop.
3. Research all rows in the batch in parallel — visit every website simultaneously, then qualify each independently.

For each row in the batch:

0. **Dedup check first** — multiple rows in the sheet are often different contacts at the same company. Before visiting the site, normalize the row's raw website into a domain (strip protocol/`www.`/path — same logic as the script's `normalize_website`) and check the cross-row cache:

```powershell
python "${CLAUDE_PLUGIN_ROOT}\scripts\company_qualifier.py" lookup-domain --output-dir "<workspace>\outputs" --website "<row's raw website value>" --stage qualification
```

   If `cached: true`, skip the site visit and steps 1-3 entirely — take the returned `sheet_row`, write it to this row's sheet position via Composio, and move to the next row. This is the common case for sheets with several contacts per company.
1. Visit the normalized website (homepage first, then product/about/pricing as needed). Use only facts from the researched pages. Fall back to Exa MCP if direct access is unreliable; mark `failed` if the site still cannot be verified.
2. Choose one label per `references/default-target-profile.md`: `priority_now`, `good_fit`, `maybe`, or `skip`.
3. Write company description, qualification reason, evidence summary, and source URL.
4. Build a result JSON with `research_status`, `research_failure_reason` (if failed), `company_description`, `qualification_label`, `qualification_reason`, `evidence_summary`, `evidence_source_url`, plus `_raw_website` and `_raw_company` (the `website`/`company` values from the webhook response for this row), then validate it:

```powershell
python "${CLAUDE_PLUGIN_ROOT}\scripts\company_qualifier.py" validate-qualification-result --output-dir "<workspace>\outputs" --result "<result.json>"
```

On success, the helper returns a `sheet_row` object with all values normalized and ready, and also stores it in the cross-row domain cache under this row's `normalized_domain` (visible in the response) so later rows at the same company can reuse it via step 0. Use Composio MCP to write that `sheet_row` into the exact sheet row number given by this row's `row` field from the webhook response — do not wait for the full batch to finish before writing, and do not look up the row by matching values.

Within a single batch processed in parallel, do step 0 for every row *before* kicking off any site visits, so two rows for the same new (not-yet-cached) company don't both research it — pick one to do the real work and have the other wait for that result instead of visiting twice.

## n8n dependency

- Production webhook (always use this, not the `/webhook-test/` path): `https://n8n-acx-v2-clone-u40987.vm.elestio.app/webhook/bdc80d7d-0f32-4dd5-9d77-c658660aedc9`
- Workflow: `Website Qualifying Automation` (n8n workflow ID `k9gbLfjBrRp86rnS`).
- The workflow's **Sheet Column Config** node resolves the website/company values per row via expressions (e.g. `{{ $json.Domain }}`). Since sheet headers vary per source, this node must be manually edited in the n8n editor to match the current sheet before running Stage 2. This skill has no way to set that itself.
- n8n also owns the "already processed" skip logic (via `research_status`) and the batch-size slicing — this skill only supplies `googleSheetUrl` and an incrementing `batchNumber` and trusts n8n's response.

## Handoff to the next skills

- `personalization` and `gamma-deck` both read rows where `research_status = success` and `qualification_label != skip` directly from the sheet via Composio — no re-running of this skill is needed for them to operate.
- Do not have this skill write any outreach copy or Gamma fields — that would collide with column ownership of the other two skills.

## Notes

- The Google Sheet is the single source of truth. There is no separate CSV or XLSX output.
- Resume an interrupted run by calling the webhook again starting at `batchNumber=1` — rows with a non-empty `research_status` are skipped automatically by n8n.
- Composio MCP is used for header inspection, column creation, and all write-backs. It is never used to read row data for research — that only comes from the n8n webhook.
