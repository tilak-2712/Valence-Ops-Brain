---
date_created: 2026-08-13
date_modified: 2026-08-14
status: active
---
# The Diagnostic One-Pager — Playbook
*Reference doc for building outbound diagnostic PDFs. Send alongside the Cozmo Blis example.*

> **⚠️ Amended 2026-08-13 after the 15-document audit. Three rules in this file are superseded.**
> `one-pager-handoff/CLAUDE.md` holds the current versions and wins where they conflict.
> 1. **No personal name → reversed 2026-08-13 → re-reversed 2026-08-14 (Tilak's call).**
>    The sign-off block is now removed entirely: no name line, no correction line. The document
>    ends on the CTA. See `one-pager-handoff/COPY_STANDARD.md` §9 for both sides of this, and
>    `files/OUTBOUND_MEMORY.md` §6 for the decision and the trigger to revisit it.
> 2. **"The CTA is an audit, never a meeting pitch" → reversed.** The document *is* the audit, so
>    that CTA asks for the thing it just gave away — offered 25 times, accepted zero. The CTA now
>    names a specific thing you'd do, with two named slots attached.
> 3. **The 250–350 word ceiling is now enforced.** All 15 documents ran 529–703 words.
>
> Also worth knowing while reading §5: the *"this isn't about X — it's about Y"* construction this
> playbook flags as a symptom of reaching for a device became the load-bearing subhead of **10 of
> 10** documents. Assign a deliberately different headline, subhead and close per clinic.

**Read this first:** this document teaches judgment, not compliance. The structure and non-negotiables below exist to protect trust and honesty — they're fixed. Everything else is a strong default, not a law. If a specific clinic's situation calls for breaking a style rule to be more specific, more true, or more human, break it. A document that follows every rule but says nothing sharp about *this* clinic has failed regardless of how compliant it is.

---

## 1. What This Is For

Not a sales pitch, not a capabilities brochure. It's proof-of-work sent after a clinic owner has already shown curiosity — usually after replying to the Day-0 DM.

**The single test for any draft:** does this make the owner think *"they clearly looked at my specific situation and are being straight with me"* — or does it read like something sent to any clinic in Bangalore? If the second, it's not done.

### Purpose hierarchy

When two goals conflict, this decides which one wins:

1. **Earn trust.** Above everything else.
2. **Create one new way of thinking about their own operation.** The second-order insight.
3. **Earn curiosity.** Make them want to know more about their own numbers.
4. **Earn the conversation.** Get the reply.

**Never optimize for closing.** Closing is what happens on the call, not the page. A document that reaches for the close too early undermines all four priorities above it.

---

## 2. The Core Philosophy

Early drafts tried to **diagnose** the clinic — here's what's probably wrong, here's roughly what it's costing you. That version was weaker.

**The correct posture: "here's what we could verify, here's what we couldn't, here's what we'd test if we had access."**

A clinic owner — especially a doctor — trusts *disciplined uncertainty* far more than confident diagnosis from a stranger. Confirmed / can't confirm / would investigate next is the actual structure of good clinical thinking. It's a register she already respects professionally. Claiming to know what's wrong in her business after one WhatsApp test reads as presumptuous no matter how well it's worded.

**The one hard rule this produces: never invent a number**, not even a conservative one. One unverified figure makes a sharp reader silently question every other line — including the true ones. Leave the money question open; let her wonder. That's a stronger hook than telling her.

---

## 3. The Diagnostic Pyramid — the model behind everything

This is the mental model to internalize before writing anything. Every statement in the document belongs to exactly one of four layers. Climb all four, in order, every time.

```
EVIDENCE      →  something you directly observed, no interpretation
OBSERVATION   →  the plain pattern that evidence shows
INSIGHT       →  what the pattern means at a systems level, not an event level
QUESTION      →  what the owner can only answer by looking at her own data
```

**Worked example:**
- Evidence: *the WhatsApp reply came 7 hours 32 minutes after the message was sent.*
- Observation: *there was no automatic acknowledgment in between.*
- Insight: *right now, there's no way for anyone — including the owner — to know whether this happens once or every night.*
- Question: *how often does this actually happen, across every enquiry, not just this one?*

Most weak drafts stop at Observation and call it Insight. The tell: if the sentence is still describing *what happened*, it's not an insight yet. An insight describes what the *not-knowing* costs, or what it implies about the system, not the event itself.

**"You replied slowly to this one message"** stays at Observation — dismissible, "my coordinator was probably asleep."
**"There's currently no way for anyone to know if this happens once or every night"** reaches Insight — it's not about the mistake, it's about the invisibility of the mistake. That's what produces "huh, I hadn't thought about it that way" instead of "okay, noted."

Every section of the document maps to a layer of this pyramid. When drafting or reviewing, ask which layer a sentence is actually operating at — that catches more problems than any style rule below.

---

## 4. Document Structure

The shape that works, in order:

**Header.** Clinic name (not the owner's personal name — keep this slightly formal). A title that signals "diagnostic," not "pitch." A subtitle that plants the systems framing early — not "here's what we found" but something closer to *"what happened next says less about that one message, and more about the system behind it."* Small case-reference metadata in a corner — a deliberate clinical-file cue (see Section 6).

**The Observed Fact (Evidence layer).** The one thing in the document that's 100% verified, zero interpretation. Usually a timed message test: sent at X, replied at Y (or not), exact gap. State it as a clean two-point timeline. Add one line confirming it was real, not hypothetical — pre-empts "did you actually test this." Nothing here is an opinion — if it's not verified, it doesn't belong in this section.

**The Core Insight (Insight layer).** One sentence, the highest-leverage line in the document. Run it through the Pyramid: if it's still describing the event, climb higher.

**Why This Matters (Observation → general pattern, never a specific claim).** A short paragraph giving defensible context for why this *category* of gap matters — never a claim about this clinic's actual patients or revenue. Says nothing about *this* clinic's numbers; it's a true statement about how this type of failure behaves in general.

**The Three Buckets — the honesty mechanic.**
- *Confirmed From Outside* — only externally, unambiguously true things
- *Can't Confirm Without Your Data* — the honest gaps
- *What We'd Check First, If We Had Access* — real operator thinking, without pitching it

Two items per bucket is usually enough; three starts to feel padded. Read as a clean checklist (✓ / – / →), not a colored callout box — a box invites a big number to fill it, which is exactly how an invented figure ended up in an earlier draft. Don't design a slot for a number you don't have.

**What We're Not Saying.** One paragraph defusing the two quiet fears: that you're about to suggest replacing staff, and that this makes patient care feel automated. Name it directly, don't over-explain. Good drafts let this section's last line echo back to the Core Insight — narrative continuity, not a new idea.

**The Close (Question layer).** End on the genuine question from the Pyramid — the one she can only answer by looking at her own data. This is where most first drafts fail by reaching for a meeting-time ask instead ("book 15 minutes Tuesday") — that's a pitch, and it trips the exact vendor-radar this document exists to avoid. Keep the emotional close and the logistics line ("15 minutes, no pitch, free") as two separate lines — don't merge them.

**Branding.** "Valence Ops" appears exactly twice — masthead and footer, nowhere else. No personal name anywhere in the document *(reversed 2026-08-13, reinstated 2026-08-14 — the sign-off block is removed and the document ends on the CTA)*.

---

## 5. Language: Non-Negotiables vs. Judgment Calls

Some of this is about trust and honesty — those are fixed. The rest is style, and style should flex to what the specific clinic and draft actually need.

### Non-negotiable (never break these)
- Never invent a number, even a conservative one
- Never put the sender's personal name in the document *(reinstated 2026-08-14 after being
  reversed on 2026-08-13 — the whole sign-off block is gone; see the amendment note above)*
- Never state a claim about the clinic — or a competitor — that isn't externally verified
- No superlatives ("best," "leading," "guaranteed," "proven") — the category is saturated with this language already
- Brand name appears exactly once

### Judgment calls (strong defaults, not laws)
- **Prefer plain, spoken language over writing-for-effect.** Before finalizing a sentence, ask: would I say this, in these words, sitting across from her? If a sentence only works on the page, it usually means it's optimizing for sounding smart rather than being true.
- **Be wary of predictable rhetorical constructions** ("this isn't about X — it's about Y" and similar) — not because they're forbidden, but because they're a symptom: reaching for a device instead of stating the point. If one fits naturally and earns its place — the Cozmo Blis close uses exactly one — that's fine. If a draft has three of them, that's a signal to simplify, not a rule being broken.
- **Concrete usually beats clever.** A timestamp or exact number tends to outperform a well-turned phrase in this category — but use judgment; occasionally the phrase *is* the sharpest way to say something true.
- **Premium comes from restraint in design, not polish in vocabulary.** Reaching for literary language to sound premium usually backfires — it's what makes something read as a corporate pitch, the exact thing this audience already distrusts.
- **Keep jargon out** — "consultation value," "procedure mix," "conversion operations," and similar startup/consulting vocabulary rarely earns its place here. If a smart 12-year-old wouldn't follow the sentence, simplify it.
- **The document shouldn't read as more polished than the DM that led to it.** A mismatch there is usually a tell, not a stylistic choice.

---

## 6. Design Principles

- One page, roughly 250–350 words of copy. Over that, cut a bucket item before touching the structure.
- Typography with a purpose: an editorial serif for narrative, a monospace for labels/timestamps/data — reinforces the clinical-file read (see Section 7), not decorative.
- One accent color, used sparingly, for labels and the timeline markers only. Avoid the generic "AI document" palette (warm cream + terracotta is the most overused combination — skip it). Paper white, near-black ink, one restrained accent reads as more premium precisely because it's quiet.
- Full width, properly used — text stranded in a narrow column with dead space on one side reads as broken, not intentional. Justify once the column is sized correctly.
- Vertically balanced — a short document shouldn't be crammed into the top two-thirds with a dead void below it.
- The observed-fact timeline is the signature visual — it's the one section that's pure fact, so it earns the most design attention.
- Don't build a slot (a big colored box) for a number you don't have.

---

## 7. Why the "Clinical Case File" Framing Works

The whole structural language — case reference numbers, timestamped observations, confirmed/unconfirmed/would-investigate — deliberately mirrors documentation a doctor already trusts professionally. She reads diagnostic reports and case notes all day. A document that *behaves* like that format — honest about uncertainty, precise about what's confirmed — speaks her professional language back to her without saying so. That's the actual trust mechanism. It's the structure, not the copywriting.

---

## 8. Self-Check Before Sending

Run every draft through this, in order:

1. **The Pyramid check.** Does the core insight actually reach Insight, or is it still sitting at Observation? (Section 3.)
2. **The skim test.** If she only reads the title, the timeline, the core insight, and the close — does the document still work? Most people skim first. Optimize for that reader, not the one who reads every word.
3. **The one-sentence test.** She'll likely remember one sentence after closing the PDF, not ten. Is it obvious which one that's supposed to be? If three sentences are competing for that role, cut two.
4. **The density pass.** Try to remove a fifth of the words. If nothing can go without losing something true or specific, it's ready. If it easily loses 20% and reads just as well, it wasn't ready.
5. **Non-negotiables check.** Scan against Section 5's fixed list — no invented numbers, no personal name, no unverified claims, no superlatives, brand mentioned once.

---

## 9. How to Build a New One

Gather these four things before drafting:

1. **One real, verifiable observed fact** — almost always a timed message test with an exact timestamp and outcome. Non-negotiable; the whole document's credibility rests on this being specific and real.
2. **Basic externally-verified facts** — ad activity, specialties, review patterns — from the pre-outbound audit, never invented.
3. **The clinic's vertical**, to calibrate the "why this matters" angle:
   - *Surgical/cosmetic* → long decision journey, multi-clinic comparison → angle is the comparison window closing
   - *Skin/derm* → recurring treatment → angle is the second visit that never gets scheduled
   - *Hair transplant* → heaviest comparison-shopping category → angle is speed and consistency as the deciding factor
   - *Dental* → quote-to-decision gap → angle is the follow-up window after a quote
4. **What's genuinely unconfirmed for this specific clinic** — don't reuse the same "can't confirm" bullets from the last doc; they should reflect real gaps in what's actually known about this one.

Then climb the Pyramid (Section 3) for the core insight, follow the structure (Section 4), and run the self-check (Section 8) before calling it done.

---

## 10. Before / After — Cozmo Blis

**Close — rejected (meeting-pitch framing):**
> "The only way to know what this is actually costing you is to look at your real numbers — how many enquiries like this come in, and how many you're still winning anyway."

**Close — kept (Question layer, curiosity-first):**
> "The real question isn't whether Cozmo Blis lost this one enquiry — it's how many nights like this one have already happened, quietly, with no record anywhere. Worth finding out together?"

**"Why this matters" — rejected (a marketing truth, not an Insight):**
> "For surgeries like liposuction or body contouring, people rarely decide after one message. They usually check with a couple of clinics before choosing."

**"Why this matters" — kept (systems-level, founder-identity specific):**
> "For a founder-led clinic, most gaps get caught eventually — someone notices, mentions it, fixes it. A gap in after-hours response is different. It's invisible by nature: nothing shows up in a report, and no one complains, because the patient who never got a reply simply never became one to begin with."

**Estimated-impact section — removed entirely:** a colored callout stating a directional revenue range (₹1.5L–₹4L/month). Replaced by the Three Buckets, zero numbers. The single highest-impact change made to the document — it removed the one thing a reader could argue with.

---

## 11. One Last Thing

This document is one instance of a repeatable system — a broader framework (five buyer-archetype openings × four vertical modules) that this playbook slots into for scaling across clinics without rewriting from scratch. Worth its own conversation if useful. Everything above holds regardless of which archetype or vertical you're building for.
