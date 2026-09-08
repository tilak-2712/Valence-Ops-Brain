---
date_created: 2026-08-13
date_modified: 2026-09-08
status: active
---
# SALES_MOTION.md — What Happens After They Reply

**Status:** v1 · drafted 2026-08-04 · **zero pilots closed — everything here is designed, not proven.** Every stage carries an explicit "what would falsify this" note. Update from real conversations, not from re-reading this file.

**Scope:** this document owns everything from the moment a clinic replies positively to the end of day 14 of a pilot. Everything *before* the reply is owned by `personalized-outbound-v2.md`, `files/OUTBOUND_MEMORY.md`, and `wedge-signal-entry.md`. Don't duplicate those here.

**Companion files:**
- `01 Playbooks/Sales Motion/01 Reply to Call.md` — triage rules + message templates
- `01 Playbooks/Sales Motion/02 Credibility Packet.md` — Loom scripts, demo spec, what ships when
- `01 Playbooks/Sales Motion/03 Operations Call.md` — the call script and compressed question map
- `01 Playbooks/Sales Motion/04 Findings and Rollout.md` — the post-call document template
- `01 Playbooks/Sales Motion/05 Pilot and Onboarding.md` — agreement terms + the first 14 days
- `01 Playbooks/Sales Motion/HOW-WE-WORK.md` — the client-facing doc (the "company profile" replacement)

---

## 0 · Why this file exists

A clinic replied. They said the observation was good and asked for a company profile. Nothing existed to send. The reply was left to cool while something got built from scratch.

That is not a content problem. It's a structural one, and it has three parts worth naming precisely, because the fix for each is different:

**(a) Nothing existed that could ship in under an hour.** Any inbound request that requires new construction loses to the attention window. A clinic owner who asks for something on Tuesday has moved on by Friday. The fix is not "write faster" — it's that the entire post-reply path must be pre-built and sitting on a shelf, so handling a warm reply costs 30 minutes of assembly, not three days of authoring.

**(b) The credibility ladder peaks too early.** The diagnostic one-pager is the most effort-intensive asset in this project, and it goes out cold or near-cold. That means after the one-pager there is nothing higher to escalate to — the curve peaks at touch 2 and flat-lines. A reply has to be able to unlock something the cold sequence didn't already spend.

**(c) The work that felt productive was the work with no exit.** Research → enrich → send → wait is a closed loop that produces a full calendar and a flat pipeline. It feels like progress because it is measurable and repeatable. The reply is the only event that breaks the loop, and it was the one event nothing was built for.

**The uncomfortable version:** ValenceOps sells speed-to-lead. A clinic that replies and waits three days for a response has watched the vendor fail at the exact thing the vendor sells. There is no recovering from that with copy.

---

## 1 · The one asymmetry to build everything on

Zero clients. Zero results. No case study. That's fixed for now and no amount of framing changes it.

What is *not* zero: the research depth. Nobody else in this market mystery-shops a clinic, times the reply, reads a spread of reviews, checks the ad library, and shows up with a timestamped finding before asking for anything.

Every competitor in this category leads with claimed results. The market has been burned by exactly that — clinic owners have signed for things that were never used, and the real objection is never price, it's *exposure*: the fear of still paying for something dead eight months from now.

So the only honest differentiation available is **method transparency**: showing exactly how the work gets done, on their own clinic, before any money changes hands, and being explicit about what isn't known yet. This is already the philosophy of `One-page-docs/diagnostic_doc_playbook.md` §2 — *"here's what we could verify, here's what we couldn't, here's what we'd test if we had access."* This document extends that same posture across five stages instead of one page.

**The corollary, which is the whole positioning:** being early is not a weakness to be hidden until asked. It is the offer. Client #1 gets two founders who will over-serve them and can't afford to fail; client #40 at an established agency gets a junior account manager. Say that out loud, name the risk honestly alongside it, and it converts better than a fabricated portfolio — in a category where every other pitch is inflated, the person being straight is the anomaly.

`OUTBOUND_MEMORY.md` §3 already bans fabricated case studies and says to admit it if asked. This turns that constraint into the position.

---

## 2 · The motion — five stages

| # | Stage | Clock | Who owns it | Exit criteria |
|---|---|---|---|---|
| 0 | **Reply triage** | ≤4 business hours | Clinic's POC (Tilak/Pratham per Notion) | Reply sent + call slot proposed |
| 1 | **Credibility packet** | ≤24 hours from reply | Same POC | Packet delivered + call booked with a date |
| 2 | **Operations call** | Within 5 days of reply | Both, defined roles | Diagnosis captured, next-step date stated on the call |
| 3 | **Findings + rollout plan** | 48–72h after the call | POC drafts, other reviews | Doc sent + 20-min decision call booked |
| 4 | **Pilot + onboarding** | Kickoff ≤7 days after yes | Both | Setup session done, first visible artifact live by day 3 |

**Read the whole table before optimizing any one row.** The most common way this breaks is a stage getting skipped because a specific clinic seems eager — an eager clinic that skips Stage 1 arrives at the call needing education, and the call becomes a pitch.

### The three rules that hold the whole thing together

**Rule 1 — Nothing ships without a date attached.**
Every asset travels with either a booked time or two named slots. Never send a document and wait to see what happens. A document without a date is a stall you built yourself.

**Rule 2 — Diagnosis and prescription never happen in the same conversation.**
The operations call diagnoses. The findings document prescribes. Splitting them means the plan gets written with a clear head instead of improvised live, it creates a second reason to talk, and it stops you sounding like every vendor who arrived with the answer pre-loaded. *(This is a deliberate departure from the original brief — see §5.)*

**Rule 3 — A warm reply outranks the send quota, always.**
If there are 3+ live conversations, stop new Day-0 sends until they're through Stage 2. Sends are infinitely repeatable; a warm reply happens rarely and expires. `OUTBOUND_MEMORY.md` §8 weekly review currently optimizes for touches per week — that metric is now subordinate to reply handling.

---

## 3 · Stage detail

### Stage 0 — Reply triage (≤4 business hours)

Three reply types, three different moves. Full templates in `01 Playbooks/Sales Motion/01 Reply to Call.md`.

| Type | What it looks like | What they're actually asking | Move |
|---|---|---|---|
| **A — Curiosity** | "Good observation." "Interesting." "How did you find this?" | *Is there more where that came from?* | Answer the question honestly and briefly, then offer the walkthrough + two slots |
| **B — Credential check** | "Send your company profile / details / pricing." "Which clients do you work with?" | *Are you real, and will this waste my time?* | Send the packet **with** two slots. Never the doc alone |
| **C — Ready** | "Call me." "When can we talk?" | Nothing — they're in | Book immediately, send the packet as pre-work |

**Type B is the one that broke last time and the one most likely to break again.** The instinct is to treat it as a document request. It isn't. It's a credential check *and* a soft stall — sending a PDF and waiting is how a warm reply becomes a cold one. The packet answers the credential question; the two named slots stop the stall.

**If the packet can't go out same-day, a holding message goes out within 4 hours anyway.** A holding message that names a date is a commitment. Silence is a verdict.

**Falsifier:** if Type B replies consistently go quiet after receiving the packet + slots, the packet is answering the wrong question. Test the shorter version (video only, no doc) before rewriting the doc.

### Stage 1 — The credibility packet (≤24 hours)

Purpose, stated as a constraint: **the call must be able to be 100% about their operation.** Any minute spent on the call explaining what ValenceOps is, or establishing that you're competent, is a minute stolen from diagnosis. Everything explanatory gets front-loaded into async assets they consume on their own time.

Three components, in build-priority order:

**1. The walkthrough video — 5–7 min, recorded once, reused.**
Face and screen. Who you are (honest about stage), what this is in plain terms, the system actually running, what a first month looks like, what you'd need. Script in `01 Playbooks/Sales Motion/02 Credibility Packet.md`.

**2. `HOW-WE-WORK.md` → PDF — the "company profile" replacement.**
Method and terms, not claims. Four pages. Includes the explicit "we're early" section. Client-facing copy in `01 Playbooks/Sales Motion/`.

**3. The live product demo — ✅ BUILT (confirmed 2026-08-13).**
A working WhatsApp number the founder can message *themselves*, during or before the call, and watch it qualify the enquiry and book them in. With zero clients, this is the closest thing to evidence that exists. A claim they can test is not a claim.

**Know the demo's edges and state them first.** Live: instant reply, qualification, booking. **Not live:** no-show recovery, quote-decay chase, dormant reactivation — those are walked through as the actual message sequences. They need real CRM state and a real missed appointment to mean anything, staging one per clinic doesn't scale, and a staged no-show proves nothing. Say so unprompted — *"I'm not going to fake that one for you"* — which is method transparency (§1), the only honest differentiation available here. Full split in `OUTBOUND_MEMORY.md` §5b.

Personalized variant for high-priority clinics: a 3–4 minute screen recording walking through *their* audit — the timestamps, the ads, the review pattern — using the same Confirmed / Can't Confirm / Would Check First structure as the one-pager. Costs ~25 minutes. Reserve it for Priority-1 rows in the Notion tracker.

**Falsifier:** if founders arrive at calls not having watched the video, the video is too long or arrived without a reason to watch it. Fix the framing sentence before the video.

### Stage 2 — The operations call (50 min, within 5 days)

Full script in `01 Playbooks/Sales Motion/03 Operations Call.md`. Shape:

| Minutes | Block | Purpose |
|---|---|---|
| 0–3 | Frame: purpose, plan, outcome | Kill the expectation of a pitch, explicitly |
| 3–8 | "Walk me through how a patient goes from first hearing about you to sitting in your chair" | One open question, then listen |
| 8–35 | Forensic blocks — speed, follow-up, data, no-shows, quotes, staff | The compressed version of `Audit_call_docs/03` |
| 35–42 | Live evidence — ask to see the WhatsApp inbox on screen | Where diagnosis stops being arguable |
| 42–47 | The mirror — play back what you heard, in their words, solve nothing | The highest-trust moment available |
| 47–50 | Next step, dated | "A short document by Thursday, then 20 minutes to decide" |

**Targets:** talk ~43% of the time, 11–14 real questions, zero solutions offered. Two people on the call with defined roles — one leads, one takes notes and asks exactly one sharp follow-up before the close. A silent second person with no job is worse than being alone.

**The single most important instruction: do not solve anything on this call.** The urge to demonstrate competence by fixing something live is the strongest failure mode here, and it costs the entire Stage-3 document its reason to exist.

**Falsifier:** if you talk more than half the time, or if you named a solution before minute 42, the call failed regardless of how it felt.

### Stage 3 — Findings + rollout plan (48–72h)

Template in `01 Playbooks/Sales Motion/04 Findings and Rollout.md`. The document does five things:

1. What we heard — their words, quoted back
2. What we verified from outside — the pre-existing audit
3. What we still can't see without your data — named honestly
4. The three things costing the most — ranked, with the reasoning visible
5. What we'd do first, and why that one — one wedge, 2–3 weeks, with week-by-week

**Scope the data ask down to exactly one item.** `08 Collateral/Audit Call Docs/02_data_intake_requirements.md` asks for a raw CRM export, Meta read-only access, WhatsApp chat history, billing counts, a staff list, and appointment data. That document is correct — for Stage 4, after a yes. Sending it at Stage 3 asks an unsigned clinic to hand over patient data to two strangers, and it will end the conversation. At Stage 3 the ask is one thing, ideally the thing they can produce in five minutes.

**Falsifier:** if clinics agree to the plan but the data never arrives, the ask was still too big. Halve it again.

### Stage 4 — Pilot + onboarding

Terms are settled in `OUTBOUND_MEMORY.md` §5 and are not re-opened here: **the audit and strategy document are free; building and running the system is paid.** Named guarantee with no patient-count promise. Completion mechanism = named POC + 4-business-hour reply SLA, end-of-pilot review call booked *before* launch, stop-clause at 3 unanswered routed replies. **The ₹2,000 refundable deposit is re-engagements / prior-ghosts only — never a first cold clinic** (this file previously listed it without the carve-out). Paid path: ₹20k setup / ₹40k month, one month's notice. That conversation happens after the free document, never before.

⚠️ **The free-pilot / paid-implementation boundary is unresolved** — see `OUTBOUND_MEMORY.md` §5. Don't describe step 3 or quote a price to a clinic until it's settled.

What's new here is the onboarding mechanics, in `01 Playbooks/Sales Motion/05 Pilot and Onboarding.md`. Two findings drive it:

- **Access-gathering is the #1 cause of stalled onboarding**, and email ping-pong for credentials burns 1–2 weeks. Fix: a single 45-minute screen-share setup session where everything is collected at once, booked before the pilot start date.
- **First visible result inside 7–10 days or momentum dies.** Fix: a deliberately small artifact live by **day 3** — something the clinic can see working, even if it's one flow on one channel. Not the full build. Something real, fast.

Then 15-minute check-ins twice a week for the pilot's duration. Short and frequent beats long and monthly.

---

## 4 · Failure modes, named

| Failure | What it looks like | Guard |
|---|---|---|
| **The brochure trap** | Building a polished capabilities deck that invites "so who else do you work with?" | Method-and-terms doc, "we're early" section stated first, never defended second |
| **The document stall** | Asset sent, no date attached, conversation cools | Rule 1 — nothing ships without a date |
| **Solving on the discovery call** | You fix something live, they say thanks, Stage 3 has nothing left to say | Rule 2 — no solutions before minute 42 |
| **The heavy data ask** | Full intake requirements sent pre-signature, clinic goes quiet | One item at Stage 3, full list at Stage 4 kickoff |
| **Send-quota crowding** | New Day-0 batch goes out while two warm replies sit unhandled | Rule 3 — replies outrank sends |
| **Capacity collapse** | Reply arrives, nothing is on the shelf, three days pass | The packet is pre-built. Handling a reply is assembly, not authoring |
| **Over-serving the wrong clinic** | 6 hours into a Priority-3 clinic that was never going to pay | Personalized assets are Priority-1 only |
| **Pilot drift** | Pilot starts, nothing visible by week 2, clinic disengages | Day-3 artifact, twice-weekly 15-min calls, review call booked before launch |

---

## 5 · Departures from the original brief — overrule these deliberately, not by accident

**1. No "company profile."** Replaced with a How We Work doc. Reasoning in §1 and §3/Stage 1. If you want a designed capabilities PDF anyway, the content in `client-facing/HOW-WE-WORK.md` is the right content to design — but the section order matters more than the design, and "we're early" must not be buried at the back.

**2. The audit call is split into two conversations.** The brief described one call that asks questions, audits, and produces a strategy and rollout plan. That's three jobs and the third one contaminates the first two: a call that has to end with a plan pressures you toward a plan you already had. Diagnosis on the call, prescription in the document, decision on a short second call. If a clinic explicitly demands the plan live, give them the ranked three things and hold the rollout for the document.

**3. `02_data_intake_requirements.md` is re-staged, not rewritten.** It's a good document sitting at the wrong point in the sequence.

**4. Send quota is now subordinate to reply handling.** `OUTBOUND_MEMORY.md` §8's weekly review counts touches. That metric stays, but it no longer wins a conflict.

---

## 6 · What to measure now

The existing `SEND_LOG.csv` tracks sends. It has no column for anything past a reply. Add a second ledger — `files/REPLY_LOG.csv`:

```
date_replied,clinic,reply_type(A/B/C),hours_to_our_response,packet_sent(y/n),
personalized_video(y/n),call_booked(y/n),call_held(y/n),findings_sent(y/n),
pilot_agreed(y/n),stage_lost_at,their_words
```

Four numbers matter more than the rest, and none of them are reply rate:

1. **Hours to first response.** Target ≤4 business hours. This is the one you control completely.
2. **Reply → call-held rate.** If this is below half, Stage 0/1 is broken.
3. **Call-held → findings-accepted rate.** If this is low, the call is being run as a pitch.
4. **Stage lost at.** Where conversations die is more informative than how many die.

**Tripwire addendum.** `OUTBOUND_MEMORY.md` §1 says 100 touches or 45 days with zero pilots re-opens the vertical question. Add a second, earlier tripwire: **if 3 clinics reach Stage 2 and none reach Stage 4, the problem is the offer or the call — not the outbound.** Stop tuning DMs at that point and rebuild the call.

---

## 7 · Build order — what to do first

Everything in `01 Playbooks/Sales Motion/` is drafted and ready to use, except the two things that need recording and building. Sequence:

1. **Record the 6-minute walkthrough video.** Script is written. One take is fine; polish is not the point and over-polish reads as agency. **Status unconfirmed as of 2026-08-13 — no file exists in this folder.**
2. **Export `HOW-WE-WORK.md` to a clean PDF.** Same typographic treatment as the one-pagers (`diagnostic_doc_playbook.md` §6). **The markdown exists; no PDF exists in this folder.** It needs to be attachable in 10 seconds. Resolve the Step-3 pricing flag in that file before exporting.
3. ~~Build the demo clinic on a live WhatsApp number.~~ **✅ DONE — confirmed 2026-08-13.** WhatsApp automation with lead qualification and booking is live. Its edges are documented in `OUTBOUND_MEMORY.md` §5b; state them unprompted.
4. **Before the next batch ships — dry-run the operations call.** One of you plays a clinic owner, the other runs the script, 50 minutes, timed. Do it twice. The first live run should not be the first run.
5. **Ongoing — `REPLY_LOG.csv` from the next reply onward.**

Do not send another Day-0 batch until items 1 and 2 exist. The cost of a reply arriving with nothing on the shelf is higher than the cost of a week without sends. **Item 3 is now done, which removes the largest piece of that risk — but the walkthrough video and the How We Work PDF are still the gate, and neither is in this folder.** Confirm their real status before the next batch rather than assuming this file is current.
