# Outbound process — proposed changes

> ## 📕 HISTORICAL RECORD — resolved 2026-08-13. Do not draft or decide from this file.
> **Adopted in full and now canon:** §1.3 rebuttal column · §1.4 evidence bar · §2.1 shop opens the
> batch · §2.2 two-test shop · §2.3 save the screenshot · §2.4 kill founder-unidentifiable clinics at
> Gate A · §2.5 four-number ledger · §3.5 published-hours admissibility · §4's stop-list. They live in
> `wedge-signal-entry.md` and `files/OUTBOUND_MEMORY.md` §3/§6 now.
>
> **§5's open question — "what happened with Sapphire and Aesthetica Veda?" — is answered:** both
> threads are still open and unworked as of 2026-08-13. A Sapphire meeting was prepped for that date
> and is being rescheduled. Both are now rows in `files/REPLY_LOG.csv`, and both still outrank every
> change in this document, exactly as it said.
>
> **Two claims in here are now out of date.** §1.1/§1.2 say the WhatsApp demo is "still unbuilt" —
> **it was built and confirmed live on 2026-08-13** (qualification + booking; no-show/quote-chase/
> reactivation are shown as message sequences, see `OUTBOUND_MEMORY.md` §5b). And §0's "0 mystery
> shops" was true of the repo but false of reality — 12 of that cohort were shopped 10–11 Aug, recorded
> in Notion Batch 2.
>
> **§4's inventory warning does NOT apply to the existing parked cohorts.** Tilak confirmed 2026-08-13
> that everything outside Notion was scraped and deliberately parked as candidate inventory for a
> future batch — never started, so not neglected. The warning holds only in its narrow form: don't fire
> a *new* scrape while a clinic sits at "replied, no call booked."
>
> **The one thing still genuinely open:** the free-pilot / paid-implementation boundary in the offer —
> see `files/OUTBOUND_MEMORY.md` §5. `COHORT-INDEX.md` maps every cohort and which are actually live.

*Drafted 2026-08-11. Reviewed against `PROCESS-MAP.md`, `MEMORY.md`, `files/OUTBOUND_MEMORY.md`, `files/OUTBOUND_SYSTEM_AUDIT.md`, `ONE-PAGER-AUDIT-AND-TEST-PLAN.md`, `wedge-signal-entry.md`, both ledgers, and the batch-7 findings docs. Nothing here is a send-blocker; it is a set of changes to argue with.*

---

## 0 · The observation everything else follows from

**The only step that produces evidence a competitor cannot reproduce is the only step that never runs.**

Batch 7: 25 full dossiers in `Pre-outbound-research/batch7/`, **0 mystery shops** — both findings docs say so explicitly, and every wedge tag in them is marked provisional. Five days after the Aug-5 one-pager audit concluded that working the two warm threads was "worth more than 40 new sends," 52 more clinics were scraped.

Scraping, dossier-writing and one-pagers are all reproducible by anyone with Apify and a Claude subscription. A timestamped thread where *you* asked their front desk for a hair transplant price and nobody chased it is not. Every hour is going into the reproducible half.

---

## 1 · Changes that should move conversion

### 1.1 Stop asking doctors for calls
25 one-pagers → 2 replies → 0 calls held. Every asset terminates in a 20–30 minute call or a free audit. A call is the most expensive thing you can ask a clinical doctor for — a block of a day already booked with patients.

Two asks that cost them nothing:
- *"Here's a number — message it the way a patient would."* ~~The WhatsApp demo has been the top item in `SALES_MOTION.md` §3 since 2026-08-04 and is still unbuilt while 25 documents shipped.~~ **✅ Built 2026-08-13** — qualification + booking are live and testable; no-show/quote-chase/reactivation are shown as message sequences (`OUTBOUND_MEMORY.md` §5b).
- *"I'm around Indiranagar Thursday — happy to swing by for ten minutes."* ~~`OUTBOUND_MEMORY.md` §4 already records that the in-person offer converts unusually well with clinic owners.~~ **Correction 2026-08-13: §4 recorded that as a "learning" but it never was one — zero meetings and zero calls have been held.** The drop-in-first ask is still the right call on reasoning alone; it is not an evidenced pattern, and this recommendation rested on treating it as one. It appears in none of the one-pagers.

A call is a second-touch ask. It is currently the first one.

### 1.2 Point the mystery shop at the demo, not just the diagnosis
Every asset sent proves a problem exists. Nothing sent shows a fix working. The bridge is nearly free: take the actual shop thread and replay it — same enquiry, answered the way the system would answer it, on a number they can message themselves. Built once per subtype (skin / hair transplant / dental), not once per clinic; the shop transcript is what makes it theirs.

### 1.3 Add a rebuttal column to every candidate hook
One sentence: *what does the doctor say back?* This generalizes the midnight-shop lesson already paid for.

| Hook | Rebuttal | Verdict |
|---|---|---|
| "Your IG DM took an hour" | *We answer on WhatsApp.* | Kill |
| "You run 25 ads" | *And?* | Kill |
| "A 1★ from January" | *That patient was difficult.* | Kill |
| "89 one-star reviews, 0 owner replies" (Derma Solutions) | — | Ship |
| "Priced a transplant Tue 2pm, went quiet, nobody chased in 9 days" | — | Ship |

If a plausible one-sentence rebuttal exists, the hook doesn't ship. This kills most of what the dossiers currently surface — that is the point.

### 1.4 Raise the evidence bar: first-party test, OR ≥2 independent instances
The strongest batch-7 findings are patterns, not incidents — Dr. Priya's booking friction across multiple independent reviewers, Derma Solutions' 7.2% one-star rate, VIDA's three reviewers on pricing pressure. Single-incident review quotes get argued with.

Related: the caveat in `findings-batch-11-15.md` — samples of 5–8 on Google's *relevance* sort — means "no complaints found" is currently worthless. Pull chronological, 25+, report negatives per 100 rather than quoting one.

---

## 2 · Changes that should cut hours

### 2.1 Fire the mystery shop first, not last
It is the only 24–72h async dependency in the process and it is scheduled after the most expensive step. Queue rule: async dependencies open the batch.

- **Monday:** 20 shops in one 40-minute sitting.
- **Tue–Thu:** research only the clinics whose threads came back interesting.

Flips 25 dossiers / 0 shops into ~20 shops / ~6 dossiers, and the six get written for clinics where you hold evidence nobody else has. Also structurally enforces the ≤10-min research decision of 2026-07-22 that `PROCESS-MAP.md` B4 admits isn't being followed — you cannot over-research a clinic you haven't shopped.

### 2.2 Cut the shop from six tests to two
Run **#1 Qualification** and **#3 Quote decay** only — both fire inside a single thread from one message.

- #4 after-hours — see §3 below.
- #5 cross-channel — ruled a weak wedge in `MEMORY.md` §2 (WhatsApp is the channel that matters).
- #2 persistence — 7–14 days, and mostly tells you what quote decay tells you sooner.
- #6 booking friction — requires actually booking; expensive, and burns the test identity.

On a ₹49,999–₹1.5L procedure, an unchased quote is the most expensive silence you can prove, and it costs one message plus silence.

> ⚠️ Departs from `wedge-signal-entry.md` §2's six-test SOP. Flagged, not slipped in.

### 2.3 Save the screenshot, not the summary
Every doc says hooks must be "screenshot-provable," but no step actually saves a screenshot. Shop results live as prose inside dossiers, so at drafting time the evidence exists only as a paraphrase — which is how a "Potential Missing Layers" template line once became Dr. Dixit's entire wedge.

Make the timestamped image the deliverable of the shop (`clinic-YYYYMMDD-test.png`); prose is derived from it, never the reverse. It is also the raw footage for the video arm.

### 2.4 Kill founder-unidentifiable clinics at Gate A
Project Skin got a complete dossier and was then blocked with "no founder found anywhere — no personalization possible." Dermatonik and Haircosmos have no doctor named anywhere either. That is a two-minute check sitting *after* the most expensive step.

"One named decision-maker reachable on a personal channel" belongs next to reachability in the kill-filter. On batch-7 evidence: 3 of 10 dossiers not written.

### 2.5 Shrink the ledgers instead of expanding them
`SEND_LOG.csv` has 11 columns and 6 rows; `REPLY_LOG.csv` has 13 columns and 0. The Aug-5 audit's own math says a copy-level A/B needs several hundred sends per arm — so `hook_category`, `opening_archetype` and `personalization_depth` collect data that cannot answer anything at 40–65 touches, which is part of why they never get filled.

Track four numbers, derived from the Notion status changes already being made by hand: **touches sent · replies · calls held · pilots.** Keep archetype assignment in the draft files as a craft discipline, not as a metric.

> ⚠️ Departs from the fixed schema in `OUTBOUND_MEMORY.md` §7.

---

## 3 · The mystery-shop window: after-hours and weekends

### 3.1 The data
`se-bangalore-scrape/raw/*.json` already carries `openingHours` (and an unused `popularTimesHistogram`) on all 251 records. Across the **171 aesthetic/derm clinics** in that scrape:

| Slot | Published open |
|---|---|
| **Saturday 6pm** | **92%** |
| Tuesday 11am | 89% |
| Tuesday 6pm | 88% |
| Saturday 4pm | 86% |
| Saturday 2pm | 80% |
| **Tuesday 2pm** | **78%** |
| Sunday noon | 70% |
| Sunday 4pm | 65% |
| Tuesday 8pm | 32% |

**220 of 223** clinics with hours are open Saturday. **158 of 223** are open Sunday.

*Caveats:* these are published hours, not verified staffing — but that cuts in favour of the test, since the published hours are the clinic's own claim. Sample is the SE Bangalore scrape (HSR / E-City / Sarjapur / Bommanahalli / Bannerghatta), keyword-filtered to aesthetic/derm, not the exact outreach cohort. Hours can be checked per clinic before shopping, since the field is already captured.

### 3.2 Weekend is not after-hours in this market
Treating it as after-hours is factually wrong for roughly two-thirds of the target set. Saturday 6pm is the highest-open slot in the dataset, it is when the patient buying a ₹1.5L transplant actually has time to enquire, and it is when the desk is thinnest. A Saturday enquiry ignored inside published hours has no rebuttal available. **Reclassify Saturday (and Sunday, for the 65–70% who publish it) as prime shopping time.**

### 3.3 Genuine after-hours (weekday 9pm–8am) — drop as a hook source
1. **The rebuttal is correct.** "We were closed" is true. Leading with it signals you don't understand how a clinic runs.
2. **No discriminating power.** `OUTBOUND_MEMORY.md` §2: *"Late-night enquiries die everywhere."* A test every clinic fails ranks nothing — the defect that retired the ICP score on 2026-07-22.
3. **Its output is already banned** (§3 midnight-shop ban). Running a test whose findings are inadmissible is paying for unusable data.
4. **Costs a test identity and a wall-clock day** to confirm something already known.

### 3.4 Three carve-outs to keep
**(a) The auto-reply text — an observation, not a test.** What matters is whether the automation *asks anything* or just promises a callback (the capture-window reframe, `MEMORY.md` §3, 2026-08-01). One message, one screenshot, no going silent, no 72-hour clock. Still marked PROVISIONAL, first used on Ministry of Skin, no reply recorded — unproven, so not load-bearing.

**(b) Sunday**, for the 65–70% who publish Sunday hours. For the rest it is a no-test.

**(c) True after-hours, confirmed heavy ad-spenders only, touch-2 material only.** Not framed as slowness — framed as spend against staffing, on two verified facts and no invented third: *"your hair ad has run since 24 July"* (Ad Library, dated) + *"I asked about it at 10:40pm Tuesday, first human reply Wednesday 11:15am"* (first-party, dated). The doctor does the arithmetic. Structural-inevitability per `MEMORY.md` §2. Only worth the identity cost on someone like Akera (25 Meta + 29 Google simultaneously).

### 3.5 The rule change
Replace **"Tue–Thu, 11am–4pm"** with:

> **An enquiry is admissible as a hook if it lands inside the hours the clinic publishes on its own Google profile.**

Broader and stricter at once:
- Kills midnight permanently, without a separate ban.
- Opens Saturday, Sunday, and weekday evenings — Tue 6pm (88%) beats Tue 2pm (78%).
- **Kills tests the current window permits.** A large share of these clinics run split shifts (`10 AM to 1 PM, 4:30 to 8:30 PM`); the 11–4 window sits on top of the midday gap. Some existing "business-hours no reply" findings may be on published-closed time and are rebuttable — re-check before any ship.
- Costs nothing to apply: the hours are already scraped.

**Bonus, free:** `popularTimesHistogram` is unused. The sharpest shop slot is not their busiest hour — an ignored enquiry at peak invites *"we were slammed."* It is a **published-open, low-traffic hour**. Nothing to explain there.

---

## 4 · What to stop

- **New scraping, while any clinic sits at "replied, no call booked."** ~150 clinics across six cohorts, 52 more added 2026-08-10, 0 pilots. There is a tripwire on touches and none on inventory. Sourcing is the most legible work in this process and has never been the constraint — which is what makes it the thing that gets done.
- **Identical text to multiple people at one clinic.** `SEND_LOG.csv` shows the same message to all three Glow Clinic POCs on 28/7. In a market where they compare notes, that is a self-inflicted burn.
- **Forcing the speed wedge onto fast responders.** Flagged in `LEARNINGS_LOG.md` 2026-07-21, flagged again in the Aug-5 audit (15/15 one-pagers, same wedge). Third time written down. The routing table has 15 rows and one is doing all the work.

---

## 5 · Open question

**What happened with Sapphire and Aesthetica Veda?** The Aug-5 audit says both were live and worth more than 40 new sends. Nothing after that date mentions them. If those threads are still open, they outrank every change in this document.
