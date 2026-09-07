# SE Bangalore clinic scrape — paused state (2026-08-10)

**Status: BLOCKED on Apify monthly usage limit. Nothing is lost — resume steps below.**

## The blocker

- Account usage: **$6.995 against a $5.00/month cap** (free tier).
- Consequence: no new runs can start, **and the datasets already scraped are locked for reading**.
- Unblock: raise the monthly limit or upgrade at https://console.apify.com/billing/subscription
  (a limit increase is enough — the data already exists, it just can't be read while locked).

## What is already scraped and waiting (do NOT re-run these)

| Area | Dataset ID | Items | Quality |
|---|---|---|---|
| HSR Layout | `G1PeyKWqrRxu4dvmi` | 78 | ✅ good — 7.4 km² polygon, valid |
| Sarjapur Road | `I4yz9GTpkIVKRYvbf` | 37 | ⚠️ partial — polygon covered only the HSR Sector-5 end |
| Bommanahalli | `uF8Qd6NQTinzjzdRj` | 4 | ❌ near-empty — 0.53 km² polygon |
| Electronic City | `KQd47YTCr0W4zXrUQ` | 0 | ❌ discard — 0.01 km² polygon |
| Bannerghatta Road | `Wm1fgbATUE3f6F7il` | 0 | ❌ discard — 0 km² polygon |

## Root cause of the empty areas (important — don't repeat)

The Google Maps actor's free-text `locationQuery` geocodes Bangalore localities through Nominatim,
which returned **degenerate polygons** for four of five areas:

- `"Electronic City, Bangalore, India"` → geocoded to **"Prime City Apartments"**, a single building,
  polygon area **0.01 km²**. The run found 117 places and discarded **76 as `outOfLocation`**,
  then reported status **SUCCEEDED with 0 items**.
- `"Bannerghatta Road, ..."` → a road centreline, polygon area **0 km²**.
- `"Bommanahalli, ..."` → 0.53 km², far smaller than the real locality.
- `"Sarjapur Road, ..."` → snapped to the HSR Sector-5 end (3.73 km²), missing the whole corridor.

**Fix: pass `customGeolocation` bounding boxes instead of `locationQuery` for Bangalore localities.**
Always check the run log line `📡 Created N map polygons with total area: X km2` before trusting output —
anything under ~1 km² for a locality means the geo-fence is wrong and results will be silently empty.

## Ready-to-run inputs for the four areas still needed

Actor: `compass/crawler-google-places`. Common settings used:

```json
{
  "searchStringsArray": ["dermatologist", "skin clinic", "hair transplant clinic", "aesthetic clinic", "cosmetology clinic"],
  "maxCrawledPlacesPerSearch": 30,
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

Per-area `customGeolocation` (coordinate order is **[longitude, latitude]**):

- **Electronic City**
  `{"type":"Polygon","coordinates":[[[77.645,12.815],[77.715,12.815],[77.715,12.878],[77.645,12.878],[77.645,12.815]]]}`
- **Bannerghatta Road** (Dairy Circle → Gottigere corridor)
  `{"type":"Polygon","coordinates":[[[77.572,12.79],[77.628,12.79],[77.628,12.95],[77.572,12.95],[77.572,12.79]]]}`
- **Sarjapur Road** (Agara → Dommasandra corridor)
  `{"type":"Polygon","coordinates":[[[77.63,12.855],[77.785,12.855],[77.785,12.945],[77.63,12.945],[77.63,12.855]]]}`
- **Bommanahalli**
  `{"type":"Polygon","coordinates":[[[77.596,12.878],[77.65,12.878],[77.65,12.925],[77.596,12.925],[77.596,12.878]]]}`

Note: only ~3 concurrent runs fit the 16 GB account memory ceiling (4 GB each). A 4th is rejected.

## Method note that worked

`scrapeContacts: true` + `scrapeSocialMediaProfiles.instagrams: true` returns
`instagramProfiles.followersCount` / `.username` attached to the correct clinic, resolved from that
clinic's own website. This removes the need for a separate Instagram actor and the risk of
matching the wrong handle by name.

## Remaining steps once unblocked

1. Run the four area inputs above; verify each run's polygon area line in the log.
2. Merge all datasets, dedupe by `placeId`.
3. Filter: `reviewsCount >= 100` AND `totalScore >= 4.0`.
4. Exclude the 80 already-scraped clinics (list held in the session; normalize names before matching —
   watch variants like "Advanced Gro Hair & Glo Skin" vs "Advanced GroHair GloSkin").
5. Output: `clinic name | rating & review count | website Y/N | instagram Y/N | follower count`.
