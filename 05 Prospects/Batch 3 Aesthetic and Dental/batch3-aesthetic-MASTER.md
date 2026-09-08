---
date_created: 2026-08-03
date_modified: 2026-08-25
status: reference
---
# Batch 3 — Aesthetic Sub-Batch · MASTER DOSSIER

> *(⚠️ Retired tests: the six-test SOP was cut to two — qualification and quote decay — on 2026-08-13. Persistence, after-hours, cross-channel and booking friction no longer run. See `wedge-signal-entry.md` §2.)*

### 10 clinics · 16 locations · Bangalore + Mysuru
**Final draft — 2026-08-03.** Everything scrapeable is done except the mystery shop.

This is the **single source of truth** for this sub-batch. It merges:
1. the original audit artifact (`claude.ai/code/artifact/18a00c9c-397c-4133-ad75-0beaa8c3a796`);
2. the contact/founder/ads gap-fill pass;
3. a founder-direct LinkedIn pass;
4. a first-hand Google-review pull (distributions for all 10 + negative text for the three worst performers);
5. a **first-hand Meta Ad Library verification of all 10** — which corrected the artifact three more times.

**Supersedes** `batch3-aesthetic-audit.md` (marked superseded, kept for history) **and the artifact**,
which is now wrong on ad activity in six places and never carried contacts at all.

> ### ⚠️ Mystery shop is NOT done — for any of the 10.
> Every `recommended_entry_sku` below is **PROVISIONAL**. The Go/No-Go gate in
> `clinic-audit-checklist.md` cannot be satisfied without it. Tilak runs this step personally.

**Provenance key:** `[GBP]` Google Business Profile · `[REV]` first-hand review pull ·
`[IG]` Instagram scrape · `[WEB]` clinic's own site · `[LI]` LinkedIn scrape ·
`[GADS]` Google Ads Transparency · `[META]` Meta Ad Library (first-hand) ·
`[AGG]` Practo/JustDial · `[ART]` carried from the artifact, **not** re-verified.

**Total Apify spend, all passes: ~$0.80.**

---

## Every correction made to the artifact

| Clinic | Artifact said | Verified |
|---|---|---|
| Sparha | Google **undetermined** | **ACTIVE — 8 ads, continuous since 15 Nov 2023 (~961 days)** `[GADS]` |
| SS Aesthetic | Google not assessed | **ACTIVE — 4 ads, started 28 Jul 2026** `[GADS]` |
| SS Aesthetic | Meta **active** | ❌ **No Meta ads found.** Google-only clinic `[META]` |
| Koza | Google "active (1 ad)" | ❌ **Google DORMANT since Aug 2025** — that was a year-old creative `[GADS]` |
| Koza | — | **Meta ACTIVE — 5 ads, two routing to WhatsApp** `[META]` |
| Feather Touch | Meta **active** | ❌ **No Meta ads found** `[META]` |
| Advanced GroHair | Meta "active chain-wide" | ⚠️ **True for the chain, false for Bangalore.** Four live franchise pages — Rajahmundry, Erode, Trichy, Ramanathapuram. **No Bangalore page advertising** `[META]` |
| SkinFit | Meta **inconclusive** | ❌ **INACTIVE.** Zero paid acquisition on either platform `[META]` |
| Contour founders | "Dr. Akanksha **Thakur**/Jha (LIKELY)" | **Dr. Akanksha Jha**, Chief Surgeon `[LI]` |
| Sparha founder | "Arti Singh, 'Dr.' unverified" | **Not a doctor at all** — MSc Zoology, MPhil Life Science, BSc Cosmetology `[LI]` |
| Rua | "no single owner — weakest-evidence call" | **3 co-equal principals, named in the clinic's own IG title** `[IG]` |
| Sanssouci | "@ai.shikro" unresolved | **A marketing agency** — Meta WhatsApp API partner selling review management `[IG]` |
| Koza branches | 5 + Electronic City "not found" | **Sarjapur Road found** instead; Electronic City still unconfirmed `[GBP]` |
| Contour LLP | "dormant since Feb" | ✅ **Confirmed** — last ad 11 Feb 2026 `[GADS]` |
| Skin and Recon | "dormant since Apr '26" | ✅ **Confirmed** — last ad 8 Apr 2026 `[GADS]` |

---

## At a glance

| # | Clinic | Locality | ★ / reviews | ≤2★ | Google Ads | Meta Ads | Founder | Status |
|---|---|---|---|---|---|---|---|---|
| 1 | **Contour Cosmetic Clinic** | BTM / Hulimavu | 4.8 / 334 | **1.2%** | **LIVE — 4 ads** | **LIVE — 2 ads** | ✅ +**direct email** | Qualified — **P1** |
| 2 | **Koza Aesthetic Care** (5 br.) | multi | 3.8–5.0 / 75 | **27.3%** (JN) | dormant Aug '25 | **LIVE — 5 ads→WhatsApp** | ❌ | Qualified — **P2** |
| 3 | **SS Aesthetic Clinic** | Indiranagar | 5.0 / 43 | **0%** | **LIVE — new 28 Jul** | none | ✅ ×2 | Qualified — **P3** |
| 4 | **Sanssouci Wellness** | Mysuru | 4.2 / 148 | **17.6%** | none found | **LIVE — 4 ads→WhatsApp** | ❌ | Qualified — Park |
| 5 | **Sparha Advanced Aesthetic** | Indiranagar | 4.2 / 352 | **18.8%** | **LIVE — 961 days** | **LIVE — 3 ads** | ✅ | Qualified — **FLAGGED** |
| 6 | **Feather Touch Aesthetic** | Jayanagar + Mysore | 4.8 / 803 | 4.0% | none found | **none found** | ❌ | Park |
| 7 | **Skin and Recon** | Jayanagar | 4.9 / 242 | 2.9% | dormant Apr '26 | none | ✅ ×2 | Qualified |
| 8 | **SkinFit Wellness** | Koramangala | 4.9 / 120 | 2.5% | none | none | ⚠️ disputed | Qualified — Park |
| 9 | **RUA Skin & Hair** (2 br.) | R'murthy + Indiranagar | 4.9–5.0 / 97 | **0%** | none found | **LIVE — 1 ad** | ✅ ×3 | Qualified |
| 10 | **Advanced GroHair GloSkin** | Jayanagar | 4.7 / 118 | 5.1% | undetermined | none (BLR) | ❌ weak | Merge into chain |

### Working order
1. **Contour** — only founder-direct email in the batch, live on both platforms today.
2. **Koza** — worst complaint pattern in the batch *and* live Meta spend into WhatsApp. Best evidence-to-spend ratio.
3. **SS Aesthetic** — Google spend started 6 days ago; §0 says go where the money just landed.
4. **Sanssouci** — complaint-answering collapsed while an agency is paid to manage reviews.
5. **Sparha** — biggest visible pain, but read the flag before deciding to engage at all.

---

# 1 · Contour Cosmetic Clinic — BTM Layout / Hulimavu
**P1. Live on Google *and* Meta, and the only founder-direct channel in the batch.**

### Basic info `[GBP]`
2nd floor, Lakshmidevi Complex, 80 Ft Rd, Muthuraya Swamy Layout, BTM Layout, Bangalore ·
Hair transplantation clinic · **4.8★ / 334 reviews**

### Points of contact
| Name | Role | Channel | Confidence |
|---|---|---|---|
| **Dr. Saket Jha** | Founder / Medical Director | 🎯 **`saket@contourcosmeticclinic.com`** — founder-direct, **verified deliverable** (`valid`, quality 80, non-free domain) `[LI]` · IG `@drsaket.jha` (verified ✓, 6,165 followers) · `linkedin.com/in/drsaketjha` | **confirmed** |
| **Dr. Akanksha Jha** | **Chief Surgeon** — MBBS, MS ENT, Otolaryngologist & Head/Neck Surgeon `[LI]` | IG `@drakanksha.jha` · `linkedin.com/in/akankshajha05` (dormant, 1 connection) | **confirmed** |
| Clinic | — | +91 86604 32589 · contact@contourcosmeticclinic.com | confirmed |
| WhatsApp | — | `wa.me/918660432589` — from IG bio `[IG]` | confirmed |

Website contourcosmeticclinic.com · IG `@contour_hair` (verified, 4,487 followers) + `@contour_skin` ·
LinkedIn company `/contour-cosmetic-clinic` · FB page ID **111333664768872** (472 likes) `[META]`
Claimed: 100+ publications, 2,000+ transplants.

### Ads
- **Google — LIVE `[GADS]`:** advertiser `AR10209256018437734401`, 4 concurrent text ads, last shown **2026-08-02**.
- **Google — LLP entity DORMANT `[GADS]`:** `AR14094849889598963713`, heavy video Oct 2025 → **11 Feb 2026**, then nothing. ✅ *Artifact confirmed.*
- **Meta — LIVE `[META]`:** 2 active ads — one from 16 Jun ("Book now"), one from 26 Jul routing to **instagram.com/contour_hair**.

### Reviews `[GBP]` `[REV]`
| 5★ | 4★ | 3★ | 2★ | 1★ | ≤2★ |
|---|---|---|---|---|---|
| 277 | 47 | 6 | 1 | 3 | **1.2%** |

Last review gap ≈0.2 months — arriving continuously. 33% of negatives answered `[ART]`.
**Qualitative:** cleanest ratio in the batch. Four negatives total across 334 reviews — too few to
carry a wedge. Negative text not read in depth (volume doesn't justify it); the *quantitative* profile
is fully verified.

```
funnel_break_stage:       Reactivation
recommended_entry_sku:    Dead-lead reactivation — PROVISIONAL
confirm_via_mystery_shop: Money is flowing on both platforms today, and the Meta ad points at
                          Instagram while the IG bio points at WhatsApp. Shop that exact path.
                          If reply is fast → redirect to "Follow-up and nurture engine".
status:                   Qualified — TOP PRIORITY.
```

---

# 2 · Koza Aesthetic Care — multi-branch chain (5 confirmed)
**P2. The strongest wedge evidence in the batch, against live Meta spend.**

### Branches `[GBP]` — all share one front-desk line: **+91 96060 09079**
| Branch | Address | ★ / reviews |
|---|---|---|
| **Jaya Nagar** | Ground Floor, 35/20, 11th Main Rd, Vishya Bank Colony, 5th Block | **3.8 / 44** ← weak point |
| Arekere | 3rd floor, Sharada Arcade, Bannerghatta Rd, Omkar Nagar | 5.0 / 2 |
| HRBR Layout / Kalyan Nagar | 914, 5th A Cross Rd, inside Motherhood Hospital | 4.6 / 9 |
| Banashankari | 4, 30th Main Rd, opp. Kempegowda Institute of Medical Science | 5.0 / 20 |
| **Sarjapur Road** ← *new find* | No 514, 1, 2-3, Sarjapur Main Rd, opp. More Mall | no reviews yet |

Electronic City (artifact's missing 6th) **not found**; Sarjapur Road likely resolves that gap.

### Points of contact
| Name | Role | Channel | Confidence |
|---|---|---|---|
| — | **No founder or owner identified anywhere** | — | — |
| "Kridha" | Service Excellence Team — signs owner replies `[REV]` | — | weak |
| Front desk | shared across all 5 branches | +91 96060 09079 | confirmed |
| **Email** | 🆕 surfaced in an owner reply `[REV]` | **kozaaestheticcare@gmail.com** | confirmed |
| Facebook | — | `facebook.com/koza.aesthetic.care` · page ID 609716852235823 · 657 likes `[META]` | confirmed |

**Blockers:** kozacare.org is **largely broken** — 17 pages 404 including `/aboutus`; only the homepage
renders `[WEB]`. Sibling domains kozacare.in / kozaaesthetic.com exist; **koza.care does not resolve
(DNS failure)**. Both guessed IG handles dead. LinkedIn company page exists but the employee scraper
is capped (see Limitations).

### Ads
- **Meta — LIVE `[META]`:** 5 active ads (started 15 Jun, 27 Jul ×2, 28 Jul). **Two route directly to
  `api.whatsapp.com/send`.** WhatsApp is the booking engine.
- **Google — DORMANT `[GADS]`:** one ad, 13 Jun → **11 Aug 2025**, nothing since.

### Aggregator `[AGG]`
Listed on JustDial at three branches — **Arekere shows 4.3★ / 208 reviews / 98 photos**, versus just
**2 reviews on Google**. Jayanagar 4.0★ / 43; Banashankari 4.6★ / 23. **Their patient feedback lives on
JustDial, not Google** — a materially different picture depending where you look. Prime/sponsored
badging not verified.

### Reviews — quantitative, Jaya Nagar `[GBP]`
| 5★ | 4★ | 3★ | 2★ | 1★ | ≤2★ |
|---|---|---|---|---|---|
| 29 | 2 | 1 | 0 | **12** | **27.3%** |

### Reviews — qualitative `[REV]` — first-hand, Jaya Nagar
The clearest "paid upfront, service never delivered" evidence anywhere in this batch:

**(a) Package bought, sessions not delivered.** A Jun 2025 reviewer on an *unlimited / 12+ session*
yearly package received **four sessions**: *"They were irregular, staff keeps quitting... After 3
times they don't even follow up."* A promised ₹6,000 refund was never paid. Their closing line is the
wedge in one sentence: *"others are left to struggle after receiving full payments."*

**(b) Equipment failure, no recovery, refund refused.** A Jun 2025 reviewer paid **₹11,800 upfront**,
travelled 40 km, was numbed for MNRF — **the machine didn't work** for the full hour. *"I didn't
receive any call from them about further course of action. I called repeatedly... they refused to
refund my money."* They state they are filing in consumer court.

**(c) Large spend, no result.** Sep 2025: *"we paid 1 lakh+ no changes."*

**(d) Sales-over-care.** Sep 2025: *"the staff seemed more interested in charging extra and selling
their products."*

**(e) Still happening.** A 1★ posted **2026-08-01 — two days ago**: *"3rd session no results at all...
Only money minded people."* **No reply.**

**(f) The sharpest finding: they answer praise and ignore complaints.** Of the 1★ reviews pulled,
**exactly one** ever received a reply. Meanwhile a *4★* review drew a warm, personalised response
signed by their "Service Excellence Team." The reply machinery exists — it is pointed only at
positive reviews.

> **Read for the wedge:** live Meta budget is pushing new enquiries into WhatsApp while existing
> paying customers report sessions undelivered, refunds refused, and no follow-up after the third
> visit. That is money in the front door leaking straight out the back, and it is provable from their
> own review page.

```
funnel_break_stage:       Follow-up Persistence
recommended_entry_sku:    Follow-up and nurture engine — PROVISIONAL
confirm_via_mystery_shop: Shop the WhatsApp path — that is where live Meta money lands, on one shared
                          line covering five branches.
status:                   Qualified — P2. Park tier (Medium) on contactability only: front desk is
                          the sole reachable channel. Founder discovery is the blocker, not the wedge.
```

---

# 3 · SS Aesthetic Clinic — Indiranagar
**P3. Google spend started six days ago. Google-only — no Meta.**

### Basic info `[GBP]`
Floor 1, Building 32, above Yamaha Showroom, opp. Filter Coffee, HAL 3rd Stage, New Thippasandra,
Indiranagar, Bangalore 560075 · Skin care clinic · **5.0★ / 43 reviews** · Google-flagged *women-owned*

### Points of contact `[WEB]`
| Name | Role | Confidence |
|---|---|---|
| **Mrs. Shylaja B.S.** | Founder | **confirmed** |
| **Mrs. Suchitra B.S.** | Co-founder | **confirmed** |
| Dr. Jabin | Clinic cosmetologist | **confirmed** |
| Clinic | +91 91132 76518 · ssaesthetics0825@gmail.com | confirmed |

ssaesthetics.in · IG `@ss_aesthetics_indiranagar` (476 followers, phone in bio) ·
FB `profile.php?id=61583357924707`
Positioning `[WEB]`: *"every treatment is doctor-led and clinically supervised — not just
technician-driven."* No personal LinkedIn located for either founder (name-search actor capped).

### Ads
- **Google — LIVE, brand new `[GADS]`:** advertiser "SS Aesthetics" `AR08697026139782119425` — 4 ads,
  **all first shown 2026-07-28**, live through 2026-08-02.
- **Meta — NONE `[META]`.** Keyword search returned only unrelated brands (Grand Seiko, Nirvana by SS,
  Access, sparify_). ⚠️ *The artifact claimed Meta active — not supported.*

### Reviews `[GBP]`
| 5★ | 4★ | 3★ | 2★ | 1★ | ≤2★ |
|---|---|---|---|---|---|
| 42 | 1 | 0 | 0 | 0 | **0%** |

**Qualitative:** zero negatives ever. Tags cluster on *experience*, not outcomes — *calm atmosphere*
(5), *professional care* (3), *warm staff* (3), *hygiene* (3), *refreshed skin* (2), *brighter skin* (2).
Treatments named: chemical peel (3), laser hair removal (2). There is **no review evidence in either
direction** — 43 reviews, all positive. The mystery shop carries this lead entirely.

```
funnel_break_stage:       Response Speed
recommended_entry_sku:    Speed-to-lead audit (§2 six-test SOP) — PROVISIONAL
confirm_via_mystery_shop: Six-day-old ad spend, two founder-operators, single channel, 43 reviews.
                          Textbook first-response-failure setup, and no review evidence exists to
                          lean on — the six tests ARE the diagnosis here.
status:                   Qualified — priority raised on new-spend signal.
```

---

# 4 · Sanssouci Wellness Clinic — Mysuru

### Basic info `[GBP]` `[WEB]`
1216, 2nd floor, above Toyota showroom, New Kantharaj Urs Road, Ballal Circle, Krishnamurthy Puram,
Mysuru 570004 — *site separately cites a Kalidasa Road flagship; two sites or a move, unresolved* ·
Category **Weight loss service** · **4.2★ / 148 reviews** · est. 19 Mar 2018 · affiliated with
Bellamente Cosmetica, Berlin.

### Points of contact
| Name | Role | Channel | Confidence |
|---|---|---|---|
| — | **No founder identified.** About page lists only generic roles `[WEB]` | — | — |
| Clinic | — | +91 96112 11581 · contactus@sanssouciwellness.com | confirmed |
| Landline (uncertain) | — | 0821-452691 `[GBP]` | weak |

sanssouciwellness.com · IG **`@sanssouci_wellness.mysuru`** (2,836 followers, 606 posts) — the
`@sanssouciwellness` handle is a dead 1-follower placeholder · FB page ID **303150316881090**
(2,192 likes) `[META]` · YouTube active.

### ⚠️ Incumbent vendor `[IG]`
IG bio: **"Managed by: @ai.shikro"**. That account's bio: *"Meta's WhatsApp API Partner 🤝 | AI-Driven
Marketing 🚀 | Social • SEO • Ads • **Reviews** • Branding"*. Sanssouci outsources social, ads,
WhatsApp API **and review management** — which makes the finding below considerably sharper.

### Ads
- **Meta — LIVE `[META]`:** 4 active ads. Two from 23 Jun (one WhatsApp CTA, one "Send message"), two
  launched **2026-08-01 — two days ago** (one WhatsApp CTA, one pointing at
  `instagram.com/sanssouci_wellness.mysuru`). **Two of four route to WhatsApp** — exactly consistent
  with an agency that sells Meta WhatsApp API integration.
- **Google:** no advertiser record `[GADS]` *(the "Sanssouci ITSM GmbH" hit is a German IT firm)*.

### Reviews — quantitative `[GBP]`
| 5★ | 4★ | 3★ | 2★ | 1★ | ≤2★ |
|---|---|---|---|---|---|
| 104 | 18 | 3 | 0 | **23** | **17.6%** |

Tags: *friendly staff* (43), *weight loss* (14), *homely atmosphere* (8), *professional team* (6).

### Reviews — qualitative `[REV]` — first-hand
**(a) The 100%-upfront pattern, verbatim across four years.** A 2020 reviewer (weight loss) and a 2024
reviewer (GFC/PRP) — unrelated — write *nearly the same sentence*: *"These people charge the entire
amount in the beginning as they know people won't pay in the end because of no results. And it is
always 30000 minimum."* Both report ₹30–40k spent, no outcome. A 2021 reviewer: *"firstly itself they
will take all the money we will having no option so we should continue there."*

**(b) Owner replies stopped — the sharpest datable finding in the batch.** Every negative from
**2019–2022 got a reply** (templated, but present). Then:
- 2025-11-27 1★ — **no reply**
- 2026-02-12 1★ *"complete scam... Zero results, zero improvement"* — **no reply**
- 2026-02-26 1★ *"waited 3 months because the machine was not working"* — **no reply**

They used to answer everything. They stopped — **while paying an agency whose pitch names "Reviews."**

**(c) Equipment downtime** — a Feb 2026 reviewer waited *three months* for a laser appointment.

**(d) Credentialing challenged** — a 2022 reviewer: *"they don't have any qualified dermatologist over
here."* The clinic replied asserting all staff are qualified.

**(e) Review-deletion pressure** — a 2022 reviewer describes the owner phoning repeatedly *"begging me
to delete the review."* ⚠️ Single-reviewer allegation; echoes the shape seen at Sparha.

> **Read for the wedge:** they pay a WhatsApp-API marketing agency and *still* leave their three most
> recent one-stars unanswered — while launching two fresh Meta ads on 1 August. New spend on top of an
> unattended back end. Specific, current, screenshot-provable.

```
funnel_break_stage:       Reactivation
recommended_entry_sku:    Dead-lead reactivation — PROVISIONAL
confirm_via_mystery_shop: Shop the WhatsApp path — the agency runs Meta's WhatsApp API, so reply
                          behaviour there IS the diagnosis.
status:                   Qualified — Park tier (High): shallow existing automation. Expect
                          vendor-displacement resistance; frame against the incumbent's own remit.
```

---

# 5 · Sparha Advanced Aesthetic Studio — Indiranagar
**Biggest visible pain in the batch — and the biggest risk. Read the flag before engaging.**

### Basic info `[GBP]` `[WEB]`
Metro Pillar 55, 842/A, 100 Feet Rd, opposite Dominos, Indiranagar 1st Stage · Skin care clinic ·
**4.2★ / 352 reviews** · established 2014

### Points of contact
| Name | Role | Channel | Confidence |
|---|---|---|---|
| **Arti Singh** | **Founder and CEO** (self-stated `[LI]`) | `linkedin.com/in/arti-singh-69b642100` (217 followers) · second dormant profile `arti-singh-5b1b4730` | **confirmed** |
| Clinic | — | +91 99727 19303 · info.sparha@gmail.com · (a review reply also cites sparha.arti@gmail.com) | confirmed |

sparha.in · IG `@sparha.aesthetic.studio` (219 followers, **live**; the GBP-listed underscore variant
`@sparha_aesthetic_studio` is **dead**) · FB `SparhaClinic`, page ID **107931040548397** (354 likes)
`[META]` · LinkedIn company `/sparha`

### ⚠️ The "Dr." title is false — never use it in outreach `[LI]`
Her own LinkedIn About: *"I am an **aesthetician**... I hold a **Master's degree in Zoology** and an
**M Phil in Life Science**, I have earned a **Bachelor's degree in Cosmetology**."* Prior roles: area
head at Inspirations and Bodycare Vibes; Miss Bhopal 1993. **No medical qualification.** Yet reviewers
address her as "Dr. Arti", and the business markets itself as a *"plastic surgery brand"* with **no
surgeon named anywhere** on site, IG, or LinkedIn.

### Ads
- **Google — LIVE, longest-running in the batch `[GADS]`:** "SPARHA ADVANCED WELLNESS STUDIO"
  `AR15248201148633448449` — 8 concurrent text ads, first shown **2023-11-15**, live **2026-08-02**.
  Individual creatives show **754–961 days** continuous run.
- **Meta — LIVE `[META]`:** 3 active ads, started 14 Jul and 21 Jul ×2, all "Learn more".

### Aggregator `[AGG]`
Listed on Practo as **"Sparha Advanced Wellness Studio, Indiranagar"** — matching the Google Ads
advertiser entity, not the trading name. Practo copy claims *"doctors and nurses trained to use
advanced technology"* — note the contrast with no named practitioner. Prime badging not verified.

### Reviews — quantitative `[GBP]`
| 5★ | 4★ | 3★ | 2★ | 1★ | ≤2★ |
|---|---|---|---|---|---|
| 258 | 21 | 7 | 3 | **63** | **18.8%** |

**Sharply bimodal** — 258 five-stars against 63 one-stars, almost nothing between. The 4.2★ headline
hides that nearly one review in five is a bottom rating. Tags: *hair transplant* (43), *supportive
staff* (19), **cost (19)**, *laser hair removal* (17).

### Reviews — qualitative `[REV]` — first-hand, 20 lowest-rated
Four shapes repeat across **independent** reviewers, 2016→2026:

**(a) Full payment upfront, then follow-up collapses.** 2023: *"I hv paid more than one lkh for
treatment and after three session they didn't call me also for any session for two months."* 2024: a
client made to pay in full **before** the procedure so billing wouldn't delay them — ₹30k of intended
spend became **₹1.45 lakh**. Another 2024: *"they will ask you to pay advance and then they treat you
badly because no way you get your money back."*

**(b) Aggressive in-chair upselling.** A 2024 laser client describes a 2.5-hour session interrupted so
the machine could serve another client, closing with a product pitch — *"this place is more of a sales
business."*

**(c) Escalation-grade: procedures without a doctor present.** An Oct 2025 reviewer (8 likes, edited
three times) alleges a transplant *"carried out entirely by unqualified technicians, with no doctor
present throughout"*, 2,500 grafts against 4,000+ promised, *"left in the care of two junior nurses."*
A separate, unrelated Dec 2025 reviewer reports undereye fillers with *"no doctor explaining the
procedure, no medical staff present."* **That Dec 2025 complaint has no owner reply.**

**(d) Consent and review-suppression allegations.** The Oct 2025 reviewer later adds: *"Sparha is now
using a video of me on Instagram that I never approved"*, and lists *"Force to remove reviews"*.
⚠️ **Allegations from one reviewer**, not established fact — but they corroborate the artifact's
independent flag, and an equivalent review-deletion account appears at Sanssouci.

**Owner reply tone has swung.** 2016–2020 replies are openly combative — one closes *"Free treatment
otherwise bad review !!!!! Ultimate"* with eye-roll emojis. 2024–2026 replies are long and
professional; the most recent 1★ (May 2026, a **loyal 15-month-package client** whose technician was
absent with no trained backup) drew a genuinely well-handled apology.

> **Read for the wedge:** acquisition is not the problem — 961 days of unbroken ad spend proves that.
> The failure is **after payment clears**: sessions unscheduled, nobody calling back, no backup when
> a technician is out.

```
funnel_break_stage:       Quote Chase
recommended_entry_sku:    Quote-decay follow-up — PROVISIONAL
confirm_via_mystery_shop: Confirm whether quotes are issued then abandoned. Open on the post-payment
                          follow-up gap — NEVER on the safety or consent allegations. Those are
                          context for YOUR decision to engage, not outbound material.
status:                   Qualified — FLAGGED. Escalation-grade allegations + a founder with no
                          medical credential marketing surgical services. Tilak's call whether to
                          work this lead at all.
```

---

# 6 · Feather Touch Aesthetic Clinic & Academy — Jayanagar + Mysore

### Locations
| Location | Address / handle | Phone | ★ / reviews |
|---|---|---|---|
| **Jayanagar (main)** | 2nd floor, B and A Square-II, 1376, 32nd E Cross Rd, 4th T Block East `[GBP]` | +91 99009 83048 / 99011 32233 | **4.8 / 803** |
| **Mysore branch** | IG `@feathertouchclinicmysore` (1,114 followers) `[IG]` | +91 99022 50038 | GBP listing thin (5 reviews) |

Mysore branch **confirmed genuine** — the Bangalore IG bio names it and it cross-links back `[IG]`.

### Points of contact
| Name | Role | Channel | Confidence |
|---|---|---|---|
| — | **No founder identified** | — | — |
| Clinic | — | +91 99009 83048 · +91 99011 32233 | confirmed |
| Mysore | — | +91 99022 50038 | confirmed |
| "Dr. Anjali" / "Madhavi" | third-party directories only | — | **weak — do not use** |

**No website exists.** Presence is IG + YouTube + directory listings.

### Digital presence — the batch outlier `[IG]`
- `@feather_touch_aesthetic_clinic` — **45,046 followers**, business account, Medical & health.
  **3.7× the next-largest account in this batch.**
- `@feather_touch_academy_` — 1,690 followers, **Permanent Makeup Academy**: a separate training
  revenue line sharing the same two phone numbers.

### Ads
- **Meta — NONE FOUND `[META]`.** Search returned only decoys (Abode Handicrafts, Aara's terracotta
  jewellery). ⚠️ *The artifact claimed Meta active — not supported.*
- **Google — none `[GADS]`.** ⚠️ *"Feather Touch Tissues" (39 ads) and "FEATHER TOUCH TRADING COMPANY"
  are unrelated businesses. Do not attribute.*

**So: 45,000 followers, 803 reviews, an academy — and zero verifiable paid acquisition on either
platform.** Growth here is organic and reputational.

### Aggregator `[AGG]`
Listed on Practo and JustDial (Jayanagar 7th Block). Prime badging not verified.

### Reviews — quantitative `[GBP]`
| 5★ | 4★ | 3★ | 2★ | 1★ | ≤2★ |
|---|---|---|---|---|---|
| 745 | 25 | 1 | 2 | **30** | **4.0%** |

### Reviews — qualitative `[ART]` — **not re-read first-hand**
**100% of negatives answered** — the healthiest reply engagement in the batch. Complaint shape is
*celebrity-priority / junior-staff overflow*: *"They give more importance to celebrities... normal
clients get unexperienced staff"*, repeated by 2+ independent reviewers. That is a **capacity** signal,
not a lead-response one. The 30 one-stars were not read individually this session.

```
funnel_break_stage:       Post-consult
recommended_entry_sku:    Founder-capacity protection — PROVISIONAL
confirm_via_mystery_shop: 45k followers + an academy + 803 well-answered reviews + no website + no
                          paid ads says attention is the constraint, not leads.
status:                   Park (Medium) — mega founder-brand. Needs a Deep-mode IG contact-graph pass
                          to name the founder before any approach.
```

---

# 7 · Skin and Recon — Jayanagar 4th Block

### Basic info `[GBP]`
255, 1st Floor, 36th Cross, 5th Main Rd, 4th Block, Jayanagar · Dermatologist · **4.9★ / 242 reviews** ·
17 yrs experience, ~5,000 patients claimed `[WEB]`

### Points of contact
| Name | Role | Channel | Confidence |
|---|---|---|---|
| **Dr. Shruthi Chikkaiah** | Chief Dermatologist — **and concurrently Head of Dept, Dermatosurgery at Cutis** `[LI]` | `linkedin.com/in/shruthi-chikkaiah` | **confirmed** |
| **Dr. Rakesh Koudki** | Plastic Surgeon, double board-certified, ~13 yrs | own bio page + IG bio | **confirmed** |
| Clinic | — | +91 63614 17399 · skinandrecon@gmail.com | confirmed |

skinandrecon.in · IG `@skinandrecon` (396 followers) · FB `facebook.com/skinandrecon`
Site hygiene: internal links still point at the staging domain `site1.kinsta.cloud` `[WEB]`.

### Ads — **zero current paid acquisition**
- Google `[GADS]`: 10 ads ran 1 Mar → **8 Apr 2026**, stopped dead. ✅ *Artifact confirmed.*
- Meta `[META]`: no page ads. ✅

### Aggregator `[AGG]`
On Practo as "Skin & Recon Dermatology And Plastic Surgery Clinic, Jayanagar 4 Block", 2 doctors listed.

### Reviews `[GBP]`
| 5★ | 4★ | 3★ | 2★ | 1★ | ≤2★ |
|---|---|---|---|---|---|
| 232 | 2 | 1 | 0 | 7 | **2.9%** |

Tags: **friendly doctor (32)**, *speedy recovery* (5), *rhinoplasty* (5), *hair transplant* (5).
**Qualitative:** 100% of negatives answered `[ART]`; tag cloud dominated by a relationship signal.
Negative text not read in depth — seven negatives across 242 reviews doesn't carry a wedge.

> **Read for the wedge:** a three-week ad burst in March–April 2026 stopped dead and never resumed,
> Meta was never used, and the chief dermatologist simultaneously heads a department elsewhere. That
> reads as attention moving — worth *asking about*, not assuming a lead-handling failure. Puts §1
> kill #6 (owner detached from lead ops) on the table as a question to test.

> ### ⛔ SUPERSEDED 2026-08-25 — do not draft from the block below
>
> **Hard kill #2 is FAILED, not passed.** This file recorded a "multi-year footprint implied."
> A full 84-review census of Ramamurthy Nagar puts the **oldest Google review at 2025-10-15** —
> **10 months 10 days old**, under the 12-month threshold. §1.1 #2 names the oldest-review date as
> the exact test and marks it scrapable. Indiranagar's first review is 2026-03-18 (~5 months).
> The kill clears ~2026-10-15. Proceeding before then is Tilak's call, not a default.
>
> **The wedge below is wrong twice.** Dead-lead reactivation needs a dormant pool a 10-month-old
> clinic does not have, and §3's dormant-patient row explicitly requires "12+ months operating."
> The mystery shop has now run (Indiranagar WhatsApp) and routes to
> **Qualification → Booking / No-show · Qualification + scoring upgrade.**
>
> **Ownership resolved further:** the site's own /about-us heads the three doctors "OUR FOUNDERS."
> **Full replacement:** `04 Clients/RUA Skin and Hair Center/RUA Skin and Hair Call Dossier 2026-08-25.md`

```
funnel_break_stage:       Reactivation
recommended_entry_sku:    Dead-lead reactivation — PROVISIONAL (weak basis)
confirm_via_mystery_shop: Ask why the April spend stopped. Do not lead with a complaint narrative —
                          there isn't one.
status:                   Qualified.
```

---

# 8 · SkinFit Wellness — Koramangala

### Basic info `[GBP]`
3rd floor, 534/A, 7th Cross Rd, 8th/4th Block, Koramangala · Skin care clinic · **4.9★ / 120 reviews** ·
**last review ≈10.4 months ago** `[ART]`

### Points of contact
| Name | Role | Channel | Confidence |
|---|---|---|---|
| **Dr. Ruby Sachdev** | named by skinfitwellness.in as clinical principal — **see warning** | `linkedin.com/in/dr-ruby-sachdev-a5b652122` · IG `@skinnfit.in` | **`likely`** ⚠️ downgraded |
| Clinic | — | +91 91879 67633 · info@skinfitwellness.in | confirmed |

IG handle for *this* clinic **not found** — `@skinfitwellness` is an unrelated Temecula, California
esthetician; `@skinfit_wellness` does not exist.

### ⚠️ Possible two-entity confusion — resolve before outreach
Her LinkedIn headline is a generic *"Beauty and Wellness Transformation"* and **never names SkinFit
Wellness** `[LI]`. Her own brand appears to be **Skinnfit Medspa** (`skinnfit.in`, IG `@skinnfit.in`) —
which my GBP sweep returned as a **separate business**: Aster Clinic, 952, 24th Main Rd, JP Nagar,
**4.7★ / 13 reviews**. Different address, different listing from SkinFit Wellness Koramangala.
Either (a) she founded both, (b) skinfitwellness.in licenses her name for marketing, or (c) two
unrelated ventures with similar names. The agency staging subdomain `skinfitwellness.nestershub.com`
serving the same site leans toward (b). Per Phase 3: **unconfirmed**.

### ⚠️ Park-tier signal — shallow existing automation (High) `[WEB]`
Brands itself **"India's First AI-Driven Cosmetology & Wellness Clinic"**, and its homepage already
sells against the exact failures ValenceOps addresses: *"Same energy. Same protocol. Same upsell
regardless of how your skin actually responds"* · *"Pricing revealed in pieces, package by package"* ·
*"Recommendations tied to commission, not need"* · *"Adaptive plan built on your scored response"* ·
*"Itemised pricing, given upfront — no surprises."*
**Pitching them generic ops automation is pitching them their own marketing.**

### Ads — zero paid acquisition
No Meta page ads `[META]`; no Google advertiser record `[GADS]`.

### Reviews `[GBP]`
| 5★ | 4★ | 3★ | 2★ | 1★ | ≤2★ |
|---|---|---|---|---|---|
| 116 | 1 | 0 | 1 | 2 | **2.5%** |

Tags: *laser treatment* (10), *supportive staff* (7), *dermatologist* (5), **personalized approach (4)**.
0% of negatives answered `[ART]`.
**Qualitative:** almost entirely positive — but **the flow stopped**. No review in ~10.4 months against
a base that was clearly accumulating. Directly observed, and the one hard current fact here.

> **Read for the wedge:** the angle that survives their positioning is the contradiction itself — a
> clinic claiming AI-driven, scored, adaptive follow-up has produced no patient review since roughly
> September 2025. Lead with the gap between claim and evidence, never with generic automation.

```
funnel_break_stage:       Reviews
recommended_entry_sku:    Review reactivation agent — PROVISIONAL
confirm_via_mystery_shop: Also settle the SkinFit ↔ Skinnfit question — you need to know who owns
                          the Koramangala clinic.
status:                   Qualified — Park tier (shallow automation). Route carefully.
```

---

# 9 · RUA Skin & Hair Center — 2 branches

### Branches `[GBP]`
| Branch | Address | Phone | ★ / reviews |
|---|---|---|---|
| Ramamurthy Nagar | 2nd Floor, No 14, TC Palya Main Rd, above Burger King | +91 99597 63678 | 4.9 / 80 |
| Indiranagar | 1060/1050, Jeevan Bima Nagar, 3rd Stage Cross Rd, HAL 3rd Stage | +91 70199 76689 | 5.0 / 17 |

### Points of contact — ownership resolved `[IG]`
The Instagram account title is literally **`RUA Skin & Hair Center | Dr. Jeevith | Dr. Eshritha |
Dr. Jatin |`**, bio: *"✨3 Expert Dermatologists · Doctor-Led."*

| Name | Role | Confidence |
|---|---|---|
| **Dr. Jeevith** · **Dr. Eshritha** · **Dr. Jatin** | Co-equal principal dermatologists | **confirmed** |

> The artifact called this *"the weakest-evidence call in the batch"*. It was never an ambiguity —
> the clinic publishes all three names in its own account title. **Resolved.**

ruaskinandhair.com · IG `@ruaskinandhair` (1,277 followers; both branch phones in bio) ·
FB page ID **857203120810863** — note only **30 page likes** `[META]` · No email surfaced.
No personal LinkedIn located for any of the three (name-search actor capped).

### Ads
- **Meta — LIVE `[META]`:** 1 active ad, started **2026-07-27**, CTA "Send message". ✅ *Artifact correct.*
- **Google:** no advertiser record `[GADS]`.

### Reviews `[GBP]`
| Branch | 5★ | 4★ | 3★ | 2★ | 1★ | ≤2★ |
|---|---|---|---|---|---|---|
| Ramamurthy Nagar | 75 | 5 | 0 | 0 | 0 | **0%** |
| Indiranagar | 17 | 0 | 0 | 0 | 0 | **0%** |

**Zero negatives at either branch, confirmed first-hand.** Nothing to read qualitatively — which is
itself the finding. A brand-new Meta ad (27 Jul) against a 30-like page suggests paid acquisition is
a recent, tentative experiment.

```
funnel_break_stage:       Reactivation
recommended_entry_sku:    Dead-lead reactivation — PROVISIONAL (weak basis)
confirm_via_mystery_shop: Thinnest evidence in the batch. Three decision-makers is itself a friction
                          risk — §1 kill #5 does NOT apply (a partnership is not committee sign-off),
                          but confirm who owns lead ops before pitching.
status:                   Qualified.
```

---

# 10 · Advanced GroHair GloSkin — Jayanagar branch
**Merge into the existing chain dossier — do not work as a standalone lead.**

### Basic info `[GBP]`
539, 2nd Floor, 10th Main Rd, above Heads Up for Tails, 4th/5th Block, Jayanagar ·
Hair transplantation clinic · **4.7★ / 118 reviews**

### Points of contact
| Name | Role | Channel | Confidence |
|---|---|---|---|
| "Karthik" | branch manager | named **only inside a patient complaint** | **weak — do not use** |
| Branch | — | +91 89402 56789 · **jayanagar@adgrohair.com** | confirmed |

**Email pattern confirmed chain-wide:** `<branch>@adgrohair.com`. Website page is thin, names no staff.

### Sibling branches already on file
[Karnataka Batches 1-2 Audit 23 Clinics.md](Karnataka Batches 1-2 Audit 23 Clinics.md) ~394–419: **Indiranagar** (+91 84978 56789)
and **HRBR Layout / Kalyan Nagar** (+91 84890 56789, hrbrlayout@adgrohair.com), with a validated
cross-branch wedge — *technician-led-not-doctor-led consultations*.

### Ads — **the chain advertises; Bangalore does not**
- **Meta `[META]`:** four live franchise pages found — **Rajahmundry** (AP), **Erode** (TN, WhatsApp
  CTA), **Trichy** (TN), **Ramanathapuram** (TN). **No Bangalore/Jayanagar page advertising.**
  ⚠️ *The artifact's "Meta active chain-wide" is true for the chain but does NOT evidence Bangalore spend.*
- **Google `[GADS]`:** only advertiser is **"Advanced GroHair & GloSkin – Theni"** (Tamil Nadu, 20 ads).
  Bangalore-specific spend: **undetermined.**

> Both platforms tell the same story: this chain's paid acquisition runs through **Tamil Nadu / Andhra
> franchise pages**, and the Bangalore branches are not visibly among them.

### Reviews `[GBP]`
| 5★ | 4★ | 3★ | 2★ | 1★ | ≤2★ |
|---|---|---|---|---|---|
| 104 | 7 | 1 | 1 | 5 | **5.1%** |

50% of negatives answered `[ART]`.
**Qualitative `[ART]` — not re-read first-hand:** two independent reviews describe **multi-session
packages abandoned mid-course with no follow-up**, consistent with the wedge already validated at the
other two branches.

```
funnel_break_stage:       Follow-up Persistence
recommended_entry_sku:    Follow-up and nurture engine — PROVISIONAL
confirm_via_mystery_shop: Same wedge as the sibling branches — treat as one chain conversation.
status:                   Qualified — merge into the Advanced Gro Hair chain dossier.
```

---

## Cross-batch patterns

**1. "Pay in full upfront, then silence" is the dominant failure.** Independently documented at
**Koza** (12+ session package → 4 sessions delivered; ₹11,800 taken, machine broken, refund refused),
**Sparha** (₹1L+, no callback for two months), **Sanssouci** (near-identical wording from unrelated
reviewers four years apart), and **Advanced GroHair** (packages abandoned mid-course). This is the most
repeated, most screenshot-provable failure in the batch — and it sits exactly where ValenceOps sells.

**2. Star ratings hide it; distributions expose it.** Koza Jaya Nagar reads 3.8★ but is **27.3%
one-star**. Sparha reads 4.2★ but is **18.8% ≤2★**. Sanssouci reads 4.2★ but is **17.6%**. Never quote
the headline rating.

**3. Clinics answer praise and ignore complaints.** Koza replies warmly to 4★ reviews while leaving
almost every 1★ unanswered, including one from two days ago. Sanssouci answered every negative until
~2022 and has answered none of its last three. The reply machinery exists; it is aimed at the wrong reviews.

**4. Ad "counts" mean nothing without dates.** Skin and Recon showed "10 ads" — all ended 8 Apr. Koza
showed "1 ad" — from Aug 2025. Only `lastShown` per creative tells you anything.

**5. WhatsApp is where the money lands.** Koza (2 of 5 live Meta ads), Sanssouci (2 of 4), and
Contour's IG CTA all route there. Mystery-shop the WhatsApp path, not the phone line.

**6. Two clinics already have vendors.** Sanssouci pays @ai.shikro; SkinFit markets itself as AI-driven.
Both are Park-tier and need framing against the incumbent, not a cold pitch.

**7. Aggregators can hold a different reality.** Koza Arekere shows **208 reviews on JustDial vs 2 on
Google**. Check both before judging a clinic's reputation.

---

## Batch comparison CSV

```csv
clinic_name,branch,locality,contact_name,contact_role,contact_confidence,phone,email,instagram,website,rating,reviews_total,pct_2star_or_below,meta_ads,google_ads,funnel_break_stage,recommended_entry_sku,wedge_state,status,unverified_fields
Contour Cosmetic Clinic,-,BTM/Hulimavu,Dr. Saket Jha,founder/medical director,confirmed,+918660432589,saket@contourcosmeticclinic.com,contour_hair,contourcosmeticclinic.com,4.8,334,1.2,active_2_ads,active_4_ads,Reactivation,Dead-lead reactivation,PROVISIONAL,Qualified-P1,
Contour Cosmetic Clinic,-,BTM/Hulimavu,Dr. Akanksha Jha,chief surgeon,confirmed,+918660432589,contact@contourcosmeticclinic.com,drakanksha.jha,contourcosmeticclinic.com,4.8,334,1.2,active,active,Reactivation,Dead-lead reactivation,PROVISIONAL,Qualified-P1,personal_email
Koza Aesthetic Care,Jaya Nagar,Jayanagar,,,none_found,+919606009079,kozaaestheticcare@gmail.com,not_found,kozacare.org,3.8,44,27.3,active_5_ads_whatsapp,dormant_since_2025-08,Follow-up Persistence,Follow-up and nurture engine,PROVISIONAL,Qualified-P2,founder;instagram;electronic_city_branch
Koza Aesthetic Care,Arekere,Arekere,,,none_found,+919606009079,kozaaestheticcare@gmail.com,not_found,kozacare.org,5.0,2,,active,dormant,Follow-up Persistence,Follow-up and nurture engine,PROVISIONAL,Qualified-P2,founder
Koza Aesthetic Care,HRBR Layout,Kalyan Nagar,,,none_found,+919606009079,kozaaestheticcare@gmail.com,not_found,kozacare.org,4.6,9,,active,dormant,Follow-up Persistence,Follow-up and nurture engine,PROVISIONAL,Qualified-P2,founder
Koza Aesthetic Care,Banashankari,Banashankari,,,none_found,+919606009079,kozaaestheticcare@gmail.com,not_found,kozacare.org,5.0,20,,active,dormant,Follow-up Persistence,Follow-up and nurture engine,PROVISIONAL,Qualified-P2,founder
Koza Aesthetic Care,Sarjapur Road,Kaikondrahalli,,,none_found,,kozaaestheticcare@gmail.com,not_found,kozacare.org,,,,active,dormant,Follow-up Persistence,Follow-up and nurture engine,PROVISIONAL,Qualified-P2,founder;phone;reviews
SS Aesthetic Clinic,-,Indiranagar,Mrs. Shylaja B.S.,founder,confirmed,+919113276518,ssaesthetics0825@gmail.com,ss_aesthetics_indiranagar,ssaesthetics.in,5.0,43,0.0,none_found,active_since_2026-07-28,Response Speed,Speed-to-lead audit,PROVISIONAL,Qualified-P3,personal_linkedin
SS Aesthetic Clinic,-,Indiranagar,Mrs. Suchitra B.S.,co-founder,confirmed,+919113276518,ssaesthetics0825@gmail.com,ss_aesthetics_indiranagar,ssaesthetics.in,5.0,43,0.0,none_found,active,Response Speed,Speed-to-lead audit,PROVISIONAL,Qualified-P3,personal_linkedin
Sanssouci Wellness Clinic,-,Mysuru,,,none_found,+919611211581,contactus@sanssouciwellness.com,sanssouci_wellness.mysuru,sanssouciwellness.com,4.2,148,17.6,active_4_ads_whatsapp,none_found,Reactivation,Dead-lead reactivation,PROVISIONAL,Qualified-Park-shallow-automation,founder;agency_incumbent_ai.shikro
Sparha Advanced Aesthetic Studio,-,Indiranagar,Arti Singh,founder and CEO (aesthetician - NOT a doctor),confirmed,+919972719303,info.sparha@gmail.com,sparha.aesthetic.studio,sparha.in,4.2,352,18.8,active_3_ads,active_961_days,Quote Chase,Quote-decay follow-up,PROVISIONAL,Qualified-FLAGGED,personal_email;no_named_surgeon
Feather Touch Aesthetic Clinic & Academy,Jayanagar,Jayanagar,,,none_found,+919900983048,,feather_touch_aesthetic_clinic,none,4.8,803,4.0,none_found,none_found,Post-consult,Founder-capacity protection,PROVISIONAL,Park-medium,founder;website_absent;negative_text_not_read
Feather Touch Aesthetic Clinic & Academy,Mysore,Mysuru,,,none_found,+919902250038,,feathertouchclinicmysore,none,,,,none_found,none_found,Post-consult,Founder-capacity protection,PROVISIONAL,Park-medium,founder
Skin and Recon,-,Jayanagar,Dr. Shruthi Chikkaiah,chief dermatologist (also HOD Dermatosurgery at Cutis),confirmed,+916361417399,skinandrecon@gmail.com,skinandrecon,skinandrecon.in,4.9,242,2.9,none,dormant_since_2026-04-08,Reactivation,Dead-lead reactivation,PROVISIONAL,Qualified,personal_email
Skin and Recon,-,Jayanagar,Dr. Rakesh Koudki,plastic surgeon,confirmed,+916361417399,skinandrecon@gmail.com,skinandrecon,skinandrecon.in,4.9,242,2.9,none,dormant,Reactivation,Dead-lead reactivation,PROVISIONAL,Qualified,personal_email;linkedin_url
SkinFit Wellness,-,Koramangala,Dr. Ruby Sachdev,named as clinical principal by clinic site only,likely,+919187967633,info@skinfitwellness.in,not_found,skinfitwellness.in,4.9,120,2.5,none,none,Reviews,Review reactivation agent,PROVISIONAL,Qualified-Park-shallow-automation,instagram;founder_affiliation_unconfirmed;skinnfit_medspa_overlap
RUA Skin & Hair Center,Ramamurthy Nagar,Ramamurthy Nagar,Dr. Jeevith/Dr. Eshritha/Dr. Jatin,co-principal dermatologists,confirmed,+919959763678,,ruaskinandhair,ruaskinandhair.com,4.9,80,0.0,active_1_ad,none_found,Reactivation,Dead-lead reactivation,PROVISIONAL,Qualified,email;personal_linkedin
RUA Skin & Hair Center,Indiranagar,Indiranagar,Dr. Jeevith/Dr. Eshritha/Dr. Jatin,co-principal dermatologists,confirmed,+917019976689,,ruaskinandhair,ruaskinandhair.com,5.0,17,0.0,active,none_found,Reactivation,Dead-lead reactivation,PROVISIONAL,Qualified,email;personal_linkedin
Advanced GroHair GloSkin,Jayanagar,Jayanagar,Karthik,branch manager,weak,+918940256789,jayanagar@adgrohair.com,not_found,advancedgrohair.in,4.7,118,5.1,none_in_bangalore,undetermined,Follow-up Persistence,Follow-up and nurture engine,PROVISIONAL,Qualified-merge-into-chain,founder;google_ads_bangalore_specific;negative_text_not_read
```

---

## Limitations — what is still NOT verified

| Gap | Detail |
|---|---|
| **Mystery shop — all 10** | Not run. Every wedge PROVISIONAL. Tilak runs this personally. |
| **Founder-direct emails** | Email-search run on 5 founder profiles; **only 1 returned an address** (Dr. Saket Jha). Akanksha Jha, Ruby Sachdev, Shruthi Chikkaiah and Arti Singh returned empty. For those four, the front desk is still the only channel. |
| **Personal LinkedIn — 5 founders unlocated** | Shylaja & Suchitra B.S., the three Rua dermatologists, Dr. Rakesh Koudki. Needs the LinkedIn **name-search** actor — capped (below). |
| **LinkedIn name/company-search actors capped** | `harvestapi/linkedin-company-employees` returned `SUCCEEDED` with **0 items** and `statusMessage: "free user run limit exceeded"`. Koza's founder was the target. Actor-level daily cap, separate from account credit — **retry tomorrow.** The direct-URL profile scraper is a different actor and is **not** capped. |
| **Koza founder + Instagram** | Unresolved. `/aboutus` 404s; `koza.care` DNS-fails; guessed IG handles dead. FB page + the new gmail are the only channels. |
| **Feather Touch founder** | Unresolved. No website. Directory names uncorroborated → `weak`, unusable. Needs a Deep-mode IG contact-graph pass. |
| **SkinFit Instagram + identity** | No handle found. **SkinFit Wellness ↔ Skinnfit Medspa relationship unresolved and material** — see §8. |
| **Negative review text — 4 clinics** | Read first-hand for **Sparha, Sanssouci, Koza Jaya Nagar** (the three worst performers, where the wedges live). **Not** read for **Feather Touch (30 one-stars)** or **Advanced GroHair (5)** — their qualitative sections remain `[ART]`. Contour (4 negatives), Skin and Recon (7) and Rua (0) were skipped deliberately: too few to carry a wedge. **All 10 star distributions are verified.** |
| **Review recency windows** | 90/180-day segmentation not computed; last-review-gap figures carried from the artifact. Totals cross-checked and matched on all 10. |
| **Google Ads by domain** | The `domains` parameter on `scrapesage/google-ads-transparency-scraper` is a **silent no-op** — 0 items twice, once in 1.6s without running. Only short brand stems resolve. So **"no advertiser record" ≠ proof of no spend** for Rua, Feather Touch, Sanssouci, SkinFit. |
| **Advanced GroHair Bangalore spend** | Undetermined on Google; **no Bangalore Meta page found**, only four out-of-state franchise pages. |
| **Aggregator Prime/sponsored badging** | Presence confirmed — Sparha and Skin and Recon on Practo; Koza (3 branches) and Feather Touch on JustDial+Practo. **Paid-tier badging not verified for any clinic** — per skill, `undetermined`, never inferred. Contour, SS Aesthetic, Rua, SkinFit not found on either aggregator. |
| **Koza Electronic City branch** | Still unconfirmed. Sarjapur Road found instead. |
| **Sanssouci address** | GBP says Ballal Circle / Krishnamurthy Puram; own site says Kalidasa Road flagship. Unresolved. |
| **Allegation status** | The consent, no-doctor-present and review-deletion accounts in §5 and §4 are **allegations by individual reviewers**, reported because they are public, specific, and corroborated in shape across two clinics. They are **not established fact** and must never appear in outbound copy. |

### Name-collision decoys correctly excluded
Feather Touch Tissues · Feather Touch Trading Company · The Feather Touch (Ireland) · Feather Touch
Nails and Lashes (Jayanagar nail salon) · SkinFit and Wellness (Temecula, CA) · SSKIN Aesthetics Ltd
(Malta) · Sanssouci ITSM GmbH (Germany) · Olena Kozachenko / Paweł Kozak-Raszkowski / Imelda Kozaly /
George Kozarov · Advanced GroHair & GloSkin **Theni / Rajahmundry / Erode / Trichy / Ramanathapuram** ·
Nilam Plastic and Cosmetic Clinic · Arogyavardhini Ayurveda · Grand Seiko India · Nirvana by SS ·
Magical Jar Organics · Abode Handicrafts · Aara's terracotta jewellery · Everlasting · Deconstruct
Skincare · HyugaLife · **Sparsha Skin Care Clinic** (Pavagada/Tumkur — already in batch1-2, unrelated
to Sparha) · **Contura Clinic** Kalyan Nagar (unrelated to Contour).
