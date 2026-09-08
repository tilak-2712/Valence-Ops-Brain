---
date_created: 2026-08-04
date_modified: 2026-09-08
status: active
---
# 05 — Pilot Agreement and the First 14 Days

**Owns:** Stage 4. From "yes" to a pilot that actually finishes.

> **Commercial shape [Tilak, 2026-08-13]: the audit and strategy document are free; building and running the system is paid.** The ₹2,000 deposit row below is correctly scoped to reactivation pilots only — keep it that way. ⚠️ Whether the *free 2–3 week pilot* still exists as a distinct step, or has collapsed into the free audit + document, is unresolved — see `OUTBOUND_MEMORY.md` §5.

**Terms are settled elsewhere and are not re-opened here.** `OUTBOUND_MEMORY.md` §5 fixes the commercial instrument: free 2–3 week pilot on one wedge, named guarantee with no patient-count promise, and a four-part completion mechanism. Post-pilot commercials follow the existing ₹5k credit / ₹20k setup / ₹40k retainer path, and that conversation happens at the review call — never before.

**What this file adds:** the mechanics that decide whether the pilot finishes. A free pilot that dies quietly in week two is worse than a no, because it burns the one thing you can't rebuild — the first reference.

---

## The two things that kill pilots

Both are known, both are boring, both are fixable in advance.

**1. Access-gathering.** The single biggest cause of stalled onboarding across service businesses, and it typically burns one to two weeks of email back-and-forth for credentials. Every day spent asking for a login is a day the clinic's enthusiasm decays from where it peaked — on the decision call.

**Fix: one 45-minute screen-share setup session, booked before the pilot start date, where everything is collected at once.** Not a document, not a checklist by email. You on a call with them, screen shared, taking what's needed while they're there. This one change is worth more than any other item in this file.

**2. No visible result inside the first week.** Speed to first win is the strongest predictor of whether a client stays engaged. Nothing visible by day 10 and the pilot becomes something happening to them rather than with them.

**Fix: a deliberately small artifact live by day 3.** Not the full build. Something real they can see working — even if it's one message on one channel. Deliberately under-scoped so it can't slip.

---

## The completion mechanism — non-negotiable at agreement

Per `OUTBOUND_MEMORY.md` §5. All four are agreed *at the yes*, not introduced later. Introducing a token deposit in week two reads as a bait-and-switch; introducing it at the yes reads as seriousness.

| # | Mechanism | Why it exists | How to say it |
|---|---|---|---|
| 1 | **Named POC + 4-business-hour reply SLA** on routed patient replies | A revived patient who waits two days is worse off than one never contacted | "One person we can reach. When a patient replies, they need a human within a few working hours — that's the part that decides whether this works" |
| 2 | **Review call booked before launch** | An unbooked end-date is how a pilot becomes indefinite | "Let's put the review in the calendar now — [date], three weeks out" |
| 3 | **Stop-clause: 3 routed replies unanswered >48h pauses the pilot** | Protects the patients, and protects you from being blamed for a failure that isn't yours | "If three patients reply and nobody gets back to them, we pause. Not to be difficult — those are your patients and a message that goes nowhere costs you more than not sending it" |
| 4 | **₹2,000 refundable token deposit** — reactivation pilots only | Free work gets deprioritised. A small returnable amount converts it into a commitment | "Two thousand rupees, refunded at the end whatever happens. It's not for the money — it's so this doesn't end up bottom of your list" |

**On the deposit:** if it creates real friction with an otherwise strong clinic, take the deposit off before taking the SLA off. Mechanism 1 is what makes the pilot work; the deposit only makes it get attention.

---

## The setup session (45 minutes, before day 1)

One call, screen shared, everything collected live. **This is where `08 Collateral/Audit Call Docs/02_data_intake_requirements.md` finally comes out** — and even here, only the sections relevant to the one wedge being piloted. Send the full document only if they ask for it in writing.

**Agenda:**

| Min | What |
|---|---|
| 0–5 | Confirm the pilot in one sentence. What's being run, what success looks like, when it ends |
| 5–20 | Collect. WhatsApp Business access, the data export, whatever the wedge needs — live, on the call |
| 20–30 | Meet the coordinator. Not optional — see below |
| 30–40 | Walk the message wording. Get it approved on the call |
| 40–45 | Confirm dates: day 3 artifact, twice-weekly check-in slots, review call |

**Run the WhatsApp quality check here** (`08 Collateral/Audit Call Docs/01` §3.5). Quality rating and messaging tier, before any campaign volume is planned. A Yellow or Red rating changes the whole timeline, and finding that out in week two rather than day zero is an avoidable disaster.

### Meeting the coordinator matters more than it looks

The owner said yes. The coordinator has to live with it, and they've had no say. From `08 Collateral/Audit Call Docs/03` QE1 and QE3, two things are usually true: the coordinator's version of reality differs from the owner's, and if there's individual commission involved, they have a real reason to resist a system that touches their patients.

**Do not skip this and do not let it be a formality.** Five minutes:

> You've been doing this longest, so you'll know things [owner] doesn't. Two questions.
>
> When a patient replies to one of these, what would make it annoying for you rather than useful?
>
> And — anything you'd want it to not do?

Then build what they said into the design and **tell them you did.** A coordinator who feels consulted makes the pilot work. One who feels bypassed can end it without ever saying anything to the owner.

Also, plainly: **any patient who converts from a routed reply is credited to the coordinator, not the system.** Say it out loud in this session. It costs nothing and removes the strongest reason for quiet resistance.

---

## The 14 days

| Day | What happens | Visible to clinic |
|---|---|---|
| **1** | Setup session. Data received. Wording approved | The call itself |
| **2** | Build. Clean and de-duplicate the list. Suppress anyone who shouldn't be contacted | — |
| **3** | **First artifact live.** The small visible thing | **Yes — the point of the day** |
| **4** | First real batch out, small. 10–20, not the whole list | Yes |
| **5** | 15-min check-in. What came back, what to change | Yes |
| **6–7** | Adjust wording on what week one showed | — |
| **8** | Second batch, larger | Yes |
| **9** | 15-min check-in | Yes |
| **10–12** | Run. Route replies. Watch the SLA | Yes — replies arriving |
| **13** | Assemble what happened, honestly, including what didn't | — |
| **14** | **Review call** (already booked) | Yes |

**On the day-3 artifact.** Pick something small and certain. Examples by wedge:

- *Quote follow-up* → the list of quoted-and-not-decided patients from the last 90 days, handed over as a clean sheet. They have never seen this list. It exists nowhere. Producing it is often the single most striking moment of the pilot, and it involves sending nothing.
- *After-hours capture* → the new auto-reply live on their number, which they can message themselves that evening.
- *No-show recovery* → the last month's no-shows as a list, with the recovery message drafted and awaiting their approval.

**Notice what these have in common:** each one shows them something about their own clinic that they couldn't see before. That's the product, demonstrated, before any result exists.

**On check-in calls:** 15 minutes, twice a week, same slots. Short and frequent beats long and monthly — it keeps the pilot present without becoming a burden, and it means a problem surfaces on day 5 rather than at the review.

---

## The review call (day 14–21)

Booked at agreement. Non-negotiable. This is the call the whole pilot exists to earn.

**Structure:**
- **0–5:** What actually happened. Numbers, plainly, including the disappointing ones. **Lead with what didn't work.** Volunteering the weak result before they find it is what makes the strong ones believable
- **5–10:** What it showed about the clinic that wasn't visible before. Often the most valuable output regardless of the numbers
- **10–15:** What we'd do next, and what we'd do differently
- **15–20:** The commercial conversation — **only if the pilot produced something real**
- **20–25:** The two asks

**On leading with what didn't work:** a review call that opens with the best number reads like every vendor report the owner has ever received, and gets discounted accordingly. One that opens with *"the second batch performed noticeably worse than the first, and here's why"* gets read as true. You cannot afford to be discounted on your first reference.

**The two asks, in this order:**

1. **Would you say so?** Whatever form they're comfortable with — a sentence, a call with another owner, permission to name the clinic. This is worth more than the retainer right now, because it's what breaks the zero-case-study constraint permanently. Ask for it clearly, once, and accept whatever they offer.
2. **Do you want to continue?** The ₹20k / ₹40k conversation. If the pilot produced nothing real, do not ask this — say so and offer to stop. A clinic you left honestly is a reference; one you upsold on a failed pilot is a liability with a story.

**If the pilot failed:**
> It didn't do what I hoped. Here's exactly where it stalled — [specific point]. I don't think you should pay for this and I'm not going to ask you to.
>
> What it did tell us is [the genuine finding]. That's yours either way, and if it's ever useful to pick this up again, you know where I am.

Then stop. This is the version that gets talked about — clinic owners in one city talk to each other, and "they told me it didn't work and refused to charge me" travels further than any case study you could have written.

---

## Log it

`REPLY_LOG.csv` row completed through `pilot_agreed`. Then a `LEARNINGS_LOG.md` entry in the existing tried → happened → changed format, whatever the outcome. The first pilot — successful or not — is the most informative event in this project's history to date, and most of what it teaches will be about the motion rather than the product.
