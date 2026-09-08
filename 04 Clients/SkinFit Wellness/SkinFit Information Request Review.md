---
date_created: 2026-08-20
date_modified: 2026-08-20
status: active
---
# SkinFit Information Request — Review

**Reviewed 2026-08-20.** Source: `~/Desktop/SkinFit-Information-Request.docx`
**Context:** Gino has said an audit is not possible in the coming week or anytime soon, and asked for a proposal with costs and the systems that could be built. The team produced this questionnaire to stand in for the audit.

---

## 0 · Verdict

**As a configuration document it is strong. As a replacement for the audit it does not work, and calling it one will cost you the best finding in this engagement.**

Everything in it is self-reported by the head of marketing. The SkinFit thesis is built on a gap between **what they believe is happening and what is actually happening** — tech handoff §4: ad structure implies 27–50 conversations a day, their own sheet records ~10, and the live hypothesis is that a large share of Messenger conversations are never recorded anywhere. **A questionnaire is structurally incapable of finding that.** Ask "roughly how many enquiries came in through each channel last week" and Gino answers from the same sheet that produces the 10/day figure. You get the recorded number. The missing number is the entire finding.

**But almost all of it is recoverable without any system access**, via two screenshots Gino can take in under a minute and a set of mystery shops that need nobody's permission. §3 below. That is the fix, and it is cheap.

Three other issues: the document is too long for a man who just said he has no time, it is addressed to one person but asks questions only the front desk can answer, and it has no date, no deadline and no return channel.

---

## 1 · What the questionnaire can and cannot answer

Scored against the eight audit objectives in `SkinFit Tech Handoff 2026-08-18.md` §8.

| # | Audit objective | Covered? | Why |
|---|---|---|---|
| 1 | Where Messenger ad-form submissions actually arrive, and whether anyone opens that inbox | ❌ | §2 asks it. **The tech handoff already records the answer: "Gino believes they reach the front desk. Nobody could say through what inbox or in what format."** Asking the same man the same question in writing returns the same non-answer |
| 2 | True conversation count vs. logged enquiry count — **the headline finding** | ❌ | The question invites an estimate from their sheet. The whole point is that the sheet may be wrong |
| 3 | Time to first reply, per channel and per hour | ❌ | Nobody self-reports their own response time accurately, and no data is being shared |
| 4 | How many enquiries get a second attempt; what happens to a quoted-and-quiet patient | ⚠️ | §4 asks it. Expect "it depends on who's handling it," which you already know |
| 5 | When enquiries arrive vs. when the desk is staffed | ⚠️ | Shift timings: yes (§9). Arrival hours: no |
| 6 | The exact point people stop responding | ❌ | Requires the threads |
| 7 | Whether a booking can be written into their system | ✅ | §1 covers this well. **Genuinely valuable — it changes what you can promise** |
| 8 | What a patient finds when they search the clinic after seeing an ad | ✅ | Not because it's asked, but because **you can check it yourself today.** Partly done already |

**Score: 2 of 8 answerable, 2 partial.** The two it answers are real and worth having. The six it misses include every one that would produce a number.

**What it does answer well, and what that is actually for:** systems, integrations, ownership of channels, who touches what, whether records merge across channels, whether bookings can be written. **That is a build-scoping document, not a diagnostic one.** It tells you what you can build. It does not tell you what is broken. Both are needed; only one of them is in this file.

---

## 2 · The compliance question buried in §2

> *"For WhatsApp and Instagram specifically: are these run from a personal number or account, the WhatsApp Business app, or the Cloud API?"*

**This is the most important question in the document and it is sitting eighth in a list of thirteen.** It determines:

- whether commitment #3 in the tech handoff §7 can be honoured as written,
- whether anything you build is on the official API or in breach of platform terms,
- whether a migration of their existing number is needed, and how long that takes,
- what is possible inside and outside the 24-hour window, which is the whole no-show and reactivation product.

**Move it to the top and ask it plainly.** The parenthetical *"happy to explain why if useful"* undersells it. If the answer is "the WhatsApp Business app on a personal phone," your build timeline and your compliance position both change before anything else in the document matters.

---

## 3 · The fix — how to get the evidence without access

The constraint Gino gave you is **time and access, not willingness.** Everything below respects both.

### 3.1 Two screenshots Gino can send in sixty seconds `highest value in this entire review`

He runs the ad account. He does not need to grant access, export anything, or involve the front desk.

1. **Meta Ads Manager → "Messaging conversations started," for a date range covering the last two weeks.** Put that against their ~10-a-day sheet. **If Meta's number is materially higher, that is the headline finding, obtained for free, from a screenshot, with no audit.** If it matches, you have killed a hypothesis cheaply and honestly, which is also worth having.
2. **Meta Leads Center / Instant Forms → the leads list and count for the same period.** If submissions are sitting there unretrieved, that is immediate recoverable money and it is audit priority #1. This is the single most likely place a real, provable loss is hiding.

**How to ask, in one line:** *"One thing that would save your team a lot of effort — two screenshots from your own Ads Manager, which only you need to touch: messaging conversations started, and the leads list in Leads Center, for the last two weeks. Nothing from the front desk."*

**Add nothing else to this ask.** It is the highest-yield thirty seconds available in this engagement and it should not be buried inside a 55-question document.

### 3.2 Mystery shops — declared, not covert

You already have one running (₹499 Messenger ad, 16 Aug 9:38 PM, unanswered as of the meeting). Two or three more across the channels you have not tested — the listed WhatsApp number, an Instagram DM, the website form — give you **time to first reply per channel and per hour, which is audit objective #3, with zero access and zero cost.**

**One judgement call, and it matters.** You have now met these people. Covert shopping a cold lead is normal practice; continuing to shop a clinic you are in an active sales conversation with is a different act, and if it surfaces later it reads badly.

**Declare it, and it stops being a risk and becomes the offer:**

> Since pulling data out is difficult right now, we'll test the enquiry flow ourselves, the way a patient would, across each channel. You don't need to do anything and nobody on your team needs to know when. We'll show you exactly what we find, including the times.

He cannot object, it costs them nothing, it requires no access, and it produces timestamped evidence the questionnaire cannot. **It also converts the constraint into the differentiator named in `SALES_MOTION.md` §1** — nobody else in this market does this. Tilak already raised a shop finding in the room on 18 Aug and it landed well; this is the same move, made in advance.

### 3.3 What you can verify yourself today, with nothing from them

- Google Business Profile for the Koramangala branch — already known to have no photos, no phone, no website, no social links, and no new review in about a year.
- Meta Ad Library — creative count, launch waves, tripwire offers. Already tracked.
- The website — no phone number, no WhatsApp link, form only.
- Practo, JustDial, and any other listing a patient would land on after seeing an ad.

**None of this needs asking for. Do it before the proposal so the proposal opens with what you found rather than what you asked.**

---

## 4 · Structural problems with the document as sent

### 4.1 It is too long, and the length contradicts the reason for its existence
1. **Roughly 55 questions across 9 sections.** The stated reason there is no audit is that nobody has time. Answering this costs more of Gino's time than a 30-minute screen share would have.
2. **The realistic outcome is a partially filled document**, returned late, and then you have spent your one clean ask and have to go back for the rest.
3. **Tier it.** Send Tier 1 only, and hold the rest for after a yes.

| Tier | Contains | Sections | Count |
|---|---|---|---|
| **1 — blocks the proposal** | The WhatsApp/API question, what system, one or two systems, export capability, can a booking be written, where ad-form leads land, who monitors what, the two screenshots, "what's most frustrating" | 1, part of 2, one from 9 | **~12** |
| **2 — shapes the build, ask after a yes** | Booking, quotes, reminders, no-shows, rescheduling | 3–7 | ~26 |
| **3 — later** | Reviews and reputation | 8 | 6 |

**Section 8 (reviews) should come out entirely.** It is a different product line, it is not the wedge, and including it makes the document read as a vendor scoping an upsell rather than someone solving the stated problem.

### 4.2 It is addressed to one person but asks questions only others can answer
4. Gino is head of marketing. He can answer sections 1 and 2. **Booking permissions, deposit collection, reschedule history, cancellation policy, front-desk shift timings and no-show handling are front-desk and founder questions.** Asking him produces guesses, and guesses that then get written into a proposal are worse than blanks.
5. **Split by respondent and say so on the document:** *"Sections 1–2 are yours. Sections 3–7 are really front-desk questions — if it's easier, we can go through those in fifteen minutes with whoever runs the desk, or you can forward them."* That also creates a second, low-threat reason to talk to someone other than Gino.

### 4.3 No date, no deadline, no return channel
6. **`SALES_MOTION.md` Rule 1: nothing ships without a date attached.** This document has no date on it, no by-when, and no named respondent. It is the exact shape of the Sapphire stall — the one documented failure with a warm lead in this project's history.
7. **Fix in the covering message, not the document:** name a return date, name the person, name the channel, and say what happens next and when. *"If we have this back by Friday, the proposal is with you on Tuesday."*

### 4.4 The estimates trap
8. Two questions invite estimates that will then become numbers in your proposal: channel volumes over a recent week (§2) and quote-to-booking share (§4).
9. **Tech handoff §10 already bans this:** *"Do not quote the enquiry volume as a hard number. Roughly ten a day is their recollection of their own sheet, not a measurement."*
10. **Rule: any figure returned by this document appears in the proposal as "your team's estimate," never as a finding.** Anything else launders a recollection into a premise, which is exactly what `CLAUDE.md` rule 5 forbids.

### 4.5 The screenshot ask has a data problem you should solve before they notice it
11. The document asks for a screenshot of the lead form and field list, and a screen recording of the booking flow. **Those may contain real patient names and phone numbers.** You have committed to taking no patient data.
12. **Add one sentence:** *"If a screenshot would show real patient names or numbers, please blur them or send a blank record — we don't need any patient data."*
13. This costs a line and **demonstrates the commitment instead of asserting it.** That is worth more than the sentence in the commitments list.

### 4.6 One line to verify before sending
14. The intro says *"This builds on the commitments already shared with your team, and nothing here changes those."* **Per tech handoff §7 the six commitments were still awaiting Adi's confirmation and the client document had not been sent.** Confirm the commitments have actually reached them since 18 Aug. If they have not, that sentence points at nothing and the first thing you ask for rests on a document they never received.

---

## 5 · What this changes about the proposal

Named here because it is the real cost of skipping the audit, and it lands in the contract rather than in the questionnaire.

1. **The proposal is now built on statements, not findings.** That is survivable, but only if it is stated rather than hidden.
2. **Use the three-way split from `diagnostic_doc_playbook.md` §2 — it fits this situation better than the one it was written for:**
   - **What we verified ourselves** — the mystery shops, the ad library, the Google listing, the website. Timestamped.
   - **What your team told us** — labelled as such, every number marked an estimate.
   - **What we still cannot see, and what we would check first.**
   **Being explicit that the audit did not happen is stronger than papering over it**, and it is the method-transparency position in `SALES_MOTION.md` §1.
3. **The proposal needs an assumptions schedule and a re-scope trigger.** Full detail in `Legal and Commercial Doc Set.md` §3A. Short version: on the original path the audit de-risked the scope; here the contract has to do that job instead.
4. **Do not name a specific day-3 artefact in the proposal.** On this path the first onboarding session is the first time you see reality. Promise the day-3 artefact, name it after access.
5. **Gino has explicitly asked for costs.** The free-pilot / paid-implementation boundary in `OUTBOUND_MEMORY.md` §5 has been flagged unresolved three times and is now blocking. **No number goes on paper until it is settled.**

---

## 6 · Recommended sequence

| # | Action | Needs from them |
|---|---|---|
| 1 | Confirm the six commitments actually reached them | Nothing |
| 2 | Send the **two-screenshot ask** as its own short message | 60 seconds of Gino |
| 3 | Send **Tier 1** of the information request, with a named return date, split by respondent, with the patient-data line added and the API question moved to the top | 10 minutes of Gino |
| 4 | Offer the **declared mystery shops** in the same message | Nothing |
| 5 | Run the shops and the external checks yourself | Nothing |
| 6 | Settle the pricing boundary | Nothing from them |
| 7 | Proposal, structured Verified / Told to us / Not yet visible, with an assumptions schedule | — |
| 8 | Hold Tier 2 for the onboarding session after a yes | — |

**The two screenshots are the whole game.** If Meta's conversation count is materially above their sheet, you have the finding the audit was supposed to produce, you have it without an audit, and the proposal writes itself.


---
Related: [[04 Clients/SkinFit Wellness/SkinFit Tech Handoff 2026-08-18|SkinFit Tech Handoff 2026-08-18]] · [[01 Playbooks/Sales Motion/SALES_MOTION|SALES_MOTION]] · [[CLAUDE|CLAUDE]] · [[01 Playbooks/diagnostic_doc_playbook|diagnostic_doc_playbook]] · [[09 Company/Legal and Commercial Doc Set|Legal and Commercial Doc Set]] · [[files/OUTBOUND_MEMORY|OUTBOUND_MEMORY]] · [[04 Clients/Sapphire Skin and Aesthetics/Sapphire Skin and Aesthetics|Sapphire Skin and Aesthetics]]
