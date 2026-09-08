# Session handoff — new_leads_1 ads + Instagram audit

**Session date** 2026-08-15 · **Written for** picking this up cold in a new Claude Code session
**Working dir** `/Users/stilak/Documents/Valence-Ops-Sales/new_leads_1`

Read this file first, then `OPEN-CHECKS-2026-08-15.md` (that's where the work resumes).

---

## 0. What to say to start tomorrow

> Read `new_leads_1/SESSION-HANDOFF-2026-08-15.md`. I want to close the open checks in
> `OPEN-CHECKS-2026-08-15.md`, starting with Calyx and the Augusté discrepancy.

Everything below is context for that.

---

## 1. What was asked

Repeat the `05 Prospects/SE Bangalore Scrape/Ads Presence 2026-08-14.md` run — Meta ads (Y/N), Google ads (Y/N),
Instagram followers — against the clinics in `new_leads_1/`.

Stated purpose: *"check what sources they have for lead flow, approximately judge how much money
they're already putting into getting leads, and get an estimate of their enquiry volume."*

**Two thirds of that purpose is not obtainable and was not delivered.** See §6.

Mid-session the approach was switched, on instruction, from Claude-in-Chrome to **Apify** (a $10
budget was mentioned — the real figure is **$5**, see §5).

---

## 2. Where things stand

**42 unique clinics. 26 fully settled on all three layers. 16 open.**

| State | Count |
|---|---|
| **Spending now** (ad in last 30 days) | **16** |
| Dormant (ad history, nothing in 30d) | 2 |
| No paid presence found | 12 |
| Unresolved | 12 |

| Layer | Yes | No | Unconfirmed | Unresolved |
|---|---|---|---|---|
| Google | 11 | 25 | 6 | 0 |
| Meta | 10 | 20 | 0 | 12 |
| Instagram | **42 / 42 resolved, none dead** | | | |

Main deliverable: **`ADS-PRESENCE-2026-08-15.md`**
Open work: **`OPEN-CHECKS-2026-08-15.md`** ← resume here
Machine-readable: **`results.json`** (one record per clinic, all three layers merged)

### The four heaviest advertisers
1. **The aesthetic Co.Skin** — both platforms, 23 Meta ads (8 in 30d), 25 Google creatives live
   14 Aug, 20,893 IG. Widest spender in the cohort by a distance.
2. **Aurilueur** — both platforms, both current to 14 Aug, much smaller base.
3. **divine aesthetics** — Meta confirmed (4 ads, 12 Aug); Google identity unconfirmed.
4. **The Aesthetic Edge** — Google only, 25 creatives, live 14 Aug.

---

## 3. Method — and the three traps that shaped it

### Meta must be queried BY PAGE, never by keyword
Tested twice, failed twice:
- Ad Library keyword search for *"The Aesthetic Edge"* → 8 ads from **"Wonderful novel story"**
- keyword search for *"divine aesthetics"* → **Jaipur Literature Festival**, *Fabzie Decore*

Meta keyword search matches **ad body text, not advertiser**. Same trap as the SE cohort.
So: find the clinic's Facebook page → query `apify/facebook-ads-scraper` with `onlyTotal: true`
against the **page URL**. Pages came from the clinics' own websites (21 free), then name-corroborated
search.

**Then confirm every page against the page name Meta itself returns.** That arbiter rejected
`Iva Mukherjee Chatterjee` (a customer's post), `Sabina's Cravings` (a blogger), `Doctors.co.in`
(a directory), `Chaser Aspira`, and `Cradle Children Hospital`.

### Country / entity always has to be checked
`Hairline Clinic Brisbane Pty Ltd` — an **Australian** advertiser — surfaced inside an India-region
query and would have been logged as a live Google advertiser for Hairline International. This is
this cohort's version of the SE cohort's UAE `DERMA ELITE POLYCLINIC L.L.C`.

### Name rarity is not identity
`ANIL ABRAHAM` (Google, 1 creative) is a bare personal name. Still unconfirmed. Precedent: the
SE cohort's verified, India-based, ten-live-ad `Mradula Singh` who turned out to be the wrong person.

### Three states, plus one
**Yes** / **Unconfirmed** (near-name match, could be another business) / **No** (page or advertiser
confirmed, zero ads) / **Unresolved** (check could not be completed). *Unresolved is not No.*

---

## 4. Gotchas that will cost time if forgotten

| Thing | Detail |
|---|---|
| **Google via curl is dead from this IP** | `adstransparency.google.com` serves a `/sorry/` CAPTCHA. Must run in-browser |
| **Google RPC needs XSRF headers** | `X-Framework-Xsrf-Token` + `X-Same-Domain`, lifted from a request the page makes itself (hook `window.fetch`, then type in the page's own search box) |
| **Region must be an array** | `f.req={"1":q,"2":10,"3":10,"4":[2356],"5":{"1":1}}` — `4` as a bare int silently returns `{}` for every query, including Amazon |
| **Country comes back inline** | Field `3` of each hit is the country code, so the `Based in:` check is free |
| **Apify google-search-scraper returns results OUT OF ORDER** | **Join on `searchQuery.term`, never by position.** A positional join mislabelled every row mid-session (Richmond got handed "Sunlight Skin Clinic"). Caught before it reached the report |
| **`activeStatus` on apify/facebook-ads-scraper** | Only `""`, `"active"`, `"inactive"` are valid. `"all"` errors |
| **`no_items` ≠ zero ads** | "Empty or private data" means the page wasn't resolved. A page that resolves with `totalCount: 0` is a real No |
| **Chrome extension dropped mid-session** | Browser fallback was unavailable for the last stretch. May need reconnecting |
| **IG source data was incomplete** | 5 clinics had no handle in the CSV. Two were recoverable free from their own website footers — always check `socials.json → ig_on_site` before paying for a search |

### Controls that passed (re-run these if results look odd)
- Google: `amazon` → 20 advertisers with country codes · `qzxwvunknownclinicxyz` → 0 hits
- Cross-check: **Augusté Skin** — SHORTLIST recorded 1 Meta ad / 5,076 followers on 14 Aug; this run
  independently got **1 Meta ad / 5,075 followers** on 15 Aug. Meta and IG layers reproduce.

---

## 5. Accounts, cost, and one security item

- **Spend: $1.1875 of $5.** Not $10 — `monthlyUsageCreditsUsd: 5` is the free credit;
  `maxMonthlyUsageUsd: 10` is the hard cap and needs a card. Cycle resets **2026-09-04**.
- Account used: **`wickered_plaza`** (nameistilak2005@gmail.com), free tier.
- The **older** Apify account `progressive_overalls` (jkstilak2005@gmail.com) is **exhausted** —
  $12.25 against a $10 cap, blocked until 2026-09-08.
- ⚠️ **The `mcp__apify__*` MCP server is still bound to the exhausted account.** The new token was
  added as a separate server `apify-http`, but MCP servers connect at session start so its tools
  were not available this session. Work was done via the **Apify REST API directly**. Either restart
  the session to pick up `apify-http`, or keep using the REST API.
- ⚠️ **Both Apify tokens are in `/Users/stilak/.claude.json` in plaintext** and were printed to
  terminal this session. Worth rotating and confirming that file isn't in any backup or sync.

Actor costs actually paid: `apify/facebook-ads-scraper` $0.0058/page · `apify/instagram-profile-scraper`
$0.0026/profile · `solidcode/ads-transparency-scraper` $0.0015/item · `apify/google-search-scraper`
$0.0045/page.

---

## 6. What this method CANNOT tell you — stated plainly

The ask included *"how much money they're putting into leads"* and *"estimate enquiry volume."*
**Neither is derivable and neither was estimated.**

- No ad library publishes budget.
- Ad **count** is not spend — one creative can outspend twenty.
- Meta impression ranges are **EU-political-only**, not available for India.
- Enquiry volume is a further inference on top of a number that doesn't exist.

What you *do* have is **presence + recency + intensity** — enough to rank who is actively buying,
not to price it. Do not let the ad counts in the report get read as a spend proxy.

---

## 7. Open work — the resume point

Full detail with per-clinic evidence is in **`OPEN-CHECKS-2026-08-15.md`**. Summary:

**Group A — closing it changes a verdict (5):** Calyx Skin Lab · Hairline International ·
divine aesthetics · Dr. Anil Abraham · moon aesthetic
**Group B — near-settled, ~2 min each (2):** Rock Aesthetics · dr_shettys_cosmetic_centre
**Group C — dormant either way, skip (3):** New Look · the radiant clinic · Pigment
**Group D — Meta page never located (6):** Seoulful · bodyscience · dermo glamm · Meraki ·
Masa · cradle of youth

### Suggested order
1. **Calyx Skin Lab** — its source URL carries `gclid` + `gad_campaignid=22135492301` +
   `utm_medium=ppc`. Somebody clicked a **live Google ad** to generate that URL, yet no advertiser
   named Calyx exists in the transparency centre. **Most likely miss in the cohort.** Currently
   filed Unresolved; the evidence says Spending now. Search for the parent/legal entity.
2. **The Augusté discrepancy** — see below. Outranks all 16.
3. **Hairline + divine aesthetics** — both currently sit in *Spending now* on an advertiser whose
   name isn't the clinic's.
4. **Rock + dr_shettys** — both link their own FB page from their own site, so the page is theirs;
   `no_items` most likely means never advertised. Converts two Unresolved to clean No.
5. **bodyscience (13,420 IG) + dermo glamm (8,349 IG)** — real audiences, Meta half unknown.
6. Skip Group C.

### ⚠️ The unresolved discrepancy — it is about the method, not a clinic
`Shortlist 2026-08-14.md` records **Augusté Skin: "Google: ~43 total · 10/30d · 4/7d"**, sourced to
Tilak on 14 Aug and marked `confirmed`. **This run found no Google advertiser named Augusté.** A
region-IN query for "Auguste Skin" returns exactly one advertiser: `SIDDANTH SARAF`.

Both cannot be right. If Augusté advertises under a legal name that a name search cannot reach, then
**every "No" in both this cohort and the SE cohort is systematically under-counting** — both were
produced by name search. Closing this validates or invalidates the whole instrument.

**To close:** open the Augusté transparency page used on 14 Aug and record the advertiser name
exactly as it appears.

---

## 8. Files in this folder

**Read these**
| File | Holds |
|---|---|
| `ADS-PRESENCE-2026-08-15.md` | The report — headline, per-clinic verdicts, IG table, rejected false positives, hypothesis-fenced interpretations |
| `OPEN-CHECKS-2026-08-15.md` | The 16 open checks with per-clinic evidence and what to do |
| `results.json` | All three layers merged, one record per clinic. **Start here for any new analysis** |

**Inputs**
`zone-leads.md` (19, Central zone) · `Clinic_Directory_Template….csv` (24 rows → 23 unique;
the `_all` copy is byte-identical, ignore it) · `targets.json` (42 normalised, IG handles resolved)

**Scripts — all re-runnable**
`build_targets.py` → targets.json · `find_socials.py` → socials.json (free FB/IG link extraction from
clinic sites) · `gads_recency.py` → gads_detail/ (needs `APIFY_TOKEN` env var; caches per clinic id,
so reruns are free) · `consolidate.py` → results.json (merges everything, applies the reject lists)

**Raw captures**
`google-ads-raw-2026-08-15.json` · `meta-ads-raw-2026-08-15.json` · `instagram-raw-2026-08-15.json` ·
`google-ads-recency.json` · `meta-ads-summary*.json` · `instagram-summary.json` ·
`fb_search_results.json` · `fb_search_round3.json` · `socials.json`

**Note on `consolidate.py`:** it carries two hand-maintained reject lists —
`GOOGLE_UNCONFIRMED` (identity not settled) and `GOOGLE_REJECT_ADVERTISERS` (Brisbane/foreign
entities), plus an inline exclusion of `Cradle Children Hospital`. **As open checks get closed,
update these and re-run it** rather than editing `results.json` by hand.

---

## 9. Things deliberately NOT done

- **Gate A was not run.** `Shortlist 2026-08-14.md` argues hard kill #10 (named decision-maker on a
  personal channel, ~2 min/clinic) should run *before* expensive research — on batch-7 evidence,
  3 of 10 dossiers need never have been written. It was flagged in the plan and you chose to proceed
  with ads/IG on all 42. Still unrun for this cohort.
- **No mystery shop.** Per `CLAUDE.md` that is always yours, and per `wedge-signal-entry.md` §4
  scraping cannot determine "response slow or none" — so **no wedge can be assigned from this data**.
  This is a shop-ordering input, not a send list.
- **No outreach drafted.** Nothing here has been written to Notion.
- **No spend or enquiry-volume estimates.** See §6.

---

## 10. Standing rules that applied (from `../CLAUDE.md`)

- **§5** — never state to a clinic anything not traced to a dated, verifiable fact in that clinic's
  dossier. The 16 *Spending now* clinics are the **only** ones where *"you're paying for enquiries
  right now"* is a fact. For the other 26 it is an assumption and cannot be said.
- **§0.1 rebuttal test** (`wedge-signal-entry.md`) — a paused ad account is not evidence of a
  conversion problem. "It got expensive" / "the campaign ended" are always available. Do not build a
  hook on the 2 dormant clinics.
- **Notion overrides this repo on per-clinic outbound state.** Nothing in this folder says whether
  any of these 42 has been contacted. A dossier here means *researched*, not *contacted*.

### One reading worth not over-trusting
16/42 spending here vs 4/35 in the SE cohort looks like a much richer list. The likelier explanation
is **selection** — SE was a polygon scrape of whoever existed, this list was hand-assembled, and a
hand-picked list of clinics that look successful will over-represent advertisers. **Do not treat 38%
as a Bangalore base rate.**
