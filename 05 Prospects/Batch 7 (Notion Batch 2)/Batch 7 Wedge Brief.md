---
date_created: 2026-08-14
date_modified: 2026-08-14
status: active
---
# Batch 7 — Observation Brief for the Follow-up-2 One-Pagers

*Rebuilt 2026-08-14, then stress-tested the same day. Every observed fact comes from a screenshot in
`mystery-shop-b7/` that I read directly. Where a screenshot and the Notion prose disagree, the
screenshot wins and the disagreement is stated.*

**Structure per clinic:** observed fact → observation → possible problem → what can't be confirmed →
the question. Per `diagnostic_doc_playbook.md` §3.

**No entry names a service.** `recommended_entry_sku` in `wedge-signal-entry.md` §4 is an internal
routing label; `MEMORY.md` §2 records what happened when those labels drifted toward client-facing
copy. What gets built is proposed after the audit, from the clinic's own data. Every "possible
problem" below is a hypothesis, because that is all it can honestly be.

**Timeline key:** shop opened Mon **10/8**. Screenshots captured **12/8**. Today **14/8**.
"Yesterday" in a screenshot = 11/8, "Today" = 12/8.

---

## 0. Read before building

### 0.1 Three "confirmed" entries in Notion are factually wrong

| Clinic | Notion says | Screenshot shows |
|---|---|---|
| **Dr. Priya's** | *"Then silence 24h+"* | **False.** Replies at 11/8 7:07 PM, 7:14 PM, 12/8 11:14 AM, ending in a full itemised price list. |
| **Project Skin** | *"Nobody did. 24h+"* | **False.** A human replied in **60 seconds** on 11/8 and later gave full pricing. |
| **Dermatonik** | *"No price"* + opener retest needed | **Partly false.** They quoted *"Starting 5500/-"*. Opener is in `dermatonik-1.png`: instant auto-reply, real content in 3 min. |

Verified accurate: **Akera's** 19h 8m with no acknowledgement, and **Project Skin's** double bot-fire.

### 0.2 Vitals Klinic gets no document

1-minute AI reply → qualifying question → **unprompted follow-up one hour later** → itemised pricing
with strike-throughs → product card with an "I'm interested" button → branch routing → treating
doctor named → native **Book appointment** form. Cold to bookable in four minutes.

Hard kill #9, *functioning system already in place*. There is no honest observation here that isn't a
compliment. *(Number shopped was +91 92068 69610, not the +91 97404 84793 on file — correct the record.)*

### 0.3 Two clinics have no screenshot

**Derma Solutions** and **Haircosmos** exist only as Notion prose. §2.3: *"the timestamped image is
the deliverable of the shop; prose is derived from it, never the reverse"* — and it names
paraphrase-as-evidence as why the Dr. Dixit wedge had to be discarded. Find them tonight or hold
those two.

### 0.4 The batch pattern, and why it can't lead everywhere

Identical three-step script at all ten. **Seven gave a price. One followed up.**

| Clinic | Price | When | Followed up? |
|---|---|---|---|
| Akera | ₹4,500 / ₹18,000 / **₹28,000** per session | 11/8 5:31 PM | No — 3 days |
| Dr. Priya's | ₹9.5k / ₹10k / ₹8.5k per session | 12/8 11:14 AM | No — 2 days |
| Project Skin | ₹3,000 / ₹6,000 per session | 12/8 2:14 PM | No — 2 days |
| VIDA | "It start from 3500 to 6500" | 11/8 6:08 PM | No — 3 days |
| Dermatonik | "Starting 5500/-" | 11/8 4:34 PM | No — 3 days |
| **Vitals** | ₹2,500 / ₹8,000 + booking link | 12/8 3:17 PM | **Yes — unprompted** |

Real, and first-party. But §2.4 of the one-pager audit: fifteen documents diagnosing one thing is
*"the tell of a solution looking for a problem, and a sharp doctor will feel it even if they can't
name it."* So it leads nowhere and appears as a second beat only where it's the sharpest thing present.

### 0.5 What the stress test changed — and why

Each observation was re-run against the §0.1 rebuttal test (*write the one sentence the doctor says
back*) and against `MEMORY.md` §2 (*could an Indian clinic owner say this, in these words, about
their own day?*). Five changed:

| Clinic | Failed on | Fix |
|---|---|---|
| **Akera** | *"That was one evening, we're normally quick"* — a complete rebuttal, and I have one data point | **Lead on the absence of any acknowledgement, not the 19 hours.** You either have an auto-reply or you don't. Not arguable, and Akera is the only clinic of twelve with none |
| **VIDA** | *"Forty-five minutes is fast"* — correct, and it kills the whole "degradation curve" | **Drop the curve. Lead on the range with nothing attached to it.** The timing was never the failure |
| **Dr. Priya's** | I asserted she personally typed the replies. **The screenshot does not prove that** — it proves the account is personal, not who holds the phone | State only what's verifiable and let the question carry it |
| **Ara** | *"No defined second path"* is a consultant's sentence, not hers | **Name the patient, not the process** |
| **Dermatonik** | Read almost identically to Gejje's — the convergence §2.4 warns about | Separate them: Gejje's withheld everything, Dermatonik gave everything and asked nothing |

**Project Skin:** the double bot-fire is demoted to colour. Two automations firing is a config
artifact, not a business failure, and leading on it reads as a gotcha.

---

## 1. Per clinic

---

### 1.1 Akera Health

**Observed fact.** Enquiry 4:23 PM Monday 10/8. First reply 11:31 AM Tuesday 11/8 — *"Hi may I know
what treatment you are looking for?"* Nothing at all in between. **No automatic acknowledgement, no
holding message, nothing.** Of the twelve clinics tested, this is the only one where an enquiry
produced no response of any kind.

**Observation.** There is no automated acknowledgement on this channel. Once someone did pick it up,
the handling was good — 12 minutes to a treatment answer, 8 more to itemised pricing including a
₹28,000-per-session procedure. The gap isn't skill. It's that nothing catches the message in the
meantime.

**Possible problem.** If the inbox is checked rather than watched, then how fast anyone hears back
depends on who happened to open it and when. An enquiry from ten minutes ago and one from last night
look the same — both are just unread. And with 25 Meta and 29 Google creatives running across two
branches, the rate at which those messages arrive is bought and steady, while the rate at which they
get picked up isn't governed by anything.

The part worth sitting with: as things stand, nobody at the clinic — including whoever signs off the
ad spend — can tell whether that Monday was unusual or ordinary.

**Can't confirm.** Whether 19 hours is typical. Daily enquiry volume. Whether phone calls are handled
differently. Whether the branches share an inbox.

**The question.** Of the WhatsApp enquiries that arrived last month, how many got a reply the same
day — and is there anywhere that could be looked up?

**Build notes.** The 19 hours is the *consequence*; the missing acknowledgement is the *fact*. Lead
on the fact — *"that was one bad evening"* answers the first and cannot answer the second. **Never
lead with the ad count**: the audit's own rebuttal table lists *"You run 25 ads" → "And?" → Kill*.
Ads attach to the first-party fact, never carry it. **Founder unidentified** — MCA on Akera
Healthcare Pvt Ltd first.

---

### 1.2 Ara Skin Clinic

**Observed fact.** 11/8, 4:33 PM: *"could you provide me with more info on acne/scars treatment
please"*. 4:35 PM: *"Can we call you sir"*. 4:36 PM: *"busy with work, could you drop the info here"*.
4:37 PM: *"so that i could have a look"*. Nothing since — three days.

**Observation.** The reply came in two minutes when it offered a call. When the patient said he was
at work and asked twice for it in writing, the thread ended.

**Possible problem.** This is the patient who messages from their desk at half four, can't take a
call, and wants something they can read on the way home. Every clinic gets them. What's unclear is
what's meant to happen for that person here — because on this occasion, nothing did. Nobody decided
to let it go; there just wasn't a next step once the call was turned down.

Worth saying plainly: this clinic answers **4 of 4** negative reviews personally and substantively,
which is the best owner engagement of the twelve. Attention isn't what's missing here.

**Can't confirm.** How often patients decline a call. Whether a call was tried and missed. Whether
written treatment information exists in a sendable form — none appeared. Whether Instagram differs.

**The question.** When a patient says "just send it to me," what's supposed to happen — and who
decides?

**Build notes.** Fully unblocked; Dr. Sonakshi Sunil confirmed via the clinic's own IG bio.
**Do not use the 18-minute reply from 10/8** — 18 minutes is fine and leading there trips §2.5.
**Do not claim ad spend**: the 19 Google creatives are registered to *"Pure Dermacare"* with no
established link, and Practo is listed but not Prime (2 patient stories vs 294 on Google). Frame
against the reputation they've earned, not money spent.

---

### 1.3 Dr. Priya's Skin & Hair

**Observed fact.** The number published as the clinic contact is a **personal WhatsApp account, not a
business one** — the profile reads `~Dr Priya J Talageri`, no business badge, video calling enabled,
"No common groups." Replies came at 4:23 PM, 7:07 PM, 7:14 PM, and 11:14 AM the next morning, the
last of them a typed-out price list: *"mnrf per session 9.5 k / dermapen 10 k per session / MDF 8.5 k
per session."*

**Observation.** First-time enquiries, clarifications and prices are all being handled from a
personal account, across the working day and into the evening. Across three days no qualifying
question was asked — not what kind of scarring, not how long, not what had been tried, not when the
patient could come in. No appointment was offered at any point.

**Possible problem.** With **5,966 Practo patient stories** against 1,613 Google reviews, Practo Prime
is a paid channel carrying real volume — and those enquiries are landing on a personal handset under
the doctor's own name. Whoever is answering, they're answering *as* her, and the clinic's ability to
respond is bounded by whatever that one account can absorb between patients.

The second half is the harder one: nothing was captured. A price went out and there's no record of
who asked, what for, or what happened next — which makes the outcome of a quote not just unknown but
unknowable.

**Can't confirm.** **Who actually holds the phone** — the account is personal, but that doesn't
establish that the doctor types every message. Whether Practo enquiries land elsewhere first. What
share of enquiries route here. Whether anything is written down somewhere else.

**The question.** Of the people quoted a price last month, how many booked — and where would that be
looked up?

**⚠️ Three hard constraints.**
- **Do not claim she personally typed the replies.** The screenshot proves the account is personal,
  not who is on it. Asserting more is exactly the failure `MEMORY.md` §2 logs — an inferred behaviour
  stated as fact. *"Whoever is answering it is answering as you"* is true either way and lands as well.
- **Do not say "then silence."** She answered every message. Saying otherwise hands her a
  one-screenshot refutation.
- **The 9:39 PM → 11:14 AM gap is after-hours and inadmissible** under §2.0.

**Build notes.** Fully unblocked. Lead with the screenshot, **never** her reviews — her one reply on
record to a critical Practo review was combative. Hold the 1★ of 14/7/26 in reserve. If the draft
reads as criticism of her rather than a question about the system, it's wrong.

---

### 1.4 VIDA Skin & Hair

**Observed fact.** 11/8, 5:23 PM: *"Ok, could you send over a pricing/quote brochure or details for
the treatments."* 6:08 PM: *"It start from 3500 to 6500."* No brochure. Two numbers with no treatment
attached to either. No next step offered. Nothing since — three days.

**Observation.** The opening was excellent — 4:39 PM on 10/8, two minutes after the enquiry:
*"Hello Tilak sir / This is Indira from Vida skin and hair transplant clinic / What treatment you are
looking for skin sir?"* Named, warm, and it asked the right question straight away. What came back at
the pricing stage was a range the patient can't act on: they don't know which treatment is ₹3,500,
which is ₹6,500, or what either includes.

**Possible problem.** The greeting is clearly a routine and it runs well. Pricing may not be a
routine at all. If there's nothing prepared to send, then every price question becomes something
somebody has to answer from memory while doing three other things — and what comes out is the
shortest true thing available. A patient comparing two or three clinics can't do anything with
"3500 to 6500," so the decision quietly moves to whoever gave them something clearer.

**Can't confirm.** Whether a brochure exists at all. Whether Indira covers every channel. Whether
prices vary enough that a range is the honest answer. Whether Practo enquiries are handled differently.

**The question.** When a patient asks what something costs, what does the person answering actually
have in front of them?

**Build notes.** **Drop the timing entirely** — 40 and 45 minutes were in my earlier draft as a
"degradation curve" and the rebuttal *"forty-five minutes is fast"* is correct and complete. The
failure was never the clock; it was that a specific request produced an unusable answer. **Do not
sell speed** — Notion's note is right, they have it and are right to be proud of it. Money is
confirmed on two channels (12 Google creatives active, advertiser *Jigisha jalu*, last shown 7/8/26;
Practo Prime, 302 patient stories). DM-1 went to the brand account — consider addressing Dr. Jigisha
N. Jalu by name. **Do not raise** the pricing-pressure reviews.

---

### 1.5 Dermatonik

**Observed fact.** 10/8, 4:34 PM enquiry → **4:34 PM** auto-reply: *"Please let us know your
concern"* → **4:37 PM** before/after acne collages → 4:39 PM clinic photos and a Google profile card.
11/8, 4:31 PM pricing request → **4:34 PM**: *"Starting 5500/-Once you come For Consultation with
Doctor Accordingly I can help you better."* Nothing since — three days.

**Observation.** This is the most generous first response of the twelve. Instant acknowledgement,
real before/after work within three minutes, a starting price inside three minutes the next day.
And in three days, not one question came back — not what kind of acne, not how long, not what had
been tried, not when they could come in. The clinic's own welcome message asked for the patient's
concern; the patient answered *"acne"*; nobody ever picked it up.

**Possible problem.** Everything here flows outward. Photos, prices, links — all sent quickly and
willingly. But if nothing comes back the other way, then from inside the clinic every enquiry looks
identical. The person ready to start a ₹50,000 course next week and the person browsing on their
lunch break both receive the same collage and the same "starting 5500," and there's no way to tell
which was which afterwards. That's a particular waste here, because the traffic is bought: **four
active Meta ads** running *"Upto 50% OFF"*, and the **longest-running Google presence of the twelve** —
near-continuous for close to a year across two advertiser entities, still live.

A second, independent instance points the same way: a 1★ of 29/6/26 describes being told by phone
that a dermatologist was available, arriving to find none, and being charged ₹700 anyway. What gets
told to a patient before they arrive isn't tracked either.

**Can't confirm.** Whether phone enquiries are qualified differently. Whether anyone follows up by
call. How many enquiries the ad spend produces. Who the treating dermatologist is.

**The question.** Of the people who got a price last month, is there any way to tell which ones were
serious?

**Build notes.** Anticipated rebuttal: *"we assess properly at the consultation."* Correct, and the
document must not appear to argue with it — the gap isn't clinical assessment, it's knowing which
enquiry is worth a phone call before they ever arrive. **Keep this document visibly distinct from
Gejje's**: that one withheld everything, this one gave everything and asked nothing. **Decide the
addressee first** — DM-1 went to Dr. Saeema Shiraaz, while all three ownership signals point at
Anjali Sanghvi, who is not evidenced to be a physician.

---

### 1.6 Project Skin

**Observed fact.** 10/8, 4:43 PM enquiry → an automated reply the same minute:
*"Hey. Thanks for reaching out! We will get back to you soon."* Nobody did that day. 11/8, 2:24 PM
the patient messaged again → **2:25 PM, sixty seconds**, a human: *"Hi, chemical peels and carbon
Laser works well for acne."* Full pricing followed on 12/8.

**Observation.** The message that promises a callback is the one that didn't produce one. The patient
got a fast, helpful human — but only after taking a second run at it himself.

**Possible problem.** Responsiveness isn't the issue; when a message is in front of this team they
answer in a minute. What may be missing is anything that puts an *unanswered* thread back in front of
someone. If nothing marks "this one got the welcome message and nothing after it," then the patients
who read *"we will get back to you soon"*, believe it, and wait are exactly the ones who disappear —
and they disappear quietly. They don't complain, they don't leave a review, and nothing in any report
shows a patient who never became one.

Context, stated once: **11 Google creatives running continuously since June 2025**, one live the day
before the test, and the website's only capture is a name/number/email form with no treatment,
concern or timeline field.

**Can't confirm.** Whether the auto-reply notifies anyone. How many threads sit acknowledged and
unanswered. Whether the website form is handled differently. Whether the second message got through
because someone was already in the inbox.

**The question.** If an enquiry got the welcome message and then nothing at all, where would that
show up?

**Build notes.** **Concede the 60-second reply explicitly and build on it** — claiming nobody replied
is false and refutable in one scroll. The double bot-fire is colour, not evidence; leading on it
reads as a gotcha. **Ownership unresolved** — a 5★ review says *"the owners manage the clinic"*,
plural, and the LLP structure fits multiple partners; multi-partner sign-off is a hard kill under
§1.1 #5. MCA on ASJ Aesthetic Clinics LLP before sending.

---

### 1.7 Gejje's Marvella

**Observed fact.** 10/8, 3:00 PM → instant auto-reply listing specialties, credentials, both
locations and the website, closing: *"Kindly share your concern, preferred location, and photos (if
comfortable) — our team will assist you."* 11/8, 4:34 PM: *"could you provide more info on acne and
scars treatment?"* → **5:01 PM**: *"Yes . Treatment available"* / *"Visit the clinic."*

**Observation.** The automated message asks for three specific things. No human returned to any of
them — never re-asked the concern, never asked which branch, never asked for the photos the clinic
itself had requested. Every human reply pointed at an in-person visit without collecting anything
first.

**Possible problem.** Somebody set that welcome message up and knew exactly what a patient should be
asked. Whatever the patient sends back may not reach anyone. If those answers aren't recorded or
handed on, the automation is doing introduction work rather than intake work — and whoever picks up
the thread starts from nothing every time, which is roughly what *"Yes . Treatment available"* sounds
like from the patient's side.

**Can't confirm.** Whether the auto-reply's answers go anywhere. Whether these response times are
typical. Whether photos get requested by phone instead. Whether the two locations share an inbox.

**The question.** When a patient does send their concern and photos as the welcome message asks, who
receives them — and what happens next?

**⚠️ Admissibility.** The pricing request went at **9:40 PM** and was answered 8:07 AM. After-hours,
**inadmissible** under §2.0, must not appear. Use the 11/8 4:34 PM → 5:01 PM exchange.

**Build notes. BLOCKED** — founder uncorroborated; Dr. Somashekar Gejje appears only on the
user-supplied list. Notion: *do not draft until verified.* Two minutes of work. **Zero ad spend
anywhere**, so no money-at-stake framing is available; 870 reviews at 5.0★ is what this is built
against. Don't lead on the 56-minute or 27-minute gaps — both are rebuttable. And note the price
refusal is genuinely defensible (*"pricing needs an examination"*), so the document must not go there.

---

### 1.8 Derma Solutions — ⚠️ no screenshot

**Observed fact (Notion prose, unverified by me).** Reply in **60 seconds**: *"Sure. Please visit our
website it's all mentioned there"*, plus links to the site, Facebook, Instagram and YouTube.

**Observation.** Someone was live and answered immediately — and the answer sent the patient back to
the internet. No concern asked, no treatment asked, no price, no appointment offered.

**Possible problem.** The speed is real; there was just nothing to say. If whoever holds the phone
has no prepared answers, the quickest true response is a link — which returns the patient to exactly
where they were before they messaged. With **1,649 Practo patient stories**, two Prime-badged doctors
and no Meta or Google spend at all, Practo *is* the acquisition strategy: the enquiry is paid for per
lead, and the reply hands it straight back.

**Can't confirm.** Who answers. Whether anything sendable exists. Whether a phone call goes
differently. Whether anyone follows up later.

**The question.** What does the person answering WhatsApp have to send that the website doesn't
already say?

**Build notes. BLOCKED on the screenshot.** Best founder access of the twelve — personal mobile
+91 99164 24736 and sandip.derm@gmail.com — and the only clinic contacted by email. Lead with the
screenshot, never the reviews: the owner's one reply on record to a serious complaint was combative.
Hold 0/10 negative-reply rate and 7.2% one-star (89 of 1,241, highest in the batch) in reserve.

---

### 1.9 Haircosmos International — ⚠️ no screenshot

**Observed fact (Notion prose, unverified by me).** *"How can i help you"* in **3 minutes**. The
follow-up — what treatments do you offer — answered **2 hours 26 minutes** later: *"we have"* /
*"gfc exosome qr678 prp"*. No price, no explanation, no next step.

**Observation.** Fast to greet. Slow on the first question that needed real knowledge — and the
answer, when it came, was four words of clinical shorthand.

**Possible problem.** Saying hello and answering properly may be two different jobs sitting with two
different people. If whoever holds the phone can greet but has to find someone else for anything
substantive, then the wait gets longer the more important the question is — the opposite of what a
**₹49,999** decision needs. And *"gfc exosome qr678 prp"* assumes someone who already knows what
those are; a patient comparing clinics on a fifty-thousand-rupee procedure usually doesn't.

Two independent reviews point the same way — an unresolved post-procedure scalp infection
(1★, 28/7/26) and a doctor no-show (1★, 4/4/26), both unanswered. **0 of 8 negative reviews replied
to across both branches.**

**Can't confirm.** Who answers. Whether a price list exists. Whether phone enquiries differ. Whether
that afternoon was unusual.

**The question.** Who's meant to answer a treatment question — and what happens to the enquiry while
they're with a patient?

**Build notes. BLOCKED twice** — no screenshot, and no founder named anywhere; the LinkedIn page is
abandoned (blank headline, 0 connections, 1 follower). DM-1 went to Dr. Saima Khan, an IG follower,
not a confirmed principal. **3 live Meta ads** (hair transplant from ₹49,999, hair patch ₹9,999,
0% EMI), Google lapsed since Dec 2025 — Meta is the only paid tap and it points at this inbox.

---

### 1.10 Vitals Klinic — no document

See §0.2. To keep it warm, the honest move is the inverse of a diagnostic: tell them their WhatsApp
handling was the best of the twelve tested and ask what they built it on. Real opener, costs nothing,
not a follow-up-2 document.

---

## 2. Ship order

| # | Clinic | Leads on | Status |
|---|---|---|---|
| 1 | **Akera Health** | The only clinic of twelve where an enquiry got no acknowledgement at all | Ready — founder ID outstanding |
| 2 | **Ara Skin** | The patient who said "just send it to me" | **Fully unblocked** |
| 3 | **Dr. Priya's** | The clinic's published number is a personal account | **Fully unblocked** |
| 4 | **VIDA** | A price range with nothing attached to either number | **Fully unblocked** |
| 5 | **Dermatonik** | Everything sent outward, nothing asked back | Ready — decide the addressee |
| 6 | **Project Skin** | The message that promises a callback is the one that didn't produce one | Ready — ownership check outstanding |
| 7 | **Gejje's Marvella** | The welcome message asks three things nobody uses | **Blocked** — verify founder (2 min) |
| 8 | **Derma Solutions** | Sixty seconds, and a link | **Blocked** — no screenshot |
| 9 | **Haircosmos** | The wait gets longer the more the question matters | **Blocked** — no screenshot, no founder |
| — | **Vitals Klinic** | — | **Do not send** |

---

## 3. What decides whether these convert — and it isn't the observation

The observations are now genuinely stronger than the previous fifteen: first-party, dated,
screenshot-backed, and each one survives a rebuttal attempt. That's a real upgrade.

**It is probably not the thing that converts.** The record on this asset is ~25 sent, 2 replies,
**0 calls**, and the audit's diagnosis was that the *ask* fails, not the finding — *"at the exact
moment the reader is most impressed, the ask is: would you like more of what you just got, but
longer, and on a call with a stranger?"* Sharpening nine observations does not touch that.

Three things that plausibly do:

1. **The close.** Still undecided, and it's where the leverage is. The playbook now requires a
   specific named thing plus two named slots, not a free audit.
2. **Something they can test.** The WhatsApp demo is **built and live**, and not one of these nine
   documents currently uses it. `OUTBOUND_MEMORY.md` §5b: a claim they can test is the only real
   evidence a company with no clients has. Ending on *"here's a number — message it the way a patient
   would"* costs them twenty seconds and nothing else in the folder comes close to that.
3. **Whether she feels recognised or surveilled.** Nine of these say, however politely, *I tested you
   and found something*. Bangalore aesthetic dermatology is a small world — same conferences, same
   device reps, same WhatsApp groups. Two of these landing on the same table dissolves the
   personalisation instantly. Worth rotating structure hard, and worth considering whether nine go
   out at once or in two waves.

### Format rules that bind these

From `10 Tooling/one-pager-handoff/CLAUDE.md` — it reverses three older rules, and the files in
`one-pager-handoff/examples/` violate all of them. Copy the scaffold, not the words.

- **250–350 words. Enforced.** The previous fifteen ran 529–703.
- **Sign with a real name** — *"— Tilak, Valence Ops"* — plus *"This is a read on public information
  and one test enquiry — not clinic data. Happy to be told where it's wrong."*
- **The close is the question, not a meeting ask.**
- **Never say "free"** — "at no cost to the clinic".
- **Never invent a number**, not even a range.
- **Rotate the structure** — the same subhead ran verbatim in 10 of 10 previous documents.
- **No superlatives.** Brand name exactly once.
- **Nothing about the service.** Confirmed / can't confirm / would check first — then the question.

---

## 4. Final angles — the build sheet

> **Truth pass, 14/8.** Every angle re-checked against the raw screenshot rather than against my own
> notes. All ten screenshots have now been read directly — including `gejjes-marvella.png`,
> `dermatonik-1.png` and `vital-skin-1.png`, which I had described before opening. The quotes held,
> but three angles did not survive as phrased and are corrected below. Two got stronger.
>
> **Corrected:** Akera (the comparison can't be said out loud) · Dr. Priya's (the angle was true but
> not news to her) · VIDA (one clause was overstated).
> **Strengthened by verification:** Gejje's · Project Skin (scoped honestly, it improves).
> **Cannot be evaluated at all:** Derma Solutions and Haircosmos — still no screenshot.

One angle per clinic. **The line** is what the document is built to make her remember — the
`diagnostic_doc_playbook.md` §8.3 one-sentence test. If three sentences compete for that role in a
draft, two get cut. **The question** is the close. **Never** is what sinks the document if it appears.

---

**1 · Akera Health** — *Nothing was listening.* ⚠️ corrected

> **The line:** A message arrived at 4:23 on a Monday afternoon and nothing acknowledged it — not a
> person, not an automatic reply — until 11:31 the next morning.

- **Opens on:** those two timestamps and the emptiness between them.
- **Turn:** the nineteen hours is what happened; the fact that nothing automatic exists on that
  channel is *why it could*. One of those is arguable — *"that was one bad evening"* — and the other
  isn't. An auto-reply either exists or it doesn't, and here it doesn't.
- **Second beat:** once someone did pick it up the handling was good — 12 minutes to a treatment
  answer, 8 more to itemised pricing. This was never a skill problem.
- **The question:** Of the WhatsApp enquiries that arrived last month, how many got a reply the same
  day — and is there anywhere that could be looked up?

**⚠️ What changed and why.** The earlier version opened *"twelve clinics were messaged that week;
yours was the only one where nothing answered."* The comparison is **factually true** — verified
across all ten screenshots plus the Krity and Theory records — but it **cannot be said to her.**
`MEMORY.md` §2 logs this exactly: a several-clinics framing signals mass-sender and is *"worse than
silence."* Telling Akera she was one of twelve tested reframes the whole document as a sweep.

The comparison stays internal. It's why this clinic is first in the queue; it never appears on the page.

- **Never:** the twelve-clinic comparison. And never lead with the ad count — *"You run 25 ads" →
  "And?"* Ads attach to the first-party fact, never carry it.

---

**2 · Ara Skin Clinic** — *The patient who said "just send it to me."*

> **The line:** You answered in two minutes when the reply offered a call. When he said he was at
> work and asked twice for it in writing, that was the end of the conversation.

- **Opens on:** 4:35 PM *"Can we call you sir"* → 4:36 PM *"busy with work, could you drop the info
  here"* → 4:37 PM *"so that i could have a look"* → three days of nothing.
- **Turn:** nobody decided to drop it. There just wasn't a next step once the call was declined.
- **Second beat:** four of four negative reviews answered personally. Attention isn't what's missing.
- **The question:** When a patient says "just send it to me," what's supposed to happen — and who
  decides?
- **Never:** the 18-minute reply, and never any claim of ad spend — the Google creatives belong to
  *"Pure Dermacare"* with no established link.

---

**3 · Dr. Priya's Skin & Hair** — *The price went out. Nothing asked him to come in.* ⚠️ corrected

> **The line:** He was sent a full price list — MNRF 9.5k, dermapen 10k, MDF 8.5k. Nobody asked him
> when he could come in, on any of the three days.

- **Opens on:** the price list itself at 11:14 AM, and the fact that it arrived from a personal
  WhatsApp account under her own name — `~Dr Priya J Talageri`, no business account.
- **Turn:** the numbers went out; nothing came back the other way and no appointment was ever
  offered. Nothing recorded who asked, what for, or what happened next — so the outcome of that quote
  isn't just unknown, it's unknowable.
- **Second beat:** 5,966 Practo patient stories against 1,613 Google reviews. That volume is paid
  for, and it lands on this number.
- **The question:** Of the people quoted a price last month, how many booked — and where would that
  be looked up?

**⚠️ What changed and why.** Two problems with the earlier version.

*"The number on your listing is your own"* is **true but not news to her.** She knows whose phone it
is. An observation she already holds isn't an observation — it's the setting. So the personal account
becomes context and the unanswered price becomes the point.

And *"no qualifying question was asked"* **doesn't survive contact with the screenshot.** She asked
*"regarding ?"* at 4:23 PM and *"U r asking about procedure?"* at 7:07 PM. Those are questions. I read
them as clarifying rather than qualifying, but that's my interpretation and she'd rebut it in one
line — *"I did ask what he wanted."* What she cannot rebut: **no appointment was offered at any point
across three days.** Binary, checkable, and it's the thing that actually costs her money.

- **Never:** claim she typed the messages herself (the account is personal; who holds it isn't
  proven), never say "silence" (false — she answered every message), never use the 9:39 PM → 11:14 AM
  gap (inadmissible under §2.0), never lead with her reviews.

---

**4 · VIDA Skin & Hair** — *He asked for something to look at. He got a starting figure.* ⚠️ corrected

> **The line:** He asked for a pricing brochure or details. What came back, forty-five minutes later,
> was one line: "It start from 3500 to 6500."

**⚠️ What changed and why.** The earlier line ended *"two numbers with nothing attached to either
one."* That's **overstated.** The message before it named acne clean-up and MNRF, so a reader could
reasonably map the two numbers onto the two treatments. She'd spot that.

What's unarguable is narrower and still enough: he asked for a brochure, no brochure exists or none
was sent, and *"start from"* means the real number is still unknown. A patient comparing two or three
clinics has nothing to compare.

- **Opens on:** the excellent bit first — 4:39 PM, *"Hello Tilak sir / This is Indira from Vida skin
  and hair transplant clinic / What treatment you are looking for skin sir?"* Named, warm, right
  question, two minutes.
- **Turn:** a patient comparing two or three clinics can't do anything with a bare range, so the
  decision quietly moves to whoever gave them something clearer.
- **The question:** When a patient asks what something costs, what does the person answering actually
  have in front of them?
- **Never:** the 40- and 45-minute gaps. *"Forty-five minutes is fast"* is a correct rebuttal and it
  takes the whole document with it. Never sell speed here.

---

**5 · Dermatonik** — *Everything went out. Nothing came back.*

> **The line:** Your welcome message asks the patient for their concern. He answered "acne." Over
> three days, nobody asked him anything else.

- **Opens on:** the generosity — instant acknowledgement, before/after work in three minutes,
  a starting price in three minutes the next day. Most open-handed first response of the twelve.
- **Turn:** if nothing comes back the other way, the person ready to start a ₹50,000 course and the
  person browsing at lunch get the same collage and the same "starting 5500" — and afterwards there's
  no way to tell which was which.
- **Second beat:** a year of near-continuous Google spend across two advertiser entities, plus four
  live Meta ads running *"Upto 50% OFF"*.
- **The question:** Of the people who got a price last month, is there a way to tell which ones were
  serious?
- **Never:** appear to argue with *"we assess properly at the consultation."* The gap isn't clinical
  assessment — it's knowing which enquiry is worth a call before anyone arrives.

---

**6 · Project Skin** — *The message that promised, and the one that delivered.*

> **The line:** "We will get back to you soon" was the only message that didn't lead anywhere. He got
> a real answer in sixty seconds — but only after messaging you a second time himself.

- **Opens on:** 4:43 PM Monday, the promise. Nothing that day. 2:24 PM Tuesday he tries again →
  2:25 PM a human answers.
- **Turn:** the patients who read that line, believe it, and wait are the ones who disappear — and
  they disappear quietly. No complaint, no review, nothing in any report showing a patient who never
  became one.
- **Second beat:** eleven Google creatives running continuously since June 2025, one live the day
  before.
- **The question:** If an enquiry got the welcome message and then nothing at all, where would that
  show up?
- **Never:** claim nobody replied. Concede the sixty seconds explicitly — the document works *because*
  of it. Double bot-fire is colour, not evidence.

**Scope it honestly, and it gets better.** We cannot claim nobody would *ever* have come back — the
patient messaged again the next afternoon, which ended the test. What's provable is narrower: the
message said *soon*, and twenty-two hours later nothing had come. Saying that limitation out loud is
the register `diagnostic_doc_playbook.md` §2 calls for — *here's what we could verify, here's what we
couldn't* — and a doctor trusts it more than a confident claim she can poke a hole in.

---

**7 · Gejje's Marvella** — *The welcome message asks three things. Nobody used any of them.* ✅ verified verbatim

> **The line:** Your automatic reply asks for the concern, the preferred location, and photos.
> Across three days and three replies, none of the three was ever mentioned again.

- **Opens on:** the auto-reply, quoted. It is genuinely the best of the twelve — specialties,
  board certification, 15+ years, both locations, website, then: *"Kindly share your concern,
  preferred location, and photos (if comfortable). Our team will assist you."*
- **The three replies that followed, in full:** *"Hlo... yes tell me"* · *"Yes . Treatment available"* /
  *"Visit the clinic"* · *"It depends on the area and treatment. Kindly have a consultation, doctor
  will explain."*
- **Turn:** somebody built that welcome message knowing exactly what a patient should be asked.
  Whatever a patient sends back doesn't appear to reach anyone — so every thread starts from nothing,
  which is what *"Yes . Treatment available"* sounds like from the patient's side.
- **The question:** When a patient does send their concern and photos as the welcome message asks,
  who receives them — and what happens next?
- **Never:** the 9:40 PM → 8:07 AM exchange (after-hours, inadmissible). Never go near price —
  *"pricing needs an examination"* is a complete and correct rebuttal.

**Two things the screenshot added.** The auto-reply reads *"Led by board-certified specialists"* —
plural, and **no doctor is named even in the clinic's own welcome message.** That independently
corroborates the founder problem: this clinic does not name a clinician anywhere, including to its
own patients. It also sharpens the angle — the automation is thorough about everything except who
you would actually be seeing.

It also confirms a second location: *"Bengaluru & Vijayanagara (Hospet)"*, which the dossier had
flagged as an unverified lead off a stray GBP email. Now corroborated from the clinic's own message.

---

**8 · Derma Solutions** — *A minute, and a link.* ⚠️ screenshot missing

> **The line:** Someone answered in under a minute — and sent him back to the website he'd already
> been reading.

- **Opens on:** *"Sure. Please visit our website it's all mentioned there"* plus four links.
- **Turn:** the speed is real; there was just nothing to say. The fastest true answer available was a
  link, which returns the patient to exactly where he started.
- **Second beat:** 1,649 Practo patient stories, two Prime-badged doctors, no Meta or Google spend at
  all. The enquiry is paid for per lead, then handed straight back.
- **The question:** What does the person answering WhatsApp have to send that the website doesn't
  already say?
- **Never:** the reviews. The one owner reply on record to a serious complaint was combative.

---

**9 · Haircosmos International** — *The wait grows with the stakes.* ⚠️ screenshot missing

> **The line:** Three minutes to say hello. Two and a half hours to answer what you actually treat.

- **Opens on:** *"How can i help you"* at 3 minutes → *"we have"* / *"gfc exosome qr678 prp"* at
  6:48 PM.
- **Turn:** greeting and answering look like two different jobs held by two different people — so the
  wait gets longer the more the question matters. That's the wrong way round for a ₹49,999 decision.
- **Second beat:** *"gfc exosome qr678 prp"* assumes a reader who already knows what those are.
  Someone comparing clinics on fifty thousand rupees usually doesn't.
- **The question:** Who's meant to answer a treatment question — and what happens to the enquiry
  while they're with a patient?
- **Never:** send this at all until the screenshot exists and a principal is named.

---

**10 · Vitals Klinic** — *The inverse. Not a diagnostic document.*

> **The line:** Of the twelve clinics tested that week, yours was the only one that followed up on
> its own, before being asked.

- **Opens on:** the 5:39 PM unprompted check-in, an hour after the first reply.
- **Why this and not a diagnostic:** they run instant reply, a qualifying question, proactive chase,
  itemised pricing, branch routing and a native booking form. Cold to bookable in four minutes.
  A document telling them their enquiry handling leaks gets answered with a screenshot of their own bot.
- **The question:** What did you build it on?
- **Format:** a short message, not a one-pager. It's a real opener and it costs nothing — but it is
  not a follow-up-2 document, and shouldn't be dressed as one.

---

### Still open

The close. Every angle above ends on its question, per the playbook. What follows the question —
the specific named thing plus two slots, and whether the live WhatsApp demo appears in it — is
undecided, and on the evidence of ~25 sent / 2 replies / 0 calls it matters more than any line above.
