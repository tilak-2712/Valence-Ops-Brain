---
date_created: 2026-08-02
date_modified: 2026-08-13
status: reference
---
# Pre-Outbound Research — Full Batch Report

> *(⚠️ Retired tests: the six-test SOP was cut to two — qualification and quote decay — on 2026-08-13. Persistence, after-hours, cross-channel and booking friction no longer run. See `wedge-signal-entry.md` §2.)*

## 10 Aesthetic Clinics · Bangalore, Mysuru · Karnataka

**Research date:** 2026-08-01
**Pipeline:** `clinic-audit-research` (Apify)
**Depth mode:** Standard for 9 clinics; **Deep** for Koza Aesthetic Care (confirmed multi-branch chain)
**Clinics researched:** 10 · **Locations audited:** 16 (branches counted separately)
**Outcome:** 9 Qualified · 1 Park · 0 Disqualified

> **This batch is provisionally complete, not decision-ready.**
> The Go/No-Go gate in the audit checklist cannot be satisfied by scraped data alone — it requires the mystery shop, which this pipeline never runs (you do that personally). Every `recommended_entry_sku` below is a **data-backed hypothesis marked PROVISIONAL**, with an explicit note on what mystery-shop finding would confirm or redirect it.

---

## Table of contents

1. [How to read this report](#1-how-to-read-this-report)
2. [Method and verification standard](#2-method-and-verification-standard)
3. [Batch at a glance](#3-batch-at-a-glance)
4. [Priority queue](#4-priority-queue--who-to-shop-first-and-why)
5. [Batch comparison table](#5-batch-comparison-table)
6. Full clinic dossiers
   - [6.1 Contour Cosmetic Clinic](#61-contour-cosmetic-clinic)
   - [6.2 Sanssouci Wellness Clinic](#62-sanssouci-wellness-clinic)
   - [6.3 Sparha Advanced Aesthetic Studio](#63-sparha-advanced-aesthetic-studio)
   - [6.4 SkinFit Wellness](#64-skinfit-wellness)
   - [6.5 Skin and Recon](#65-skin-and-recon)
   - [6.6 Advanced GroHair GloSkin — Jayanagar](#66-advanced-grohair-gloskin--jayanagar-branch)
   - [6.7 Koza Aesthetic Care (5 branches)](#67-koza-aesthetic-care--5-branch-chain)
   - [6.8 SS Aesthetic Clinic](#68-ss-aesthetic-clinic)
   - [6.9 Rua Skin & Hair Center (2 branches)](#69-rua-skin--hair-center--2-branches)
   - [6.10 Feather Touch Aesthetic Clinic & Academy](#610-feather-touch-aesthetic-clinic--academy--parked)
7. [Cross-batch patterns](#7-cross-batch-patterns)
8. [Corrections made during self-review](#8-corrections-made-during-self-review)
9. [Limitations — what was not verified](#9-limitations--what-was-not-verified)
10. [Tool health notes](#10-tool-health-notes-for-the-next-batch)
11. [Data provenance](#11-data-provenance)
12. [Recommended next actions](#12-recommended-next-actions)

---

## 1. How to read this report

### Contact confidence labels
Every named contact carries one of four labels. A name match alone is never treated as confirmation.

| Label | Meaning |
|---|---|
| **confirmed** | The clinic's own website/page names this person in this role, or their own profile names the clinic |
| **likely** | Corroborated by role, credential, or locality — but not stated on both sides |
| **weak** | Name matches only, no corroboration (e.g. a staff name appearing only inside a patient complaint) |
| **none found** | No named human was discoverable through any source checked |

### Ad-status values
| Value | Meaning |
|---|---|
| **active** | Ads confirmed running, verified this session |
| **dormant** | Ads confirmed to have run historically, confirmed stopped, with a date |
| **none found** | Checked the clinic's own page/ID directly and found nothing |
| **inconclusive** | Search returned only unrelated results and no direct page/ID existed to check |
| **undetermined** | The check ran but the tool cannot be trusted to have answered (see §10) |

`undetermined` is **not** the same as "no ads." This distinction matters: reporting "no ads" from an unreliable check is a documented failure mode of this pipeline, and it happened to be triggerable in this exact batch.

### Funnel break stages
Drawn strictly from the wedge playbook §4 enum: `Response Speed` · `Qualification` · `Follow-up Persistence` · `Quote Chase` · `Booking / No-show` · `Post-consult` · `Reviews` · `Reactivation` · `None (pass)`.

### Wedge names
Every `recommended_entry_sku` is quoted verbatim from the playbook's §3 routing table. No wedge names were invented for this batch.

### A note on review quotes
Google reviews contain real patients' names and medical details. Quotes below are **minimized deliberately**: they carry only what establishes the *business* finding. Reviewer names are omitted, and clinical specifics are reduced to the minimum needed to convey severity. Where an allegation is serious, it is stated as an allegation and surfaced prominently rather than smoothed into surrounding prose.

---

## 2. Method and verification standard

### What was run
| Step | Actor | Coverage |
|---|---|---|
| Instagram profile refresh | `apify/instagram-profile-scraper` | All 10 handles — bio, followers, posts, external URL |
| Google Business Profile + reviews + contact enrichment | `compass/crawler-google-places` | 5 runs, 22 places returned, ~1,100 reviews pulled newest-first |
| Meta ads (keyword sweep) | `apify/facebook-ads-scraper` | All 10 clinics |
| Meta ads (direct page verification) | `apify/facebook-ads-scraper` | 3 clinics where a real FB page URL was known |
| Google Ads Transparency (name + domain) | `scrapesage/google-ads-transparency-scraper` | All 10 clinics, both query paths |
| Google Ads Transparency (direct advertiser ID) | `scrapesage/google-ads-transparency-scraper` | 3 known advertiser IDs — used as the tie-break |
| Website team/about/contact crawl | `apify/website-content-crawler` | 8 domains, 14 pages captured |
| LinkedIn person search | `harvestapi/linkedin-profile-search` | **Failed — daily free-tier cap hit** |

### Actor-health preflight (run before spending)
All actors confirmed live and non-deprecated. Success rates at time of check: `compass/crawler-google-places` 88.8% (the weakest — flagged, and its coverage was individually verified per clinic), `apify/facebook-ads-scraper` 98.4%, `scrapesage/google-ads-transparency-scraper` 99.1%, `harvestapi/linkedin-profile-scraper` 99.5%, `apify/instagram-profile-scraper` 99.6%, `apify/website-content-crawler` 96.8%.

### The six-point verification loop, applied after every call
An Apify `SUCCEEDED` status means "the code exited," not "the data is real." Each run was checked for:

1. **Coverage** — items returned vs. inputs submitted. *This caught three separate gaps in this batch* (Rua's second branch, Koza's sixth branch, SkinFit's claimed second location).
2. **Error/summary key-value records** — read where present.
3. **Full `statusMessage`** — *this is how the LinkedIn cap was caught*: the actor reported `SUCCEEDED` while its status message read `"free user run limit reached"` and it returned zero items.
4. **Field completeness with quirk awareness** — distinguishing genuinely empty fields from known-benign artifacts.
5. **Cross-source corroboration** — GBP vs. Instagram vs. website, checked for agreement on phone, domain, and branch count. *Mismatches found and reported rather than silently resolved.*
6. **Manual tie-break on load-bearing claims** — anything that reverses a prior finding got one direct check. *This is how the Google Ads tool failure was caught.*

### Prior-batch data was deliberately not trusted
A handoff file in the working directory contained Instagram data and partial Google Ads results for 8 of these 10 clinics from an earlier session. **None of it was carried forward as fact.** Instagram was re-pulled fresh and Google Ads was re-verified. The handoff was used only for steering — which doctors to look for, which sites are chains. Two clinics (Sparha, Feather Touch) were entirely new.

### Four GBP runs timed out at 600 seconds
This is a known behavior of `compass/crawler-google-places` at this review depth, not a failure. All four had already written their results before hitting the wall; partial output was harvested and the missing slices were re-run in a targeted follow-up. Coverage was reconciled per clinic before anything was reported.

---

## 3. Batch at a glance

| Metric | Value |
|---|---|
| Clinics researched | 10 |
| Locations audited | 16 |
| Qualified | 9 |
| Parked | 1 (Feather Touch — mega-founder-brand) |
| Disqualified | 0 |
| Confirmed active ad spend (Meta and/or Google) | 6 clinics |
| Google Ads status marked `undetermined` | 7 clinics (tool failure, §10) |
| Founder/owner identified with **confirmed** confidence | 5 clinics |
| Clinics with **no named human** found at all | 3 (Koza, Sanssouci, Feather Touch) |
| Reviews read and analyzed | ~1,100 across 16 locations |
| Clinics with escalation-grade allegations | 1 (Sparha) |
| Personal LinkedIn profiles resolved | 0 — actor cap hit |
| Aggregator (Practo/JustDial) paid listings checked | 0 — no verified actor exists |

**Estimated Apify spend:** roughly **$1.50–2.50**. This is an estimate from observed per-event pricing and item counts, not a figure read from your billing page — check the Apify console for the exact charge.

---

## 4. Priority queue — who to shop first, and why

Ranked by **strength of verified evidence**, not by clinic size. The ranking answers one question: where is the mystery shop most likely to confirm a real, sellable gap?

### Tier 1 — shop this week

**1. Contour Cosmetic Clinic.** The only clinic in the batch whose ad spend is confirmed *active today* through a direct advertiser-ID lookup rather than a fuzzy search — the highest-confidence "ads✓" signal available. Pair that with a 33% owner-reply rate on negatives (well below the batch's better performers) and the dead-lead reactivation hypothesis has genuine evidential weight rather than being a default assumption.

**2. Sanssouci Wellness Clinic.** Active Meta spend feeding a clinic with the batch's **highest negative-review rate (16.7%)** and the single most consistent complaint shape found anywhere in this batch — four independent reviewers, in their own words, describing paying for multi-session packages and receiving no measurable result. That pattern is screenshot-provable and sits directly next to money already spent.

**3. Sparha Advanced Aesthetic Studio.** Active ads, 352 reviews, and a recurring pattern of ₹1L–2L package commitments where support allegedly deteriorated after payment. Carries escalation-grade allegations that you should read before deciding to pursue (§6.3).

### Tier 2 — queue within this batch

**4. SkinFit Wellness.** The cleanest *directly observed* funnel signal in the batch, requiring no mystery shop to establish: the review engine stopped **10.4 months ago**. Reviews aren't slow — they're stopped, with a 0% owner-reply rate on the negatives that do exist.

**5. Koza Aesthetic Care (Jaya Nagar branch specifically).** Within a 5-branch chain running confirmed ads on both platforms, one branch is visibly failing: 3.8★, a 27% negative rate, and 8% owner reply. Its negatives are *current*, including one posted the day of research.

**6. Advanced GroHair GloSkin (Jayanagar).** Two independent reviews describing multi-session treatments abandoned mid-course with no chase from the clinic — a persistence gap rather than a first-response gap.

### Tier 3 — shop to disprove, not to confirm

**7. Skin and Recon.** The healthiest reputation in the batch (3.3% negatives, 100% reply rate, two fully credentialed named leads). Ads stopped ~4 months ago. There may simply be no gap here — treat the shop as a test of whether this is a "None (pass)."

**8. SS Aesthetic Clinic** and **9. Rua Skin & Hair Center.** Both have active ads and *zero* negative reviews across their entire history. There is no review-based evidence of a break at either. The wedge assignment rests entirely on the "ads✓ + unknown response speed" default. Be willing to record these as passes.

### Parked — different motion entirely

**10. Feather Touch Aesthetic Clinic & Academy.** 45,037 Instagram followers, 803 reviews, 100% negative-reply rate — the healthiest engagement metrics in the batch. This is a mega-founder-brand: longer cycle, harder access, nurture rather than cold DM.

---

## 5. Batch comparison table

One row per clinic **or branch**. `undetermined` = check ran but couldn't resolve · `not_run` = step skipped by depth mode · `n/a` = genuinely not applicable.

| clinic_name | branch | locality | rating | reviews_total | reviews_90d | neg_90d | reviews_180d | neg_180d | last_review_gap_mo | owner_reply_rate_neg | meta_ads | google_ads | funnel_break_stage | recommended_entry_sku | wedge_state | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Contour Cosmetic Clinic | — | BTM, Bangalore | 4.8 | 334 | 45 | 2 | 53 | 2 | 0.2 | 33% | active | **active today** | Reactivation | Dead-lead reactivation | PROVISIONAL | Qualified |
| Sanssouci Wellness Clinic | — | Mysuru | 4.2 | 148 | 4 | 0 | 16 | 2 | 0.8 | 80% | active | undetermined | Reactivation | Dead-lead reactivation | PROVISIONAL | Qualified |
| Sparha Advanced Aesthetic Studio | — | Indiranagar | 4.2 | 352 | 10 | 2 | 15 | 2 | 0.3 | 89% | active | undetermined | Quote Chase | Quote-decay follow-up | PROVISIONAL | Qualified — flagged |
| SkinFit Wellness | Koramangala | Bangalore | 4.9 | 120 | 0 | 0 | 0 | 0 | **10.4** | 0% | inconclusive | undetermined | Reviews | Review reactivation agent | PROVISIONAL | Qualified |
| Skin and Recon | — | Jayanagar | 4.9 | 242 | 43 | 0 | 57 | 1 | 0.5 | 100% | none found | dormant since Apr '26 | Reactivation | Dead-lead reactivation (weak) | PROVISIONAL | Qualified |
| Advanced GroHair GloSkin | Jayanagar | Bangalore | 4.7 | 119 | 24 | 0 | 37 | 3 | 0.1 | 50% | active | undetermined | Follow-up Persistence | Follow-up and nurture engine | PROVISIONAL | Qualified |
| Koza Aesthetic Care | **Jaya Nagar** | Bangalore | **3.8** | 44 | 2 | 2 | 4 | 2 | 0.0 | **8%** | active | active (1 ad) | Reactivation | Dead-lead reactivation | PROVISIONAL | Qualified — weak branch |
| Koza Aesthetic Care | HRBR/Kalyan Nagar | Bangalore | 4.6 | 9 | 1 | 1 | 1 | 1 | 2.8 | 0% | active | active (1 ad) | Reactivation | Dead-lead reactivation | PROVISIONAL | Qualified |
| Koza Aesthetic Care | Banashankari | Bangalore | 5.0 | 20 | 0 | 0 | 0 | 0 | 10.1 | n/a | active | active (1 ad) | Reactivation | Dead-lead reactivation | PROVISIONAL | Qualified |
| Koza Aesthetic Care | Arekere | Bangalore | 5.0 | 2 | 0 | 0 | 0 | 0 | 19.5 | n/a | active | active (1 ad) | Reactivation | Dead-lead reactivation | PROVISIONAL | Qualified |
| Koza Aesthetic Care | Sarjapur Road | Bangalore | — | 0 | 0 | 0 | 0 | 0 | n/a | n/a | active | active (1 ad) | not_run | not_run | PROVISIONAL | Qualified |
| SS Aesthetic Clinic | — | Indiranagar | 5.0 | 43 | 13 | 0 | 38 | 0 | 0.0 | n/a (0 neg) | active | undetermined | Reactivation | Dead-lead reactivation | PROVISIONAL | Qualified |
| Rua Skin & Hair Center | Ramamurthy Nagar | Bangalore | 4.9 | 80 | 17 | 0 | 61 | 0 | 0.0 | n/a (0 neg) | active | undetermined | Reactivation | Dead-lead reactivation | PROVISIONAL | Qualified |
| Rua Skin & Hair Center | Indiranagar | Bangalore | 5.0 | 17 | 10 | 0 | 17 | 0 | 0.8 | n/a (0 neg) | active | undetermined | Reactivation | Dead-lead reactivation | PROVISIONAL | Qualified |
| Feather Touch Aesthetic | Jayanagar (main) | Bangalore | 4.8 | 803 | 78 | 4 | 120 | 4 | 0.1 | 100% | inconclusive | undetermined | Post-consult | Founder capacity protection | PROVISIONAL | **Park** |
| Feather Touch Aesthetic | Mysuru | Mysuru | 5.0 | 5 | 5 | 0 | 5 | 0 | 0.0 | n/a | inconclusive | undetermined | not_run | not_run | PROVISIONAL | **Park** |

A machine-readable version with the full field contract (including contact columns and `unverified_fields`) is at [batch-comparison-table.csv](batch-comparison-table.csv).

---

## 6. Full clinic dossiers

---

### 6.1 Contour Cosmetic Clinic

**Locality:** 2nd floor, Lakshmidevi Complex, 80 Ft Rd, Vishweshwaraiah Road, 6th Stage Phase 2, BTM Layout, Bengaluru 560076
**Category:** Hair transplantation clinic
**Depth mode:** Standard

#### Basic info
| Field | Value |
|---|---|
| Phone | +91 86604 32589 |
| Email | contact@contourcosmeticclinic.com |
| Website | contourcosmeticclinic.com (live, crawled) |
| Instagram | @contour_hair — 4,443 followers, 446 posts, **verified account** |
| LinkedIn (company) | linkedin.com/company/contour-cosmetic-clinic |
| YouTube | @shapeyourstory |
| Legal entities on record | "Contour Cosmetic Clinic" and "Contour Cosmetic Clinic LLP" — both verified advertisers |

**Notable:** the Instagram bio's external link is a **WhatsApp deep link** (`wa.me/918660432589`), not a website. The clinic is deliberately routing social traffic straight into WhatsApp — consistent with the project's standing assumption that WhatsApp is the real booking engine, and directly relevant to where a dead-lead backlog would physically live.

#### Disqualification screen
No hard kills triggered. Has website + Instagram + GBP; operating well over 12 months (review history predates 2026 substantially); single clinic with two named clinical leads, not a corporate committee; the ask is ops automation, not marketing. No park signals. **Qualified.**

#### Contacts
| Name | Role | Source | Confidence |
|---|---|---|---|
| **Dr. Saket Jha** | Lead surgeon — MDS (OMFS), FFPS, FFAS. Maxillofacial, Facial Plastic & Hair Transplant Surgeon | contourcosmeticclinic.com team section, explicitly "Led by Dr. Saket Jha" | **confirmed** |
| **Dr. Akanksha Thakur** | Otolaryngologist, Plastic & Reconstructive Surgeon — MBBS, MS-ENT | contourcosmeticclinic.com team section | **confirmed as team member; name variant unresolved** |

**Name discrepancy, unresolved:** the clinic's own Instagram bio credits the clinic to "@drsaket.jha & @drakanksha.**jha**" while the website team page names her Akanksha **Thakur**. Very likely the same person (maiden vs. married name), but this was not independently confirmed. If outreach personalizes to her by name, verify first.

LinkedIn personal profiles: **not attempted** — actor cap exhausted. The *company* page is independently confirmed via GBP contact enrichment.

#### Ads — the load-bearing finding
This is the most important verified fact in the batch, and it required a manual tie-break to establish.

**Google Ads Transparency, via direct advertiser-ID lookup:**

| Entity | Advertiser ID | Verified | Ad activity |
|---|---|---|---|
| Contour Cosmetic Clinic | `AR10209256018437734401` | yes | **Currently active.** Latest ad last shown **2026-08-01 (research day)**. Continuous TEXT/IMAGE/VIDEO creatives running since March 2026, individual ads sustained 11–42 days each |
| Contour Cosmetic Clinic LLP | `AR14094849889598963713` | yes | **Dormant.** 10 creatives ran Aug 2025 → all stopped by **2026-02-11** |

**Interpretation:** this reads as a genuine entity restructuring — the LLP-registered ad account was retired around February 2026 and the main entity took over, with spend continuing uninterrupted since. This clinic is, right now, among the most consistent Google Ads spenders in the batch.

**Why this matters beyond Contour:** a brand-name query for "Contour Cosmetic Clinic Bangalore" returned **zero** advertisers, and a domain query for `contourcosmeticclinic.com` also returned **zero** — for an advertiser that is verifiably active *today*. That failure is what invalidated the Google Ads check for the rest of the batch (§10).

**Meta Ads Library:** active — confirmed via exact page-name match ("Contour cosmetic clinic") within a noisy keyword result set.

**Aggregator paid listing:** undetermined, not checked.

#### Reviews analysis
**4.8★ · 334 reviews total · 120 newest pulled and read in full**

Distribution (all-time): 277×5★ · 47×4★ · 6×3★ · 1×2★ · 3×1★

| Window | Reviews | ≤2★ |
|---|---|---|
| Last 90 days | 45 | 2 |
| Last 180 days | 53 | 2 |
| Most recent review | 2026-07-26 (0.2 months ago) | — |

**Negatives: 3 of 120 sampled (2.5%). Owner reply rate: 33% (1 of 3).**

That reply rate is the operative signal. Skin and Recon and Feather Touch both answer 100% of their negatives; Sparha answers 89%. Contour answers one in three — while spending more measurably on ads than anyone else in the batch. Money is going in the front door faster than attention is going out the back.

Quoted negatives (minimized):
- *2026-07-03, no owner reply* — alleges hair thinned significantly after 5 sessions of an exosome treatment.
- *2026-06-08, owner replied* — alleges a long wait despite holding an appointment, and a rushed consultation.
- *2026-01-28, no owner reply* — one-word text "Super" rated 1★. Almost certainly a mis-tap rather than a complaint; counted in the arithmetic for honesty, but carries no signal.

**Fake-review check:** volume and pacing look organic. A 2.5% negative rate at 334 reviews with genuine 4★ mass (47) rather than a pure 5★ wall is a healthy, believable distribution.

#### Wedge routing
```
funnel_break_stage:       Reactivation
recommended_entry_sku:    Dead-lead reactivation — PROVISIONAL
confirm_via_mystery_shop: Strongest ads✓ evidence in the batch (verified current spend
                          via advertiser ID, not a query match) combined with a
                          below-average negative-reply rate. If the DM/WhatsApp reply
                          is slow or absent, this wedge is very likely correct. If the
                          reply is fast, escalate to the six-test SOP — given the ad
                          volume, qualification, persistence, or quote-decay are the
                          next most probable breaks.
status:                   Qualified — highest ad-spend confidence in batch
unverified_fields:        personal LinkedIn (both doctors); whether "Akanksha Thakur"
                          and "Akanksha Jha" are the same person; aggregator paid
                          listing; reason for the Feb-2026 LLP → main-entity switch
```

---

### 6.2 Sanssouci Wellness Clinic

**Locality:** 1216, 2nd floor, above Toyota showroom, New Kantharaj Urs Road, Ballal Circle, Mysuru 570004
**Category:** Weight loss service (GBP primary category) — operates across skin, hair, and weight loss
**Depth mode:** Standard
**Note:** the only non-Bangalore clinic in this batch. Still Karnataka.

#### Basic info
| Field | Value |
|---|---|
| Phone | +91 96112 11581 · 0821-4526910 |
| Email | contactus@sanssouciwellness.com |
| Website | sanssouciwellness.com (live, crawled) |
| Instagram | @sanssouci_wellness.mysuru — 2,831 followers, 606 posts |
| Established | **19 March 2018** (stated on own website) — comfortably clears the 12-month hard kill |

The website claims an affiliation with **Bellamente Cosmetica, Berlin** and describes "Indo-German methodologies." This is a self-reported marketing claim; it was not independently verified and should not be repeated as fact.

#### Disqualification screen
No hard kills. Operating 8+ years. Not a corporate committee structure as far as can be determined. **Qualified** — though see the contact gap below, which puts it near the "front desk is the only reachable contact" park route without quite landing there.

#### Contacts
| Name | Role | Source | Confidence |
|---|---|---|---|
| — | **No named doctor, founder, or operator found anywhere** | website + Instagram + GBP all checked | **none found** |
| @ai.shikro | "Managed by" per Instagram bio | Instagram bio only | **weak / unresolved** |
| Clinic switchboard | +91 96112 11581 · contactus@sanssouciwellness.com | GBP + website | confirmed |

**The @ai.shikro question stayed open.** The website crawl was expected to resolve it and did not — no management company, agency, or operator name appears anywhere on the site, and the "Expert Team" section names no individuals at all. It could be a marketing agency handle or an internal staff account. **Do not assume either.** If this lead is pursued, resolving who actually makes decisions is step one.

#### Ads
- **Meta Ads Library:** **active** — 3 ads matching "Sanssouci Wellness."
- **Google Ads Transparency:** undetermined (query returned zero; not trusted — see §10).
- **Aggregator:** undetermined, not checked.

#### Reviews analysis
**4.2★ · 148 reviews total · 120 newest read in full**

Distribution (all-time): 104×5★ · 18×4★ · 3×3★ · 0×2★ · **23×1★**

That 1★ tail is ~15.5% of all reviews — the heaviest in the batch.

| Window | Reviews | ≤2★ |
|---|---|---|
| Last 90 days | 4 | 0 |
| Last 180 days | 16 | 2 |
| Most recent review | 2026-07-07 (0.8 months ago) | — |

**Negatives: 20 of 120 sampled (16.7%) — highest in the batch. Owner reply rate: 80% (16 of 20).**

An important nuance: review velocity here is *slow* (only 4 reviews in 90 days versus Feather Touch's 78), and most negative volume is older than the 180-day window. The clinic engages well with criticism — 80% reply rate is genuinely good — but the underlying complaints are strikingly consistent.

Quoted negatives (minimized):
- *2026-02-26, no reply* — alleges a paid laser-removal course was "a total waste of money and time," with a **3-month scheduling delay caused by a broken machine**, then further delays.
- *2026-02-12, no reply* — alleges "zero results, zero improvement," describes the clinic as "a complete scam."
- *2025-11-27, no reply* — "staff is friendly but doctor is too rude."
- *2024-11-03, no reply* — alleges a promised outcome from a 6-session PRP/GFC hair course did not materialize; reports ₹40,000+ spent with no visible growth.

**Recurring complaint shape — the clearest in this batch.** At least four independent reviewers, across two years and in their own words, describe the same thing: *paid upfront for a multi-session package, received no measurable result, and nobody tracked or owned the outcome.* This is not a first-response problem. It is a post-sale follow-through problem.

**Fake-review check:** the distribution is polarized (104 five-star against 23 one-star with almost nothing at 2★) which is typical of genuine service businesses with inconsistent delivery, not of bulk-purchased reviews. Nothing suggests manipulation.

#### Wedge routing
```
funnel_break_stage:       Reactivation
recommended_entry_sku:    Dead-lead reactivation — PROVISIONAL
confirm_via_mystery_shop: Basis is active Meta ads plus the batch's highest negative
                          rate with a strongly repeated "paid, no result" pattern.
                          Note the alternative reading: the complaints describe
                          quote/package follow-through failure more than lead-response
                          failure. If the mystery shop finds a slow first response,
                          Dead-lead reactivation holds. If the first response is fast
                          but package outcomes go untracked, redirect to
                          "Quote-decay follow-up" (§3).
status:                   Qualified
unverified_fields:        operator/founder identity (none found); @ai.shikro role;
                          Google Ads status; Bellamente Cosmetica Berlin affiliation;
                          aggregator paid listing
```

---

### 6.3 Sparha Advanced Aesthetic Studio

**Locality:** Metro Pillar 55, 842/A, 100 Feet Rd, opposite Dominos, Indira Nagar 1st Stage, H Colony, Indiranagar, Bengaluru 560038
**Category:** Skin care clinic — skin, hair, body, and surgical aesthetics
**Depth mode:** Standard

> **Name correction:** your list spelled this "Sparsha." The business's actual name, per both its Instagram handle and its Google Business Profile, is **"Sparha"** — no second "s". Worth getting right in any outreach.

#### Basic info
| Field | Value |
|---|---|
| Phone | +91 99727 19303 (GBP primary) · +919740354950 (secondary, from contact enrichment) |
| Email | info.sparha@gmail.com |
| Website | sparha.in (live, crawled) |
| Instagram | **two accounts** — @sparha.aesthetic.studio (the handle you supplied: 217 followers, 50 posts) and @sparha_aesthetic_studio (the larger primary account, surfaced via GBP) |
| Facebook | facebook.com/SparhaClinic |
| LinkedIn (company) | linkedin.com/company/sparha |
| YouTube | @sparha_aesthetic_studio |
| Established | **2014** (stated on own website) |

#### Identity resolution — a flag that resolved benignly
The handle supplied has only 217 followers and 50 posts, which sat oddly against a bio claiming "20+ years experience" and "Multi-Awarded Aesthetic & Plastic Surgery Brand." That mismatch was checked rather than assumed away. **It resolved cleanly:** GBP confirms 352 genuine Google reviews, a 2014 founding date, a company LinkedIn page, and a second larger Instagram account. The handle you were given simply isn't this business's primary social presence. The underlying business is real, established, and substantial.

#### Disqualification screen
No hard kills — 12 years operating, full channel presence. **Qualified**, with escalation flags recorded below.

#### Contacts
| Name | Role | Source | Confidence |
|---|---|---|---|
| **Arti Singh** | Founder (2014) | sparha.in — "Established by Arti Singh in 2014" | **confirmed as founder** |

**Credential discrepancy, unresolved and worth your attention.** The website credits her purely as "Arti Singh" — no "Dr." title, no degree, no medical qualification listed anywhere on the site. Independently, a negative Google review refers to "Dr. Arti" in the context of overseeing procedures. These two things cannot both be casually true. **Confirm whether she holds a medical qualification before any outreach addresses her as "Dr."** — getting this wrong in a first message would be a costly, and entirely avoidable, error.

#### Ads
- **Meta Ads Library:** **active** — 3 ads confirmed via the clinic's own Facebook page (`facebook.com/SparhaClinic`), an exact match rather than a keyword guess.
- **Google Ads Transparency:** undetermined (§10).
- **Aggregator:** undetermined, not checked.

#### Reviews analysis
**4.2★ · 352 reviews total · 120 newest read in full**

Distribution (all-time): 258×5★ · 21×4★ · 7×3★ · 3×2★ · **63×1★** (~18% — second-heaviest 1★ share in the batch)

| Window | Reviews | ≤2★ |
|---|---|---|
| Last 90 days | 10 | 2 |
| Last 180 days | 15 | 2 |
| Most recent review | 2026-07-24 (0.3 months ago) | — |

**Negatives: 9 of 120 sampled (7.5%). Owner reply rate: 89% (8 of 9) — genuinely high engagement.**

#### Escalation-grade allegations — surfaced, not smoothed

Two of these go beyond ordinary service complaints. They are reproduced as allegations, because that is what they are — unverified statements by reviewers — but they are not buried, because the audit standard requires exactly the opposite.

- *2025-12-06, **no owner reply*** — alleges under-eye filler injections were administered with **no doctor present and no medical staff explaining the procedure**, and disputes that the volume of filler charged for was actually administered. An unsupervised injectable-procedure allegation is a patient-safety claim, not a customer-service claim.
- *2025-10-26, owner replied* — alleges the clinic used **the reviewer's own video on Instagram without their approval**, in the reviewer's words: *"using a video of me on Instagram that I never approved."* This is a consent and likeness-use allegation.
- *2026-06-26, owner replied* — alleges that after a **₹2,00,000** payment, support quality "dropped exponentially," and that defective goods were supplied (subsequently replaced), with staff shifting blame between themselves.
- *2026-05-17, owner replied* — describes a **15-month package** purchased on the strength of earlier good service, which the reviewer alleges was then not honoured.

**Recurring complaint shape:** high-ticket commitments (₹1L–2L range) where service quality allegedly declined *after* payment cleared. Three of the four quoted reviews are independent expressions of this same pattern.

**Weighing it honestly:** an 89% owner-reply rate shows the clinic actively monitors and answers criticism, which is a real point in its favour and partially mitigates the picture. It does not neutralise the substance of the unsupervised-injectable or unconsented-media claims, which are qualitatively different from "we waited too long."

Under the project's escalation rule, this clinic hits **one** of the three flag criteria (multiple independent reviews alleging harm or improper practice). It does *not* hit the other two — ad volume is normal for the batch, and the founder is clearly connected to the business. One criterion alone earns a clear caveat, not a "do not pursue." That is the call recorded here.

#### Wedge routing
```
funnel_break_stage:       Quote Chase
recommended_entry_sku:    Quote-decay follow-up — PROVISIONAL
confirm_via_mystery_shop: Basis is a recurring pattern of ₹1L+ package commitments
                          where support allegedly declined post-payment. Test #3
                          (quote decay) is the direct probe: request a price on a
                          high-ticket procedure, then go quiet, and see whether anyone
                          chases. Two items warrant your awareness independent of the
                          wedge: the injectable-without-doctor allegation and the
                          unconsented-media allegation. Also resolve Arti Singh's
                          credential before any personalized outreach.
status:                   Qualified — escalation-grade allegations present (1 of 3
                          project flag criteria met; caveat, not a kill)
unverified_fields:        Arti Singh's medical credentials; personal LinkedIn;
                          Google Ads status; aggregator paid listing
```

---

### 6.4 SkinFit Wellness

**Locality:** 3rd floor, 534/A, 7th Cross Rd, 8th Block / 4th Block, Koramangala, Bengaluru 560034
**Category:** Skin care clinic — positions as "India's first AI-driven cosmetology & wellness clinic"
**Depth mode:** Standard

#### Basic info
| Field | Value |
|---|---|
| Phone | +91 91879 67633 |
| Email | info@skinfitwellness.in |
| Website (per GBP) | skinfitwellness.in (live, crawled) |
| Website (per Instagram bio link) | **skinnfit.in** — a *different* domain. See below. |
| Instagram | @skinfitwellness.in — 1,605 followers, 243 posts |

#### Identity resolution — a correction to an earlier conclusion in this batch

This one changed twice, and the final answer is "unresolved, leaning connected." The reasoning is laid out in full because the conclusion is genuinely uncertain and you should be able to judge it yourself.

The Instagram bio claims two locations: *"Koramangala | Richmond Road."* A targeted GBP search for a Richmond Road location returned **no distinct listing** — it resolved back to the same Koramangala profile. Separately, the search surfaced a similarly-named business: **"Skinnfit Medspa"** (double-n), operating out of an Aster Clinic in J.P. Nagar, with its own domain `skinnfit.in`, its own phone, and 13 reviews.

**My first conclusion was that these were unrelated businesses** — a same-name-different-entity collision, based on the different spelling and different domain.

**That conclusion was wrong, and I reversed it.** Two independent pieces of evidence point to a real connection:

1. **SkinFit Wellness's own Instagram bio links to `skinnfit.in`** — the *other* business's domain. This is a clinic-authored link, not an outside inference.
2. **A 2023 Skinnfit Medspa review references "Dr. Ruby" by name** as the person escalated to — the same founder name as SkinFit Wellness.

**Current best read:** Skinnfit Medspa is most likely an earlier, related, or affiliated venture of the same founder rather than an unrelated namesake. It is **not** confirmed as SkinFit Wellness's "Richmond Road" branch — the addresses don't match (J.P. Nagar ≠ Richmond Road), and the GBP website fields differ. The relationship is real but its exact nature is **unresolved**.

**Consequence:** the claimed Richmond Road second location remains **unconfirmed** — treat SkinFit Wellness as single-location until you know otherwise.

**One further item, disclosed for completeness:** the single negative review on the Skinnfit Medspa listing (2023, no owner reply) alleges non-payment to a service provider and names a staff member, stating the matter was raised with "Dr. Ruby" without resolution. This is a **B2B payment dispute allegation, unverified, from a single reviewer three years ago**, on a 13-review listing whose relationship to the target clinic is itself unconfirmed. It carries very little weight and should not drive any decision — it is recorded only because selectively omitting an inconvenient finding would corrupt the audit.

#### Disqualification screen
No hard kills. **Qualified.**

#### Contacts
| Name | Role | Source | Confidence |
|---|---|---|---|
| **Dr. Ruby Sachdev** | Founder | skinfitwellness.in/about-us — full founder narrative on the clinic's own site | **confirmed** |

Her documented background, from the clinic's own about page: Resident Doctor at Deen Dayal Upadhyay Hospital, Delhi → joined VLCC as Regional Dermatologist for South India → 18 years there, rising to Head of Aesthetic Operations, with the site claiming oversight of 100,000+ treatments → conducted a skincare masterclass for Femina Miss India 2020 state finalists → awarded **'Best Aesthetic Professional', Times Health Awards 2023** → founded SkinFit Wellness. The site states every clinician is trained directly by her.

This is the most substantively documented founder in the batch. All of it is self-reported on the clinic's own site and none of it was independently verified, but it is specific, checkable, and internally consistent.

LinkedIn: **not attempted** — the actor cap was hit before her query could run. She is the single highest-value LinkedIn target in this batch when the cap resets.

#### Ads
- **Meta Ads Library:** **inconclusive.** The keyword sweep returned 11 results, none belonging to this clinic (all unrelated brands — HyugaLife, Home Essentials, Dr. Su Formulations, and similar). No Facebook page URL was found via GBP to check directly. **This is not evidence of "no Meta ads"** — it is an unanswered question.
- **Google Ads Transparency:** undetermined (§10).
- **Aggregator:** undetermined, not checked.

#### Reviews analysis — the clearest standalone finding in the batch
**4.9★ · 120 reviews · full history read**

Distribution (all-time): 116×5★ · 1×4★ · 0×3★ · 1×2★ · 2×1★

| Window | Reviews | ≤2★ |
|---|---|---|
| Last 90 days | **0** | 0 |
| Last 180 days | **0** | 0 |
| Most recent review | **2025-09-17 — 10.4 months ago** | — |

**Negatives: 3 all-time. Owner reply rate: 0% — none of the three were ever answered.**

This is the inverse of every other clinic in this batch. Everywhere else, reviews are arriving continuously and the analysis question is *what do the recent ones say*. Here, **nothing has arrived in nearly a year** despite a strong 4.9★ historical rating.

The audit standard is explicit that this stall is itself the finding — reporting "no recent complaints" as though it were health would be exactly backwards. A clinic with a genuinely satisfied recent patient base and a functioning ask-for-review habit does not go 10 months in silence. Either the review-collection habit died, or patient volume did, or the person who owned that process left. All three are worth knowing, and all three are sellable.

Quoted negative:
- *2025-09-01, **no owner reply*** — alleges unprofessional handling of a rescheduled appointment: booked with Dr. Ruby, forced to reschedule, arrived on time for the rebooked slot, waited, completed a form, then experienced further friction. Notably the reviewer states they had **not yet met the doctor** — the failure was entirely front-desk/booking-layer.

The remaining two negatives (2025-02, 2024-01) have no text.

**Fake-review check:** the 116/1/0/1/2 distribution is unusually top-heavy, but with all reviews historical rather than recently bulk-added, there is no burst pattern to suggest manipulation. The concern here is dormancy, not authenticity.

#### Wedge routing
```
funnel_break_stage:       Reviews
recommended_entry_sku:    Review reactivation agent — PROVISIONAL
confirm_via_mystery_shop: The "reviews stalled ~10 months ago" diagnosis is directly
                          observed from data rather than inferred — this is the
                          highest-confidence non-mystery-shop finding in the batch.
                          What the shop should establish is WHY: front-desk turnover,
                          a dropped post-visit ask, or a genuine drop in patient
                          volume. That determines whether review reactivation alone is
                          the right entry or whether a broader post-consult follow-up
                          gap sits underneath it. The one substantive negative is a
                          pure booking-layer failure, which hints at the latter.
status:                   Qualified
unverified_fields:        Meta ads (inconclusive, no FB page found); Google Ads;
                          whether a genuine Richmond Road location exists; the exact
                          relationship between SkinFit Wellness and Skinnfit Medspa;
                          Dr. Ruby Sachdev's LinkedIn; aggregator paid listing
```

---

### 6.5 Skin and Recon

**Locality:** 255, 1st Floor, 36th Cross, 5th Main Rd, 4th Block, Jayanagar, Bengaluru 560011
**Category:** Dermatologist + Plastic Surgery clinic
**Legal name (from the Google Ads advertiser record):** SKIN AND RECON DERMATOLOGY AND PLASTIC SURGERY CLINIC
**Depth mode:** Standard

#### Basic info
| Field | Value |
|---|---|
| Phone | +91 63614 17399 |
| Email | skinandrecon@gmail.com |
| Website | skinandrecon.in (live, crawled) |
| Instagram | @skinandrecon — 396 followers, 182 posts |
| Facebook | facebook.com/skinandrecon |

**A useful catch on data quality:** this clinic's Instagram bio "website" field is not a website at all — it's a Google Maps short link. The real website (`skinandrecon.in`) surfaced only through the GBP contact enrichment. Had the audit relied on the Instagram field alone, it would have concluded the clinic has no website. This is precisely why the GBP pull and the website crawl are both run rather than treating one as a substitute for the other.

#### Disqualification screen
No hard kills. Review history runs back to at least 2024; two named, individually credentialed clinical leads; not a committee structure. **Qualified.**

#### Contacts
| Name | Role | Source | Confidence |
|---|---|---|---|
| **Dr. Shruthi Chikkaiah** | **Chief Dermatologist** — MBBS, MD (Dermatology), FRGUHS (Dermatosurgery). 10+ years. Graduated, completed masters and fellowship at Bangalore Medical College. Trained in hair transplant surgery in India and abroad. Medical educator. | skinandrecon.in/about — explicitly titled "Chief dermatologist at Skin & Recon clinic" | **confirmed** |
| **Dr. Rakesh Koudki** | Plastic Surgeon — MBBS, MS, MCH (Plastic Surgery), FACS. Double board certified, 13+ years. MCH at Safdarjung Hospital Delhi; microvascular/reconstructive fellowship at TATA Memorial Mumbai; aesthetic fellowships in Istanbul and San Diego. Member ISAPS, IAAPS (life), APSI, IMA (life), KAPRAS (life). | skinandrecon.in/about — full biography on own site | **confirmed** |

This is the strongest credential documentation in the batch — full degree chains, named training institutions, and professional memberships, all published by the clinic itself. **Both contacts are unambiguously confirmed.**

Note for outreach: Dr. Shruthi's title is "Chief Dermatologist" and "Consultant Dermatologist," not "Founder." The playbook is explicit that titles should be read literally — neither person's page claims ownership. Who actually owns the business is **not established**.

#### Ads
**Google Ads Transparency — verified via direct advertiser-ID lookup** (`AR08757128262854901761`, confirmed as a real, verified advertiser this session):

10 ad creatives found. All activity clusters between **2026-03-01 and 2026-04-08**, across TEXT, IMAGE, and VIDEO formats, with individual ads sustained 12–22 days.

**Every single one stopped by 2026-04-08 — roughly four months ago.** This clinic ran a concentrated ~5-6 week Google Ads push through Q1 2026 and then went completely dark.

**Meta Ads Library:** **none found** — checked directly against the clinic's own Facebook page rather than by keyword (the keyword sweep for "Skin and Recon" returned pure noise: drama-app and streaming-service advertisers). No active Meta ads on that page.

**Aggregator:** undetermined, not checked.

#### Lead capture infrastructure
The website runs a **Collectchat** interactive form widget — a third-party conversational lead-capture tool. This is a genuinely useful signal: someone at this clinic has previously invested in formalising enquiry capture. There is existing infrastructure to build on, which the playbook treats as a positive rather than a disqualifier.

#### Reviews analysis
**4.9★ · 242 reviews total · 120 newest read in full**

Distribution (all-time): 232×5★ · 2×4★ · 1×3★ · 0×2★ · 7×1★

| Window | Reviews | ≤2★ |
|---|---|---|
| Last 90 days | 43 | **0** |
| Last 180 days | 57 | 1 |
| Most recent review | 2026-07-15 (0.5 months ago) | — |

**Negatives: 4 of 120 sampled (3.3%). Owner reply rate: 100% (4 of 4).**

Notably, reviews have kept arriving at a healthy clip (43 in 90 days) *despite* the ad spend stopping four months ago — organic demand is clearly still functioning.

Quoted negatives (minimized):
- *2026-03-04, owner replied* — alleges a prescribed serum and gel combination worsened a skin allergy after two days of use, following a long journey to reach the clinic.
- *2025-02-24, owner replied* — alleges being billed ₹4,000–5,000 for "unnecessary tablets and lotions" for a minor skin patch.
- *2024-09-23, owner replied* — reports a 20-minute wait and a good consultation, but alleges a ₹8,000+ product bill plus ₹700 per-person consultation fee felt disproportionate.

**Recurring complaint shape:** the theme is *product-cost versus value delivered* — patients feeling over-prescribed or overcharged for take-home products. It is **not** a scheduling, responsiveness, ghosting, or booking-friction complaint. That distinction matters: this is a treatment-value perception issue, which sits outside the funnel-automation product.

**Fake-review check:** a 3.3% negative rate with a **100% owner reply rate** is a genuine positive signal. Per the audit standard, well-answered negatives *raise* confidence in a review corpus rather than lowering it.

#### Wedge routing
```
funnel_break_stage:       Reactivation
recommended_entry_sku:    Dead-lead reactivation — PROVISIONAL (weak basis, stated
                          plainly)
confirm_via_mystery_shop: This is the most ambiguous wedge call in the batch and
                          should be treated as such. Ads stopped ~4 months ago;
                          reviews, reply behaviour, and credentials all look genuinely
                          healthy; the complaint pattern points at pricing perception,
                          not funnel mechanics. The data does not clearly show an
                          active funnel break today. Shop it to test two things:
                          (1) is there an un-worked backlog from the Q1 2026 ad push,
                          and (2) current response speed on a fresh enquiry. If the
                          response is fast and no backlog exists, record this as a
                          "None (pass)" candidate rather than forcing a wedge onto it.
status:                   Qualified
unverified_fields:        aggregator paid listing; LinkedIn (both doctors); who
                          actually owns the business; why ad spend stopped in April
```

---

### 6.6 Advanced GroHair GloSkin — Jayanagar branch

**Locality:** 539, 2nd Floor, 10th Main Rd, above Heads Up For Tails, 5th Block, Jayanagar, Bengaluru 560041
**Category:** Hair transplantation clinic
**Depth mode:** Standard
**Scope note:** your list named the Jayanagar branch specifically, so that is what was audited. This is one branch of a substantial multi-city chain.

#### Basic info
| Field | Value |
|---|---|
| Phone | +91 89402 56789 |
| Email | jayanagar@adgrohair.com |
| Website | advancedgrohair.in/jayanagar/hair-skin/ (branch page on the chain domain) |
| Instagram | @adgloskinclinicjayanagar — 1,418 followers, 209 posts |
| Sister account | @adgrohairclinicjayanagar (hair-specific, linked from the bio) |
| Bio link | adgloskin.com |

The branch operates a **split-brand structure**: "GloSkin" for skin, "GroHair" for hair, each with its own Instagram account and its own email subdomain convention. Any outreach should be clear about which side of the business it addresses.

#### Chain context
The Meta ads sweep incidentally mapped the chain's footprint — near-identical page names exist for **Rajahmundry, Erode, Sivakasi, Trichy, Ramanathapuram, Electronic City, Potheri, HSR Layout, Rajajinagar**, and Jayanagar. This is a multi-state operation, not a local independent.

**Implication for qualification:** a chain of this size raises a legitimate question about hard kill #5 (committee/multi-partner sign-off, no single decision-maker). **This was not resolved.** No ownership or franchise structure was established. If decisions at this branch require chain-level sign-off, this lead may be disqualifiable — worth establishing early rather than deep into a sales cycle.

**Prior-batch context, explicitly not re-verified:** the handoff file notes that two other branches of this chain were previously found to have a cross-branch pattern of patients being consulted by technicians rather than doctors. That finding was **not re-checked this session** and is reproduced here only as something to watch for, not as an established fact about Jayanagar.

#### Disqualification screen
No hard kills confirmed. **Qualified**, with the #5 question flagged above as genuinely open.

#### Contacts
| Name | Role | Source | Confidence |
|---|---|---|---|
| "Karthik" | Branch manager | Named in a 2024 negative Google review | **weak** |
| Branch line | +91 89402 56789 · jayanagar@adgrohair.com | GBP | confirmed |

**No doctor, owner, or verified staff member was identified for this branch.** "Karthik" is a name-match from a patient complaint, with no website bio or staff directory to corroborate it, and it comes attached to a criticism — using it in outreach would be both unreliable and tactless. It is recorded at `weak` for completeness only.

#### Ads
- **Meta Ads Library:** **active** — the chain runs a network of per-city pages, and "Advanced Gloskin Clinic Jayanagar" specifically appeared among 15 active results.
- **Google Ads Transparency:** undetermined (§10).
- **Aggregator:** undetermined, not checked.

#### Reviews analysis
**4.7★ · 119 reviews · full history read**

Distribution (all-time): 105×5★ · 7×4★ · 1×3★ · 1×2★ · 5×1★

| Window | Reviews | ≤2★ |
|---|---|---|
| Last 90 days | 24 | 0 |
| Last 180 days | 37 | 3 |
| Most recent review | 2026-07-30 (0.1 months ago) | — |

**Negatives: 6 of 119 (5%). Owner reply rate: 50% (3 of 6) — inconsistent.**

Quoted negatives (minimized):
- *2026-03-27, **no owner reply***, in Hindi — alleges payment was taken but treatment was not completed: the clinic stopped the course after only 3 sittings and told the patient not to return. (*"paise bhi le liye treatment bhi pura nahi diya 3 sitting ke baad hi mana kar diya ki aap ab mat aana"*)
- *2026-03-24, **no owner reply*** — "very bad product, please don't use."
- *2024-09-11, owner replied* — alleges no results and poor service, naming the branch manager as rushing consultations and prioritising revenue over care.

**Recurring complaint shape:** **treatment abandonment mid-course.** Two independent reviewers describe multi-session treatment plans that simply stopped, with no follow-up, no recovery attempt, and no chase from the clinic. This is the sharpest signal in this branch's data, and it maps cleanly onto a follow-up/persistence gap rather than a first-response gap.

The 50% reply rate reinforces it — both 2026 negatives went unanswered while the older 2024 one was addressed, suggesting review monitoring has itself lapsed recently.

#### Wedge routing
```
funnel_break_stage:       Follow-up Persistence
recommended_entry_sku:    Follow-up and nurture engine — PROVISIONAL
confirm_via_mystery_shop: Basis is two independent reviews describing multi-session
                          treatments abandoned without the clinic chasing the patient
                          to continue or resolve. Probe with SOP test #2 (persistence:
                          reply, then go silent, count follow-ups over 7-14 days) and
                          test #3 (quote decay). If nobody chases a lapsed package,
                          this wedge holds. Separately and early: establish whether
                          this branch can make its own decisions or needs chain-level
                          sign-off — hard kill #5 is genuinely open here.
status:                   Qualified — decision-authority question unresolved
unverified_fields:        doctor/owner identity; branch vs. chain decision authority;
                          whether the prior batch's technician-not-doctor pattern
                          applies here; Google Ads status; aggregator paid listing
```

---

### 6.7 Koza Aesthetic Care — 5-branch chain

**Brand:** Koza Aesthetic Care — "Providing World Class Treatment since 2021" (own website)
**Depth mode:** **Deep** — escalated mid-batch when the chain structure was confirmed
**Shared phone across all branches:** +91 96060 09079

#### Basic info
| Field | Value |
|---|---|
| Website | kozacare.org (live, crawled) |
| Instagram | @koza.aesthetic.care — **12,252 followers**, 488 posts |
| Bio link | linktr.ee/KozaAestheticCare |
| Branches claimed in bio | 6 — Banashankari, Ecity, Jayanagar, Arekere, HRBR Layout, Sarjapur |
| Branches confirmed via GBP | **5 of 6** |

#### Branch reconciliation
| Branch | GBP listing | Address |
|---|---|---|
| Arekere | ✅ found | 3rd floor, Sharada Arcade, Bannerghatta Rd, above Yamaha showroom, Omkar Nagar, 560076 |
| Sarjapur Road | ✅ found | No 514, 1, 2-3, Sarjapur Main Rd, opp. More Mall, Kaikondrahalli, 560035 |
| HRBR Layout / Kalyan Nagar | ✅ found | 914, 5th A Cross Rd, **inside Motherhood Hospital**, HRBR Layout 1st Block, 560043 |
| Banashankari | ✅ found | 4, 30th Main Rd, opp. Kempegowda Institute of Medical Science, Banashankari 3rd Stage, 560085 |
| Jaya Nagar | ✅ found | Ground Floor, 35/20, 11th Main Rd, Vishya Bank Colony, 5th Block, Jayanagar, 560041 |
| **Electronic City** | ❌ **not found** | A targeted GBP search resolved back to the Jaya Nagar listing. Either it has no standalone Google Business Profile, or it is not discoverable that way, or the bio is stale. **Marked undetermined — not assumed absent.** |

The HRBR branch operating *inside Motherhood Hospital* is worth noting — a host-facility arrangement may carry different decision-making and lead-flow dynamics than a standalone unit.

*(A "KOJA" cosmetics store in New Delhi also appeared in results. Different business entirely, discarded as search noise.)*

#### Disqualification screen
No hard kills confirmed — website + Instagram + GBP all present, operating since 2021. **Qualified.**

However: a 5-6 branch chain with **no identifiable owner** raises the same hard-kill #5 question as Advanced GroHair. It was not resolved.

#### Contacts
| Name | Role | Source | Confidence |
|---|---|---|---|
| — | **No named founder, doctor, or manager found anywhere** | website + Instagram + GBP all checked | **none found** |
| Shared switchboard | +91 96060 09079 (identical across every branch) | GBP | confirmed |

**This is a real and consequential gap.** The website is entirely templated — stock "Professionally Certified Team," "FDA Approved Technology," "Highly Standardized Protocols" copy, with **no team page, no doctor bios, and no named individuals of any kind.** For a business running 12,252 Instagram followers, ads on two platforms, and 5+ locations, the total absence of a named human is itself informative: either deliberately corporate-anonymous, or genuinely operator-run without a clinical figurehead.

A single switchboard number shared across all five branches also means every branch's leads funnel through one contact point — relevant to where a response-speed failure would occur.

**Not yet attempted:** `harvestapi/linkedin-company-employees` was never run for this clinic. It was not blocked by the free-tier cap (that cap applies to the *profile-search* actor) — it simply wasn't reached within this session's time budget. **This is the single most promising unexplored contact route in the batch** and should be the first action if Koza is prioritised.

#### Ads
- **Meta Ads Library:** **active** — 7 ads under an exact "Koza Aesthetic Care" page-name match, all currently running.
- **Google Ads Transparency:** **active** — 1 ad, advertiser ID `AR01656777896355692545`. This is the **only** clinic whose Google Ads presence was confirmed through the brand-name query path (which failed for everyone else), so it is corroborated by an ID.
- **Aggregator:** undetermined, not checked.

#### Reviews analysis — per branch

| Branch | Rating | Reviews | Most recent | Gap | Negatives | Reply rate |
|---|---|---|---|---|---|---|
| Arekere | 5.0★ | 2 | 2024-12-15 | **19.5 mo** | 0 | n/a |
| Sarjapur Road | — | 0 | — | — | — | n/a |
| HRBR / Kalyan Nagar | 4.6★ | 9 | 2026-05-07 | 2.8 mo | 1 | **0%** |
| Banashankari | 5.0★ | 20 | 2025-09-27 | **10.1 mo** | 0 | n/a |
| **Jaya Nagar** | **3.8★** | **44** | 2026-08-01 (today) | 0.0 mo | **12 (27%)** | **8%** |

**Jaya Nagar is the problem branch, and it is also the only branch with enough current volume to read.**

Distribution at Jaya Nagar: 29×5★ · 2×4★ · 1×3★ · 0×2★ · **12×1★**

Quoted negatives (minimized):
- *2026-08-01 — posted the day of research, **no owner reply*** — "Worst experience. Don't expect the results here, worst staff behaviour. We have been coming here from last 3 months and 3rd session no results at all... Only money minded people."
- *2026-06-11, **no owner reply*** — alleges staff "are dishonest and misleading. They tell patients one thing but do something else," singling out the receptionist as "very unprofessional and unhelpful."
- *2026-01-01, **no owner reply*** — "really worst experience in my life, they just money minded people."

**Recurring complaint shape:** no-results-after-paid-sessions, compounded by **near-total owner silence** — 11 of 12 negatives were never answered. The receptionist/front-desk criticism connects directly to the shared-switchboard structure noted above.

**On the other four branches — read carefully.** Their clean ratings are **thin or stale data, not evidence of health**:
- Arekere: 2 reviews, nothing in 19.5 months
- Banashankari: 20 reviews, nothing in 10.1 months
- HRBR: 9 reviews, its single negative unanswered
- Sarjapur Road: zero reviews, no rating at all

Four of five branches have effectively stopped generating reviews while the chain actively spends on ads. That is its own finding.

**Fake-review check:** Jaya Nagar's negative volume and complaint diversity look organic. The other branches' prolonged silence suggests a review-collection process that either never existed or has lapsed chain-wide.

#### Wedge routing
```
funnel_break_stage:       Reactivation
recommended_entry_sku:    Dead-lead reactivation — PROVISIONAL
confirm_via_mystery_shop: Shop the Jaya Nagar branch specifically — it is the only one
                          with current, readable signal, and its 8% negative-reply
                          rate plus "no results after 3 sessions" pattern also points
                          toward a Reviews / post-consult problem, not purely a
                          lead-response one. If the shop finds slow or no response,
                          Dead-lead reactivation holds. If response is fast but
                          follow-through fails, redirect to "Follow-up and nurture
                          engine." Consider shopping one clean branch (Banashankari)
                          alongside it for contrast — the chain-wide inconsistency may
                          be the more sellable story than any single branch.
                          Also confirm whether an Electronic City branch exists.
status:                   Qualified — Jaya Nagar flagged as materially weaker than
                          its siblings
depth_mode:               Deep (escalated from Standard on confirming the chain)
unverified_fields:        founder/owner identity (none found anywhere); decision
                          authority across branches; Electronic City branch existence;
                          LinkedIn company-employees search (NOT YET RUN — best
                          remaining contact route); aggregator paid listing
```

---

### 6.8 SS Aesthetic Clinic

**Locality:** Floor 1, Building 32, above Yamaha Showroom, opposite Filter Coffee, HAL 3rd Stage, Indiranagar (New Thippasandra), Bengaluru 560075
**Category:** Skin care clinic
**Depth mode:** Standard

#### Basic info
| Field | Value |
|---|---|
| Phone | +91 91132 76518 |
| Email | ssaesthetics0825@gmail.com |
| Website | ssaesthetics.in (live, crawled) |
| Instagram | @ss_aesthetics_indiranagar — 471 followers, 161 posts |
| Facebook | facebook.com/profile.php?id=61583357924707 |
| YouTube | channel present |

The email address (`ssaesthetics0825@gmail.com`) is a Gmail account with what looks like a date stamp — a small signal that this may be a relatively young operation, or at least one without formalised business email. Combined with the newly-created Facebook page ID, this clinic looks **recently established**, though not recently enough to trip the 12-month hard kill (see below).

#### Disqualification screen
- **Hard kill #2 (operating under 12 months)** — checked carefully given the signals above. The review history runs to 38 reviews within the last 180 days out of 43 total, which *could* indicate a young business. However, the oldest reviews predate the 180-day window, and nothing establishes a founding date under 12 months. **Not triggered, but this is the one clinic in the batch where it is worth a second look during the mystery shop.** If it turns out to be under a year old, it becomes a hard kill.
- No other hard kills. **Qualified.**

#### Contacts
| Name | Role | Source | Confidence |
|---|---|---|---|
| **Mrs. Shylaja B.S.** | **Founder** | ssaesthetics.in — "Our founder Mrs. Shylaja B.S." | **confirmed** |
| **Mrs. Suchitra B.S.** | **Co-founder** | ssaesthetics.in — "co-founder Mrs. Suchitra B.S." | **confirmed** |
| Dr. Jabin | Clinic cosmetologist | ssaesthetics.in — "Dr. Jabin, our clinic cosmetologist" | **likely** (named once, no bio or credentials given) |

**A positional note worth registering.** The website leads with *"every treatment is doctor-led and clinically supervised — not just technician-driven"* — yet the two named founders carry "Mrs." rather than a medical title, and the only clinical person named is a single cosmetologist mentioned in passing. This is not a disqualifier and the playbook does not penalise non-physician ownership. But the gap between the "doctor-led" positioning and the named team is worth being aware of, particularly given that a competitor in this same batch (Advanced GroHair) has been criticised by patients for exactly this technician-versus-doctor issue.

Two confirmed, named, non-clinical **owners** is actually a strong access position — these are decision-makers, not gatekeepers.

#### Ads
- **Meta Ads Library:** **active, and very current** — 6 ads confirmed via the clinic's own Facebook page. Start dates of **2026-07-31 and 2026-08-01**, i.e. ads launched the day before and the day of research. This clinic is actively spending right now.
- **Google Ads Transparency:** undetermined (§10).
- **Aggregator:** undetermined, not checked.

#### Reviews analysis
**5.0★ · 43 reviews · full history read**

Distribution (all-time): 42×5★ · 1×4★ · **0×3★ · 0×2★ · 0×1★**

| Window | Reviews | ≤2★ |
|---|---|---|
| Last 90 days | 13 | 0 |
| Last 180 days | 38 | 0 |
| Most recent review | 2026-07-31 (essentially today) | — |

**Negatives: zero. There is nothing to analyse.**

**Fake-review sanity check — flagged, deliberately, in both directions.** A perfect 5.0★ across 43 reviews with not a single critical review, on a clinic *actively running paid acquisition*, is an unusually clean pattern. Paid traffic normally brings at least some mismatched expectations. Two honest readings:

1. It is a genuinely new, small, well-run clinic whose early patients are happy — entirely plausible, and consistent with the young-business signals above.
2. The review corpus has been curated or solicited selectively.

**Nothing in the review text itself reads as templated or bulk-generated**, and there is no burst pattern. The evidence does not support an accusation. It is flagged so the observation is on record, not smoothed away — and so that the mystery shop treats the "flawless reputation" with appropriate scepticism, exactly as the playbook's "strong surface reputation is not a disqualifier — the mystery shop decides" rule requires.

#### Wedge routing
```
funnel_break_stage:       Reactivation
recommended_entry_sku:    Dead-lead reactivation — PROVISIONAL (weak basis, stated
                          plainly)
confirm_via_mystery_shop: There is NO review-based evidence of a funnel break at this
                          clinic. The wedge assignment rests entirely on "active ads +
                          unknown response speed" being the highest-priority default
                          row in §3. The mystery shop is doing all the diagnostic work
                          here. Two things to establish: (1) response speed and
                          qualification depth on a fresh enquiry, and (2) how long the
                          clinic has actually been operating — if under 12 months, this
                          becomes hard kill #2 and the lead should be dropped.
                          Access is a genuine strength: two named, confirmed owners.
status:                   Qualified
unverified_fields:        Google Ads status; aggregator paid listing; LinkedIn for
                          both founders; Dr. Jabin's credentials; exact founding date
                          (relevant to hard kill #2)
```

---

### 6.9 Rua Skin & Hair Center — 2 branches

**Category:** Dermatologist — Dermatology, Cosmetology, Lasers, Hair Transplants
**Depth mode:** Standard
**Positioning:** "3 Expert Dermatologists | Doctor-Led"

#### Basic info
| Field | Value |
|---|---|
| Website | ruaskinandhair.com (live, crawled) |
| Instagram | @ruaskinandhair — 1,259 followers, 265 posts |
| Facebook | facebook.com/profile.php?id=61581739901248 |
| YouTube | @RUASkinandhair |
| Instagram display name | "RUA Skin & Hair Center \| Dr. Jeevith\| Dr. Eshritha\| Dr. Jatin\|" |

#### Branches — both confirmed
| Branch | Address | Phone |
|---|---|---|
| **Ramamurthy Nagar** | 2nd Floor, No 14, TC Palya Main Rd, above Burger King, 1st Block, Akshaya Nagar, Bengaluru 560016 | +91 99597 63678 |
| **Indiranagar** | Building 1060/1050, Jeevan Bima Nagar, 3rd Stage Cross Road, next to National Centre For Excellence, Puttappa Layout, Bengaluru 560075 | +91 70199 76689 |

The Indiranagar branch was **missed by the initial GBP run** and recovered by a targeted follow-up search — caught by the coverage check in the verification loop. Both branches share the same website, Instagram, and Facebook presence, confirming they are one business rather than a name collision.

*(A "REGROW HAIR AND SKIN" clinic in Ramamurthy Nagar also appeared in results — unrelated business, discarded as noise.)*

#### Disqualification screen
No hard kills. Website + Instagram + GBP all present; ~97 combined reviews across two branches with history extending beyond 12 months. Three practising doctors rather than a single mega-founder or a corporate committee. No park signals. **Qualified.**

#### Contacts
| Name | Role | Source | Confidence |
|---|---|---|---|
| **Dr. Eshritha** | Dermatologist — patient testimonials reference vitiligo surgery and general dermatology | ruaskinandhair.com testimonials | **likely** |
| **Dr. Jatin** | Dermatologist | ruaskinandhair.com testimonials | **likely** |
| **Dr. Jeevith** | Dermatologist | Instagram bio and GBP title only | **weak** |
| Branch lines | +91 99597 63678 (Ramamurthy Nagar) · +91 70199 76689 (Indiranagar) | GBP | confirmed |

**Why "likely" and not "confirmed":** the website's crawled content names Dr. Eshritha and Dr. Jatin repeatedly and substantively — but inside *patient testimonials*, not in a formal team-page biography. The site has an "OUR TEAM" navigation section that the crawl did not capture as a separate page. Being named by patients on the clinic's own site is strong corroboration, but it is not the same as a clinic-authored role statement, so the label reflects that honestly.

Dr. Jeevith appears **only** in the Instagram bio and the GBP listing title — no site content captured this session names them. Hence `weak`.

**No single owner is identified.** The clinic presents as a three-doctor collective. Per the playbook's instruction to read titles literally, ownership is recorded as **collective or unclear**, not attributed to any one person.

LinkedIn: **not attempted** — actor cap exhausted.

#### Ads
- **Meta Ads Library:** **active** — 1 ad, started 2026-07-27, still running as of research day. Confirmed via the clinic's own Facebook page rather than keyword search (the keyword sweep returned heavy noise — romance-novel and AI-chat apps).
- **Google Ads Transparency:** undetermined (§10).
- **Aggregator:** undetermined, not checked.

#### Reviews analysis

**Ramamurthy Nagar — 4.9★ · 80 reviews · full history read**
Distribution: 75×5★ · 5×4★ · **0×3★ · 0×2★ · 0×1★**

| Window | Reviews | ≤2★ |
|---|---|---|
| Last 90 days | 17 | 0 |
| Last 180 days | 61 | 0 |
| Most recent review | 2026-08-01 (research day) | — |

**Indiranagar — 5.0★ · 17 reviews · full history read**
Distribution: 17×5★ · nothing else

| Window | Reviews | ≤2★ |
|---|---|---|
| Last 90 days | 10 | 0 |
| Last 180 days | 17 | 0 |
| Most recent review | 2026-07-07 (0.8 months ago) | — |

**Combined: ~97 reviews across two branches. Zero negative reviews of any kind, at either location, across the entire available history.**

**Fake-review sanity check.** This is the cleanest record in the batch and, like SS Aesthetic, unusually so. The distribution is not a pure 5★ wall — Ramamurthy Nagar has 5 genuine 4★ reviews, which is a mild point *toward* authenticity, since fabricated corpora rarely bother with 4★ entries. Review text names specific doctors and specific procedures (vitiligo surgery, skin infections) rather than generic praise, and arrival is spread continuously rather than bursty.

Still: **zero critical reviews across two branches and ~97 reviews is atypical**, and it is flagged as an observation rather than explained away. The honest reading is that the evidence points toward genuine, if selectively-solicited, satisfaction — but the mystery shop should not treat the flawless rating as proof of a functioning funnel.

#### Wedge routing
```
funnel_break_stage:       Reactivation
recommended_entry_sku:    Dead-lead reactivation — PROVISIONAL (WEAKEST BASIS IN THE
                          BATCH — flagged explicitly)
confirm_via_mystery_shop: This is the thinnest wedge call of all 10 clinics and should
                          be treated with corresponding scepticism. There is one
                          active Meta ad and zero negative signal of any kind across
                          two branches. The assignment exists because "ads✓ + unknown
                          response speed" is the §3 default, not because anything in
                          the data points to a break. The mystery shop's response-speed
                          and persistence tests determine everything here. If the reply
                          is fast and well-qualified, this is a strong "None (pass)"
                          candidate and should be recorded as such rather than pursued.
status:                   Qualified
unverified_fields:        Dr. Jeevith's role (site team page not captured); formal
                          role confirmation for Dr. Eshritha and Dr. Jatin; who owns
                          the business; LinkedIn for all three doctors; Google Ads
                          status; aggregator paid listing
```

---

### 6.10 Feather Touch Aesthetic Clinic & Academy — PARKED

**Locality:** 2nd floor, B AND A SQUARE-II, 1376, 32nd E Cross Rd, 4th T Block East, Jayanagar, Bengaluru 560041
**Branch:** Feather Touch Skin & Hair Clinic — 1st floor, 2629-2, Temple Rd, opposite VV Puram police station, Vani Vilas Mohalla, Mysuru 570002
**Category:** Skin care clinic **and training academy**
**Depth mode:** Standard (Deep recommended if pursued)
**Status: PARK — mega-founder-brand, Medium priority**

#### Basic info
| Field | Value |
|---|---|
| Instagram | @feather_touch_aesthetic_clinic — **45,037 followers, 870 posts** |
| Phones | +91 99009 83048 · 99011 32233 (main) · 99022 50038 (Mysuru) |
| External link | youtube.com/@FeatherTouchAestheticAcademy |
| Mysuru branch IG | @feathertouchclinicmysore |
| Website | **none found** |

**Scale context:** 45,037 followers is **3.7× the next-largest account in this batch** (Koza at 12,252) and roughly 36× the batch median. This is a different category of business from everything else here.

The "& Academy" in the name is significant: this is a clinic *and* a training business, and the external link points at the Academy's YouTube rather than at a clinic site. Part of the audience is aspiring practitioners, not patients — which affects how the follower number should be read.

#### Why this is parked rather than queued
The playbook's §1.2 park tier lists **"Mega founder-brand (very large personal following)"** at Medium priority, with the reasoning that these are a longer sales cycle and harder access, but strong underlying fit — approached via founder-capacity-protection framing and a nurture tier, never a cold DM.

This clinic matches that description exactly. It is **not disqualified**; it needs a different motion from the other nine.

#### Disqualification screen
- Hard kill #1 (no website **and** no Instagram **and** no GBP): **not triggered.** No website was found, but Instagram and GBP are both strong. The playbook is explicit (§1.3) that missing one channel is not a disqualifier where others exist.
- No other hard kills. **Qualified but parked.**

#### Contacts
| Name | Role | Source | Confidence |
|---|---|---|---|
| — | **No named founder or doctor identified** | GBP + Instagram bio checked; website crawl impossible (no site found) | **none found** |

**This is the most conspicuous contact gap in the batch**, precisely because of the account's scale — a 45K-follower aesthetic brand with an eponymous training academy almost certainly has a recognisable founder figure. Standard depth mode simply did not reach it: no website meant no team page to crawl, and the Instagram bio names only phone numbers and the branch account.

**The Deep-mode Instagram contact graph is the right next step** — bio links, tagged and collab accounts on posts, recurring staff names in captions, and story highlight titles are all cheap, staff-oriented routes that were not run here. If this lead is pursued, that pass comes first.

#### Ads
- **Meta Ads Library:** **inconclusive.** The keyword sweep returned a single result with no page-name match and inactive status. No Facebook page URL was discoverable via GBP to check directly. **Not evidence of "no Meta ads."**
- **Google Ads Transparency:** undetermined (§10).
- **Aggregator:** undetermined, not checked.

#### Reviews analysis

**Main clinic (Jayanagar) — 4.8★ · 803 reviews · 120 newest read in full**
Distribution (all-time): 745×5★ · 25×4★ · 1×3★ · 2×2★ · 30×1★

| Window | Reviews | ≤2★ |
|---|---|---|
| Last 90 days | **78** | 4 |
| Last 180 days | 120 | 4 |
| Most recent review | 2026-07-30 (0.1 months ago) | — |

**78 reviews in 90 days is by far the highest review velocity in the batch** — roughly 1.7× Feather Touch's nearest rival and more than 19× the slowest.

**Negatives: 4 of 120 sampled (3.3%). Owner reply rate: 100% (4 of 4).**

Quoted negatives (minimized):
- *2026-07-20, owner replied* — alleges the clinic "give[s] more importance to celebrities not to normal clients," with normal members served by "unexperienced staff" and poor communication.
- *2026-06-30, owner replied* — alleges a skin condition worsened over the course of a recommended treatment and product regimen, despite patient adherence.
- *2026-06-12, owner replied* — "really worst place, this is not a clinic only business place, all are pushing packages... high amounts and no professionally workers."
- *2026-05-09, owner replied* — alleges a treatment room had only a fan rather than air conditioning, describing the experience as uncomfortable and unhygienic.

**Recurring complaint shape — and it is the diagnostic one.** At least two independent reviewers describe a **two-tier service experience**: polished delivery for high-profile and celebrity clients, inconsistent junior-staffed delivery for everyone else. That is a textbook **founder-capacity overflow** signal. It is not a lead-response problem, not a follow-up problem, and not a reviews problem — it is what happens when demand outgrows the founder's personal availability and the brand's promise outruns what the bench can deliver.

**Mysuru branch — 5.0★ · 5 reviews.** Too thin to analyse meaningfully. Most recent 2026-07-31.

**Fake-review check:** 803 reviews with a 100% reply rate on negatives, a healthy 25-review 4★ band, and steady high-velocity arrival is a genuinely well-managed review corpus. No manipulation indicators.

#### Wedge routing
```
funnel_break_stage:       Post-consult
recommended_entry_sku:    Founder capacity protection — PROVISIONAL
                          (§3 park row, Medium priority)
confirm_via_mystery_shop: The wedge rests on a recurring "VIP versus normal client"
                          service-quality pattern from independent reviewers, which is
                          exactly the overflow signal the mega-founder-brand park route
                          anticipates. This is NOT a standard entry lead: expect a
                          longer cycle, approach through nurture rather than cold DM,
                          and lead with protecting the founder's calendar rather than
                          fixing a leak. Before any outreach, run a Deep-mode Instagram
                          contact-graph pass to identify the founder by name — pitching
                          founder-capacity protection without knowing the founder's
                          name is not viable.
status:                   PARK (mega-founder-brand, Medium priority) — route
                          differently from the rest of the batch
depth_mode:               Standard (escalate to Deep before pursuing)
unverified_fields:        founder/owner name (not found — blocking for this wedge);
                          whether a website exists; Meta ads (inconclusive); Google Ads;
                          aggregator paid listing; Mysuru branch phone
```

---

## 7. Cross-batch patterns

Observations that only emerge by looking across all 16 locations.

**1. Owner reply rate on negatives is the sharpest differentiator available from scraped data.** The batch splits cleanly into clinics that answer criticism (Skin and Recon 100%, Feather Touch 100%, Sparha 89%, Sanssouci 80%) and clinics that largely do not (Koza Jaya Nagar 8%, SkinFit 0%, Koza HRBR 0%, Contour 33%). This single metric correlates with almost everything else worth knowing about how a clinic handles inbound attention, and it is fully screenshot-provable — making it strong wedge evidence under the "closest to money already spent, fastest to a visible win" priority rule.

**2. "No results after paid sessions" is the dominant complaint archetype in this market.** It appears independently at Sanssouci, Koza Jaya Nagar, Advanced GroHair, Sparha, and Feather Touch — five separate businesses, different neighbourhoods, different price points. It consistently outranks scheduling complaints, rudeness complaints, and wait-time complaints. The implication for positioning: the pain these clinics' patients articulate is about *outcome ownership after payment*, which sits closer to post-consult and quote-chase wedges than to pure speed-to-lead.

**3. Multi-branch chains diverge sharply, and averaging them hides the opportunity.** Koza ranges from 3.8★ to 5.0★ across five branches. Rua runs 4.9★ and 5.0★. Feather Touch runs 4.8★ and 5.0★. Auditing a chain as a single entity would have buried Koza Jaya Nagar's 27% negative rate entirely — it is the strongest signal in that whole account, and it is invisible at the brand level.

**4. Review dormancy is a real and under-noticed pattern.** SkinFit (10.4 months), Koza Arekere (19.5), Koza Banashankari (10.1) have all effectively stopped collecting reviews while continuing to operate — and in Koza's case, while continuing to spend on ads. Three of sixteen locations are in this state. A clean rating with a stale date is not a healthy clinic; it is a stalled proof engine, and it is directly sellable.

**5. Named-founder discoverability varies enormously and predicts access difficulty.** Five clinics have confirmed named leadership on their own websites (Skin and Recon, Contour, SS Aesthetic, SkinFit, Sparha). Three have nobody identifiable anywhere (Koza, Sanssouci, Feather Touch) — and notably, two of those three are the largest by social following. Scale and anonymity correlate here, which inverts the usual assumption that bigger brands are easier to research.

**6. WhatsApp-first routing is visible in the data.** Contour's Instagram bio links directly to a `wa.me` deep link rather than a website. This supports the project's standing assumption that WhatsApp is the real booking engine and that Instagram comment scraping is low-yield — a dead-lead backlog at these clinics lives in WhatsApp threads, not in a CRM.

**7. Ad-platform coverage is asymmetric and neither platform alone is sufficient.** Meta ads were confirmed active at 6 clinics; Google ads were confirmed at only 2 (and one of those only because a prior advertiser ID was already known). A Meta-only check would have missed Contour's substantial and current Google spend; a Google-only check would have missed active Meta spend at SS Aesthetic, Sparha, Sanssouci, and Rua. Both checks are load-bearing.

---

## 8. Corrections made during self-review

The audit standard requires reviewing the draft as if auditing someone else's work, and relabelling anything that turns out to be assumed rather than verified. Four things changed. They are listed because a report that shows no corrections after a self-review pass usually means the pass was not real.

**1. SkinFit Wellness ↔ Skinnfit Medspa — conclusion reversed.**
First conclusion: unrelated businesses, a same-name collision, based on different spelling and different domains.
**Reversed after finding two contradicting signals:** SkinFit Wellness's own Instagram bio links to `skinnfit.in` (the other entity's domain), and a Skinnfit Medspa review names "Dr. Ruby." Final position: **likely related, exact relationship unresolved** — and explicitly *not* confirmation of the claimed Richmond Road branch, since the addresses still do not match. Detail in §6.4.

**2. Google Ads "no ads" findings — downgraded across 7 clinics.**
Initial reading treated zero-result queries as meaning no Google ad presence. A control check against Contour — a *verified, currently-active* advertiser — returned zero through both the brand-name and the domain query paths. Since the tool demonstrably fails to surface a live advertiser, every zero-result became **`undetermined`** rather than "no ads." Reporting "no ads" from a Meta-only or unreliable check is a documented failure mode of this pipeline, and it was live in this batch.

**3. Meta ads for SkinFit and Feather Touch — reclassified as `inconclusive`.**
The keyword sweep returned results for these queries, but inspection showed they belonged to entirely unrelated advertisers (HyugaLife, Home Essentials, drama-streaming apps). Counting those as "checked" would have been false coverage. With no Facebook page URL available to check directly, the honest label is `inconclusive`.

**4. Sparha's follower-count anomaly — investigated rather than assumed.**
The supplied handle's 217 followers looked inconsistent with a bio claiming a multi-awarded 20-year brand, which pattern-matches to a corporate-brand collision. It was checked and **resolved benignly** — 352 real Google reviews, a 2014 founding date, a company LinkedIn page, and a second larger Instagram account. The supplied handle simply is not the primary account. Recorded as resolved rather than left as a suspicion.

---

## 9. Limitations — what was not verified

Stated plainly, because gaps that are buried get mistaken for findings.

| # | Gap | Scope | Why |
|---|---|---|---|
| 1 | **Mystery shop not run** | All 10 clinics | Out of scope by design — you run this. Every wedge is provisional as a direct consequence. |
| 2 | **Google Ads status** | 7 of 10 clinics | Both query paths on the Transparency actor failed a live control test. Marked `undetermined`. |
| 3 | **Personal LinkedIn profiles** | All named doctors, 0 resolved | `harvestapi/linkedin-profile-search` hit its daily free-tier cap. Retry on a later day. |
| 4 | **Meta ads** | SkinFit, Feather Touch | Keyword search returned only unrelated advertisers; no Facebook page URL available to check directly. |
| 5 | **Aggregator paid listings (Practo Prime / JustDial)** | All 10 clinics | No verified actor exists for this step. Store search surfaced only Practo *doctor-directory* scrapers, none of which report Prime/sponsored badging. Time-boxed given batch size. This unlocks a §3 wedge row that stays invisible until solved. |
| 6 | **Claimed locations not found** | Koza Electronic City; SkinFit Richmond Road | Both claimed in Instagram bios; neither has a discoverable standalone GBP listing. Marked undetermined, not absent. |
| 7 | **Founder identity** | Koza, Sanssouci, Feather Touch | No named human found through any checked source. For Feather Touch this blocks the recommended wedge. |
| 8 | **LinkedIn company-employees search** | Koza (and others with company pages) | Never run — not cap-blocked, just not reached in this session. Best remaining contact route for Koza. |
| 9 | **Decision authority in chains** | Advanced GroHair, Koza | Hard kill #5 (committee sign-off, no single decision-maker) could not be assessed. Both are multi-branch operations with no identified owner. |
| 10 | **Identity ambiguities** | Contour ("Akanksha Thakur" vs "Akanksha Jha"); Sparha (Arti Singh's medical credential); Rua (Dr. Jeevith's role) | Each documented in the relevant dossier. All three would affect how outreach addresses a named person. |
| 11 | **Inbound lead volume, average treatment value, owner detachment, existence of lead data** | All 10 clinics | Hard kills #3, #4, #6, #8 are not scrapable by nature. Marked `undetermined` per the playbook rather than guessed. |
| 12 | **Website team pages** | Rua ("OUR TEAM" section), Feather Touch (no site found) | Crawl did not capture Rua's team page as a separate document; this is why its doctors sit at `likely` rather than `confirmed`. |

---

## 10. Tool health notes for the next batch

Worth carrying forward — two of these cost real time this session.

**`scrapesage/google-ads-transparency-scraper` — brand-name and domain queries are unreliable.**
A verified, currently-active advertiser (Contour, `AR10209256018437734401`, ads running the day of the check) returned **zero results** through both `queries` and `domains`. Only the `advertiserIds` path returned it correctly. **Recommendation:** treat query-based results as non-authoritative. Where an advertiser ID is known, use it. Where one is not, mark `undetermined` — never "no ads." Consider building a persistent advertiser-ID registry across batches, since IDs are stable and make future checks both cheap and trustworthy.

**`harvestapi/linkedin-profile-search` — silent daily cap, exactly as documented.**
Returned `status: SUCCEEDED`, `exitCode: 0`, zero items, and `statusMessage: "free user run limit reached"`. Nothing but the status message reveals the failure. **Recommendation:** read `statusMessage` on every run of this actor before trusting an empty result, and spend the daily allowance on the highest-value unconfirmed names first rather than in list order. The cap is separate from account credit.

**`compass/crawler-google-places` — 600s timeout at 120-review depth is normal.**
Four of five runs timed out, all having already written results. Batches of 3-5 search terms with `maxReviews: 120` reliably exceed 600s. **Recommendation:** either raise the timeout to 900s, or split into batches of 3, or accept the timeout and plan for a reconciliation pass. The results written before the timeout are complete and usable — do not discard them.

**Apify account memory cap (16 GB) limits parallelism.**
Four concurrent GBP runs consumed the full allocation and blocked a fifth actor from starting. **Recommendation:** cap concurrent runs at 3 for `compass/crawler-google-places`, or sequence the ads checks after the GBP runs finish.

**`apify/facebook-ads-scraper` keyword search is extremely noisy for Indian clinic names.**
Queries returned romance-novel apps, drama-streaming services, and unrelated clinics in other cities. **Recommendation:** always prefer a direct Facebook page URL (available from GBP contact enrichment) over keyword search. Keyword results should be filtered by exact `pageName` match before being counted.

**`apify/website-content-crawler` requires `includeUrlGlobs` as objects, not strings.**
The correct shape is `[{"glob": "**/team/**"}]`, not `["**/team/**"]`. A string array fails input validation with a bare "must be object" error.

---

## 11. Data provenance

Every figure in this report traces to a tool call made in this session on 2026-08-01. Nothing was carried forward from prior batches as fact.

| Actor | Runs | Key outputs |
|---|---|---|
| `apify/instagram-profile-scraper` | 1 | 10/10 profiles — bio, followers, posts, external URL |
| `compass/crawler-google-places` | 5 | 22 place records across 16 real locations + 6 noise results; ~1,100 reviews; contact enrichment |
| `apify/facebook-ads-scraper` | 2 | Keyword sweep (10 queries, 100 items) + direct page verification (3 pages) |
| `scrapesage/google-ads-transparency-scraper` | 5 | Brand-name query, domain query, advertiser-ID lookup, ad-creative detail, control test |
| `apify/website-content-crawler` | 1 | 8 domains, 14 pages including 3 team/about pages |
| `harvestapi/linkedin-profile-search` | 2 | **Both failed** — free-tier cap |

**Estimated spend:** ~$1.50–2.50, derived from observed per-event pricing and item counts. Not read from billing — verify in the Apify console for the exact figure.

**Search noise identified and discarded:** REGROW HAIR AND SKIN (Ramamurthy Nagar), The Skin Doctors (Pimpri-Chinchwad, Maharashtra), KOJA cosmetics store (New Delhi), Skinnfit Medspa (retained as a related-entity question rather than discarded — see §6.4).

---

## 12. Recommended next actions

**Immediate — yours to run:**
1. **Mystery-shop Contour Cosmetic Clinic first.** Strongest verified ad spend, below-average reply rate, WhatsApp-first routing means the backlog is findable.
2. **Then Sanssouci and Sparha** — both have concrete, quotable complaint patterns that make the opening frame land without needing invention.
3. **Shop Koza's Jaya Nagar branch specifically**, and consider shopping Banashankari alongside it — the intra-chain contrast may be a stronger story than either branch alone.
4. **Treat Skin and Recon, SS Aesthetic, and Rua as disprove-first.** All three may be passes. Record them as such if the shop says so rather than forcing a wedge.

**Research follow-ups when limits reset:**
5. **Retry LinkedIn person search tomorrow.** Priority order: Dr. Ruby Sachdev (SkinFit), Dr. Saket Jha (Contour), Dr. Shruthi Chikkaiah and Dr. Rakesh Koudki (Skin and Recon), Arti Singh (Sparha — also resolves the credential question).
6. **Run `harvestapi/linkedin-company-employees` for Koza and Sparha** — both have confirmed company pages and Koza has no other contact route.
7. **Run a Deep-mode Instagram contact-graph pass on Feather Touch** — its recommended wedge cannot be pitched without a founder name.
8. **Solve the aggregator check.** Either find a Practo Prime / JustDial actor that reports sponsored badging, or establish a reliable manual method. It unlocks a §3 wedge row that is currently invisible for every clinic in every batch.

**Verification items before any personalized outreach:**
9. Confirm whether Arti Singh (Sparha) holds a medical qualification before addressing her as "Dr."
10. Confirm whether Contour's "Akanksha Thakur" and "Akanksha Jha" are the same person.
11. Confirm SS Aesthetic has been operating over 12 months — if not, it becomes hard kill #2.
12. Establish decision authority at Advanced GroHair Jayanagar and Koza before investing in a cycle — hard kill #5 is open at both.

---

*Report generated by the `clinic-audit-research` pipeline. Individual per-clinic dossiers: files 01–10 in this directory. Machine-readable comparison table: `batch-comparison-table.csv`. Interactive dashboard: published artifact.*

*No message was sent to any clinic. No mystery shop was performed. All wedges are provisional.*
