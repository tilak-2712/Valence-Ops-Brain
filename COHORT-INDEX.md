# Cohort Index — every clinic cohort, where it lives, what state it's in

*Created 2026-08-13 during the folder self-audit. There was no index before this: eight cohorts had
accumulated across six folders with inconsistent naming (a `batch7/` with no batch 4, 5 or 6), and
the only way to find a clinic's dossier was to grep. Keep this current — a new cohort without a row
here is a cohort that will be re-scraped by accident.*

**The exclusion list lives in `Apify Discovery Context.md` §4.** Check it before any new scrape.

---

## The eight cohorts

| # | Cohort | Where | Clinics | Shopped? | State |
|---|---|---|---|---|---|
| 1 | **Batch 1 — the Notion cohort** | `05 Prospects/Batch 1 Notion Cohort/Outreach 1.md`, `Outreach 2.md`, `Outreach 3.md`, `Outreach 4.md`, `Outreach 5.md` | ~28 tracked, ~40 dossiers written | Partly — and several shops are inadmissible | **LIVE.** The only cohort in the Notion tracker. All 6 logged sends came from here. Sent through clinic 15 (Karishma). |
| 2 | **Karnataka batches 1–2** | `05 Prospects/Karnataka Batches 1-2/Karnataka Batches 1-2 Audit 23 Clinics.md` | 23 | No — PENDING on all 23 | Audited 23–24 Jul. No outbound. |
| 3 | **Batch 3 — aesthetic** | `05 Prospects/Batch 3 Aesthetic and Dental/batch3-aesthetic-MASTER.md` | 10 clinics / 16 locations | No | Source of truth for this sub-batch. Superseded draft archived. |
| 4 | **Batch 3 — dental** | `05 Prospects/Batch 3 Aesthetic and Dental/Batch 3 Dental Audit.md` | 11 clinics / 14 locations | No | Compiled 30 Jul, Standard depth, partial. |
| 5 | **Batch 3 — remainder** | `05 Prospects/Batch 3 Remainder/` (`00 Batch 3 Remainder Full Report.md` + 10 dossiers) | 10 of 11 | No | Executed output of `Handoff Batch 3 Remaining 8.md`. **Aisri Cosmetic Clinic and SkinRx Clinix from that handoff have no dossier — verify whether they were dropped deliberately.** 3 of these are outside Karnataka (Navi Mumbai, Warangal, Hyderabad). |
| 6 | **Batch 7 → tracked in Notion as "Batch 2"** | `05 Prospects/Batch 7 (Notion Batch 2)/` (15 dossiers) + `go-list-mystery-shop.md` + both findings docs. **Live state: Notion `collection://754da695-40e4-839a-a0e7-07e28a0a27d8`** | 25 dossiers; **12 in Notion** | **Yes — 12 shopped 10–11/8/26** | **LIVE and the most advanced cohort in the project.** 5 wedges confirmed · 2 silence clocks running (Krity 360, Theory of Skin — do not message) · 4 retest-needed · 1 pending screenshot review · DM-1 sent at 7 clinics. **The repo dossiers do not contain any of this** — the shop transcripts, wedges and next actions live only in Notion's `Wedge` and `Notes` fields. |
| 7 | **The `clinics/` cohort** | `clinics/` (13 dossiers + `rejected-candidates.md` + `master-scrape-log.csv`) | 13 | Mixed | Scraped 19 Jul. Non-overlapping with Batch 1 except `evenly-skin-and-hair-clinic.md`. |
| 8 | **SE Bangalore scrape** | `se-bangalore-scrape/NEW-CLINICS-TABLE.md` + `raw/*.json` + `Session 2026-08-10 SE Bangalore Scrape.md` | 52 core new targets, from 251 raw records | No | **Raw targets only** — no dossiers, no contact work. Sarjapur Rd and Bommanahalli are under-covered (37 and 4 raw records); their re-runs died with the Apify budget. |

Also present: `IG Pregate 40 Clinics.md` (an IG screen over 40 names, 8 Aug — the gate that produced cohort 6's go-list) and `LinkedIn Sales Navigator Personas.md` (persona definitions, not a cohort).

---

## How to read this index

**Notion membership is the line.** A cohort with rows in the "Valence Leads tracker" is being worked
— that's cohort 1 (Notion "Batch 1", 19 rows) and cohort 6 (Notion "Batch 2", 12 rows), ~31 clinics.
Everything else is **parked inventory**: scraped deliberately, never started, waiting for Tilak to call
it up for a future batch.

**This is not a backlog and not sprawl.** *(Corrected by Tilak 2026-08-13 — an earlier version of this
section framed the parked cohorts as evidence of sourcing bias. Retracted.)* Nothing on those clinics
was begun and abandoned. Don't count them in a conversion denominator, don't propose triaging them
unprompted, and don't describe them as work owed.

The Aug-11 §4 point still holds in its narrow form: don't fire a *new* scrape while a clinic sits at
"replied, no call booked." Two do right now.

---

## Open questions on this index

1. **Batch numbering.** There is no batch 4, 5 or 6, and the cohort the repo calls `batch7/` is
   "Batch 2" in Notion. Worth aligning the names — two systems disagreeing on which batch is which is
   how the "zero mystery shops" error happened.
2. **Cohort 5's two missing dossiers** — Aisri and SkinRx were items 9 and 11 in the handoff and have
   no output in `05 Prospects/Batch 3 Remainder/`.
3. **Sapphire has no Notion row**, despite being the warmest thread in the project's history. It is
   tracked only in `files/REPLY_LOG.csv` and `Meeting Brief Sapphire 2026-08-13.md`.
4. **The batch-7 repo dossiers are now behind Notion.** Twelve of them have shop transcripts, confirmed
   wedges and framing lines that exist only in Notion's `Wedge` / `Notes` fields. Either backfill them
   into the dossiers or accept that for this cohort the dossier is the *pre-shop* record and Notion is
   the current one — and say so where drafting reads from.
