# IG Pre-Gate — 40-Clinic Shortlist Screen

**Run date:** 2026-08-08 · **Source:** Apify `apify/instagram-profile-scraper`, run `EesNLVkPYhlCqqs50`, dataset `HF2DOpdkMh15tt4eV` · **Cost:** ~$0.10 (39 profiles @ $0.0026, about-section add-on disabled)

**Coverage check (per MEMORY.md §2 Apify verification rule):** 39 handles submitted, 39 dataset items returned, 0 failed requests. But "Succeeded" ≠ complete — **6 items came back with no usable payload** and are logged as data gaps below, not as findings. Post-level metrics are computed from the 12 most recent posts per account (the actor's cap), so `posts/30d` saturates at 12 and `posts/90d` is a floor, not a total.

## What this screen can and cannot decide

Scraped: follower count, post count, verified/private/business flags, bio, external link, business category, and the 12 most recent posts with timestamps and comment counts.

**Not scraped this run (declined to conserve credits):** Meta ad spend, Google review recency, website/booking-flow state.

That matters for how far the screen goes. `wedge-signal-entry.md` §0 requires the wedge to be *diagnosed* from the earliest provable break — and every row in the §3 routing table keys off either ad spend or response speed. **Neither is in this dataset.** So the wedge column below is a *hypothesis to test*, never a finding. The mystery shop stays Tilak's (standing rule, MEMORY.md §2) and is the gate that actually decides.

One framework correction worth stating up front, because it changes the shape of this list: `wedge-signal-entry.md` §1.3 says **missing one channel is explicitly NOT a disqualifier**. A dead Instagram is therefore not a kill — it removes the IG-first sequence and reroutes the clinic to WhatsApp/phone. Several clinics with dead IG accounts below carry 600–1,600 Google reviews, which makes them stronger prospects than some of the active-IG accounts, not weaker.

---

## Tier A — Qualified, work these first (10)

Active account, real audience, identifiable founder, no hard kill, single-decision-maker read.

| # | Clinic | Handle | Followers | Last post | Posts/30d | Comments (12 posts) | Reviews | Why it clears |
|---|---|---|---|---|---|---|---|---|
| 1 | Gejje's Marvella (Basavanagudi) | @gejjesmarvella | 6,933 | 1d ago | 12 | 17 | 684–869 | Plastic + reconstructive + hair transplant = highest ticket in the set. Daily cadence, live audience, own website. |
| 2 | Haircosmos International (JP Nagar + Whitefield) | @haircosmos_international | 18,525 | 1d ago | 12 | **0 across all 12** | 169–499 | Hair transplant, two branches, posting daily to 18.5K and getting literally zero comments. Broadcast with no inbound loop. |
| 3 | Ara Skin Clinic (Basavanagudi) | @ara_skin_clinic | 4,757 | 2d ago | 12 | **0 across all 12** | 294 | Dr. Sonakshi Sunil named and fronted. Daily posting, zero engagement return. Same shape as Haircosmos, smaller. |
| 4 | Dr. Priya's Skin & Hair (Marathahalli) | @drpriyaskinandhairclinic | 9,660 | 2d ago | 9 | 9 (0 on all 9 recent) | 1,613 | 1,613 reviews is a very strong organic base. 1,108 posts, own domain, founder-named. |
| 5 | Akera Health (HSR + HRBR) | @akera.health | 2,314 | 3d ago | 9 | 14 | 314 | Two branches with separate numbers in bio, own site, Morpheus8/anti-ageing mix. Clean mid-tier founder profile. |
| 6 | Derma Solutions (Marathahalli) | @dermasolutionsskinclinic | 159 | 4d ago | 6 | **0 across all 12** | **1,241** | The sharpest mismatch in the set — 1,241 Google reviews against 159 IG followers. Reputation is doing the work; IG is not a channel here. Bio links straight to WhatsApp. |
| 7 | Routines by Dr. Apoorva (Malleshwaram) | @routinesbydrapoorva | 2,032 | 4d ago | 8 | 54 (one post at 33) | 217 | Only Tier A account with real two-way comment activity. Founder-run read is strong: personal name, WhatsApp number in bio, no website. |
| 8 | VIDA Skin & Hair Transplant (Whitefield) | @vida_skin_clinic | 1,165 | 12d ago | 5 | 6 | 390 | Dr. Jigisha Jalu named with full credentials. 738 posts, own site, hair transplant ticket size. |
| 9 | Dermatonik (HSR) | @dermatonik_ | 2,454 | 10d ago | 2 | 6 | 305 | **Cadence just broke** — steady ~5-day rhythm through June, then only 2 posts in 30 days. Recent, datable change worth opening on. |
| 10 | Theory of Skin (Indiranagar) | @theoryofskin_dermatology | 15,553 | 8d ago | 9 | 4 | 215 | Dr. Sanjana Shivashankar, **verified**, 577 posts. Sits on the park boundary — see the judgment note below. |

**Judgment call on Theory of Skin vs Dr. Divya Sharma.** These two look nearly identical on follower count (15.5K vs 16.2K) but land in different tiers, so the reasoning should be visible rather than buried. Divya Sharma carries 1,760 Google reviews, 15+ years, and giveaway-scale engagement (one post at 523 comments) — an established brand with the gatekeeper problem `OUTBOUND_MEMORY.md` §6 defers. Theory of Skin has a comparable audience but only **215 reviews and 4 comments across 12 posts** — a large following that isn't converting into patient volume or engagement. That profile is more likely to still be reachable and still feel the problem, which is why it stays in Tier A. If it turns out to have a social manager or agency in place, it drops to park.

## Tier B — Qualified but thinner, second wave (5)

| # | Clinic | Handle | Followers | Last post | Posts/30d | Reviews | Caveat |
|---|---|---|---|---|---|---|---|
| 10 | D White Feather (Whitefield) | @dwhitefeather_clinic | 4,965 | 11d ago | 3 | 633 | Good review base, cadence slipping. Contact number in bio is a Delhi-series mobile (9310…) — worth confirming the clinic is Bangalore-operated. |
| 11 | Vitals Klinic (E-City + BTM) | @vitalsklinic | 8,100 | 2d ago | 10 | 272 | Posts every 2 days at 14:00 UTC almost exactly — **scheduled by a tool or agency**. Routes to §1.2 "existing but shallow automation" (High priority park, not a kill). |
| 12 | Krity 360 (Bellandur) | @krity.360 | 456 | 4d ago | 4 | 157 | Aesthetic dentistry + facial aesthetics + permanent makeup. High ticket, but small audience and irregular posting. |
| 13 | Project Skin (HSR) | @projectskin.in | 2,189 | **45d ago** | 0 | 98 | Was posting through H1, stopped after 24 Jun. Under the 100-review line. Real audience, stalled account. |
| 14 | Dr AG Skin & Hair (Malleshwaram) | @dr.ag_skin_hair_clinic | 365 | 12d ago | 4 | 32 | Only 32 reviews and no external link at all. Thinnest genuinely-active account here. |

## Tier C — Dead or dormant IG, but the clinic is not disqualified (9)

Per §1.3, these do **not** get killed for a dead Instagram. They lose the IG-first sequence and reroute to WhatsApp/phone/email. The top three carry review bases that beat most of Tier A.

| Clinic | Handle | Last post | Dormant | Reviews | Read |
|---|---|---|---|---|---|
| Nirmal Skin & Hair (Vijayanagar) | @nirmalskinclinic | 2017-08-25 | **~9 years** | 1,008 | 1,008 reviews with an IG abandoned since 2017. Strong clinic, IG is not a channel. Route via website/phone. |
| Therapeía (Basavanagudi) | @therapeia_skin_hair_ent_centre | 2025-03-16 | 17 months | 644 | Same shape. Own site. Skin+Hair+ENT. |
| Dr Sachith Abraham (Koramangala) | @the_medical_skin_clinic | 2024-11-23 | 21 months | 218 | **Bio points at a different handle, @drsachith** — this scraped account is likely the abandoned one. Re-check the live handle before writing this off. |
| Nutriderma (JP Nagar) | @nutridermaclinics | 2026-04-04 | 4 months | 142 | Had consistent comment activity (2–5/post) until it stopped. Recently dormant, not dead. |
| Dr. Renu Nair (JP Nagar/HSR) | @drrenuskinclinic | 2026-04-13 | 4 months | 126 | 284 posts, zero comments on all 12 recent. Own domain. |
| Skyn D'Or (Bellandur) | @skyndor_skinclinic | 2026-06-01 | 2 months | **25** | 6,839 followers against 25 Google reviews — audience and patient base badly out of step. Two pinned posts hold 56 and 12 comments (likely a giveaway). Treat the follower number with suspicion. |
| Sanjeevani Cos Derma (Rajajinagar) | @sanjeevanicosderma | 2026-03-24 | 4.5 months | 122 | 553 followers, zero comments across all 12 posts. |
| LIYANSH / Dr Jayashree (Rajajinagar) | @dr.jayashree_theskindoc | 2026-05-05 | 3 months | 74 | 113 followers, 14 posts, external link goes to **Apollo 24|7** — she may be practising through the aggregator rather than a standalone clinic. Under the review line too. |
| ASHRAYA Skin & Neuro (Rajajinagar) | @ashrayaskinandneuro8 | 2025-04-09 | 16 months | 120 | **0 followers, 1 post.** Account never launched. |

## Park — fits the criteria but deferred by standing policy (5)


`OUTBOUND_MEMORY.md` §6 defers mega-founder-brand clinics until Case Study #1 exists; §1.1 #5 kills multi-partner sign-off.

| Clinic | Handle | Followers | Why parked |
|---|---|---|---|
| Layers Skin & Hair (Indiranagar) | @layersclinics | 48,018 | **"23+ branches across India."** Chain — §1.1 #5 committee sign-off. Closest thing to a hard kill in the set; confirm before spending time. |
| Mister Hair (HSR) | @misterhair_clinic | 57,500 | Verified, 3 cities, no-cost EMI, cal.com booking funnel already built. Mega founder brand → §1.2 park. Note the **24 Google reviews against 57.5K followers and a "1000+ patients" claim** — that gap is worth understanding. |
| Dr. Divya Sharma (Marathahalli) | @dr.divya_sharma | 16,166 | 1,760 reviews, 15+ years, one post at **523 comments** (giveaway mechanics). Mega founder brand → park. |
| Venkat Center (Vijayanagar) | @venkat_center | 1,668 | Est. 2003, 3 locations, Skin+Hair+ENT+Plastic. Multi-partner. Your own note already said likely PARK — confirmed. |
| Imex Care (Marathahalli/Whitefield) | @imexcare | 914 | Dental, 1,641 reviews, but bio reads **"Page managed by @dawn_prevails | Orthodontist, @dentst_poooshetty9 | Implantologist"** — two named partners = §1.1 #5 risk. Also dormant since 14 Apr. |

## Out of scope — 1

| Clinic | Handle | Finding |
|---|---|---|
| Dr Alka's Skincare (Vijayanagar) | @dralkaskincareuk | **Wrong entity.** This account is "Dr Alka's Skincare & Healthcare UK" — bio reads *"Cannock, Staffordshire"*, posting daily from the UK. It is not the Bangalore Vijayanagar clinic on your list. The handle mapping in the shortlist is incorrect; the Bangalore clinic's real handle is unknown. |

## Data gaps — resolve the handle before any decision (7)

None of these are kills. The handle is broken, private, or returned nothing — the clinic is simply unassessed.

| Clinic | Handle | What came back |
|---|---|---|
| Dr Roshan's HT & Skin (Whitefield) | @drroshanhtc | `not_found` — handle dead or renamed |
| Clinique Internationale (JP Nagar) | @drbhaveshgupta_ | `not_found` — 362 reviews, worth re-finding |
| SKINPRO / Dr Shruthi (Rajajinagar) | @drshruthiskinpro | `not_found` |
| Looks Studio HT (Whitefield) | @looksstudioindia | `not_found` — 37 reviews anyway, low value |
| AARNA Aesthetic (Jayanagar) | @aarna_clinic | `Restricted profile` — exists, blocked to scraping. Has own website. |
| Tolasi Dermatology (Koramangala) | @sushantswamy | **Private account**, 323 followers, 17 posts, bio "Die empty" — this is a personal account, not the clinic page. 290 reviews say the clinic is real; find the clinic handle. |
| DERMACLIN by Dr. Gopal (Basavanagudi) | — | No handle submitted (unverified in source list) |

**Partial returns — profile fields only, no post data:** @snehasoodaesthetics (204 followers, 255 reviews, linktr.ee), @skinsummit.in (539 followers, 284 reviews, no website), @neomax_facialaesthetics (74 followers, 128 reviews, no website). Activity is unknown for these three; the two with real review bases (Sood, Skin Summit) are worth a manual look.

---

## Where this leaves the funnel

40 listed → **15 qualified and actionable** (Tier A + B), **9 alive as clinics but not via Instagram**, 4 parked on standing policy, 1 wrong entity, 10 unassessed pending handle fixes.

**Highest-value next actions, in order:**

1. **Mystery-shop Tier A** (yours). Until that runs, no wedge below is more than a guess.
2. **Fix 4 handles that gate real clinics** — Clinique Internationale (362 reviews), Tolasi (290), Dr Sachith (218, try @drsachith), SKINPRO (89). Roughly 15 minutes of manual checking recovers three genuinely qualified prospects.
3. **Run the Meta Ad Library layer** on Tier A only (10 clinics, free — no Apify cost). Ads-yes flips the wedge from guesswork to the "Ads ✓ · response slow" row, the highest-priority route in the table.
4. **Decide on the three non-IG heavyweights** — Nirmal (1,008 reviews), Therapeía (644), Derma Solutions (1,241). Combined they hold more patient proof than all of Tier A. They need a WhatsApp/phone sequence that doesn't exist yet.

## Wedge hypotheses — unconfirmed, do not draft from these

Recorded so the mystery shop has something to falsify. Each needs the ad check and the response-time test before it earns a `recommended_entry_sku` tag.

- **Ara, Haircosmos, Derma Solutions, Dr. Priya** — daily posting, zero comments across every recent post. *If* the ad check comes back positive and response is slow, these route to dead-lead reactivation. *If* no ads, they route to "reputation markets for free, inbox kills what it earns."
- **Dermatonik** — cadence broke ~10 days ago after a steady rhythm. A datable change, but a stalled posting schedule is not evidence of a funnel break. Needs the shop.
- **Vitals Klinic** — machine-regular 2-day posting is good evidence of a scheduling tool, which is §1.2 "shallow automation." That is a park-tier depth-upgrade pitch, not an opener.
- **Skyn D'Or** — 6,839 followers vs 25 reviews. Either the audience is bought/giveaway-driven or almost no patient converts. Worth knowing which; not yet a wedge.
