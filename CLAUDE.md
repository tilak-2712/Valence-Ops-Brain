# Valence Ops — Outbound & Sales

ValenceOps sells operations/revenue-automation to Indian elective clinics — skin, dermatology, cosmetology, hair-transplant, and dental — primarily in Bangalore. The product is not marketing/lead-gen; it's fixing what happens *after* an enquiry lands (response speed, qualification, follow-up, no-show recovery, reactivation).

**Team:** Tilak and Pratham split the clinic list between them (tracked per-clinic in Notion, see below).

**Read `MEMORY.md` in this same folder at the start of any work here** — it holds adaptive learnings, collaboration preferences, and open threads that this file doesn't repeat. Update it per the rule at the top of that file whenever something new is confirmed or superseded.

---

## How to work in this folder

This is the standing operating contract. It applies without being re-briefed.

1. **Push back before you produce.** If the ask contradicts a settled decision, rests on an unproven assumption, or is aimed at the wrong bottleneck, say so in one or two sentences first — then do the work. Silent compliance is the failure mode here, not over-caution.
2. **Correct the premise, not just the output.** If a request contains a wrong fact about this project, name the wrong fact and where the right one lives. Don't quietly work around it.
2b. **Nothing in this folder is scripture — including this file.** Whenever a claim is cited or sourced, from a document or from Tilak, check whether it is actually evidenced before building on it. If the sourcing is weak, say so with the reasoning. Two things this specifically means:
   - **Tilak's real-world feedback is reliable** — what a clinic replied, what a shop showed, what was sent. Take it as fact.
   - **His predictions, choices and framings are hypotheses** — which wedge will land, which clinic is worth the effort, what a test will prove. Pressure-test them; don't execute on faith. If he reaffirms after the pushback, it's his call — proceed in full.
   - Watch especially for a plan that conflicts with a rule recently adopted. Name the conflict specifically and show the arithmetic.
3. **Verdict first, then evidence.** Compressed answers. Tables over paragraphs. Push depth into a file rather than into the reply.
4. **Label the epistemic status of everything.** `confirmed` (real-world evidence exists) / `provisional` (designed, untested) / `hypothesis` (a guess). A provisional thing that has been used in the field is still provisional. Never let a provisional item quietly graduate.
5. **Never state to a clinic anything that isn't traced to a dated, verifiable fact** in that clinic's dossier. Anything marked *Potential / Possible / Unknown / ❓* is a thing to test, never a thing to say.
6. **Scale to the ask.** Large-scope requests (a full sequence across 20 clinics) are normal; execute at that scale rather than scoping down unprompted.
7. **Deliverables get saved to files**, not just shown in chat.

---

## Precedence — when two documents disagree

Higher wins. This ladder is the tiebreaker; it is not a reading order.

1. **`files/OUTBOUND_MEMORY.md` §3–§6** — banned phrases, tone, offer terms, decision log.
2. **`MEMORY.md`** (this folder) — cross-session calibration: no vague referents, felt-problem over research-recitation, Indian doctor-led framing over SaaS English.
3. **`wedge-signal-entry.md`** — disqualification, mystery-shop SOP, signal→wedge routing.
4. **`personalized-outbound-v2.md`** — structure, sequence, templates, self-check.
5. Everything else.

**The Notion tracker overrides all five on per-clinic state** (status, priority, owner). Check it before assuming a clinic's status from any document.

---

## Folder map

### Governing docs — read these, keep these current
| File | What it owns |
|---|---|
| `MEMORY.md` | Cross-session calibration, confirmed vs. provisional feedback, live project threads |
| `taste-n-judgement.md` | How Tilak judges work — copy, tone, design, evidence, commercials. The taste layer beneath the rules. **Standing rule: every feedback, conviction-driven change, pivot, new perspective or expression of taste goes into this file the same session, unprompted.** See its maintenance block for the full trigger list |
| `files/OUTBOUND_MEMORY.md` | Tripwires, hook rankings, banned phrases, tone, offer terms, decision log, update ritual |
| `wedge-signal-entry.md` | Disqualification framework, the 2-test mystery-shop SOP, signal→wedge routing table |
| `personalized-outbound-v2.md` | The drafting engine — buyer psychology, Three Threads sequence, templates, self-check |
| `SALES_MOTION.md` + `sales-motion/` | Everything after a positive reply: 5 stages, clocks, scripts, client-facing docs. **Designed, never run.** |
| `PROCESS-MAP.md` | The process as it actually runs, step by step, with automation judgments |
| `COHORT-INDEX.md` | Which clinic cohort is which, how many, what state each is in |

### Ledgers — the only things that turn hypothesis into evidence
| File | State as of 2026-08-13 |
|---|---|
| `files/SEND_LOG.csv` | **6 rows, all no-reply** (Cozmo Blis ×3, Glow Clinic ×3). Under-counts reality badly — see the tripwire note in `OUTBOUND_MEMORY.md` §1. |
| `files/REPLY_LOG.csv` | **2 rows, both open threads** (Sapphire, Aesthetica Veda). Zero calls held, zero pilots. |
| `files/LEARNINGS_LOG.md` | Dated tried → happened → changed entries |

### Audits — the correction layer. Read these before trusting any older doc.
| File | What it found |
|---|---|
| `files/OUTBOUND_SYSTEM_AUDIT.md` (22 Jul) | The pipeline terminated at research, not outreach. Source of the kill-filter, 4-touch sequence, reply-handling frameworks. |
| `ONE-PAGER-AUDIT-AND-TEST-PLAN.md` (5 Aug) | The one-pager wins attention and loses conversion: 25 sends → 2 replies → **0 calls**. Template convergence across all 15 docs. |
| `outbound-process-changes-2026-08-11.md` (11 Aug) | The only irreproducible step — the mystery shop — is the only one that never runs. Source of the published-hours rule and the 2-test shop. |

**These three are historical records of what was found, not live rulebooks.** Everything in them that became a rule now lives in the governing docs above. Where a proposal in them was rejected, the rejection is logged in `OUTBOUND_MEMORY.md` §6 — don't re-adopt it from the audit doc.

### Research — clinic facts, cite from here, never invent
- `Pre-outbound-research/` — the current dossiers. See `COHORT-INDEX.md` for which file covers which cohort.
- `Research-docs/`, `clinics/`, `se-bangalore-scrape/` — other cohorts, also indexed in `COHORT-INDEX.md`.
- `clinic-audit-checklist.md`, `clinic-research-sources.md` — the field schema and the source list.
- `.claude/skills/clinic-audit-research/SKILL.md` — the Apify research pipeline.

### Assets
- `One-page-docs/` — the 15 "Revenue Diagnostic" one-pagers, **sent cold as touch 2/3** (not, as this file previously claimed, only to clinics that replied positively). `diagnostic_doc_playbook.md` is the format doctrine.
- `one-pager-handoff/` — the self-contained build kit for whoever produces one-pagers. Contains frozen snapshot copies of `wedge-signal-entry.md` and `diagnostic_doc_playbook.md` — **edit the root originals, then re-sync the copies.**
- `Audit_call_docs/` — Stage-2/Stage-4 call and intake documents.
- `Pitch-decks/`, `valenceops_context_1.pdf`, `AI Readiness Workbook .pdf`, `revenue_os_discovery_audit_fillable.pdf` — reference material.

### `_archive/`
Retired duplicates and violations. **Never read from here when drafting.** See `_archive/README.md`.

---

## Notion is the outbound ledger. Read it at the start of any session that touches outbound state.

**Tilak does not report sends in this chat, and will not be asked to.** Every send, follow-up,
mystery-shop result and next-touch date lives in Notion. The repo holds research; Notion holds what
actually happened. **Notion overrides every file in this folder on per-clinic outbound state.**

Parent page **"Valence Leads tracker"** — `3a7da695-40e4-8052-8c3b-e8e33e5fd806`. Two child databases:

**Batch 1** · `collection://3a7da695-40e4-81b6-8648-000b3828bb89` · 19 rows
Send state is free text in `Status`: who got which touch on which channel, plus the *next* follow-up
date — e.g. *"Sent DM 3 to Praharsh / Sent Email 2 + doc to Karan Singh / Follow up 5 — 7/8/26."*
Other fields: City, Contact, Founder, Point-of-contact, Priority, Specialty, Website.

**Batch 2** · `collection://754da695-40e4-839a-a0e7-07e28a0a27d8` · 12 rows
Richer and far more useful. Adds **`DM status`**, **`Mystery shop status`** (Wedge confirmed / Test
running / Retest needed / Pending review), **`Wedge`**, **`Notes`**.
The `Wedge` and `Notes` fields carry **full mystery-shop transcripts, timestamps, framing lines and
next actions** — the richest outbound evidence in the entire project, and none of it is in the repo.
Read them before drafting anything for a Batch-2 clinic.

### Two rules that follow from this

1. **Repo presence ≠ contacted.** All clinic research gets dumped here, including leads neither Tilak
   nor Pratham will ever contact, because it's useful raw material. A clinic with a dossier but no
   Notion row has **not** been shopped and **not** been messaged. It is parked inventory for a future
   batch — not a backlog, not neglected work. Don't count it in any denominator.
2. **Never compute rates from `files/SEND_LOG.csv`.** It is a frozen 6-row historical fragment that
   captures a small fraction of what has been sent. Counts come from Notion.

---

## Drafting outbound copy — order of operations

1. Pull the clinic's row from the Notion tracker (owner, priority, contact channels).
2. Read that clinic's dossier — find it via `COHORT-INDEX.md`.
3. Diagnose the wedge via `wedge-signal-entry.md` §3 — cite the evidence, don't default.
4. **Run the rebuttal test** (`wedge-signal-entry.md` §0.1): write the one sentence the doctor says back. If a plausible rebuttal exists, the hook doesn't ship.
5. Draft per `personalized-outbound-v2.md`, with `files/OUTBOUND_MEMORY.md` §3–§5 as the override layer.
6. Check `MEMORY.md` for standing calibration before finalizing tone and structure.
7. Report notable outcomes only — a reply, a clear win, a clear flop — per `OUTBOUND_MEMORY.md` §7. Per-send logging is explicitly not expected.

## Before starting a new batch — the two standing blocks

Both predate this audit and both are still unmet. State them if a new batch is requested.

- **`SALES_MOTION.md` §7:** do not send another Day-0 batch until the walkthrough video and the How We Work PDF exist as files.
- **`OUTBOUND_MEMORY.md` §6 (2026-08-04):** a warm reply outranks the send quota. Sapphire and Aesthetica Veda are both open.
