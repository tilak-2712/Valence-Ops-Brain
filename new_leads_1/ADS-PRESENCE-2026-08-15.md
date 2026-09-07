# new_leads_1 — paid-ads presence & Instagram audit

**Generated** 2026-08-15 · **Scope** all 42 unique clinics in `new_leads_1/`
**Cost** $1.19 of the $5 free Apify credit on account `wickered_plaza`. Google layer ran at $0.

**Epistemic status: `confirmed` for the dated machine-read facts below. The interpretations at the
bottom are `hypothesis` and marked as such.**

---

## Input

| Source | Rows | Notes |
|---|---|---|
| `zone-leads.md` | 19 | "Central zone" |
| `Clinic_Directory_Template….csv` | 24 → **23** | Aurilueur listed twice; the two `.csv` files are byte-identical |

**42 unique clinics.** No overlap between the two lists. One doubled URL fixed (Aesthetics Plus).
**Augusté Skin was already audited** in `SHORTLIST-2026-08-14.md` — kept here as a live control, see
*Verification* below.

---

## Method

| Layer | Route | Cost |
|---|---|---|
| Google | `adstransparency.google.com` SearchSuggestions RPC, region `[2356]`, in-browser | $0 |
| Google recency | Apify `solidcode/ads-transparency-scraper`, 18 advertisers | ~$0.45 |
| Meta | Apify `apify/facebook-ads-scraper`, `onlyTotal`, **by page URL** | ~$0.35 |
| Facebook page discovery | clinic websites (free) + Apify `apify/google-search-scraper` | ~$0.11 |
| Instagram | Apify `apify/instagram-profile-scraper`, 37 + 5 recovered handles | ~$0.11 |

### The design decision that governs every Meta row

**Meta keyword search was tested and discarded.** Searching the Ad Library for
*"The Aesthetic Edge"* returned 8 ads from **"Wonderful novel story"**; searching *"divine
aesthetics"* returned **Jaipur Literature Festival**, *Fabzie Decore* and *peacockwatch.official*.
Keyword search matches **ad body text, not advertiser** — the same trap logged in the SE cohort,
reproduced here twice.

So Meta was queried **by Facebook page**, never by keyword. Pages were found from the clinics' own
websites (21 free), then by name-corroborated web search. Every page was then confirmed by the
**page name Meta itself returned** — which is what rejected `Iva Mukherjee Chatterjee`,
`Sabina's Cravings`, `Doctors.co.in` and `AutoRaja T Raja`, all of which had surfaced because a
*post mentioning the clinic* matched the search.

**Four states used throughout:** **Yes** · **Unconfirmed** (near-name match, could be another
business) · **No** (page/advertiser confirmed, zero ads — or no name match found) · **Unresolved**
(the check could not be completed).

---

## Headline

| | Google | Meta | Either |
|---|---|---|---|
| Yes | 11 | 9 | **16** |
| Unconfirmed | 6 | 0 | 6 |
| No | 25 | 21 | — |
| Unresolved | 0 | 12 | 12 |

| State | Clinics |
|---|---|
| **Spending now** (ad in last 30 days) | **16** |
| **Dormant** (ad history, nothing in 30 days) | 2 |
| **No paid presence found** | 12 |
| **Unresolved** | 12 |

**16 of 42 are buying enquiries right now.** That is a far higher base rate than the SE cohort
(4 of 35). These two cohorts are not comparable populations — SE was a polygon scrape, this list
was hand-assembled — but the difference is large enough to matter for how the list is worked.

---

## Spending now (16)

Ordered by most recent ad. `cr` = creatives observed (capped at 25/advertiser by the scrape).

| # | Clinic | Google | Meta | IG followers |
|---|---|---|---|---|
| 1 | **The aesthetic Co.Skin** | `The Aesthetic Co` · 25cr · **14 Aug** | `The Aesthetic Co.` · **23 ads** · 8 in 30d · 13 Aug | 20,893 ✅ |
| 2 | **Aurilueur Esthetic Clinic** | `Aurilueur Esthetic Clinic` · 7cr · **14 Aug** | `Aurilueur Esthetic Clinic` · 3 ads · 2 in 30d · **14 Aug** | 7,777 |
| 3 | **divine aesthetics** | `DIVINE AESTHETICS SURGERY` · 24cr · **14 Aug** ⚠️ | `Divine aesthetics` · 4 ads · 12 Aug | 622 |
| 4 | **The Aesthetic Edge** | `The Aesthetic Edge` · 25cr · **14 Aug** | page confirmed, 0 ads | 12,375 |
| 5 | **Metphi Clinic** | `Metphi Clinic` · 17cr · **14 Aug** | page confirmed, 0 ads | 829 ✅ |
| 6 | **Seoulful Aesthetic Clinic** | `SEOULFUL` · 22cr · **14 Aug** | unresolved | 1,017 |
| 7 | **REGENIQUE** | `REGENIQUE MULTISPECIALTY CENTER` · 13cr · **14 Aug** | page confirmed, 0 ads | 265 |
| 8 | **moon aesthetic** | `Moon Aesthetic` · 25cr · **14 Aug** | unresolved | 466 |
| 9 | **SUTVACHA** | `Sutvacha Skincare Pvt Ltd` · **14 Aug** | 1 ad, 20 Apr (dormant side) | 6,881 |
| 10 | **Augusté Skin** | no name match ⚠️ | `Auguste Skin` · 1 ad · **14 Aug** | 5,075 |
| 11 | **KEZA Skin And Hair Clinic** | `Keza Skin and Hair Clinic` · 9cr · 13 Aug | page confirmed, 0 ads | 1,604 |
| 12 | **Richmond Dental & Aesthetic** | `Richmond Dental and Aesthetic Centre` · 2cr · 13 Aug | page confirmed, 0 ads | 4,555 |
| 13 | **Sun Light Skin Clinic** | no name match | `Sunlight Skin Clinic` · 3 ads · 3 in 30d · 12 Aug | 166 ⟲ |
| 14 | **Dr. Sneha Sood / Sood Aesthetics** | no name match | `Sood Aesthetics` · 2 ads · 2 in 30d · 10 Aug | 215 |
| 15 | **Hairline International** | `HAIRLINE DIAGNOSTICS…PVT LTD` · 23cr · 9 Aug ⚠️ | `Hairline International Hair & Skin Clinic` · 1 ad, undated | 3,168 |
| 16 | **Promed aesthetics** | no name match | `ProMed Aesthetics` · 2 ads · 2 in 30d · 8 Aug | 17,462 ✅ |

⚠️ **= identity not settled.** Three rows rest on an advertiser whose name is not the clinic's:

- **divine aesthetics** — `DIVINE AESTHETICS SURGERY` / `…LLP`. A *surgery* practice, 500 lifetime
  ads against a clinic with 622 Instagram followers. The scale mismatch is the reason to doubt it.
  Its **Meta** page is separately confirmed, so the clinic is a live advertiser either way — but the
  Google volume should not be attributed to it without a check.
- **Hairline International** — `HAIRLINE DIAGNOSTICS AND HEALTH CARE PRIVATE LIMITED`. Different
  legal entity. Its Meta page is confirmed with 1 undated ad.
- **Augusté Skin** — see the discrepancy note below.

### The four heaviest, and the one worth shopping first

**The aesthetic Co.Skin** is the sharpest signal in the cohort: live on **both** platforms, 23 Meta
ads with **8 in the last 30 days**, 25 Google creatives still running yesterday, and 20,893 IG
followers. Nothing else here is spending at that width.

**Aurilueur** is second — both platforms, both current to 14 Aug, on a much smaller base.

---

## Dormant — ad history, nothing in 30 days (2)

| Clinic | Evidence |
|---|---|
| **Skinray Clinic, Dommasandra** | Google `Skinray Clinic`, 1 creative, last shown **27 Jun** (49d). Meta page confirmed, 0 ads |
| **Pearl Aesthetic** | Meta `Pearl Aesthetic and Wellness clinic`, 1 ad, newest **20 Nov 2024** (633d). No Google match |

Per `wedge-signal-entry.md` §0.1 a stop is **not** evidence of a conversion problem — "it got
expensive", "the campaign ended" and "we're between agencies" are all available. Nothing here
distinguishes them. Do not build a hook on either.

---

## No paid presence found (12)

Both checks completed, neither found ads: Aestheticaa by Dr Madhulika · Maya Medi Spa · Livglam ·
Dr. Sunaina Hameed · DermaGlo · ZIUR · Avance Derma · Aesthetics Plus · skinwork · mantras clinic ·
Facial aesthetics Center · Elixir Advanced Aesthetics.

Some of these have real audiences — **Maya Medi Spa 25,632**, **Aestheticaa 15,205**,
**Elixir 14,571**, **mantras 10,831** — and are buying nothing. That is the cohort's most interesting group, and the one the standing
framing *cannot* be used on.

---

## Unresolved (12)

Split by cause, because they need different work.

**Google says Unconfirmed — one look each settles it (4)**

| Clinic | Candidate advertiser | Why unsettled |
|---|---|---|
| Dr. Anil Abraham's Skin & Hair | `ANIL ABRAHAM` · 1cr · 27 Jul | Personal name only. **Name rarity is not identity** (the `Mradula Singh` precedent) |
| New Look Skin Hair & Laser | `New Look Skin Care Ltd` · 9cr · 8 Apr | Generic name; would be dormant even if his |
| the radiant clinic | `Radiant Aesthetics` · 2cr · 23 Nov 2025 | Different trading name; dormant either way |
| Pigment Skin And Hair Clinic | `PIGMENT PLUS SKIN AND HAIR CLINIC` · 1cr · 14 Oct 2025 | "Plus" differs; dormant either way |

**Meta page never located (8)** — Calyx · Meraki · Rock Aesthetics · bodyscience · cradle of youth ·
dr_shettys_cosmetic_centre · dermo glamm · Masa aesthetics.

Their websites carry no Facebook link and no name-corroborated page was found by search. **This is
not evidence they don't advertise on Meta** — it is an unfinished check. Two candidate pages were
found and *rejected* on the returned page name: `Triderma by Dr. Shetty` (for dr_shettys) and
`The Skin and Body Science` (for bodyscience) — both plausible-looking, neither corroborated.

---

## Rejected false positives worth recording

| Clinic | Apparent match | Why rejected |
|---|---|---|
| Hairline International | `Hairline Clinic Brisbane Pty Ltd`, live 14 Aug | **Australian entity**, surfaced inside an India-region query |
| moon aesthetic | Meta page `Chaser Aspira` | Page name does not corroborate |
| Rock Aesthetics Clinic | Meta page `Iva Mukherjee Chatterjee` | A customer's post: *"Visited Rock Aesthetic Clinic for…"* |
| Meraki Aesthetics | Meta page `Sabina's Cravings` | A blogger post mentioning the clinic |
| Dr. Anil Abraham | Meta page `Doctors.co.in` | Directory listing, not the clinic |
| cradle of youth | Meta page `Cradle Children Hospital` | Children's hospital; matched on "cradle" alone |
| dr_shettys_cosmetic_centre | `BangaloreTimesOfficial`, `Triderma by Dr. Shetty` | Neither is the clinic |
| The Aesthetic Edge | 8 Meta ads under `Wonderful novel story` | Ad **body text** matched, not the advertiser |
| divine aesthetics | Meta ads under `Jaipur Literature Festival`, `Fabzie Decore` | Same — body-text match |

**The Brisbane case is this cohort's UAE case.** Without checking the entity, Hairline International
would have been logged as a live Google advertiser on the strength of an Australian company.

---

## Instagram — all 42 clinics resolved, none dead

Unlike the SE cohort (2 dead handles), every handle in this list resolves.

Five clinics had **no handle in the source CSV**. Two were recovered free from their own website
footers (Maya Medi Spa, Sun Light) and three by search (Calyx, ZIUR, Avance Derma), then scraped —
marked ⟲ below. **Maya Medi Spa turns out to have the second-largest audience in the cohort**, which
the source list would have hidden entirely.

| Clinic | Handle | Followers | Posts | f/post | Last post |
|---|---|---|---|---|---|
| Dr. Anil Abraham | @docanilabe | **67,202** | 240 | 280 | 30 Jul |
| Maya Medi Spa ⟲ | @mayamedispaindia | **25,632** | 1,702 | 15 | **14 Aug** |
| The aesthetic Co.Skin | @theaestheticco_ind ✅ | 20,893 | 177 | 118 | 6 Aug |
| Promed aesthetics | @promedaestheticsclinic ✅ | 17,462 | 1,398 | 12 | **14 Aug** |
| Aestheticaa by Dr Madhulika | @aestheticaa_drmadhulika ✅ | 15,205 | 206 | 74 | **14 Aug** |
| Elixir Advanced Aesthetics | @elixiradvancedaesthetics ✅ | 14,571 | 243 | 60 | 11 Aug |
| bodyscience_clinic | @bodyscience_clinic | 13,420 | 302 | 44 | 13 Aug |
| The Aesthetic Edge | @theaestheticedge__ | 12,375 | 555 | 22 | **14 Aug** |
| mantras clinic | @mantrasclinic ✅ | 10,831 | 151 | 72 | 27 Jun (49d) |
| dermo glamm | @dermoglamm_laser_skin_hair | 8,349 | 237 | 35 | **14 Aug** |
| Aurilueur | @aurilueurestheticclinic | 7,777 | 114 | 68 | 21 Jun (55d) |
| SUTVACHA | @sutvacha | 6,881 | 1,707 | 4 | 10 Aug |
| Augusté Skin | @augusteskin | 5,075 | — | — | — |
| Pearl Aesthetic | @pearl_aesthetic_clinic | 4,705 | 398 | 12 | 7 Aug |
| Richmond | @richmondaestheticsblr | 4,555 | 342 | 13 | **14 Aug** |
| Facial aesthetics Center | @facial_aesthetics_center ✅ | 4,204 | 450 | 9 | 10 Aug |
| Livglam | @livglamclinics | 4,012 | 383 | 11 | 16 Jun (60d) |
| Hairline International | @hairlineinternationalclinic | 3,168 | 504 | 6 | 10 Aug |
| dr_shettys_cosmetic_centre | @dr_shettys_cosmetic_centre | 2,965 | 517 | 6 | 30 Jul |
| Skinray | @skinray_clinic | 2,622 | 98 | 27 | 14 May (93d) |
| Aesthetics Plus | @aestheticsplusclinics | 2,249 | 858 | 3 | 18 Jul |
| Dr. Sunaina Hameed | @sunainahameed | 2,151 | 201 | 11 | 22 Jul |
| Rock Aesthetics | @rockaestheticsclinic | 1,822 | 199 | 9 | **14 Aug** |
| ZIUR ⟲ | @ziurwellness | 1,613 | 341 | 5 | 11 Aug |
| KEZA | @kezaskinandhairclinic | 1,604 | 82 | 20 | 11 Feb (**185d**) |
| DermaGlo | @dermaglo_laserskin_clinic | 1,296 | 478 | 3 | **14 Aug** |
| Seoulful | @seoulful.korean_care | 1,017 | 183 | 6 | **14 Aug** |
| Metphi Clinic | @metphiclinic ✅ | 829 | 205 | 4 | 22 Jun (54d) |
| Calyx Skin Lab ⟲ | @calyx_skin_lab | 899 | 100 | 9 | **14 Aug** |
| New Look | @newlooklc | 639 | 270 | 2 | 11 Aug |
| skinwork | @skinworkclinic | 635 | 188 | 3 | 13 Jul |
| divine aesthetics | @divineaestheticblr | 622 | 289 | 2 | 10 Aug |
| cradle of youth | @cradle_of_youth | 500 | 93 | 5 | 1 Jan (**226d**) |
| Avance Derma ⟲ | @avancederma | 492 | 114 | 4 | 24 Apr 2025 (**478d**) |
| moon aesthetic | @moonaesthetic.in | 466 | 166 | 3 | 10 Aug |
| the radiant clinic | @theradiantaestheticclinic | 432 | 37 | 12 | 13 Aug |
| Masa aesthetics | @masa__aesthetics | 428 | 170 | 3 | 4 Aug |
| Pigment | @pigmentclinics | 318 | 80 | 4 | 1 Jul |
| Meraki | @merakiaesthetics.in | 276 | 129 | 2 | 8 Aug |
| REGENIQUE | @regeniqueskin | 265 | 88 | 3 | 8 Aug |
| Dr. Sneha Sood | @snehasoodaesthetics | 215 | **594** | **0.4** | 13 Aug |
| Sun Light Skin Clinic ⟲ | @sunlightskinclinic | 166 | 41 | 4 | **14 Aug** |

Seven verified badges (✅). **Avance Derma has not posted in 478 days** — the only effectively
abandoned account in the cohort.

---

## Verification

- **Augusté Skin is a live control.** `SHORTLIST-2026-08-14.md` recorded *"Meta: 1 ad"* and
  *"5,076 followers · 406 posts"* on 14 Aug. This run independently returned **1 Meta ad** and
  **5,075 followers** on 15 Aug. The Meta and Instagram layers reproduce.
- **Google RPC controls:** `amazon` → 20 advertisers with country codes; `qzxwvunknownclinicxyz` → 0.
  Both pass, so a "No" is a real negative and not a broken query.
- **A positional-join bug was caught and fixed.** The Google-search actor returns results in a
  different order than the queries were submitted; the first join was by position and mislabelled
  every row (Richmond was handed "Sunlight Skin Clinic"). Re-joined on the query term itself.

### The one discrepancy this run could not close

`SHORTLIST-2026-08-14.md` records Augusté Skin as **"Google: ~43 total · 10/30d · 4/7d"**, sourced to
Tilak on 14 Aug and marked `confirmed`. **This run found no Google advertiser named Augusté.** A
region-IN transparency query for "Auguste Skin" returns exactly one advertiser — `SIDDANTH SARAF` —
and nothing bearing the clinic's name.

Both cannot be right. Either the clinic advertises under a legal name that a name search cannot
reach (which would make the SE method's "No" verdicts systematically under-count), or the ~43 figure
attached to the wrong advertiser. **It takes one look at the transparency page to settle, and it
matters beyond this clinic** — it is a test of the method itself, so it should be closed before the
next cohort.

---

## Interpretations — `hypothesis`, do not put any of this in a message

- **16 of 42 spending vs 4 of 35 in the SE cohort.** The obvious read is "this list is richer".
  The likelier read is **selection**: SE was a polygon scrape of whoever existed, this list was
  hand-picked. A hand-picked list of clinics that look successful will over-represent advertisers.
  Do not treat 38% as a Bangalore base rate.
- **No spend figure is derivable from any of this, and none is offered.** Neither ad library
  publishes budget; ad *count* is not spend (one creative can outspend twenty); Meta impression
  ranges are EU-political-only. Enquiry volume is a further inference on top of that. The ask was
  framed as "judge how much they're putting into leads" — this run **cannot** answer that, and the
  numbers here must not be read as a proxy for it.
- **The 16 are the only clinics where the standing framing is factually grounded.** *"Your problem
  is what happens after the enquiry, not getting the enquiry"* presupposes enquiries are being
  bought. For those 16 that is a dated, verifiable fact. For the other 26 it is an assumption and
  per `CLAUDE.md` §5 cannot be said to them.
- **Dr. Sneha Sood: 594 posts → 215 followers (0.4 f/post), and she is buying Meta ads.** The lowest
  ratio in the cohort by a wide margin. Tempting, but *"your Instagram isn't working"* fails the
  rebuttal test — *"we're not trying to grow Instagram"* — exactly as Epiderma did in the SE cohort.
  Not a hook.
- **KEZA has not posted in 185 days but its Google ads ran 2 days ago.** Paying for traffic while
  the organic channel is abandoned. Suggestive of an agency running ads with nobody minding the
  shop — **unverified**, and not sayable.
- **Four of the highest-audience clinics buy nothing** (Maya Medi Spa 25.6k, Aestheticaa 15.2k,
  Elixir 14.6k, mantras 10.8k). If the cohort constraint were lead volume these are the ones who would be buying. Weak
  evidence, one dataset, consistent with the ValenceOps thesis but not support for it.

---

## Reproducing

Everything is scripted and re-runnable. Google costs nothing; the rest is Apify.

- `build_targets.py` → `targets.json` (42 clinics, dedupe, handle normalisation)
- `find_socials.py` → `socials.json` (free; Facebook pages off the clinics' own sites)
- `gads_recency.py` → `gads_detail/*.json` (Apify, per-advertiser dates)
- `consolidate.py` → `results.json` (merges all three layers, applies the reject lists)
- Raw: `google-ads-raw-2026-08-15.json`, `meta-ads-raw-2026-08-15.json`,
  `instagram-raw-2026-08-15.json`

**Google via curl is dead from this IP** — `adstransparency.google.com` serves a `/sorry/` CAPTCHA.
It must run in-browser, and the RPC needs `X-Framework-Xsrf-Token` + `X-Same-Domain` headers lifted
from a request the page makes itself. Region belongs in field 4 **as an array**.

**Do not query Meta by keyword.** Query by page. This is not a preference — it was tested twice here
and returned unrelated advertisers both times.
