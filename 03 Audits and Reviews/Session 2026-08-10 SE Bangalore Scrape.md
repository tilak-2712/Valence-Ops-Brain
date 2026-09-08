---
date_created: 2026-08-10
date_modified: 2026-08-10
status: reference
---
# Session log — SE Bangalore clinic scrape (2026-08-10)

Complete context for this session: the ask, every decision, what ran, what broke, and where it
finished.

> **STATUS: COMPLETED (with partial coverage).** The limit was raised mid-session by $3, the
> geocoding was fixed, and the scrape finished. **Deliverable: `05 Prospects/SE Bangalore Scrape/New Clinics Table 2026-08-10.md`
> — 52 core new targets.** Sections 1–10 below describe the *first, blocked* attempt and are kept
> as the record of what went wrong; **§14 holds the final outcome and supersedes §9–§11.**

Companion files:
- `05 Prospects/SE Bangalore Scrape/New Clinics Table 2026-08-10.md` — **the deliverable**
- `05 Prospects/SE Bangalore Scrape/raw/*.json` — all 251 raw records
- `05 Prospects/SE Bangalore Scrape/process.py` — re-runnable filter/dedupe/exclusion pipeline
- `scrape-southeast-bangalore-RESUME.md` — **superseded**; only its Sarjapur/Bommanahalli polygons
  are still live (also reproduced in §14)

---

## 1. The request

Scrape skin / aesthetic / dermatology / cosmetology / hair clinics from **Bangalore South-East &
outer expansion areas**, specifically these five:

1. HSR Layout
2. Electronic City
3. Sarjapur Road
4. Bommanahalli
5. Bannerghatta Road

**Qualification criteria:**
- Decent Google Business Profile: **100+ reviews** (floor, no upper bound — "150+" was not a separate cutoff)
- **4.0+ star rating** minimum
- Has a website? (Y/N)
- Has an Instagram? (Y/N) — and if yes, **follower count only**

**Required output format:**

```
clinic name | review rating & no. | website (Y/N) | instagram (Y/N) | follower count
```

**Hard constraint:** rule out, at the start, every clinic already on the previously-scraped list of
80 (reproduced in §2). Keep that list side by side during the work rather than filtering at the end.

**Scope discipline requested by Tilak:** "what I've asked you is just a basic look up and check, not
deep crawling or scraping. use just what's enough to get the job done." Do not overdo; do not
under-deliver; self-correct rather than drift.

**Process instruction:** stop and ask questions before or mid-session rather than guessing.
Parallelise with subagents only if it does not increase error rate.

---

## 2. Exclusion list — 80 already-scraped clinics (do NOT return these as new)

Preserved verbatim from the session, since it existed only in conversation.

**Elective clinics / healthcare:**

1. Aura Cutisurg Clinic — dermatology, hair, cosmetic procedures, general surgery
2. Clinic Next Face — skin, hair, anti-ageing, injectable aesthetics
3. Dr. Sculpt Aesthetic Clinic — plastic surgery, cosmetic surgery, hair transplant, dermatology
4. Dr. Keshav's Skin, Hair, Cosmetic & Laser Clinic — dermatology, hair, cosmetic, laser
5. Ministry of Skin — dermatology, hair, skin, injectables
6. DNA Skin Clinic — dermatology, hair transplant, cosmetic dermatology, laser
7. Dr. Karishma Aesthetics — plastic surgery, cosmetic surgery, dermatology, body contouring
8. Dr. Ritika Shanmugam Skin, Hair & Aesthetic Clinic — dermatology, skin, hair restoration, injectables
9. Dr. Dixit Cosmetic Dermatology Clinic — cosmetic dermatology, hair, injectables, lasers
10. Anew Cosmetic Clinic — cosmetic dermatology, plastic surgery, hair, dental aesthetics
11. Dr. Swetha's Cosmoderm Centre — dermatology, hair, skin, aesthetics
12. Dr. Juvita Aesthetics — skin, hair & laser clinic
13. Vtiara Hair & Skin Clinic — hair transplant, hair loss, dermatology, lasers
14. Iridescent Aesthetics — dermatology, skin, hair, injectables, body fat
15. Dr. Tina's Skin Solutionz — dermatology, skin, hair
16. Cozmo Blis — plastic surgery, cosmetic surgery, liposuction
17. The Glow Clinic — medical dermatology, clinical aesthetics
18. Skinology Centre — skin / dermatology clinic
19. AvatarLuxe Aestheticians — aesthetics
20. Idha Skin, Hair & Laser Clinic — skin, hair, laser
21. LA CROWN Dermatology Aesthetic Clinic — dermatology, aesthetics
22. Aesthetica Veda Clinic — aesthetic clinic
23. Sparsha Skin Care Clinic — skin care
24. Pruthvi Children's and Skin Clinic — paediatrics + skin
25. Pranav Skin and Cosmetology Clinic — skin, cosmetology
26. Venkat Center for Aesthetic Health — hair, skin, plastic surgery
27. DermaZeal Clinic — dermatology
28. Dermaville Skin Clinic — skin
29. Dr. Rai's Skin & Hair Clinic — skin & hair
30. Dr K Srinivasa Murthy's Skin & Cosmetology Centre — skin, cosmetology
31. Ridhi's Skin and Hair Transplant Clinic — skin, hair transplant
32. CosMediQ Hair Transplant and Skin Clinic — hair transplant, skin
33. Nishka Skin Clinic — skin
34. ProSkincare Esthetics — skin care / esthetics
35. Neo Follicle Hair Transplant Clinic — hair transplant
36. Skinmatics — skin
37. Subodha Skin And Cosmetic Clinic — skin, cosmetic
38. Dr. Saurav's Skin Clinic — skin
39. Dr. Sowmya's Skin and Hair Clinic — skin & hair
40. Advanced Gro Hair & Glo Skin Clinic — hair & skin
41. Artistry Clinics — aesthetics
42. Cura Care — GBP "corporate office" (home-visit therapy) — scrape anomaly
43. Praba's Vcare Health Clinic — hair & skin chain (flagged, excluded)
44. Aarha AesthetiQ — aesthetics
45. Contour Cosmetic Clinic — hair transplantation clinic (GBP)
46. Koza Aesthetic Care — aesthetic care (5-branch chain)
47. SS Aesthetic Clinic — skin care clinic (GBP)
48. Sanssouci Wellness Clinic — weight loss service (GBP)
49. Sparha Advanced Aesthetic Studio — skin care clinic (GBP)
50. Feather Touch Aesthetic Clinic & Academy — aesthetic clinic
51. Skin and Recon — skin, dermatosurgery / reconstruction
52. SkinFit Wellness — skin care clinic (GBP)
53. RUA Skin & Hair Center — skin & hair
54. Advanced GroHair GloSkin — hair transplantation clinic (GBP)
55. Chisel Dental Clinic — dental
56. Sky Dental Clinic — dental
57. Dr Tanisha's Emerge Dental Studio — dental
58. Aspen Dental Care — dental
59. Reneu Dental Studio — dental
60. Smiley House — multi-speciality dental
61. Small Bites — kids-only dental chain
62. Amaya Dental Clinic — dental
63. Smile Xpressions — multi-speciality dental
64. The Dental Axis — dental
65. Aesthete Lifestyle Dentistry — dental
66. Gejje's Marvella — plastic surgery clinic (GBP)
67. Haircosmos International — hair transplantation clinic (GBP)
68. Ara Skin Clinic — skin care clinic (GBP)
69. Dr. Priya's Skin & Hair Clinic — skin care clinic (GBP)
70. Akera Health — dermatologist / skin & hair
71. Derma Solutions — multi-speciality (dermatology, hair transplant, cosmetology)
72. Routines by Dr. Apoorva — dermatologist (GBP)
73. Theory of Skin — dermatologist (GBP)
74. Dermatonik — skin care clinic (GBP)
75. VIDA Skin & Hair Transplant — hair transplantation clinic (GBP)
76. Vitals Klinic — skin, hair, laser
77. Krity 360 — facial aesthetics, dental, hair
78. D White Feather — hair & skin
79. Dr AG Skin & Hair Clinic — skin, hair, hair transplant
80. Project Skin — dermatology, aesthetics

Tilak's note: *"80 unique clinics. outreach 4 and outreach-5 are re-dossiers of clinics already in
batch1-2, so they're merged here rather than double-counted."*

**Matching caution:** entries 40 and 54 ("Advanced Gro Hair & Glo Skin Clinic" / "Advanced GroHair
GloSkin") look like the same business listed twice. Normalize names before matching — do not compare
literally. Show excluded matches for audit rather than dropping them silently.

**Categories in scope** (from Tilak): dermatology/dermatologist · skin care clinic · skin & hair
clinic · skin, hair & laser · cosmetology · cosmetic dermatology · aesthetic clinic · medical
aesthetics · aesthetic studio · aesthetic academy · wellness clinic · hair transplantation ·
hair loss/trichology · laser skin · injectables/anti-ageing · body contouring/liposuction ·
plastic surgery · cosmetic surgery · dermatosurgery/reconstruction · general surgery ·
multi-speciality (derm + HT + cosmetology) · dental (all forms) · paediatrics + skin ·
weight loss service · corporate office (home-visit therapy).

---

## 3. Questions asked, and Tilak's answers

| Question | Answer |
|---|---|
| Is "100–150+ reviews" a 100 floor or a strict 150 cutoff? | **100+ is the floor**, no upper bound |
| Filter on star rating too, or review count alone? | **Yes — add a 4.0+ star minimum** |
| OK to spend Apify credits at ~30–60 actor calls? | **Yes, but keep it a basic lookup** — not deep crawling/scraping; use only what's enough |
| Parallelise with subagents, or sequential? | **Whatever gives near-zero error rate and is fastest**; report the chosen approach before starting |

Tilak then confirmed: *"yes go ahead. all the best."*

---

## 4. Approach decided (and stated to Tilak before starting)

**Batched-sequential in the main thread, not subagents.**

Reasoning given:
- The dedupe against the 80-clinic list is the highest-risk step. Splitting it across 5 subagents
  creates 5 independent applications of that list — the most likely source of a clinic wrongly
  dropped or wrongly kept.
- Google Maps scraping does not need subagents: the actor takes multiple search terms per run, so
  parallelism would multiply cost without saving wall-clock time.

Planned as ~3 actor calls: one Maps sweep → in-thread filter + dedupe → one Instagram pass.

**Risk flagged upfront to Tilak:** Instagram handles are not in Google Maps data, so resolving them
by name risks matching the wrong account. Commitment made: mark IG "Y" only where unambiguous, mark
uncertain ones "unconfirmed" rather than guessing a follower count.

**That risk was then eliminated** — see §5.

---

## 5. Method win: Instagram follower counts come free and correctly attributed

The actor `compass/crawler-google-places` supports:

- `scrapeContacts: true` — finds the business's social profiles **from its own website**
- `scrapeSocialMediaProfiles: { instagrams: true }` — enriches those profiles with follower data

Confirmed present in live output: `instagramProfiles.followersCount`, `.username`, `.profileURL`,
`.postsCount`, `.isBusinessAccount`, `.privateProfile`.

**Why this matters:** the handle is resolved from the clinic's own website, not guessed from its
name. This removes the wrong-account risk entirely and eliminates the need for a separate Instagram
actor. Keep this approach on future runs.

---

## 6. Actor configuration used

Actor: **`compass/crawler-google-places`** (Google Maps Scraper, id `nwua9Gu5YrADL7ZDj`)

```json
{
  "searchStringsArray": ["dermatologist", "skin clinic", "hair transplant clinic", "aesthetic clinic", "cosmetology clinic"],
  "maxCrawledPlacesPerSearch": 20,
  "language": "en",
  "countryCode": "in",
  "placeMinimumStars": "four",
  "skipClosedPlaces": true,
  "scrapeContacts": true,
  "scrapeSocialMediaProfiles": { "instagrams": true, "facebooks": false, "youtubes": false, "tiktoks": false, "twitters": false },
  "maxReviews": 0,
  "maxImages": 0,
  "scrapePlaceDetailPage": false
}
```

Deliberately kept shallow per Tilak's "basic lookup" constraint: **no review text, no images, no
detail pages, no leads enrichment, no email verification, no competitor analysis.**

**Pricing (FREE tier), for future budgeting:**
- $0.004 per place scraped
- +$0.001 per place per filter applied (min-stars and skip-closed each count)
- +$0.002 per place for contacts enrichment
- +$0.10 per 1,000 Instagram profiles enriched
- $0.00005 per actor start

**Account memory ceiling:** 16 GB total; each run takes 4 GB → **max 3 concurrent runs** in
practice. A 4th run was rejected with an explicit memory-limit error.

---

## 7. Runs executed — full ledger

| Area | Run ID | Dataset ID | Final status | Items | Verdict |
|---|---|---|---|---|---|
| HSR Layout | `fNC79A8I1d1UP8x5I` | `G1PeyKWqrRxu4dvmi` | SUCCEEDED | **78** | ✅ valid |
| Electronic City | `BxbTO6pEV6ipKwCPz` | `KQd47YTCr0W4zXrUQ` | SUCCEEDED | **0** | ❌ bad geo-fence |
| Sarjapur Road | `fa4egA5MRxuZo9K9x` | `I4yz9GTpkIVKRYvbf` | ABORTED | **37** | ⚠️ partial |
| Bommanahalli | `JalCIv7zOLzlrSCbd` | `uF8Qd6NQTinzjzdRj` | SUCCEEDED | **4** | ❌ bad geo-fence |
| Bannerghatta Road | `abnoGh5xaGgGjUXPu` | `Wm1fgbATUE3f6F7il` | SUCCEEDED | **0** | ❌ bad geo-fence |

**Raw total: 119 place records** — unfiltered, undeduped, uncompared against the exclusion list.

Note: Bannerghatta's first launch attempt was rejected outright on the memory ceiling; it was
re-launched after a slot freed. Sarjapur shows ABORTED — most likely evicted under the memory
ceiling when Bannerghatta started. Its 37 items are still valid data, just incomplete coverage.

---

## 8. Root cause of the empty areas — the important finding

The actor geocodes free-text `locationQuery` through Nominatim. For four of five Bangalore
localities it produced **degenerate polygons**, and the runs then discarded real clinics as
`outOfLocation` while still reporting **SUCCEEDED**.

Evidence from the run logs:

| Area | Geocoded to | Polygon area |
|---|---|---|
| HSR Layout | HSR Layout, Bengaluru South City Corporation | **7.4 km²** ✅ |
| Sarjapur Road | *Sarjapur Road, Sector 5, HSR Layout* — the wrong end of a ~15 km corridor | 3.73 km² ⚠️ |
| Bommanahalli | Bommanahalli, Bengaluru South | 0.53 km² ❌ |
| Electronic City | **"Prime City Apartments"** — a single residential building | **0.01 km²** ❌ |
| Bannerghatta Road | Bannerghatta Road, Lakkasandra — a road centreline | **0 km²** ❌ |

The Electronic City run is the clearest case. Its own summary line:

```
📊 0 places scraped | duplicate: 37 | seen: 117 | searchPages: 5 | paginations: 10
   | outOfLocation: 76 | notHavingMinimumStars: 4
```

It **saw 117 places and threw away 76 for being outside a polygon the size of an apartment block**,
then reported success with zero results.

### Rules to carry forward

1. **Do not use free-text `locationQuery` for Bangalore localities.** Pass `customGeolocation`
   bounding boxes instead.
2. **Always read the log line** `📡 Created N map polygons with total area: X km2` before trusting
   any output. Under ~1 km² for a named locality means the geo-fence is wrong and results will be
   silently empty.
3. **Watch the `outOfLocation` counter** in the run summary. A high value against a low scrape count
   is the signature of this failure.
4. This is a concrete new instance of the existing `MEMORY.md` rule that an Apify "Succeeded" does
   not mean real or complete data. It was that rule that caught this — without it, the conclusion
   would have been the false "Electronic City has no qualifying clinics."

---

## 9. Current blocker

**Apify monthly usage hard limit exceeded.**

- Usage: **$6.995 against a $5.00/month cap** (free tier)
- New runs are rejected: `Monthly usage hard limit exceeded`
- **Datasets already scraped are locked for reading**: `Dataset is locked because you have reached
  your monthly usage limit.` — this applies to both the raw API and the MCP tool
- Dataset **metadata** (item counts) is still readable; **items** are not

Consequence: the 119 captured records cannot be opened, so no filtering, no dedupe, and no table
could be produced. No clinic name from this scrape has been seen.

**Unblock:** raise the monthly limit or upgrade at
https://console.apify.com/billing/subscription — a limit increase suffices; the data already exists.

---

## 10. State of the deliverable — nothing verified yet

Answering the two questions Tilak asked at the end, recorded so the answers aren't lost:

**"How many clinics have we got?"** → **Zero qualified.** 119 is raw Google Maps records, not
qualifying clinics. Still to be applied: the 100+ review filter (only the star filter ran
server-side), dedupe by `placeId`, the 80-clinic exclusion, and category-noise removal (general
physicians, dental, salons pulled in by broad search terms). Realistic expectation: **single digits
to low teens** of genuinely new clinics, all from HSR Layout.

**"Are all of the clinics new ones not on my list?"** → **Unknown — assume not.** The exclusion list
was applied at **zero** points; it was planned for the merge step, which never ran. Expect
*significant* overlap: the usable records are all from HSR Layout, which is territory already
worked, and Sarjapur's polygon snapped onto the HSR Sector-5 end so those 37 likely duplicate the
HSR 78. Broad category searches surface the most prominent clinics first — exactly the ones already
on the list.

Also worth noting: **Electronic City and Bannerghatta Road — the two areas most likely to hold
untouched prospects — returned nothing at all**, and that is a geocoding failure, not an absence of
clinics.

---

## 11. Resume plan

1. Raise the Apify monthly limit (unlocks the existing datasets *and* permits new runs).
2. **Do not re-run HSR Layout** — `G1PeyKWqrRxu4dvmi` (78 items) is good data, already paid for.
3. Run the four areas below with `customGeolocation`. Max 3 concurrent.
4. After each run, verify the polygon-area log line before trusting output.
5. Merge all datasets; dedupe by `placeId`.
6. Filter: `reviewsCount >= 100` AND `totalScore >= 4.0`.
7. Apply the §2 exclusion list with normalized name matching.
8. Deliver **two** tables so the filtering is auditable:
   - New qualifying clinics: `clinic name | rating & review count | website Y/N | instagram Y/N | follower count`
   - Excluded-as-already-known, with the matched list entry shown
9. Estimated additional spend: ~$2–4.

### Corrected polygons (coordinate order is **[longitude, latitude]**)

- **Electronic City**
  `{"type":"Polygon","coordinates":[[[77.645,12.815],[77.715,12.815],[77.715,12.878],[77.645,12.878],[77.645,12.815]]]}`
- **Bannerghatta Road** (Dairy Circle → Gottigere corridor)
  `{"type":"Polygon","coordinates":[[[77.572,12.79],[77.628,12.79],[77.628,12.95],[77.572,12.95],[77.572,12.79]]]}`
- **Sarjapur Road** (Agara → Dommasandra corridor)
  `{"type":"Polygon","coordinates":[[[77.63,12.855],[77.785,12.855],[77.785,12.945],[77.63,12.945],[77.63,12.855]]]}`
- **Bommanahalli**
  `{"type":"Polygon","coordinates":[[[77.596,12.878],[77.65,12.878],[77.65,12.925],[77.596,12.925],[77.596,12.878]]]}`

Use `maxCrawledPlacesPerSearch: 30` for these (larger polygons split into more segments), with all
other settings from §6 unchanged.

---

## 12. Open items for Tilak

1. **Raise the Apify cap?** Nothing further is possible until this is done.
2. **Log the geocoding trap in `MEMORY.md`?** Offered but not done — `MEMORY.md` was not edited
   without permission, since it is Tilak's calibration record. It would sit naturally alongside the
   existing "Apify verification" entry in §2 as a confirmed, evidence-backed learning.
3. **Search-term breadth** — the five terms used were deliberately narrow per the "basic lookup"
   constraint. Worth confirming whether terms like "laser clinic", "trichologist", "cosmetic
   surgeon", or "medspa" should be added on the re-run.
4. **Area definitions** — the corrected bounding boxes are drawn generously (e.g. Bannerghatta Road
   as the full Dairy Circle → Gottigere corridor). Confirm these match the intended catchments.

---

## 13. Unrelated note from earlier in the session

`claude mcp list` output showed the Apify MCP server configured with its API token in **plaintext**
(`APIFY_TOKEN=apify_api_u3dh...`). It is visible in this session's scrollback. Worth rotating if that
output was shared anywhere.

---

## 14. FINAL OUTCOME (supersedes §9–§11)

Tilak raised the Apify cap from $5 to $10 (+$3 headroom) and asked to continue, with the standing
instruction: **save results incrementally so nothing is lost when the limit hits.**

### What was done

1. **Rescued the already-paid-for data first** — the 119 previously-locked records were dumped to
   `05 Prospects/SE Bangalore Scrape/raw/` before spending anything new.
2. **Built `autosave.sh`** — snapshots datasets to disk every 20s during runs, and only overwrites
   when it receives a valid non-empty JSON array (so a lock/error response can't clobber good data).
3. **Re-ran Electronic City and Bannerghatta Rd with `customGeolocation` bounding boxes.**
   Polygons verified before trusting output: **53.16 km²** and **108 km²** (previously 0.01 and 0).
4. Merged, filtered, deduped and exclusion-matched everything via `process.py`.

### Runs added this round

| Area | Run ID | Dataset ID | Items | Polygon |
|---|---|---|---|---|
| Electronic City | `25kk5jBVYxaZbExEg` | `ZJu2cruEq8uT8am2I` | **57** | 53.16 km² ✅ |
| Bannerghatta Rd | `pLwhIwnzePiGyedu3` | `0gaZO7T1bDDxghMDq` | **75** | 108 km² ✅ |

**Raw total: 251 records → 234 unique places after dedupe.**

### Final counts

| Bucket | Count |
|---|---|
| **A. Core new targets** | **52** |
| B. National chains (deferred per mega-brand rule) | 18 |
| C. Adjacent (dental-led / salon / homeopathy / hospital) | 12 |
| D. Excluded — already on the 80-list | 19 |
| Below 100 reviews / 4.0 stars | 90 |
| Category noise | 43 |

### Budget outcome — overshot

Spend reached **$12.14 against the $10 cap (~$2.14 over)**. Cause: the Electronic City polygon split
into **20 map segments**, costing far more per run than estimated from the earlier single-segment
runs. **No data was lost** — autosave held partial results throughout, and the complete datasets
were pulled before any lock took effect.

**Lesson for next time:** cost scales with *map segments*, not just with the per-search-term cap.
Check the log line `📡 The location was split into N map segments` right after launch; a large N on
a big polygon means budget accordingly or shrink the polygon.

### Two data-quality traps caught (both would have corrupted the deliverable)

1. **Platform Instagram handles.** `scrapeContacts` harvests *every* Instagram link on a website,
   including footer badges. Live examples: `@tv` (Instagram's own account, 1.9M followers) attributed
   to a small HSR clinic; `@wix` (a "built with Wix" badge, 880k) attributed to **two unrelated
   clinics**; `@ekacarehq` (a healthtech vendor) attributed to a third. Fix: a `PLATFORM_HANDLES`
   blocklist plus a name-affinity check; handles with no relation to the clinic name are reported as
   **"unconfirmed"** rather than given a follower number.
2. **Over-aggressive name normalization causing false exclusions.** Stripping too many words left
   only generic terms, which wrongly matched "Dr. Pai Skin, Hair & Healthcare" to "Dr AG Skin & Hair
   Clinic". Fix: a non-exact match now requires a shared **distinctive** (non-generic) word — "skin",
   "hair", "aesthetic" etc. don't count as evidence of identity.

### Exclusion-list findings for Tilak

- **Two clinics excluded that were NOT on the 80-name list** but are in Batch 1 per `CLAUDE.md` /
  `MEMORY.md`: **Evenly Skin and Hair Clinic** and **Sapphire Skin & Aesthetics Clinic**.
  → The 80-name list may be out of sync with the Notion tracker; worth reconciling.
- **One clinic caught only by its Instagram handle**, not its name: "Vitals Hair and Skin Clinic" →
  `@vitalsklinic` → **Vitals Klinic**, already on the list. Name-only matching would have missed it.
- "Advanced GroHair" appears at both HSR Layout and Electronic City; both matched list entries 40/54,
  which are themselves a duplicate pair.

### Coverage still outstanding

| Area | Records | Confidence |
|---|---|---|
| HSR Layout | 78 | ✅ good |
| Bannerghatta Rd | 75 | ✅ good |
| Electronic City | 57 | ✅ good |
| Sarjapur Rd | 37 | ⚠️ **under-covered** — still on the bad 3.73 km² polygon |
| Bommanahalli | 4 | ❌ **barely covered** — still on the bad 0.53 km² polygon |

**Sarjapur Rd and Bommanahalli were never re-run** — budget ran out. Their numbers reflect a broken
geo-fence, not a real absence of clinics. Corrected polygons, ready to run:

- **Sarjapur Rd** (Agara → Dommasandra corridor)
  `{"type":"Polygon","coordinates":[[[77.63,12.855],[77.785,12.855],[77.785,12.945],[77.63,12.945],[77.63,12.855]]]}`
- **Bommanahalli**
  `{"type":"Polygon","coordinates":[[[77.596,12.878],[77.65,12.878],[77.65,12.925],[77.596,12.925],[77.596,12.878]]]}`

Estimated cost to finish both: ~$1–2, given Sarjapur's corridor will split into multiple segments.

### Open items

1. **Re-run Sarjapur Rd + Bommanahalli** when budget allows — this is the main gap.
2. **Reconcile the 80-name list against the Notion tracker** (see Evenly / Sapphire above).
3. **Log the two Apify traps in `MEMORY.md`?** Offered, not yet done — `MEMORY.md` has not been
   edited without permission. Both are confirmed with direct evidence and belong alongside the
   existing "Apify verification" entry in §2.
