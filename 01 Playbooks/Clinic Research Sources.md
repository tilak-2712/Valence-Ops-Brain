---
date_created: 2026-08-13
date_modified: 2026-08-13
status: active
---
# Clinic Research — Final Source List & Ingestion Guide

## How this fits into the workflow

You scrape/copy raw material from the sources below for a given clinic, then dump it to me — pasted text, screenshots, whatever's fastest. I'll ingest it, cross-reference it, and hand back a synthesis structured for `personalized-outbound-v2.md`. You take that straight into the skill and draft.

Every source on this list earns its place the same way: it diagnoses a specific stage of the Patient Revenue OS we're actually selling. Nothing here is "thorough for its own sake" — if a source doesn't change either the DM's hook or the wedge service, it's not on this list.

---

## Bring these every time (10 min hard ceiling)

### 1 · Instagram
**Pull:** bio, last 10–15 post/Reel captions and dates, and ONE comment asking about price/location/booking that went unanswered or got a 2+ day late reply — exact text and date, not a paraphrase.
**Diagnoses:** Stage 2 (Lead Qualification / Instant Response) — proves it's broken or missing.
**Feeds:** the hook, almost every time.

### 2 · Mystery shop — one channel · **runs FIRST, before any of the others**
**Pull:** the clinic's published Google hours for that day, then shop inside them. Exact sent timestamp, exact reply timestamp or "no reply, X days," what the reply said, whether anyone asked a qualifying question, and whether a quote went unchased. **Save the timestamped screenshot** — that image is the deliverable, not the paraphrase.
**Diagnoses:** Stage 2, first-hand. Your strongest data point — and the only one a competitor cannot reproduce.
**Feeds:** the hook, and the wedge routing in `wedge-signal-entry.md` §3.
**⚠️ Sequencing changed 2026-08-13:** this is now the *first* step in a batch, not a later one. It is the only 24–72h async dependency in the process, and running it last is how batch 7 produced 25 dossiers and zero shops. Research only the clinics whose threads came back interesting. Inadmissible if it lands outside their published hours.

### 3 · Google reviews
**Pull:** review count, rating, date of most recent review, and the text of any review flagging wait times, no follow-up, pricing surprises, or ghosting after payment.
**Diagnoses:** Stage 9 (Post-Consultation Follow-Up / Review Request) — a stale review date proves no review-request automation runs.
**Feeds:** the review-request wedge, or backup hook if Instagram comes up dry.

### 4 · Meta Ad Library (ads.meta.com/adlibrary)
**Pull:** is the exact Page name running active/past ads, which procedure/offer, how long it's been running or how many ads total.
**Diagnoses:** Stage 1 (Acquisition) — confirms paid leads exist somewhere to recover.
**Feeds:** the dead-lead-reactivation wedge specifically.

---

## Only if the default four didn't give you a clean hook

### 5 · Practo — derm/dental clinics only
**Pull:** review count/rating if listed, and any open patient Q&A question with a date that hasn't been answered.
**Diagnoses:** same as Instagram (Stage 2), a second channel.
**Skip for:** hair-transplant-only clinics — Practo's Q&A volume there is too thin to be worth the time.

### 6 · Mystery shop — second channel
**Pull:** same as #2, on the other channel.
**Use only when:** the first channel came back clean with nothing to use. Don't shop both by default — you need one clean fact, not two corroborating ones.

---

## 60-second glances — fold into what you're already doing, don't schedule separate time

### 7 · Website view-source
**Pull:** Ctrl+F the page source for "leadconnectorhq" (GoHighLevel), Calendly, Picktime, a chatbot widget script, or a "powered by [agency]" footer. While you're already on their site.
**Diagnoses:** Stages 4–5 (Booking/Confirmation) — whether any automation already exists.
**Why it stays:** prevents pitching something they already have. Doesn't raise reply rate — prevents a wasted shot.

### 8 · WhatsApp catalog / away-message
**Pull:** does a catalog exist, what the away-message says, business hours listed. Glance at it while you're mystery-shopping WhatsApp for #2 — zero extra minutes.
**Diagnoses:** Stage 1 entry point + Stage 2 automation.

---

## Off this list, on purpose

- **Competitive snapshot** — cut. Almost never changes the wedge decision.
- **Hiring postings** — moved out entirely. It answers "should I pursue this clinic at all," which is a call you make *before* picking a clinic to audit — not personalization data for a DM you're already writing. Useful, but it's a different stage of the funnel than this list covers.

---

## What to send me, and how

- **Exact text and dates, not summaries.** "A comment asked about price" isn't usable. "Comment on the Jul 14 Reel: 'how much for full face?' — no reply as of today" is the hook itself.
- **Tell me what you didn't find, too.** "No ads found" or "no WhatsApp button" is information — it rules wedges in or out just as much as a positive finding does.

## What I'll hand back

1. The hook — one specific, dated, verifiable fact
2. Founder-run — Y/N, with evidence
3. Ad spend — Y/N, procedure, duration
4. Review data — count, rating, most recent date, notable content
5. Mystery shop result — channel, sent/reply timestamps
6. Wedge service recommendation — with the reasoning, not just the label
7. Kill-switch check — anything that should pause this prospect
8. Supporting context — area, founder's name, tone/register — for the video/follow-up layer, not the Day 0 DM

You take that straight into `personalized-outbound-v2.md` and draft.


---
Related: [[01 Playbooks/personalized-outbound-v2|personalized-outbound-v2]] · [[01 Playbooks/wedge-signal-entry|wedge-signal-entry]]
