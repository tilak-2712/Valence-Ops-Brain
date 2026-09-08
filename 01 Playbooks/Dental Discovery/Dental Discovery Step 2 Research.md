---
date_created: 2026-08-09
date_modified: 2026-08-13
status: active
---
# STEP 2 — RESEARCH (Bangalore Dental)

**Cap: $1.20.** Input: `_dental-qualified.md`, QUALIFIED rows only. Nothing else — PARK rows and
anything from `_dental-rejected.md` stay out.

Output: full dossiers in `Pre-outbound-research/batch3-dental-audit.md`, ready for mystery shop and
outreach drafting.

*(Remaining $0.80 of the $5.00 ceiling is reserve for re-runs and gap-fills.)*

---

## Actor

`compass/crawler-google-places`, this time **with review text**:

```
maxReviews: 60
reviewsSort: "newest"
maxTotalChargeUsd: 1.20
```

Read a **spread** — recent and older, positive and negative. The aggregate rating is not the point.
The review *text* is what makes an outbound hook credible instead of generic.

---

## 1 · Decision-maker — Gate E

Find a single named founder-dentist from GBP, IG bio, website team page, LinkedIn, or Practo.

Record with explicit confidence:

- **`confirmed`** — named on the clinic's own property (GBP title, own IG bio, own website team page),
  or corroborated across two independent sources
- **`likely`** — third-party listing only (Practo, JustDial), no corroboration
- **`weak`** — inferred, or no name found anywhere

Signals:
- `"Dr. X's [Clinic Name]"` in the GBP title → strong single-owner signal
- Neutral brand name, no doctor attached anywhere → warning, not yet a kill
- Two-or-three-partner practice → **PARK**, note which partner appears to own operations
- Front-desk-only contact → **PARK**, route via Practo doctor listing / website team page / LinkedIn

**Expect a high failure rate.** `batch3-dental-audit.md` found no named decision-maker on 5 of 11
dental clinics (Chisel, Sky Dental, Smiley House, both Amaya branches). If this run does markedly
better, re-check the names before believing it.

Also record every contact channel with confidence, and **flag explicitly when a listed number reads
as a front-desk or booking line rather than the founder** — this has caught us out before.

---

## 2 · Review screen — Gate F

**F.1 — Upselling / over-treatment complaints → EXCLUDE.**
If patients accuse the clinic of pushing unnecessary treatment, inflating plans, or pressuring on
price, kill it. Selling automated follow-up to a clinic that already over-treats makes the problem
worse and puts our positioning behind a bad actor. Quote the review that triggered it.

**F.2 — Wedge material, NOT disqualifiers.** Log with exact quotes:

| Theme in reviews | Points to |
|---|---|
| No-shows, missed appointments, rescheduling friction | No-show recovery |
| Waiting time, rushed, doctor unavailable | Capacity / handling |
| Billing surprises, quote changed later | Quote decay |
| Ghosted after enquiry, no callback | Response speed |

**F.3 — Last-review gap ≥ 3 months** → review/recall reactivation signal. Record the gap in months.

**F.4 — High-ticket procedures named in reviews.** Count reviews mentioning implants, aligners,
Invisalign, veneers, smile makeover, full-mouth work, and quote them. This corroborates the Gate C
demand evidence from Step 1 with patient-side proof. **If a clinic passed Gate C on ads but zero
reviews mention high-ticket work, flag the contradiction** — don't quietly ignore it.

---

## 3 · Wedge routing

Tag each clinic per `wedge-signal-entry.md` §4:

| Signal | Entry wedge | funnel_break_stage |
|---|---|---|
| High-ticket ads live · slow or no reply | Dead-lead reactivation | Response Speed |
| Implant/aligner quote given, never chased | **Quote-decay follow-up** | Quote Chase |
| Fast reply · no qualification questions | Qualification + scoring | Qualification |
| After-hours unanswered, or promise-only auto-reply | 24/7 capture + qualification | Response Speed |
| Reviews cite no-shows, rescheduling friction | No-show recovery | Booking / No-show |
| Good review volume, last review ≥3 months old | Review / recall reactivation | Reviews |
| Practo Prime paid listing · slow response | Dead-lead reactivation (aggregator) | Response Speed |
| Multiple breaks | Earliest provable break wins | — |

**Three constraints:**

- **Every wedge here is PROVISIONAL.** No mystery shop has run. Mark each `confirm_via_mystery_shop:`
  with the specific test. Never present a routed wedge as a diagnosed one.
- **Treatment-plan non-acceptance is dentistry's biggest revenue leak and is NOT usable.** It happens
  in the chair, invisible to a mystery shop or GBP. `wedge-signal-entry.md` §0 requires the wedge to
  be provable. Don't route to it.
- **Never default to dead-lead reactivation.** Route from evidence, or mark the wedge unresolved and
  say what's missing.

---

## 4 · Mystery-shop instruction

Per clinic, write the specific test. Dental default:

> Ask for a price on a single implant or full aligner treatment via WhatsApp. Note response time and
> whether anyone asks a qualifying question. Then go quiet 7–14 days and count follow-ups.

This is the quote-decay test — the strongest provable dental wedge, and low-suspicion: "what's the
cost for a single implant" is a completely natural question, and the answer reveals both the price
tier and whether they qualify the enquirer.

**Tilak runs all mystery shops himself. Never send a test enquiry on his behalf.** Leave the field as
`pending — user to mystery-shop`.

---

## Verification

- Reviews returned vs. requested, per clinic. Far fewer than requested → flag, don't silently accept
- Read `statusMessage`, not just `status`; check for a separate errors key
- **Every quote must be a real quote.** Never paraphrase a review and present it as text
- Nothing enters a dossier as fact unless it traces to a specific line — a dated finding, a direct
  review quote, or a confirmed ad/digital-presence fact. Items marked "Potential", "Possible" or
  "Unknown" are hypotheses to test, never findings
- Report actual charge vs. $1.20, and **total spend across both steps vs. the $5.00 ceiling**

---

## Output

**`Pre-outbound-research/batch3-dental-audit.md`** — one block per clinic, following the existing batch
dossier structure:

```
Clinic name · area · GBP category
Founder: name | role | credential | source | confidence
Contact: [channels, each with confidence + front-desk flag]
Instagram: handle | followers | posts | last post | account type
Reviews: total | rating | ≤2★ count and % | last-review gap (months)
Gate B evidence: criterion + exact quote + source URL
Gate C evidence: signal + specifics (advertiser ID / ad text)
F.4 patient-side corroboration: N reviews naming high-ticket work + quotes
Wedge material: [theme → exact review quote]
funnel_break_stage:       [stage]
recommended_entry_sku:    [wedge] — PROVISIONAL
confirm_via_mystery_shop: [the specific test]
status:                   Qualified / Park (+ reason) / Excluded (+ reason)
point_of_contact:         [blank — Tilak or Pratham to assign]
```

**Report inline:**

1. Input count → final qualified count
2. Founder confidence distribution: confirmed / likely / weak
3. How many excluded on F.1 upselling
4. How many showed the Gate C / F.4 contradiction (ads say demand, reviews don't)
5. Wedge distribution — which SKU came up most
6. Spend: this step, and both steps combined vs. $5.00

---

## Post-mortem — answer directly, no hedging

1. Did the two-gate model (B + C) work, or did one gate do all the killing? If Gate C never rejected
   anything Gate B passed, the second gate is decorative and should be cut.
2. Was Google Ads actually the better dental spend signal? That was reasoning, not observation.
3. Did review-text mentions of high-ticket work corroborate the ad evidence, or contradict it?
4. What was the `clinic-brand`-only IG rate, and does the Three Threads sequence survive it?
5. Did the F.1 upselling screen ever fire? If it rejected nobody, it may be unnecessary overhead.
6. Is high-ticket dental in Bangalore a volume vertical, or a 15–20 clinic niche? This decides whether
   there's a batch 2.
7. What would you change in `Dental Discovery Criteria.md` before running again?

**Memory updates — propose, don't write.** For `MEMORY.md` §3 (as `[PROVISIONAL]`),
`files/OUTBOUND_MEMORY.md` §6 decision log, and `Dental Discovery Criteria.md` §6. Follow the
`MEMORY.md` maintenance rule: overrides need real-world proof, new things get appended, duplicates
get skipped. **A completed scrape is not proof that a wedge works — only a reply is.**
