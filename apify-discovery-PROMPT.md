# MESSAGE 2 — THE RUN PROMPT (paste after Claude confirms Message 1)

Run the discovery batch now, using the context I gave you. Budget: **$5.00 total Apify free-tier credit — hard ceiling.** Target output: **15–20 qualified clinics** that pass every ICP gate.

Work in four phases. **Stop and report at the end of Phase 0 and Phase 1 before spending more.**

---

## PHASE 0 — Preflight (spend: $0)

1. Read `https://api.apify.com/v2/users/me/limits` as an MCP resource. Report **actual remaining credit**. If it is materially under $5, tell me and rescale the plan before continuing.
2. Run `fetch-actor-details` on each of these and report current pricing model + whether any is deprecated:
   - `compass/crawler-google-places`
   - `apify/instagram-profile-scraper`
   - `apify/facebook-ads-scraper`
   - `scrapesage/google-ads-transparency-scraper`
3. Post your budget allocation using the envelopes below, adjusted to real pricing:

| Phase | Purpose | Cap (`maxTotalChargeUsd`) |
|---|---|---|
| 1 | Google Maps discovery, metadata only, no reviews | **$1.40** |
| 2 | Instagram gate screen on the shortlist | **$0.70** |
| 3 | Deep enrichment on finalists (reviews + Meta ads + Google ads) | **$2.20** |
| — | Reserve for re-runs and gap-fills | **$0.70** |

**Stop here. Report Phase 0 and wait for my go-ahead.**

---

## PHASE 1 — Discovery, wide and cheap (cap $1.40)

Use `compass/crawler-google-places`. **Metadata only on this pass — set `maxReviews: 0`.** You only need review *count*, rating, category, website, phone, and socials to filter. Do not pull review text yet; that is Phase 3 and it is where the money goes.

Settings:
- `scrapeContacts: true`
- `maxReviews: 0`
- `maxCrawledPlacesPerSearch: 15`
- `timeout: 600`
- `language: "en"`, `countryCode: "in"`
- Split into **several calls of 4–6 search terms each**. Do not submit all terms in one run — that is exactly what timed out before.

Search terms — combine each of these with the Bangalore micro-markets from the context (rotate, don't hammer one area):

```
dermatology clinic
skin clinic
skin and hair clinic
cosmetology clinic
aesthetic clinic
medical aesthetics clinic
hair transplant clinic
trichology clinic
cosmetic dermatology
laser skin clinic
medspa
anti ageing clinic
```

Target: **180–250 raw place records** before filtering.

Then filter, on scraped data only, in this order (cheapest rejections first):

1. **Name-match against the exclusion list** (§4 of the context) — loose matching, ignore case/punctuation/`&` vs `and`/"Dr." variations/branch suffixes. When in doubt, exclude.
2. **Vertical filter** — drop everything in §2.2 and §2.3. Dental is a hard zero. Read the Google category *and* the name; both lie sometimes, so use whichever is more damning.
3. **Review count ≥ 20.**
4. **Chain size** — count distinct places sharing a brand name. 6+ branches or 3+ states = exclude.
5. **Has at least one of** website / Instagram / GBP with real contact info.

**Report:** raw place count, count dropped at each filter step (with reasons), and the surviving shortlist — target **45–65 candidates**. Name every clinic you dropped for being on the exclusion list so I can verify the match was right.

**Stop here. Report Phase 1 and wait for my go-ahead.**

---

## PHASE 2 — Instagram gate (cap $0.70)

For every shortlist candidate with a discoverable Instagram handle, run `apify/instagram-profile-scraper`. Batch the handles — the actor accepts an array, so this should be a small number of calls, not one per clinic.

If the Google Maps record has no IG handle, do **one** cheap check: look at the clinic's website footer or run a targeted web search for the handle. If you still can't find one, mark `IG: none found` and drop the candidate — the IG gate is mandatory.

Apply the gate from §2.5 of the context, strictly:

- Followers **≥ 1,000** — under this, reject
- Posts **≥ 20**
- Last post **within 60 days**
- Public account

Then compute, from the `latestPosts` field: average likes + comments across the most recent posts, and engagement rate = that average ÷ followers. Flag anything under **0.5%** as `engagement: suspect`.

Sort survivors: **preferred band 2,000–80,000 followers** ranks highest. Anything over **100,000** goes to a separate PARK list (max 3, clearly labelled, not counted toward the 15–20).

**Report:** the gate results as a table — clinic, handle, followers, posts, days since last post, engagement %, pass/fail, and reason for every failure. Target: **20–28 survivors** going into Phase 3.

---

## PHASE 3 — Deep enrichment on the finalists (cap $2.20)

Take the **top 18–22** survivors by IG quality + review count. Run all three:

**3a. Reviews** — `compass/crawler-google-places` again, this time on the specific place URLs, with `maxReviews: 60`, `reviewsSort: "newest"`. **Batch 5–6 places per call, `timeout: 600`.** Also pull the lowest-rated slice where the actor supports it.

From each: the full star distribution, the **1★ percentage**, whether the owner replies to negatives, the date of the most recent unanswered 1★, and — read the actual text — whether the **"paid upfront then silence"** pattern appears. Quote at most one short line per finding, business detail only, no patient names or clinical details.

**3b. Meta ads** — `apify/facebook-ads-scraper`, one Ad Library search URL per clinic, `active_status: "all"`, batched. Record: active ad count, earliest and latest ad dates, and the CTA destination (WhatsApp / Messenger / website / lead form). Note that dynamic-catalog ads legitimately return `{{product.brand}}` as body text — that is a real ad, not junk data.

**3c. Google ads** — `scrapesage/google-ads-transparency-scraper`, `resultType: "advertisers"`. **Do not skip this.** A Meta-only check has wrongly returned "no ads" in every batch we have run. Record advertiser status, first-seen date, and whether the account is currently active or dormant.

If a clinic shows **no ads on either platform**, do one cheap Practo / JustDial check (`apify/rag-web-browser` on the listing) for Prime badging or sponsored placement. If you cannot determine it, write `Aggregator paid listing: undetermined` — never infer it.

Run the §5.2 verification loop after every one of these calls.

---

## PHASE 4 — Output

Deliver three things.

### 4.1 A CSV, exactly these columns, in this order

```
clinic_name,vertical,area,city,branches,website,phone,email,instagram_handle,ig_followers,ig_posts,ig_days_since_last_post,ig_engagement_pct,google_rating,review_count,one_star_pct,oldest_review_date,owner_replies_to_negatives,meta_ads_active,meta_ads_count,meta_ad_cta,google_ads_status,aggregator_paid_listing,founder_name,founder_confidence,high_ticket_services,park_flag,icp_score,entry_wedge,wedge_status,evidence_line,source_confidence
```

Rules for the fields:
- `founder_confidence`: `confirmed` / `probable` / `unknown`. Never state a founder name without one.
- `high_ticket_services`: the specific ₹25k+ procedures you actually found evidence of. Blank if none — and if it's blank, the clinic should not be in this list.
- `icp_score`: 0–10.
- `entry_wedge`: from the routing table in §7 of the context. Exactly one.
- `wedge_status`: `PROVEN` (visible in scraped evidence) or `HYPOTHESIS` (depends on mystery-shop data you don't have). Most will be HYPOTHESIS. Be honest about it.
- `evidence_line`: one sentence, the single most screenshot-provable finding.
- `source_confidence`: `high` / `medium` / `low` — plus which actor it came from.

### 4.2 A short dossier per clinic — 8–12 lines each

Basic info · founder + confidence · contact ladder · Instagram read (followers, engagement, what they actually post, whether the founder has a personal account) · ads · reviews (distribution + the sharpest negative, quoted briefly) · the wedge and why the evidence points there · anything that would make me *not* want to pitch them.

### 4.3 A limitations section — mandatory

Be blunt. Cover:
- Total Apify spend, broken down by phase and actor
- Any actor run that partially completed, silently dropped items, or hit a cap — and what data is therefore missing
- Every founder name that is `probable` or `unknown`
- Every clinic where the wedge is a hypothesis and what mystery-shop test would settle it
- Any name-collision or geography call you made where you could have been wrong
- Clinics you excluded as near-matches to the exclusion list, so I can double-check the call

---

## Standing rules for this run

- **Never fabricate a field.** `undetermined` and `unknown` are correct answers. An invented one costs us a real conversation.
- **Do not soften a red flag** for tonal consistency. If a clinic has negligence allegations or looks like a cloned listing, say so plainly and flag do-not-pursue.
- **Do not return a dental clinic**, a salon, an ayurveda centre, or a corporate chain branch. This is the one thing I will check first, and one bad row makes me distrust the whole list.
- If you cannot reach 15 qualified clinics inside the budget, **return fewer and say why.** A short honest list beats a padded one. Do not pad with clinics that failed the Instagram gate.
- Report spend after every phase, running total against the $5.00 ceiling.
