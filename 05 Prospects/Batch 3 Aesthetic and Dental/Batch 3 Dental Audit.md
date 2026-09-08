---
date_created: 2026-08-03
date_modified: 2026-08-03
status: reference
---
# Batch 3 Audit — Bangalore Dental Cohort (11 clinics, 14 locations)

**Compiled:** 2026-07-30 · **Depth mode:** Standard (partial — see Limitations)
**Pipeline:** `apify/instagram-profile-scraper` · `compass/crawler-google-places` · `scrapesage/google-ads-transparency-scraper`
**Mystery shop:** PENDING on all — user to run. Every wedge below is PROVISIONAL.

> ⚠️ **Batch incomplete.** Apify free-tier credit exhausted mid-run. Meta Ads was **never checked**
> for any clinic in this batch, and the 8 skin/aesthetic clinics have **no GBP data at all**.
> See Limitations at the end. Do not read "no ads" anywhere below as verified — only Google Ads
> was checked.

---

## Excluded before enrichment — out of state (3)

Their own Instagram bios place them outside Karnataka. Excluded to avoid spending on out-of-scope
leads; confirm if you want them researched anyway.

| Clinic | Own bio states | Founder (from bio) |
|---|---|---|
| Skin Aesthete | 📍 Navi Mumbai | @dr_sonalahuja |
| Aisri Cosmetic Clinic | 📍 Warangal (Telangana) | @akshitha_aroori1111, co-founder @dr.kavyadsp |
| SkinRx Clinix / Dr K Pratyusha | Kukatpally, **Hyderabad** | Dr K Pratyusha, MBBS MD DVL |

---

## Name-collision decoys correctly excluded

Surfaced by the 2-places-per-search setting; **not** the target clinics:

- **Aspen Dentals** — Gurugram, **Haryana** (4.9★/299). Distinct from Aspen Dental Care, RT Nagar.
- **Saumitras The Dental Axis** — Varanasi, **Uttar Pradesh** (4.9★/934). Distinct from The Dental Axis, Horamavu.
- **Chisel Dental Care** — Kattigenahalli (4.6★/80), separate business from Chisel Dental Clinic, Koramangala.
- **Smiley Dental Care** — LBS Nagar (4.7★/110), separate from Smiley House, Horamavu.
- **Smile Center Multispeciality** — Koramangala (5.0★/119), separate from Smile Xpressions.

---

## 1 · Chisel Dental Clinic

**Basic Info** — 18, 1st Main Rd, 1st Block Koramangala, Bengaluru 560034 · Dental clinic
**Contacts** — 📞 +91 99721 17009 · ✉️ chiseldentalclinics@gmail.com · chiseldental.co.in · FB /chiseldental · IG @chiseldentalclinic (1,777 followers, 63 posts)
**Contact confidence** — `generic` / clinic-level only, **no named founder found** (`weak`). No LinkedIn on listing.

**Digital Presence** — IG bio claims "No.1 Dental Clinic in Bangalore", "1,00,000+ Happy Patients", "4.8⭐ rating on Google". Actual GBP is **4.7★** — minor self-overclaim, worth knowing before quoting their own numbers back.

**Ads** — Google Ads: **none found**. Meta: `not_run`.

**Reviews Analysis** — **4.7★ / 2,981 total** (5★ 2,689 · 4★ 89 · 3★ 18 · 2★ 15 · 1★ 170)
- All-time ≤2★: 185 (6.2%)
- 80 newest pulled: **all 80 fall within 90 days** → extremely high review velocity
- **Negatives in the recent 80: zero.** Newest review 2026-07-30 (same-day)
- Read: the 170 one-stars are historical, not current. Recent reputation is clean.

**Marketing Analysis** — Highest review volume in the batch by 2.5x, with velocity to match. Nothing visibly broken from public data. This is the profile most likely to be a §1.1 #9 candidate (passes everything) — only the mystery shop can tell.

```
funnel_break_stage:       undetermined — no public break visible
recommended_entry_sku:    Instant response + organic capture — PROVISIONAL (weak basis)
confirm_via_mystery_shop: If response is slow → §3 row "No ads · website ✓ · high reviews · slow or
                          no response". If fast → run the §2 six-test SOP; genuine hard-kill #9 risk.
status:                   Qualified — low confidence, needs mystery shop to find any break
```

---

## 2 · Sky Dental Clinic

**Basic Info** — 618, 80 Feet Rd, 4th Block Koramangala, Bengaluru 560034 · Dentist
**Contacts** — 📞 +91 93532 48386 · IG @_sky_dental_clinic_ (4,264 followers, 255 posts) · website is a **zoca.com third-party booking page**, not an owned site
**Contact confidence** — `generic` (`weak` — no named doctor anywhere in bio, GBP, or listing)

**Digital Presence** — IG bio claims **4 branches**: Koramangala, RR Nagar, Kothanur, Sahakar Nagar. **GBP search returned only Koramangala** — the other 3 branches were not captured and are unaudited.

**Ads** — Google Ads: **none found**. Meta: `not_run`.

**Reviews Analysis (Koramangala only)** — **4.9★ / 826 total** (5★ 783 · 4★ 23 · 3★ 1 · 2★ 1 · 1★ 18)
- All-time ≤2★: 19 (2.3%)
- 80 newest: 52 within 90 days, 80 within 180 days. Newest 2026-07-30
- **1 negative in the pull, replied.** July 2026 — a detailed complaint about a wisdom-tooth extraction outcome; clinic responded.

**Marketing Analysis** — Strong reputation, real velocity, and 4 locations — but no owned website (booking runs through a third-party page) and no named decision-maker discoverable publicly. The front-desk-only-contact park route (§1.2) may apply.

```
funnel_break_stage:       undetermined — needs mystery shop
recommended_entry_sku:    Instant response + organic capture — PROVISIONAL
confirm_via_mystery_shop: Response speed across the 4 branches; also test IG DM vs WhatsApp
                          (§3 "WhatsApp fast · Instagram DMs slow → IG→WhatsApp handoff").
status:                   Qualified · 3 of 4 branches unaudited
```

---

## 3 · Dr Tanisha's Emerge Dental Studio

**Basic Info** — 1st floor, 7th Main Rd, HAL 2nd Stage, Indiranagar, Bengaluru 560038 · Dentist
**Contacts** — 📞 +91 82968 01240 (same number in IG bio and GBP — cross-corroborated) · emergedentalstudio.com · IG @emergedentalstudio (141 followers, 108 posts)
**Founder** — **Dr. Tanisha Kaulavkar, MDS, Prosthodontist & Implantologist** — named in her own IG bio. Confidence: `confirmed` (clinic account names her; GBP title is "Dr Tanisha's Emerge Dental Studio").

**Digital Presence** — IG bio's link is a **Google Form** for appointments, not a booking system. 141 followers is very thin for a clinic running paid search.

**Ads** — **Google Ads: 10 active/recent** (advertiser `AR05362007493549490177`). Meta: `not_run`.

**Reviews Analysis** — **5.0★ / 152 total** (5★ 151 · 4★ 1 · zero 3★/2★/1★)
- All-time ≤2★: **0 (0%)** — a genuinely spotless record
- 80 newest: 13 within 90 days, 18 within 180 days. Newest 2026-07-13
- Velocity is modest (13/90 days) relative to running 10 ads

**Marketing Analysis** — Paying for Google traffic into a funnel with a Google Form as the booking mechanism and 141 IG followers. Perfect reputation, thin capture infrastructure. The gap is between ad click and booked chair.

```
funnel_break_stage:       Response Speed
recommended_entry_sku:    Dead-lead reactivation — PROVISIONAL
confirm_via_mystery_shop: Basis is 10 live Google Ads + a Google-Form booking path. If the form/DM
                          reply is fast → redirect to "Follow-up and nurture engine" (§3 row 2).
status:                   Qualified — strong fit (solo founder, confirmed, ads running)
```

---

## 4 · Aspen Dental Care

**Basic Info** — 1st Floor, Jalaram Mall, 80 Feet Rd, RT Nagar, Bengaluru 560032 · Dentist
**Contacts** — 📞 +91 97412 24772 · ✉️ info@aspendentalcare.in · aspendentalcare.in · IG @aspendentalcare (178 followers, **empty bio**) · FB /AspenDentalCareBangalore
**Founder** — **Dr. Pramod Pillai** — LinkedIn `linkedin.com/in/dr-pramod-pillai-8905356a`, found **on the clinic's own GBP listing**, and named repeatedly in reviews as the trusted primary dentist. Confidence: `confirmed`.

**Digital Presence** — Instagram bio is completely empty; 178 followers.

**Ads** — Google Ads: **none found**. Meta: `not_run`.

**Reviews Analysis** — **4.8★ / 185 total** (5★ 172 · 4★ 6 · 3★ 0 · 2★ 0 · 1★ 7)
- All-time ≤2★: 7 (3.8%)
- 80 newest: 13 within 90 days, 25 within 180 days. Newest 2026-07-29
- **2 negatives in the pull, 1 of 2 replied**

Two distinct, quotable complaint shapes:
- **Doctor-substitution without notice** (1★, 2026-07-22, *replied*): a long-term patient booked assuming Dr. Pillai would perform their extraction, and was told **one hour before surgery** it would be someone else.
- **Refusal to quote any price by phone** (1★, 2024-12-04, **no reply**): quotes the dentist as saying *"I'm not selling you tomatoes to give you a price, I'm selling you services. I need you to come to the clinic to tell a price."* Reviewer reads it as a tactic to force a visit.

**Marketing Analysis** — Reputation rests heavily on one named doctor, and the sharpest complaint is that patients can't get a price without physically attending. That's a qualification/quote-stage break, and it's screenshot-provable.

```
funnel_break_stage:       Quote Chase
recommended_entry_sku:    Quote-decay follow-up — PROVISIONAL
confirm_via_mystery_shop: Ask for a price on a high-ticket procedure (implant/aligners) by phone or
                          DM. If they refuse to quote and nobody follows up → confirmed. If they
                          quote then go silent → same SKU, stronger evidence.
status:                   Qualified — founder confirmed with direct LinkedIn
```

---

## 5 · Reneu Dental Studio

**Basic Info** — 2nd Floor, 172/2, Horamavu Main Rd, Kallumantapa, Horamavu, Bengaluru 560113 · Dental clinic
**Contacts** — **No phone on GBP.** GBP "website" field contains only their **Instagram URL** — no owned site. IG @thereneu_dental (122 followers, 20 posts)
**Contact confidence** — `weak` — no named doctor anywhere. Bio says only "Intl. Certified Doctors".

**Digital Presence — two concrete anomalies:**
- The WhatsApp link in their IG bio is a **US number** (`wa.me/17306636247`, `countryName=US`) for a Horamavu, Bangalore clinic — almost certainly a setup error sending enquiries into a dead or wrong channel.
- 20 posts total, 122 followers — barely-established presence.

**Ads** — Google Ads: **none found**. Meta: `not_run`.

**Reviews Analysis** — **5.0★ / 16 total** (all 16 five-star, zero negatives)
- **Newest review 2026-09-09... no: 2025-09-09 — approximately 10.7 months stale**
- **Zero reviews in the last 90 days. Zero in the last 180 days.**
- 16 reviews with a 5.0★ average and a 10-month gap is a very thin, possibly dormant footprint.

**Marketing Analysis** — This is the weakest lead in the dental cohort. Three separate hard-kill risks that public data can't settle: possible **#2 (operating <12 months)** — 16 reviews and a 10-month stall are consistent with either a new clinic or a stalled one; possible **#3 (inbound <20/month)**; and no reachable named decision-maker (**§1.2 park**).

```
funnel_break_stage:       Reviews (proof engine stalled ~10.7 months)
recommended_entry_sku:    Review reactivation agent — PROVISIONAL
confirm_via_mystery_shop: First verify it's actually operating and >12 months old before spending
                          effort. Also test whether the US WhatsApp number in bio reaches anyone.
status:                   Park — thin footprint, no named contact, hard-kill #2/#3 undetermined
```

---

## 6 · Smiley House (Multi Speciality Dental Clinic)

**Basic Info** — 1st Floor, 22, Jayanti Nagar Main Rd, Horamavu, Bengaluru 560016 · Dental clinic
**Contacts** — 📞 +91 99649 55533 · IG @smileyhouseclinic (**49 followers**, 65 posts)
**Contact confidence** — `weak` — no named doctor in bio, GBP, or listing.

**Digital Presence — placeholder artifact (verified, not a scraper error):** the GBP website field is an unresolved **bit.ly shortlink** (`bit.ly/2K6fhzb`). Because it never resolves to their own domain, contact enrichment returned **`instagram.com/bitly`, `facebook.com/bitly`, `linkedin.com/company/bitly`** — Bitly's own corporate accounts. Anyone clicking through their Google listing's social links lands on Bitly, not the clinic. Same class of unconfigured-link failure as the Wix/ThemeRex cases in prior batches.

**Ads** — Google Ads: **none found**. Meta: `not_run`.

**Reviews Analysis** — **5.0★ / 555 total** (5★ 541 · 4★ 9 · 3★ 1 · 2★ 1 · 1★ 3)
- All-time ≤2★: 4 (0.7%) — near-spotless at real volume
- 80 newest: **40 within 90 days**, all 80 within 180 days. Newest 2026-07-25
- **Zero negatives in the recent 80.**

**Marketing Analysis** — Genuinely strong operation (555 reviews at 5.0★, 40 in 90 days) with a 49-follower Instagram and a broken shortlink as its web presence. Reputation is being earned offline and captured nowhere. Note: presence-building is **not** a valid wedge (hard kill #7) — the bit.ly finding is evidence of neglect, useful as a credibility opener, not the offer.

```
funnel_break_stage:       undetermined — needs mystery shop
recommended_entry_sku:    Instant response + organic capture — PROVISIONAL
confirm_via_mystery_shop: 555 reviews at 5.0★ means demand is real; test whether inbound enquiries
                          get answered. Slow/no response → confirms this SKU.
status:                   Qualified · no named contact yet (§1.2 park route may apply)
```

---

## 7 · Small Bites — Kids-Only Dental Chain (2 of N branches captured)

**Basic Info** — Multi-branch pediatric dental chain. IG bio: *"India's first Kids-Only Dental Chain · Multiple locations across Bengaluru · Invisalign® First For Kids"*. **More branches exist than the 2 captured.**
**Contacts** — smallbites.in · IG @smallbites.in (5,007 followers, 1,165 posts) · FB /SmallBitesChildrenDentalClinic
**Founder** — **Dr. Premila Naidu** — LinkedIn `linkedin.com/in/dr-premila-naidu-786a8575`, found **on both branches' GBP listings**. Confidence: `confirmed`.

| Branch | Rating | Reviews | ≤2★ all-time | 90d | Neg 90d | Newest |
|---|---|---|---|---|---|---|
| Bhartiya City (Thanisandra) | 4.9★ | 198 | 1 (0.5%) | 24 | **0** | 2026-07-27 |
| Indiranagar / Domlur | 4.9★ | 495 | 4 (0.8%) | **57** | **0** | 2026-07-27 |

📞 Bhartiya City +91 89085 85089 · Indiranagar +91 99720 97815

**Reviews Analysis** — **Zero negatives in 80 pulled at either branch.** Indiranagar is running 57 reviews in 90 days — the second-highest velocity in the cohort. Both branches independently clean, which for a chain is a meaningful signal (chains usually diverge — Artistry Clinics ran 9.4% vs 13.3% across branches in batch 2).

**Ads** — Google Ads: **none found** under "Small Bites Dental". Meta: `not_run`.

**Marketing Analysis** — Best-run operation in the dental cohort on public evidence: real scale, 5,007 followers, confirmed founder with LinkedIn, zero recent complaints across two branches. Also the clearest ICP question: a multi-branch chain with a Pvt-Ltd-style footprint may trip hard kill #5 (no single decision-maker) — Dr. Naidu's LinkedIn suggests otherwise, but verify.

```
funnel_break_stage:       undetermined — no public break visible
recommended_entry_sku:    Instant response + organic capture — PROVISIONAL (weak basis)
confirm_via_mystery_shop: Nothing is visibly broken. Run the §2 six-test SOP rather than assuming a
                          wedge. Genuine hard-kill #9 candidate. Also confirm decision-maker
                          singularity (#5) given multi-branch structure.
status:                   Qualified — high value, low diagnosed break. Verify #5 and #9.
```

---

## 8 · Amaya Dental Clinic (2 branches)

**Basic Info** — Two Bangalore branches. amayadental.in · IG @amaya.dental (659 followers, 410 posts)
**Contact confidence** — `generic` — emails and phones per branch, **no named founder** found anywhere (`weak`).

| Branch | Rating | Reviews | ≤2★ all-time | 90d | Neg 90d | Newest | Contact |
|---|---|---|---|---|---|---|---|
| Sahakar Nagar | 5.0★ | 142 | **0 (0%)** | **2** | 0 | 2026-06-19 | +91 63666 14266 |
| Vasanth Nagar | 5.0★ | 270 | 2 (0.7%) | **6** | 1 (no text, **unreplied**) | 2026-07-19 | +91 95918 95500 · amayadental.ind@gmail.com |

**Ads** — **Google Ads: 100–200 active/recent** (advertiser `AR11045639696049766401`, "AMAYA DENTAL CLINIC"). **This is the largest ad volume in the entire batch.** Meta: `not_run`.

**Reviews Analysis** — Both branches at 5.0★ with essentially zero complaints. But review velocity is **the lowest in the cohort relative to spend**: 2 reviews in 90 days at Sahakar Nagar, 6 at Vasanth Nagar — while running 100–200 ads.

**Marketing Analysis — the sharpest quantified mismatch in this batch.** Somewhere between 100 and 200 live Google ads are driving traffic, and the clinic is generating 2–6 reviews per quarter per branch off it. Either the ads aren't converting to visits, or visits aren't converting to reviews. Both are proof-engine failures downstream of money already spent — exactly the §0 priority profile (closest to money spent, screenshot-provable).

```
funnel_break_stage:       Reviews
recommended_entry_sku:    Review engine first, infra second — PROVISIONAL
confirm_via_mystery_shop: Basis is 100–200 Google Ads against 2–6 reviews/quarter. If enquiry
                          response is also slow → redirect to "Dead-lead reactivation" (§3 row 1),
                          which outranks this on priority.
status:                   Qualified — strongest ad-spend signal in batch; no named contact yet
```

---

## 9 · Smile Xpressions Multispeciality Dental Clinic

**Basic Info** — 1st floor, Haralur Main Rd, Ambalipura, HSR Layout, Bengaluru 560103 · Dental clinic
**Contacts** — 📞 +91 89717 11617 (matches IG bio) · ✉️ smilexpressionsdentalclinic@gmail.com · smilexpressions.in
**Founder** — **Dr. Shagun Agarwal** — two Instagram accounts exist: `@drshagunagarwal` (on GBP listing) and `@drshagunagarwal_invisalign` (3,442 followers, the handle you supplied). Google Ads advertiser name is literally **"DR.SHAGUNS SMILE XPRESSIONS MULTI SPECIALITY DENTAL CLINIC"**. Confidence: `confirmed` (name appears in advertiser registration, GBP, and IG).

**Ads** — **Google Ads: 18 active/recent** (`AR15908331643434172417`). Meta: `not_run`.

**Reviews Analysis** — **4.9★ / 1,162 total** (5★ 1,115 · 4★ 11 · 3★ 1 · 2★ 2 · 1★ 33)
- All-time ≤2★: 35 (3.0%)
- 80 newest: **all 80 within 90 days** — very high velocity. Newest 2026-07-29
- **3 negatives in the recent 80 — only 1 of 3 replied**

**Recurring complaint shape — upselling pressure, from two independent reviewers weeks apart:**
- 1★, 2026-06-29, **no reply**: *"...I felt pressured into additional treatments such as alignment suggestions, cleaning, cavity fillings, and grinding/drilling that seemed more like upselling than necessary."*
- 1★, 2026-06-06, *replied*: went in for a routine checkup and cleaning, was told a tooth needed a root canal, said they'd never felt pain in it and asked to wait, and describes being pressured into it while alone.
- 1★, 2026-06-27, **no reply**: *"Don't go with positive reviews."*

**Marketing Analysis** — Highest-volume dental lead after Chisel, with real ad spend and a **repeated, independently-corroborated pattern** of patients feeling pushed into unnecessary treatment — plus 2 of 3 recent negatives left unanswered. The pattern repetition is what makes this credible rather than anecdotal.

```
funnel_break_stage:       Reviews
recommended_entry_sku:    Review engine first, infra second — PROVISIONAL
confirm_via_mystery_shop: 18 ads live + 2 of 3 recent negatives unanswered. If enquiry response is
                          slow → "Dead-lead reactivation" (§3 row 1) takes priority. If fast but
                          unqualified → "Follow-up and nurture engine".
status:                   Qualified — founder confirmed, ads confirmed, repeated complaint pattern
```

---

## 10 · The Dental Axis

**Basic Info** — Agara main road, 10th St, Babusapalya, Horamavu, Bengaluru 560113 · Dental clinic
**Contacts** — 📞 +91 63626 61757 · IG @the_dental_axis (**70 followers**, 38 posts)
**Founder** — **Dr. Bagyashree Rajamani** — named in the clinic IG bio ("Dr Bagyashree R"). Confidence: `likely` (own bio names her; no LinkedIn or independent corroboration found).

**Digital Presence — two verified findings:**
- GBP "website" is a **third-party booking platform page** (`click4appointment.com/clinic-details/thedentalaxis-3418`) — no owned domain.
- The email returned by contact enrichment is **`contactus@click4appointment.in`** — that's the **platform's** support address, not the clinic's. Do not use it as a contact.

**Ads** — **Google Ads: 9 active/recent** (`AR05568478614556508161`). Meta: `not_run`.

**Reviews Analysis** — **4.9★ / 43 total** (5★ 42 · 4★ 0 · 3★ 0 · 2★ 0 · 1★ 1)
- **Newest review 2026-02-18 — approximately 5.4 months stale**
- **Zero reviews in the last 90 days.** Exactly 1 in the last 180 days — and it's the negative one.
- The sole negative (1★, 2026-02-18, *replied*) alleges the reviews are inauthentic: *"I feel all the reviews are written by the clinic."* It also describes being told a tooth needed extraction rather than a root canal, then facing the same recommendation a year later.

**Marketing Analysis** — Running 9 paid Google ads while: review generation has been dead for 5.4 months, the only recent review is a fake-review allegation, Instagram has 70 followers, and there's no owned website or clinic email. Money is going out; nothing is being captured or proven. Small footprint but the break is unusually clear.

```
funnel_break_stage:       Reviews (proof engine stalled 5.4 months while ads run)
recommended_entry_sku:    Review engine first, infra second — PROVISIONAL
confirm_via_mystery_shop: 9 live ads + zero reviews in 90 days is the provable break. Confirm the
                          click4appointment booking path actually reaches the clinic — if enquiries
                          die there, redirect to "Dead-lead reactivation" (§3 row 1).
status:                   Qualified — small but clearest diagnosed break in the cohort
```

---

## 11 · Aesthete Lifestyle Dentistry (2 branches)

**Basic Info** — Two branches. lifestyledentistry.in · IG @aesthetelifestyledent (1,514 followers, 165 posts)
**Founders** — **Dr. Akshai and Dr. Ashish Shetty** ("The Shetty Twins", 3rd-generation practice per IG bio). The Residency Rd GBP listing is titled *"Aesthete Lifestyle Dentistry - Dr. Ashish & Akshay Shetty"* — clinic and listing both name them. Confidence: `confirmed`. No personal LinkedIn found.

| Branch | Rating | Reviews | ≤2★ all-time | 90d | Neg 90d | Newest | Contact |
|---|---|---|---|---|---|---|---|
| Residency Rd (Ashok Nagar) | 4.9★ | 72 | 2 (2.8%) | 9 | 0 | 2026-07-30 | +91 80 2221 2648 |
| HSR Layout | 4.9★ | 195 | 6 (3.1%) | 8 | 0 | 2026-07-30 | +91 80 2550 4231 · aesthetedent@gmail.com |

**Reviews Analysis** — **All 4 negatives across both branches were replied to (4/4).** That's the best review-response discipline in the dental cohort. Recent velocity is modest (8–9 per branch per 90 days).
- Notable 1★, 2025-12-19, *replied*: a measured complaint arguing the clinic should be clearer and more truthful about where its actual strengths lie, framing patients as paying customers investing time and money. Reasoned rather than angry — and answered.
- 1★, 2024-06-29, *replied*: felt the doctor was too busy with other patients to properly assist on a first visit for extraction + aligners.

**Ads** — Google Ads: **none found**. Meta: `not_run`.

**Marketing Analysis** — Well-run, answers its critics, decent following, positioned on high-ticket work (orthognathic surgery, Invisalign, makeovers). The visible gap is volume, not quality: 8–9 reviews per branch per quarter against a 3rd-generation reputation and 1,514 followers. Nothing is broken enough to diagnose from public data alone.

```
funnel_break_stage:       undetermined — needs mystery shop
recommended_entry_sku:    Quote-decay follow-up — PROVISIONAL
confirm_via_mystery_shop: High-ticket focus (orthognathic, Invisalign) makes quote-decay the most
                          likely break. Ask for a price on aligners/surgery, then go quiet and
                          count follow-ups. If nobody chases → confirmed.
status:                   Qualified — founders confirmed, strong reply discipline
```

---

## Limitations — what was NOT verified

| Gap | Reason |
|---|---|
| **Meta Ads — all 19 clinics** | Run **aborted**: "You've reached the maximum usage for your current billing cycle." No clinic in this batch has verified Meta ad status. Every "no ads found" above refers to **Google only**. |
| ~~**GBP + reviews — 8 skin/aesthetic clinics**~~ **RESOLVED 2026-08-03** | Originally never ran (credit exhausted). Rua Skin & Hair, Skin and Recon, Koza Aesthetic Care, Advanced GloSkin Jayanagar, SS Aesthetic, Contour Cosmetic, Sanssouci Wellness, SkinFit Wellness. **These 8 (plus Sparha and Feather Touch) have since been fully audited — GBP, contacts, founders, and ad activity — see [batch3-aesthetic-audit.md](batch3-aesthetic-audit.md).** |
| **Aggregator paid-listing check (Practo/JustDial)** | Never ran — credit. `undetermined` for all. |
| **Website content crawl** | Never ran — credit. Team/about pages unread, so no staff names beyond what bios and GBP gave. |
| **Sky Dental — 3 of 4 branches** | Only Koramangala captured by GBP search. |
| **Small Bites — branches beyond 2** | Bio says "multiple locations"; only Bhartiya City and Indiranagar captured. |
| **GBP batch A run status** | `FAILED` at 360s, but wrote all 5 target clinics before failing — coverage verified manually, not assumed. |
| **Founder identity — 5 clinics** | Chisel, Sky Dental, Smiley House, Amaya (both branches) have **no named decision-maker** discoverable from public data. §1.2 front-desk-only park route may apply. |
| **Hard kills #3, #4, #6, #8** | Not scrapable — `undetermined` for every clinic, as always. |
| **Hard kill #2 (Reneu)** | Cannot confirm whether under 12 months old; 16 reviews with a 10.7-month stall is ambiguous. |
