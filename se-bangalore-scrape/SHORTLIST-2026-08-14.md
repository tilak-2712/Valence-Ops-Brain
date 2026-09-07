# SE Bangalore — shortlist from the 35-clinic working list

**Generated** 2026-08-14 · **Inputs** `QUALIFIED-TARGETS-2026-08-14.md` (GBP + IG) ·
`ADS-PRESENCE-2026-08-14.md` (Meta + Google ads, IG audit, Tilak's manual checks 14 Aug)

---

## Verdict first

**Clinics that can be messaged today: 0.**
**Clinics shortlisted for the mystery shop: 15** — 14 from the SE scrape, plus Auguste Skin Clinic
(Shanthala Nagar, separate origin, currently ranked #1).

Every row of the signal→wedge routing table (`wedge-signal-entry.md` §3) is keyed on a *response*
signal — "response slow or none", "fast first reply", "greeting-only auto-reply". §4 of that doc
states it plainly: **scraping cannot determine "response slow or none."** Ads, followers, reviews
and ratings pick the *order* clinics get shopped in. They cannot pick the wedge, and without a
wedge there is no message.

So this file is a **shop queue**, not a send list. `funnel_break_stage` and
`recommended_entry_sku` stay unset for all 35 until a shop runs.

### Gate A has not been run on any of these 35

Hard kill #10 — *no named decision-maker reachable on a personal channel* — is determinable before
outreach and costs about two minutes per clinic. It has not been checked for a single clinic here.
The doc is emphatic about sequencing: on batch-7 evidence, 3 of 10 dossiers need never have been
written because this check came after the expensive step, not before it.

**Run Gate A on Tier 1 and Tier 2 (14 clinics, ~30 minutes) before shopping anything.** Expect some
attrition — the 35 were selected by *website presence*, which says nothing about whether a founder
is named anywhere.

---

## Tier 1 — shop this week (5)

Live paid ads confirmed. These are the only clinics where *"you are paying for enquiries right
now"* is a dated, verifiable fact rather than an assumption — which is the condition `CLAUDE.md` §5
sets before anything can be said to a clinic.

| # | Clinic | Rating (reviews) | Ads | IG | Why it ranks here |
|---|---|---|---|---|---|
| 1 | **Auguste Skin Clinic** | **5.0 (136)** | **Google: ~43 total · 10/30d · 4/7d · 4 yesterday** · Meta: 1 ad, <100 impressions | **5,076 · 406 posts** | Only clinic live on **both** platforms, with the **only named founder** in the set. See below |
| 2 | Cutis Epicorium HSR | 4.7 (235) | **Google: 17 total · 10/30d · 9/7d** | none found | Nine ads in seven days. Actively managed budget, not a stale account |
| 3 | Aiconic Skin Clinic | 4.7 (393) | **Google: 22 ads**, verified | none found | Highest live ad count in the SE cohort, paired with 393 reviews |
| 4 | Zenith Aesthetic Care | 4.3 (274) | **Meta: 3 active** | none found | Only confirmed live Meta advertiser in the SE cohort. Lowest rating (4.3) — check reviews for the reason before shopping |
| 5 | Allure Skin Hair Laser | 4.9 (139) | **Google: 10 total · 2/30d · 1/7d** | none found | Live but thin spend |

**Pattern worth noting:** the four SE-cohort clinics here have **no Instagram** discoverable from
their website. The four buying attention are the four not building it organically. Auguste breaks
the pattern — it does both. Interesting, `hypothesis`, not usable in a message.

### Auguste Skin Clinic — separate origin, not from this scrape

`augusteskin.com` · **Shanthala Nagar** · Co-founder **Dr. Ayesha Sabah**
Source: Tilak, 14 Aug 2026. `confirmed` for the facts below.

**Shanthala Nagar is central Bangalore, not SE.** This clinic did not come from the SE polygon
scrape and is not in `results.json`, `raw/`, or the 35-clinic working list. It is logged here
because it ranks, not because it belongs to the cohort — do not let it inflate any SE denominator.

Why it outranks everything else:

| Signal | Auguste | Best of the SE 35 |
|---|---|---|
| Google ads, last 7 days | **4** | 9 (Cutis Epicorium) |
| Google ads, last 30 days | **10** | 10 (Cutis Epicorium) |
| Google ads, lifetime | **~43** | 22 (Aiconic) |
| Live on both platforms | **Yes** | None |
| Named decision-maker | **Dr. Ayesha Sabah** | None confirmed |
| Instagram | **5,076 · 406 posts, actively maintained** | 16,000 (DYU, dormant advertiser) |
| Rating | **5.0 across 136** | 5.0 across 509 (CLINIQUE) |

Two readings to keep honest:

- **The Meta ad is not a Meta presence.** One ad under 100 impressions is a rounding error, not a
  campaign. Auguste is a *Google* advertiser that has touched Meta. Do not describe them as running
  Meta ads.
- **"Probably has a freelancer or agency"** for the Instagram is Tilak's inference — `hypothesis`,
  not fact. It matters in one direction only: an incumbent marketing vendor raises gatekeeper risk
  and edges toward hard kill #7 (*primary ask is lead gen / content*). It does **not** conflict with
  the ValenceOps offer, which sits after the enquiry, not before it.
- **5.0 across 136 reviews** is unusually clean at that volume and can indicate review gating.
  A chronological pull (§0.2, 25+ minimum) would settle it. Not a shop blocker.

### Pre-shop checklist — Auguste

**Two blockers. Everything else is either already satisfied or explicitly not pre-determinable.**

| # | Requirement | Source | Status |
|---|---|---|---|
| 1 | **Published opening hours** | §2.0 — a shop is admissible *only* inside hours the clinic publishes on its own Google profile | ❌ **BLOCKER.** Not held |
| 2 | **A high-ticket procedure to ask about** | §2.1 test 2 — quote decay needs a ₹49,999–₹1.5L procedure | ❌ **BLOCKER.** Service list and pricing not held |
| 3 | `popularTimesHistogram` | §2.0 — the sharpest slot is published-open **and low-traffic**; an ignored enquiry at peak invites *"we were slammed"* | ⚠️ Strongly wanted. Free if the GBP record is pulled for #1 |
| 4 | Oldest Google review date | Hard kill #2 — operating under 12 months | ⚠️ Unknown. 136 reviews implies establishment but does not date it |
| 5 | Named decision-maker | Hard kill #10 / Gate A | ✅ Dr. Ayesha Sabah |
| 6 | Personal channel for her | Hard kill #10 is *named **and** reachable* | ⚠️ Needed before the **message**, not before the shop |
| 7 | Who the other co-founder is | Hard kill #5 — multi-partner sign-off | ⚠️ "Co-founder" implies ≥2. Not a kill for a 2-doctor clinic; matters for who to address |
| 8 | Enquiry volume · avg ticket value · owner detachment · enquiry data | Hard kills #3, #4, #6, #8 | ➖ **Explicitly not pre-determinable.** Mark `undetermined`, do not infer |

Items 1 and 2 are one Google Business Profile pull and one read of `augusteskin.com`. Both are
free — no Apify credit, no API key.

Item 3 is the difference between a finding and a rebuttable finding. Published-open *and* quiet is
the slot with nothing to explain away. Saturday 6pm is open at 92% across this market and is when
the desk is thinnest.

## Tier 2 — shop this batch (10)

No live ads, website present, high review volume. This is `wedge-signal-entry.md` §3 row 5 —
*"No ads · website ✓ · high reviews · slow or no response"* → **Very high** priority, the same
priority band as the ads rows. Not running ads is explicitly **not** a disqualifier (§1.3).

Cut line is **400+ reviews**. That is my line, not the doc's — it is the cohort's top third.

| # | Clinic | Rating (reviews) | Ads | IG | Note |
|---|---|---|---|---|---|
| 5 | iSkin clinic | 4.9 (2317) | none found | none found | 6× the next-highest review count. **Chain risk — verify before working** |
| 6 | SkinOcare | 4.9 (1363) | none found | handle dead | Second-highest volume in the cohort |
| 7 | SKYE - Skin & Hair Sciences | 4.7 (564) | none found | none found | |
| 8 | CLINIQUE — Dr Idris | 5.0 (509) | none found | none found | Perfect 5.0 across 509. Hair transplant — high ticket. **Possible multi-location** |
| 9 | Rejuvaderm | 4.7 (508) | Meta page match, **recency unchecked** | none found | Moves to Tier 1 if the page is live |
| 10 | Dr Shishira R J - Skin Aura | 4.9 (498) | none found | none found | |
| 11 | SkinChime | 4.9 (469) | none found | 5,525 · 1,058 posts | Doctor-led brand: *"Dr Arpita, Dermatologist in Bangalore"* |
| 12 | The New Body Perfect & Smile Lounge | 4.5 (462) | none found | none found | Weight-loss / electrolysis led — **confirm it fits the vertical** |
| 13 | Smiles N Aesthetics | 4.8 (421) | none found | none found | Dental-led. In scope per `CLAUDE.md`, different treatment economics |
| 14 | Derma Elite Skin Care | 4.7 (402) | Meta page match, **recency unchecked** | 1,855 ✅verified | Moves to Tier 1 if the page is live |

**Rows 9 and 14 are the cheapest upgrades available.** Both are confirmed advertisers whose
recency was never checked — the check is one look at each Meta page, no API key. If either is live,
it joins Tier 1 and the shop order changes.

---

## Tier 3 — queue behind the above (21)

Not rejected. Nothing here clears the Tier-1 or Tier-2 bar on current evidence, and several would
move up on one cheap check.

| Clinic | Rating (reviews) | Ads | IG | Distinguishing signal |
|---|---|---|---|---|
| Dr. Pai Skin, Hair & Healthcare | 4.8 (384) | none | 145 · 175 posts | 16 reviews short of Tier 2. Doctor-led: *"Dr Ravish Pai"* |
| Clinique Internationale | 4.9 (362) | none | handle dead | |
| Yogin's Clinic | 4.8 (331) | none | none | |
| AMINTRI Skin & Hair | 4.7 (329) | none | **~10,000** · 71 posts | 140+ followers/post — anomalous, unverified |
| SkinCure Clinic - Dr. Ashish B Shetty | 4.8 (329) | none | none | |
| Dr Veena Rao's Aviva | 4.9 (314) | none | none | |
| Dr Harini BS | 4.9 (287) | none | none | |
| Dr Mradula's Aesthetica | 4.8 (264) | **confirmed none** *(TS)* | none | Ads ruled out by hand — no reactivation wedge |
| Epiderma Skin and Hair | 4.8 (258) | **confirmed none** *(TS)* | 201 · **846 posts** | Highest post count, second-lowest audience. Doctor-led |
| Tricho Derma Clinic | 4.6 (246) | none | none | |
| The Derma Theory | 4.7 (243) | Meta match, recency unchecked | 5,993 · 746 posts | Third cheap upgrade — check the Meta page |
| Skin Xperts Super-speciality | 4.7 (240) | none | none (Wix badge only) | |
| Vahin Wellness Centre | 4.1 (236) | none | none | Lowest rating in the cohort |
| DYU Aesthetics | 4.9 (217) | **Google: 5 total · 0/30d** — dormant | **~16,000** ✅verified · 633 posts | Strongest IG in cohort. Meta `DYU Healthcare` still unresolved |
| AHIS Aesthetics | 5.0 (207) | none | none | Perfect 5.0. Hair transplant — high ticket |
| Maira Wellness Clinic | 4.6 (195) | none | none | |
| Aesthetic Grandeur | 4.9 (172) | none | **~13,000** · 76 posts | 170+ followers/post — anomalous, unverified |
| Arvique Aesthetics | 4.9 (154) | none | 1,039 · 107 posts | |
| Vivaa Wellness Center | 4.4 (142) | **Google: 5 total · 0/30d** — dormant | none | Meta `VIVAA Wellness Clinic` still unresolved |
| Krian Healthcare | 4.6 (140) | none | none | Listed as general practitioner — confirm vertical fit |
| Dr Jyothshna's Skin Hair & Laser | 4.6 (134) | none | none | |

---

## What would change this ranking, cheapest first

| Check | Cost | Effect |
|---|---|---|
| Meta page recency for Rejuvaderm, Derma Elite, The Derma Theory | 3 page loads | Up to 3 clinics move into Tier 1 |
| Meta resolution for DYU and Vivaa | 2 page loads | Either moves from dormant to live |
| Gate A — named decision-maker, Tiers 1–2 | ~30 min | Removes clinics that cannot be personalised at all |
| Chain check on iSkin, CLINIQUE/Dr Idris, AHIS | brand-count across `raw/` | Catches the La Densitae shape before effort is spent |
| Chronological review pull, 25+ per clinic | Apify | The only route to booking-friction and ghosting signals (§3 rows 9–10), currently invisible |

The last one is the real gap. Review *counts* are in hand; review *text* is not, and §0.2 requires
chronological pulls of 25+ before any review-derived finding can ship. Two routing rows — no-show
recovery and quote-decay — are unreachable without it.

---

## What this file deliberately does not do

It does not assign a wedge to any clinic. Ads presence narrows the candidates
(`wedge-signal-entry.md` §3 rows 1–4 need ads; row 5 needs their absence) but every one of those
rows still turns on the response finding. Assigning a wedge now would mean guessing at the one
variable the whole framework is built to test — and per §4 both schema fields stay `PROVISIONAL`
until the shop has run.

The dormant advertisers invite the read *"they stopped because leads weren't converting."* That is
recorded as `hypothesis` in `ADS-PRESENCE-2026-08-14.md` with its rebuttal attached, and is not a
ranking input here.
