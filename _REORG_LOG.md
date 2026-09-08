# Reorg Log — Valence Ops Brain vault

*Permanent record of the 2026-09-07 → 2026-09-08 reorganisation. Written in Phase 5. Companion files: `_vault_audit.csv` (Phase 0 inventory), `_reorg_manifest.csv` (Phase 1 plan), `_reorg_manifest_NOTES.md` (amendments). Baseline tag: `pre-reorg`.*

## 1 · Reconciliation

| Check | Result |
|---|---|
| Files in Phase 0 audit (469 on 7 Sep + 3 PDFs added 8 Sep) | **472** |
| Of those, present at their manifest destination | **472** |
| Missing / unaccounted for | **0**  |
| Moved to `99_Review/` (never deleted) | **17** — 11 `.DS_Store`, 4 build-output PDFs, 1 stale README copy, 1 duplicate CSV export |
| Files created by the reorg itself | **11** — `.claude/skills/wrap/SKILL.md`, `04 Clients/Aesthetica Veda/Aesthetica Veda.md`, `04 Clients/Aurilueur Esthetic Clinic/Aurilueur Esthetic Clinic.md`, `04 Clients/RUA Skin and Hair Center/RUA Skin and Hair Center.md`, `04 Clients/Sapphire Skin and Aesthetics/Sapphire Skin and Aesthetics.md`, `04 Clients/SkinFit Wellness/SkinFit Wellness.md`, `05 Prospects/Batch 7 (Notion Batch 2)/Batch 7 (Notion Batch 2).md`, `_archive/_WRITE_POLICY.md`, `_reorg_manifest.csv`, `_reorg_manifest_NOTES.md`, `_vault_audit.csv` |
| Files on disk now (excl. `.git`) | **483** = 472 + 11, plus this log makes 484 |
| Attachments (non-md) byte-identical to audit checksum | **288 / 291** — the 3 that differ: `.obsidian/graph.json` and `.obsidian/workspace.json` (Obsidian's own state, rewritten by the app), and `11 Hand-Off/PROJECT-INSTRUCTIONS-paste-this.txt` (2 lines of filename references updated in the Phase 2 commit) |
| Notes whose original text is byte-identical once the injected frontmatter and `Related:` footer are stripped | **104** |
| Notes with reference substitutions (old path/filename → new), counted in lines | **77** — listed in §5 |
| Total bytes, audited set: before → after | 96,967,507 → 97,035,531 (grew by frontmatter + footers; nothing shrank) |
| Wikilinks in vault | **862** across 112 notes |
| Unresolved wikilinks | **0**  |
| Notes still with zero links in and out | **23** (was 175 of 181) — listed in §7 |

## 2 · Rules applied, and the amendments

Brief rules 1–8 applied throughout: no deletion (git mv only; `.DS_Store` moved with plain `mv` because gitignored), no body-text rewrites, link integrity in the same commit as each move, orphans flagged not moved, merge candidates flagged not merged, existing frontmatter merged not duplicated.

Amendments agreed with Tilak on 2026-09-08 (full text in `_reorg_manifest_NOTES.md`):

1. **Protected files** — `CLAUDE.md`, `MEMORY.md`, `taste-n-judgement.md`, `files/OUTBOUND_MEMORY.md`: not moved, not renamed, no frontmatter, no footer. Only path/filename substitutions on existing lines (counts in §5).
2. **`files/` kept intact**; the proposed `02 Ledgers` folder dropped.
3. **No tags, no `_tag_registry.md`.** Frontmatter reduced to `date_created`, `date_modified` (filesystem metadata only), `status` (active / reference).
4. **MOCs limited** to the five client folders and the Batch 7 cohort.
5. **18 heavily-cited notes keep their original filenames** (≥5 prose citations); alias-by-frontmatter was proposed and not applied — the graph shows them by filename.
6. **Write policy adopted** into `CLAUDE.md` § "Write policy" (draft archived at `_archive/_WRITE_POLICY.md`); `/wrap` skill added at `.claude/skills/wrap/SKILL.md`. Frozen sinks: `files/SEND_LOG.csv`, `files/REPLY_LOG.csv`, `files/LEARNINGS_LOG.md`, `_archive/`, `11 Hand-Off/`.


## 3 · Commits (oldest first)

- `1634c06` Phase 0: vault audit CSV
- `4222cc1` Phase 1: reorg manifest; write policy adopted into CLAUDE.md
- `611a7a3` Phase 2 pilot: Project-Hand-Off → 11 Hand-Off (9 files, refs updated)
- `1918a94` Phase 1 follow-up: archive the write-policy draft (git mv failed on untracked file)
- `4227608` Phase 3: Pitch-decks → 04 Clients/Sapphire (1 files)
- `5de859e` Phase 3: Audit_call_docs → 08 Collateral/Audit Call Docs (6 files)
- `599cf77` Phase 3: sales-motion → 01 Playbooks/Sales Motion (7 files)
- `1204f9d` Phase 3: root → 01 Playbooks (13 files)
- `037b643` Phase 3: root → 03 Audits and Reviews (5 files)
- `a78861a` Phase 3: root → 04 Clients (11 files)
- `ceddb71` Phase 3: root → 05 Prospects (5 files)
- `476868b` Phase 3: root → 06 Outreach Drafts (5 files)
- `10c8bec` Phase 3: root → 08 Collateral + 09 Company (10 files)
- `d75e9ea` Phase 3: Proposals & SOW → 04 Clients (12 files)
- `8327a93` Phase 3: Resources → 04 Clients / 08 Collateral (47 files)
- `aec62b0` Phase 3: One-page-docs → 07 One-Pagers (93 files)
- `798ea13` Phase 3: Pre-outbound-research/batch7 → 05 Prospects/Batch 7 (32 files)
- `eda7c3a` Phase 3: Pre-outbound-research → 05 Prospects (rest) (11 files)
- `623abc1` Phase 3: Research-docs → 05 Prospects/Batch 3 Remainder (12 files)
- `9305979` Phase 3: clinics → 05 Prospects/Scrape 2026-07-19 (15 files)
- `373b1cd` Phase 3: se-bangalore-scrape → 05 Prospects/SE Bangalore Scrape (14 files)
- `6c7500a` Phase 3: new_leads_1 → 05 Prospects/New Leads 1 Batch 9 (58 files)
- `2c86f1b` Phase 3: verify-2026-08-18 → 05 Prospects/Verify 2026-08-18 (12 files)
- `ec03d6e` Phase 3: Mystery_Shop_2026-08-15 → 05 Prospects/Mystery Shop 2026-08-15 (14 files)
- `366634b` Phase 3: lead-qualifier-suite → 10 Tooling (17 files)
- `fb519e8` Phase 3: one-pager-handoff → 10 Tooling (26 files)
- `424dca6` Phase 3 fix-up: folder-prefixed references resolved to new paths
- `9cdd885` Phase 4: wikilinks from concrete references + 6 maps of content


## 4 · Duplicates

**Consolidated to `99_Review/` (byte-identical by sha256, canonical copy kept in place):**

- `Resources/_source/aurilueur-proposal/out.pdf` → `99_Review/Resources/_source/aurilueur-proposal/out.pdf` — byte-identical to 'Proposals & SOW/Aurilueur Esthetic Clinic - Enquiry and Appointment Systems Proposal.pdf' which is the shipped/canonical copy; this one is the headless-Chrome build artefact named in the kit README
- `Resources/_source/rua-proposal/rua-out.pdf` → `99_Review/Resources/_source/rua-proposal/rua-out.pdf` — byte-identical to 'Proposals & SOW/RUA Skin & Hair Center - Patient Communications Proposal.pdf' which is the shipped/canonical copy; this one is the headless-Chrome build artefact named in the kit README
- `Resources/_source/rua-sow/rua-sow-out.pdf` → `99_Review/Resources/_source/rua-sow/rua-sow-out.pdf` — byte-identical to 'Proposals & SOW/RUA Skin & Hair Center - Scope of Work.pdf' which is the shipped/canonical copy; this one is the headless-Chrome build artefact named in the kit README
- `Resources/_source/skinfit-proposal-v2/README.md` → `99_Review/Resources/_source/skinfit-proposal-v2/README.md` — byte-identical to 'Resources/_source/skinfit-proposal/README.md' which is the shipped/canonical copy; v2 kit's README still names the v1 output path (Phase 0 note), so it is the stale copy
- `Resources/_source/skinfit-proposal-v2/out.pdf` → `99_Review/Resources/_source/skinfit-proposal-v2/out.pdf` — byte-identical to 'Proposals & SOW/SkinFit Wellness - Patient Communications Proposal v2.pdf' which is the shipped/canonical copy; this one is the headless-Chrome build artefact named in the kit README
- `new_leads_1/Clinic_Directory_Template csv 3b771d3ba7f680e0b00acf18a11921d5_all.csv` → `99_Review/new_leads_1/Clinic_Directory_Template csv 3b771d3ba7f680e0b00acf18a11921d5_all.csv` — byte-identical to 'new_leads_1/Clinic_Directory_Template csv 3b771d3ba7f680e0b00acf18a11921d5.csv' which is the shipped/canonical copy
- 11 × `.DS_Store` → `99_Review/<original path>`

**Byte-identical but deliberately kept in place (kit integrity):**

- 55 files: the 7 example one-pager sets (html/jpg/pdf) inside `10 Tooling/one-pager-handoff/examples/`, the kit's copies of `wedge-signal-entry.md` and `diagnostic_doc_playbook.md`, and Poppins fonts + `style.css` in the four proposal build kits. Reason: the handoff kit is documented as self-contained and the proposal kits resolve fonts by relative path.

## 5 · Reference substitutions (path or filename only, no other prose)

| Note | Lines with a substituted path/name |
|---|---|
| `01 Playbooks/Sales Motion/SALES_MOTION.md` | 16 |
| `05 Prospects/New Leads 1 Batch 9/Session Handoff 2026-08-15.md` | 13 |
| `COHORT-INDEX.md` | 12 |
| `05 Prospects/Batch 7 (Notion Batch 2)/Batch 7 Master All Clinics.md` | 11 |
| `CLAUDE.md` | 10 |
| `MEMORY.md` | 10 |
| `04 Clients/SkinFit Wellness/SkinFit Proposal and SOW Review 2026-08-22.md` | 9 |
| `04 Clients/SkinFit Wellness/SkinFit Tech Handoff 2026-08-18.md` | 9 |
| `01 Playbooks/Dental Discovery/Dental Discovery Step 1 Qualify.md` | 8 |
| `11 Hand-Off/00 Start Here.md` | 8 |
| `files/OUTBOUND_MEMORY.md` | 8 |
| `01 Playbooks/Dental Discovery/Dental Discovery Criteria.md` | 7 |
| `11 Hand-Off/Setup.md` | 7 |
| `01 Playbooks/Sales Motion/03 Operations Call.md` | 6 |
| `01 Playbooks/Dental Discovery/Dental Discovery Step 2 Research.md` | 5 |
| `03 Audits and Reviews/Outbound Process Changes 2026-08-11.md` | 5 |
| `03 Audits and Reviews/Session 2026-08-10 SE Bangalore Scrape.md` | 5 |
| `05 Prospects/New Leads 1 Batch 9/Ads Presence 2026-08-15.md` | 5 |
| `01 Playbooks/Process Map.md` | 4 |
| `03 Audits and Reviews/One-Pager Steelman 2026-08-14.md` | 4 |
| `04 Clients/Aurilueur Esthetic Clinic/Aurilueur Revenue Research 2026-09-05.md` | 4 |
| `01 Playbooks/Research Prompts/Prompt Research Clinics 11-15.md` | 3 |
| `01 Playbooks/Sales Motion/05 Pilot and Onboarding.md` | 3 |
| `05 Prospects/Batch 7 (Notion Batch 2)/Batch 7 Consolidated State.md` | 3 |
| `05 Prospects/New Leads 1 Batch 9/Day 0 DMs 2026-08-23.md` | 3 |
| `05 Prospects/New Leads 1 Batch 9/Flag Resolutions 2026-08-15.md` | 3 |
| `05 Prospects/New Leads 1 Batch 9/Wedge Angles Batch 9 2026-08-19.md` | 3 |
| `05 Prospects/SE Bangalore Scrape/Shortlist 2026-08-14.md` | 3 |
| `09 Company/Legal and Commercial Doc Set.md` | 3 |
| `01 Playbooks/Lead Prioritization Method.md` | 2 |
| `01 Playbooks/LinkedIn Sales Navigator Personas.md` | 2 |
| `01 Playbooks/Sales Motion/04 Findings and Rollout.md` | 2 |
| `01 Playbooks/diagnostic_doc_playbook.md` | 2 |
| `03 Audits and Reviews/ONE-PAGER-AUDIT-AND-TEST-PLAN.md` | 2 |
| `04 Clients/SkinFit Wellness/SkinFit Information Request Review.md` | 2 |
| `05 Prospects/Batch 3 Aesthetic and Dental/batch3-aesthetic-MASTER.md` | 2 |
| `05 Prospects/Batch 7 (Notion Batch 2)/Batch 7 Wedge Brief.md` | 2 |
| `05 Prospects/New Leads 1 Batch 9/Clinic Check Table 2026-08-15.md` | 2 |
| `05 Prospects/New Leads 1 Batch 9/Open Checks 2026-08-15.md` | 2 |
| `05 Prospects/New Leads 1 Batch 9/Shop Queue 01-10 2026-08-15.md` | 2 |
| `05 Prospects/SE Bangalore Scrape/Ads Presence 2026-08-14.md` | 2 |
| `05 Prospects/SE Bangalore Scrape/Qualified Targets 2026-08-14.md` | 2 |
| `08 Collateral/Audit Call Docs/02_data_intake_requirements.md` | 2 |
| `09 Company/Paperwork Handbook 2026-09-06.md` | 2 |
| `09 Company/Pricing and Build Cost 2026-08-21.md` | 2 |
| `10 Tooling/one-pager-handoff/COPY_STANDARD.md` | 2 |
| `10 Tooling/one-pager-handoff/diagnostic_doc_playbook.md` | 2 |
| `.claude/skills/clinic-audit-research/SKILL.md` | 1 |
| `01 Playbooks/Sales Motion/02 Credibility Packet.md` | 1 |
| `03 Audits and Reviews/Event Snapshot 2026-09-02.md` | 1 |
| `04 Clients/Aurilueur Esthetic Clinic/Aurilueur Bangalore Price Benchmarks 2026-09-05.md` | 1 |
| `04 Clients/Aurilueur Esthetic Clinic/Source/aurilueur-proposal/README.md` | 1 |
| `04 Clients/Sapphire Skin and Aesthetics/Meeting Brief Sapphire 2026-08-13.md` | 1 |
| `04 Clients/SkinFit Wellness/Meeting Brief SkinFit 2026-08-18.md` | 1 |
| `04 Clients/SkinFit Wellness/Runsheet SkinFit Gino 2026-08-18.md` | 1 |
| `05 Prospects/Batch 3 Aesthetic and Dental/Handoff Batch 3 Remaining 8.md` | 1 |
| `05 Prospects/Batch 7 (Notion Batch 2)/Batch 11-15 Summary.md` | 1 |
| `05 Prospects/Batch 7 (Notion Batch 2)/Findings Batch 11-15.md` | 1 |
| `05 Prospects/Batch 7 (Notion Batch 2)/Findings Batch 7 Clinics 11-20.md` | 1 |
| `05 Prospects/New Leads 1 Batch 9/Contact List Batch 9 2026-08-19.md` | 1 |
| `05 Prospects/New Leads 1 Batch 9/Day 0 DMs 2026-08-20.md` | 1 |
| `05 Prospects/New Leads 1 Batch 9/Shop 9 Wedge Review 2026-08-19.md` | 1 |
| `05 Prospects/New Leads 1 Batch 9/Shop Queue 11-20 2026-08-15.md` | 1 |
| `05 Prospects/New Leads 1 Batch 9/Shop Queue 2026-08-15.md` | 1 |
| `05 Prospects/New Leads 1 Batch 9/Shop Queue Remainder 2026-08-15.md` | 1 |
| `05 Prospects/Verify 2026-08-18/Enquiry Flow Shortlist 2026-08-19.md` | 1 |
| `05 Prospects/Verify 2026-08-18/Qualified Leads 2026-08-19.md` | 1 |
| `05 Prospects/Verify 2026-08-18/Resume Note 2026-08-18.md` | 1 |
| `06 Outreach Drafts/Cold Emails Utkarsha Keshav Karishma Dixit Juvita.md` | 1 |
| `10 Tooling/one-pager-handoff/CLAUDE.md` | 1 |
| `11 Hand-Off/01 State of Play.md` | 1 |
| `11 Hand-Off/05 Clinic Inventory.md` | 1 |
| `files/OUTBOUND_SYSTEM_AUDIT.md` | 1 |
| `05 Prospects/Batch 1 Notion Cohort/Outreach 3.md` | 0 |
| `05 Prospects/Batch 1 Notion Cohort/Outreach 4.md` | 0 |
| `05 Prospects/Batch 1 Notion Cohort/Outreach 5.md` | 0 |
| `_archive/README.md` | 0 |

The first pass missed references of the form `old-folder/filename`; commit `424dca6` resolved those against the manifest. `_archive/` was never edited, so it still cites pre-reorg paths by design.


## 6 · Merge candidates — left for Tilak, nothing merged

| A | B | Overlapping section | Note |
|---|---|---|---|
| `05 Prospects/Batch 1 Notion Cohort/Outreach 1.md` | `_archive/Valence-Research-Intelligence/OUTREACH document.md` | Every clinic's '### ICP Qualification' section (Aura Cutisurg etc.) | Same dossier set; Pre-outbound copy (mod 2026-08-13) adds 11 '(ICP/prestige scoring was RETIRED 2026-07-22)' annotations; _archive copy (mod |
| `05 Prospects/Batch 1 Notion Cohort/Outreach 2.md` | `_archive/Valence-Research-Intelligence/outreach -2.md` | '# ICP Qualification' section of Dr. Swetha's Cosmoderm Centre dossier and 8 others | Same pattern as above: 9 RETIRED annotations only in the Pre-outbound copy |
| `.claude/skills/clinic-audit-research/SKILL.md` | `_archive/clinic-apify-research-skill.md` | '## Phase 0 — Intake, depth mode, preflight, pre-screen' and 'What this skill is for' | SKILL.md (2026-08-13) adds the '> Sequencing changed 2026-08-13' block; _archive copy (2026-07-30) is the prior version (29 diff lines) |
| `_archive/personalized-outbound-skill.md` | `01 Playbooks/personalized-outbound-v2.md` | '## The Sequence — Three Threads' → '### 5 · The meet ask' and '### 6 · The silence bumps' (v1: 'call/offline meet ask', | v2 adds 'Revised 2026-08-13' block (rev-share struck, 2-touch cap). Shared verbatim: Offer Engineering Lens, Risk Reversal Standard, Languag |
| `05 Prospects/Batch 7 (Notion Batch 2)/Batch 7 Follow-up 2 Messages.md` | `05 Prospects/Batch 7 (Notion Batch 2)/Batch 7 Master All Clinics.md` | The 12 per-clinic Follow-up 2 message bodies (## 1 · Akera Health … ## 12) are embedded inside the MASTER's per-clinic r | 84% of FOLLOWUP2 text is contained in MASTER; MASTER is the declared precedence file |
| `04 Clients/Aurilueur Esthetic Clinic/Source/aurilueur-proposal/README.md` | `04 Clients/SkinFit Wellness/Source/skinfit-proposal/README.md` | Whole file: 'build kit' rebuild instructions (Chrome headless command, Poppins/palette design system) | Only title line and output PDF path differ. Note: skinfit-proposal-v2/README.md still names the v1 output path |
| `11 Hand-Off/04 Wedge Routing.md` | `01 Playbooks/wedge-signal-entry.md` | '### 2.3 Save the screenshot, not the summary', '### 2.4 Verdict', 'Hard kills — disqualify immediately', 'Signal → wedg | 04-WEDGE-ROUTING is a condensed hand-off rewrite of wedge-signal-entry (which carries a Change log and §4 schema tagging that 04 lacks) |
| `05 Prospects/Batch 7 (Notion Batch 2)/Batch 7 Consolidated State.md` | `11 Hand-Off/05 Clinic Inventory.md` | '## 1. Send + shop state, all 12' ↔ 'PART A · Batch 2 — the live cohort (12 clinics)'; the five confirmed wedges (Dr. Pr | Same 12-clinic Batch 7/'Batch 2' roster snapshot, 2026-08-13/14, different framing |
| `05 Prospects/Verify 2026-08-18/Final Table.md` | `05 Prospects/Verify 2026-08-18/Qualified Leads 2026-08-19.md` | Clinic table (IG followers / Google reviews / Meta ads / Google ads) rows e.g. dr_shettys_cosmetic_centre, Hairline Inte | QUALIFIED-LEADS re-sorts the table into Qualified / Borderline / Held back sections |
| `01 Playbooks/Sales Motion/SALES_MOTION.md` | `01 Playbooks/Sales Motion/01 Reply to Call.md` | SALES_MOTION '## 2 · The motion — five stages' + '## 3 · Stage detail' ↔ the five per-stage files (01 Reply→Call, 02 Cre | Heading-level overlap (not caught by shingles — prose differs). Summary vs expanded stage docs |
| `03 Audits and Reviews/ONE-PAGER-AUDIT-AND-TEST-PLAN.md` | `03 Audits and Reviews/One-Pager Steelman 2026-08-14.md` | Audit '## 5 · The three arms' ↔ Steelman '## 4 · The test design — and why the Aug-5 three-arm plan can't run'; Steelman | Steelman explicitly supersedes/responds to the Aug-5 audit; sequential reviews of the same one-pager set |
| `05 Prospects/Batch 7 (Notion Batch 2)/Findings Batch 11-15.md` | `05 Prospects/Batch 7 (Notion Batch 2)/Findings Batch 7 Clinics 11-20.md` | '## 1. Master table' — clinics #11–15 appear in both; '## 4/6 Provisional wedges' for the same clinics | 11–15 is a subset range of 11–20 for Batch 7; also both carry 'Corrections to' sections aimed at go-list-mystery-shop.md / wedge-signal-entr |
| `01 Playbooks/clinic-audit-checklist.md` | `01 Playbooks/wedge-signal-entry.md` | checklist '## 4 · Booking-Flow Mystery Shop' ↔ wedge-signal-entry '## 2. Speed-to-lead audit SOP' | Both define the mystery-shop procedure; wedge-signal-entry is the declared canonical rulebook |
| `11 Hand-Off/03 Drafting Engine.md` | `01 Playbooks/personalized-outbound-v2.md` | 03 '## 4 · The sequence — 4 touches, 2 channels' ↔ v2 '## The Sequence — Three Threads' / '### 6 · The silence bumps — t | Hand-off condensation of the outbound skill |
| `01 Playbooks/Dental Discovery/Dental Discovery Criteria.md` | `01 Playbooks/Dental Discovery/Dental Discovery Step 1 Qualify.md` | CRITERIA '## 2. Qualification gates' ↔ STEP-1 '1A · Discovery + hard kills' … '1D · Demand gate' | CRITERIA defines the gates, STEP-1 operationalises them with budgets; intended pair, not a merge |
| `04 Clients/SkinFit Wellness/Source/skinfit-proposal/proposal.html` | `04 Clients/SkinFit Wellness/Source/skinfit-proposal-v2/proposal.html` | Same 7 sections (Where this picks up … What the system runs on); 20 changed text lines | v1 → v2 of the same SkinFit proposal; v1 PDF 'SkinFit Wellness - Patient Communications Proposal.pdf' and v2 PDF both live in Proposals & SO |
| `04 Clients/SkinFit Wellness/SkinFit Wellness - Patient Conversion System.pdf` | `04 Clients/SkinFit Wellness/SkinFit Wellness - Patient Conversion and Intelligence System.pdf` | Three SkinFit 'Patient Conversion' PDFs generated 2026-08-30 within 54 minutes; no HTML source in vault for any of them | Binary — not text-compared. Flag only: which is the sent version is unknowable from the files |
| `_archive/one-pager-handoff.zip` | `one-pager-handoff/ (folder)` | ZIP (3.2 MB, 2026-08-04) presumably packages an earlier one-pager-handoff/ tree | Not extracted/compared; binary archive. Flag for human decision |
| `04 Clients/SkinFit Wellness/SkinFit Wellness - Patient Conversion *.pdf` (×3) | same-named `.html` sources in the same folder | Three PDFs generated 2026-08-30 within 54 min | Which one was sent is unknowable from files. **Correction to Phase 0:** the HTML sources do exist; they were in `Resources/`. |

## 7 · Orphans remaining (flagged, not moved)

- `.claude/skills/clinic-audit-research/SKILL.md`
- `.claude/skills/wrap/SKILL.md`
- `01 Playbooks/Research Prompts/Apify Discovery Prompt.md`
- `05 Prospects/Batch 3 Remainder/09 Sparha Aesthetic Studio.md`
- `05 Prospects/Scrape 2026-07-19/Amintri Skin Hair Clinic.md`
- `06 Outreach Drafts/Cold Emails Utkarsha Keshav Karishma Dixit Juvita.md`
- `06 Outreach Drafts/Outreach Drafts Vtiara.md`
- `08 Collateral/Audit Call Docs/01 Shadow Audit Checklist.md`
- `10 Tooling/lead-qualifier-suite/skills/gamma-deck/SKILL.md`
- `10 Tooling/lead-qualifier-suite/skills/gamma-deck/references/gamma-deck-spec.md`
- `10 Tooling/lead-qualifier-suite/skills/orchestrator/SKILL.md`
- `10 Tooling/lead-qualifier-suite/skills/personalization/SKILL.md`
- `10 Tooling/lead-qualifier-suite/skills/personalization/references/personalization-spec.md`
- `10 Tooling/lead-qualifier-suite/skills/qualification/SKILL.md`
- `10 Tooling/lead-qualifier-suite/skills/qualification/references/default-target-profile.md`
- `10 Tooling/one-pager-handoff/BUILD_GUIDE.md`
- `10 Tooling/one-pager-handoff/CLAUDE.md`
- `10 Tooling/one-pager-handoff/diagnostic_doc_playbook.md`
- `11 Hand-Off/03 Drafting Engine.md`
- `11 Hand-Off/04 Wedge Routing.md`
- `11 Hand-Off/06 Decisions and Learnings.md`
- `11 Hand-Off/Setup.md`
- `_reorg_manifest_NOTES.md`

Sixteen of these are tooling, skill and hand-off files that were excluded as link *sources* on purpose; the rest are notes nothing else names. No thematic links were invented for them.


## 8 · Tags created

None. The tag registry was dropped by amendment 3.


## 9 · Maps of content created

- `04 Clients/SkinFit Wellness/SkinFit Wellness.md` — navigation only, no facts
- `04 Clients/Aurilueur Esthetic Clinic/Aurilueur Esthetic Clinic.md` — navigation only, no facts
- `04 Clients/RUA Skin and Hair Center/RUA Skin and Hair Center.md` — navigation only, no facts
- `04 Clients/Sapphire Skin and Aesthetics/Sapphire Skin and Aesthetics.md` — navigation only, no facts
- `04 Clients/Aesthetica Veda/Aesthetica Veda.md` — navigation only, no facts
- `05 Prospects/Batch 7 (Notion Batch 2)/Batch 7 (Notion Batch 2).md` — navigation only, no facts

## 10 · Links added — per source note, with the reason for each

Signals accepted as concrete: **cited by name** (the note names the target file), **client name** (one of the five clients), **clinic name** (a clinic that has a dossier; full name match only), **cohort member** (a Batch 7 note links to its MOC). No thematic guesses.

- `01 Playbooks/Clinic Research Sources.md` → personalized-outbound-v2 (cited by name); wedge-signal-entry (cited by name)
- `01 Playbooks/Dental Discovery/Dental Discovery Criteria.md` → Apify Discovery Context (cited by name); CLAUDE (cited by name); clinic-audit-checklist (cited by name); wedge-signal-entry (cited by name); personalized-outbound-v2 (cited by name); MEMORY (cited by name); Batch 3 Dental Audit (cited by name); OUTBOUND_MEMORY (cited by name); Sapphire Skin and Aesthetics (client name)
- `01 Playbooks/Dental Discovery/Dental Discovery Step 1 Qualify.md` → Dental Discovery Criteria (cited by name); Apify Discovery Context (cited by name); CLAUDE (cited by name); personalized-outbound-v2 (cited by name); MEMORY (cited by name); Batch 3 Dental Audit (cited by name); Sapphire Skin and Aesthetics (client name)
- `01 Playbooks/Dental Discovery/Dental Discovery Step 2 Research.md` → Batch 3 Dental Audit (cited by name); wedge-signal-entry (cited by name); Dental Discovery Criteria (cited by name); MEMORY (cited by name); OUTBOUND_MEMORY (cited by name)
- `01 Playbooks/Lead Prioritization Method.md` → wedge-signal-entry (cited by name); OUTBOUND_SYSTEM_AUDIT (cited by name); MEMORY (cited by name); OUTBOUND_MEMORY (cited by name); Outreach 3 (cited by name); CLAUDE (cited by name); Sapphire Skin and Aesthetics (client name)
- `01 Playbooks/LinkedIn Sales Navigator Personas.md` → personalized-outbound-v2 (cited by name); wedge-signal-entry (cited by name); MEMORY (cited by name); Aesthetica Veda (client name); 12 Haircosmos International (clinic name); 11 Gejje's Marvella (clinic name); 20 VIDA Skin and Hair Transplant (clinic name); 06 Contour Cosmetic Clinic (clinic name); 03 Koza Aesthetic Care (clinic name)
- `01 Playbooks/Process Map.md` → wedge-signal-entry (cited by name); OUTBOUND_MEMORY (cited by name); Apify Discovery Context (cited by name); Dental Discovery Criteria (cited by name); MEMORY (cited by name); IG Pregate 40 Clinics (cited by name); go-list-mystery-shop (cited by name); personalized-outbound-v2 (cited by name); diagnostic_doc_playbook (cited by name); ONE-PAGER-AUDIT-AND-TEST-PLAN (cited by name); SALES_MOTION (cited by name); LEARNINGS_LOG (cited by name); Sapphire Skin and Aesthetics (client name); Aesthetica Veda (client name)
- `01 Playbooks/Research Prompts/Apify Discovery Context.md` → SkinFit Wellness (client name); RUA Skin and Hair Center (client name); Sapphire Skin and Aesthetics (client name); Aesthetica Veda (client name); 12 Haircosmos International (clinic name); 05 SS Aesthetic Clinic (clinic name); 01 RUA Skin and Hair Center (clinic name); 07 Sanssouci Wellness Clinic (clinic name); 08 SkinFit Wellness (clinic name); 06 Contour Cosmetic Clinic (clinic name); 02 Skin and Recon (clinic name); 03 Koza Aesthetic Care (clinic name); 10 Feather Touch Aesthetic Clinic (clinic name); Clinique Hair Transplant Centre (clinic name); Evenly Skin and Hair Clinic (clinic name); Mister Hair Clinic (clinic name); Smile World Dental Clinic (clinic name); Vrudhii Aesthetics (clinic name); Dermaqure (clinic name); The Derma Theory (clinic name); Nikhilesh Dental Clinic (clinic name); Tooth and Root Dental Clinic (clinic name); Looks Hair and Skin Clinic (clinic name); Beeyens Skin and Laser Clinic (clinic name)
- `01 Playbooks/Research Prompts/Prompt Research Clinics 11-15.md` → CLAUDE (cited by name); MEMORY (cited by name); wedge-signal-entry (cited by name); Outreach 1 (cited by name); go-list-mystery-shop (cited by name); Batch 11-15 Summary (cited by name); 22 Krity 360 (clinic name); 21 Vitals Klinic (clinic name); 25 Project Skin (clinic name)
- `01 Playbooks/Sales Motion/01 Reply to Call.md` → OUTBOUND_MEMORY (cited by name); MEMORY (cited by name)
- `01 Playbooks/Sales Motion/02 Credibility Packet.md` → OUTBOUND_MEMORY (cited by name); HOW-WE-WORK (cited by name); diagnostic_doc_playbook (cited by name); MEMORY (cited by name)
- `01 Playbooks/Sales Motion/03 Operations Call.md` → 03 Discovery Call Question Map (cited by name); wedge-signal-entry (cited by name); 02_data_intake_requirements (cited by name)
- `01 Playbooks/Sales Motion/04 Findings and Rollout.md` → diagnostic_doc_playbook (cited by name); MEMORY (cited by name); OUTBOUND_MEMORY (cited by name)
- `01 Playbooks/Sales Motion/05 Pilot and Onboarding.md` → OUTBOUND_MEMORY (cited by name); 02_data_intake_requirements (cited by name); LEARNINGS_LOG (cited by name)
- `01 Playbooks/Sales Motion/HOW-WE-WORK.md` → diagnostic_doc_playbook (cited by name); OUTBOUND_MEMORY (cited by name)
- `01 Playbooks/Sales Motion/SALES_MOTION.md` → personalized-outbound-v2 (cited by name); OUTBOUND_MEMORY (cited by name); wedge-signal-entry (cited by name); 01 Reply to Call (cited by name); 02 Credibility Packet (cited by name); 03 Operations Call (cited by name); 04 Findings and Rollout (cited by name); 05 Pilot and Onboarding (cited by name); HOW-WE-WORK (cited by name); diagnostic_doc_playbook (cited by name); 02_data_intake_requirements (cited by name)
- `01 Playbooks/clinic-audit-checklist.md` → personalized-outbound-v2 (cited by name); wedge-signal-entry (cited by name); OUTBOUND_SYSTEM_AUDIT (cited by name)
- `01 Playbooks/diagnostic_doc_playbook.md` → CLAUDE (cited by name); COPY_STANDARD (cited by name); OUTBOUND_MEMORY (cited by name)
- `01 Playbooks/personalized-outbound-v2.md` → OUTBOUND_MEMORY (cited by name); MEMORY (cited by name); wedge-signal-entry (cited by name)
- `01 Playbooks/wedge-signal-entry.md` → OUTBOUND_MEMORY (cited by name); MEMORY (cited by name); Sapphire Skin and Aesthetics (client name); Aesthetica Veda (client name); 19 Dermatonik (clinic name); 25 Project Skin (clinic name)
- `03 Audits and Reviews/Event Snapshot 2026-09-02.md` → taste-n-judgement (cited by name); personalized-outbound-v2 (cited by name); wedge-signal-entry (cited by name); OUTBOUND_MEMORY (cited by name); OUTBOUND_SYSTEM_AUDIT (cited by name); CLAUDE (cited by name); SkinFit Wellness (client name); Aurilueur Esthetic Clinic (client name); RUA Skin and Hair Center (client name); Sapphire Skin and Aesthetics (client name); Aesthetica Veda (client name); 13 Ara Skin Clinic (clinic name); 16 Derma Solutions (clinic name); 19 Dermatonik (clinic name); 22 Krity 360 (clinic name); 21 Vitals Klinic (clinic name); 14 Dr. Priya's Skin and Hair Clinic (clinic name); 18 Theory of Skin (clinic name); 12 Haircosmos International (clinic name); 11 Gejje's Marvella (clinic name); 20 VIDA Skin and Hair Transplant (clinic name); 25 Project Skin (clinic name); 15 Akera Health (clinic name); 01 RUA Skin and Hair Center (clinic name); The Derma Theory (clinic name)
- `03 Audits and Reviews/ONE-PAGER-AUDIT-AND-TEST-PLAN.md` → CLAUDE (cited by name); OUTBOUND_MEMORY (cited by name); diagnostic_doc_playbook (cited by name); MEMORY (cited by name); SALES_MOTION (cited by name); LEARNINGS_LOG (cited by name); Sapphire Skin and Aesthetics (client name); Aesthetica Veda (client name)
- `03 Audits and Reviews/One-Pager Steelman 2026-08-14.md` → ONE-PAGER-AUDIT-AND-TEST-PLAN (cited by name); diagnostic_doc_playbook (cited by name); COPY_STANDARD (cited by name); MEMORY (cited by name); CLAUDE (cited by name); OUTBOUND_MEMORY (cited by name); SALES_MOTION (cited by name); wedge-signal-entry (cited by name); Sapphire Skin and Aesthetics (client name); Aesthetica Veda (client name)
- `03 Audits and Reviews/Outbound Process Changes 2026-08-11.md` → wedge-signal-entry (cited by name); OUTBOUND_MEMORY (cited by name); COHORT-INDEX (cited by name); Process Map (cited by name); MEMORY (cited by name); OUTBOUND_SYSTEM_AUDIT (cited by name); ONE-PAGER-AUDIT-AND-TEST-PLAN (cited by name); SALES_MOTION (cited by name); Findings Batch 11-15 (cited by name); LEARNINGS_LOG (cited by name); Sapphire Skin and Aesthetics (client name); Aesthetica Veda (client name); 16 Derma Solutions (clinic name); 19 Dermatonik (clinic name); 25 Project Skin (clinic name)
- `03 Audits and Reviews/Session 2026-08-10 SE Bangalore Scrape.md` → New Clinics Table 2026-08-10 (cited by name); MEMORY (cited by name); CLAUDE (cited by name); SkinFit Wellness (client name); RUA Skin and Hair Center (client name); Sapphire Skin and Aesthetics (client name); Aesthetica Veda (client name); 13 Ara Skin Clinic (clinic name); 16 Derma Solutions (clinic name); 19 Dermatonik (clinic name); 22 Krity 360 (clinic name); 21 Vitals Klinic (clinic name); 14 Dr. Priya's Skin and Hair Clinic (clinic name); 18 Theory of Skin (clinic name); 12 Haircosmos International (clinic name); 11 Gejje's Marvella (clinic name); 20 VIDA Skin and Hair Transplant (clinic name); 25 Project Skin (clinic name); 15 Akera Health (clinic name); 05 SS Aesthetic Clinic (clinic name); 01 RUA Skin and Hair Center (clinic name); 07 Sanssouci Wellness Clinic (clinic name); 08 SkinFit Wellness (clinic name); 06 Contour Cosmetic Clinic (clinic name); 02 Skin and Recon (clinic name); 03 Koza Aesthetic Care (clinic name); 10 Feather Touch Aesthetic Clinic (clinic name); Evenly Skin and Hair Clinic (clinic name)
- `04 Clients/Aurilueur Esthetic Clinic/Aurilueur Bangalore Price Benchmarks 2026-09-05.md` → Aurilueur Revenue Research 2026-09-05 (cited by name); Sapphire Skin and Aesthetics (client name); 16 Derma Solutions (clinic name)
- `04 Clients/Aurilueur Esthetic Clinic/Aurilueur Revenue Research 2026-09-05.md` → CLAUDE (cited by name); wedge-signal-entry (cited by name); SkinFit Information Request Review (cited by name); taste-n-judgement (cited by name); Aurilueur Bangalore Price Benchmarks 2026-09-05 (cited by name); SkinFit Wellness (client name); 16 Derma Solutions (clinic name)
- `04 Clients/Aurilueur Esthetic Clinic/Runsheet Aurilueur 2026-08-21.md` → SALES_MOTION (cited by name)
- `04 Clients/Aurilueur Esthetic Clinic/Source/aurilueur-proposal/README.md` → Aurilueur Esthetic Clinic - Enquiry and Appointment Systems Proposal.pdf (cited by name); SkinFit Wellness (client name)
- `04 Clients/RUA Skin and Hair Center/RUA Skin and Hair Call Dossier 2026-08-25.md` → wedge-signal-entry (cited by name); batch3-aesthetic-MASTER (cited by name); SALES_MOTION (cited by name); 01 RUA Skin and Hair Center (clinic name)
- `04 Clients/Sapphire Skin and Aesthetics/Meeting Brief Sapphire 2026-08-13.md` → Outreach 3 (cited by name); ONE-PAGER-AUDIT-AND-TEST-PLAN (cited by name); SALES_MOTION (cited by name); 03 Operations Call (cited by name); Outbound Process Changes 2026-08-11 (cited by name); wedge-signal-entry (cited by name)
- `04 Clients/SkinFit Wellness/Meeting Brief SkinFit 2026-08-18.md` → SkinFit Wellness - Revenue Diagnostic.pdf (cited by name); SALES_MOTION (cited by name); OUTBOUND_MEMORY (cited by name); Sapphire Skin and Aesthetics (client name); 16 Derma Solutions (clinic name); 22 Krity 360 (clinic name); 18 Theory of Skin (clinic name); 08 SkinFit Wellness (clinic name)
- `04 Clients/SkinFit Wellness/Runsheet SkinFit Gino 2026-08-18.md` → Meeting Brief SkinFit 2026-08-18 (cited by name); MEMORY (cited by name); Sapphire Skin and Aesthetics (client name); 08 SkinFit Wellness (clinic name)
- `04 Clients/SkinFit Wellness/SkinFit Information Request Review.md` → SkinFit Tech Handoff 2026-08-18 (cited by name); SALES_MOTION (cited by name); CLAUDE (cited by name); diagnostic_doc_playbook (cited by name); Legal and Commercial Doc Set (cited by name); OUTBOUND_MEMORY (cited by name); Sapphire Skin and Aesthetics (client name)
- `04 Clients/SkinFit Wellness/SkinFit Proposal and SOW Review 2026-08-22.md` → SkinFit Wellness - Enquiry Handling Review.pdf (cited by name); SkinFit Tech Handoff 2026-08-18 (cited by name); Pricing and Build Cost 2026-08-21 (cited by name); Legal and Commercial Doc Set (cited by name); taste-n-judgement (cited by name); SkinFit Information Request Review (cited by name); SALES_MOTION (cited by name); Sapphire Skin and Aesthetics (client name); 08 SkinFit Wellness (clinic name)
- `04 Clients/SkinFit Wellness/SkinFit Tech Handoff 2026-08-18.md` → 08 SkinFit Wellness (cited by name); batch3-aesthetic-MASTER (cited by name); SkinFit Wellness - Revenue Diagnostic.pdf (cited by name); SkinFit Wellness - Enquiry Handling Review.pdf (cited by name); Meeting Brief SkinFit 2026-08-18 (cited by name); Runsheet SkinFit Gino 2026-08-18 (cited by name); taste-n-judgement (cited by name)
- `04 Clients/SkinFit Wellness/SkinFit Technical Brief.md` → 08 SkinFit Wellness (clinic name)
- `04 Clients/SkinFit Wellness/Source/skinfit-proposal/README.md` → SkinFit Wellness - Patient Communications Proposal.pdf (cited by name); SkinFit Wellness - Enquiry Handling Review.pdf (cited by name); 08 SkinFit Wellness (clinic name)
- `05 Prospects/Batch 1 Notion Cohort/Outreach 3.md` → Sapphire Skin and Aesthetics (client name); Evenly Skin and Hair Clinic (clinic name)
- `05 Prospects/Batch 1 Notion Cohort/Outreach 4.md` → Aesthetica Veda (client name)
- `05 Prospects/Batch 1 Notion Cohort/Outreach 5.md` → 16 Derma Solutions (clinic name)
- `05 Prospects/Batch 3 Aesthetic and Dental/Batch 3 Dental Audit.md` → SkinFit Wellness (client name); RUA Skin and Hair Center (client name); 08 SkinFit Wellness (clinic name); 02 Skin and Recon (clinic name); 03 Koza Aesthetic Care (clinic name)
- `05 Prospects/Batch 3 Aesthetic and Dental/Handoff Batch 3 Remaining 8.md` → wedge-signal-entry (cited by name); clinic-audit-checklist (cited by name); Karnataka Batches 1-2 Audit 23 Clinics (cited by name); SkinFit Wellness (client name); RUA Skin and Hair Center (client name); 05 SS Aesthetic Clinic (clinic name); 01 RUA Skin and Hair Center (clinic name); 07 Sanssouci Wellness Clinic (clinic name); 08 SkinFit Wellness (clinic name); 06 Contour Cosmetic Clinic (clinic name); 02 Skin and Recon (clinic name); 03 Koza Aesthetic Care (clinic name)
- `05 Prospects/Batch 3 Aesthetic and Dental/batch3-aesthetic-MASTER.md` → wedge-signal-entry (cited by name); clinic-audit-checklist (cited by name); RUA Skin and Hair Call Dossier 2026-08-25 (cited by name); SkinFit Wellness (client name); RUA Skin and Hair Center (client name); 05 SS Aesthetic Clinic (clinic name); 01 RUA Skin and Hair Center (clinic name); 07 Sanssouci Wellness Clinic (clinic name); 08 SkinFit Wellness (clinic name); 06 Contour Cosmetic Clinic (clinic name); 02 Skin and Recon (clinic name); 03 Koza Aesthetic Care (clinic name); 10 Feather Touch Aesthetic Clinic (clinic name)
- `05 Prospects/Batch 3 Remainder/00 Batch 3 Remainder Full Report.md` → wedge-signal-entry (cited by name); SkinFit Wellness (client name); RUA Skin and Hair Center (client name); 05 SS Aesthetic Clinic (clinic name); 01 RUA Skin and Hair Center (clinic name); 07 Sanssouci Wellness Clinic (clinic name); 08 SkinFit Wellness (clinic name); 06 Contour Cosmetic Clinic (clinic name); 02 Skin and Recon (clinic name); 03 Koza Aesthetic Care (clinic name); 10 Feather Touch Aesthetic Clinic (clinic name)
- `05 Prospects/Batch 3 Remainder/01 RUA Skin and Hair Center.md` → RUA Skin and Hair Center (client name); 06 Contour Cosmetic Clinic (clinic name)
- `05 Prospects/Batch 3 Remainder/04 Advanced GroHair GloSkin Jayanagar.md` → wedge-signal-entry (cited by name)
- `05 Prospects/Batch 3 Remainder/06 Contour Cosmetic Clinic.md` → 02 Skin and Recon (clinic name)
- `05 Prospects/Batch 3 Remainder/08 SkinFit Wellness.md` → SkinFit Wellness (client name)
- `05 Prospects/Batch 7 (Notion Batch 2)/11 Gejje's Marvella.md` → Batch 7 MOC (cohort member)
- `05 Prospects/Batch 7 (Notion Batch 2)/12 Haircosmos International.md` → Batch 7 MOC (cohort member)
- `05 Prospects/Batch 7 (Notion Batch 2)/13 Ara Skin Clinic.md` → Batch 7 MOC (cohort member)
- `05 Prospects/Batch 7 (Notion Batch 2)/14 Dr. Priya's Skin and Hair Clinic.md` → Batch 7 MOC (cohort member)
- `05 Prospects/Batch 7 (Notion Batch 2)/15 Akera Health.md` → Batch 7 MOC (cohort member)
- `05 Prospects/Batch 7 (Notion Batch 2)/16 Derma Solutions.md` → Batch 7 MOC (cohort member)
- `05 Prospects/Batch 7 (Notion Batch 2)/18 Theory of Skin.md` → Batch 7 MOC (cohort member)
- `05 Prospects/Batch 7 (Notion Batch 2)/19 Dermatonik.md` → Batch 7 MOC (cohort member)
- `05 Prospects/Batch 7 (Notion Batch 2)/20 VIDA Skin and Hair Transplant.md` → Batch 7 MOC (cohort member)
- `05 Prospects/Batch 7 (Notion Batch 2)/21 Vitals Klinic.md` → Batch 7 MOC (cohort member)
- `05 Prospects/Batch 7 (Notion Batch 2)/22 Krity 360.md` → wedge-signal-entry (cited by name); Batch 7 MOC (cohort member)
- `05 Prospects/Batch 7 (Notion Batch 2)/25 Project Skin.md` → Batch 7 MOC (cohort member)
- `05 Prospects/Batch 7 (Notion Batch 2)/Batch 11-15 Summary.md` → wedge-signal-entry (cited by name); 21 Vitals Klinic (cited by name); 22 Krity 360 (cited by name); 25 Project Skin (cited by name); MEMORY (cited by name); Batch 7 MOC (cohort member)
- `05 Prospects/Batch 7 (Notion Batch 2)/Batch 7 Consolidated State.md` → MEMORY (cited by name); OUTBOUND_MEMORY (cited by name); dr-priya.png (cited by name); akera-health.png (cited by name); project-skin.png (cited by name); krity-360-wa.png (cited by name); theory-of-skin.png (cited by name); vital-skin-1.png (cited by name); vital-skin-2.png (cited by name); SALES_MOTION (cited by name); wedge-signal-entry (cited by name); Sapphire Skin and Aesthetics (client name); Aesthetica Veda (client name); 13 Ara Skin Clinic (clinic name); 16 Derma Solutions (clinic name); 19 Dermatonik (clinic name); 22 Krity 360 (clinic name); 21 Vitals Klinic (clinic name); 18 Theory of Skin (clinic name); 12 Haircosmos International (clinic name); 11 Gejje's Marvella (clinic name); 25 Project Skin (clinic name); 15 Akera Health (clinic name); Batch 7 MOC (cohort member)
- `05 Prospects/Batch 7 (Notion Batch 2)/Batch 7 Follow-up 2 Messages.md` → MEMORY (cited by name); 13 Ara Skin Clinic (clinic name); 16 Derma Solutions (clinic name); 19 Dermatonik (clinic name); 21 Vitals Klinic (clinic name); 12 Haircosmos International (clinic name); 11 Gejje's Marvella (clinic name); 25 Project Skin (clinic name); 15 Akera Health (clinic name); Batch 7 MOC (cohort member)
- `05 Prospects/Batch 7 (Notion Batch 2)/Batch 7 Go List Full Report.md` → wedge-signal-entry (cited by name); personalized-outbound-v2 (cited by name); 13 Ara Skin Clinic (clinic name); 16 Derma Solutions (clinic name); 19 Dermatonik (clinic name); 14 Dr. Priya's Skin and Hair Clinic (clinic name); 18 Theory of Skin (clinic name); 12 Haircosmos International (clinic name); 11 Gejje's Marvella (clinic name); 20 VIDA Skin and Hair Transplant (clinic name); 15 Akera Health (clinic name); Batch 7 MOC (cohort member)
- `05 Prospects/Batch 7 (Notion Batch 2)/Batch 7 Master All Clinics.md` → Batch 7 Consolidated State (cited by name); Batch 7 Wedge Brief (cited by name); Batch 7 Follow-up 2 Messages (cited by name); Batch 7 Go List Full Report (cited by name); Batch 11-15 Summary (cited by name); Findings Batch 7 Clinics 11-20 (cited by name); OUTBOUND_MEMORY (cited by name); MEMORY (cited by name); wedge-signal-entry (cited by name); personalized-outbound-v2 (cited by name); ONE-PAGER-AUDIT-AND-TEST-PLAN (cited by name); akera-health.png (cited by name); dr-priya.png (cited by name); project-skin.png (cited by name); dermatonik-1.png (cited by name); dermatonik-2.png (cited by name); vida-skin-n-hair.png (cited by name); gejjes-marvella.png (cited by name); ara-skin.png (cited by name); vital-skin-1.png (cited by name); vital-skin-2.png (cited by name); krity-360-wa.png (cited by name); theory-of-skin.png (cited by name); SALES_MOTION (cited by name); CLAUDE (cited by name); Sapphire Skin and Aesthetics (client name); Aesthetica Veda (client name); 13 Ara Skin Clinic (clinic name); 16 Derma Solutions (clinic name); 19 Dermatonik (clinic name); 22 Krity 360 (clinic name); 21 Vitals Klinic (clinic name); 14 Dr. Priya's Skin and Hair Clinic (clinic name); 18 Theory of Skin (clinic name); 12 Haircosmos International (clinic name); 11 Gejje's Marvella (clinic name); 20 VIDA Skin and Hair Transplant (clinic name); 25 Project Skin (clinic name); 15 Akera Health (clinic name); Batch 7 MOC (cohort member)
- `05 Prospects/Batch 7 (Notion Batch 2)/Batch 7 Wedge Brief.md` → diagnostic_doc_playbook (cited by name); wedge-signal-entry (cited by name); MEMORY (cited by name); dermatonik-1.png (cited by name); OUTBOUND_MEMORY (cited by name); CLAUDE (cited by name); gejjes-marvella.png (cited by name); vital-skin-1.png (cited by name); 13 Ara Skin Clinic (clinic name); 16 Derma Solutions (clinic name); 19 Dermatonik (clinic name); 21 Vitals Klinic (clinic name); 12 Haircosmos International (clinic name); 11 Gejje's Marvella (clinic name); 20 VIDA Skin and Hair Transplant (clinic name); 25 Project Skin (clinic name); 15 Akera Health (clinic name); Batch 7 MOC (cohort member)
- `05 Prospects/Batch 7 (Notion Batch 2)/Findings Batch 11-15.md` → wedge-signal-entry (cited by name); go-list-mystery-shop (cited by name); 22 Krity 360 (clinic name); 21 Vitals Klinic (clinic name); 25 Project Skin (clinic name); Batch 7 MOC (cohort member)
- `05 Prospects/Batch 7 (Notion Batch 2)/Findings Batch 7 Clinics 11-20.md` → go-list-mystery-shop (cited by name); personalized-outbound-v2 (cited by name); 16 Derma Solutions (clinic name); 19 Dermatonik (clinic name); 18 Theory of Skin (clinic name); 11 Gejje's Marvella (clinic name); 25 Project Skin (clinic name); 15 Akera Health (clinic name); Batch 7 MOC (cohort member)
- `05 Prospects/Batch 7 (Notion Batch 2)/IG Pregate 40 Clinics.md` → wedge-signal-entry (cited by name); OUTBOUND_MEMORY (cited by name); 13 Ara Skin Clinic (clinic name); 16 Derma Solutions (clinic name); 19 Dermatonik (clinic name); 22 Krity 360 (clinic name); 21 Vitals Klinic (clinic name); 18 Theory of Skin (clinic name); 12 Haircosmos International (clinic name); 11 Gejje's Marvella (clinic name); 20 VIDA Skin and Hair Transplant (clinic name); 25 Project Skin (clinic name); 15 Akera Health (clinic name); Batch 7 MOC (cohort member)
- `05 Prospects/Batch 7 (Notion Batch 2)/go-list-mystery-shop.md` → wedge-signal-entry (cited by name); 13 Ara Skin Clinic (clinic name); 16 Derma Solutions (clinic name); 19 Dermatonik (clinic name); 22 Krity 360 (clinic name); 21 Vitals Klinic (clinic name); 18 Theory of Skin (clinic name); 12 Haircosmos International (clinic name); 11 Gejje's Marvella (clinic name); 20 VIDA Skin and Hair Transplant (clinic name); 25 Project Skin (clinic name); 15 Akera Health (clinic name); Batch 7 MOC (cohort member)
- `05 Prospects/Karnataka Batches 1-2/Karnataka Batches 1-2 Audit 23 Clinics.md` → Aesthetica Veda (client name); 16 Derma Solutions (clinic name)
- `05 Prospects/New Leads 1 Batch 9/Ads Presence 2026-08-15.md` → Zone Leads (cited by name); Shortlist 2026-08-14 (cited by name); wedge-signal-entry (cited by name); CLAUDE (cited by name); Aurilueur Esthetic Clinic (client name)
- `05 Prospects/New Leads 1 Batch 9/Clinic Check Table 2026-08-15.md` → Zone Leads (cited by name); CLAUDE (cited by name); Session Handoff 2026-08-15 (cited by name); wedge-signal-entry (cited by name); Aurilueur Esthetic Clinic (client name)
- `05 Prospects/New Leads 1 Batch 9/Contact List Batch 9 2026-08-19.md` → Wedge Angles Batch 9 2026-08-19 (cited by name); Shop 9 Wedge Review 2026-08-19 (cited by name); MEMORY (cited by name); OUTBOUND_MEMORY (cited by name); SALES_MOTION (cited by name)
- `05 Prospects/New Leads 1 Batch 9/Day 0 DMs 2026-08-20.md` → Outreach Drafts Ministry of Skin (cited by name); MEMORY (cited by name); personalized-outbound-v2 (cited by name); OUTBOUND_MEMORY (cited by name)
- `05 Prospects/New Leads 1 Batch 9/Day 0 DMs 2026-08-23.md` → Day 0 DMs 2026-08-20 (cited by name); SALES_MOTION (cited by name); HOW-WE-WORK (cited by name); OUTBOUND_MEMORY (cited by name)
- `05 Prospects/New Leads 1 Batch 9/Flag Resolutions 2026-08-15.md` → Open Checks 2026-08-15 (cited by name); Shop Queue Remainder 2026-08-15 (cited by name); Ads Presence 2026-08-14 (cited by name); wedge-signal-entry (cited by name); Aurilueur Esthetic Clinic (client name); 25 Project Skin (clinic name)
- `05 Prospects/New Leads 1 Batch 9/Open Checks 2026-08-15.md` → Ads Presence 2026-08-15 (cited by name); Shortlist 2026-08-14 (cited by name)
- `05 Prospects/New Leads 1 Batch 9/Session Handoff 2026-08-15.md` → Open Checks 2026-08-15 (cited by name); Ads Presence 2026-08-14 (cited by name); Ads Presence 2026-08-15 (cited by name); Shortlist 2026-08-14 (cited by name); Zone Leads (cited by name); CLAUDE (cited by name); wedge-signal-entry (cited by name); Aurilueur Esthetic Clinic (client name)
- `05 Prospects/New Leads 1 Batch 9/Shop 9 Wedge Review 2026-08-19.md` → Mystery Shop 9 (cited by name); wedge-signal-entry (cited by name); OUTBOUND_MEMORY (cited by name); MEMORY (cited by name); SALES_MOTION (cited by name); HOW-WE-WORK (cited by name); 13 Ara Skin Clinic (clinic name); 22 Krity 360 (clinic name); 18 Theory of Skin (clinic name); 11 Gejje's Marvella (clinic name); 25 Project Skin (clinic name)
- `05 Prospects/New Leads 1 Batch 9/Shop Queue 01-10 2026-08-15.md` → Shop Queue 2026-08-15 (cited by name); Shop Queue 11-20 2026-08-15 (cited by name); CLAUDE (cited by name); wedge-signal-entry (cited by name); Shortlist 2026-08-14 (cited by name); Aurilueur Esthetic Clinic (client name)
- `05 Prospects/New Leads 1 Batch 9/Shop Queue 11-20 2026-08-15.md` → Shop Queue 2026-08-15 (cited by name); wedge-signal-entry (cited by name); CLAUDE (cited by name)
- `05 Prospects/New Leads 1 Batch 9/Shop Queue 2026-08-15.md` → Shop Queue 11-20 2026-08-15 (cited by name); wedge-signal-entry (cited by name); CLAUDE (cited by name); SALES_MOTION (cited by name); OUTBOUND_MEMORY (cited by name); Aurilueur Esthetic Clinic (client name); Sapphire Skin and Aesthetics (client name); Aesthetica Veda (client name)
- `05 Prospects/New Leads 1 Batch 9/Shop Queue Remainder 2026-08-15.md` → Shop Queue 01-10 2026-08-15 (cited by name); Shop Queue 11-20 2026-08-15 (cited by name); Open Checks 2026-08-15 (cited by name); wedge-signal-entry (cited by name)
- `05 Prospects/New Leads 1 Batch 9/Wedge Angles Batch 9 2026-08-19.md` → Clinic Check Table 2026-08-15 (cited by name); Shop 9 Wedge Review 2026-08-19 (cited by name); OUTBOUND_MEMORY (cited by name); wedge-signal-entry (cited by name); SALES_MOTION (cited by name); HOW-WE-WORK (cited by name); 16 Derma Solutions (clinic name); 22 Krity 360 (clinic name); 18 Theory of Skin (clinic name); 25 Project Skin (clinic name)
- `05 Prospects/SE Bangalore Scrape/Ads Presence 2026-08-14.md` → Qualified Targets 2026-08-14 (cited by name); wedge-signal-entry (cited by name); CLAUDE (cited by name); The Derma Theory (clinic name)
- `05 Prospects/SE Bangalore Scrape/New Clinics Table 2026-08-10.md` → CLAUDE (cited by name); MEMORY (cited by name); Sapphire Skin and Aesthetics (client name); 19 Dermatonik (clinic name); 21 Vitals Klinic (clinic name); 12 Haircosmos International (clinic name); 25 Project Skin (clinic name); 06 Contour Cosmetic Clinic (clinic name); 10 Feather Touch Aesthetic Clinic (clinic name); Evenly Skin and Hair Clinic (clinic name); The Derma Theory (clinic name)
- `05 Prospects/SE Bangalore Scrape/Qualified Targets 2026-08-14.md` → New Clinics Table 2026-08-10 (cited by name); The Derma Theory (clinic name)
- `05 Prospects/SE Bangalore Scrape/Shortlist 2026-08-14.md` → Qualified Targets 2026-08-14 (cited by name); Ads Presence 2026-08-14 (cited by name); wedge-signal-entry (cited by name); CLAUDE (cited by name); The Derma Theory (clinic name)
- `05 Prospects/Scrape 2026-07-19/Dr. Praba Independent Clinic.md` → SkinFit Wellness (client name); 15 Akera Health (clinic name)
- `05 Prospects/Scrape 2026-07-19/Mister Hair Clinic.md` → Sapphire Skin and Aesthetics (client name)
- `05 Prospects/Scrape 2026-07-19/Rejected Candidates 2026-07-19.md` → 12 Haircosmos International (clinic name); The Derma Theory (clinic name)
- `05 Prospects/Verify 2026-08-18/Enquiry Flow Shortlist 2026-08-19.md` → Final Table (cited by name); CLAUDE (cited by name); wedge-signal-entry (cited by name); The Derma Theory (clinic name)
- `05 Prospects/Verify 2026-08-18/Final Table.md` → The Derma Theory (clinic name)
- `05 Prospects/Verify 2026-08-18/Qualified Leads 2026-08-19.md` → Disqualified 2026-08-18 (cited by name); The Derma Theory (clinic name)
- `05 Prospects/Verify 2026-08-18/Qualified Leads 2026-08-20.md` → The Derma Theory (clinic name)
- `05 Prospects/Verify 2026-08-18/Resume Note 2026-08-18.md` → Final Table (cited by name); The Derma Theory (clinic name)
- `06 Outreach Drafts/Outreach Drafts Glow Clinic.md` → OUTBOUND_SYSTEM_AUDIT (cited by name); MEMORY (cited by name); OUTBOUND_MEMORY (cited by name)
- `06 Outreach Drafts/Outreach Drafts Ministry of Skin.md` → OUTBOUND_MEMORY (cited by name)
- `06 Outreach Drafts/Outreach Drafts Utkarsha to Evenly.md` → LEARNINGS_LOG (cited by name); Sapphire Skin and Aesthetics (client name); Evenly Skin and Hair Clinic (clinic name)
- `08 Collateral/Audit Call Docs/02_data_intake_requirements.md` → SALES_MOTION (cited by name); 04 Findings and Rollout (cited by name)
- `09 Company/Legal and Commercial Doc Set.md` → MEMORY (cited by name); SkinFit Information Request Review (cited by name); SALES_MOTION (cited by name); CLAUDE (cited by name); OUTBOUND_MEMORY (cited by name); 05 Pilot and Onboarding (cited by name); SkinFit Wellness (client name); Sapphire Skin and Aesthetics (client name); 08 SkinFit Wellness (clinic name)
- `09 Company/Paperwork Handbook 2026-09-06.md` → Legal and Commercial Doc Set (cited by name); SkinFit Wellness (client name); Aurilueur Esthetic Clinic (client name); RUA Skin and Hair Center (client name)
- `09 Company/Pricing and Build Cost 2026-08-21.md` → OUTBOUND_MEMORY (cited by name); SkinFit Technical Brief (cited by name); SkinFit Tech Handoff 2026-08-18 (cited by name); taste-n-judgement (cited by name); wedge-signal-entry (cited by name); SkinFit Wellness (client name); 08 SkinFit Wellness (clinic name)
- `COHORT-INDEX.md` → Apify Discovery Context (cited by name); Outreach 1 (cited by name); Outreach 2 (cited by name); Outreach 3 (cited by name); Outreach 4 (cited by name); Outreach 5 (cited by name); Karnataka Batches 1-2 Audit 23 Clinics (cited by name); batch3-aesthetic-MASTER (cited by name); Batch 3 Dental Audit (cited by name); 00 Batch 3 Remainder Full Report (cited by name); Handoff Batch 3 Remaining 8 (cited by name); go-list-mystery-shop (cited by name); Rejected Candidates 2026-07-19 (cited by name); Evenly Skin and Hair Clinic (cited by name); New Clinics Table 2026-08-10 (cited by name); Session 2026-08-10 SE Bangalore Scrape (cited by name); IG Pregate 40 Clinics (cited by name); LinkedIn Sales Navigator Personas (cited by name); Meeting Brief Sapphire 2026-08-13 (cited by name); Sapphire Skin and Aesthetics (client name); 22 Krity 360 (clinic name); 18 Theory of Skin (clinic name)

## 11 · Left open, needs a human

- Empty directory chain `Resources/_source/skinfit-proposal-v2/Resources/_source/aurilueur-proposal/` — untracked by git; delete or leave, Tilak's call.
- Which of the three SkinFit "Patient Conversion" PDFs was sent.
- `.claude/skills/clinic-audit-research/SKILL.md` now writes new dossiers to `05 Prospects/`; the next batch should name its cohort subfolder.
- Rows in `_reorg_manifest.csv` marked medium remain as recorded decisions; flip any and re-run the corresponding move if wanted.


## 12 · Every move

| Old | New | Action |
|---|---|---|
| `clinic-research-sources.md` | `01 Playbooks/Clinic Research Sources.md` | move |
| `dental-discovery-CRITERIA.md` | `01 Playbooks/Dental Discovery/Dental Discovery Criteria.md` | flag-merge-candidate |
| `dental-discovery-STEP-1-QUALIFY.md` | `01 Playbooks/Dental Discovery/Dental Discovery Step 1 Qualify.md` | flag-merge-candidate |
| `dental-discovery-STEP-2-RESEARCH.md` | `01 Playbooks/Dental Discovery/Dental Discovery Step 2 Research.md` | move |
| `lead-prioritization-method.md` | `01 Playbooks/Lead Prioritization Method.md` | move |
| `linkedin-sales-navigator-personas.md` | `01 Playbooks/LinkedIn Sales Navigator Personas.md` | move |
| `PROCESS-MAP.md` | `01 Playbooks/Process Map.md` | move |
| `apify-discovery-CONTEXT.md` | `01 Playbooks/Research Prompts/Apify Discovery Context.md` | move |
| `apify-discovery-PROMPT.md` | `01 Playbooks/Research Prompts/Apify Discovery Prompt.md` | move |
| `prompt-research-clinics-11-15.md` | `01 Playbooks/Research Prompts/Prompt Research Clinics 11-15.md` | move |
| `sales-motion/01-reply-to-call.md` | `01 Playbooks/Sales Motion/01 Reply to Call.md` | flag-merge-candidate |
| `sales-motion/02-credibility-packet.md` | `01 Playbooks/Sales Motion/02 Credibility Packet.md` | flag-merge-candidate |
| `sales-motion/03-operations-call.md` | `01 Playbooks/Sales Motion/03 Operations Call.md` | flag-merge-candidate |
| `sales-motion/04-findings-and-rollout.md` | `01 Playbooks/Sales Motion/04 Findings and Rollout.md` | flag-merge-candidate |
| `sales-motion/05-pilot-and-onboarding.md` | `01 Playbooks/Sales Motion/05 Pilot and Onboarding.md` | flag-merge-candidate |
| `sales-motion/client-facing/HOW-WE-WORK.md` | `01 Playbooks/Sales Motion/HOW-WE-WORK.md` | move |
| `SALES_MOTION.md` | `01 Playbooks/Sales Motion/SALES_MOTION.md` | flag-merge-candidate |
| `clinic-audit-checklist.md` | `01 Playbooks/clinic-audit-checklist.md` | flag-merge-candidate |
| `One-page-docs/diagnostic_doc_playbook.md` | `01 Playbooks/diagnostic_doc_playbook.md` | move |
| `personalized-outbound-v2.md` | `01 Playbooks/personalized-outbound-v2.md` | flag-merge-candidate |
| `wedge-signal-entry.md` | `01 Playbooks/wedge-signal-entry.md` | flag-merge-candidate |
| `EVENT-SNAPSHOT-2026-09-02.md` | `03 Audits and Reviews/Event Snapshot 2026-09-02.md` | move |
| `ONE-PAGER-AUDIT-AND-TEST-PLAN.md` | `03 Audits and Reviews/ONE-PAGER-AUDIT-AND-TEST-PLAN.md` | flag-merge-candidate |
| `ONE-PAGER-STEELMAN-2026-08-14.md` | `03 Audits and Reviews/One-Pager Steelman 2026-08-14.md` | flag-merge-candidate |
| `outbound-process-changes-2026-08-11.md` | `03 Audits and Reviews/Outbound Process Changes 2026-08-11.md` | move |
| `SESSION-2026-08-10-se-bangalore-scrape.md` | `03 Audits and Reviews/Session 2026-08-10 SE Bangalore Scrape.md` | move |
| `outreach-aesthetica-veda-vaibhav-whatsapp.md` | `04 Clients/Aesthetica Veda/Aesthetica Veda Vybhav WhatsApp First Touch.md` | move |
| `AURILUEUR-BANGALORE-PRICE-BENCHMARKS-2026-09-05.md` | `04 Clients/Aurilueur Esthetic Clinic/Aurilueur Bangalore Price Benchmarks 2026-09-05.md` | move |
| `Proposals & SOW/Aurilueur Esthetic Clinic - Enquiry and Appointment Systems Proposal.pdf` | `04 Clients/Aurilueur Esthetic Clinic/Aurilueur Esthetic Clinic - Enquiry and Appointment Systems Proposal.pdf` | move |
| `Resources/Aurilueur Esthetic Clinic - Operations Findings.pdf` | `04 Clients/Aurilueur Esthetic Clinic/Aurilueur Esthetic Clinic - Operations Findings.pdf` | move |
| `Resources/Aurilueur Esthetic Clinic - What We're Seeing Across Bangalore.pdf` | `04 Clients/Aurilueur Esthetic Clinic/Aurilueur Esthetic Clinic - What We're Seeing Across Bangalore.pdf` | move |
| `Resources/Aurilueur Esthetic Clinic - Intake Form (Post-Meeting).md` | `04 Clients/Aurilueur Esthetic Clinic/Aurilueur Esthetic Clinic Intake Form (Post Meeting).md` | move |
| `AURILUEUR-REVENUE-RESEARCH-2026-09-05.md` | `04 Clients/Aurilueur Esthetic Clinic/Aurilueur Revenue Research 2026-09-05.md` | move |
| `RUNSHEET-aureliere-2026-08-21.md` | `04 Clients/Aurilueur Esthetic Clinic/Runsheet Aurilueur 2026-08-21.md` | move |
| `Resources/_source/aurilueur-proposal/README.md` | `04 Clients/Aurilueur Esthetic Clinic/Source/aurilueur-proposal/README.md` | flag-merge-candidate |
| `Resources/_source/aurilueur-proposal/fonts/Poppins-400-normal.ttf` | `04 Clients/Aurilueur Esthetic Clinic/Source/aurilueur-proposal/fonts/Poppins-400-normal.ttf` | move |
| `Resources/_source/aurilueur-proposal/fonts/Poppins-500-italic.ttf` | `04 Clients/Aurilueur Esthetic Clinic/Source/aurilueur-proposal/fonts/Poppins-500-italic.ttf` | move |
| `Resources/_source/aurilueur-proposal/fonts/Poppins-500-normal.ttf` | `04 Clients/Aurilueur Esthetic Clinic/Source/aurilueur-proposal/fonts/Poppins-500-normal.ttf` | move |
| `Resources/_source/aurilueur-proposal/fonts/Poppins-600-normal.ttf` | `04 Clients/Aurilueur Esthetic Clinic/Source/aurilueur-proposal/fonts/Poppins-600-normal.ttf` | move |
| `Resources/_source/aurilueur-proposal/proposal.html` | `04 Clients/Aurilueur Esthetic Clinic/Source/aurilueur-proposal/proposal.html` | move |
| `Resources/_source/aurilueur-proposal/style.css` | `04 Clients/Aurilueur Esthetic Clinic/Source/aurilueur-proposal/style.css` | move |
| `Proposals & SOW/RUA Skin & Hair Center - Patient Communications Proposal.pdf` | `04 Clients/RUA Skin and Hair Center/RUA Skin & Hair Center - Patient Communications Proposal.pdf` | move |
| `Proposals & SOW/RUA Skin & Hair Center - Scope of Work.pdf` | `04 Clients/RUA Skin and Hair Center/RUA Skin & Hair Center - Scope of Work.pdf` | move |
| `Pre-outbound-research/rua-skin-hair-CALL-DOSSIER-2026-08-25.md` | `04 Clients/RUA Skin and Hair Center/RUA Skin and Hair Call Dossier 2026-08-25.md` | move |
| `Resources/_source/rua-proposal/fonts/Poppins-400-normal.ttf` | `04 Clients/RUA Skin and Hair Center/Source/rua-proposal/fonts/Poppins-400-normal.ttf` | move |
| `Resources/_source/rua-proposal/fonts/Poppins-500-italic.ttf` | `04 Clients/RUA Skin and Hair Center/Source/rua-proposal/fonts/Poppins-500-italic.ttf` | move |
| `Resources/_source/rua-proposal/fonts/Poppins-500-normal.ttf` | `04 Clients/RUA Skin and Hair Center/Source/rua-proposal/fonts/Poppins-500-normal.ttf` | move |
| `Resources/_source/rua-proposal/fonts/Poppins-600-normal.ttf` | `04 Clients/RUA Skin and Hair Center/Source/rua-proposal/fonts/Poppins-600-normal.ttf` | move |
| `Resources/_source/rua-proposal/proposal.html` | `04 Clients/RUA Skin and Hair Center/Source/rua-proposal/proposal.html` | move |
| `Resources/_source/rua-proposal/style.css` | `04 Clients/RUA Skin and Hair Center/Source/rua-proposal/style.css` | move |
| `Resources/_source/rua-sow/sow.html` | `04 Clients/RUA Skin and Hair Center/Source/rua-sow/sow.html` | move |
| `MEETING-BRIEF-sapphire-2026-08-13.md` | `04 Clients/Sapphire Skin and Aesthetics/Meeting Brief Sapphire 2026-08-13.md` | move |
| `Pitch-decks/sapphire-skin-clinic.pdf` | `04 Clients/Sapphire Skin and Aesthetics/sapphire-skin-clinic.pdf` | move |
| `MEETING-BRIEF-skinfit-2026-08-18.md` | `04 Clients/SkinFit Wellness/Meeting Brief SkinFit 2026-08-18.md` | move |
| `RUNSHEET-skinfit-gino-2026-08-18.md` | `04 Clients/SkinFit Wellness/Runsheet SkinFit Gino 2026-08-18.md` | move |
| `SKINFIT-INFORMATION-REQUEST-REVIEW.md` | `04 Clients/SkinFit Wellness/SkinFit Information Request Review.md` | move |
| `SKINFIT-PROPOSAL-SOW-REVIEW-2026-08-22.md` | `04 Clients/SkinFit Wellness/SkinFit Proposal and SOW Review 2026-08-22.md` | move |
| `SKINFIT-TECH-HANDOFF-2026-08-18.md` | `04 Clients/SkinFit Wellness/SkinFit Tech Handoff 2026-08-18.md` | move |
| `SKINFIT-TECHNICAL-BRIEF.md` | `04 Clients/SkinFit Wellness/SkinFit Technical Brief.md` | move |
| `Resources/SkinFit Wellness - Enquiry Handling Review.pdf` | `04 Clients/SkinFit Wellness/SkinFit Wellness - Enquiry Handling Review.pdf` | move |
| `Proposals & SOW/SkinFit Wellness - Enquiry System Strategy.html` | `04 Clients/SkinFit Wellness/SkinFit Wellness - Enquiry System Strategy.html` | move |
| `Proposals & SOW/SkinFit Wellness - Enquiry System Strategy.pdf` | `04 Clients/SkinFit Wellness/SkinFit Wellness - Enquiry System Strategy.pdf` | move |
| `Proposals & SOW/SkinFit Wellness - Patient Communications Proposal v2.pdf` | `04 Clients/SkinFit Wellness/SkinFit Wellness - Patient Communications Proposal v2.pdf` | move |
| `Proposals & SOW/SkinFit Wellness - Patient Communications Proposal.pdf` | `04 Clients/SkinFit Wellness/SkinFit Wellness - Patient Communications Proposal.pdf` | move |
| `Resources/SkinFit Wellness - Patient Conversion Proposal.html` | `04 Clients/SkinFit Wellness/SkinFit Wellness - Patient Conversion Proposal.html` | move |
| `Proposals & SOW/SkinFit Wellness - Patient Conversion Proposal.pdf` | `04 Clients/SkinFit Wellness/SkinFit Wellness - Patient Conversion Proposal.pdf` | flag-merge-candidate |
| `Resources/SkinFit Wellness - Patient Conversion System.html` | `04 Clients/SkinFit Wellness/SkinFit Wellness - Patient Conversion System.html` | move |
| `Proposals & SOW/SkinFit Wellness - Patient Conversion System.pdf` | `04 Clients/SkinFit Wellness/SkinFit Wellness - Patient Conversion System.pdf` | flag-merge-candidate |
| `Resources/SkinFit Wellness - Patient Conversion and Intelligence System.html` | `04 Clients/SkinFit Wellness/SkinFit Wellness - Patient Conversion and Intelligence System.html` | move |
| `Proposals & SOW/SkinFit Wellness - Patient Conversion and Intelligence System.pdf` | `04 Clients/SkinFit Wellness/SkinFit Wellness - Patient Conversion and Intelligence System.pdf` | flag-merge-candidate |
| `Resources/SkinFit Wellness - Revenue Diagnostic.pdf` | `04 Clients/SkinFit Wellness/SkinFit Wellness - Revenue Diagnostic.pdf` | move |
| `Resources/SkinFit Wellness - Scope of Work.html` | `04 Clients/SkinFit Wellness/SkinFit Wellness - Scope of Work.html` | move |
| `Proposals & SOW/SkinFit Wellness - Scope of Work.pdf` | `04 Clients/SkinFit Wellness/SkinFit Wellness - Scope of Work.pdf` | move |
| `Resources/_source/skinfit-proposal-v2/fonts/Poppins-400-normal.ttf` | `04 Clients/SkinFit Wellness/Source/skinfit-proposal-v2/fonts/Poppins-400-normal.ttf` | move |
| `Resources/_source/skinfit-proposal-v2/fonts/Poppins-500-italic.ttf` | `04 Clients/SkinFit Wellness/Source/skinfit-proposal-v2/fonts/Poppins-500-italic.ttf` | move |
| `Resources/_source/skinfit-proposal-v2/fonts/Poppins-500-normal.ttf` | `04 Clients/SkinFit Wellness/Source/skinfit-proposal-v2/fonts/Poppins-500-normal.ttf` | move |
| `Resources/_source/skinfit-proposal-v2/fonts/Poppins-600-normal.ttf` | `04 Clients/SkinFit Wellness/Source/skinfit-proposal-v2/fonts/Poppins-600-normal.ttf` | move |
| `Resources/_source/skinfit-proposal-v2/proposal.html` | `04 Clients/SkinFit Wellness/Source/skinfit-proposal-v2/proposal.html` | flag-merge-candidate |
| `Resources/_source/skinfit-proposal-v2/style.css` | `04 Clients/SkinFit Wellness/Source/skinfit-proposal-v2/style.css` | move |
| `Resources/_source/skinfit-proposal/README.md` | `04 Clients/SkinFit Wellness/Source/skinfit-proposal/README.md` | flag-merge-candidate |
| `Resources/_source/skinfit-proposal/fonts/Poppins-400-normal.ttf` | `04 Clients/SkinFit Wellness/Source/skinfit-proposal/fonts/Poppins-400-normal.ttf` | move |
| `Resources/_source/skinfit-proposal/fonts/Poppins-500-italic.ttf` | `04 Clients/SkinFit Wellness/Source/skinfit-proposal/fonts/Poppins-500-italic.ttf` | move |
| `Resources/_source/skinfit-proposal/fonts/Poppins-500-normal.ttf` | `04 Clients/SkinFit Wellness/Source/skinfit-proposal/fonts/Poppins-500-normal.ttf` | move |
| `Resources/_source/skinfit-proposal/fonts/Poppins-600-normal.ttf` | `04 Clients/SkinFit Wellness/Source/skinfit-proposal/fonts/Poppins-600-normal.ttf` | move |
| `Resources/_source/skinfit-proposal/proposal.html` | `04 Clients/SkinFit Wellness/Source/skinfit-proposal/proposal.html` | flag-merge-candidate |
| `Resources/_source/skinfit-proposal/style.css` | `04 Clients/SkinFit Wellness/Source/skinfit-proposal/style.css` | move |
| `Pre-outbound-research/OUTREACH document.md` | `05 Prospects/Batch 1 Notion Cohort/Outreach 1.md` | flag-merge-candidate |
| `Pre-outbound-research/outreach -2.md` | `05 Prospects/Batch 1 Notion Cohort/Outreach 2.md` | flag-merge-candidate |
| `Pre-outbound-research/outreach 3.md` | `05 Prospects/Batch 1 Notion Cohort/Outreach 3.md` | move |
| `Pre-outbound-research/outreach 4 (1).md` | `05 Prospects/Batch 1 Notion Cohort/Outreach 4.md` | move |
| `Pre-outbound-research/outreach-5 (1).md` | `05 Prospects/Batch 1 Notion Cohort/Outreach 5.md` | move |
| `Pre-outbound-research/batch3-dental-audit.md` | `05 Prospects/Batch 3 Aesthetic and Dental/Batch 3 Dental Audit.md` | move |
| `handoff-batch3-remaining-8.md` | `05 Prospects/Batch 3 Aesthetic and Dental/Handoff Batch 3 Remaining 8.md` | move |
| `Pre-outbound-research/batch3-aesthetic-MASTER.md` | `05 Prospects/Batch 3 Aesthetic and Dental/batch3-aesthetic-MASTER.md` | move |
| `Research-docs/00-BATCH-FULL-REPORT.md` | `05 Prospects/Batch 3 Remainder/00 Batch 3 Remainder Full Report.md` | move |
| `Research-docs/01-rua-skin-and-hair-center.md` | `05 Prospects/Batch 3 Remainder/01 RUA Skin and Hair Center.md` | move |
| `Research-docs/02-skin-and-recon.md` | `05 Prospects/Batch 3 Remainder/02 Skin and Recon.md` | move |
| `Research-docs/03-koza-aesthetic-care.md` | `05 Prospects/Batch 3 Remainder/03 Koza Aesthetic Care.md` | move |
| `Research-docs/04-advanced-grohair-gloskin-jayanagar.md` | `05 Prospects/Batch 3 Remainder/04 Advanced GroHair GloSkin Jayanagar.md` | move |
| `Research-docs/05-ss-aesthetic-clinic.md` | `05 Prospects/Batch 3 Remainder/05 SS Aesthetic Clinic.md` | move |
| `Research-docs/06-contour-cosmetic-clinic.md` | `05 Prospects/Batch 3 Remainder/06 Contour Cosmetic Clinic.md` | move |
| `Research-docs/07-sanssouci-wellness-clinic.md` | `05 Prospects/Batch 3 Remainder/07 Sanssouci Wellness Clinic.md` | move |
| `Research-docs/08-skinfit-wellness.md` | `05 Prospects/Batch 3 Remainder/08 SkinFit Wellness.md` | move |
| `Research-docs/09-sparha-aesthetic-studio.md` | `05 Prospects/Batch 3 Remainder/09 Sparha Aesthetic Studio.md` | move |
| `Research-docs/10-feather-touch-aesthetic-clinic.md` | `05 Prospects/Batch 3 Remainder/10 Feather Touch Aesthetic Clinic.md` | move |
| `Research-docs/batch-comparison-table.csv` | `05 Prospects/Batch 3 Remainder/batch-comparison-table.csv` | move |
| `Pre-outbound-research/batch7/11-gejjes-marvella.md` | `05 Prospects/Batch 7 (Notion Batch 2)/11 Gejje's Marvella.md` | move |
| `Pre-outbound-research/batch7/12-haircosmos-international.md` | `05 Prospects/Batch 7 (Notion Batch 2)/12 Haircosmos International.md` | move |
| `Pre-outbound-research/batch7/13-ara-skin-clinic.md` | `05 Prospects/Batch 7 (Notion Batch 2)/13 Ara Skin Clinic.md` | move |
| `Pre-outbound-research/batch7/14-dr-priyas-skin-and-hair-clinic.md` | `05 Prospects/Batch 7 (Notion Batch 2)/14 Dr. Priya's Skin and Hair Clinic.md` | move |
| `Pre-outbound-research/batch7/15-akera-health.md` | `05 Prospects/Batch 7 (Notion Batch 2)/15 Akera Health.md` | move |
| `Pre-outbound-research/batch7/16-derma-solutions.md` | `05 Prospects/Batch 7 (Notion Batch 2)/16 Derma Solutions.md` | move |
| `Pre-outbound-research/batch7/18-theory-of-skin.md` | `05 Prospects/Batch 7 (Notion Batch 2)/18 Theory of Skin.md` | move |
| `Pre-outbound-research/batch7/19-dermatonik.md` | `05 Prospects/Batch 7 (Notion Batch 2)/19 Dermatonik.md` | move |
| `Pre-outbound-research/batch7/20-vida-skin-and-hair-transplant.md` | `05 Prospects/Batch 7 (Notion Batch 2)/20 VIDA Skin and Hair Transplant.md` | move |
| `Pre-outbound-research/batch7/21-vitals-klinic.md` | `05 Prospects/Batch 7 (Notion Batch 2)/21 Vitals Klinic.md` | move |
| `Pre-outbound-research/batch7/22-krity-360.md` | `05 Prospects/Batch 7 (Notion Batch 2)/22 Krity 360.md` | move |
| `Pre-outbound-research/batch7/25-project-skin.md` | `05 Prospects/Batch 7 (Notion Batch 2)/25 Project Skin.md` | move |
| `Pre-outbound-research/batch7/batch-11-15-summary.md` | `05 Prospects/Batch 7 (Notion Batch 2)/Batch 11-15 Summary.md` | move |
| `Pre-outbound-research/batch7/BATCH7-CONSOLIDATED-STATE.md` | `05 Prospects/Batch 7 (Notion Batch 2)/Batch 7 Consolidated State.md` | flag-merge-candidate |
| `Pre-outbound-research/batch7/BATCH7-FOLLOWUP2-MESSAGES.md` | `05 Prospects/Batch 7 (Notion Batch 2)/Batch 7 Follow-up 2 Messages.md` | flag-merge-candidate |
| `Pre-outbound-research/batch7/go-list-full-report.md` | `05 Prospects/Batch 7 (Notion Batch 2)/Batch 7 Go List Full Report.md` | move |
| `Pre-outbound-research/batch7/BATCH7-MASTER-ALL-CLINICS.md` | `05 Prospects/Batch 7 (Notion Batch 2)/Batch 7 Master All Clinics.md` | flag-merge-candidate |
| `Pre-outbound-research/batch7/BATCH7-WEDGE-BRIEF.md` | `05 Prospects/Batch 7 (Notion Batch 2)/Batch 7 Wedge Brief.md` | move |
| `findings-batch-11-15.md` | `05 Prospects/Batch 7 (Notion Batch 2)/Findings Batch 11-15.md` | flag-merge-candidate |
| `findings-batch7-clinics-11-20.md` | `05 Prospects/Batch 7 (Notion Batch 2)/Findings Batch 7 Clinics 11-20.md` | flag-merge-candidate |
| `ig-pregate-40-clinics.md` | `05 Prospects/Batch 7 (Notion Batch 2)/IG Pregate 40 Clinics.md` | move |
| `Pre-outbound-research/batch7/mystery-shop-b7/akera-health.png` | `05 Prospects/Batch 7 (Notion Batch 2)/Mystery Shop B7/akera-health.png` | move |
| `Pre-outbound-research/batch7/mystery-shop-b7/ara-skin.png` | `05 Prospects/Batch 7 (Notion Batch 2)/Mystery Shop B7/ara-skin.png` | move |
| `Pre-outbound-research/batch7/mystery-shop-b7/dermatonik-1.png` | `05 Prospects/Batch 7 (Notion Batch 2)/Mystery Shop B7/dermatonik-1.png` | move |
| `Pre-outbound-research/batch7/mystery-shop-b7/dermatonik-2.png` | `05 Prospects/Batch 7 (Notion Batch 2)/Mystery Shop B7/dermatonik-2.png` | move |
| `Pre-outbound-research/batch7/mystery-shop-b7/dr-priya.png` | `05 Prospects/Batch 7 (Notion Batch 2)/Mystery Shop B7/dr-priya.png` | move |
| `Pre-outbound-research/batch7/mystery-shop-b7/gejjes-marvella.png` | `05 Prospects/Batch 7 (Notion Batch 2)/Mystery Shop B7/gejjes-marvella.png` | move |
| `Pre-outbound-research/batch7/mystery-shop-b7/krity-360-wa.png` | `05 Prospects/Batch 7 (Notion Batch 2)/Mystery Shop B7/krity-360-wa.png` | move |
| `Pre-outbound-research/batch7/mystery-shop-b7/project-skin.png` | `05 Prospects/Batch 7 (Notion Batch 2)/Mystery Shop B7/project-skin.png` | move |
| `Pre-outbound-research/batch7/mystery-shop-b7/theory-of-skin.png` | `05 Prospects/Batch 7 (Notion Batch 2)/Mystery Shop B7/theory-of-skin.png` | move |
| `Pre-outbound-research/batch7/mystery-shop-b7/vida-skin-n-hair.png` | `05 Prospects/Batch 7 (Notion Batch 2)/Mystery Shop B7/vida-skin-n-hair.png` | move |
| `Pre-outbound-research/batch7/mystery-shop-b7/vital-skin-1.png` | `05 Prospects/Batch 7 (Notion Batch 2)/Mystery Shop B7/vital-skin-1.png` | move |
| `Pre-outbound-research/batch7/mystery-shop-b7/vital-skin-2.png` | `05 Prospects/Batch 7 (Notion Batch 2)/Mystery Shop B7/vital-skin-2.png` | move |
| `go-list-mystery-shop.md` | `05 Prospects/Batch 7 (Notion Batch 2)/go-list-mystery-shop.md` | move |
| `Pre-outbound-research/batch1-2-audit-23-clinics.md` | `05 Prospects/Karnataka Batches 1-2/Karnataka Batches 1-2 Audit 23 Clinics.md` | move |
| `Mystery_Shop_2026-08-15/Aestheticaa_Dr_Madhulika_AcnePeel_2026-08-15.jpg` | `05 Prospects/Mystery Shop 2026-08-15/Aestheticaa_Dr_Madhulika_AcnePeel_2026-08-15.jpg` | move |
| `Mystery_Shop_2026-08-15/Body_Science_The_Aesthetic_Clinic_HairFall_2026-08-15/Body_Science_The_Aesthetic_Clinic_HairFall_2026-08-15_Part1.jpg` | `05 Prospects/Mystery Shop 2026-08-15/Body_Science_The_Aesthetic_Clinic_HairFall_2026-08-15/Body_Science_The_Aesthetic_Clinic_HairFall_2026-08-15_Part1.jpg` | move |
| `Mystery_Shop_2026-08-15/Body_Science_The_Aesthetic_Clinic_HairFall_2026-08-15/Body_Science_The_Aesthetic_Clinic_HairFall_2026-08-15_Part2.jpg` | `05 Prospects/Mystery Shop 2026-08-15/Body_Science_The_Aesthetic_Clinic_HairFall_2026-08-15/Body_Science_The_Aesthetic_Clinic_HairFall_2026-08-15_Part2.jpg` | move |
| `Mystery_Shop_2026-08-15/Divine_Aesthetics_AcneTreatment_2026-08-15.jpg` | `05 Prospects/Mystery Shop 2026-08-15/Divine_Aesthetics_AcneTreatment_2026-08-15.jpg` | move |
| `Mystery_Shop_2026-08-15/Dr_Sood_Aesthetics_HairFall_2026-08-15/Dr_Sood_Aesthetics_HairFall_2026-08-15_Part1.jpg` | `05 Prospects/Mystery Shop 2026-08-15/Dr_Sood_Aesthetics_HairFall_2026-08-15/Dr_Sood_Aesthetics_HairFall_2026-08-15_Part1.jpg` | move |
| `Mystery_Shop_2026-08-15/Dr_Sood_Aesthetics_HairFall_2026-08-15/Dr_Sood_Aesthetics_HairFall_2026-08-15_Part2.jpg` | `05 Prospects/Mystery Shop 2026-08-15/Dr_Sood_Aesthetics_HairFall_2026-08-15/Dr_Sood_Aesthetics_HairFall_2026-08-15_Part2.jpg` | move |
| `Mystery_Shop_2026-08-15/Elixir_Advanced_Aesthetics_HairLoss_2026-08-15.jpg` | `05 Prospects/Mystery Shop 2026-08-15/Elixir_Advanced_Aesthetics_HairLoss_2026-08-15.jpg` | move |
| `Mystery_Shop_2026-08-15/Kavana_Dermo_Glamm_HairFall_2026-08-15.jpg` | `05 Prospects/Mystery Shop 2026-08-15/Kavana_Dermo_Glamm_HairFall_2026-08-15.jpg` | move |
| `Mystery_Shop_2026-08-15/Maya_HairFall_2026-08-15.jpg` | `05 Prospects/Mystery Shop 2026-08-15/Maya_HairFall_2026-08-15.jpg` | move |
| `Mystery_Shop_2026-08-15/Moon_Aesthetic_HairFall_2026-08-15/Moon_Aesthetic_HairFall_2026-08-15_Part1.jpg` | `05 Prospects/Mystery Shop 2026-08-15/Moon_Aesthetic_HairFall_2026-08-15/Moon_Aesthetic_HairFall_2026-08-15_Part1.jpg` | move |
| `Mystery_Shop_2026-08-15/Moon_Aesthetic_HairFall_2026-08-15/Moon_Aesthetic_HairFall_2026-08-15_Part2.jpg` | `05 Prospects/Mystery Shop 2026-08-15/Moon_Aesthetic_HairFall_2026-08-15/Moon_Aesthetic_HairFall_2026-08-15_Part2.jpg` | move |
| `Mystery_Shop_2026-08-15/Regenique_Dermatology_and_Aesthetics_HairThinning_2026-08-15.jpg` | `05 Prospects/Mystery Shop 2026-08-15/Regenique_Dermatology_and_Aesthetics_HairThinning_2026-08-15.jpg` | move |
| `Mystery_Shop_2026-08-15/Sun_Light_Skin_Clinic_HairSpa_2026-08-15.jpg` | `05 Prospects/Mystery Shop 2026-08-15/Sun_Light_Skin_Clinic_HairSpa_2026-08-15.jpg` | move |
| `new_leads_1/ADS-PRESENCE-2026-08-15.md` | `05 Prospects/New Leads 1 Batch 9/Ads Presence 2026-08-15.md` | move |
| `new_leads_1/CLINIC-CHECK-TABLE-2026-08-15.md` | `05 Prospects/New Leads 1 Batch 9/Clinic Check Table 2026-08-15.md` | move |
| `new_leads_1/Clinic_Directory_Template csv 3b771d3ba7f680e0b00acf18a11921d5.csv` | `05 Prospects/New Leads 1 Batch 9/Clinic_Directory_Template csv 3b771d3ba7f680e0b00acf18a11921d5.csv` | move |
| `new_leads_1/CONTACT-LIST-BATCH-9-2026-08-19.md` | `05 Prospects/New Leads 1 Batch 9/Contact List Batch 9 2026-08-19.md` | move |
| `new_leads_1/DAY0-DMS-2026-08-20.md` | `05 Prospects/New Leads 1 Batch 9/Day 0 DMs 2026-08-20.md` | move |
| `new_leads_1/DAY0-DMS-2026-08-23.md` | `05 Prospects/New Leads 1 Batch 9/Day 0 DMs 2026-08-23.md` | move |
| `new_leads_1/FLAG-RESOLUTIONS-2026-08-15.md` | `05 Prospects/New Leads 1 Batch 9/Flag Resolutions 2026-08-15.md` | move |
| `new_leads_1/mystery shop 9.md` | `05 Prospects/New Leads 1 Batch 9/Mystery Shop 9.md` | move |
| `new_leads_1/Mystery_Shop_2026-08-15-1.zip` | `05 Prospects/New Leads 1 Batch 9/Mystery_Shop_2026-08-15-1.zip` | move |
| `new_leads_1/OPEN-CHECKS-2026-08-15.md` | `05 Prospects/New Leads 1 Batch 9/Open Checks 2026-08-15.md` | move |
| `new_leads_1/SESSION-HANDOFF-2026-08-15.md` | `05 Prospects/New Leads 1 Batch 9/Session Handoff 2026-08-15.md` | move |
| `new_leads_1/SHOP-9-WEDGE-REVIEW-2026-08-19.md` | `05 Prospects/New Leads 1 Batch 9/Shop 9 Wedge Review 2026-08-19.md` | move |
| `new_leads_1/SHOP-QUEUE-01-10-2026-08-15.md` | `05 Prospects/New Leads 1 Batch 9/Shop Queue 01-10 2026-08-15.md` | move |
| `new_leads_1/SHOP-QUEUE-11-20-2026-08-15.md` | `05 Prospects/New Leads 1 Batch 9/Shop Queue 11-20 2026-08-15.md` | move |
| `new_leads_1/SHOP-QUEUE-2026-08-15.md` | `05 Prospects/New Leads 1 Batch 9/Shop Queue 2026-08-15.md` | move |
| `new_leads_1/SHOP-QUEUE-REMAINDER-2026-08-15.md` | `05 Prospects/New Leads 1 Batch 9/Shop Queue Remainder 2026-08-15.md` | move |
| `new_leads_1/WEDGE-ANGLES-BATCH-9-2026-08-19.md` | `05 Prospects/New Leads 1 Batch 9/Wedge Angles Batch 9 2026-08-19.md` | move |
| `new_leads_1/zone-leads.md` | `05 Prospects/New Leads 1 Batch 9/Zone Leads.md` | move |
| `new_leads_1/build_targets.py` | `05 Prospects/New Leads 1 Batch 9/build_targets.py` | move |
| `new_leads_1/consolidate.py` | `05 Prospects/New Leads 1 Batch 9/consolidate.py` | move |
| `new_leads_1/fb_search_results.json` | `05 Prospects/New Leads 1 Batch 9/fb_search_results.json` | move |
| `new_leads_1/fb_search_round3.json` | `05 Prospects/New Leads 1 Batch 9/fb_search_round3.json` | move |
| `new_leads_1/fb_url_provenance.json` | `05 Prospects/New Leads 1 Batch 9/fb_url_provenance.json` | move |
| `new_leads_1/fb_urls.json` | `05 Prospects/New Leads 1 Batch 9/fb_urls.json` | move |
| `new_leads_1/fb_urls2.json` | `05 Prospects/New Leads 1 Batch 9/fb_urls2.json` | move |
| `new_leads_1/find_socials.py` | `05 Prospects/New Leads 1 Batch 9/find_socials.py` | move |
| `new_leads_1/gads_detail/1.json` | `05 Prospects/New Leads 1 Batch 9/gads_detail/1.json` | move |
| `new_leads_1/gads_detail/10.json` | `05 Prospects/New Leads 1 Batch 9/gads_detail/10.json` | move |
| `new_leads_1/gads_detail/11.json` | `05 Prospects/New Leads 1 Batch 9/gads_detail/11.json` | move |
| `new_leads_1/gads_detail/14.json` | `05 Prospects/New Leads 1 Batch 9/gads_detail/14.json` | move |
| `new_leads_1/gads_detail/16.json` | `05 Prospects/New Leads 1 Batch 9/gads_detail/16.json` | move |
| `new_leads_1/gads_detail/20.json` | `05 Prospects/New Leads 1 Batch 9/gads_detail/20.json` | move |
| `new_leads_1/gads_detail/26.json` | `05 Prospects/New Leads 1 Batch 9/gads_detail/26.json` | move |
| `new_leads_1/gads_detail/28.json` | `05 Prospects/New Leads 1 Batch 9/gads_detail/28.json` | move |
| `new_leads_1/gads_detail/3.json` | `05 Prospects/New Leads 1 Batch 9/gads_detail/3.json` | move |
| `new_leads_1/gads_detail/30.json` | `05 Prospects/New Leads 1 Batch 9/gads_detail/30.json` | move |
| `new_leads_1/gads_detail/35.json` | `05 Prospects/New Leads 1 Batch 9/gads_detail/35.json` | move |
| `new_leads_1/gads_detail/36.json` | `05 Prospects/New Leads 1 Batch 9/gads_detail/36.json` | move |
| `new_leads_1/gads_detail/39.json` | `05 Prospects/New Leads 1 Batch 9/gads_detail/39.json` | move |
| `new_leads_1/gads_detail/40.json` | `05 Prospects/New Leads 1 Batch 9/gads_detail/40.json` | move |
| `new_leads_1/gads_detail/5.json` | `05 Prospects/New Leads 1 Batch 9/gads_detail/5.json` | move |
| `new_leads_1/gads_detail/6.json` | `05 Prospects/New Leads 1 Batch 9/gads_detail/6.json` | move |
| `new_leads_1/gads_detail/7.json` | `05 Prospects/New Leads 1 Batch 9/gads_detail/7.json` | move |
| `new_leads_1/gads_detail/9.json` | `05 Prospects/New Leads 1 Batch 9/gads_detail/9.json` | move |
| `new_leads_1/gads_queries.json` | `05 Prospects/New Leads 1 Batch 9/gads_queries.json` | move |
| `new_leads_1/gads_recency.py` | `05 Prospects/New Leads 1 Batch 9/gads_recency.py` | move |
| `new_leads_1/google-ads-raw-2026-08-15.json` | `05 Prospects/New Leads 1 Batch 9/google-ads-raw-2026-08-15.json` | move |
| `new_leads_1/google-ads-recency.json` | `05 Prospects/New Leads 1 Batch 9/google-ads-recency.json` | move |
| `new_leads_1/instagram-raw-2026-08-15.json` | `05 Prospects/New Leads 1 Batch 9/instagram-raw-2026-08-15.json` | move |
| `new_leads_1/instagram-summary.json` | `05 Prospects/New Leads 1 Batch 9/instagram-summary.json` | move |
| `new_leads_1/meta-ads-raw-2026-08-15.json` | `05 Prospects/New Leads 1 Batch 9/meta-ads-raw-2026-08-15.json` | move |
| `new_leads_1/meta-ads-summary-round2.json` | `05 Prospects/New Leads 1 Batch 9/meta-ads-summary-round2.json` | move |
| `new_leads_1/meta-ads-summary-round3.json` | `05 Prospects/New Leads 1 Batch 9/meta-ads-summary-round3.json` | move |
| `new_leads_1/meta-ads-summary.json` | `05 Prospects/New Leads 1 Batch 9/meta-ads-summary.json` | move |
| `new_leads_1/results.json` | `05 Prospects/New Leads 1 Batch 9/results.json` | move |
| `new_leads_1/socials.json` | `05 Prospects/New Leads 1 Batch 9/socials.json` | move |
| `new_leads_1/targets.json` | `05 Prospects/New Leads 1 Batch 9/targets.json` | move |
| `se-bangalore-scrape/ADS-PRESENCE-2026-08-14.md` | `05 Prospects/SE Bangalore Scrape/Ads Presence 2026-08-14.md` | move |
| `se-bangalore-scrape/NEW-CLINICS-TABLE.md` | `05 Prospects/SE Bangalore Scrape/New Clinics Table 2026-08-10.md` | move |
| `se-bangalore-scrape/QUALIFIED-TARGETS-2026-08-14.md` | `05 Prospects/SE Bangalore Scrape/Qualified Targets 2026-08-14.md` | move |
| `se-bangalore-scrape/SHORTLIST-2026-08-14.md` | `05 Prospects/SE Bangalore Scrape/Shortlist 2026-08-14.md` | move |
| `se-bangalore-scrape/autosave.log` | `05 Prospects/SE Bangalore Scrape/autosave.log` | move |
| `se-bangalore-scrape/autosave.sh` | `05 Prospects/SE Bangalore Scrape/autosave.sh` | move |
| `se-bangalore-scrape/gen_targets.py` | `05 Prospects/SE Bangalore Scrape/gen_targets.py` | move |
| `se-bangalore-scrape/process.py` | `05 Prospects/SE Bangalore Scrape/process.py` | move |
| `se-bangalore-scrape/raw/bannerghatta.json` | `05 Prospects/SE Bangalore Scrape/raw/bannerghatta.json` | move |
| `se-bangalore-scrape/raw/bommanahalli_partial.json` | `05 Prospects/SE Bangalore Scrape/raw/bommanahalli_partial.json` | move |
| `se-bangalore-scrape/raw/eleccity.json` | `05 Prospects/SE Bangalore Scrape/raw/eleccity.json` | move |
| `se-bangalore-scrape/raw/hsr.json` | `05 Prospects/SE Bangalore Scrape/raw/hsr.json` | move |
| `se-bangalore-scrape/raw/sarjapur_partial.json` | `05 Prospects/SE Bangalore Scrape/raw/sarjapur_partial.json` | move |
| `se-bangalore-scrape/results.json` | `05 Prospects/SE Bangalore Scrape/results.json` | move |
| `Pre-outbound-research/south-bangalore-scrape-2026-08-10.csv` | `05 Prospects/SE Bangalore Scrape/south-bangalore-scrape-2026-08-10.csv` | move |
| `clinics/amintri-skin-hair-clinic.md` | `05 Prospects/Scrape 2026-07-19/Amintri Skin Hair Clinic.md` | move |
| `clinics/beeyens-skin-and-laser-clinic.md` | `05 Prospects/Scrape 2026-07-19/Beeyens Skin and Laser Clinic.md` | move |
| `clinics/clinique-hair-transplant-centre.md` | `05 Prospects/Scrape 2026-07-19/Clinique Hair Transplant Centre.md` | move |
| `clinics/dermaqure.md` | `05 Prospects/Scrape 2026-07-19/Dermaqure.md` | move |
| `clinics/dr-praba-independent-clinic.md` | `05 Prospects/Scrape 2026-07-19/Dr. Praba Independent Clinic.md` | move |
| `clinics/evenly-skin-and-hair-clinic.md` | `05 Prospects/Scrape 2026-07-19/Evenly Skin and Hair Clinic.md` | move |
| `clinics/looks-hair-and-skin-clinic.md` | `05 Prospects/Scrape 2026-07-19/Looks Hair and Skin Clinic.md` | move |
| `clinics/mister-hair-clinic.md` | `05 Prospects/Scrape 2026-07-19/Mister Hair Clinic.md` | move |
| `clinics/nikhilesh-dental-clinic.md` | `05 Prospects/Scrape 2026-07-19/Nikhilesh Dental Clinic.md` | move |
| `clinics/rejected-candidates.md` | `05 Prospects/Scrape 2026-07-19/Rejected Candidates 2026-07-19.md` | move |
| `clinics/smile-world-dental-clinic.md` | `05 Prospects/Scrape 2026-07-19/Smile World Dental Clinic.md` | move |
| `clinics/the-derma-theory.md` | `05 Prospects/Scrape 2026-07-19/The Derma Theory.md` | move |
| `clinics/tooth-and-root-dental-clinic.md` | `05 Prospects/Scrape 2026-07-19/Tooth and Root Dental Clinic.md` | move |
| `clinics/vrudhii-aesthetics.md` | `05 Prospects/Scrape 2026-07-19/Vrudhii Aesthetics.md` | move |
| `clinics/master-scrape-log.csv` | `05 Prospects/Scrape 2026-07-19/master-scrape-log.csv` | move |
| `verify-2026-08-18/DISQUALIFIED.md` | `05 Prospects/Verify 2026-08-18/Disqualified 2026-08-18.md` | move |
| `verify-2026-08-18/ENQUIRY-FLOW-SHORTLIST.md` | `05 Prospects/Verify 2026-08-18/Enquiry Flow Shortlist 2026-08-19.md` | move |
| `verify-2026-08-18/FINAL-TABLE.md` | `05 Prospects/Verify 2026-08-18/Final Table.md` | flag-merge-candidate |
| `verify-2026-08-18/QUALIFIED-LEADS-2026-08-19.md` | `05 Prospects/Verify 2026-08-18/Qualified Leads 2026-08-19.md` | flag-merge-candidate |
| `verify-2026-08-18/QUALIFIED-LEADS-2026-08-20.md` | `05 Prospects/Verify 2026-08-18/Qualified Leads 2026-08-20.md` | move |
| `verify-2026-08-18/RESUME.md` | `05 Prospects/Verify 2026-08-18/Resume Note 2026-08-18.md` | move |
| `verify-2026-08-18/domains.json` | `05 Prospects/Verify 2026-08-18/domains.json` | move |
| `verify-2026-08-18/doms.txt` | `05 Prospects/Verify 2026-08-18/doms.txt` | move |
| `verify-2026-08-18/fetchig.sh` | `05 Prospects/Verify 2026-08-18/fetchig.sh` | move |
| `verify-2026-08-18/gads.json` | `05 Prospects/Verify 2026-08-18/gads.json` | move |
| `verify-2026-08-18/gbp.json` | `05 Prospects/Verify 2026-08-18/gbp.json` | move |
| `verify-2026-08-18/state.json` | `05 Prospects/Verify 2026-08-18/state.json` | move |
| `outreach-emails-utkarsha-keshav-karishma-dixit-juvita.md` | `06 Outreach Drafts/Cold Emails Utkarsha Keshav Karishma Dixit Juvita.md` | move |
| `outreach-drafts-glow-clinic.md` | `06 Outreach Drafts/Outreach Drafts Glow Clinic.md` | move |
| `outreach-drafts-ministry-of-skin.md` | `06 Outreach Drafts/Outreach Drafts Ministry of Skin.md` | move |
| `outreach-drafts-utkarsha-to-evenly.md` | `06 Outreach Drafts/Outreach Drafts Utkarsha to Evenly.md` | move |
| `outreach-drafts-vtiara.md` | `06 Outreach Drafts/Outreach Drafts Vtiara.md` | move |
| `One-page-docs/Aesthetica Veda - Revenue Diagnostic.html` | `07 One-Pagers/Aesthetica Veda - Revenue Diagnostic.html` | move |
| `One-page-docs/Aesthetica Veda - Revenue Diagnostic.jpg` | `07 One-Pagers/Aesthetica Veda - Revenue Diagnostic.jpg` | move |
| `One-page-docs/Aesthetica Veda - Revenue Diagnostic.pdf` | `07 One-Pagers/Aesthetica Veda - Revenue Diagnostic.pdf` | move |
| `One-page-docs/Aesthetica Veda - Revenue Diagnostic.png` | `07 One-Pagers/Aesthetica Veda - Revenue Diagnostic.png` | move |
| `One-page-docs/Akera Health - Enquiry Diagnostic.html` | `07 One-Pagers/Akera Health - Enquiry Diagnostic.html` | move |
| `One-page-docs/Akera Health - Enquiry Diagnostic.jpg` | `07 One-Pagers/Akera Health - Enquiry Diagnostic.jpg` | move |
| `One-page-docs/Akera Health - Enquiry Diagnostic.pdf` | `07 One-Pagers/Akera Health - Enquiry Diagnostic.pdf` | move |
| `One-page-docs/Akera Health - Enquiry Diagnostic.png` | `07 One-Pagers/Akera Health - Enquiry Diagnostic.png` | move |
| `One-page-docs/Ara Skin Clinic - Enquiry Diagnostic.html` | `07 One-Pagers/Ara Skin Clinic - Enquiry Diagnostic.html` | move |
| `One-page-docs/Ara Skin Clinic - Enquiry Diagnostic.jpg` | `07 One-Pagers/Ara Skin Clinic - Enquiry Diagnostic.jpg` | move |
| `One-page-docs/Ara Skin Clinic - Enquiry Diagnostic.pdf` | `07 One-Pagers/Ara Skin Clinic - Enquiry Diagnostic.pdf` | move |
| `One-page-docs/Ara Skin Clinic - Enquiry Diagnostic.png` | `07 One-Pagers/Ara Skin Clinic - Enquiry Diagnostic.png` | move |
| `One-page-docs/AvatarLuxe - A Revenue Diagnostic (WhatsApp image).jpg` | `07 One-Pagers/AvatarLuxe - A Revenue Diagnostic (WhatsApp image).jpg` | move |
| `One-page-docs/AvatarLuxe - A Revenue Diagnostic.pdf` | `07 One-Pagers/AvatarLuxe - A Revenue Diagnostic.pdf` | move |
| `One-page-docs/Clinic Next Face - A Revenue Diagnostic (WhatsApp image).jpg` | `07 One-Pagers/Clinic Next Face - A Revenue Diagnostic (WhatsApp image).jpg` | move |
| `One-page-docs/Clinic Next Face - A Revenue Diagnostic.pdf` | `07 One-Pagers/Clinic Next Face - A Revenue Diagnostic.pdf` | move |
| `One-page-docs/Cozmo Blis - What We Found.pdf` | `07 One-Pagers/Cozmo Blis - What We Found.pdf` | move |
| `One-page-docs/DNA Skin Clinic - A Revenue Diagnostic (WhatsApp image).jpg` | `07 One-Pagers/DNA Skin Clinic - A Revenue Diagnostic (WhatsApp image).jpg` | move |
| `One-page-docs/DNA Skin Clinic - A Revenue Diagnostic.pdf` | `07 One-Pagers/DNA Skin Clinic - A Revenue Diagnostic.pdf` | move |
| `One-page-docs/DNA Skin Clinic - Revenue Diagnostic.html` | `07 One-Pagers/DNA Skin Clinic - Revenue Diagnostic.html` | move |
| `One-page-docs/DNA Skin Clinic - Revenue Diagnostic.jpg` | `07 One-Pagers/DNA Skin Clinic - Revenue Diagnostic.jpg` | move |
| `One-page-docs/DNA Skin Clinic - Revenue Diagnostic.pdf` | `07 One-Pagers/DNA Skin Clinic - Revenue Diagnostic.pdf` | move |
| `One-page-docs/DNA Skin Clinic - Revenue Diagnostic.png` | `07 One-Pagers/DNA Skin Clinic - Revenue Diagnostic.png` | move |
| `One-page-docs/Derma Solutions - Enquiry Diagnostic.html` | `07 One-Pagers/Derma Solutions - Enquiry Diagnostic.html` | move |
| `One-page-docs/Derma Solutions - Enquiry Diagnostic.jpg` | `07 One-Pagers/Derma Solutions - Enquiry Diagnostic.jpg` | move |
| `One-page-docs/Derma Solutions - Enquiry Diagnostic.pdf` | `07 One-Pagers/Derma Solutions - Enquiry Diagnostic.pdf` | move |
| `One-page-docs/Derma Solutions - Enquiry Diagnostic.png` | `07 One-Pagers/Derma Solutions - Enquiry Diagnostic.png` | move |
| `One-page-docs/Dermatonik Aesthetic Clinic - Enquiry Diagnostic.html` | `07 One-Pagers/Dermatonik Aesthetic Clinic - Enquiry Diagnostic.html` | move |
| `One-page-docs/Dermatonik Aesthetic Clinic - Enquiry Diagnostic.jpg` | `07 One-Pagers/Dermatonik Aesthetic Clinic - Enquiry Diagnostic.jpg` | move |
| `One-page-docs/Dermatonik Aesthetic Clinic - Enquiry Diagnostic.pdf` | `07 One-Pagers/Dermatonik Aesthetic Clinic - Enquiry Diagnostic.pdf` | move |
| `One-page-docs/Dermatonik Aesthetic Clinic - Enquiry Diagnostic.png` | `07 One-Pagers/Dermatonik Aesthetic Clinic - Enquiry Diagnostic.png` | move |
| `One-page-docs/Dermaville Skin Clinic - Revenue Diagnostic.html` | `07 One-Pagers/Dermaville Skin Clinic - Revenue Diagnostic.html` | move |
| `One-page-docs/Dermaville Skin Clinic - Revenue Diagnostic.jpg` | `07 One-Pagers/Dermaville Skin Clinic - Revenue Diagnostic.jpg` | move |
| `One-page-docs/Dermaville Skin Clinic - Revenue Diagnostic.pdf` | `07 One-Pagers/Dermaville Skin Clinic - Revenue Diagnostic.pdf` | move |
| `One-page-docs/Dermaville Skin Clinic - Revenue Diagnostic.png` | `07 One-Pagers/Dermaville Skin Clinic - Revenue Diagnostic.png` | move |
| `One-page-docs/Dr. Dixit - Revenue Diagnostic.html` | `07 One-Pagers/Dr. Dixit - Revenue Diagnostic.html` | move |
| `One-page-docs/Dr. Dixit - Revenue Diagnostic.jpg` | `07 One-Pagers/Dr. Dixit - Revenue Diagnostic.jpg` | move |
| `One-page-docs/Dr. Dixit - Revenue Diagnostic.pdf` | `07 One-Pagers/Dr. Dixit - Revenue Diagnostic.pdf` | move |
| `One-page-docs/Dr. Dixit - Revenue Diagnostic.png` | `07 One-Pagers/Dr. Dixit - Revenue Diagnostic.png` | move |
| `One-page-docs/Dr. Juvita Aesthetics - Revenue Diagnostic.html` | `07 One-Pagers/Dr. Juvita Aesthetics - Revenue Diagnostic.html` | move |
| `One-page-docs/Dr. Juvita Aesthetics - Revenue Diagnostic.jpg` | `07 One-Pagers/Dr. Juvita Aesthetics - Revenue Diagnostic.jpg` | move |
| `One-page-docs/Dr. Juvita Aesthetics - Revenue Diagnostic.pdf` | `07 One-Pagers/Dr. Juvita Aesthetics - Revenue Diagnostic.pdf` | move |
| `One-page-docs/Dr. Juvita Aesthetics - Revenue Diagnostic.png` | `07 One-Pagers/Dr. Juvita Aesthetics - Revenue Diagnostic.png` | move |
| `One-page-docs/Dr. Priya's Skin & Hair Clinic - Enquiry Diagnostic.html` | `07 One-Pagers/Dr. Priya's Skin & Hair Clinic - Enquiry Diagnostic.html` | move |
| `One-page-docs/Dr. Priya's Skin & Hair Clinic - Enquiry Diagnostic.jpg` | `07 One-Pagers/Dr. Priya's Skin & Hair Clinic - Enquiry Diagnostic.jpg` | move |
| `One-page-docs/Dr. Priya's Skin & Hair Clinic - Enquiry Diagnostic.pdf` | `07 One-Pagers/Dr. Priya's Skin & Hair Clinic - Enquiry Diagnostic.pdf` | move |
| `One-page-docs/Dr. Priya's Skin & Hair Clinic - Enquiry Diagnostic.png` | `07 One-Pagers/Dr. Priya's Skin & Hair Clinic - Enquiry Diagnostic.png` | move |
| `One-page-docs/Dr. Swetha's Cosmoderm Centre - Revenue Diagnostic.html` | `07 One-Pagers/Dr. Swetha's Cosmoderm Centre - Revenue Diagnostic.html` | move |
| `One-page-docs/Dr. Swetha's Cosmoderm Centre - Revenue Diagnostic.jpg` | `07 One-Pagers/Dr. Swetha's Cosmoderm Centre - Revenue Diagnostic.jpg` | move |
| `One-page-docs/Dr. Swetha's Cosmoderm Centre - Revenue Diagnostic.pdf` | `07 One-Pagers/Dr. Swetha's Cosmoderm Centre - Revenue Diagnostic.pdf` | move |
| `One-page-docs/Dr. Swetha's Cosmoderm Centre - Revenue Diagnostic.png` | `07 One-Pagers/Dr. Swetha's Cosmoderm Centre - Revenue Diagnostic.png` | move |
| `One-page-docs/Dr. Tina's Skin Solutionz - A Revenue Diagnostic (WhatsApp image).jpg` | `07 One-Pagers/Dr. Tina's Skin Solutionz - A Revenue Diagnostic (WhatsApp image).jpg` | move |
| `One-page-docs/Dr. Tina's Skin Solutionz - A Revenue Diagnostic.pdf` | `07 One-Pagers/Dr. Tina's Skin Solutionz - A Revenue Diagnostic.pdf` | move |
| `One-page-docs/Dr. Tina's Skin Solutionz - Enquiry Diagnostic.html` | `07 One-Pagers/Dr. Tina's Skin Solutionz - Enquiry Diagnostic.html` | move |
| `One-page-docs/Dr. Tina's Skin Solutionz - Enquiry Diagnostic.jpg` | `07 One-Pagers/Dr. Tina's Skin Solutionz - Enquiry Diagnostic.jpg` | move |
| `One-page-docs/Dr. Tina's Skin Solutionz - Enquiry Diagnostic.pdf` | `07 One-Pagers/Dr. Tina's Skin Solutionz - Enquiry Diagnostic.pdf` | move |
| `One-page-docs/Dr. Tina's Skin Solutionz - Enquiry Diagnostic.png` | `07 One-Pagers/Dr. Tina's Skin Solutionz - Enquiry Diagnostic.png` | move |
| `One-page-docs/Gejje's Marvella - Enquiry Diagnostic.html` | `07 One-Pagers/Gejje's Marvella - Enquiry Diagnostic.html` | move |
| `One-page-docs/Gejje's Marvella - Enquiry Diagnostic.jpg` | `07 One-Pagers/Gejje's Marvella - Enquiry Diagnostic.jpg` | move |
| `One-page-docs/Gejje's Marvella - Enquiry Diagnostic.pdf` | `07 One-Pagers/Gejje's Marvella - Enquiry Diagnostic.pdf` | move |
| `One-page-docs/Gejje's Marvella - Enquiry Diagnostic.png` | `07 One-Pagers/Gejje's Marvella - Enquiry Diagnostic.png` | move |
| `One-page-docs/Iridescent Aesthetics - A Revenue Diagnostic (WhatsApp image).jpg` | `07 One-Pagers/Iridescent Aesthetics - A Revenue Diagnostic (WhatsApp image).jpg` | move |
| `One-page-docs/Iridescent Aesthetics - A Revenue Diagnostic.pdf` | `07 One-Pagers/Iridescent Aesthetics - A Revenue Diagnostic.pdf` | move |
| `One-page-docs/Maya Medi Spa - Enquiry Diagnostic.html` | `07 One-Pagers/Maya Medi Spa - Enquiry Diagnostic.html` | move |
| `One-page-docs/Maya Medi Spa - Enquiry Diagnostic.jpg` | `07 One-Pagers/Maya Medi Spa - Enquiry Diagnostic.jpg` | move |
| `One-page-docs/Maya Medi Spa - Enquiry Diagnostic.pdf` | `07 One-Pagers/Maya Medi Spa - Enquiry Diagnostic.pdf` | move |
| `One-page-docs/Maya Medi Spa - Enquiry Diagnostic.png` | `07 One-Pagers/Maya Medi Spa - Enquiry Diagnostic.png` | move |
| `One-page-docs/Ministry of Skin - Revenue Diagnostic.html` | `07 One-Pagers/Ministry of Skin - Revenue Diagnostic.html` | move |
| `One-page-docs/Ministry of Skin - Revenue Diagnostic.jpg` | `07 One-Pagers/Ministry of Skin - Revenue Diagnostic.jpg` | move |
| `One-page-docs/Ministry of Skin - Revenue Diagnostic.pdf` | `07 One-Pagers/Ministry of Skin - Revenue Diagnostic.pdf` | move |
| `One-page-docs/Ministry of Skin - Revenue Diagnostic.png` | `07 One-Pagers/Ministry of Skin - Revenue Diagnostic.png` | move |
| `One-page-docs/Project Skin - Enquiry Diagnostic.html` | `07 One-Pagers/Project Skin - Enquiry Diagnostic.html` | move |
| `One-page-docs/Project Skin - Enquiry Diagnostic.jpg` | `07 One-Pagers/Project Skin - Enquiry Diagnostic.jpg` | move |
| `One-page-docs/Project Skin - Enquiry Diagnostic.pdf` | `07 One-Pagers/Project Skin - Enquiry Diagnostic.pdf` | move |
| `One-page-docs/Project Skin - Enquiry Diagnostic.png` | `07 One-Pagers/Project Skin - Enquiry Diagnostic.png` | move |
| `One-page-docs/The Glow Clinic - Revenue Diagnostic.html` | `07 One-Pagers/The Glow Clinic - Revenue Diagnostic.html` | move |
| `One-page-docs/The Glow Clinic - Revenue Diagnostic.jpg` | `07 One-Pagers/The Glow Clinic - Revenue Diagnostic.jpg` | move |
| `One-page-docs/The Glow Clinic - Revenue Diagnostic.pdf` | `07 One-Pagers/The Glow Clinic - Revenue Diagnostic.pdf` | move |
| `One-page-docs/The Glow Clinic - Revenue Diagnostic.png` | `07 One-Pagers/The Glow Clinic - Revenue Diagnostic.png` | move |
| `One-page-docs/VIDA Skin & Hair Transplant Clinic - Enquiry Diagnostic.html` | `07 One-Pagers/VIDA Skin & Hair Transplant Clinic - Enquiry Diagnostic.html` | move |
| `One-page-docs/VIDA Skin & Hair Transplant Clinic - Enquiry Diagnostic.jpg` | `07 One-Pagers/VIDA Skin & Hair Transplant Clinic - Enquiry Diagnostic.jpg` | move |
| `One-page-docs/VIDA Skin & Hair Transplant Clinic - Enquiry Diagnostic.pdf` | `07 One-Pagers/VIDA Skin & Hair Transplant Clinic - Enquiry Diagnostic.pdf` | move |
| `One-page-docs/VIDA Skin & Hair Transplant Clinic - Enquiry Diagnostic.png` | `07 One-Pagers/VIDA Skin & Hair Transplant Clinic - Enquiry Diagnostic.png` | move |
| `One-page-docs/Venkat Center - Revenue Diagnostic.html` | `07 One-Pagers/Venkat Center - Revenue Diagnostic.html` | move |
| `One-page-docs/Venkat Center - Revenue Diagnostic.jpg` | `07 One-Pagers/Venkat Center - Revenue Diagnostic.jpg` | move |
| `One-page-docs/Venkat Center - Revenue Diagnostic.pdf` | `07 One-Pagers/Venkat Center - Revenue Diagnostic.pdf` | move |
| `One-page-docs/Venkat Center - Revenue Diagnostic.png` | `07 One-Pagers/Venkat Center - Revenue Diagnostic.png` | move |
| `One-page-docs/Vtiara Hair & Skin Clinic - Revenue Diagnostic.html` | `07 One-Pagers/Vtiara Hair & Skin Clinic - Revenue Diagnostic.html` | move |
| `One-page-docs/Vtiara Hair & Skin Clinic - Revenue Diagnostic.jpg` | `07 One-Pagers/Vtiara Hair & Skin Clinic - Revenue Diagnostic.jpg` | move |
| `One-page-docs/Vtiara Hair & Skin Clinic - Revenue Diagnostic.pdf` | `07 One-Pagers/Vtiara Hair & Skin Clinic - Revenue Diagnostic.pdf` | move |
| `One-page-docs/Vtiara Hair & Skin Clinic - Revenue Diagnostic.png` | `07 One-Pagers/Vtiara Hair & Skin Clinic - Revenue Diagnostic.png` | move |
| `AI Readiness Workbook .pdf` | `08 Collateral/AI Readiness Workbook .pdf` | move |
| `Audit_call_docs/01_shadow_audit_checklist.md` | `08 Collateral/Audit Call Docs/01 Shadow Audit Checklist.md` | move |
| `Audit_call_docs/01_shadow_audit_checklist.docx` | `08 Collateral/Audit Call Docs/01_shadow_audit_checklist.docx` | move |
| `Audit_call_docs/02_data_intake_requirements.docx` | `08 Collateral/Audit Call Docs/02_data_intake_requirements.docx` | move |
| `Audit_call_docs/02_data_intake_requirements.md` | `08 Collateral/Audit Call Docs/02_data_intake_requirements.md` | move |
| `Audit_call_docs/03_discovery_call_question_map.md` | `08 Collateral/Audit Call Docs/03 Discovery Call Question Map.md` | move |
| `Audit_call_docs/03_discovery_call_question_map.docx` | `08 Collateral/Audit Call Docs/03_discovery_call_question_map.docx` | move |
| `Resources/What We're Seeing Across Bangalore.pdf` | `08 Collateral/What We're Seeing Across Bangalore.pdf` | move |
| `Resources/Where Enquiries Go Quiet.html` | `08 Collateral/Where Enquiries Go Quiet.html` | move |
| `Resources/Where Enquiries Go Quiet.jpg` | `08 Collateral/Where Enquiries Go Quiet.jpg` | move |
| `Resources/Where Enquiries Go Quiet.pdf` | `08 Collateral/Where Enquiries Go Quiet.pdf` | move |
| `Resources/Where Enquiries Go Quiet.png` | `08 Collateral/Where Enquiries Go Quiet.png` | move |
| `revenue_os_discovery_audit_fillable.pdf` | `08 Collateral/revenue_os_discovery_audit_fillable.pdf` | move |
| `LEGAL-AND-COMMERCIAL-DOC-SET.md` | `09 Company/Legal and Commercial Doc Set.md` | move |
| `PAPERWORK-HANDBOOK-2026-09-06.md` | `09 Company/Paperwork Handbook 2026-09-06.md` | move |
| `PRICING-BUILD-COST-2026-08-21.md` | `09 Company/Pricing and Build Cost 2026-08-21.md` | move |
| `Valence-Data-Register.pdf` | `09 Company/Valence-Data-Register.pdf` | move |
| `Valence_Ops_Systems_and_Current_Technical_Stack.pdf` | `09 Company/Valence_Ops_Systems_and_Current_Technical_Stack.pdf` | move |
| `money-and-tax-explainer.html` | `09 Company/money-and-tax-explainer.html` | move |
| `valenceops-context-september.pdf` | `09 Company/valenceops-context-september.pdf` | move |
| `valenceops_context_1.pdf` | `09 Company/valenceops_context_1.pdf` | move |
| `lead-qualifier-suite/.claude-plugin/marketplace.json` | `10 Tooling/lead-qualifier-suite/.claude-plugin/marketplace.json` | move |
| `lead-qualifier-suite/.claude-plugin/plugin.json` | `10 Tooling/lead-qualifier-suite/.claude-plugin/plugin.json` | move |
| `lead-qualifier-suite/scripts/company_qualifier.py` | `10 Tooling/lead-qualifier-suite/scripts/company_qualifier.py` | move |
| `lead-qualifier-suite/skills/gamma-deck/SKILL.md` | `10 Tooling/lead-qualifier-suite/skills/gamma-deck/SKILL.md` | move |
| `lead-qualifier-suite/skills/gamma-deck/agents/openai.yaml` | `10 Tooling/lead-qualifier-suite/skills/gamma-deck/agents/openai.yaml` | move |
| `lead-qualifier-suite/skills/gamma-deck/references/gamma-deck-spec.md` | `10 Tooling/lead-qualifier-suite/skills/gamma-deck/references/gamma-deck-spec.md` | move |
| `lead-qualifier-suite/skills/orchestrator/SKILL.md` | `10 Tooling/lead-qualifier-suite/skills/orchestrator/SKILL.md` | move |
| `lead-qualifier-suite/skills/orchestrator/agents/openai.yaml` | `10 Tooling/lead-qualifier-suite/skills/orchestrator/agents/openai.yaml` | move |
| `lead-qualifier-suite/skills/personalization/SKILL.md` | `10 Tooling/lead-qualifier-suite/skills/personalization/SKILL.md` | move |
| `lead-qualifier-suite/skills/personalization/agents/openai.yaml` | `10 Tooling/lead-qualifier-suite/skills/personalization/agents/openai.yaml` | move |
| `lead-qualifier-suite/skills/personalization/references/personalization-spec.md` | `10 Tooling/lead-qualifier-suite/skills/personalization/references/personalization-spec.md` | move |
| `lead-qualifier-suite/skills/qualification/SKILL.md` | `10 Tooling/lead-qualifier-suite/skills/qualification/SKILL.md` | move |
| `lead-qualifier-suite/skills/qualification/agents/openai.yaml` | `10 Tooling/lead-qualifier-suite/skills/qualification/agents/openai.yaml` | move |
| `lead-qualifier-suite/skills/qualification/references/default-target-profile.md` | `10 Tooling/lead-qualifier-suite/skills/qualification/references/default-target-profile.md` | move |
| `one-pager-handoff/BUILD_GUIDE.md` | `10 Tooling/one-pager-handoff/BUILD_GUIDE.md` | move |
| `one-pager-handoff/CLAUDE.md` | `10 Tooling/one-pager-handoff/CLAUDE.md` | move |
| `one-pager-handoff/COPY_STANDARD.md` | `10 Tooling/one-pager-handoff/COPY_STANDARD.md` | move |
| `one-pager-handoff/diagnostic_doc_playbook.md` | `10 Tooling/one-pager-handoff/diagnostic_doc_playbook.md` | move |
| `one-pager-handoff/examples/DNA Skin Clinic - Revenue Diagnostic.html` | `10 Tooling/one-pager-handoff/examples/DNA Skin Clinic - Revenue Diagnostic.html` | move |
| `one-pager-handoff/examples/DNA Skin Clinic - Revenue Diagnostic.jpg` | `10 Tooling/one-pager-handoff/examples/DNA Skin Clinic - Revenue Diagnostic.jpg` | move |
| `one-pager-handoff/examples/DNA Skin Clinic - Revenue Diagnostic.pdf` | `10 Tooling/one-pager-handoff/examples/DNA Skin Clinic - Revenue Diagnostic.pdf` | move |
| `one-pager-handoff/examples/Dr. Dixit - Revenue Diagnostic.html` | `10 Tooling/one-pager-handoff/examples/Dr. Dixit - Revenue Diagnostic.html` | move |
| `one-pager-handoff/examples/Dr. Dixit - Revenue Diagnostic.jpg` | `10 Tooling/one-pager-handoff/examples/Dr. Dixit - Revenue Diagnostic.jpg` | move |
| `one-pager-handoff/examples/Dr. Dixit - Revenue Diagnostic.pdf` | `10 Tooling/one-pager-handoff/examples/Dr. Dixit - Revenue Diagnostic.pdf` | move |
| `one-pager-handoff/examples/Dr. Juvita Aesthetics - Revenue Diagnostic.html` | `10 Tooling/one-pager-handoff/examples/Dr. Juvita Aesthetics - Revenue Diagnostic.html` | move |
| `one-pager-handoff/examples/Dr. Juvita Aesthetics - Revenue Diagnostic.jpg` | `10 Tooling/one-pager-handoff/examples/Dr. Juvita Aesthetics - Revenue Diagnostic.jpg` | move |
| `one-pager-handoff/examples/Dr. Juvita Aesthetics - Revenue Diagnostic.pdf` | `10 Tooling/one-pager-handoff/examples/Dr. Juvita Aesthetics - Revenue Diagnostic.pdf` | move |
| `one-pager-handoff/examples/Dr. Swetha's Cosmoderm Centre - Revenue Diagnostic.html` | `10 Tooling/one-pager-handoff/examples/Dr. Swetha's Cosmoderm Centre - Revenue Diagnostic.html` | move |
| `one-pager-handoff/examples/Dr. Swetha's Cosmoderm Centre - Revenue Diagnostic.jpg` | `10 Tooling/one-pager-handoff/examples/Dr. Swetha's Cosmoderm Centre - Revenue Diagnostic.jpg` | move |
| `one-pager-handoff/examples/Dr. Swetha's Cosmoderm Centre - Revenue Diagnostic.pdf` | `10 Tooling/one-pager-handoff/examples/Dr. Swetha's Cosmoderm Centre - Revenue Diagnostic.pdf` | move |
| `one-pager-handoff/examples/Ministry of Skin - Revenue Diagnostic.html` | `10 Tooling/one-pager-handoff/examples/Ministry of Skin - Revenue Diagnostic.html` | move |
| `one-pager-handoff/examples/Ministry of Skin - Revenue Diagnostic.jpg` | `10 Tooling/one-pager-handoff/examples/Ministry of Skin - Revenue Diagnostic.jpg` | move |
| `one-pager-handoff/examples/Ministry of Skin - Revenue Diagnostic.pdf` | `10 Tooling/one-pager-handoff/examples/Ministry of Skin - Revenue Diagnostic.pdf` | move |
| `one-pager-handoff/examples/The Glow Clinic - Revenue Diagnostic.html` | `10 Tooling/one-pager-handoff/examples/The Glow Clinic - Revenue Diagnostic.html` | move |
| `one-pager-handoff/examples/The Glow Clinic - Revenue Diagnostic.jpg` | `10 Tooling/one-pager-handoff/examples/The Glow Clinic - Revenue Diagnostic.jpg` | move |
| `one-pager-handoff/examples/The Glow Clinic - Revenue Diagnostic.pdf` | `10 Tooling/one-pager-handoff/examples/The Glow Clinic - Revenue Diagnostic.pdf` | move |
| `one-pager-handoff/examples/Vtiara Hair & Skin Clinic - Revenue Diagnostic.html` | `10 Tooling/one-pager-handoff/examples/Vtiara Hair & Skin Clinic - Revenue Diagnostic.html` | move |
| `one-pager-handoff/examples/Vtiara Hair & Skin Clinic - Revenue Diagnostic.jpg` | `10 Tooling/one-pager-handoff/examples/Vtiara Hair & Skin Clinic - Revenue Diagnostic.jpg` | move |
| `one-pager-handoff/examples/Vtiara Hair & Skin Clinic - Revenue Diagnostic.pdf` | `10 Tooling/one-pager-handoff/examples/Vtiara Hair & Skin Clinic - Revenue Diagnostic.pdf` | move |
| `one-pager-handoff/wedge-signal-entry.md` | `10 Tooling/one-pager-handoff/wedge-signal-entry.md` | move |
| `Project-Hand-Off/00-START-HERE.md` | `11 Hand-Off/00 Start Here.md` | move |
| `Project-Hand-Off/01-STATE-OF-PLAY.md` | `11 Hand-Off/01 State of Play.md` | move |
| `Project-Hand-Off/02-BUYER-OFFER-AND-DEMO.md` | `11 Hand-Off/02 Buyer Offer and Demo.md` | move |
| `Project-Hand-Off/03-DRAFTING-ENGINE.md` | `11 Hand-Off/03 Drafting Engine.md` | flag-merge-candidate |
| `Project-Hand-Off/04-WEDGE-ROUTING.md` | `11 Hand-Off/04 Wedge Routing.md` | flag-merge-candidate |
| `Project-Hand-Off/05-CLINIC-INVENTORY.md` | `11 Hand-Off/05 Clinic Inventory.md` | flag-merge-candidate |
| `Project-Hand-Off/06-DECISIONS-AND-LEARNINGS.md` | `11 Hand-Off/06 Decisions and Learnings.md` | move |
| `Project-Hand-Off/PROJECT-INSTRUCTIONS-paste-this.txt` | `11 Hand-Off/PROJECT-INSTRUCTIONS-paste-this.txt` | move |
| `Project-Hand-Off/SETUP.md` | `11 Hand-Off/Setup.md` | move |
| `.DS_Store` | `99_Review/.DS_Store` | consolidate-duplicate |
| `Mystery_Shop_2026-08-15/.DS_Store` | `99_Review/Mystery_Shop_2026-08-15/.DS_Store` | consolidate-duplicate |
| `One-page-docs/.DS_Store` | `99_Review/One-page-docs/.DS_Store` | consolidate-duplicate |
| `Pre-outbound-research/.DS_Store` | `99_Review/Pre-outbound-research/.DS_Store` | consolidate-duplicate |
| `Pre-outbound-research/batch7/.DS_Store` | `99_Review/Pre-outbound-research/batch7/.DS_Store` | consolidate-duplicate |
| `Pre-outbound-research/batch7/mystery-shop-b7/.DS_Store` | `99_Review/Pre-outbound-research/batch7/mystery-shop-b7/.DS_Store` | consolidate-duplicate |
| `Proposals & SOW/.DS_Store` | `99_Review/Proposals & SOW/.DS_Store` | consolidate-duplicate |
| `Resources/.DS_Store` | `99_Review/Resources/.DS_Store` | consolidate-duplicate |
| `Resources/_source/aurilueur-proposal/out.pdf` | `99_Review/Resources/_source/aurilueur-proposal/out.pdf` | consolidate-duplicate |
| `Resources/_source/rua-proposal/rua-out.pdf` | `99_Review/Resources/_source/rua-proposal/rua-out.pdf` | consolidate-duplicate |
| `Resources/_source/rua-sow/rua-sow-out.pdf` | `99_Review/Resources/_source/rua-sow/rua-sow-out.pdf` | consolidate-duplicate |
| `Resources/_source/skinfit-proposal-v2/README.md` | `99_Review/Resources/_source/skinfit-proposal-v2/README.md` | consolidate-duplicate |
| `Resources/_source/skinfit-proposal-v2/out.pdf` | `99_Review/Resources/_source/skinfit-proposal-v2/out.pdf` | consolidate-duplicate |
| `lead-qualifier-suite/.DS_Store` | `99_Review/lead-qualifier-suite/.DS_Store` | consolidate-duplicate |
| `lead-qualifier-suite/skills/.DS_Store` | `99_Review/lead-qualifier-suite/skills/.DS_Store` | consolidate-duplicate |
| `lead-qualifier-suite/skills/gamma-deck/.DS_Store` | `99_Review/lead-qualifier-suite/skills/gamma-deck/.DS_Store` | consolidate-duplicate |
| `new_leads_1/Clinic_Directory_Template csv 3b771d3ba7f680e0b00acf18a11921d5_all.csv` | `99_Review/new_leads_1/Clinic_Directory_Template csv 3b771d3ba7f680e0b00acf18a11921d5_all.csv` | consolidate-duplicate |
