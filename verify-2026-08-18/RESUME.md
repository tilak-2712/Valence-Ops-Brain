# Resume note — 2026-08-18, stopped mid-job

## Where it stands

| Column | Verified | Flagged | Pending |
|---|---|---|---|
| Google reviews | 57 | 1 (HK Permanent Make Up — no GBP under that name) | 0 |
| Google ads | 53 | 5 | 0 |
| **Meta ads** | **57** | **1** | **0** |
| Instagram | 30 | 0 | **26** |

`state.json` is current and authoritative. `FINAL-TABLE.md` is STALE — it predates the
Meta column being finished. Regenerate it before using it.

## The only work left
26 Instagram handles + follower counts, for rows where `ig_status == "PENDING"`.
All free — no Apify needed. Apify spend to date: $0.09 of $0.34 (FREE plan, resets 1 Sep).

## Method for the remaining Instagram work
**Use WebFetch on `https://www.instagram.com/<handle>/` — it works and is far faster than
driving the browser.** (Discovered late in the last run; the earlier plan of browser
navigation per profile is unnecessary.)

1. `WebSearch` restricted to instagram.com: `<clinic name> <area> Bangalore instagram`
2. **Verify the handle is theirs before recording** — bio/link should match the clinic's
   `website`, `phone` or `area` field in state.json. Near-identical handles are a real
   hazard: iSkin returns both `@iskin_clinics` and `@iskin_clinic`.
3. WebFetch the profile for the follower count.
4. Cannot confidently tie handle to clinic → leave null, `ig_status: FLAG-handle-unverified`.
   Handle resolves to nothing → `ig_status: dead`.
5. Already known dead, leave alone: SkinOcare `@skinocare.co.in`,
   Clinique Internationale `@drbhaveshgupta_`.

## Standing rule
Never write an unverified value. A blank plus a flag is correct; a guess is a failure.

## Meta findings from this run (already saved, do not redo)
Newly confirmed running Meta ads — each changes the clinic's priority tier:
- **Rejuvaderm** (4.7 · 508) — ~6 active, advertiser `Rejuvaderm`, latest 6 Aug
- **The Derma Theory** (4.7 · 243) — active, advertiser card confirmed
- **Maira Wellness Clinic** (4.6 · 195) — now live on BOTH platforms
- **Masa aesthetics** (5.0 · 67) — live on Meta while its Google account went dormant 72d ago

Downgraded: **Derma Elite** — 6 keyword hits, all other advertisers. No active Meta ads.

## Traps that cost time last run — do not rediscover
- Meta result counts are meaningless; keyword search matches ad BODY TEXT. Only an
  advertiser name on the card is evidence. (SkinChime→DramaReel, Vibrant→Naaptol.)
- Meta has no batch path: GraphQL capture, iframes (`frame-ancestors`), popups, and
  `search_type=page` were all tried and all fail.
- Google Ads Transparency `SearchCreatives` page size 200 returns an EMPTY SET instead of
  erroring. Use 40. Always run a known-positive control before trusting a negative.
