---
date_created: 2026-08-13
date_modified: 2026-08-13
status: active
---
# Valence Ops — The Outbound Process As It Actually Runs Today

Reconstructed from the files in this folder (Aug 2026). This is a description of the current
process, not a proposal. Written as the input document for the n8n automation discussion.

> **Updated 2026-08-13** after the folder self-audit. Phase C1 (mystery shop) and Phase G2 (ledgers)
> changed materially. Where this file and `wedge-signal-entry.md` / `files/OUTBOUND_MEMORY.md`
> disagree, those two win — this is a map, not a rulebook.

Each step lists: **what happens → who does it → what it costs → what it produces**.
The `AUTOMATABLE` tag at the end of each step is a first-pass judgment only — argue with it.

---

## PHASE A — SOURCING (cold list → shortlist)

### A1. Define the vertical criteria
- Write/adjust a criteria doc before scraping anything (`Apify Discovery Context.md` for aesthetic,
  `Dental Discovery Criteria.md` for dental).
- Contains: verticals in/out, corporate-chain auto-exclude, hard kills, IG gate, geography
  (Bangalore micro-markets), and the **exclusion list** of every clinic already in the pipeline
  (§4 — ~150 names across 6 cohorts).
- Human judgment, done once per vertical. **AUTOMATABLE: no.**

### A2. Preflight the scrape
- Check Apify credit (`/v2/users/me/limits`), `fetch-actor-details` on every actor in the roster,
  estimate cost per phase, set `maxTotalChargeUsd` on every call.
- Report the plan and wait for go-ahead before spending.
- ~10 min, mechanical. **AUTOMATABLE: yes — this is a fixed checklist.**

### A3. Discovery scrape (cap ~$1.10)
- `compass/crawler-google-places`, `maxReviews: 0`, metadata only, 4–6 search terms per call,
  rotated across micro-markets. Target 250–350 raw records.
- **AUTOMATABLE: yes.**

### A4. Gate A — hard kills
- Kill in a fixed order: exclusion-list match → pediatric-only → not an independent clinic →
  mixed vertical → reviews < 20 → chain (6+ branches / corporate parent) → geo mismatch →
  no website AND no IG AND no GBP contact.
- Then tier (TIER-1 = name/category contains implant, aligner, smile design, etc.).
- Deterministic rules on scraped fields. **AUTOMATABLE: yes — near-fully.**

### A5. Gate B/C/D — the expensive gates
- **IG gate** (`instagram-profile-scraper`): is there a live account, is it posting, is there a
  personal founder account or only a brand page.
- **Procedure gate** (`website-content-crawler`): does the high-ticket work actually exist.
- **Demand gate** (Google Ads Transparency + Facebook Ads): is anyone paying for enquiries.
- **AUTOMATABLE: yes for the fetch; the pass/fail judgment on ambiguous cases is currently LLM work.**

### A6. Verification loop — after EVERY actor call
- `status: Succeeded` is not evidence. Check items-returned vs. submitted, read `statusMessage`,
  look for a separate errors key, spot-check field completeness, cross-corroborate.
- This exists because a Maps enrichment actor silently returned 0 items after a mid-run rate-limit
  (`MEMORY.md` §2).
- **AUTOMATABLE: yes — and it should be, since it's the step most likely to get skipped by a human.**

### A7. Output the shortlist
- A CSV with a fixed column contract + a `go-list` split by route: full-IG route / thin-IG route /
  non-IG (WhatsApp-phone-website only) route.
- Current live examples: `IG Pregate 40 Clinics.md` → `go-list-mystery-shop.md`.
- **AUTOMATABLE: yes (formatting), no (the route call on edge cases).**

---

## PHASE B — RESEARCH (shortlist → dossier)

### B1. Decision-maker discovery — Gate E
- Contact ladder: GBP → website team page → Practo doctor listing → LinkedIn → IG contact graph.
- Every contact gets a **confidence label**; front-desk numbers are marked as such, not passed off
  as the founder's WhatsApp (this has bitten — see `MEMORY.md` §5, Clinic Next Face).
- **AUTOMATABLE: partly. The ladder is mechanical; "is this the founder's personal account" is not.**

### B2. Review analysis — Gate F
- Not the aggregate rating. Read a spread — recent and older, positive and negative — and report
  **patterns and quotable lines**, because a direct patient quote is what makes a hook credible.
- **AUTOMATABLE: the fetch yes; the reading is the point and is LLM/human work.**

### B3. Write the dossier
- Fixed schema: Basic Info → ICP Qualification → Digital Presence → Ads → Lead Sources →
  Mystery Shop → Reviews → Marketing Analysis → `funnel_break_stage` + `recommended_entry_sku`.
- Goes to `Pre-outbound-research/`. This is the source of truth — nothing gets invented later.
- **AUTOMATABLE: assembly yes, analysis no.**

### B4. Depth decision (a live tension, not a settled step)
- 2026-07-22 decision: **≤10-min light research for Day 0, full audit only after a reply signal.**
  Reason: 45–90 min/prospect produced 20 dossiers and 0 sends.
- In practice the deep dossiers still get built up front. Worth naming this in the discussion —
  it's the single biggest time sink in the whole process.

---

## PHASE C — DIAGNOSIS (dossier → wedge)

### C1. Mystery shop — **now runs FIRST, at the top of the batch** *(changed 2026-08-13)*
- Tilak does this personally. **Never automated, never delegated, never fake-sent by an agent.**
- **Admissible only if the enquiry lands inside the hours the clinic publishes on its own Google
  profile.** Replaces the old "Tue–Thu 11am–4pm" window, which excluded Saturday (92% published-open,
  the best slot in the dataset) while permitting tests on split-shift closed time.
- **Two tests**, both firing from a single message: qualification · quote decay. Persistence,
  after-hours, cross-channel and booking friction are retired — see `wedge-signal-entry.md` §2.2.
- **The screenshot is the deliverable**, not the prose summary.
- 24–72h wall-clock dependency — which is *why* it opens the batch. Monday: ~20 shops in one
  40-minute sitting. Tue–Thu: research only the threads that came back interesting.
- **AUTOMATABLE: no. But the *scheduling, reminding, and logging* of it is.**

### C2. Route the signal to a wedge
- `wedge-signal-entry.md` §3: a lookup table from signal combination → entry wedge → opening frame
  → priority. E.g. `ads ✓ + fast reply + no qualification` → follow-up/nurture engine.
- Rule when several breaks exist: earliest provable break wins, and it must be
  screenshot-provable / closest to money already spent / fastest to show a visible win.
- **AUTOMATABLE: the table lookup is literally a routing table. The evidence judgment behind it isn't.**

### C3. Evidence admissibility check
- Every claim must trace to a dated mystery-shop result, a direct review quote, or a confirmed
  ad/digital-presence fact. Anything marked "Potential," "Possible," "Unknown," or "❓" in the
  research is a hypothesis to test — **never** something to say to the clinic.
- This rule exists because a whole 3-message sequence for Dr. Dixit got built on a boilerplate
  "Potential Missing Layers" template line and had to be discarded.
- **AUTOMATABLE: as a check, yes — a claim→source validator is a real n8n/Claude Code job.**

---

## PHASE D — DRAFTING (wedge → messages)

### D1. Load the rules stack, in precedence order
1. `files/OUTBOUND_MEMORY.md` §3–§5 (banned phrases, tone, offer framing) — **overrides everything**
2. `personalized-outbound-v2.md` (structure, Three Threads, templates)
3. `MEMORY.md` (cross-session calibration: no vague referents, felt-problem not research-recitation,
   Indian doctor-led framing not SaaS English)

### D2. Draft the Three Threads sequence per clinic
- **Day 0 DM**: hook → identity (1 line) → tiny ask. 30–125 words. No pitch.
- Branches: positive reply → video → WhatsApp bridge → pilot offer → call/coffee.
  Silence → one bump at Day 2–3. Decline → accept cleanly, zero push.
- Cadence override: **4 touches / 2 channels** (IG ×2 → WhatsApp ×2), then park 60–90 days.
- Assign a deliberate **opening archetype** per clinic (7 named archetypes) — because 4 parallel
  agents with identical prompts converged on the same opening skeleton for 11/19 DMs.

### D3. Self-check before anything is shown
- Banned vocabulary sweep (leads, funnel, pipeline, conversion, ROI, growth, scale your practice…).
- No guaranteed patient numbers, ever. No fabricated case studies — none exist.
- CTA must be strictly diagnostic ("the one thing I'd check first"), never a promised fix.
- Does every claim trace to a fact? Does the CTA connect to the hook? *(This one has failed in
  the field — Glow Clinic's hook was DM speed, the ask was about no-shows.)*
- **AUTOMATABLE: the banned-phrase and CTA-link checks are pure lint. The voice is not.**

### D4. Save the drafts to a file
- Every batch goes to a markdown file in the folder, not just chat.

---

## PHASE E — SENDING

### E1. Pull the row from Notion ("Valence Ops Leads Tracker")
- Owner (Tilak/Pratham), priority, status, contact channels. This is authoritative — check it
  before assuming a clinic's status from anywhere else.

### E2. Send manually
- IG DM / WhatsApp / email, from a personal account, founder-to-founder.
- **Not automated by policy** — a personal-account send is the whole premise of the sequence.

### E3. Touch 2 — the diagnostic one-pager
- A designed PDF/PNG ("[Clinic] — Revenue Diagnostic") built per `diagnostic_doc_playbook.md`.
- Currently the most effort-intensive asset in the whole system, and it ships **cold**.
- Known problems, already audited in `ONE-PAGER-AUDIT-AND-TEST-PLAN.md`: template convergence
  across the 15 docs, every doc ~2× its own spec, the CTA gives away the thing it's asking for.

### E4. Update Notion + log
- Status change per clinic, per touch.
- **AUTOMATABLE: yes, and this is probably the highest-ratio automation in the list.**

---

## PHASE F — AFTER A REPLY (`SALES_MOTION.md`)

Five stages, each with a clock and a named owner:

| # | Stage | Clock | Exit |
|---|---|---|---|
| 0 | Reply triage | ≤4 business hours | Reply sent + call slot proposed |
| 1 | Credibility packet | ≤24h | Packet delivered + call booked with a date |
| 2 | Operations call (50 min) | ≤5 days | Diagnosis captured, next-step date stated live |
| 3 | Findings + rollout doc | 48–72h after call | Doc sent + 20-min decision call booked |
| 4 | Pilot + onboarding | Kickoff ≤7 days after yes | Setup done, visible artifact live by day 3 |

Three governing rules:
1. **Nothing ships without a date attached** — every asset travels with a booked time or two slots.
2. **Diagnosis and prescription never happen in the same conversation.**
3. **A warm reply outranks the send quota** — 3+ live conversations pauses new Day-0 sends.

⚠️ This whole phase is **designed but never run** — zero conversations have gone through it.
And the build order says: *do not send another Day-0 batch until the 6-minute walkthrough video
and the How We Work PDF exist as files.*

---

## PHASE G — LEARNING LOOP

### G1. Outcome reporting (irregular by design)
- Tilak reports only when something is notable — a reply, a clear win, a clear flop. Not per send.
  Format: `clinic | touch # | outcome | their exact words | anything odd`.

### G2. Ledgers *(schema changed 2026-08-13)*
- `files/SEND_LOG.csv` — **6 columns** (`date,clinic,channel,touch_num,outcome,notes`), 6 rows, all
  no-reply. `subtype`, `hook_category`, `opening_archetype`, `personalization_depth` and `send_time`
  were dropped: at 40–65 lifetime touches they collect data that cannot answer anything, which is
  why they went unfilled. Prior values were preserved into `notes`.
- `files/REPLY_LOG.csv` — **2 rows, both open threads** (Sapphire, Aesthetica Veda).
- `files/LEARNINGS_LOG.md` — dated tried → happened → changed entries.
- **The logged 6 badly under-counts reality** — ~25 clinics received a one-pager as touch 2/3.

### G3. Weekly review (20 min, fixed agenda)
The four numbers (touches · replies · **calls held** · pilots) → where conversations died
(`stage_lost_at`) → exactly one experiment, and only one that could plausibly *triple* the rate
(format, offer, or asset type — never a sentence) → **tripwire check, unskippable.**
*The old agenda's "kill the weakest hook category / double the best" steps are cut: they needed ≥8
sends per category to return a verdict, which never happened, so they could never legally run.*

### G4. The tripwires — **neither was being counted**
- **100 touches OR 45 days from first send with zero pilots** → the clinics-only bet gets re-examined.
  As of 2026-08-13: **≈19 / 45 days, ≈40–65 / 100 touches, 0 pilots.** The counter had never been
  filled in once since it was installed on 2026-07-22.
- **3 clinics reach the operations call and none reach a pilot** → the problem is the offer or the
  call, stop tuning DMs. Currently **0 of 3** — no clinic has reached an operations call.

---

## WHERE THE WORK ACTUALLY IS

Ranked by manual hours consumed, for the automation conversation:

1. **Research dossier writing (B3)** — biggest sink. Already has a decision against it (≤10 min
   light research) that isn't being followed.
2. **Diagnostic one-pager production (E3)** — most effort per asset, ships cold, audit says it's
   converging on a template anyway.
3. **Drafting + self-check (D2/D3)** — the part that must stay high-quality, but half of the
   self-check is mechanical lint.
4. **Notion status upkeep + logging (E4/G2)** — low skill, high frequency, and it's the step that
   silently doesn't happen (REPLY_LOG is empty).
5. **Scrape → gate → verify (A3–A6)** — already scripted in prose; deterministic enough to run
   unattended with a cost cap.

## WHAT MUST NOT BE AUTOMATED

Stated explicitly in the docs, not up for debate without a decision entry:

- **Mystery shops** — Tilak runs them personally. No agent ever sends a test DM to a clinic.
- **The actual send** — personal account, founder-to-founder, is the premise.
- **Any claim that isn't traced to a verified fact** — the whole system's credibility rests on this.
- **Reply handling inside 4 business hours** — ValenceOps sells speed-to-lead; being slow to a warm
  clinic is a live demonstration of failing at the product.
