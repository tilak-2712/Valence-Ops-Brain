# Vitals Klinic

> ⚠️ **PRE-SHOP RECORD — live state is in Notion, not here.** This dossier was written before the
> mystery shop ran. This cohort is tracked in Notion as **"Batch 2"**
> (`collection://754da695-40e4-839a-a0e7-07e28a0a27d8`), where the `Mystery shop status`, `Wedge` and
> `Notes` fields carry the shop transcript, timestamps, the confirmed wedge and the next action.
> **Read the Notion row before drafting anything for this clinic.** Where the two disagree, Notion wins.
> Any `recommended_entry_sku: … PROVISIONAL` line below may already have been confirmed or redirected.


**Depth mode:** Standard (Apify re-run) · **Locality:** BTM Layout + Electronic City + Whitefield, Bangalore · **Research date:** 2026-08-08

> **Source key:** `[A]` = Apify re-run, 2026-08-08 · `[S]` = ScrapeGraph pass, 2026-08-08 (retained where Apify didn't cover it) · `[IG]` = Apify Instagram run `EesNLVkPYhlCqqs50`
> **⚠️ This dossier contains one direct contradiction of the earlier pass — see Ads.**

## Basic Info
- **Legal/brand name:** Vitals Klinic (GBP listings vary: "Vitals Skin and Hair Clinic", "Vitals skin Hair and laser klinic")
- **Website:** vitalsklinic.com `[A]` — 40+ treatment SEO pages crawled, plus dedicated location pages for BTM Layout, Electronic City and Whitefield, confirming 3 active branches `[A]`
- **Instagram:** @vitalsklinic — 8,100 followers, 595 posts, last post 2026-08-06, 10 posts/30d, 2 comments across last 12 posts `[IG]`
- **Socials:** Facebook /vitalsklinic (page ID 317939428557405) · LinkedIn /company/vitals-klinic `[A]`
- **Emails:** vitalsklinic@gmail.com, contact@vitalsklinic.com `[A]`
- **Founder:** Dr. Harish Prasad B.R — personal LinkedIn verified, headline "MD Dermatologist | Vitals Klinic, Bangalore" `[S]`. Sole named doctor. Website has a `/team-of-qualified-dermatologist` page `[A]`.

### Locations found `[A]`
| Branch | Reviews | Rating | Most recent review | Status |
|---|---|---|---|---|
| **BTM Layout** (390, 7th Cross Rd, BTM 2nd Stage) | **1,892** | 4.7★ | 2026-08-07 | Active |
| Whitefield (Arcadia Grace #205A) | 6 | 4.3★ | 2026-07-29 | Active |
| BEL Layout / Bedarahalli | 14 | 4.6★ | — | **PERMANENTLY CLOSED** |

**⚠️ Two corrections to prior data.** The earlier pass recorded **272 reviews / 4.6★** and stated it "matched the source table exactly." The BTM listing actually carries **1,892 reviews / 4.7★** `[A]`. The 272 figure matches no listing found here — it may have been the Electronic City listing, which **did not surface in this run** and remains uncaptured. Separately, a **permanently closed** fourth listing exists at Bedarahalli — not previously known.

## ICP Qualification
- §1.1 #1 — website + IG + GBP all present. **Pass.**
- §1.1 #2 — 1,892 reviews, continuous flow. **Pass.**
- §1.1 #4 — no prices published on site. **Unknown, not inferred.**
- §1.1 #5 — single named doctor across 3 branches. **Pass.**
- **Status: Qualified** (provisional, pending mystery shop).

## Digital Presence
- Website booking paths `[S]`: `/book-appointment/` page, WhatsApp click-to-chat (`api.whatsapp.com/send?phone=+919740484793`) with a generic pre-filled greeting, "Request a Call Back" form. **No live chat widget. No qualification questions at any entry point.**
- Site builder credited to VBS Technologies — a web-design vendor, not a social/marketing agency `[S]`.
- The go-list hypothesis that the clockwork ~2-day / 14:00 UTC posting cadence implies an agency remains **uncorroborated** by either pass.

## Ads
**Meta — 0 ads. Verified twice.** `[A]`
- Active-only query: `totalCount: 0`, `isResultComplete: true`, page resolved as "Vitals Klinic" (ID 317939428557405), `pageIsDeleted: false`, `captchaRequired: false`.
- All-status re-query (active + inactive): `totalCount: 0`, `hiddenAds: 0`, `hasBlankAds: false`, `isResultComplete: true`.

> **⚠️ DIRECT CONTRADICTION — unresolved.** The ScrapeGraph pass reported **1 active Meta ad, Library ID 2055649615024286, started 2026-07-24, FB+IG, "comment HAIR" creative — described as screenshot-verified.** Both passes ran on 2026-08-08. Two clean Apify queries against the confirmed Page ID return zero ads ever, active or inactive. These cannot both be right.
> Most likely explanation: the earlier result came from a **name/keyword search that matched a different advertiser's page**, which is the documented failure mode from batch 11–20 (a keyword sweep there returned Colgate and Nestlé ads for clinic queries). **Treat the "1 active ad" as unconfirmed and do not build a wedge on it.** If Tilak still has that screenshot, checking which Page name it shows would settle this in seconds.

**Google Ads — 0 creatives** for vitalsklinic.com `[A]`. Previously `pending`; now a clean zero.

**Practo — Prime confirmed** (4.5★, 146 patient stories, ₹1,000 consultation, Dr. Harish Prasad B.R, entity match verified) `[S]`. Not re-tested this run; retained.

**JustDial:** not located. `pending`.

## Lead Sources
Phone (4 numbers), WhatsApp click-to-chat, call-back form, website, Instagram, Google Business Profile (3 listings), **Practo Prime (only confirmed paid channel)**.

## Mystery Shop Findings
`pending — Tilak to run.`

## Reviews Analysis `[A]`
**BTM Layout — 1,892 reviews, 4.7★.** Distribution: 1,649×5★ · 145×4★ · 15×3★ · 13×2★ · **70×1★ (3.7%)**. 165 newest sampled, most recent 2026-08-07, oldest in sample 2026-01-19 — roughly 165 reviews in 7 months, a fast, healthy flow.

**A recurring, cross-branch booking-failure pattern — three independent reviewers:**

- **1★, 2026-07-03 (BTM):** *"Had got appointment for 12 PM. Doctor doesnt turn up till 1 PM. After I leave, I get a call from reception that the doctor has just reached the clinic. Wonder why they dont teach time sense to doctors in medical college."* → Owner reply, in full: *"It was medical emergency so it was delayed"*
- **1★, 2026-07-15 (Whitefield):** *"It's worst service...no hospital board...after Waiting for one hour doctor did not came.. pathetic"* → Owner reply: *"Sir we called u so many times but there was no response since heavy traffic doctor got late sorry for inconvenience"*
- **2★ (BTM):** *"Despite making appointments at 11am the doctor only makes time to see you for about 3-5 mins almost 1 hour beyond the scheduled appointment time... I sat in the lobby waiting for long periods of time only for my consultation to be treated like a quick 2 minute chat."* Also describes pressure to buy medicines from the in-house pharmacy "well above online price options" at ~₹4k per consult. **No reply.**
- **1★ (BTM):** receptionist dispute over a wrong serum handed over against prescription. **No reply.**

**Owner reply behaviour — an asymmetry worth naming.** Positive reviews receive long, warm, personalised replies (*"Hi Tanmaya, thank you for the wonderful 5-star review!..."*). The two most detailed negatives received **no reply at all**; the two that did got one curt line each. Someone is actively working the review channel — but only the happy half of it.

**Fake-review check:** no burst pattern; language is specific and varied on both sides. Reads organic.

> The earlier pass sampled 8 of 272 reviews and found **zero negatives**, concluding "no reviews mentioning wait times... surfaced." At 165 reviews the pattern above is unmistakable. This is the clearest demonstration in the batch of why sample depth changes the answer.

## Marketing Analysis
No direct ad spend on either platform (Meta zero now verified, Google zero confirmed). Acquisition runs on **Practo Prime + a very large organic review base**. The operational weakness is not lead capture — it is what happens to a lead who has already booked.

---
```
funnel_break_stage:       Booking / No-show
recommended_entry_sku:    No-show recovery — PROVISIONAL
confirm_via_mystery_shop: Basis changed from the earlier pass. With Meta spend now unconfirmed, dead-lead reactivation loses its footing. What replaces it is stronger and screenshot-provable: three independent unreplied/curtly-replied reviews across two branches describing confirmed appointments where the doctor did not appear for an hour or more — plus 3-5 minute consults after hour-long waits. That is a booking/no-show break, not a response-speed break. Confirm via §2 test #6 (book a consult, then reschedule last-minute, and see whether anyone proactively recovers the slot) and test #1 (does the WhatsApp click-to-chat ask anything before booking, or just take the slot?). If booking turns out clean, fall back to the Practo Prime aggregator row, since Prime is the only confirmed paid channel.
status:                   Qualified
depth_mode:               Standard (Apify re-run)
unverified_fields:        Meta ad status (direct contradiction with prior pass — Apify says zero, twice); Electronic City GBP listing not captured; source of the "272 reviews" figure; JustDial; avg treatment value
```
