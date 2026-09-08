# Copy Standard — Revenue Diagnostic One-Pagers

This file exists because the same mistakes were made repeatedly and corrected in
live review. Every rule below is a correction that was actually issued on a real
draft, not a theory. `diagnostic_doc_playbook.md` gives the doctrine; this file
is the accumulated delta between the doctrine and what actually shipped.

---

## 1. Who you are writing for

An Indian doctor who owns their clinic. Not a US SaaS founder.

They see themselves as clinicians, not business operators. They have very likely
been burned by a marketing agency before — assume it, never say it. Lead with
de-risking, not features.

**The translation test — apply to every sentence:** could this line be said, in
these words, by an Indian clinic owner describing their own day? If it sounds
like a consultant's slide, rewrite it as a scene.

Banned vocabulary — replace on sight:

| Never write | Write instead |
|---|---|
| leads, lead generation | enquiries, patients |
| funnel, pipeline, conversion | (describe what actually happens) |
| ROI, CAC, revenue leakage | (name the concrete cost) |
| operational efficiency, admin tasks | (the actual task being repeated) |
| customer experience | (what the patient actually experiences) |
| patient journey, nurture, engagement | (the specific step) |
| infrastructure, scale your practice | (the specific thing being built) |
| decision window, operational continuity | (say the plain thing) |
| "gap" used as filler | name the actual gap |

**Rejected:** "Manual dependency creates operational inefficiency at scale."

**Accepted:** "That's the same person typing out that same 'hi, what treatment
are you looking for' reply to every single enquiry — and every minute spent on
that is a minute not spent with the patient actually sitting in your clinic."

Short sentences, plain words. If a smart 12-year-old wouldn't follow it,
simplify it.

---

## 2. The insight must be an insight, not an observation

This is the single most common failure. Climb the pyramid:

```
EVIDENCE     → what you directly observed, zero interpretation
OBSERVATION  → the plain pattern that evidence shows
INSIGHT      → what it means at a SYSTEM level, not an event level
QUESTION     → what only they can answer by looking at their own data
```

**Tell:** if the sentence still describes *what happened*, it is not an insight
yet. An insight describes what the *not-knowing* costs, or what the pattern
implies about the system.

- Observation (weak, dismissible): *"You replied slowly to this one message."*
  → she thinks *"my coordinator was probably asleep"* and moves on.
- Insight (lands): *"Right now there's no way for anyone to know if this happens
  once or every night."* → it's not about the mistake, it's about the
  **invisibility** of the mistake.

**Research-recitation vs. felt-problem.** Reporting a researched fact reads as
competent but doesn't land emotionally. Naming the *structural consequence* of a
verified fact, stated as the founder's problem rather than as a research summary,
does.

**The line you must not cross:** never assert an unverified fact, or an
unverified emotional/behavioural state ("you're probably frustrated," "I bet you
have 40 of these"). But stating the *necessary logical consequence* of a verified
fact is not invention — it is the actual craft. "Multi-visit treatments + no
tracking system → some patients drop off invisibly" is a logical certainty from
the audit, not an invented pain point. Ground the observation in evidence; let
the framing carry the emotional precision.

---

## 3. Never accuse. Compliment first, then pivot.

**Rejected v1 (Ministry of Skin):** *"I tested it myself. Nobody did."*
Reads as an accusation against her team.

**Accepted v2:** *"Your WhatsApp already does something a lot of clinics don't
bother with: after hours, it promises people someone will personally call them
back. Good instinct — most clinics don't go that far. Here's the part worth
flagging: when I tested it, that callback never came."*

Sequence: **acknowledge what genuinely works → name the specific miss as a
shared/structural risk, not a team failure → give the concrete mechanism → close
with exactly what's being offered.**

The `What we're not saying` section does this defusing explicitly. It must name
the two quiet fears: (a) you're about to suggest replacing staff, (b) this will
make patient care feel automated. Name them directly, don't over-explain. Its
last line should echo back to the core insight — narrative continuity, not a new
idea.

---

## 4. No vague referents. Ever.

Every phrase pointing at an action or consequence must name the concrete thing it
refers to — what breakdown, what fix, what happens to the patient.

- Rejected: "what I'd check first," "probably not a one-off," "sorting that out"
- Required: name it explicitly

---

## 5. Never build a wedge on a secondary channel's slowness

If WhatsApp is fast and Instagram is slow, that is **not** a wedge. WhatsApp is
the channel Indian clinic patients actually use to enquire and book. A slow
Instagram DM costs the clinic little if the real volume and real decisions happen
on WhatsApp. This mistake was made twice — first on Vtiara, then repeated on The
Glow Clinic — before it was caught.

If the primary channel is already fast **and** human-staffed, the real wedge is
the *time cost of that manual handling* — staff hand-typing the same replies to
routine enquiries instead of spending that time on the patient physically in the
clinic — not a cross-channel speed contest.

---

## 6. Selling to a clinic that's already doing well

When speed, persistence, or automation already exists, do **not** sell speed —
they have it and are usually proud of it. Sell **fragility and cost**:

> "This works because of one person. What happens on their day off, after 8pm,
> or if they quit? And how much of their day goes to chasing people who were
> never going to book?"

Position the offer as: *keep their existing closer, remove the manual chasing.*
Nothing about how they treat patients changes.

---

## 7. Document structure (fixed)

| Section | Pyramid layer | Rule |
|---|---|---|
| Masthead | — | Valence Ops wordmark left, case-ref block right |
| Clinic name | — | **The first big thing on the page.** Largest type. |
| Tagline | Insight, compressed | One italic accent line. The hook. |
| Subtitle | — | "What we found says less about X, and more about Y" |
| **Observed** | Evidence | 100% verified, zero interpretation. The signature visual — it earns the most design attention because it's the one section that is pure fact. |
| Core insight | Insight | One block. The highest-leverage line in the document. |
| Why This Matters | Observation → pattern | Why this *category* of gap matters. Never a claim about their actual numbers. |
| Confirmed From Outside | Evidence | ✓ Only externally, unambiguously true things |
| Can't Confirm Without Your Data | honesty | – The real gaps. Never reuse another clinic's bullets. |
| What We'd Check First | operator thinking | → Real thinking, without pitching |
| What we're not saying | defusing | See §3 |
| Close | Question | The question only their own data answers |
| CTA | — | **A specific thing you'd do, with a time attached — see §9.** ⚠️ CHANGED 2026-08-13. **The document ends here.** |
| ~~Sign-off~~ | — | **REMOVED 2026-08-14 — Tilak's call.** No name line, no correction line. See §9. |
| Footer | — | Valence Ops |

Two items per bucket is usually right; three starts to feel padded (four only if
every one is genuinely load-bearing — see DNA and Vtiara).

**Total copy: 250–350 words, and the ceiling is real.** ⚠️ CHANGED 2026-08-13 —
this file previously said 350–450, the playbook said 250–350, and all fifteen
shipped documents ran 529–703 against both. Over the ceiling, cut a bucket item
before touching the structure.

**Build on A4.** ⚠️ ADDED 2026-08-14. Ten of the eleven built documents set a
custom canvas of 210 × 426–456mm — 1.43×–1.54× A4 — which is how the word ceiling
was silently escaped: the page grew to fit the copy. Dr. Dixit is the only
document that held A4 and the only one under 530 words. Fix the canvas and the
word count enforces itself.

---

## 8. Observed-section variants — pick by evidence shape

Do not force everything into a timeline. The structure should encode what the
evidence actually is:

- **Two-point timeline** (Dixit, Ministry of Skin, Glow) — a gap between two
  moments. Use when the finding is *what happened between X and Y*.
- **Parallel channels** (Swetha's) — same test, two channels, same result. Use
  when the finding is *this is systemic, not a fluke*.
- **Sequence list** (Juvita) — four touches in a row. Use when the finding is
  *volume of effort*, not a timing gap.
- **Public signals** (DNA) — no mystery shop exists; three converging public
  facts. Use **only** when there's no verified test, and it **must** carry a
  caveat line stating nothing came from inside the clinic.

---

## 9. The close and CTA

The close is the **Question** layer. Most first drafts fail here by reaching for
a meeting ask — that's a pitch, and it trips the exact vendor-radar this document
exists to avoid.

- Rejected: *"The only way to know what this is costing you is to look at your
  real numbers."*
- Accepted: *"The real question isn't whether Cozmo Blis lost this one enquiry —
  it's how many nights like this one have already happened, quietly, with no
  record anywhere."*

**Authority without a fabricated stat.** Open the close with honest pattern
language:

> "This isn't unique to <clinic> — it's one of the most common patterns we see
> across founder-led dermatology practices in Bangalore."

True, defensible, no invented percentage. **Never attach a number to this**
unless given a real, citable source.

**CTA wording — ⚠️ REVERSED 2026-08-13. The old rule is below, struck, so it is
not re-adopted from an older draft.**

> ~~A full audit — mapping <the specific thing> — takes about 30 minutes, at no
> cost to the clinic.~~

Why it was reversed: **the document *is* the audit**, so that CTA asks for the
thing it just gave away. It was offered ~25 times and accepted zero times, and it
shipped with no date on it every single time, in violation of `SALES_MOTION.md`
Rule 1. See `files/OUTBOUND_MEMORY.md` §6, 2026-08-13.

**The CTA now names a specific thing you would do that the document has not
already given, and it costs the reader as little as possible.**

⚠️ **Open conflict — ask Tilak which applies before building.** Two rules adopted
on 2026-08-13 point opposite ways on a *cold* asset:

| Source | Says |
|---|---|
| `one-pager-handoff/CLAUDE.md` | the CTA carries **two named slots** |
| `files/OUTBOUND_MEMORY.md` §3, banned moves | **"asking a doctor for a call as the first ask"** is banned — *"lead with something that costs them nothing — a number they can message themselves, or a ten-minute drop-in"* |

Two named slots on a cold touch-2 document is asking a doctor for a call as the
first ask. The named-slot rule comes from `SALES_MOTION.md` Rule 1, which governs
what happens **after a reply** — it is correct there and contested here. Full
reasoning in `One-Pager Steelman 2026-08-14.md` §3.2.

**Two zero-cost asks worth using while that is unresolved** (both pass every
non-negotiable in this file):

1. **The live demo number.** The WhatsApp qualification-and-booking flow is built
   and live (`OUTBOUND_MEMORY.md` §5b) and currently appears in no asset.
   *"Here's the number — message it the way a patient would, and see what comes
   back."* Twenty seconds, no calendar, no reply to a stranger.
2. **The self-count.** A number they work out themselves, from their own phone —
   which does **not** violate the never-invent-a-number rule, because you aren't
   supplying it. *"Scroll back two weeks in your WhatsApp and count how many
   people asked a price and never got a second message. That number is the whole
   audit."*

Still never: "free" (use *at no cost to the clinic*), "no pitch," "hop on a call."
Keep the emotional close and the logistics line as two separate lines — don't
merge them.

**Sign-off — ⚠️ REMOVED 2026-08-14. Tilak's direct call. Supersedes the
2026-08-13 rule below, which is struck so it is not re-adopted from an older draft.**

> ~~— Tilak, Valence Ops~~
> ~~*This is a read on public information and two test enquiries — not clinic data.
> Happy to be told where it's wrong.*~~

**The document now ends on the CTA line.** No name, no correction line, nothing
after it but the footer.

**Why removed:** the document is attached to a DM that already comes from a named
person, so the name inside repeats what the reader already has — and masthead +
sign-off + footer put the wordmark on the page three times, against "brand exactly
twice" (`BUILD_GUIDE.md` §3).

**What the removed rule was protecting against, kept here on purpose:** a faceless
case file from an unknown firm invites exactly one question — *"who are you?"* —
and that is the question the one real warm lead in this project's history actually
asked, after reading a nameless document. **If a clinic replies to one of these
asking who Valence Ops is, that is the signal to put it back.** Nothing else is.

---

## 10. Self-check before delivering

1. **Pyramid check** — does the core insight actually reach Insight, or is it
   still sitting at Observation?
2. **Skim test** — if she reads only the clinic name, tagline, Observed block,
   core insight, and close, does the document still work? Optimise for the
   skimmer, not the person who reads every word.
3. **One-sentence test** — she'll remember one sentence after closing the PDF.
   Is it obvious which one? If three are competing for that role, cut two.
4. **Density pass** — try removing a fifth of the words. If nothing can go
   without losing something true or specific, it's ready.
5. **Non-negotiables** — no invented numbers, **no sign-off block at all**
   (⚠️ changed 2026-08-14 — the document ends on the CTA; this line has now
   reversed twice, see §9), no unverified claims, no superlatives, "at no cost"
   not "free," brand exactly twice — masthead and footer, nowhere else.
6. **Translation test (§1)** — every sentence.
7. **Word count** — 250–350, measured, on an A4 canvas. Not "about right." §7.
8. **Structure rotation** — is this document's headline shape, subhead shape and
   close deliberately different from the last three? All fifteen existing
   documents converged on four formulas; the same subhead appears verbatim in
   10 of 10. Bangalore aesthetic derm is a small world.
9. **Banned vocabulary applies to the title too** (⚠️ added 2026-08-14). The
   existing documents are titled *"Revenue Diagnostic"* — "revenue" is on the
   §1 banned list, set in the largest type on the page. And drop
   *"Confidential — Prepared exclusively for X"*: real confidential documents
   don't announce it, pitch decks do.
