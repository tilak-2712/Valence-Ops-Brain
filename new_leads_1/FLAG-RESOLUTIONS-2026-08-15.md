# Flag resolutions 21–31 — Tilak's manual checks, 2026-08-15

**Source:** Tilak, transparency-centre and GBP checks run by hand on 2026-08-15.
**Epistemic status:** `confirmed` — first-party observation of live ad libraries and Google listings.
**Supersedes:** `results.json` and `OPEN-CHECKS-2026-08-15.md` on all eleven clinics below.
`results.json` is now stale for Calyx, Pigment, Meraki and Hairline and must not be quoted on them.

---

## The finding that matters more than any single clinic

**Three of the eleven reverse a Google verdict, all in the same direction — toward more spending.**

| Clinic | Machine-read 15 Aug | Manual check 15 Aug |
|---|---|---|
| Calyx Skin Lab | **No** — no advertiser named Calyx exists | `RASAA AESTHETIC SERVICES LLP` — **200 all-time, 62 in 30d, 59 in 7d** |
| Pigment Skin And Hair | Unconfirmed — 1 creative, last **14/10/2025** | **8 running through yesterday** |
| Meraki Aesthetics | **No** | **4 in 30d, 2 live in the last 7d** |

All three were produced by **advertiser-name search**, and all three were wrong because the clinic
advertises under a name the search cannot reach. This is exactly what the Augusté discrepancy
predicted, now confirmed three more times.

**Consequence:** every Google **"No"** in this cohort and in the SE cohort is a *name-search miss
away from being a Yes*. That includes the eleven "settled, nothing flagged" clinics in
`SHOP-QUEUE-REMAINDER-2026-08-15.md` Group 2 and the 26 no-paid-presence clinics in
`05 Prospects/SE Bangalore Scrape/Ads Presence 2026-08-14.md`. **Stop treating a name-search No as settled.**
The reliable route is the reverse one Calyx demonstrated: start from the clinic's own paid landing
page or GBP entity, not from its trading name.

## A second measurement error, mine

`gads_recency.py:50` sends `"maxResults": 25`. **Every "25 creatives" in every report I produced is
a cap, not a count.** Three clinics sit exactly on it — The aesthetic Co.Skin, The Aesthetic Edge and
moon aesthetic — so their true creative counts are **≥25, unknown**. Read every 25 as a floor.
Counts below 25 (Aurilueur 7, KEZA 9, REGENIQUE 13, Metphi 17, Seoulful 22, Hairline 23, divine 24)
are real.

---

## The eleven, resolved

| # | Clinic | Outcome | Moves to |
|---|---|---|---|
| 21 | Dr. Anil Abraham's | No ads found either platform; **no findable website**; **24 Google reviews, 4.6★** | **Park** |
| 22 | Hairline International | Domain confirmed `hairline.co.in` → the 23 Google creatives **are theirs**. 2 branches (Indiranagar 475 reviews, Koramangala ~265), both 4.4★ | **Tier 1** |
| 23 | dr_shettys_cosmetic_centre | Meta account exists, **zero ads**. Google already No | Settled — no paid presence |
| 24 | Rock Aesthetics Clinic | **No Meta ads account.** Google No. Good website, 1,822 IG, posts consistently | Settled — no paid presence |
| 25 | **Calyx Skin Lab** | `RASAA AESTHETIC SERVICES LLP` — **200 all-time · 62 in 30d · 59 in 7d, current through yesterday** | **Tier 1 — heaviest current buyer in the cohort** |
| 26 | New Look Skin Hair & Laser | No active Google or Meta. 638 IG / 270 posts | Settled — no paid presence |
| 27 | the radiant clinic | No active Google or Meta. 432 IG / 37 posts | Settled — no paid presence |
| 28 | Masa aesthetics | No active Meta, no active Google. ~400 IG / 170 posts | Settled — no paid presence |
| 29 | **Pigment Skin And Hair** | **8 Google ads running through yesterday** — reverses the 305-day-dormant record | **Tier 1** |
| 30 | **Meraki Aesthetics** | **4 Google ads in 30d, 2 live in 7d** — reverses a No | **Tier 1** |
| 31 | cradle of youth | Instagram, Meta and Google all dead | **Dropped** |

### Per-clinic notes

**21 · Dr. Anil Abraham's — park, and the reason changed.** It was parked on §1.2 mega-founder-brand
(67,202 followers). The volume signal now argues the same way independently: **24 lifetime Google
reviews** against a 67k personal following means the audience is the doctor's, not the clinic's, and
the clinic itself is small. Hard kill #3 (under ~20 enquiries/month) stays formally `undetermined` —
reviews are not enquiries — but 24 is the weakest volume signal in the cohort. No website findable is
its own problem: it is not hard kill #1 (Instagram and a GBP both exist), but it removes the route
Calyx just proved is the reliable one.

**22 · Hairline International — the wrong-entity flag clears.** With `hairline.co.in` confirmed as
the advertiser's domain, `HAIRLINE DIAGNOSTICS AND HEALTH CARE PRIVATE LIMITED` is the clinic's legal
entity and the **23 creatives, last seen 9 Aug, are theirs.** Two branches is not the chain I assumed,
so the hard kill #5 concern drops from likely to open — **but it is still open**: a Pvt Ltd with two
branches can have one owner or four. **Settle it at Gate A with the founder name, not before.**
**740 reviews across the two branches is the strongest inbound-volume signal in the whole cohort** —
the only clinic here where hard kill #3 looks comfortably passed.

**23 · dr_shettys** and **24 · Rock** — both resolve exactly as predicted: page exists, never
advertised. Two Unresolved become clean No's. They stay out of the queue on priority, not on doubt.

**25 · Calyx Skin Lab — the biggest find of the sweep.** `RASAA AESTHETIC SERVICES LLP`, 62 creatives
in 30 days and 59 in the last 7, current through yesterday. Against **899 Instagram followers and 100
posts**, this is a clinic buying nearly all of its attention. It is the sharpest
paid-versus-organic ratio in the cohort by a wide margin.
⚠️ **Two cautions.** (a) The advertiser is an **LLP** — hard kill #5, multi-partner sign-off, the same
structure that has Project Skin blocked in Notion Batch 2. Settle ownership before drafting anything.
(b) 59 creatives is not 59 rupees; creative count is not spend, and a clinic rotating creatives fast
may be testing, not scaling. The admissible fact is *"you are running Google ads right now, in
volume"* — nothing about budget.

**29 · Pigment Skin And Hair** — live, 8 ads through yesterday. One thing to close: the machine record
found the advertiser as `PIGMENT PLUS SKIN AND HAIR CLINIC` — **confirm the 8 live ads sit under that
same entity** and not a third name, before any of it is cited. 318 followers / 80 posts, so like
Calyx this is a buy-not-build clinic.

**30 · Meraki Aesthetics** — live, 4 in 30 days, 2 in the last 7. Same identity note as Pigment:
record the advertiser name exactly, since a name search had previously returned nothing.

**31 · cradle of youth — dropped on your call.** All three channels dead, no website, no Instagram
post since 1 January. Removed from the cohort; do not count it in any denominator.

---

## What this does to the queue

**Tier 1 goes from 15 to 19** — Calyx, Hairline, Pigment and Meraki all join on confirmed live spend.
**The cohort drops from 42 to 41** (cradle of youth removed).

That puts Tier 1 + Tier 2 at **24 clinics against a ~20 sitting size** (`wedge-signal-entry.md` §2),
so the first sitting has to be cut rather than simply run. Gate A is the correct instrument for that
cut — it removes clinics on whether a message can be written at all, which is a better filter than
follower count.

**Still open, and it now matters more than it did this morning:**

1. **Augusté** — the original discrepancy, still unrecorded. Three confirmed name-search misses make
   this the deciding test of how much of both cohorts needs re-checking.
2. **Ownership on Calyx (LLP) and Hairline (Pvt Ltd, 2 branches)** — hard kill #5 on the two clinics
   that just moved highest.
3. **Phone numbers and published hours for all 41** — unchanged, and still the reason nothing here
   is shoppable yet.
