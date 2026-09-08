---
date_created: 2026-08-14
date_modified: 2026-08-14
status: reference
---
# SE Bangalore — paid-ads presence & Instagram audit

**Generated** 2026-08-14 · **Scope** the 35-clinic working list in `Qualified Targets 2026-08-14.md`
**Cost** ₹0 / $0.00 — no Apify credits used. Account still holds ~$0.34 of its $5 monthly free tier.

**Epistemic status of this file: `confirmed` for the facts below, which are dated, machine-read
and reproducible. The *interpretations* at the bottom are `hypothesis` and marked as such.**

---

## Method — and why the raw counts in it are not the answer

| Platform | Route | Discriminator |
|---|---|---|
| Meta | Ad Library keyword search, in-browser fetch (`credentials: include`) | count of `page_name` in the embedded payload — **not** ad count |
| Google | `adstransparency.google.com` `SearchService/SearchSuggestions` RPC, region `[2356]` = India | advertiser legal name + `Based in:` on the advertiser page |
| Instagram | logged-out profile HTML, `og:description` | `<title>` shape distinguishes live from dead handle |

**The trap that governs every row.** Meta's keyword search matches *ad body text*, not advertiser.
Searching "SkinChime" returns 30 ads from *Love Romance*; "SKYE Skin & Hair Sciences" returns
*Myntra Beauty*. A non-zero ad count is therefore **not evidence the clinic advertises**. Only an
advertiser-name match counts. Every "no" below means *no page bearing this clinic's name was
found*, not *the search returned nothing*.

Three states used throughout: **Yes** (advertiser name matches the clinic) · **Unconfirmed**
(a near-name match exists but could be a different business — Tilak to verify) · **No**.

---

## Headline

**Updated 14 Aug after Tilak manually checked all 7 unconfirmed near-matches. `confirmed`.**

| | Meta | Google | Either |
|---|---|---|---|
| Yes | 4 | 5 | **9** |
| Unresolved | 2 | 0 | 2 |
| No | 29 | 30 | 26 |

**26 of 35 clinics show no paid-ads presence on either platform.** Treat that as the base rate for
this cohort, not as a per-clinic fact — Meta search is name-based and a clinic advertising under a
differently-named page would read as "No" here.

### The distinction that matters more than yes/no

Ad-library totals are lifetime. Recency splits the 9 advertisers into three states that call for
completely different conversations:

| State | Clinics | What it means |
|---|---|---|
| **Spending now** | Aiconic, Cutis Epicorium, Allure, Zenith | Live budget on acquisition today |
| **Dormant** — ran ads, nothing in 30 days | DYU, Vivaa | Stopped. Reason unknown. |
| **Recency unknown** | Rejuvaderm, Derma Elite, The Derma Theory | Meta page match only; no date check run |

The three "recency unknown" rows are a gap, not a finding. They were confirmed by advertiser-name
match on Meta before the recency question was being asked, and no one has checked whether those
pages are currently running anything.

---

## Advertisers (9)

Ordered by current activity. Ad counts marked *(TS)* were read by Tilak off the ad-library
transparency pages on 14 Aug and supersede the machine-read counts in the previous version.

### Spending now (4)

| Clinic | Meta | Google | Ad activity |
|---|---|---|---|
| Aiconic Skin Clinic | No | **Yes** | `Aiconic skin private limited` · verified · **22 ads** |
| Cutis Epicorium HSR | No | **Yes** | **17 total · 10 in 30d · 9 in 7d · 0 yesterday/today** *(TS)* |
| Allure Skin Hair Laser | No | **Yes** | **10 total · 2 in 30d · 1 in 7d · 1 yesterday** *(TS)* |
| Zenith Aesthetic Care | **Yes** | No | **3 active Meta ads** *(TS)* |

Cutis Epicorium is the sharpest signal in the cohort — nine ads inside seven days, then nothing for
two. That is a live account being actively managed, not a dormant one.

### Dormant — ad history, nothing in the last 30 days (2)

| Clinic | Meta | Google | Ad activity |
|---|---|---|---|
| DYU Aesthetics | unresolved | **Yes** | **5 total · 0 in 30d** *(TS)* |
| Vivaa Wellness Center | unresolved | **Yes** | **5 total · 0 in 30d** *(TS)* |

### Confirmed advertiser, recency never checked (3)

| Clinic | Meta | Google | Evidence |
|---|---|---|---|
| Rejuvaderm | **Yes** | No | Meta page `Rejuvaderm`, 14 refs |
| Derma Elite Skin Care | **Yes** | No | Meta page `Derma Elite skin care clinic` |
| The Derma Theory | **Yes** | No | Meta page `The Derma Theory` |

**Do not treat these three as active.** Name-match only. Whether the pages are currently running
ads is unknown and takes one look at each Meta page to settle.

---

## Resolved to No by manual check (2)

| Clinic | Prior near-match | Verdict *(TS, 14 Aug)* |
|---|---|---|
| Epiderma Skin & Hair | Meta `eEpiderma Skin Laser & Hair Transplant`, 10 refs | **No Google ads. No Meta ads.** `eEpiderma` is a different business |
| Dr Mradula's Aesthetica | Google `Mradula Singh` · verified · 10 ads | **No Google ads. No Meta ads.** Not her |

The `Mradula Singh` case is worth keeping: an uncommon first name, identity-verified, India-based,
ten live ads — and still the wrong person. Name rarity is not identity.

## Still unresolved (2)

| Clinic | Open question |
|---|---|
| DYU Aesthetics | Meta page `DYU Healthcare` (14 ads) — same business or not? Google side is settled |
| Vivaa Wellness Center | Meta page `VIVAA Wellness Clinic` (2 ads) — "Center" vs "Clinic". Google side is settled |

Both were checked on Google, not Meta. If either Meta page is theirs, that clinic moves from
**dormant** to **spending now**, which flips how it should be approached.

## Rejected false positives worth recording

| Clinic | Apparent match | Why rejected |
|---|---|---|
| Derma Elite Skin Care | `DERMA ELITE POLYCLINIC L.L.C`, 5 Google ads | **Based in United Arab Emirates.** Name-identical, wrong country. |
| CLINIQUE / Dr Idris | `La Clinique Monte-Carlo Eyes & Hair Surgery` | Monaco |
| Dr. Pai Skin Hair | Meta page `Dr. Jamuna Pai's SkinLab` | different, much larger Mumbai brand |
| Allure Skin Hair Laser | Meta page `VK Allure Derma Clinic` | different business |
| Tricho Derma Clinic | Meta page `Dr. Derma Tricho Hair & Skin Aesthetics` | word-order coincidence |
| Skin Aura Clinic | `AURA AESTHETIC SKIN AND HAIR CLINIC`, `SKIN AURA BRAIN & SPINE NEURO CENTRE` | unrelated |
| Cutis Epicorium HSR | Meta page `Epicorium Skin Clinic - Kochi` | different city; the HSR branch's own ads are on Google |
| Epiderma Skin & Hair | Meta page `eEpiderma Skin Laser & Hair Transplant` | confirmed a different business *(TS, 14 Aug)* |
| Dr Mradula's Aesthetica | Google `Mradula Singh` · verified · 10 ads | confirmed not her *(TS, 14 Aug)* |

The UAE case is the one to remember: without the `Based in:` check, Derma Elite would have been
logged as a Google advertiser and it is not.

---

## Instagram

### Two handles in the source doc do not exist

| Doc claim | Reality |
|---|---|
| SkinOcare → `@skinocare.co.in`, "follower count pending" | **handle does not resolve** |
| Clinique Internationale → `@drbhaveshgupta_`, "follower count pending" | **handle does not resolve** |

Both return a 605,19x-byte page with a bare `<title>Instagram</title>` — byte-identical to a
control request for a deliberately nonsensical handle, and structurally different from a live
profile (which returns `(@handle) • Instagram photos and videos`). Verified twice, three hours
apart in method (JSON API and HTML), same result.

This retires job 1 in the source doc's "Outstanding work" section. It was scoped as *"only the
follower number failed to fetch; these handles are confirmed and tied to the right business."*
**They are not confirmed and no scrape would have returned a number.** Both clinics likely do have
an Instagram — these were read off website footers and are stale or mistyped. Finding the real
handles is manual work, left for Tilak per instruction.

### The nine live accounts

| Clinic | Handle | Followers (14 Aug) | Posts | Doc said | Δ |
|---|---|---|---|---|---|
| DYU Aesthetics | @dyuaesthetics ✅verified | ~16,000 | 633 | 15,944 | ≈ |
| Aesthetic Grandeur | @aesthetic_grandeur_clinic | ~13,000 | **76** | 12,837 | ≈ |
| Amintri Skin & Hair | @amintri.skin | ~10,000 | **71** | 10,267 | ≈ |
| The Derma Theory | @thedermatheory | 5,993 | 746 | 5,996 | −3 |
| SkinChime | @skinchimeclinic | 5,525 | 1,058 | 5,531 | −6 |
| Derma Elite | @derma_elite_skincare ✅verified | 1,855 | 401 | 1,857 | −2 |
| Arvique Aesthetics | @arviqueclinic | 1,039 | 107 | 1,039 | 0 |
| Epiderma | @epidermaskinclinic | 201 | **846** | 201 | 0 |
| Dr. Pai | @dr.paiskin | 145 | 175 | 145 | 0 |

All nine confirm the source doc's numbers within normal drift. Two carry a **verified badge**
(DYU, Derma Elite) — a field the original scrape did not capture.

Account names differ from clinic names in three cases, which matters for how outreach addresses
them: `@skinchimeclinic` presents as **"Dr Arpita | Dermatologist in Bangalore"**, `@dr.paiskin`
as **"Dr Ravish Pai"**, `@epidermaskinclinic` as **"By Dr Dharam & Dr Abhilasha"**. These are
doctor-led personal brands, not clinic brands.

---

## Interpretations — `hypothesis`, do not put any of this in a message

- **Epiderma: 846 posts → 201 followers.** The highest post count in the cohort and the
  second-lowest audience. Sustained effort, no compounding. A real asymmetry, but "your Instagram
  isn't working" fails the rebuttal test (`wedge-signal-entry.md` §0.1) — the obvious reply is
  *"we're not trying to grow Instagram."* Not a hook as it stands.
- **Amintri (71 posts / 10K) and Aesthetic Grandeur (76 posts / 13K)** sit at ~140–180 followers
  per post, against 5–20 for everyone else in the list. Could be paid promotion, an agency, or
  purchased followers. **Unverified, and unusable in outreach without evidence.**
- **9 of 35 have ad history; at most 4 are spending today.** If that holds, the cohort's constraint
  is unlikely to be lead volume — consistent with ValenceOps' positioning, but this is one weak
  reading of one dataset and is not evidence for it.
- **Two clinics ran ads and stopped** (DYU, Vivaa — 5 ads each, nothing in 30 days), and a third
  went from 9 ads in a week to zero for two days (Cutis Epicorium). The tempting read is *"they
  stopped because the leads didn't convert,"* which is exactly the ValenceOps thesis. **It does not
  survive the rebuttal test** (`wedge-signal-entry.md` §0.1): the doctor's obvious reply is *"we
  stopped because it got expensive"* or *"the campaign ended"* or *"we're between agencies."* A
  stop is not evidence of a conversion problem, and nothing in this file distinguishes the causes.
  Do not build a hook on a paused ad account.
- **The 4 currently spending are the only ones where the standing framing is factually grounded.**
  "Your problem is what happens after the enquiry, not getting the enquiry" presupposes enquiries
  are being bought. For Aiconic, Cutis Epicorium, Allure and Zenith that is a dated, verifiable
  fact. For the other 31 it is an assumption, and per `CLAUDE.md` §5 it cannot be said to them.

---

## Reproducing

No API key needed for any of it; nothing here consumed Apify credit.

- Google: POST `adstransparency.google.com/anji/_/rpc/SearchService/SearchSuggestions?authuser=0`,
  form body `f.req={"1":"<query>","2":10,"3":10,"4":[2356],"5":{"1":1}}`. **The region belongs in
  field 4 as an array** — the shape in the earlier working notes returns `{}` for every query,
  including Amazon, which looks exactly like a true negative and is not one. Script:
  `05 Prospects/SE Bangalore Scrape/gads.py` (in scratchpad; move it in if this becomes routine).
- Meta: must run from a real browser — plain curl gets a JS challenge, and the old
  `/ads/library/async/search_ads/` endpoint now 404s. Fetch the Ad Library HTML in-page and count
  `page_name` occurrences.
- Instagram: logged-out profile HTML, `og:description`. Live vs dead is decided by `<title>`.
  Avoid the `/api/v1/users/web_profile_info/` JSON route — it throttles to HTTP 400 after ~4 calls.


---
Related: [[05 Prospects/SE Bangalore Scrape/Qualified Targets 2026-08-14|Qualified Targets 2026-08-14]] · [[01 Playbooks/wedge-signal-entry|wedge-signal-entry]] · [[CLAUDE|CLAUDE]] · [[05 Prospects/Scrape 2026-07-19/The Derma Theory|The Derma Theory]]
