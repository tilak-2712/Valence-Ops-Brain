---
date_created: 2026-08-14
date_modified: 2026-08-14
status: reference
---
# The One-Pager — Steel-Man Review
*2026-08-14. Reviews the 10 HTML/PDF diagnostics in `07 One-Pagers/` plus the 5 earlier PDF-only ones, the handoff kit, and the rules that now govern them.*

**Read `ONE-PAGER-AUDIT-AND-TEST-PLAN.md` (5 Aug) first — this does not repeat it.** That audit's diagnosis
(reply rate fine, calls-held is the metric; template convergence; word bloat; wrong CTA) is correct and I
am not re-litigating it. This file contains only what that audit missed, plus a test design that fits the
budget actually available.

---

## 0 · Verdict

**The document is excellent and it is in the wrong job.** It was designed as post-curiosity proof-of-work
(`diagnostic_doc_playbook.md` §1, first line) and is being fired as a cold touch-2 lead magnet. Almost
every problem below is a symptom of that one misplacement, not of the writing.

**Don't A/B two one-pagers against each other.** At this volume that test cannot return a readable
answer, and the touch budget left before the tripwire fires is less than one three-arm test. The
question worth spending the remaining touches on is not *which document wins* — it is *whether a
document belongs at this stage at all.*

**One thing I'd change before anything else, and it costs nothing:** the CTA. Not because the copy is
weak, but because the CTA adopted on 2026-08-13 (two named slots) contradicts a banned move adopted in
the same file on the same day. See §4.

---

## 1 · Steel-man — what is genuinely good and must survive any redesign

Four things here are better than what most agencies in this category ship, and a rewrite that loses them
would be a downgrade even if it converts better in the short run.

| What | Why it's actually good |
|---|---|
| **A timestamped first-party test of their own WhatsApp number** | Almost nobody does primary research on the prospect. This is real, unfakeable evidence about *them*, not a scraped fact. It is the single strongest asset in the project and every format below should keep it. |
| **The Three Buckets** (confirmed / can't confirm / would check first) | The best structural idea in the whole kit. It mirrors differential diagnosis — stated confidence, stated uncertainty, stated next test — which is a register a doctor already trusts professionally. Keep this even if you throw the document away. |
| **Never invent a number** | Correct and rare. "You're losing ₹4L a month" is the exact script this market has learned to detect. Holding this line under pressure is the reason a sharp reader doesn't discount the true lines. See §3.4 for the one class of number this rule is over-blocking. |
| **Compliment-first, then pivot** (`COPY_STANDARD.md` §3) | Right for a face-conscious, doctor-led, hierarchical market. The Ministry of Skin v1→v2 correction is a genuinely good piece of craft. |

The Aug-5 audit is harsh on this document. It is right about outcomes and slightly unfair about quality:
this is a well-made artifact. The problem is the slot, not the workmanship.

---

## 2 · Where the design bet is being undercut by its own execution

### 2.1 It is not a one-pager. It is a 1.5-page vertical strip delivered as a phone image. `confirmed`

Measured from the source files:

| Doc | Page size | vs. A4 height | Words |
|---|---|---|---|
| Vtiara | 210 × 456 mm | **1.54×** | 700 |
| DNA Skin | 210 × 444 mm | 1.49× | 703 |
| Ministry of Skin / Aesthetica Veda / Venkat / Dermaville | 210 × 438 mm | 1.47× | 552–622 |
| The Glow Clinic | 210 × 435 mm | 1.46× | 598 |
| Dr. Swetha's | 210 × 426 mm | 1.43× | 627 |
| **Dr. Dixit** | **A4** | **1.0×** | **529** |

Exported PDF: one page, 594.96 × 1233.12 pts. Exported JPG: **1868 × 3871 px — aspect ratio 1 : 2.07.**

Two consequences nobody has costed:

1. **The word-ceiling argument is downstream of this.** The page grew to fit the copy instead of the copy
   being cut to fit the page. That's why "enforce 250–350 words" has never once been complied with — the
   constraint that would have forced it was silently removed first. Fix the canvas back to A4 and the
   word count fixes itself. Note Dixit is the only doc that held A4 and the only one under 530 words.
2. **A 1 : 2.07 image is the wrong object for the channel it's sent on.** These go to WhatsApp as JPGs.
   In a chat bubble, a very tall image is scaled and cropped — which means the clinic name and the
   headline, the exact two elements the skim test in `COPY_STANDARD.md` §10.2 optimises for, are
   plausibly not visible until the recipient taps through and pinch-zooms. Body copy is 13.5px at
   1868px wide; at a ~300px chat-bubble render that is roughly 2px of type.

> **Verify this in 30 seconds and it costs zero touches:** WhatsApp one of the JPGs to yourself, and to
> two people on different phones. Look at the bubble *before* tapping. If the masthead and clinic name
> are cropped out, the most-sent asset in the project has been failing at the first half-second on every
> send, and no amount of copy work would ever have shown it. `hypothesis` until you look — but it is the
> cheapest check on this list and the highest-consequence one.

### 2.2 The title and the footer are the two strongest vendor tells on the page `confirmed`

The whole design bet (`diagnostic_doc_playbook.md` §7) is that a clinical case-file register earns a
doctor's trust structurally, without saying so. Two elements break that register:

- **"Revenue Diagnostic"** — set in the largest type block on the page. "Revenue" is agency vocabulary.
  `COPY_STANDARD.md` §1 bans *revenue leakage, ROI, funnel, conversion* on sight — and then the document's
  own title leads with the banned register. A doctor reads "Revenue Diagnostic" and knows in one word
  that this is a sales asset wearing a lab coat. **The document violates its own banned-vocabulary rule
  in its title.**
- **"Confidential — Prepared exclusively for [Clinic]"** — real confidential documents do not announce
  their own confidentiality. Pitch decks and agency proposals do. This line is doing the opposite of what
  it was designed to do: it is the single most legible "this is a template with your name merged into it"
  signal in the file.

Cheap fixes, no structural change: title it what it is — *"What happened when we messaged your WhatsApp"*
or *"Enquiry Diagnostic"* — and delete the confidentiality line entirely.

### 2.3 Production polish is a liability on a cold channel — and you already proved this once `confirmed`

`MEMORY.md` §2 logs the only confirmed craft learning in this project: a voice-note script written to the
same quality bar as written copy **failed when narrated**, and the conclusion drawn was that *"the
imperfections are the asset — an obviously one-pass human recording is precisely what outperforms the
polished email and deck that already got ignored. Written-copy polish is an active liability in spoken
channels."*

That learning has a wider form that was never applied: **production polish is a liability in cold
channels generally, not just spoken ones.** The more designed an asset is, the more loudly it announces
that money was spent to sell to the reader. A hand-built PDF with embedded fonts, a case-ref code and a
monospace type system is unambiguously a *produced artefact*. A screenshot is not.

Two independent signals point the same way:
- The Aug-5 audit independently singled out **Clinic Next Face** — the least conforming, least polished,
  named-and-signed document — as *"the most human, most disarming register in the entire folder."*
- The one confirmed learning in the project says the same thing about voice.

The most expensive asset in the project goes to the coldest audience. That is backwards on effort and,
on this evidence, probably backwards on effect.

---

## 3 · Four things the Aug-5 audit did not catch

### 3.1 The document creates a political problem for the doctor, and the cheapest way out of it is silence `hypothesis`

To the owner, this document is not primarily a diagnosis of a system. It is **documentary evidence, held
by a stranger, that a named member of their staff took 13.5 hours to send a fee.** In a face-conscious
market that is an embarrassment, and the socially cheapest responses to embarrassment are, in order:
say nothing; or hand it to someone below you.

`COPY_STANDARD.md` §3 and the "What we're not saying" block defuse two fears — *you'll suggest replacing
staff* and *this makes care feel automated*. **Neither of those is the live fear.** The live fear is
*someone is about to get scolded, and an outsider is watching.*

This predicts both real outcomes exactly:
- **Sapphire** ran a credential check — *who are you to be holding this on me?*
- **Aesthetica Veda** handed over a decision-maker's email — *this is now the manager's problem.*

Both were read as sales-process failures. They are equally well explained as the document working
correctly on the wrong axis. Unproven, but it is the only single explanation on offer that predicts both
data points, and it is testable: one line of copy, placed **before** the evidence rather than after it,
that puts the cause on the absence of a system and explicitly off any person. Right now the defusing
arrives four sections too late — after the reader has already been shown the receipt.

### 3.2 The CTA rule adopted on 2026-08-13 contradicts a banned move adopted on 2026-08-13 `confirmed`

Same date, same file family, opposite instructions:

| Source | Rule |
|---|---|
| `10 Tooling/one-pager-handoff/CLAUDE.md`, changed 2026-08-13 | *"The CTA names a specific thing you'd do, **plus two named slots**."* |
| `files/OUTBOUND_MEMORY.md` §3, banned moves, added 2026-08-13 | *"**Asking a doctor for a call as the first ask.** 25 one-pagers → 2 replies → 0 calls. A call is the most expensive thing you can ask of a clinician. **Lead with something that costs them nothing** — a number they can message themselves, or a ten-minute drop-in."* |

Two named slots on a cold touch-2 asset **is** asking a doctor for a call as the first ask. The arithmetic
in the banned-move entry — 25 → 2 → 0 — is the argument against the CTA rule that was adopted alongside it.

**Resolution, and it is clean:** the named-slot mechanic comes from `SALES_MOTION.md` Rule 1, which governs
what happens **after a reply**. It is right there and wrong here. Sapphire is exactly where it belongs —
that thread died as a document stall with no date attached, which is what Rule 1 exists to prevent. On a
cold asset, use the resolution the banned-move entry itself names: *something that costs them nothing.*

### 3.3 The demo is live and appears in zero assets `confirmed`

`OUTBOUND_MEMORY.md` §5b, confirmed 2026-08-13: the WhatsApp qualification-and-booking flow is **built and
live**, and *"this is the only real evidence a company with no clients has — a claim they can test is not
a claim."*

It appears in none of the 15 documents, is absent from `COPY_STANDARD.md`, and is absent from the handoff
kit. The cheapest high-leverage edit available in the entire project is one line at the bottom of the
document:

> *Here's the number — message it the way a patient would, and see what comes back.*

It costs the reader 20 seconds. No calendar, no reply to a stranger, no data shared, no commitment.
And unlike every other ask in the kit, it does not require them to trust you — it requires them to test you.

### 3.4 The no-numbers rule is over-applied: it is blocking numbers *they* compute `confirmed`

The rule kills invented numbers, which is right. But it has also killed a class of number that does not
violate it at all — **a number the owner works out for themselves, from their own phone, with no input
from you.**

> *Open your WhatsApp. Scroll back two weeks. Count how many people asked a price and never got a second
> message from you. That number is the whole audit.*

No fabrication, no estimate, no range, no data request, no meeting. It passes every non-negotiable in
`COPY_STANDARD.md` §10.5. And it does the one thing the document currently cannot do: it converts a reader
into a participant, and it converts *"huh, interesting"* into a felt number. Curiosity does not book a call.
A number they counted themselves at 10pm might.

`diagnostic_doc_playbook.md` §2 says *"leave the money question open; let her wonder — that's a stronger
hook than telling her."* This is the missing third option. Don't tell her, and don't leave her wondering.
**Make her count.**

---

## 4 · The test design — and why the Aug-5 three-arm plan can't run

### 4.1 The budget

`OUTBOUND_MEMORY.md` §1: **~70–90 of 100 touches spent, ~19 of 45 days, 0 pilots.** The tripwire is
10–30 touches from firing. The Aug-5 plan is 3 arms × 13 = **39 touches.** It does not fit. Running it
means the tripwire fires mid-test, with three underpowered results and no decision available.

### 4.2 The statistics, stated honestly

The Aug-5 audit says a copy-level A/B is dead on arrival at n=40 and it is right. **Its own three-arm
plan is dead on arrival for the same reason.** The primary metric is *calls held*, currently 0 of 25.
Distinguishing 0% from 15% at 13 per arm is a coin flip wearing a lab coat. Its verdict rule —
"2+ held calls from ~13 wins outright" — would fire on an event that, at a true 8% rate, happens by
chance about a quarter of the time in a single arm.

**At this volume the only readable signal is a step change: something happening that has never happened
before.** Not a rate difference. So design for step changes, and sequence rather than parallelise —
parallel arms buy nothing when the arms can't be compared to each other, and they burn the tripwire
budget twice as fast.

### 4.3 What I'd actually run

**Test 0 — costs zero touches. Do this today.** WhatsApp a JPG to yourself and two others; look at the
bubble before tapping (§2.1). And when the Sapphire call happens, ask one question: *"when the document
came through — what made you ask for a company profile instead?"* One sentence from a real buyer beats
39 sends, and this is already the folder's own rule (a warm reply outranks the send quota).

**Test 1 — change the ask, keep everything else. n≈12.** Same research, same evidence, same wedge, same
document. Two edits: the CTA becomes the demo number plus the self-count (§3.3, §3.4), and the title and
confidentiality line go (§2.2). **Read: does anyone message the number?** That is a metric that has never
existed, so any non-zero result is a step change rather than a rate to be squinted at. It also directly
tests the banned-move entry's own stated fix, which resolves §3.2 with evidence instead of argument.

**Test 2 — only if Test 1 returns nothing. n≈12.** Drop the document. Send a 60–90 second screen recording
of their real thread with your face in the corner, ending on the demo number. This is Aug-5's Arm B, still
the highest-EV untested format: unfakeable, answers *"who are you"* before it's asked, a link rather than
an attachment, ~10 minutes per clinic against what a one-pager costs now.

**The format I'd add to the option set that isn't in the Aug-5 plan: the screenshot receipt.** One image —
their actual chat thread, timestamps visible, nothing else. One sentence under it. One ask. No masthead,
no case-ref, no type system, no branding. Three minutes to make. It is the WhatsApp-native object — a
screenshot is what an actual person sends — and by §2.3 its lack of polish is the point, not a compromise.
It cannot be mistaken for a template because there is nothing there to template. Highest proof-per-minute
in the entire option set. Worth running as Test 2's control if Test 2 runs at all.

### 4.4 What the document should become regardless

Demote it to the job it was designed for: **post-reply proof-of-work at touch 3+, sent after curiosity
exists** — which is what `diagnostic_doc_playbook.md` §1 said in its first line before it drifted. At that
point the reader has opted in to 600 words, the polish reads as respect rather than as sales spend, "who
are you" has already been answered by a human, and named slots become the right ask instead of the wrong one.
Every criticism above evaporates the moment the document is fired at the right stage. Nothing about it needs
rewriting. It needs re-slotting.

---

## 5 · Blocking defect in the handoff kit — the corrected document cannot currently be built

`10 Tooling/one-pager-handoff/CLAUDE.md` instructs the builder to read `COPY_STANDARD.md` **first** and calls it
**"Non-negotiable."** `COPY_STANDARD.md` still carries four rules that were reversed on 2026-08-13:

| `COPY_STANDARD.md` | Says | Reversed by |
|---|---|---|
| §7 structure table, CTA row | *"The audit. ~30 minutes. At no cost to the clinic."* | handoff `CLAUDE.md` — CTA names a specific thing + a time |
| §7 last line | *"Total copy: roughly 350–450 words"* | playbook §6 and handoff `CLAUDE.md` — **250–350** |
| §9 *"CTA wording (settled)"* + *"Never: book a call"* | the free-audit close, verbatim | same reversal |
| §10.5 non-negotiables | *"no personal name"* | handoff `CLAUDE.md` — sign with a real name |

Whoever builds the next document reads the file labelled non-negotiable first and rebuilds the old
document. This is precisely the pattern `MEMORY.md` §2 names as the most damaging in this project — the
folder holding both the rule and its refutation, so drafting can pick up either.

Also: the word ceiling exists in two values across three files (250–350 in the playbook and handoff
`CLAUDE.md`, 350–450 in `COPY_STANDARD.md` §7), and neither was ever met — every document ran 529–703.

**Also diverged:** `10 Tooling/one-pager-handoff/diagnostic_doc_playbook.md` and `10 Tooling/one-pager-handoff/wedge-signal-entry.md`
are both out of sync with their root originals. The handoff kit is shipping stale copies of two governing docs.

**Fixed in this pass:** `COPY_STANDARD.md` §7, §9 and §10 synced to the 2026-08-13 decisions, and the two
frozen copies re-synced from root. No new decisions were made — this only applies decisions already logged
in `OUTBOUND_MEMORY.md` §6.

---

## 6 · Summary — what to do, in order

| # | Action | Cost | Basis |
|---|---|---|---|
| 1 | WhatsApp a JPG to yourself; check the bubble before tapping | 30 sec, 0 touches | §2.1 |
| 2 | Ask Sapphire what the document made them think | 1 question on a call already scheduled | §4.3 |
| 3 | Resolve the CTA conflict — cold asset gets the demo number + the self-count; named slots stay for warm threads | one decision | §3.2 |
| 4 | Put the demo number in the asset. It is live and it is in nothing | one line | §3.3 |
| 5 | Cut the canvas back to A4 — the word ceiling then enforces itself | one CSS line | §2.1 |
| 6 | Kill the "Revenue Diagnostic" title and the confidentiality line | two edits | §2.2 |
| 7 | Move the blame-defusing line above the evidence, not below it | one line | §3.1 |
| 8 | Run Test 1 at n≈12. Read: did anyone message the number | ~12 touches | §4.3 |
| 9 | Re-slot the document to touch 3+ / post-reply | a sequence decision | §4.4 |

**Not recommended:** rewriting the copy, testing headlines, running the three parallel arms, or
re-adopting the ₹7,500 paid diagnostic (rejected 2026-08-13, and §5 of `OUTBOUND_MEMORY.md` stands).

---

## 7 · Epistemic status of everything above

| Claim | Status |
|---|---|
| Page dimensions, aspect ratio, word counts, font sizes, PDF page size | `confirmed` — measured from source files |
| The two CTA rules contradict each other; `COPY_STANDARD.md` carries four reversed rules; the handoff copies are diverged | `confirmed` — quoted from the files, dates checked |
| The demo is live and absent from every asset | `confirmed` — `OUTBOUND_MEMORY.md` §5b + grep of the kit |
| "Revenue" violates the banned-vocabulary table | `confirmed` — `COPY_STANDARD.md` §1 |
| WhatsApp crops the bubble and the masthead is not visible | `hypothesis` — verify in 30 seconds, item 1 |
| The document creates a blame problem and silence is the cheap exit | `hypothesis` — explains both real replies; explains is not proves |
| The self-count number outperforms leaving the money question open | `hypothesis` — passes every existing rule; untested |
| The screenshot receipt beats the designed document on a cold channel | `hypothesis` — generalises one `confirmed` voice-note learning to a channel it was never tested on |
| Polish is a liability on cold channels | `provisional` — confirmed for voice notes, extended by argument to documents |
