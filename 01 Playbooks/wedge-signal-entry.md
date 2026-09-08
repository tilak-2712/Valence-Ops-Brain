---
date_created: 2026-08-13
date_modified: 2026-08-13
status: active
---
# Valence Ops — Clinic Qualification, Disqualification & Wedge Routing Playbook

*v2 · last updated 2026-08-13 · Owner: Tilak & Pratham*

**What changed in v2 (folder self-audit):** the whole file was stored with escaped markdown and rendered as raw text with visible backslashes — repaired. The six-test mystery-shop SOP is cut to two. The after-hours test is retired (it contradicted the project's own ban on inadmissible-hours findings). The "Tue–Thu 11am–4pm" window is replaced by published-hours admissibility. The rebuttal test is added as §0.1. Hard kills #3/#4/#6/#8 are marked as not determinable pre-outbound. Decision entries: `files/OUTBOUND_MEMORY.md` §6, 2026-08-13.

---

## 0. Core operating rule

The entry wedge is **diagnosed, never pre-selected**. For every clinic, find the earliest provable stage in the Revenue OS funnel where money is visibly dying, and lead with the offer that fixes that stage. Dead-lead reactivation is one wedge among many — not the default.

When multiple breaks exist in the same clinic, prioritize the one that is:
1. Screenshot-provable
2. Closest to money already spent
3. Fastest to show a visible win

**One hard kill disqualifies a clinic. Soft signals route to a park tier, not a kill.**

### 0.1 The rebuttal test — run this before anything ships

For every candidate hook, write **the one sentence the doctor says back.** If a plausible one-sentence rebuttal exists, the hook does not ship.

| Hook | Rebuttal | Verdict |
|---|---|---|
| "Your IG DM took an hour" | *We answer on WhatsApp.* | Kill |
| "You run 25 ads" | *And?* | Kill |
| "A 1★ from January" | *That patient was difficult.* | Kill |
| "We messaged at midnight and got a reply at 9am" | *We were closed.* | Kill |
| "89 one-star reviews, 0 owner replies" | — | Ship |
| "Priced a transplant Tue 2pm, went quiet, nobody chased in 9 days" | — | Ship |

This generalizes the midnight-shop lesson the project already paid for. **It kills most of what the dossiers currently surface. That is the intent, not a side effect.**

### 0.2 The evidence bar

A finding ships only if it is **a first-party test, OR a pattern across ≥2 independent instances.** Single-incident review quotes get argued with; patterns don't.

Review pulls must be **chronological, 25+ minimum**. Report negatives per 100 rather than quoting one. Small samples on Google's *relevance* sort make "no complaints found" a worthless statement — it is an artifact of the sort order, not a fact about the clinic.

---

## 1. Disqualification framework

### 1.1 Hard kills — disqualify immediately, do not audit further

| # | Signal | Why it's a kill | Determinable before outreach? |
|---|--------|------------------|---|
| 1 | No website **and** no Instagram **and** no Google Business Profile | Nothing to build automation on; no channel where enquiries even arrive | **Yes** — scrapable |
| 2 | Operating under 12 months (check oldest Google review date) | No established patient base, no dormant patients to recover, unproven revenue to pay from | **Yes** — scrapable |
| 3 | Inbound volume under ~20 enquiries/month across all channels | Not enough volume for any system to act on | **No** — mark `undetermined`, never guess |
| 4 | Average treatment value below ₹25,000 | The fee structure doesn't work below this | **Partly** — inferable from advertised pricing or review-quoted amounts; label as an estimate |
| 5 | Committee or multi-partner sign-off required (no single decision-maker) | No one can say yes without external consensus | **Yes** — Pvt Ltd chains, corporate groups |
| 6 | Owner fully detached from operations — genuinely feels no pain | Nobody in the building experiences the problem | **No** — a discovery-call finding, not a screen |
| 7 | Primary ask is lead generation, ads, website redesign, or content | Marketing-agency client, not an ops-automation client. Refer out — builds goodwill | **Yes** |
| 8 | No enquiry data exists anywhere (no WhatsApp history, phone register, diary) | The audit has nothing to run on | **No** — a discovery-call finding |
| 9 | Clinic passes both speed-to-lead tests (§2) | Functioning system already in place | **No** — post-mystery-shop only |
| **10** | **No named decision-maker reachable on a personal channel** *(added 2026-08-13)* | No founder named anywhere means no personalization is possible, which means no message can be written | **Yes — and it costs two minutes** |

**On #10:** this sat *after* the most expensive step for the whole of batch 7. Project Skin received a complete dossier and was then blocked with "no founder found anywhere." Dermatonik and Haircosmos have no doctor named either. On batch-7 evidence, 3 of 10 dossiers need never have been written. **Check it at Gate A, next to reachability.**

**On #3, #4, #6, #8:** four of the ten hard kills cannot be determined before outreach. Mark them `undetermined` and move on — do **not** infer them, and do not let an `undetermined` quietly become a pass in a summary table. A batch report that shows "Unknown" in those four columns for every clinic is behaving correctly, not failing.

### 1.2 Park — not a kill, deprioritize and revisit with a specific approach

| Signal | Priority | Why park, not kill | Approach when revisited |
|--------|----------|---------------------|---------------------------|
| Mega founder-brand (very large personal following) | **Medium** | Longer cycle, gatekeepers, likely incumbent agency — but strong underlying fit | Founder-capacity-protection pitch; nurture tier, not cold DM. **Deferred to post-Case-Study-#1** per the 2026-07-22 decision |
| Existing but shallow automation (greeting-only auto-reply, no qualification) | **High** | Fit is strong, wedge is a depth upgrade rather than a new build | "The bot says hi — nobody finds out who's worth calling first" |
| Front desk is the only reachable contact today | **Medium** | Founder-discovery failure, not a clinic failure | Route through Practo doctor listing, website team page, or LinkedIn before killing |

### 1.3 Explicitly NOT disqualifiers

Do not kill a clinic for any of these alone:

- **Not running Meta ads.** Only removes the dead-lead-reactivation wedge. Also check Practo Prime / JustDial paid listings as a substitute "paying for enquiries" signal, and check Google Ads Transparency — a Meta-only check has wrongly reported "no ads" in every batch so far.
- **Missing one channel** (no website OR no Instagram), as long as WhatsApp plus one other channel exists.
- **Messy or unused CRM/spreadsheet.** Poorly configured tracking is still infrastructure to build on.
- **Strong surface reputation with no visible weakness.** The mystery shop decides, not first impressions.

---

## 2. Speed-to-lead audit SOP

**When to run this:** at the *start* of a batch, before research — not after. *(Changed 2026-08-13. The shop is the only 24–72h async dependency in the process and it was scheduled after the most expensive step, which is how batch 7 produced 25 dossiers and zero shops.)*

**Queue rule: async dependencies open the batch.**
- **Monday:** ~20 shops in one 40-minute sitting.
- **Tue–Thu:** research only the clinics whose threads came back interesting.

This flips 25 dossiers / 0 shops into ~20 shops / ~6 dossiers, and those six get written for clinics where you hold evidence nobody else has. It also structurally enforces the ≤10-minute research decision of 2026-07-22 — you cannot over-research a clinic you haven't shopped.

**Framing:** a fast responder is a strong prospect, not a weak one — the owner already believes enquiries are money. The goal is not to disqualify them; it's to find the specific gap in an otherwise good instinct.

**Tilak runs every shop personally. No agent ever sends a message to a clinic, for any reason.**

### 2.0 Admissibility — the rule that governs every shop

> **An enquiry is admissible as a hook if, and only if, it lands inside the hours the clinic publishes on its own Google profile.**

Broader and stricter than the old "Tue–Thu, 11am–4pm" window, which is retired:

- **Kills midnight permanently**, without needing a separate ban. "We were closed" is a correct rebuttal and leading with it signals you don't understand how a clinic runs.
- **Opens Saturday, Sunday and weekday evenings.** Across the 171 aesthetic/derm clinics in the SE Bangalore scrape: Saturday 6pm is the highest published-open slot at **92%**, Tuesday 6pm at 88%, Tuesday 2pm at only 78%. **220 of 223** clinics with published hours are open Saturday; 158 are open Sunday. Weekend is not after-hours in this market — it is when the patient buying a ₹1.5L procedure actually has time to enquire, and when the desk is thinnest.
- **Kills some tests the old window permitted.** Many of these clinics run split shifts (`10 AM–1 PM, 4:30–8:30 PM`), so the 11–4 window sat on top of the midday closure. **Some existing "business-hours no reply" findings are on published-closed time and are rebuttable — re-check before shipping any of them.** This already bit once: the Sapphire shop was sent Sunday outside published hours and answered at Monday opening time.
- **Costs nothing to apply** — `openingHours` is already captured on every scraped record.

**Free upgrade, currently unused:** `popularTimesHistogram` is already in the scrape data. The sharpest slot is not the clinic's busiest hour — an ignored enquiry at peak invites *"we were slammed."* It is a **published-open, low-traffic hour.** Nothing to explain there.

### 2.1 The two tests

Both fire inside a single thread, from one message. *(Cut from six on 2026-08-13.)*

| # | Test | How to run it | If it fails → wedge |
|---|------|----------------|----------------------|
| 1 | **Qualification** | In their reply, did anyone ask about concern, treatment interest, budget, or timeline — or did they just answer your question? | Qualification + scoring layer |
| 2 | **Quote decay** | Ask for a price on a high-ticket procedure, receive it, then go quiet. Does anyone chase the quote? | Quote-decay follow-up |

On a ₹49,999–₹1.5L procedure, **an unchased quote is the most expensive silence you can prove**, and it costs one message plus silence.

### 2.2 Retired tests — and why (don't reinstate without a decision entry)

| Retired test | Why |
|---|---|
| **After-hours** (10–11pm enquiry) | The rebuttal is correct — they were closed. No discriminating power: late-night enquiries die everywhere, and a test every clinic fails ranks nothing (the same defect that retired ICP scoring). Its output is inadmissible under §2.0 anyway, so running it is paying for unusable data. **It also directly contradicted this project's own midnight ban while sitting in the canonical SOP.** |
| **Cross-channel** (IG vs WhatsApp speed) | A retired wedge — WhatsApp is the channel that matters in this market. A slow IG DM costs the clinic little if real volume happens on WhatsApp. See `MEMORY.md` §2. |
| **Persistence** (go silent, count follow-ups over 7–14 days) | Takes 7–14 days and mostly tells you what quote decay tells you sooner. |
| **Booking friction** (book, then reschedule last-minute) | Requires actually booking. Expensive, and it burns the test identity. |

**Two carve-outs survive:**

**(a) The auto-reply text — an observation, not a test.** What matters is whether the automation *asks anything* or just promises a callback. One message, one screenshot, no going silent, no 72-hour clock. Still **PROVISIONAL** (`MEMORY.md` §3) — first used on Ministry of Skin, no reply, unproven. Don't make it load-bearing.

**(b) True after-hours, confirmed heavy ad-spenders only, touch-2 material only.** Never framed as slowness — framed as spend against staffing, on two verified facts and no invented third: *"your hair ad has run since 24 July"* (Ad Library, dated) + *"I asked about it at 10:40pm Tuesday, first human reply Wednesday 11:15am"* (first-party, dated). The doctor does the arithmetic. Only worth the identity cost on someone running 25 Meta + 29 Google simultaneously.

### 2.3 Save the screenshot, not the summary

Every document in this folder says hooks must be "screenshot-provable," and **no step actually saved a screenshot.** Shop results lived as prose inside dossiers, so at drafting time the evidence existed only as a paraphrase — which is precisely how a generic "Potential Missing Layers" template line once became Dr. Dixit's entire wedge.

**The timestamped image is the deliverable of the shop** (`clinic-YYYYMMDD-test.png`). Prose is derived from it, never the reverse. It is also the raw footage for any video asset.

### 2.4 Verdict

- **Fails one or both tests** → the failure identifies the wedge. Pick the entry wedge using the §0 priority rule, then run it through the §0.1 rebuttal test.
- **Passes both** → hard kill #9. Log and move on — do not keep probing.

### 2.5 Pitch angle when the clinic has a fast *human* responder

Do not sell speed — they already have it and are usually proud of it. Sell **fragility and cost**:

> "This works because of one person. What happens on their day off, after 8pm, or if they quit? And how much of their day goes to typing the same reply to people who were never going to book?"

Position the offer as: keep their existing closer, remove the manual chasing. Nothing about how they close changes.

**Standing warning, flagged three separate times and still happening:** the speed wedge keeps getting forced onto clinics the shop proved are *fast* — Glow at 5 min, Vtiara at 17 min, Aesthetica Veda at 29 min — by conceding the fact and substituting an abstraction ("the reply is fast, that's not the gap, the gap is…"). That reframe is structurally weaker: it gives up the concrete verifiable fact and replaces it with something the founder cannot check. All 15 one-pagers diagnose a variant of the same thing. **The routing table below has 15 rows and one of them is doing all the work.** If the shop says fast, either find a genuinely different wedge from §3, or don't send.

---

## 3. Signal → wedge routing table

| Signal combination | Entry wedge | Opening frame | Priority |
|---|---|---|---|
| Ads ✓ · response slow or none | Dead-lead reactivation | "You already paid for these enquiries. They're dying in your inbox." | Very high |
| Ads ✓ · fast first reply · no qualification, no follow-up | Follow-up and nurture engine | "You won the first 5 minutes and lost the next 14 days." | Very high |
| Ads ✓ · no website · thin GBP (low reviews) · fast human reply | Review engine first, infra second | "Your ads send strangers to a thin profile — trust leaks before the message ever arrives." | High |
| Ads ✓ · greeting-only auto-reply · no qualification questions | Qualification + scoring upgrade | "The bot says hi. Nobody finds out who's worth calling first." | High |
| No ads · website ✓ · high reviews · slow or no response | Instant response + organic capture | "Your reputation markets for free. Your inbox kills what it earns." | Very high |
| No ads · high review count but last review months old | Review reactivation agent | "Your best patients left quietly. The proof engine stalled months ago." | Medium |
| No ads · multi-session treatments (PRP, laser, aligners) · 12+ months operating | Dormant-patient reactivation | "These people already trusted you enough to walk in once. They're sitting in your WhatsApp history." | High |
| Practo Prime / JustDial paid listing · slow response | Dead-lead reactivation (aggregator) | "You pay Practo for enquiries, then leave them on read. Same leak, different bill." | High |
| Reviews mention booking friction, waits, or ghosting after payment | No-show recovery | "Every empty chair this month was a booked patient last week." | Medium |
| High-ticket quote given, never chased afterward | Quote-decay follow-up | "An unchased ₹1.5L quote is the most expensive silence in the clinic." | High |
| Fast human speed-caller · manual chasing · one person holds it all | Systematize the hustle | "Keep your closer. Remove the chasing. What happens after 8pm, or on their day off?" | Very high |
| Mega founder brand · overflow signals (delayed DMs, solo-doctor bottleneck) | Founder capacity protection | "You solved attention. The leak is between the message and the chair." | Medium (park) |
| Front desk is the only reachable contact today | — (access problem, not offer problem) | Route via Practo listing / website team page / LinkedIn before approaching | Medium (park) |
| Multiple breaks present at once | Earliest provable break wins | Enter on one wedge only; the full Revenue OS is the expansion, never the opener | Follows the highest-priority row that applies |

**Retired row:** *WhatsApp fast · Instagram DMs slow* → IG→WhatsApp handoff. Killed 2026-07-28 after being led with twice. A cross-channel speed comparison is only a wedge if the *slow* channel is the one the business runs on — and in this market that is WhatsApp, not Instagram.

**Priority key:** Very high = shop and send this week · High = queue within the current batch · Medium = park, revisit once the very-high/high queue is worked through. Any hard-kill combination from §1.1 does not enter this table at all.

**Before any row ships:** run §0.1. Several frames above ("You run 25 ads") are one-sentence-rebuttable as written and need a first-party fact attached to survive.

---

## 4. Applying this to clinic audits — schema tagging

Add two fields at the end of every dossier:

- **`funnel_break_stage`** — one of: `Response Speed` / `Qualification` / `Follow-up Persistence` / `Quote Chase` / `Booking / No-show` / `Post-consult` / `Reviews` / `Reactivation` / `None (pass)`.
- **`recommended_entry_sku`** — the §3 wedge corresponding to that break stage.

Both are **`PROVISIONAL` until the mystery shop has run.** Scraping cannot determine "response slow or none," so state explicitly which shop finding would confirm or redirect the wedge.

If a clinic hits a hard kill, skip both fields and mark the audit `Disqualified` with the specific kill number.

---

## Change log
- **v2 — 2026-08-13.** Escaped-markdown repair. Six tests → two. After-hours/cross-channel/persistence/booking-friction retired. Published-hours admissibility replaces the fixed window. Rebuttal test (§0.1) and evidence bar (§0.2) added. Hard kill #10 (no named decision-maker) added; #3/#4/#6/#8 marked not-pre-determinable. Shop moved to the front of the batch. Screenshot-as-deliverable rule added. IG→WhatsApp handoff row retired. Standing warning on forcing the speed wedge added to §2.5.
- v1 — initial draft combining disqualification framework, speed-to-lead SOP, and signal-to-wedge routing table with priority tiers.


---
Related: [[files/OUTBOUND_MEMORY|OUTBOUND_MEMORY]] · [[MEMORY|MEMORY]] · [[04 Clients/Sapphire Skin and Aesthetics/Sapphire Skin and Aesthetics|Sapphire Skin and Aesthetics]] · [[04 Clients/Aesthetica Veda/Aesthetica Veda|Aesthetica Veda]] · [[05 Prospects/Batch 7 (Notion Batch 2)/19 Dermatonik|19 Dermatonik]] · [[05 Prospects/Batch 7 (Notion Batch 2)/25 Project Skin|25 Project Skin]]
