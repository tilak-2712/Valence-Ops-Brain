---
date_created: 2026-08-08
date_modified: 2026-08-13
status: active
---
# Pre-Outbound Research — Full Batch Report

> *(⚠️ Retired tests: the six-test SOP was cut to two — qualification and quote decay — on 2026-08-13. Persistence, after-hours, cross-channel and booking friction no longer run. See `wedge-signal-entry.md` §2.)*


> ⚠️ **PRE-SHOP RECORD — live state is in Notion, not here.** This dossier was written before the
> mystery shop ran. This cohort is tracked in Notion as **"Batch 2"**
> (`collection://754da695-40e4-839a-a0e7-07e28a0a27d8`), where the `Mystery shop status`, `Wedge` and
> `Notes` fields carry the shop transcript, timestamps, the confirmed wedge and the next action.
> **Read the Notion row before drafting anything for this clinic.** Where the two disagree, Notion wins.
> Any `recommended_entry_sku: … PROVISIONAL` line below may already have been confirmed or redirected.

## Go List — 10 Skin/Hair Clinics · Bangalore

**Research date:** 2026-08-08
**Pipeline:** `clinic-audit-research` (Apify)
**Depth mode:** Standard, all 10 clinics
**Clinics researched:** 10 · **Locations audited:** 12 (2 clinics are 2-branch chains: Haircosmos International, Akera Health)
**Outcome:** 10 Qualified · 0 Park · 0 Disqualified

> **This batch is provisionally complete, not decision-ready.**
> The Go/No-Go gate cannot be satisfied by scraped data alone — it requires the mystery shop, which this pipeline never runs (the user does that personally). Every `recommended_entry_sku` below is a **data-backed hypothesis marked PROVISIONAL**, with an explicit note on what mystery-shop finding would confirm or redirect it.

---

## Table of contents

1. [How to read this report](#1-how-to-read-this-report)
2. [Method and verification standard](#2-method-and-verification-standard)
3. [Batch at a glance](#3-batch-at-a-glance)
4. [Priority queue — who to shop first, and why](#4-priority-queue--who-to-shop-first-and-why)
5. [Batch comparison table](#5-batch-comparison-table)
6. Full clinic dossiers
   - [6.1 Gejje's Marvella](#61-gejjes-marvella)
   - [6.2 Haircosmos International (2 branches)](#62-haircosmos-international--2-branches)
   - [6.3 Ara Skin Clinic](#63-ara-skin-clinic)
   - [6.4 Dr. Priya's Skin & Hair Clinic](#64-dr-priyas-skin--hair-clinic)
   - [6.5 Akera Health (2 branches)](#65-akera-health--2-branches)
   - [6.6 Derma Solutions](#66-derma-solutions)
   - [6.7 Routines by Dr. Apoorva](#67-routines-by-dr-apoorva)
   - [6.8 Theory of Skin](#68-theory-of-skin)
   - [6.9 Dermatonik](#69-dermatonik)
   - [6.10 VIDA Skin & Hair Transplant Clinic](#610-vida-skin--hair-transplant-clinic)
7. [Cross-batch patterns](#7-cross-batch-patterns)
8. [Corrections made during self-review](#8-corrections-made-during-self-review)
9. [Limitations — what was not verified](#9-limitations--what-was-not-verified)
10. [Tool health notes for the next batch](#10-tool-health-notes-for-the-next-batch)
11. [Data provenance](#11-data-provenance)
12. [Recommended next actions](#12-recommended-next-actions)

---

## 1. How to read this report

### Contact confidence labels
Every named contact carries one of four labels. A name match alone is never treated as confirmation.

| Label | Meaning |
|---|---|
| **confirmed** | The clinic's own channel (IG bio, website, or LinkedIn) names this person in this role, or their own profile names the clinic |
| **likely** | Corroborated by role, credential, email domain, or ad-account name — but not stated cleanly on both sides |
| **weak** | Name matches only (e.g. supplied in the user's brief but not independently found this session) |
| **not_found** | No named human was discoverable through any source checked this session |

### Ad-status values
| Value | Meaning |
|---|---|
| **N active** | Ads confirmed running, verified against the clinic's own page/domain this session |
| **N, inactive since [date]** | Ads confirmed to have run historically, confirmed stopped, with a date |
| **0 found / 0 active** | Checked the clinic's own page/domain directly and found nothing |
| **undetermined** | No confirmable page/domain existed to check directly, or the check returned only unrelated results |

`undetermined` is **not** the same as "no ads." Two ad-related corrections had to be made mid-batch this session — see §8.

### Funnel break stages
Drawn strictly from the wedge playbook §4 enum: `Response Speed` · `Qualification` · `Follow-up Persistence` · `Quote Chase` · `Booking / No-show` · `Post-consult` · `Reviews` · `Reactivation` · `None (pass)`.

### Wedge names
Every `recommended_entry_sku` is quoted verbatim from the playbook's §3 routing table. No wedge names were invented for this batch.

### A note on review quotes
Google reviews contain real patients' names and medical details. Quotes below are **minimized deliberately** — they carry only what establishes the *business* finding. Reviewer names are omitted throughout this report; clinical specifics are reduced to the minimum needed to convey severity. Where an allegation is serious, it is stated as an allegation and surfaced prominently rather than smoothed into surrounding prose.

---

## 2. Method and verification standard

### What was run
| Step | Actor | Coverage |
|---|---|---|
| GBP + reviews + contact enrichment | `compass/crawler-google-places` | 2 batched runs, 12 places returned (7+5 search terms), 120 newest reviews pulled per place |
| Instagram profile refresh | `apify/instagram-profile-scraper` | All 10 handles — bio, followers, posts, external URL |
| Meta ads (keyword sweep, then corrected) | `apify/facebook-ads-scraper` | All 10 clinics via keyword search first; **8 re-run against confirmed Facebook Page URLs** after the keyword sweep proved unreliable (see §8) |
| Google Ads Transparency (name mode, then corrected) | `scrapesage/google-ads-transparency-scraper` | All 10 via brand-name query first; **9 re-run by domain** after name-mode resolved only 1 of 10 (see §8) |
| Aggregator (Practo) paid-listing check | `apify/rag-web-browser` (site-scoped search) | All 10 clinics |
| Website team/about/contact crawl | `apify/website-content-crawler` | All 10 domains, 48 pages captured (all homepages + linked pages) |
| LinkedIn person (direct URL) | `harvestapi/linkedin-profile-scraper` | 2 of 10 — the only two clinics where GBP's contact enrichment surfaced a usable direct LinkedIn URL |
| LinkedIn person (name search) | Not run this session | Not prioritized against the daily free-tier cap; the 2 direct-URL pulls above were free of that cap and preferred |

### Actor-health preflight (run before spending)
All actors confirmed live and non-deprecated before the batch started. Success rates at time of check: `compass/crawler-google-places` 90%, `apify/facebook-ads-scraper` 99.2%, `scrapesage/google-ads-transparency-scraper` 99.4%, `apify/instagram-profile-scraper` 99.4%, `apify/website-content-crawler` 96.6%. No fallback actor substitution was needed.

### The six-point verification loop, applied after every call
An Apify `SUCCEEDED` status means "the code exited," not "the data is real." Each run was checked for:

1. **Coverage** — item count vs. inputs submitted. Both GBP batches returned full coverage (7/7, 5/5). The website crawl's *first* attempt under-covered badly (6 of 10 sites, because `maxCrawlPages` is a **global** cap across all start URLs, not per-site as assumed) — caught and re-run at a higher cap, recovering all 10.
2. **Error/summary key-value records** — read where present (e.g. the Google Ads `STATE` record, which confirmed only 1 of 10 name-mode queries had actually resolved to an advertiser, rather than trusting the dataset count alone).
3. **Full `statusMessage`** — read on every run; no silent free-tier cap hits occurred this session (the LinkedIn name-search cap that has bitten prior batches was avoided by using direct-URL pulls instead).
4. **Field completeness with quirk awareness** — e.g. one Akera Health Meta ad legitimately renders `{{product.brand}}` as body text (a dynamic/catalog-ad placeholder, not broken data); Ara Skin Clinic's GBP contact enrichment surfaced a Wix-style placeholder email (`info@domainname.com`) alongside a real one, reported as a finding rather than dropped.
5. **Cross-source corroboration** — IG follower counts vs. the user's supplied brief matched almost exactly for all 10 clinics (a good trust signal on both the brief and this session's pulls). GBP-surfaced websites corrected three clinics the original brief had listed as having no website (Derma Solutions, Routines by Dr. Apoorva, Theory of Skin) — see §8.
6. **Manual tie-break on load-bearing/reversing claims** — applied twice this session, both documented in §8: the Meta ads keyword-search false positives, and Ara Skin Clinic's Google Ads attribution to an unrelated-looking advertiser name.

---

## 3. Batch at a glance

- **10 clinics, 12 audited locations** (Haircosmos International and Akera Health are each 2-branch).
- **10 Qualified, 0 Park, 0 Disqualified.** No clinic hit a Phase 6 hard-kill; no clinic met 2+ of the "do not pursue as standard lead" escalation criteria (one clinic, Derma Solutions, meets 1 of 3 — see its dossier — which per the playbook earns a caveat, not a flag).
- **Confirmed founder/operator contact:** 6 of 10 clinics (Ara Skin, Dr. Priya's, Derma Solutions, Routines, Theory of Skin, VIDA). **No individual named anywhere:** Haircosmos International, Akera Health. **Likely but unconfirmed:** Gejje's Marvella (brief-supplied name only), Dermatonik (business-side owner inferred from three independent signals, not a confirmed physician).
- **Confirmed Practo Prime payers:** Dr. Priya's Skin & Hair, Derma Solutions, VIDA Skin & Hair Transplant.
- **Heaviest paid-ad spend:** Akera Health, by a wide margin — 25 active Meta ads + 29 active Google ads simultaneously, across just two branches.
- **Stalest review pipeline:** Theory of Skin — 126 days (4.2 months) since the newest Google review, despite an active, verified 15.5k-follower Instagram.
- **Cleanest engagement record:** Ara Skin Clinic — 100% (4/4) of sampled negative reviews received a substantive owner reply.
- **Worst engagement record:** Derma Solutions — 0% (0/10) of sampled negative reviews replied, combined with the highest all-time negative rate in the batch (7.2%).

---

## 4. Priority queue — who to shop first, and why

Ranked by mystery-shop urgency, not alphabetically. This reflects screenshot-provable evidence and money already at stake, per the playbook's §0 priority rule — it is not a final ranking of lead quality.

1. **Akera Health** — largest confirmed paid-lead volume in the entire batch (54 combined active ads across Meta + Google, both branches). If response is slow, this is the single highest-value reactivation opportunity here. If response is fast, the six-test SOP (§2) is worth running in full given the ad scale.
2. **Dr. Priya's Skin & Hair Clinic** — highest review volume in the batch (1,613) and a confirmed Practo Prime listing with 5,966 Practo patient stories; a real booking-friction pattern is already visible in the reviews.
3. **Derma Solutions** — confirmed Practo Prime + the worst combination of negative-review rate (7.2%) and reply rate (0%) in the batch; also the only clinic with a quality/consent-adjacent complaint pattern worth being aware of before outreach.
4. **Haircosmos International** — active Meta ad spend on high-ticket hair-transplant offers (₹49,999+), paired with zero owner replies to negative reviews across both branches, including one describing an unresolved post-procedure complication.
5. **VIDA Skin & Hair Transplant** — currently-active Google Ads (last shown today) + confirmed Practo Prime, though its comparatively strong 60% reply rate on negatives means this could resolve to "None (pass)" faster than most.
6. **Theory of Skin** — the clearest Reviews-stage break in the batch; less urgent than the ads-driven leads above but a distinctive, quantified signal (4.2-month review gap) worth confirming.
7. **Dermatonik** — heaviest sustained Google Ads presence by duration (~1 year, two advertiser entities) plus a specific pre-visit qualification-failure complaint.
8. **Ara Skin Clinic** — thinnest-evidence wedge in the batch (excellent review engagement; Google Ads activity confirmed but attribution to this clinic unconfirmed).
9. **Gejje's Marvella** — no ads found on any channel; genuinely clean reviews; provisional wedge is the weakest-basis call, same as Routines.
10. **Routines by Dr. Apoorva** — no visible weakness anywhere in the data collected this session; the mystery shop here answers whether this is a rare hard-kill #9 candidate ("passes all six tests") rather than a lead to route.

---

## 5. Batch comparison table

| Clinic | Branch | Rating | Reviews | 90d neg | Reply rate (neg) | Meta ads | Google ads | Aggregator | Wedge | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| Gejje's Marvella | Basavanagudi | 5.0 | 870 | 0/28 | 50% | 0 active | 0 found | undetermined | Instant response + organic capture | Qualified |
| Haircosmos International | JP Nagar | 4.9 | 169 | 0/3 | 0% | 3 active | inactive since Dec'25 | undetermined | No-show recovery | Qualified |
| Haircosmos International | Whitefield | 4.9 | 499 | 4/23 | 0% | 3 active | inactive since Dec'25 | undetermined | No-show recovery | Qualified |
| Ara Skin Clinic | Shankarapura | 4.8 | 294 | 0/28 | 100% | undetermined | 19 active (attribution unconfirmed) | listed, no Prime | Dead-lead reactivation | Qualified |
| Dr. Priya's Skin & Hair | Marathahalli | 4.7 | 1,613 | 6/89 | 14% | 0 active | 0 found | **Prime confirmed** | Dead-lead reactivation (aggregator) | Qualified |
| Akera Health | HSR Layout | 4.9 | 315 | 3/11 | 17% | **25 active** | **29 active** | listed, no Prime | Dead-lead reactivation | Qualified |
| Akera Health | HRBR Layout | 4.9 | 361 | 0/26 | 50% | 25 active | 29 active | listed, no Prime | Dead-lead reactivation | Qualified |
| Derma Solutions | Marathahalli | 4.6 | 1,241 | 8/64 | **0%** | 0 active | 0 found | **Prime confirmed** | Dead-lead reactivation (aggregator) | Qualified |
| Routines by Dr. Apoorva | Malleshwaram | 5.0 | 217 | 0/40 | n/a (0 neg) | undetermined | 0 found | false match | Instant response + organic capture | Qualified |
| Theory of Skin | Indiranagar | 4.6 | 215 | 0/0 | 14% | 0 active | inactive since Jun'26 | listed, no Prime | Review reactivation agent | Qualified |
| Dermatonik | HSR Layout | 4.8 | 304 | 2/53 | 20% | 4 active | heavy, sustained (2 entities) | undetermined | Qualification + scoring upgrade | Qualified |
| VIDA Skin & Hair Transplant | Whitefield | 4.8 | 390 | 0/54 | 60% | 0 active | 12 active | **Prime confirmed** | Dead-lead reactivation (aggregator) | Qualified |

Full machine-readable version with contact fields: `batch-comparison-table.csv` (this batch's 12 rows appended to the running file).

---

## 6. Full clinic dossiers

### 6.1 Gejje's Marvella

**Depth mode:** Standard · **Locality:** Basavanagudi, Bangalore

**Basic Info**
- Address: Level 4, Bangalore Superspecialty Center, New High School Rd, behind Metro Station National College, Parvathipuram, Vishweshwarapura, Basavanagudi, Bengaluru 560004. Phone +91 99162 49637.
- Category: Plastic surgery clinic (GBP) — Plastic / Aesthetic Surgery / Hair Transplant / Dermatology per positioning.
- Website: gejjesmarvella.com (confirmed live). Instagram: @gejjesmarvella — 6,933 followers, 523 posts.
- Facebook: facebook.com/GejjesMarvella.
- **Possible second location — unconfirmed:** GBP contact enrichment returned two emails: `gejjesmarvella@gmail.com` and `gejjesmarvellahosapete@gmail.com`. Hosapete is a separate city (~330km from Bangalore). Not in the original brief and **not audited** — flagged as a lead for the user to verify, not assumed to be a real second branch.

**ICP Qualification** — Passes both hard kills. No park signals. **Status: Qualified.**

**Digital Presence** — Founder listed in the brief as **Dr. Somashekar Gejje**; not independently named in the clinic's own IG bio or GBP category, so treated as **weak** confidence, not confirmed. IG bio: "Plastic Surgery, Reconstructive Surgery, Aesthetic Surgery, Hair transplantation, Hand Surgery, Dermatology" — unusually broad specialty mix for this batch.

**Contacts**
| Name | Role | Source | Confidence |
|---|---|---|---|
| Dr. Somashekar Gejje | Founder (per brief) | User-supplied list only | weak |
| Clinic phone | — | GBP | confirmed |
| Clinic email | gejjesmarvella@gmail.com | GBP | confirmed |

LinkedIn not attempted this session (not prioritized against the cap). Not verified, not "not found."

**Ads** — Meta: 0 active ads on the confirmed page. Google Ads: 0 found by domain. Aggregator: Practo search resolved to an unrelated clinic — undetermined.

**Reviews** — 5.0★, 870 reviews all-time. Sampled 120 newest: 2 negatives, 1 replied (50%). Last 90 days: 28 sampled, 0 negative. Last 180 days: 39 sampled, 0 negative. Most recent review: today (0-day gap). Fake-review sanity check: clean, no burst pattern, quotes are specific — genuinely strong reputation.

**Marketing Analysis** — No paid spend on Meta or Google; growth appears organic. Hosapete-email finding suggests a possible multi-city footprint outside this session's scope.

```
funnel_break_stage:       Response Speed
recommended_entry_sku:    Instant response + organic capture — PROVISIONAL
confirm_via_mystery_shop: No ads and no visible review-side weakness — the weakest-evidence wedge call for this clinic. A slow/no reply confirms this row; a fast reply redirects toward the six-test SOP or "None (pass)" candidacy.
status:                   Qualified
unverified_fields:        Dr. Somashekar Gejje founder confirmation; possible Hosapete branch; LinkedIn; Practo listing status
```

---

### 6.2 Haircosmos International — 2 branches

**Depth mode:** Standard · **Locality:** Bangalore (JP Nagar, Whitefield)

**Basic Info** — Legal entity per Google Ads: "HAIRCOSMOS DIAGNOSTIC AND HEALTH CARE PRIVATE LIMITED." Category: Hair transplantation clinic. Website: haircosmosinternational.com. Instagram: @haircosmos_international — 18,525 followers, 568 posts.
- **JP Nagar** — 1st Floor, 15, 24th Main Rd, Puttenahalli, JP Nagar 7th Phase, Bengaluru 560078. Phone +91 72049 92757.
- **Whitefield** — 32, Varthur Main Rd, opposite Sigma Soft Tech Park, Ramagondanahalli, Whitefield, Bengaluru 560066. Phone +91 73491 87047.
- **Data-quality flag:** the JP Nagar GBP listing's website field is malformed — it concatenates the real domain with an unrelated-looking URL (`drpiyushranjan.com`). Likely a broken GBP field, not a founder lead; not corroborated elsewhere.

**ICP Qualification** — Passes both hard kills. No park signals (no individual doctor branding to trigger a mega-founder-brand read). **Status: Qualified.**

**Digital Presence** — **No founder or doctor named anywhere** — not the IG bio, not the website's About Us page (entirely generic), not GBP. Brand is positioned around the clinic name and award claims, not a person. Matches the brief's "—" founder entry.

**Contacts**
| Name | Role | Source | Confidence |
|---|---|---|---|
| — (none named) | — | — | — |
| Clinic phones | JP Nagar / Whitefield | GBP | confirmed |
| LinkedIn page | "Haircosmos International" | linkedin.com/in/haircosmos-international-7006a7238 | confirmed exists, not useful — blank headline, 0 connections, 1 follower |

**Ads** — Meta: **3 active ads** on the confirmed page (Independence Day laser hair removal offer; hair patch from ₹9,999; hair transplant from ₹49,999 with 0% EMI). Google Ads: 1 ad creative found by domain, shown May–Dec 2025 — **inactive since December 2025.** Aggregator: Practo search returned a category page, not a direct listing — undetermined.

**Reviews**
- **Whitefield:** 4.9★, 499 reviews. Sampled negatives: 6, **0 replied (0%)**. Most recent: 2026-08-02 (5-day gap). One 1★ describes a relative's scalp infection after a procedure, unresolved for 1.5 months, staff reportedly deflecting responsibility — no reply. Another: "8 sessions... saw no results... she said I should do 6 more and pay more" — no reply.
- **JP Nagar:** 4.9★, 169 reviews. Sampled negatives: 2, **0 replied.** Most recent: 2026-06-28 (**40-day gap**, noticeably staler than Whitefield). One 1★ describes a booked appointment where "the doctor never showed up" — no reply.
- **Recurring shape across both branches:** unresolved post-procedure issues and no-shows, paired with zero owner replies to any negative in either branch's sample.

**Marketing Analysis** — Active, aggressive Meta ad spend on high-ticket offers; Google Ads lapsed since Dec 2025. Zero owner responses to negatives across two branches, including one unresolved medical complication, is the sharpest signal here.

```
funnel_break_stage:       Booking / No-show
recommended_entry_sku:    No-show recovery — PROVISIONAL
confirm_via_mystery_shop: Active Meta spend on high-ticket transplant offers + two independent, unreplied reviews describing a doctor no-show (JP Nagar) and an unresolved complication (Whitefield). If confirmed live, this holds; if response is simply slow rather than a booking-process failure, redirect to Dead-lead reactivation.
status:                   Qualified
unverified_fields:        Founder/owner identity (none found); JP Nagar website field anomaly; Practo listing status; LinkedIn (exists but empty)
```

---

### 6.3 Ara Skin Clinic

**Depth mode:** Standard · **Locality:** Shankarapura, Basavanagudi, Bangalore

**Basic Info** — Address: 1st floor, Paras Vatika, 49/1, Shankar Mutt Rd, Shankarapura, Bengaluru 560004. Phone +91 98898 82246. Category: Skin care clinic. Website: araskinclinic.com. Instagram: @ara_skin_clinic — 4,758 followers, 711 posts.
- Facebook link on GBP is a broken placeholder (`facebook.com/share`).
- GBP contact enrichment found a leftover Wix-template email (`info@domainname.com`) alongside the real `glow@araskinclinic.com` — reported as a data-hygiene finding.

**ICP Qualification** — Passes both hard kills. No park signals. **Status: Qualified.**

**Digital Presence** — Founder **Dr. Sonakshi Sunil** confirmed via the clinic's own IG bio. Follower count cross-corroborates cleanly with the brief (4,758 vs. 4,757).

**Contacts**
| Name | Role | Source | Confidence |
|---|---|---|---|
| Dr. Sonakshi Sunil | Founder/Dermatologist | Own IG bio | confirmed |
| Clinic phone / email | — | GBP | confirmed |

**Ads** — Meta: tried keyword search and page-name search — both returned unrelated pages; **no matching Facebook Page found**, undetermined. Google Ads: **19 active/recent ad creatives** by domain, spanning Sept 2023 through today — ⚠️ **billed under advertiser name "Pure Dermacare,"** not "Ara Skin Clinic." A web search found no connection between the two names. Treated as: activity very likely real (long-running, points at this exact domain) but ownership/attribution unconfirmed. Aggregator: Practo listing confirmed, **no Prime badge**, thin profile (2 patient stories vs. 294 on Google).

**Reviews** — 4.8★, 294 reviews. Sampled negatives: 4, **all 4 replied (100%) — the strongest owner-engagement pattern in this batch.** Replies are substantive, not templated (e.g. a real clinical explanation for why single-session laser results are limited). Last 90 days: 28 sampled, 0 negative.

**Marketing Analysis** — Clean, well-run clinic with the best negative-review response behavior in the batch. Only real ambiguity is the Google Ads attribution question.

```
funnel_break_stage:       Response Speed
recommended_entry_sku:    Dead-lead reactivation — PROVISIONAL
confirm_via_mystery_shop: Weakest-evidence wedge in this batch. Basis: domain-matched but attribution-uncertain Google Ads (19 creatives under "Pure Dermacare") plus an otherwise clean, well-answered review record. A slow/no response confirms this wedge; a fast one likely redirects to "None (pass)" or the six-test SOP. Confirm in parallel whether Ara Skin Clinic itself runs the "Pure Dermacare"-attributed ads at all.
status:                   Qualified
unverified_fields:        Google Ads attribution; Meta ads presence; LinkedIn; Practo Prime status confirmed absent (not undetermined)
```

---

### 6.4 Dr. Priya's Skin & Hair Clinic

**Depth mode:** Standard · **Locality:** Marathahalli, Bangalore

**Basic Info** — Address: 1st Floor, CRM Sowbhagya Enclave, No:35/1, HAL Old Airport Rd, near Spice Garden Bus Stop, Marathahalli, Bengaluru 560037. Phone +91 97410 32946. Category: Skin care clinic. Website: drpriyaskinandhairclinic.com. Instagram: @drpriyaskinandhairclinic — 9,660 followers.

**ICP Qualification** — Passes both hard kills. No park signals. **Status: Qualified. Highest inbound-volume signal in the batch** (1,613 reviews).

**Digital Presence** — Founder **Dr. Priya J Talageri** confirmed — the IG account is literally hers. Practo additionally lists a second doctor, **Dr. Naveen M Nayak** (Nephrologist — an unusual specialty pairing, not investigated further).

**Contacts**
| Name | Role | Source | Confidence |
|---|---|---|---|
| Dr. Priya J Talageri | Founder/Dermatologist | Own IG account; corroborated on Practo | confirmed |
| Dr. Naveen M Nayak | Nephrologist, also listed here | Practo listing | likely |

**Ads** — Meta: 0 active ads on the confirmed page. Google Ads: 0 found by domain. Aggregator: **CONFIRMED PRIME** — "Max. 60 mins wait + Verified details," 98% recommended, **5,966 patient stories on Practo** (vs. 1,613 on Google — Practo is arguably a bigger lead channel than Google reviews suggest).

**Reviews** — 4.7★, 1,613 reviews — highest volume in the batch. Sampled negatives: 7, **~1 replied (~14%).** Recurring shape: booking/appointment friction — multiple reviewers independently confirm a time by phone and then face long unstructured waits ("there is no appointment system," 1h45m wait). One reply found: an owner explanation of a chronic scalp condition possibly aggravated by minoxidil.

**Marketing Analysis** — No direct ad spend — the entire paid-acquisition story is **Practo Prime.** Combined with a real, recurring booking-friction pattern and a low reply rate, this is a strong "paying for leads and possibly leaking them" candidate.

```
funnel_break_stage:       Response Speed
recommended_entry_sku:    Dead-lead reactivation (aggregator) — PROVISIONAL
confirm_via_mystery_shop: Confirmed Practo Prime (5,966 stories) + recurring "no real appointment system" complaints + ~14% reply rate. Test via a Practo-originated enquiry specifically: slow/absent response confirms this wedge; a fast reply redirects toward No-show recovery (booking friction persists even with fast contact) or the six-test SOP.
status:                   Qualified
unverified_fields:        LinkedIn (malformed URL); Dr. Naveen M Nayak's actual role/affiliation
```

---

### 6.5 Akera Health — 2 branches

**Depth mode:** Standard · **Locality:** Bangalore (HSR Layout, HRBR Layout)

**Basic Info** — Legal entity per Google Ads: "Akera Healthcare Private Limited." Category: Dermatologist. Website: akerahealth.com. Instagram: @akera.health — 2,313 followers.
- **HSR Layout** — 2nd Floor, 112, 27th Main Rd, Sector 2, Bengaluru 560102. Phone +91 72044 84955.
- **HRBR Layout** — 2nd Floor, LV Plaza, HRBR Layout 1st Block, Banaswadi, Bengaluru 560043. Phone +91 72044 88355.

**ICP Qualification** — Passes both hard kills. No park signals (3 named doctors on Practo, no single mega-founder-brand). **Status: Qualified. Highest combined paid-ad volume in this entire batch — top mystery-shop priority.**

**Digital Presence** — No individual founder named in IG bio or website — brand positioned around "Akera." Practo lists 3 dermatologists: Dr. Lavina Mittal, Dr. Smruthi T, Dr. Champati Prabhavathi — none independently confirmed as owner.

**Contacts**
| Name | Role | Source | Confidence |
|---|---|---|---|
| Dr. Lavina Mittal / Dr. Smruthi T / Dr. Champati Prabhavathi | Dermatologists (HSR) | Practo listing | likely |
| Clinic phones | HSR / HRBR | GBP | confirmed |

**Ads** — Meta: **25 active ads**, the highest in this batch — aggressive, high-frequency discount campaigns (laser hair removal, chemical peels, GFC hair treatment, laser toning; "1000+ Happy Clients" claims). One legitimately renders `{{product.brand}}` (dynamic catalog placeholder, not broken data). Google Ads: confirmed via advertiser-mode search — **"Akera Healthcare Private Limited," 29 ads.** Aggregator: Practo listing confirmed (4.5★, 26 stories), **no Prime badge on any of the 3 doctors** — all paid spend is Meta + Google, not the aggregator.

**Reviews**
- **HSR:** 4.9★, 315 reviews. Sampled negatives: 6, 1 replied (~17%) — the one reply was substantive, referencing an actual follow-up call already had with the reviewer.
- **HRBR:** 4.9★, 361 reviews. Sampled negatives: 2, 1 replied (50%) — empathetic tone, defended doctor credentials without being combative.
- Where owners do reply, tone is constructive — better than most of this batch — but combined reply rate (2/8, 25%) is still low relative to the ad scale driving traffic.

**Marketing Analysis** — By far the heaviest, most sustained paid-acquisition spend in the batch, funded entirely through direct ads (not the aggregator). Review quality is genuinely good at both branches — the textbook "ads ✓, unknown response speed" profile.

```
funnel_break_stage:       Response Speed
recommended_entry_sku:    Dead-lead reactivation — PROVISIONAL
confirm_via_mystery_shop: 25 active Meta ads + 29 active Google ads simultaneously — the largest confirmed paid-lead volume in this batch, on a 2-branch practice with strong (4.9★) reviews at both locations. The strongest, cleanest "Ads ✓" signal in the batch and the top-priority mystery shop. A fast responder here is still a strong prospect — redirect to Follow-up and nurture engine or the six-test SOP if so.
status:                   Qualified
unverified_fields:        Founder/owner identity (3 doctors found, none confirmed as owner); LinkedIn
```

---

### 6.6 Derma Solutions

**Depth mode:** Standard · **Locality:** Marathahalli, Bangalore

**Basic Info** — Address: Number 3, 1st Floor, Scorpio House, near Marathahalli Bridge, Bengaluru 560037. Phone +91 97412 23217. Category: Multi-speciality clinic. Website: dermasolutions.co.in — **correction to the original brief**, which listed "WhatsApp link only"; a real, live website was found via GBP this session. Instagram: @dermasolutionsskinclinic — 159 followers (smallest in this batch).

**ICP Qualification** — Passes both hard kills formally. No park signals triggered. **Status: Qualified** — see caution note below (not a disqualifier, but relevant context).

**Digital Presence** — Lead doctor **Dr. Sandeep Mahapatra** confirmed via direct LinkedIn pull (`linkedin.com/in/dr-sandeep-mahapatra-315411112`). His LinkedIn headline literally reads *"Consultant Dermatologist and Hair Transplant Surgeon"* — read literally, not explicitly "founder." His own About text, however, says *"Derma Solutions and Neo Follicile Hair Transplant are **Our 2 Clinics**"* — language implying an ownership stake. Reported as: **likely owner-operator**, title says consultant. 1,930 connections, 2,009 followers, 12+ years experience, 3,000+ transplants claimed. A second linked brand, "Neo Follicle Hair Transplant Clinic," was named but not audited this session.

**Contacts**
| Name | Role | Source | Confidence |
|---|---|---|---|
| Dr. Sandeep Mahapatra | Consultant Dermatologist / likely owner-operator | LinkedIn (direct URL), corroborated by IG and Practo | confirmed contact; role framing likely |
| Dr. Thyagaraj J | Plastic Surgeon | Practo listing | likely |

**Ads** — Meta: 0 active. Google Ads: 0 found. Aggregator: **CONFIRMED PRIME** — both Dr. Mahapatra and Dr. Thyagaraj J carry the badge. 1,649 Practo stories (vs. 1,241 Google). Note: Practo rating is 4.0★ vs. Google's 4.6★ — a real cross-platform divergence.

**Reviews** — 4.6★, 1,241 reviews. Distribution includes **89×1★ — 7.2% one-star rate, the highest negative percentage in this entire batch.** Sampled negatives: 10, **0 replied (0%) — the flattest engagement in this batch.** One 1★ alleges untrained nursing staff and a "messed up" hair transplant requiring a fix elsewhere. Another describes a booked evening appointment where the patient waited an hour, was never seen, and left. A ~9-months-ago Practo-sourced review describes being made to sign a consent form for a different, junior doctor to perform a paid procedure without full agreement — **Dr. Mahapatra's own reply to that one was defensive** ("Please don't spread misinformation").

**Caution note (Phase 5/6):** two independent reviews raise consent-process and procedure-quality concerns. This does not meet the hard-kill bar, but it's an escalation-grade pattern worth surfacing plainly. Also worth knowing: the one owner reply on record to a serious complaint was combative rather than de-escalating — relevant to how outreach should be framed with this founder.

**Marketing Analysis** — No paid ad spend; acquisition runs almost entirely through Practo Prime. Combined with the highest negative rate and flattest reply rate in the batch, this is a strong aggregator-reactivation candidate with real service-quality context attached.

```
funnel_break_stage:       Response Speed
recommended_entry_sku:    Dead-lead reactivation (aggregator) — PROVISIONAL
confirm_via_mystery_shop: Confirmed Practo Prime (1,649 stories, 2 Prime-badged doctors) + 0/10 owner replies to negatives + highest all-time negative rate in the batch (7.2%). A secondary, overlapping candidate is No-show recovery given the repeated booking-friction reviews — confirm which break is actually live.
status:                   Qualified
unverified_fields:        Whether Dr. Mahapatra is formally founder vs. consultant-with-equity; Dr. Thyagaraj J's affiliation depth; "Neo Follicle" relationship (not audited)
```

---

### 6.7 Routines by Dr. Apoorva

**Depth mode:** Standard · **Locality:** Malleshwaram, Bangalore

**Basic Info** — Address: No.285, 1st Floor, between 17th and 18th Cross, Sampige Rd, Malleshwaram, Bengaluru 560003. Phone +91 91102 61781. Category: Dermatologist. Website: routinesbydrapoorva.com — **correction to the original brief**, which listed "None (Maps link)"; a real, live website was found this session. Instagram: @routinesbydrapoorva — 2,033 followers, with the **highest engagement-to-follower ratio in this batch** (54 comments across 12 posts per the brief).

**ICP Qualification** — Passes both hard kills. No park signals. **Status: Qualified.** No visible weakness surfaced this session — see the honesty note below.

**Digital Presence** — Founder **Dr. Apoorva Bharadwaj** confirmed — the IG account is literally hers.

**Contacts**
| Name | Role | Source | Confidence |
|---|---|---|---|
| Dr. Apoorva Bharadwaj | Founder/Dermatologist | Own IG account | confirmed |

**Ads** — Meta: tried keyword and page-name search, both returned unrelated pages; no page found — undetermined. GBP also returned no Facebook link. Google Ads: 0 found by domain. Aggregator: Practo search resolved to a **different doctor entirely** — "Dr. Apoorva Singh" in Ghaziabad, a different city and person. No real Bangalore listing found — reporting the false match explicitly.

**Reviews** — 5.0★, 217 reviews — one of the cleanest profiles in this batch. Distribution: 212×5★, 4×4★, 0×3★/2★, 1×1★. Last 90 days: 40 sampled, **0 negative.** Last 180 days: 85 sampled, **0 negative.** No recurring complaint shape to report — there isn't one in the data available this session.

**Marketing Analysis** — No ad spend found anywhere, no resolvable Practo presence. This reads as an organic-growth, high-engagement, high-satisfaction small practice — the strongest "no visible weakness" profile in the batch.

```
funnel_break_stage:       Response Speed
recommended_entry_sku:    Instant response + organic capture — PROVISIONAL
confirm_via_mystery_shop: Thinnest-evidence wedge call in the batch, stated honestly: no ads, near-perfect reviews, high organic engagement, no findable complaint pattern anywhere. Per the playbook, "strong surface reputation with no visible weakness" is explicitly NOT a disqualifier — the mystery shop decides. If this clinic passes all six speed-to-lead tests, it's a legitimate hard-kill #9 candidate ("functioning system already in place") rather than a lead to route on the standard playbook.
status:                   Qualified
unverified_fields:        Meta ads presence (page not resolvable); Practo listing (false match returned, real status unknown); LinkedIn
```

---

### 6.8 Theory of Skin

**Depth mode:** Standard · **Locality:** Indiranagar, Bangalore

**Basic Info** — Address: 578, 9th A Main Rd, 1st Stage, Defence Colony, Indiranagar, Bengaluru 560038. Phone +91 96862 37333. Category: Dermatologist. Website: theoryofskin.co.in — **correction to the original brief**, which listed "None (Maps link)." Instagram: @theoryofskin_dermatology — 15,552 followers, **verified account.**

**ICP Qualification** — Passes both hard kills. **Park signal (§1.2, Medium):** possible mega-founder-brand pattern given the verified, individually-branded account with 15.5K followers — not disqualifying, but route through the standard playbook rather than a founder-capacity pitch unless the mystery shop confirms overflow signals. **Status: Qualified.**

**Digital Presence** — Founder **Dr. Sanjana Shivashankar** confirmed — the verified IG account is literally hers.

**Contacts**
| Name | Role | Source | Confidence |
|---|---|---|---|
| Dr. Sanjana Shivashankar | Founder/Dermatologist | Own verified IG account | confirmed |

**Ads** — Meta: 0 active on the confirmed page. Google Ads: advertiser "Sanjana Shivashankar," **5 ad creatives found, last shown 2026-06-01 — activity stopped roughly 2 months ago.** Aggregator: Practo listing confirmed, 74 patient stories, 4.0★ Practo rating, **no Prime badge visible.**

**Reviews** — 4.6★, 215 reviews. Distribution: **19×1★ — 8.8% one-star rate, second-highest in this batch.** **Most recent review: 2026-04-03 — a 126-day (~4.2 month) gap, the stalest review flow in the entire batch**, despite the active, verified, 15K+ follower Instagram and Google Ads that ran until ~2 months ago. Sampled negatives: 14, 2 replied (~14%). Recurring shape: appointment-confirmation failures — two independent, detailed reviews describe confirming a booking and then being told on arrival the doctor isn't available. **The stall itself is the headline finding here** — a review pipeline quiet for 4+ months despite active marketing elsewhere is itself the signal, not evidence of health.

**Marketing Analysis** — Google Ads paused ~2 months ago; no Meta ads. Review flow stalled 4+ months. Combined with a real appointment-confirmation-failure pattern, this looks like a clinic where the online reputation engine has gone quiet at the same time operational friction is visible in what reviews do exist.

```
funnel_break_stage:       Reviews
recommended_entry_sku:    Review reactivation agent — PROVISIONAL
confirm_via_mystery_shop: Newest Google review is 126 days old despite an active, verified 15K-follower Instagram and Google Ads that ran until ~2 months ago — a genuine, quantified stall. Secondary corroborating signal: two independent reviews describing appointment-confirmation failures, which could alternatively point to No-show recovery. Confirm via mystery shop: fast/accurate response redirects toward No-show recovery; broader disengagement confirms Review reactivation as the entry.
status:                   Qualified
unverified_fields:        LinkedIn; Practo Prime status confirmed absent (not undetermined); reason for the Google Ads pause
```

---

### 6.9 Dermatonik

**Depth mode:** Standard · **Locality:** HSR Layout, Bangalore

**Basic Info** — Address: 2nd Floor, 1655, 27th Main Rd, opposite NIFT College, 1st Sector, HSR Layout, Bengaluru 560102. Phone +91 89510 11944. Category: Skin care clinic. Website: dermatonik.com. Instagram: @dermatonik_ — 2,454 followers.

**ICP Qualification** — Passes both hard kills. No park signals. **Status: Qualified.**

**Digital Presence** — **No dermatologist named anywhere** — the website deliberately describes services as delivered by "your dermatologist" without naming one, on every service page crawled. GBP surfaced a secondary email, `Info@anjalisanghvi.com`, alongside `dermatonik@gmail.com`. The website credits **Anjali Sanghvi** by name for **permanent makeup services specifically** — not as medical director. The Google Ads advertiser record for this domain is registered as **"Anjali Sanghvi LLP."** Reading these three independent signals together: **Anjali Sanghvi is very likely the business owner/operator**, but there is no evidence she is the treating dermatologist — reported as **likely**, not confirmed.

**Contacts**
| Name | Role | Source | Confidence |
|---|---|---|---|
| Anjali Sanghvi | Likely owner/operator; credited on-site for permanent makeup | GBP secondary email + website PMU page + Google Ads entity name (3 independent signals) | likely |

**Ads** — Meta: **4 active ads**, aggressive "Limited-Period Special... Upto 50% OFF" language (HydraFacial, acne, pigmentation/melasma, skin boosters). Google Ads: **two separate advertiser entities** ("Anjali Sanghvi LLP" and a differently-cased duplicate) — **the heaviest sustained Google Ads presence in the batch by duration**, near-continuous for close to a year, still active today. Aggregator: Practo search returned a generic directory page, not a specific listing — undetermined.

**Reviews** — 4.8★, 304 reviews. Sampled negatives: 10, 2 replied (20%), tone somewhat formulaic/defensive. One 1★ describes calling ahead and being told a dermatologist was available, then being told on arrival there wasn't one, and still being charged ₹700 for a consultation that didn't happen — no refund given, no reply. **This is a distinct funnel-break signature** — bad information given *before* the visit, not just slow response.

**Marketing Analysis** — Heaviest, most sustained Google Ads spend in the batch plus active Meta ads, funding a clinic that anonymizes its own doctors. The clearest single incident — inaccurate phone availability information leading to a charged, unfulfilled visit — points at the qualification stage of the funnel rather than pure response speed.

```
funnel_break_stage:       Qualification
recommended_entry_sku:    Qualification + scoring upgrade — PROVISIONAL
confirm_via_mystery_shop: Heavy, sustained ad spend (two Google Ads entities, ~1 year, plus active Meta ads) combined with a detailed reviewer account of inaccurate phone availability information before a paid visit — maps to the "greeting-only/no qualification" §3 signal. Test via a call/DM asking about a specific concern: if the front desk accurately screens, redirect to Dead-lead reactivation given the ad volume.
status:                   Qualified
unverified_fields:        Treating dermatologist's identity (never named); Anjali Sanghvi's exact role/title; Practo listing status; two-entity Google Ads reason
```

---

### 6.10 VIDA Skin & Hair Transplant Clinic

**Depth mode:** Standard · **Locality:** Whitefield, Bangalore

**Basic Info** — Address: 2, 75, Whitefield Main Rd, Giddens Layout, Narayanappa Garden, Whitefield, Bengaluru 560066. Phone +91 70325 82393. Category: Hair transplantation clinic. Website: vidaskinandhairclinic.com. Instagram: @vida_skin_clinic — 1,165 followers, notably high post count (738) relative to following.

**ICP Qualification** — Passes both hard kills. No park signals. **Status: Qualified.**

**Digital Presence** — Founder **Dr. Jigisha N. Jalu** confirmed — the IG account is literally hers.

**Contacts**
| Name | Role | Source | Confidence |
|---|---|---|---|
| Dr. Jigisha N. Jalu | Founder/Dermatologist | Own IG account; corroborated on Practo | confirmed |

**Ads** — Meta: 0 active. Google Ads: advertiser "Jigisha jalu," **12 ad creatives, currently active (last shown 2026-08-07 — essentially today).** Aggregator: **CONFIRMED PRIME** — Dr. Jalu carries the badge, 302 patient stories, 90% recommended. Notable channel mix: active on Google Ads + Practo Prime, but **zero Meta ad spend** — a different acquisition profile from most of this batch.

**Reviews** — 4.8★, 390 reviews (matches brief exactly). Sampled negatives: 5, **3 replied (60%) — one of the better reply rates in this batch.** Recurring shape: **three independent reviewers, across different dates, describe pricing pressure and escalating costs** — a repeated pattern even though reply behavior to complaints is otherwise good. This is service-quality/trust context, not itself a named §3 wedge.

**Marketing Analysis** — Active, current Google Ads plus confirmed Practo Prime, no Meta presence at all. Comparatively strong reply behavior on negatives is a genuine positive signal — this owner engages with criticism, even if the underlying pricing-pressure pattern recurs.

```
funnel_break_stage:       Response Speed
recommended_entry_sku:    Dead-lead reactivation (aggregator) — PROVISIONAL
confirm_via_mystery_shop: Confirmed Practo Prime + currently-active Google Ads (last shown today) — real, current paid spend across two channels. This clinic's decent reply behavior (60% on negatives) weakens the "slow response" assumption somewhat — if the DM/call reply is fast, likely redirects toward "None (pass)" or a nurture/qualification wedge. The recurring pricing-pressure complaints are real context but don't map to a named §3 wedge on their own.
status:                   Qualified
unverified_fields:        LinkedIn; whether pricing-pressure pattern reflects an actual funnel break or a service-positioning issue
```

---

## 7. Cross-batch patterns

- **Booking/appointment-confirmation friction appears independently in 4 of 10 clinics** (Dr. Priya's, Derma Solutions, Haircosmos JP Nagar, Theory of Skin) — in each case, multiple reviewers describe confirming a time and then facing a no-show, long unstructured wait, or a doctor who turns out not to be available. This is the single most repeated funnel-break signature in this batch and is worth watching for at the category level, not just per-clinic.
- **Owner reply rate to negative reviews varies enormously** — from 100% (Ara Skin Clinic) to 0% (Derma Solutions, and effectively 0% at both Haircosmos branches). Reply rate did not correlate with ad spend: the two heaviest advertisers (Akera, Dermatonik) both sit in the 17–20% range, not markedly better than clinics spending nothing.
- **Practo Prime, where confirmed, correlates with the largest review-volume clinics** (Dr. Priya's: 1,613; Derma Solutions: 1,241; VIDA: 390) — consistent with Prime's booking-volume value proposition. None of the three heaviest Meta/Google advertisers (Akera, Haircosmos, Dermatonik) pay for Prime — their acquisition strategy is direct-ads-only.
- **Three clinics in the original brief were incorrectly listed as having no website** (Derma Solutions, Routines by Dr. Apoorva, Theory of Skin) — all three had live, functioning sites findable via GBP. Worth flagging in case the same gap exists elsewhere in the source list this batch was drawn from.
- **No individual doctor is named publicly** for 2 of 10 clinics (Haircosmos International, Akera Health) — both are also the two heaviest advertisers in the batch, which may make founder-level outreach harder to route without further digging (front-desk-only contact, per the playbook's Phase 4/§1.2 park guidance).

---

## 8. Corrections made during self-review

1. **Meta ads keyword-search false positives.** The first Meta ads pass used `search_type=keyword_unordered` against all 10 clinic names and returned 139 "ads" — the large majority unrelated (Colgate India, Nestlé Nutrition Institute, random unaffiliated dermatologists in other cities). Re-ran against confirmed Facebook Page URLs sourced from GBP contact enrichment for 8 of 10 clinics, which returned clean, attributable data. For the 2 clinics with no confirmed page (Ara Skin Clinic, Routines by Dr. Apoorva), a second attempt using `search_type=page` also failed to resolve a real match — reported as undetermined rather than guessed.
2. **Google Ads Transparency name-mode near-total miss.** The first pass queried all 10 clinic names in `advertisers` mode and resolved only 1 of 10 (Akera Health) to an actual advertiser record — confirmed via the run's `STATE` key-value record, not just the low dataset count, per the mandatory manual tie-break on a reversing/load-bearing finding. Re-ran in `ads` mode by domain for the other 9, which correctly surfaced active advertisers for 5 more clinics that the name-mode pass had silently missed (Ara Skin, Haircosmos, Theory of Skin, Dermatonik, VIDA).
3. **Website crawl under-coverage.** The first website-content-crawler run set `maxCrawlPages: 5` assuming it was a per-site cap; it is in fact a **global** cap across all 10 start URLs, so only 6 sites got crawled at all before the budget ran out. Re-ran with a global cap of 45, recovering all 10 sites (48 pages total).
4. **Ara Skin Clinic Google Ads attribution.** The domain-matched ads are billed under "Pure Dermacare," not the clinic's own name. A direct web search for a connection between the two names found none — reported as unconfirmed attribution rather than either dropping the finding or asserting it as the clinic's own spend.

---

## 9. Limitations — what was not verified

- **Mystery shop:** not run for any of the 10 clinics. Every wedge in this report is **PROVISIONAL** and depends on it — this is the single largest gap across the whole batch, by design (this pipeline never runs it).
- **LinkedIn founder search:** only attempted for 2 of 10 clinics, both via a direct URL surfaced by GBP contact enrichment (Derma Solutions, Haircosmos International — the latter's profile turned out to be empty/unused). Not run for the other 8 against the daily free-tier cap on name-based search; **not verified**, not "not found."
- **Founder/owner identity unresolved** for Haircosmos International and Akera Health — no individual named on any public channel checked this session.
- **Aggregator (Practo) status undetermined** for 4 of 10 clinics (Gejje's Marvella, Haircosmos International, Dermatonik — no direct listing resolved; Routines by Dr. Apoorva — search false-matched to a different doctor in a different city). No verified dedicated actor exists for this check; it was run via web search, time-boxed per clinic.
- **Google Ads attribution uncertain** for Ara Skin Clinic — active spend confirmed pointing at their domain, billed under an unrelated-looking name with no confirmed link.
- **Website crawl capped** at homepage + directly-linked pages per site (48 pages across 10 sites); deeper content beyond what was captured may exist unseen.
- **Notion "Valence Ops Leads Tracker":** connector was not authorized in this session, so existing status/priority/owner fields (if any) were not cross-checked or treated as authoritative. Proceeded without blocking the batch, per the playbook's explicit instruction.

---

## 10. Tool health notes for the next batch

- `compass/crawler-google-places` — reliable this run (90% platform success rate, full 12/12 coverage across both batches). Keep `maxReviews` around 120 and `scrapeReviewsPersonalData: false` (privacy-minimizing, and reviewer PII wasn't needed for the analysis).
- `apify/facebook-ads-scraper` — **never trust a bare keyword search.** Always resolve a real Facebook Page URL first (GBP contact enrichment is the cheapest source) and query that directly; `search_type=page` is a weak fallback, not a reliable substitute, when no page URL exists.
- `scrapesage/google-ads-transparency-scraper` — **`advertisers` mode by brand name is unreliable** (missed 9/10 in this batch); **`ads` mode by domain is far more reliable.** Note `domains` input is not accepted in `advertisers` mode — use `ads` mode for domain-based checks.
- `apify/website-content-crawler` — **`maxCrawlPages` is a global cap across all `startUrls`, not per-site.** For a 10-site batch, budget accordingly (this session used 45 for 10 sites at depth 1) rather than assuming a per-site number.
- No dedicated Practo/JustDial actor was found in the Apify Store this session either — the `rag-web-browser` site-scoped search workaround remains the best available method, and remains inconsistent (false matches occurred once this session, for Routines by Dr. Apoorva).

---

## 11. Data provenance

All figures in this report trace to a specific Apify actor run or web search made in this session on 2026-08-08:
- GBP + reviews: 2 `compass/crawler-google-places` runs (7 + 5 search terms, 12 places).
- Instagram: 1 `apify/instagram-profile-scraper` run (10 usernames).
- Meta ads: 3 `apify/facebook-ads-scraper` runs (initial keyword sweep, corrected page-URL pass, page-name fallback for 2 clinics).
- Google Ads: 2 `scrapesage/google-ads-transparency-scraper` runs (name-mode, then domain-mode correction).
- Aggregator: 10 `apify/rag-web-browser` site-scoped searches.
- Website content: 2 `apify/website-content-crawler` runs (initial under-covered pass, corrected full pass).
- LinkedIn: 1 `harvestapi/linkedin-profile-scraper` run (2 direct URLs).
- 1 targeted web search to check the Ara Skin Clinic / "Pure Dermacare" naming question.

No figure in this report was carried over from a prior batch, memory, or inference not traceable to one of the above.

---

## 12. Recommended next actions

1. **Run the mystery shop, starting with Akera Health** (highest confirmed ad volume), then Dr. Priya's Skin & Hair and Derma Solutions (highest volume / Practo Prime + worst engagement).
2. **Confirm the Ara Skin Clinic Google Ads attribution** directly with the clinic before treating that ad spend as their own in any outreach.
3. **Consider a light LinkedIn or web search for a Haircosmos International and Akera Health decision-maker** — both are the batch's heaviest advertisers but have no named individual, which will make outreach harder to route without a name.
4. **Feed the corrected website URLs** for Derma Solutions, Routines by Dr. Apoorva, and Theory of Skin back into whatever source list produced the original brief, so the gap doesn't repeat.
5. Once mystery-shop results land, hand qualifying clinics to `personalized-outbound-v2.md` for message/offer drafting — this pipeline stops at the provisional wedge, by design.


---
Related: [[01 Playbooks/wedge-signal-entry|wedge-signal-entry]] · [[01 Playbooks/personalized-outbound-v2|personalized-outbound-v2]] · [[05 Prospects/Batch 7 (Notion Batch 2)/13 Ara Skin Clinic|13 Ara Skin Clinic]] · [[05 Prospects/Batch 7 (Notion Batch 2)/16 Derma Solutions|16 Derma Solutions]] · [[05 Prospects/Batch 7 (Notion Batch 2)/19 Dermatonik|19 Dermatonik]] · [[05 Prospects/Batch 7 (Notion Batch 2)/14 Dr. Priya's Skin and Hair Clinic|14 Dr. Priya's Skin and Hair Clinic]] · [[05 Prospects/Batch 7 (Notion Batch 2)/18 Theory of Skin|18 Theory of Skin]] · [[05 Prospects/Batch 7 (Notion Batch 2)/12 Haircosmos International|12 Haircosmos International]] · [[05 Prospects/Batch 7 (Notion Batch 2)/11 Gejje's Marvella|11 Gejje's Marvella]] · [[05 Prospects/Batch 7 (Notion Batch 2)/20 VIDA Skin and Hair Transplant|20 VIDA Skin and Hair Transplant]] · [[05 Prospects/Batch 7 (Notion Batch 2)/15 Akera Health|15 Akera Health]] · [[05 Prospects/Batch 7 (Notion Batch 2)/Batch 7 (Notion Batch 2)|Batch 7 (Notion Batch 2)]]
