---
name: clinic-audit-research
description: Run the Apify-powered pre-outbound research and audit pipeline for a batch of Indian elective clinics (skin, derm, cosmetology, hair transplant, dental). Use whenever the user pastes a batch of clinic names, LinkedIn URLs, or Instagram handles and asks to research, audit, scrape, enrich, or qualify them. Produces a verified dossier per clinic — contacts, GBP + review analysis, ad activity, disqualification screen, and a wedge routed from wedge-signal-entry.md — after a mandatory self-evaluation pass. Does not draft outreach (that is the personalized-outbound skill) and does not mystery-shop (the user does that).
---

# Clinic Audit Research — Apify Pipeline (v2)

## What this skill is for

Turn a raw list of clinic names/links into **verified, decision-ready dossiers** that populate
`clinic-audit-checklist.md` and hand off cleanly to the `personalized-outbound` skill.

The user should be **on** this loop (final review), not **in** it (correcting drafts). That means:
run the pipeline, verify it against Phase 2, screen it against Phase 6, route the wedge per
Phase 7, then **self-evaluate in Phase 8 and fix what fails before presenting anything.**
Never show a first draft.

### Hard scope boundaries

| In scope | Out of scope |
|---|---|
| Contacts, GBP + reviews, ads, socials, website, identity, disqualification, provisional wedge | **Mystery shop** — user does this personally, always |
| Populating checklist §0–§3, §5, §6 | Checklist §4 (mystery shop) — leave as `PENDING — user to run` |
| Flagging what wedge the data *points to* | Drafting DMs, video scripts, offers → `personalized-outbound-v2.md` |
| Reporting `funnel_break_stage` + `recommended_entry_sku` | Logging sends → `files/SEND_LOG.csv` (user reports notable outcomes only) |

**Every dossier ships as *provisionally complete*. Say so.** The wedge depends on mystery-shop data
this pipeline never produces.

> **Sequencing changed 2026-08-13 — read this before running a batch.** The mystery shop now runs
> *before* research, not after (`wedge-signal-entry.md` §2). The intended input to this skill is a
> shortlist of clinics **whose threads have already come back interesting**, not a raw list. Batch 7
> ran the old way and produced 25 dossiers against 0 shops — every wedge in it is untrustworthy.
> If handed a raw unshopped list, say so once, then proceed in Lite mode unless told otherwise —
> a full-depth dossier on an unshopped clinic is the most expensive way to be wrong.
>
> The mystery-shop Go/No-Go gate that used to sit in `clinic-audit-checklist.md` has been deleted;
> the gate is now the **rebuttal test** (§0.1) plus published-hours admissibility (§2.0).

---

## Document precedence

Read these before finalizing; they override anything in this file where they conflict:

1. **`wedge-signal-entry.md`** — authoritative for disqualification (§1), speed-to-lead SOP (§2),
   and the signal→wedge routing table (§3). **Never invent a wedge name.** Route to §3's exact
   wedge + opening frame.
2. **`clinic-audit-checklist.md`** — the field schema this skill fills.
3. **`files/OUTBOUND_MEMORY.md`** — overrides `personalized-outbound-v2.md` where they conflict.
4. **`MEMORY.md`** (project root) + auto-memory — standing calibration.
5. **Notion "Valence Ops Leads Tracker"** — *if the connector is available*, check it for existing
   status/priority/owner before researching, and treat it as authoritative for those three fields.
   If it is not authorized in the session, note that and proceed — do not block the batch, and do
   not guess a clinic's tracker state.

---

## Privacy & data-handling rules

Google reviews and social comments contain **real patients' names and medical details.** This
pipeline reads them for business diagnosis, not to build a picture of any individual.

- Quote only what establishes the **business** finding. A review proving "no owner replies to
  complaints" does not require the reviewer's full name or their diagnosis.
- **Minimize patient identifiers.** Prefer `"a June 2026 1★ reviewer"` over a full name. Use a name
  only when it is genuinely load-bearing (e.g. the user must locate that exact review to respond
  to it) — and then only the name as publicly displayed, never combined with clinical detail.
- **Never restate clinical specifics** (test results, diagnoses, procedure outcomes for a named
  person) beyond the minimum needed to convey severity. `"alleges a serious adverse drug reaction"`
  carries the signal; the lab values do not.
- **Never compile** patient information across sources, and never scrape follower/liker lists to
  identify patients. Staff/contact discovery only (see Phase 4).
- Everything collected is **public business information for B2B prospecting.** If a step would only
  make sense as profiling an individual patient, don't run it.

---

## Phase 0 — Intake, depth mode, preflight, pre-screen

### 0.1 Normalize the batch
Clinic name, any LinkedIn profile/company URL, any IG handle, stated locality (default Bangalore).

### 0.2 Ask once for LinkedIn URLs, then proceed regardless
Direct-URL profile pulls cost `$0.004` vs `$0.10` for a name search — ~25x cheaper — *and* dodge the
search actor's daily cap. Ask once. **If they're not available, continue with the cheaper sources
(GBP → website team page → company page) rather than stalling the batch.**

### 0.3 Pick a depth mode
Match effort to how much is actually in question. Default **Standard**; state which mode you're using.

| Mode | Runs | Use when |
|---|---|---|
| **Lite** | GBP + reviews + Meta/Google ads + website + basic contacts | Wedge is likely obvious from GBP alone; large batch; low credit; urgent triage |
| **Standard** | Lite + LinkedIn person + Instagram profile + aggregator check | Default for a normal batch |
| **Deep** | Standard + IG contact graph + LinkedIn company people + per-branch analysis | Ambiguous identity, high-value target, multi-branch chain, or contacts are the bottleneck |

Escalate a single clinic to Deep mid-batch when it earns it (identity unresolved, no reachable
contact, chain detected). Don't run Deep across the board by default — that's the waste this
mode system exists to prevent.

### 0.4 Actor-health preflight (before spending)
Actors change pricing, schema, and reliability without notice. For each actor the batch will use:
- Confirm it still exists and isn't deprecated (`fetch-actor-details`)
- Check `successRate` and monthly users — treat a sharp drop or <90% as a warning
- Diff the input schema against the call you're about to make (fields get renamed/removed)
- Check pricing hasn't moved enough to change the batch estimate
- Note the **fallback actor** for anything critical

If a primary actor looks unhealthy, switch to its fallback and say so in the limitations section.

### 0.5 Cheap hard-kill pre-screen
Run the low-cost hard-kill checks (Phase 6 §1.1) *before* deep enrichment. Three are answerable from
a single GBP pull plus a two-minute look:
- No website **and** no Instagram **and** no GBP → kill #1
- Oldest Google review < 12 months old → kill #2 (operating under a year)
- **No named decision-maker anywhere — GBP, website team page, IG bio → kill #10.** *(Added
  2026-08-13.)* If no doctor is named, no personalization is possible, so no message can be written.
  Batch 7 discovered this **after** writing complete dossiers for Project Skin, Dermatonik and
  Haircosmos — 3 of 10 dossiers wasted on a check that costs two minutes.

Deep-enrich only what survives. `wedge-signal-entry.md` §1.1 is explicit: *"disqualify immediately,
do not audit further."*

### 0.6 State the plan
Batch size, depth mode, actors, rough cost estimate, and any preflight concerns — before running.

---

## Phase 1 — Raw collection

Use **real Apify actors**, never web search as a substitute for a scrapable field. Batch multiple
clinics into single actor calls where the input accepts an array.

*(Web search and page fetches remain fully valid for what scrapers don't cover: identity
disambiguation, discovering additional branches, news/legal/regulatory findings, and obscure
contacts. The rule is only about substitution where a verified scraper exists.)*

### Verified actor roster

| Purpose | Actor | Notes from live use |
|---|---|---|
| GBP + reviews + contacts + socials | `compass/crawler-google-places` | The workhorse — one call returns metadata, phone/email/IG/FB/LinkedIn, reviews, review distribution. **Split into batches of 5–6 clinics** and set `timeout: 600`; a 13-clinic run with 120 reviews each **timed out at 500s** having completed only 17 places. |
| Meta ads | `apify/facebook-ads-scraper` | Reliable. One Ad Library search URL per clinic, `active_status=all`, batched. |
| Google ads | `scrapesage/google-ads-transparency-scraper` | `resultType: "advertisers"`. **Never skip** — a Meta-only check has wrongly reported "no ads" in every batch so far. |
| LinkedIn person (URL known) | `harvestapi/linkedin-profile-scraper` | Preferred path. Pass URL directly. `$0.004`, no cap. Use email-search mode (`$0.01`) when founder contact matters. |
| LinkedIn person (name only) | `harvestapi/linkedin-profile-search` | ⚠️ **Own daily free-tier cap (~10 calls/session), separate from account credit.** Fails *silently* with `statusMessage: "free user run limit reached"` while reporting SUCCEEDED. Spend it on the highest-value unconfirmed names first, not list order. |
| LinkedIn company people | `harvestapi/linkedin-company-employees` | 98.7% success, 20.8k users. Only when a **company** page URL exists. |
| Instagram profile | `apify/instagram-profile-scraper` | Returns bio, followers, external URL, **and per-post like/comment counts** in `latestPosts` — read that nested field, it is free engagement signal. |
| Instagram following list | `coderx/instagram-followers-following-scraper-no-cookies-login` | `scrape_type: "following"` **only — never followers.** Following is small, curated, staff-heavy. Followers are mostly unrelated patients: expensive, low yield, and a privacy problem. Fallback: `dead00/...-no-cookies` (cheaper, less proven). |
| Website content | `apify/website-content-crawler` | **Cap at 5–8 pages per site.** An uncapped run hit 205 pages and timed out. Prioritize `/team`, `/about`, `/doctors`, `/contact`. |

### Banned / default-off

- ❌ **`s-r/google-maps-contact-details`** — silently rate-limits (HTTP 429, 0 items, still reports
  SUCCEEDED). Superseded by `compass/crawler-google-places` with `scrapeContacts: true`.
- ⏸️ **`apify/instagram-comment-scraper`** — off by default. Rationale (user-validated, and
  consistent with `personalized-outbound-v2.md`): WhatsApp is the real booking engine; IG/FB
  commenters are a small minority. Use only if a specific clinic visibly runs its funnel through
  IG DMs. Post-level like/comment *counts* from the profile scraper are sufficient proxy evidence.

### Aggregator paid-listing check (Standard+)

`wedge-signal-entry.md` §1.3: not running Meta ads is **not** a disqualifier — check
**Practo Prime / JustDial paid listings** as a substitute "paying for leads" signal. This unlocks
the §3 row *"Practo Prime / JustDial paid listing · slow response → Dead-lead reactivation
(aggregator)"*, which is otherwise invisible.

**Known weak step — no verified actor yet.** At runtime: search the Apify store for a Practo/
JustDial actor, else fall back to `apify/rag-web-browser` on the clinic's listing and look for Prime
badging / sponsored placement. **If it cannot be determined, write
`Aggregator paid listing: undetermined` — never infer it.** Report back which method worked so this
line can be upgraded to a named actor.

---

## Phase 2 — Verification loop (after *every* actor call)

Apify `SUCCEEDED` means "the code exited," **not** "the data is real." Apply all six:

1. **Coverage** — item count vs. inputs submitted. A silent drop is the strongest failure signal,
   stronger than any status field.
2. **Error/summary KV record** — many actors write their real failure to a separate key-value store
   record (`errors`, `summary`). Read it whenever the run lists one.
3. **Full `statusMessage`** — not just SUCCEEDED/FAILED. This is where
   `"free user run limit reached"` and `"Reached limit of max crawled places"` appear.
4. **Field completeness, with quirk awareness** — distinguish genuinely empty from known-benign:
   - Meta dynamic/catalog ads legitimately return `{{product.brand}}` as body text. Real ad, not junk.
   - Wix/WordPress **placeholder** socials (`instagram.com/wix`, `facebook.com/ThemeRexStudio`,
     `info@mysite.com`) are real findings about an unconfigured site — report them as such, don't
     silently drop them or mistake them for the clinic's accounts.
5. **Cross-source corroboration** — where two pulls should agree (follower count, website URL),
   check they do. Agreement is a trust signal; mismatch needs a closer look before either is used.
6. **Manual tie-break on load-bearing claims** — anything that *reverses* a prior finding
   ("no ads" → "26 ads") or is high-stakes (fraud/negligence allegation) gets one direct check
   before being stated as settled fact.

**On a partial/timed-out run:** harvest what completed, then re-run only the missing slice. Never
present partial coverage as complete.

---

## Phase 3 — Identity resolution

- **Generic names** (e.g. "Siri Clinic", "Cura Care", "Ridhi's") → set `maxCrawledPlacesPerSearch ≥ 2`
  and report best-guess candidates **with an explicit confidence level**. Never silently pick one.
- **Multi-branch** — 2+ distinct places for one query means a chain. Audit **each branch separately**;
  do not discard the others. Branches diverge sharply (one Artistry Clinics branch ran 9.4% negative
  reviews, the other 13.3%).
- **Corporate-brand collisions** — if a search resolves to a large hospital/chain brand, confirm
  scale from its *own* IG bio or ad copy before treating it like a solo practice.
- **Geographic mismatch** — verify the clinic is actually in the stated state. A "Karnataka" lead
  turned out to be a Kolkata chain whose own IG bio listed only `KOL • AMD • SLG • GAU • HYD`.
  Same-name-different-city is common (Skinmatics Bangalore vs. a Chennai namesake).
- **Founder vs. consultant** — read the LinkedIn title **literally**. "Consultant Dermatologist"
  ≠ founder, even if patients name them in every review. Report exactly what the profile says.
- **Unconfirmed affiliation** — if a supplied LinkedIn profile never names the clinic in
  headline/About, flag the person→clinic link as **unconfirmed**. The user's list is a lead, not
  ground truth. (Seen repeatedly: two batch-2 contacts didn't name their clinic; one named contact
  turned out to be transitioning out of clinical work entirely.)

---

## Phase 4 — Contact discovery

Goal: **founder-level contacts preferred, generic clinic contacts acceptable as fallback.** Work
down the ladder and stop when you have a named human with a reachable channel. This also serves
`wedge-signal-entry.md` §1.2's "front desk is the only reachable contact" park route.

### 4.1 Core ladder (all modes)
1. **Personal LinkedIn** (URL supplied or found) — often carries a **personal** mobile + email
   directly in the About section. Check it before falling back to the clinic switchboard.
2. **GBP contact enrichment** — phone, email, and socials off the listing/website.
3. **Website team/about page** — free (already crawling), and gives **names + titles** with no
   inference: clinic head, operator, manager, other doctors, surgeons.
4. **LinkedIn company People section** (`harvestapi/linkedin-company-employees`) — when a company
   page exists. Return profile URLs where resolvable; **names + titles are the acceptable minimum.**

### 4.2 Instagram contact graph (Deep mode, or when 4.1 yields no named human)
Cheap, staff-oriented signals only — in rough order of value:
- **Clinic IG bio** — often names the founder or links their personal account directly
- **Linked founder/doctor personal accounts** — from the bio, or reciprocal links between accounts
- **Accounts the clinic follows** (`following`, never `followers`) — curated and staff-heavy
- **Tagged and collab posts** — co-authored/tagged accounts on clinic posts are frequently staff
  (`taggedUsers` and `coauthorProducers` are already returned by the profile scraper — free)
- **Recurring staff names in captions** — "Dr. X performed…", "our therapist Y" — gives names to
  cross-reference
- **Story highlight titles** — occasionally name doctors or per-doctor service lines

**Explicitly excluded:** follower lists and recurring-liker overlap. Low yield for staff discovery,
and it amounts to profiling patients — see the privacy rules above.

### 4.3 Confidence labelling (required)
Every contact gets a label. A name match alone is **not** confirmation.
- **`confirmed`** — the person's own profile/page names the clinic, or the clinic names them
- **`likely`** — corroborated by role/credential/locality but not stated on both sides
- **`weak`** — name matches only; no corroboration. Report as weak or not at all
- **`discard`** — contradicted, or a same-name different person

Report per clinic: every contact found, tagged `founder` / `doctor` / `manager` / `front-desk` /
`generic`, with **source** and **confidence**. Do not manufacture a contact.

---

## Phase 5 — Review analysis standard

Never report bare count + rating. Per clinic **and per branch**:

**Totals (all-time):** star rating, total review count, and the full distribution (5★/4★/3★/2★/1★).

**Recency windows** — pull `reviewsSort: "newest"`, ~100–150 reviews, then segment:
- **Last 90 days** — count, and how many are ≤2★
- **Last 180 days** — same
- **Date of most recent review** + **gap in months** (checklist §3 requires this; it also drives the
  §3 wedge row *"high review count but last review months old → Review reactivation agent"*)

**Weight qualitative analysis to the recent window.** Anything older than ~6 months is context, not
signal. But note the inverse explicitly: if *all* reviews are years old (one clinic's newest
negative was from 2022), that stall **is itself the finding** — don't report "no recent complaints"
as if it were health.

**Read the negatives.** Pull all ≤2★ in the window and report:
- Exact count and % of the sampled pull rated ≤2★
- **Owner reply rate among those negatives** (0/5 replied is a materially different clinic from
  6/6 replied — and reply *tone* matters too: defensive, combative, and templated replies are each
  a distinct finding)
- 2–4 verbatim quotes, each with date and reply status — **minimized per the privacy rules**
- **Recurring complaint shapes** across multiple reviewers — a pattern repeated by independent
  patients is far sharper wedge evidence than one complaint. Watch for the shapes that map straight
  onto §3 rows: unanswered enquiries, front-desk/phone failure, no-show or booking friction,
  quotes never chased, no results after paid sessions, technician-instead-of-doctor.
- **Escalation-grade allegations** (negligence, fraud, legal notice, physical harm) get surfaced
  prominently, never smoothed into the surrounding prose.

**Fake/bulk-review sanity check:** bursts of generic 5★ in a narrow window; a perfect rating with a
large N is worth a light flag, but a genuine, well-answered single negative in 203 reviews *raises*
confidence rather than lowering it. Say which way the evidence points.

---

## Phase 6 — Disqualification & park screen (canonical)

Apply `wedge-signal-entry.md` §1 directly. **One hard kill disqualifies.**

### Scrapable hard kills — check these
| # | Signal |
|---|---|
| 1 | No website **and** no Instagram **and** no GBP |
| 2 | Operating < 12 months (oldest Google review date) |
| 5 | Committee / multi-partner sign-off, no single decision-maker (Pvt Ltd chains, corporate groups) |
| 7 | Primary ask is lead-gen, ads, website redesign, or content → **refer out** |
| 9 | Passes both speed-to-lead tests — *only determinable post-mystery-shop* |
| **10** | **No named decision-maker reachable on a personal channel** — added 2026-08-13. **Check this at Phase 0.5, not at the end.** Batch 7 wrote complete dossiers for Project Skin, Dermatonik and Haircosmos before discovering none of them names a doctor anywhere: 3 of 10 dossiers that need never have been written. |

### Not scrapable — mark `undetermined`, do not guess
- #3 inbound volume < ~20 leads/month
- #4 average treatment value < ₹25,000 (may be *partially* inferable from advertised pricing or
  review-quoted amounts — report as an estimate, clearly labelled)
- #6 owner detached from lead ops
- #8 no lead data exists anywhere

### Explicitly NOT disqualifiers (§1.3) — never kill for these alone
Not running Meta ads · missing one channel (website OR Instagram, if WhatsApp + one other exists) ·
messy CRM · strong surface reputation with no visible weakness.

### Park tier (§1.2) — deprioritize, don't kill
Mega founder-brand (Medium) · shallow existing automation (High) · front-desk-only contact (Medium,
route via the Phase 4 ladder).

### Additional escalation flag (project-specific)
Flag **do not pursue as a standard lead**, explicitly and unsmoothed, when 2+ of these hold:
- Ad volume an order of magnitude above every other lead in the batch (thousands of ads = corporate
  chain, not a solo practice)
- Multiple independent reviews alleging fraud, negligence, legal action, or physical harm
- The named contact's own profile doesn't connect them to the business at all

One alone still earns a clear caveat. (This maps onto hard kills #5/#7 in practice — a real batch-2
lead hit all three simultaneously.)

---

## Phase 7 — Wedge routing (strict)

**Route to `wedge-signal-entry.md` §3. Use its exact wedge name and opening frame. Never invent one.**

Then emit the two fields §4 mandates on every dossier:

- **`funnel_break_stage`** — one of: `Response Speed` / `Qualification` / `Follow-up Persistence` /
  `Quote Chase` / `Booking / No-show` / `Post-consult` / `Reviews` / `Reactivation` / `None (pass)`
- **`recommended_entry_sku`** — the §3 wedge matching that stage

Disqualified clinics: skip both fields, mark `Disqualified` + the specific kill reason instead.

### Priority rule (§0) when multiple breaks exist
Pick the break that is (1) screenshot-provable, (2) closest to money already spent, (3) fastest to
a visible win. **Enter on one wedge only** — the full Revenue OS is the expansion, never the opener.

### Critical honesty constraint — provisional wedges
Many §3 rows and **both** speed-to-lead tests depend on response-speed data that only the
mystery shop produces. Scraping cannot determine "response slow or none."

So: mark the wedge **`PROVISIONAL`**, and state explicitly which mystery-shop finding would confirm
or change it. Example:

> `recommended_entry_sku`: Dead-lead reactivation — **PROVISIONAL**
> Basis: 26 active Google Ads + 0/5 recent negative reviews answered.
> Confirm/redirect via mystery shop: if the DM reply is fast, this becomes
> "Follow-up and nurture engine" (§3 row 2) instead.

**Presence/content gaps are evidence, not wedges.** "No Instagram," "dead website," "stale content"
may support a §3 wedge but must never *be* the wedge — per hard kill #7 that's a marketing-agency
ask, and the clinic should be flagged refer-out if it's the only real gap.

---

## Phase 8 — Self-evaluation loop (mandatory, before output)

Once a draft exists, review it as if auditing someone else's work. Do not skip; do not present the
pre-correction draft.

1. Re-read the whole batch against Phases 1–7.
2. Per clinic: **"Did I verify this, or am I assuming it?"** Anything unverified gets relabelled
   honestly (`not verified — [reason]`), never stated as fact.
3. Confirm every number — negative-rate %, ad count, follower count, founder confirmation — traces
   to a **specific tool call made this session**, not memory, not a prior batch, not inference.
4. Sweep the batch for: missed multi-branch chains · unresolved name ambiguity · geographic
   mismatches · any lead that should trip Phase 6 · any wedge not drawn from §3 · missing
   `funnel_break_stage` / `recommended_entry_sku` · contacts missing a confidence label.
5. Check for the specific failure modes this pipeline has actually produced before:
   - "no ads" asserted from a Meta-only check
   - review analysis based on the 3 reviews Google shows without login
   - a silently rate-limited actor treated as successful
   - a wedge that hard-kill #7 says to refer out
6. **Privacy pass** — scan every quote and field: is any patient name or clinical detail present
   that isn't load-bearing? Strip it.
7. Confirm every dossier says mystery-shop is pending and the wedge is provisional.
8. **Only now** produce the final output.

---

## Output

### 1. Markdown dossier → `05 Prospects/` (always)
Canonical, feeds `personalized-outbound`. Follow the existing section order:

```
Basic Info → ICP Qualification → Digital Presence → Ads → Lead Sources →
Mystery Shop Findings (PENDING) → Reviews Analysis → Marketing Analysis
```

Close every clinic with:
```
funnel_break_stage:       <enum>
recommended_entry_sku:    <§3 wedge> — PROVISIONAL
confirm_via_mystery_shop: <what would confirm or redirect it>
status:                   Qualified | Park (<tier/reason>) | Disqualified (<kill #>)
```

### 2. Batch comparison table — strict field contract (always)
Emit as a markdown table, and as CSV when the user wants it for the Notion tracker. Exact columns,
in this order, one row per clinic **or per branch**:

```
clinic_name, branch, locality, category, contact_name, contact_role, contact_confidence,
contact_channel, phone, email, instagram, website, rating, reviews_total, reviews_90d,
negatives_90d, reviews_180d, negatives_180d, last_review_gap_months, owner_reply_rate_negatives,
meta_ads, google_ads, aggregator_paid_listing, funnel_break_stage, recommended_entry_sku,
wedge_state, status, disqualify_reason, depth_mode, unverified_fields
```

Conventions: `undetermined` for a check that ran but couldn't resolve; `not_run` for a step the depth
mode skipped; `wedge_state` is always `PROVISIONAL` pre-mystery-shop; `unverified_fields` is a
semicolon-separated list so gaps are machine-visible, not buried in prose.

### 3. Visual artifact — conditional
Publish/update the accumulating audit artifact (**republish the same URL**, don't mint a new one)
when the batch is ≥6 clinics, or contains a Phase 6-flagged lead, or the user asks for it.
Skip it for small/urgent batches — the markdown + table are the real deliverables.

When built, include: batch overview table · per-clinic/per-branch cards (sourced contact strip,
founder confirmation + source, review stats with quoted negatives and reply status, ad activity,
routed §3 wedge with frame) · Phase 6-flagged leads on a visually distinct card ·
**a limitations section** listing what wasn't verified and why. Disclose gaps; never hide them.

### 4. Evidence tagging — load-bearing claims only
Not a full ledger on every field. For claims that drive a decision — the wedge basis, a
disqualification, a founder confirmation, a reversal of a prior finding — record inline:
**source (actor or URL) + confidence + date pulled.** Everything else is covered by the per-clinic
sources line.

---

## Cost discipline

Observed, on a $5/month Apify free tier:

| Batch | Clinics | Cost | Per clinic |
|---|---|---|---|
| Name-based LinkedIn search | 13 | ~$2.46 | ~$0.19 |
| Direct LinkedIn URLs supplied | 10 (17 places incl. branches) | ~$0.95 | ~$0.095 |

- Set `maxTotalChargeUsd` on **every** call so a runaway run errors instead of overspending quietly.
- Direct LinkedIn URLs are ~25x cheaper than name search — always ask once.
- Multi-branch chains multiply GBP cost; budget for more places than clinic names.
- **Lite mode is the lever when credit is tight** — it drops the two priciest optional steps
  (LinkedIn person, IG graph) while keeping the wedge-critical data.
- If remaining credit looks tight for the batch size, say so **before** running, with the estimate.
- Actor-level free-tier caps (LinkedIn search) are **separate** from account credit. Hitting one
  isn't a billing problem — it's a coverage gap to disclose or re-run on a later day.

---

## Anti-patterns

- ❌ Substituting web search / a raw page fetch for a real scraper when a reliable one exists.
  *(Web search for identity, branches, news/legal, obscure contacts is fine and encouraged.)*
- ❌ Reporting ad status from Meta alone, or skipping the aggregator check in Standard+.
- ❌ Treating `SUCCEEDED` as proof of data. Phase 2 applies unconditionally.
- ❌ Reporting review counts/ratings without reading the negatives.
- ❌ Inventing a wedge name, or making presence/content the wedge.
- ❌ Stating a wedge as settled when it depends on mystery-shop data.
- ❌ Softening or burying a Phase 6 flag for tonal consistency.
- ❌ Treating the user's supplied contact as confirmed affiliation.
- ❌ Reporting a contact without a confidence label, or inventing one from a bare name match.
- ❌ Quoting patient names or clinical details beyond what the business finding requires.
- ❌ Scraping follower/liker lists to identify patients.
- ❌ Running Deep mode across a whole batch by default.
- ❌ Presenting the pre-Phase-8 draft.
- ❌ Mystery-shopping, or sending any message to a clinic. Ever. The user does this.
