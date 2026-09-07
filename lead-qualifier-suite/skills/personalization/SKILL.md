---
name: personalization
description: Write approved, grounded custom outreach lines (Email 1 copy) for leads already qualified by the qualification skill. Reads qualified rows directly from the Google Sheet via Composio MCP — no n8n involved. Requires collaborative copy/template approval before generating any lines.
---

# Personalization

Second skill in the `lead-qualifier-suite` pipeline. Depends on the `qualification` skill having already run on this sheet — it only reads rows that already have `qualification_label` and `evidence_summary` filled in. It never re-runs qualification and never touches the n8n webhook; all row reads and all writes go through Composio MCP.

Read `references/personalization-spec.md` before designing custom fields.

## Stage 1: Approve the copy contract

1. Ask for the Google Sheet URL or ID (reuse the same sheet the qualification skill was run on).
2. Use Composio MCP to read the sheet headers and confirm the qualification columns exist (`qualification_label`, `evidence_summary`, `company_description`, `research_status`, at minimum). If they don't exist, tell the user to run the `qualification` skill first — do not proceed.
3. Collaborate to lock: outreach template, insertion points, wording pattern, sentence constraints, max length, prohibited claims, and whether fields must tie to GTM outcomes. Propose field names and one grounded example per field, show a completed example message, and wait for explicit approval.
4. Create the approved JSON spec per `references/personalization-spec.md`, then register it:

```powershell
python "${CLAUDE_PLUGIN_ROOT}\scripts\company_qualifier.py" init-personalization --output-dir "<workspace>\outputs" --spec "<approved-spec.json>"
```

`init-personalization` validates the spec against the existing run state (created by the `qualification` skill in the same `--output-dir`) and prints the full `output_columns` list including the new custom fields. Before adding any column, diff against the sheet's current headers via Composio — only create columns that are actually missing.

If `--output-dir` has no `run-state.json` yet, the qualification skill hasn't been initialized for this sheet — stop and run it first.

## Stage 2: Write custom lines

1. Read all rows from the sheet via Composio where `research_status = success`, `qualification_label` is not `skip`, and the first custom field column is blank. Process them in manageable batches (e.g. 10-20 rows at a time), in parallel within a batch.
2. **Dedup check first** — custom fields describe the *company*, not the individual contact, so rows sharing a company (same `normalized_domain`) should get identical field values instead of being redrafted per row. Before drafting, check the cross-row cache using the row's `normalized_domain` column value (already on the sheet from the `qualification` skill):

```powershell
python "${CLAUDE_PLUGIN_ROOT}\scripts\company_qualifier.py" lookup-domain --output-dir "<workspace>\outputs" --domain "<row's normalized_domain>" --stage personalization
```

   If `cached: true`, skip drafting entirely — take the returned `sheet_row`, write it to this row via Composio, and move to the next row.
3. For rows not found in the cache, use the existing `company_description` and `evidence_summary` already on the sheet as grounding — re-visit the website only if that evidence is insufficient to satisfy the approved wording contract.
4. Generate each custom field exactly per the approved wording contract. Normalize first names used in variables — leave blank if missing or unreliable. (First-name personalization, if the template uses it, lives in a separate sheet column outside this skill's custom fields — the custom fields themselves must stay company-level so they're safe to reuse across contacts.)
5. Build a result JSON containing every approved custom field plus `_qualification_label` (the value read from that row's `qualification_label` column) and `_normalized_domain` (the value read from that row's `normalized_domain` column — required so the result can be cached for other rows at the same company), then validate it:

```powershell
python "${CLAUDE_PLUGIN_ROOT}\scripts\company_qualifier.py" validate-personalization-result --output-dir "<workspace>\outputs" --result "<result.json>"
```

On success, the helper returns a `sheet_row` object with just the custom fields, and also stores it in the cross-row domain cache so later rows at the same company can reuse it via step 2. Use Composio MCP to write it into the exact sheet row number — do not wait for the full batch to finish before writing, and do not look up the row by matching values.

Within a single batch processed in parallel, do step 2 for every row *before* drafting anything, so two rows for the same new (not-yet-cached) company don't both get independently drafted — pick one to do the real work and have the other wait for that result instead of drafting twice.

## Notes

- Custom fields must remain blank for `skip` and `failed` rows — the validator enforces this from `_qualification_label`.
- Do not alter the approved custom-field contract mid-run; if the user changes the wording contract, treat it as a new spec and re-run `init-personalization` (existing values for previously-written rows are not retroactively changed).
- This skill never reads from or writes to the n8n webhook — that belongs solely to the `qualification` skill.
- This skill is independent of the `gamma-deck` skill; either can run first, both only depend on `qualification` having completed.
