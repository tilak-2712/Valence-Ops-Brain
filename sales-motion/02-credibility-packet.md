# 02 — The Credibility Packet

**Owns:** Stage 1. Everything that must be true *before* the call so the call can be entirely about their clinic.

**The constraint this exists to satisfy:** on the operations call you get roughly 50 minutes of a clinic owner's attention. Every minute spent explaining what ValenceOps is, or establishing that you're not a time-waster, is stolen from diagnosis. So all of it moves async, into things they consume on their own time, at their own pace, more than once if they want.

**Secondary effect worth being honest about:** the packet also disqualifies people. A founder who watches six minutes and books a call is materially warmer than one who agrees to a call cold. Fewer calls, better calls, is the right trade at two people.

---

## What's in it

| Asset | Effort | Reuse | Priority |
|---|---|---|---|
| Walkthrough video (6 min) | Half a day once | Every reply forever | **Build first** |
| `HOW-WE-WORK` PDF | Written — needs design pass | Every reply forever | **Build first** |
| Live demo WhatsApp number | — | Every reply forever | ✅ **Built 2026-08-13** |
| Personalized audit video (3–4 min) | 25 min per clinic | One clinic | Priority-1 rows only |

The first two ship together as the default packet. The demo gets mentioned in the message and used live on the call. The personalized video is an upgrade, not a requirement.

---

## Asset 1 — The walkthrough video (6 minutes, recorded once)

**Format:** screen recording with your face in the corner. Loom, or anything equivalent. Recorded once, sent to every clinic that replies.

**On polish:** don't over-produce it. A clean single take with a couple of "let me show you" moments reads as a founder who knows their thing. A scripted, edited, music-bedded video reads as an agency, and agency is the exact thing this audience has been burned by. One or two verbal stumbles left in is a feature.

**Do not use the word "AI" before the four-minute mark.** `OUTBOUND_MEMORY.md` §3 — outcomes first, mechanism only if asked. Show what happens; name the technology later or not at all.

### Script

**[0:00–0:35] Who and why**
> I'm Tilak, one of two people at Valence Ops. This is a six-minute version of what we do, so that if we end up speaking, we can spend that time on your clinic instead of on us.
>
> Straight up, before anything else: we're early. We don't have a folder of clinic case studies to show you. I'd rather you hear that from me in the first thirty seconds than work it out on a call. What I can do is show you exactly how this works and let you test it yourself — that's most of what this video is.

**[0:35–1:35] The problem, in their language**
> Most of what gets sold to clinics is about getting more people to message you. We don't do that at all.
>
> What we work on is what happens after someone messages. Somebody asks about laser on WhatsApp at nine at night. Somebody books a consult for Thursday and doesn't turn up. Somebody comes in, gets a quote for a package, says they'll think about it, and nobody ever follows up because the front desk is busy with the people who are actually standing there.
>
> None of that shows up anywhere. There's no report that says "we lost eleven people this month at the quote stage." The patient just doesn't come back, and nobody knows it happened. That's the part we work on.

**[1:35–4:15] The system, on screen**
Screen share the demo clinic. Show, don't narrate.

> Let me show you rather than describe it. This is a demo clinic we set up — a real WhatsApp number, and you can message it yourself after this if you want.
>
> *[Send a message from your phone on screen, at a visibly late hour]* Here's a patient asking about hair transplant pricing at 11pm. Watch what comes back.
>
> *[Show the reply]* Two things I'd point out. It doesn't pretend to be a person. And it doesn't just say "we'll get back to you in the morning" — it asks what they came for. Which treatment, roughly when they're thinking, which branch.
>
> *[Show the coordinator view]* So when your coordinator opens this at nine the next morning, they're not starting from "hi." They've got a name, a number, what the person actually wants, and when. They can pick up the phone and open with something useful.
>
> *[Show the handoff]* And the second your coordinator replies, the automated side stops. It doesn't talk over your staff. That's usually the first thing owners ask about.
>
> *[Show no-show flow]* Same idea after a booking. Someone books for Thursday, doesn't show — right now most clinics do nothing, because there's no list. Here it goes out within the hour, while it's still a rescheduling conversation rather than an awkward one.

**[4:15–5:15] What a first month looks like**
> If we work together, the first thing is a call — about half an hour, mostly me asking questions about how enquiries move through your clinic. I don't pitch on that call.
>
> Then a short document: what I found, the three things that seem to be costing you most, and which one I'd fix first. You read it and decide.
>
> If you want to go ahead, we run one thing — not everything — for two to three weeks, free. Just that one thing, so you can see whether it does anything before you've spent money or changed how your team works.

**[5:15–6:00] The ask, and the honest close**
> What we need from you is small at the start. Mostly access to see what's already happening, and one person at your end who can reply to us within a few hours when something needs a decision. That second one matters more than it sounds — it's the thing that decides whether this works.
>
> And on us being early — the trade is real in both directions. You don't get a track record. You do get the two people who built this working on your clinic directly, because right now there's nobody else for us to hand it to.
>
> If that's worth half an hour, the times are in the message. Thanks for watching this far.

**Framing sentence when you send it** *(the video won't get watched without one)*:
> Six minutes, and about half of it is me showing you the thing running rather than talking about it.

---

## Asset 2 — The HOW WE WORK document

Content lives in `client-facing/HOW-WE-WORK.md`. Design notes:

- Four pages. Not eight. If it runs long, cut before designing.
- Same typographic system as the diagnostic one-pagers — editorial serif for narrative, monospace for labels and terms (`diagnostic_doc_playbook.md` §6). It should be visibly from the same firm as the one-pager they already received.
- "Valence Ops" appears once, and both names appear — this document, unlike the one-pager, is *about* who you are, so the no-personal-names rule is deliberately reversed here.
- No stock photography. No icons of handshakes or gears. Restraint reads as premium; polish reads as agency.
- **Section order is load-bearing.** "We're early" is page 3 of 4, after method and before commercials — early enough to be volunteered, late enough that they already understand what's on offer. Do not move it to the back.

---

## Asset 3 — The demo clinic ✅ BUILT — confirmed 2026-08-13

> **What is live:** WhatsApp automation with lead qualification and booking. Hand them the number.
> **What is NOT live, and must be said unprompted:** no-show recovery, quote-decay chase and dormant
> reactivation are walked through as the actual message sequences, never demoed. They need real CRM
> state and a real missed appointment to mean anything; staging one per clinic doesn't scale and a
> staged no-show proves nothing. Full split in `OUTBOUND_MEMORY.md` §5b. Naming the limit yourself is
> method transparency; letting them find it is a credibility hit.

**Why this is the highest-return thing on the list:** with zero clients, every credibility claim is a claim. A demo the founder can message from their own phone is not a claim — it's a thing they tested. It converts "trust me" into "check for yourself," which is the only move available to a company with no results.

It also does something a video can't: it survives being forwarded. The founder shows it to their partner or their coordinator, and it works for them too.

### Spec

**Identity.** A fictional clinic — "Northline Skin & Hair (demo)" or similar. Explicitly labelled a demo everywhere. Never impersonate a real clinic, and never use a real clinic's name or branding.

**Number.** A dedicated WhatsApp Business number, separate from anything used for outreach. Keep the outreach number and the demo number apart — a demo number that starts sending cold DMs gets the account limited.

**Three flows. Three, not twelve.** A demo with twelve flows is a demo nobody finishes.

1. **After-hours capture.** Patient messages outside hours. Reply acknowledges, then asks three things: which treatment, rough timeline, which branch. Captures name and number. Ends with a real commitment ("someone will call you between 10 and 12 tomorrow") rather than an open-ended one.
2. **No-show recovery.** Booking exists, patient doesn't show. Message within the hour, warm, offers two concrete alternative slots rather than asking them to suggest one.
3. **Quote follow-up.** Consult happened, quote given, silence. A message at 48 hours that asks one question rather than repeating the offer.

**The coordinator view.** A simple sheet or dashboard showing what got captured, so the founder sees what their front desk would actually receive in the morning. This half is what sells it — the patient-side message is nice; the "your coordinator opens this and already knows what to say" is the point.

**The handoff demo.** Be able to show, live, the automation stopping mid-conversation the moment a human replies. Every owner asks about collision with their staff (`Audit_call_docs/03` QE3 records this as the biggest adoption risk). Showing it is worth more than any reassurance.

**Guardrails to build in and mention:**
- Nothing claims to be a human.
- No medical advice, ever — any clinical question routes to a person immediately.
- No patient data leaves the clinic's own systems. Say this plainly; DPDP and medical data make this a real concern, not a checkbox.

**How to use it on the call:** ask them to message it, live, from their own phone, while you're both on the call. Ten seconds of them watching a reply land on their own screen does more than the whole video.

---

## Asset 4 — The personalized audit video (Priority-1 only)

Three to four minutes, screen-recorded, walking through *their* audit. ~25 minutes to make. Reserve it for Priority-1 rows in the Notion tracker — it doesn't scale and doesn't need to.

**Structure, mirroring the one-pager's honesty mechanic** (`diagnostic_doc_playbook.md` §4):

1. **[0:00–0:30]** Why you made this specifically for them.
2. **[0:30–1:15] The observed fact.** On screen: the actual WhatsApp thread, the timestamps, the gap. No interpretation. Just show it.
3. **[1:15–2:00] What that means at a systems level.** Not "you replied slowly" — that's dismissible and a coordinator being asleep explains it. The insight is that there's currently no way for anyone, including them, to know whether this happens once a month or every night.
4. **[2:00–2:45] What you couldn't confirm.** Name the honest gaps out loud. This is the part that builds trust — a stranger admitting the limits of what he can see from outside is doing something no vendor does.
5. **[2:45–3:30] What you'd check first, and the ask.** One question they can only answer by looking at their own data. Then the two slots.

**Do not re-spend a fact already used in the cold sequence.** If the one-pager already used the midnight gap and the ad count in full, the video needs a different angle or it's the fourth telling of the same thing. `MEMORY.md` §2 flags this exact failure on Cozmo Blis.

---

## Self-check before any packet goes out

1. Is there a date or two named slots in the same message? *(Rule 1. Most common miss.)*
2. Does the "we're early" line appear before anyone had to ask?
3. Any banned vocabulary — leads, funnel, conversion, ROI, growth, scale, infrastructure? *(`OUTBOUND_MEMORY.md` §3)*
4. Any number claimed that isn't verified? *(No patient counts. No revenue estimates. Ever.)*
5. Does "AI" appear before the four-minute mark of the video, or anywhere in the covering message?
6. Would a clinic owner say these sentences out loud, in these words? *(`MEMORY.md` §2 — the translation check.)*
7. Is the packet more polished than the one-pager that preceded it? *(A jump in polish is a tell. `diagnostic_doc_playbook.md` §5.)*
