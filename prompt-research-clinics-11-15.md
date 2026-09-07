# Prompt — Research Clinics #11–15 (ScrapeGraphAI / Claude Code)

Paste everything below the line into Claude Code, run from the `Valence-Ops-Sales` folder.

---

Research the five clinics below and produce one dossier each, following this project's existing conventions.

## Read first, in this order

1. `CLAUDE.md` — folder map and order of operations
2. `MEMORY.md` — standing calibration; §2 in particular
3. `wedge-signal-entry.md` — §1 disqualification framework, §2 speed-to-lead SOP, §3 signal→wedge routing table, §4 schema tagging
4. `Pre-outbound-research/OUTREACH document.md` — copy the section schema used there (Basic Info → ICP Qualification → Digital Presence → Ads → Lead Sources → Mystery Shop Findings → Reviews Analysis → Marketing Analysis)
5. `go-list-mystery-shop.md` — where these five come from

Do not draft any outbound copy in this task. Research only.

## The five clinics

Instagram data below was already scraped (Apify run `EesNLVkPYhlCqqs50`, 2026-08-08). **Do not re-scrape Instagram.** Treat these as given and spend your effort on everything that is missing.

| # | Clinic | Area | IG handle | Followers | IG posts | Last post | Posts/30d | Comments across last 12 posts | Google reviews | Website |
|---|---|---|---|---|---|---|---|---|---|---|
| 11 | Vitals Klinic | Electronic City + BTM | @vitalsklinic | 8,100 | 595 | 2026-08-06 | 10 | 2 | 272 | vitalsklinic.com |
| 12 | Krity 360 | Bellandur | @krity.360 | 456 | 130 | 2026-08-04 | 4 | 6 | 157 | krity.in |
| 13 | D White Feather | Whitefield | @dwhitefeather_clinic | 4,965 | 181 | 2026-07-28 | 3 | 26 | 633 | dwhitefeather.in |
| 14 | Dr AG Skin & Hair | Malleshwaram | @dr.ag_skin_hair_clinic | 365 | 152 | 2026-07-27 | 4 | 2 | 32 | none found |
| 15 | Project Skin | HSR Layout | @projectskin.in | 2,189 | 140 | 2026-06-24 | 0 | 12 | 98 | projectskin.in |

Two notes carried over from the IG screen, to verify rather than assume:

- **Vitals Klinic** posts every ~2 days at almost exactly 14:00 UTC. That pattern suggests a scheduling tool or an agency. If you find independent evidence of an agency or marketing partner, it routes to `wedge-signal-entry.md` §1.2 "existing but shallow automation" (park tier, not a kill).
- **Dr AG** has 32 Google reviews and no website found. If it also turns out to be under 12 months old or below the inbound-volume floor, it hits a §1.1 hard kill — say so plainly and stop researching it rather than padding the dossier.

## What to collect

Instagram is done. These five gaps are the job:

**1. Meta ad spend** (`wedge-signal-entry.md` §3 keys the highest-priority wedges off this)
- Search each clinic's exact Facebook Page name in the Meta Ad Library.
- Record: active ads yes/no, count, which procedure or offer, how long running.
- The Ad Library is JavaScript-heavy and often defeats scrapers. **If you cannot get a clean result, record it as `pending — manual check` and move on.** Do not infer ad spend from anything else, and do not guess.

**2. Google Business Profile**
- Current review count and rating (the counts in the table above came from an earlier list — verify, and flag any that have moved).
- Date of the most recent review, and the gap in months.
- Read a spread of actual reviews — recent and older, positive and negative. Report themes with **direct quotes**, not just the aggregate. Look specifically for: wait times, no follow-up, ghosting after payment, pricing surprises, difficulty booking.

**3. Website and booking flow** (the main thing ScrapeGraphAI is good for here)

For each site, extract:
- Every contact/booking path: enquiry form, WhatsApp click-to-chat, phone numbers, chat widget, embedded booking tool. Name the specific tool if identifiable.
- Whether any chat widget or auto-responder is present, and whether it asks qualification questions or only greets.
- Treatment list, with special attention to **multi-session treatments** (PRP, laser packages, hair transplant, aligners, skin-cycle programmes) — these drive the reactivation wedge.
- Any published prices or price ranges. Needed for the §1.1 #4 check (₹25,000 average treatment value floor).
- Number of named doctors or partners. Needed for the §1.1 #5 check (single decision-maker vs. committee sign-off).
- Founding year / "since" claims. Needed for the §1.1 #2 check (under 12 months = kill).
- Founder name and any personal contact route.
- Branch count and locations.

**4. Aggregator presence**
- Practo, JustDial, Lybrate. Note whether the listing looks **paid/promoted** (Practo Prime badge, JustDial sponsored placement). A paid aggregator listing is a "paying for leads" signal equivalent to ads — it opens the aggregator dead-lead row in §3.
- For Dr AG, which has no website: use Practo and JustDial as the primary source, and try to recover a founder contact route there.

**5. Founder reachability**
- Personal Instagram vs. brand page. Personal LinkedIn. Direct WhatsApp vs. front-desk line.
- `MEMORY.md` §5 records that front-desk-only numbers have been a repeated discovery failure. If the only reachable contact is a front desk, say so — that is §1.2 park (an access problem, not an offer problem), not a kill.

## Tooling

Use the ScrapeGraphAI MCP for website and listing extraction. Check which tools are actually exposed before planning around them — typically a smart-extract tool (URL + natural-language schema), a markdownify tool, a search tool, and a crawler.

- Prefer the natural-language extraction tool with an explicit field list over dumping whole pages.
- Crawl the money pages, not just the homepage: `/contact`, `/book`, `/appointment`, `/treatments`, `/services`, `/pricing`, `/about`, `/team`.
- Use web search to locate Practo/JustDial/GBP URLs first, then scrape the specific URL.
- Batch related pages per clinic rather than one call per field.

**Carry over the verification rule from `MEMORY.md` §2.** It was learned on Apify but applies to any scraper: a tool reporting success does not mean it returned real, complete data. After every call — confirm the content actually corresponds to the right clinic and the right city, check field completeness, and cross-corroborate anything surprising against a second source. Bangalore clinic names collide constantly, and the last screen surfaced a live example: a handle on the shortlist turned out to belong to a same-named clinic in Staffordshire, UK. Verify entity identity before recording anything.

## Hard rules

1. **Never invent or infer a finding.** If something is not confirmed, write `Unknown` or `pending`. Do not write "likely," "probably," or "presumably" into a factual field.
2. **Do not mystery-shop.** Do not send DMs, WhatsApp messages, emails, or form submissions to any clinic. Leave the Mystery Shop Findings section as `pending — Tilak to run`. This is a standing rule in `MEMORY.md` §2.
3. **Do not treat a template "Potential Missing Layers" checklist item as a finding.** `MEMORY.md` §2 records a full wedge being built on one and having to be discarded.
4. **A hard kill stops the work.** If a clinic hits any `wedge-signal-entry.md` §1.1 signal, mark it `Disqualified` with the specific kill reason and skip the wedge tagging entirely. Do not keep researching to fill out the page.
5. **A missing channel is not a kill** (§1.3). No website, or no ads, only removes specific wedges.
6. Cite a source URL for every factual claim.

## Output

Write one file per clinic to `Pre-outbound-research/`, matching the existing section schema. At the end of each, add the two §4 tags:

- `funnel_break_stage` — one of: `Response Speed` / `Qualification` / `Follow-up Persistence` / `Quote Chase` / `Booking / No-show` / `Post-consult` / `Reviews` / `Reactivation` / `None (pass)`
- `recommended_entry_sku` — the matching wedge from §3

Both tags are **provisional until the mystery shop runs**, since §3 routes on response speed. Label them that way. Where the wedge genuinely cannot be narrowed without the shop, say which specific test would decide it (§2 lists six).

Then write one summary file, `Pre-outbound-research/batch-11-15-summary.md`, containing:
- A table of the five with: hard-kill status, provisional wedge, priority tier (Very high / High / Medium-park), and the single strongest screenshot-provable fact found.
- A "could not retrieve" list — every field that failed, with which source failed and why, so it is visible rather than silently missing.
- The specific mystery-shop tests Tilak should run per clinic to confirm each provisional wedge.

## Finally

Re-read each dossier against `MEMORY.md` and confirm: every factual claim traces to a cited source, no inferred behaviour is stated as fact, no mystery-shop field is filled in, and any clinic marked disqualified names the specific §1.1 signal. Report anything you were unable to verify rather than leaving it to look complete.
