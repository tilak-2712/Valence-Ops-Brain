---
date_created: 2026-08-09
date_modified: 2026-08-09
status: active
---
# STEP 1 — QUALIFY (Bangalore Dental)

**Cap: $3.00.** Output: a shortlist of clinics that actually fit the ICP. No dossiers, no review
text, no wedge routing — that's Step 2.

Context doc: `Dental Discovery Criteria.md`. Read it before running this.

**Purpose of splitting this out:** dental ATV is bimodal inside a single clinic — the same practice
runs ₹3,000 root canals and ₹3,00,000 full-arch cases. GBP category can't tell them apart. So
qualification is a real step here, not a formality, and no clinic gets expensive research until it
survives it.

---

## Before you spend anything

### Two blockers — ask me, wait for answers

1. **Dental exclusion:** `Apify Discovery Context.md` §2.2 excludes dental this round; `CLAUDE.md`
   lists it as a target. Which governs?
2. **IG gate:** §2.5 accepts a clinic account, but `personalized-outbound-v2.md` needs a **personal
   founder account** for the Three Threads sequence, and `MEMORY.md` §5 records this biting already
   (Juvita, Vtiara, Sapphire). Dental founders under-index on personal IG. Do brand-page-only clinics
   pass, park, or die? *If unanswered, default to park-and-flag — never silently pass.*

### Free pre-check (recommended, costs $0)

Run gates A–D on the 11 clinics in `05 Prospects/Batch 3 Aesthetic and Dental/Batch 3 Dental Audit.md` using only the data
already in that file. Known answers to check against: **Dr Tanisha** (MDS Prosthodontist &
Implantologist), **Smile Xpressions** (`@drshagunagarwal_invisalign`) and **Aesthete** (aligners in
review text) should all pass Gate B. **Small Bites** should die at Gate A. If they don't, the gates
are written wrong — fix them before scraping.

### Preflight

- Read `https://api.apify.com/v2/users/me/limits`. Report real remaining credit; rescale caps if under $5.
- `fetch-actor-details` on: `compass/crawler-google-places`, `apify/instagram-profile-scraper`,
  `apify/website-content-crawler`, `scrapesage/google-ads-transparency-scraper`,
  `apify/facebook-ads-scraper`. **`website-content-crawler` is new to this project** — estimate the
  cost of 6 pages × 60 domains and flag if it breaks the $0.85 sub-cap.
- Build the exclusion list: `Apify Discovery Context.md` §4 + the 11 clinics in
  `Batch 3 Dental Audit.md`. Match loosely (case, punctuation, `Dr.`, `&`/`and`, branch suffixes).

**Report preflight and wait for go-ahead before scraping.**

---

## Budget inside this step

| Sub-step | Actor | Cap |
|---|---|---|
| 1A Discovery | `compass/crawler-google-places` (`maxReviews: 0`) | $1.10 |
| 1B Instagram | `apify/instagram-profile-scraper` | $0.55 |
| 1C Procedure | `apify/website-content-crawler` | $0.85 |
| 1D Demand | Google Ads Transparency + Facebook Ads | $0.50 |
| | **Step 1 total** | **$3.00** |

Set `maxTotalChargeUsd` on every call. Never carry an unspent sub-cap forward without telling me.

---

## 1A · Discovery + hard kills — cap $1.10

`compass/crawler-google-places` · `maxReviews: 0` · `scrapeContacts: true` · `language: "en"` ·
`countryCode: "in"` · `timeout: 600`

**Metadata only.** Review text is Step 2 and it's where the money goes.

**Search terms — primary. Split into calls of 4–6 terms; all-at-once has timed out before.**

```
dental implant clinic · dental implant centre · implantologist
all on 4 dental implants · full mouth rehabilitation · full mouth implants
smile makeover clinic · smile design clinic · dental veneers
cosmetic dentist · aesthetic dentistry clinic
clear aligners clinic · invisalign provider · orthodontist
prosthodontist · dental aesthetics clinic
```

**Secondary — only if primary yields under 200 records:**
`dental clinic · dental studio · multispeciality dental clinic · dental care centre`

**Never run:** `dentist near me` · `kids dentist` · `pediatric dental` · `emergency dental` ·
`teeth cleaning` · `root canal clinic` — these return the low-ATV pain segment by construction.

Rotate against the Bangalore micro-markets in `Apify Discovery Context.md` §3. Karnataka only.
Overflow to Mysuru / Mangaluru / Hubballi-Dharwad only if Bangalore falls short.
**Raw target: 250–350 records.**

### Gate A — kill in this order

1. Name matches the exclusion list
2. **Kids-only / pediatric** — `kids`, `child`, `children`, `pedo`, `pediatric`, `paediatric`
3. Not an independent dental clinic — hospital, lab, pharmacy, aggregator, or a doctor's profile inside a hospital
4. **Mixed skin/aesthetic + dental** (per criteria Gate A.7 — report this count separately)
5. Review count < 20
6. **Chain** — 6+ branches, 3+ states, or a corporate/DSO parent. Count branches across the whole raw pull; the branch-count rule is the mechanism, the name list in `Dental Discovery Criteria.md` §4 is an unverified shortcut
7. Geographic mismatch — GBP says Bangalore, website or bio says elsewhere
8. No website **and** no Instagram **and** no GBP contact info

### Tiering — ordering only, NOT a kill

**TIER-1** if name or category contains: `implant` · `prostho` · `ortho` · `aligner` · `invisalign` ·
`smile design` · `smile makeover` · `cosmetic dent` · `aesthetic dent` · `veneer` · `full mouth` ·
`all on 4` · `all on 6` · `maxillofacial`

**TIER-2** = everything else that survived. A generically-named practice can still be an implant
practice — 1C is the real check. TIER-2 only gets processed if TIER-1 doesn't produce 15–20 qualified.

**Process TIER-1 through 1B–1D first.**

---

## 1B · Instagram gate — cap $0.55

`apify/instagram-profile-scraper` on TIER-1 survivors. Scrape the clinic account, and the personal
founder account too if one is named on GBP or the website.

Apply `Apify Discovery Context.md` §2.5 unchanged:

| Test | Threshold |
|---|---|
| Clinic **or** founder IG exists, public | Yes |
| Followers | **≥ 1,000** (under → reject, no exceptions) |
| Posts | **≥ 20** |
| Last post | **within 60 days** |

Preferred band 2,000–80,000. Over 100,000 → **PARK**, max 3, listed separately, doesn't count toward
target. Engagement under 0.5% → flag `possible bought followers`, don't reject.

**Record account type per clinic:** `founder-personal` / `clinic-brand` / `both`. Apply my blocker
answer; default to park-and-flag.

*Runs before the procedure gate because it's cheaper per rejection, even though it's the softer kill.*

---

## 1C · Procedure gate — cap $0.85 · the hardest cut

`apify/website-content-crawler` on 1B survivors. `maxCrawlDepth: 2`, `maxCrawlPages: 6` per domain.
Target URLs containing: `services` · `treatments` · `implant` · `ortho` · `aligner` · `invisalign` ·
`smile` · `cosmetic` · `veneer` · `about` · `team` · `doctors`.

No website → don't crawl. Fall back to IG bio + highlight titles + GBP service list, mark
`confidence: weak`.

### Gate B — confirm AT LEAST ONE

1. **Named premium implant system** — Nobel Biocare, Straumann, or equivalent
   *(Korean-only — Osstem, Dentium — at ₹15–30K → record `borderline: korean-only`, don't auto-pass)*
2. **Invisalign provider status** or a named clear-aligner partnership
3. **Smile design or veneers** as a distinct service page, not a buried line item
4. **Full-mouth rehab / All-on-4 / All-on-6** named as a service
5. **Founder credential** — MDS Prosthodontist, Implantologist, or Orthodontist

**Auto-fail:** site and IG dominated by cleanings, fillings, RCT, extractions, check-ups with no
high-ticket service page anywhere.

**Every pass must cite the exact URL or bio line the evidence came from.** A pass with no citable
source is not a pass. A "Potential" or "Possible" item is a hypothesis to test, never a finding.

**🛑 If Gate B rejects more than 70% of its input, stop and report before 1D.** That's not a run
failure — it's a finding that the high-ticket dental population in Bangalore is thinner than assumed,
and it's worth knowing before spending the rest.

---

## 1D · Demand gate — cap $0.50

`scrapesage/google-ads-transparency-scraper` first and heaviest, `apify/facebook-ads-scraper` second.
Google is primary in dental — search intent dominates. **This is the inverse of the aesthetic runs
and it's deliberate.**

### Gate C — confirm AT LEAST ONE

Gate B proves the clinic *offers* high-ticket work. Gate C proves someone is *buying* it. A clinic
with an All-on-4 page doing two arches a year has a ₹5L sticker price and no addressable pipeline.
**Both B and C must pass.**

1. **Google Ads on high-ticket keywords** ★ — implant, aligner, Invisalign, smile makeover, smile
   design, veneers, full mouth. Record advertiser ID, ad count, last-shown date, actual ad text.
   **Ads on `dentist near me`, emergency, toothache, RCT, extraction or cleaning do NOT count** —
   that's the pain segment, below the ₹25,000 bar. A clinic advertising only on pain terms fails Gate
   C even though it's clearly spending. Log these separately as near-misses.
2. **Practo Prime or JustDial paid listing** — counts fully. Manual check is fine; say it was manual.
3. **Meta ads on high-ticket procedures** — corroborating, weaker in dental. A Meta-only pass with
   nothing else is a **PARK**, not a PASS.

Fails all three → **kill**.

---

## Verification — before any report

- Items returned vs. submitted, at every sub-step. A search term or profile returning zero is a
  signal, not a non-event — name it
- Read `statusMessage`, not just `status`. "Succeeded" has silently returned 0 items on this project
  after a mid-run rate limit
- Check for a separate errors/summary key and report its contents
- Spot-check 5 records per sub-step for field completeness
- **"No ads found" must mean the check ran and returned zero, not that it was skipped.** State which
- Any finding that reverses an earlier one gets manually verified before it's recorded — "no ads"
  flipping to "26 active ads" happened before and the reversal was wrong until independently confirmed

---

## Output

**`_dental-qualified.md`** — one row per survivor:

`clinic name | area | GBP category | review count | rating | website | phone | IG handle / followers / last post / account type | Gate B criterion + exact evidence + source URL + confidence | Gate C signal + specifics | TIER | status (QUALIFIED / PARK + reason)`

**`_dental-rejected.md`** — every drop: `clinic name | gate | specific reason`

**Report inline:**

1. Raw count by search term → survivors at each gate, with drop reasons
2. Gate B rejection rate, and whether the 70% stop condition fired
3. Gate C: which signal carried each pass; how many are pain-segment-only near-misses
4. **Account-type distribution — how many are `clinic-brand` only. If that's over half, say so loudly:
   it means the Three Threads sequence needs rework before this batch can ship, which is a bigger
   finding than the clinic list.**
5. Actual spend vs. $3.00, by sub-step
6. Qualified count, TIER-1 vs TIER-2

**Stop. Step 2 runs only on QUALIFIED rows, after my go-ahead.**


---
Related: [[01 Playbooks/Dental Discovery/Dental Discovery Criteria|Dental Discovery Criteria]] · [[01 Playbooks/Research Prompts/Apify Discovery Context|Apify Discovery Context]] · [[CLAUDE|CLAUDE]] · [[01 Playbooks/personalized-outbound-v2|personalized-outbound-v2]] · [[MEMORY|MEMORY]] · [[05 Prospects/Batch 3 Aesthetic and Dental/Batch 3 Dental Audit|Batch 3 Dental Audit]] · [[04 Clients/Sapphire Skin and Aesthetics/Sapphire Skin and Aesthetics|Sapphire Skin and Aesthetics]]
