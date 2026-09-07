# Batch #11–15 Summary — Vitals Klinic, Krity 360, D White Feather, Dr AG Skin & Hair, Project Skin

> *(⚠️ Retired tests: the six-test SOP was cut to two — qualification and quote decay — on 2026-08-13. Persistence, after-hours, cross-channel and booking friction no longer run. See `wedge-signal-entry.md` §2.)*


> ⚠️ **PRE-SHOP RECORD — live state is in Notion, not here.** This dossier was written before the
> mystery shop ran. This cohort is tracked in Notion as **"Batch 2"**
> (`collection://754da695-40e4-839a-a0e7-07e28a0a27d8`), where the `Mystery shop status`, `Wedge` and
> `Notes` fields carry the shop transcript, timestamps, the confirmed wedge and the next action.
> **Read the Notion row before drafting anything for this clinic.** Where the two disagree, Notion wins.
> Any `recommended_entry_sku: … PROVISIONAL` line below may already have been confirmed or redirected.


*Researched 2026-08-08. Full dossiers: `21-vitals-klinic.md`, `22-krity-360.md`, `23-d-white-feather.md`, `24-dr-ag-skin-and-hair.md`, `25-project-skin.md` (all in `Pre-outbound-research/batch7/`). Instagram data per Apify run `EesNLVkPYhlCqqs50`, 2026-08-08 — not re-scraped. Mystery shop **not run** on any of the five — all mystery-shop fields are `pending — Tilak to run`, and every `funnel_break_stage`/`recommended_entry_sku` tag below is provisional per wedge-signal-entry.md §4.*

## Summary table

| # | Clinic | Hard-kill status | Provisional wedge | Priority tier | Strongest screenshot-provable fact |
|---|---|---|---|---|---|
| 11 | Vitals Klinic | Not killed | Dead-lead reactivation (if slow response) or Qualification upgrade (if fast) | High — Meta ad spend confirmed live | **1 active Meta ad, started 2026-07-24, running on Facebook + Instagram** (Ad Library ID 2055649615024286, screenshot-verified) + **Practo Prime confirmed paid listing** |
| 12 | Krity 360 | **Unresolved — possible §1.1 #2 age kill, needs manual check before proceeding** | Systematize the hustle (if age clears) | Park until age resolved | Oldest review found in this pass dates to **2025-11-17** (~9 months before research date) — could not confirm an older review exists; Google Maps' relevance-sort means this is not conclusive, but it is the single flag that should be resolved first |
| 13 | D White Feather | Not killed — founded 2021, directly confirmed | Quote-decay follow-up (candidate) | High — largest review base (633), one confirmed negative review | Website directly states **"since 2021"**; a genuine 1★ review states *"Highly overpriced!... Avoid if you don't want to get overcharged"* (2026-01-13) — the only unambiguous negative review surfaced in this batch |
| 14 | Dr AG Skin & Hair | **Not killed — task's suggested hard-kill hypothesis directly disproven** | Cannot be narrowed — thinnest evidence base in batch | Medium-park — small, low-digital-spend, single-doctor practice | **Website exists and was located** (dragskinandhairclinic.com) despite source data saying "none found"; oldest review dated **2024-08-08** (~2 years old) directly clears the under-12-months concern; a different clinic's Practo listing was nearly mismatched to this one and had to be explicitly ruled out |
| 15 | Project Skin | Not killed | Instant response + organic capture (candidate) | High — strong reputation, weak digital front door | **5.0★ across 102 reviews** (up from 98 in source table) with **zero WhatsApp path anywhere on the website** and **Instagram dormant since 2026-06-24** (0 posts/30d) — the only clinic in this batch with no WhatsApp click-to-chat found |

**None of the five clinics hit a confirmed §1.1 hard kill.** Krity 360 carries an unresolved age-verification flag that should be closed before further investment — see below. Dr AG Skin & Hair's two task-flagged concerns (no website, possible <12-months) were both directly investigated and disproven with dated evidence.

## Could-not-retrieve list

**Google Ads Transparency Center — failed for all five clinics.** Every attempt (`adstransparency.google.com/?region=IN&domain=...`) returned an empty/unparseable result, consistent with the JS-heavy rendering risk flagged in the task brief. Recorded as `pending — manual check` for Vitals Klinic, Krity 360, D White Feather, Dr AG Skin & Hair, and Project Skin. **This is the single most consistent gap across the batch — recommend a manual browser check for all five before this field is treated as settled.**

**Meta Ad Library — mixed results, one confirmed failure worth flagging specifically:**
- Vitals Klinic: succeeded, screenshot-confirmed 1 active ad.
- Krity 360: succeeded, screenshot-confirmed 0 active ads.
- D White Feather: **failed** — first pass returned a false "0 ads" reading, but a screenshot check showed the results panel never rendered (blank page). Recorded as `pending — manual check`, explicitly not a confirmed zero. This is the one Meta ad-spend field in the batch that needs a manual re-check, since an automated pass produced a misleading signal that a screenshot caught.
- Dr AG Skin & Hair: failed to render, `pending — manual check`.
- Project Skin: succeeded, screenshot-confirmed 0 active ads (queried as "Project Skin HSR" for specificity).

**Practo — could not confirm for 4 of 5 clinics:**
- Vitals Klinic: confirmed (Practo Prime, 4.5★, 146 stories, ₹1,000 consult fee) — entity match verified against doctor name and location.
- Krity 360: guessed URL 404'd — `pending — manual check`.
- D White Feather: guessed URL failed to resolve — `pending — manual check`.
- Dr AG Skin & Hair: a Practo URL was found via search but **confirmed via direct extraction to belong to an entirely different clinic** ("EastArise Aesthetics Clinic LLP") — a live example of the name-collision risk `MEMORY.md` warns about. The correct listing (if one exists) is `pending — manual check`.
- Project Skin: not located — `pending — manual check`.

**JustDial — not confirmed for any of the five.** One direct URL attempt (Vitals Klinic) failed with a fetch error; the remaining four were not attempted due to credit budget after repeated Practo/JustDial URL-guessing failures earlier in the batch. All five recorded as `pending — manual check`.

**Founder/doctor identity:**
- Vitals Klinic: confirmed (Dr. Harish Prasad B.R, personal LinkedIn verified).
- Krity 360: confirmed (Dr. Kavita Raghotham) but a second clinician (dental) appears in reviews under two different name spellings ("Dr. Mishali" / "Dr. Teju") — role unresolved.
- D White Feather: confirmed (Dr. Kanchan Chaudhary, founder) plus a second named associate dermatologist (Dr. Abhishek Ponathil) — governance structure (sole owner vs. co-owner) not resolved.
- Dr AG Skin & Hair: confirmed (Dr. Dinesh GG), single doctor.
- Project Skin: **not found at all** — no doctor/founder name appears anywhere on the website, and a targeted search did not surface one. This is the weakest founder-reachability result in the batch — currently only a general phone/email/form exists, no personal route of any kind.

**Business-age verification — one open flag:** Krity 360's oldest recoverable review (2025-11-17) is under 12 months before this research date. This was **not** treated as a hard kill because Google Maps' default review ordering is relevance-based, not chronological, so an older review may exist but wasn't surfaced. This needs a direct manual check (sort GBP reviews oldest-first, or ask the clinic directly) before Krity 360 is either cleared or disqualified under §1.1 #2.

**Review-count drift flagged:**
- Project Skin: 98 (source table) → 102 (this research) — moved, noted in dossier.
- Vitals Klinic, Krity 360, D White Feather, Dr AG Skin & Hair: all matched the source table exactly (272, 157, 633, 32 respectively).

**Other notable gaps:**
- No treatment prices were found published on any of the five websites, so the §1.1 #4 (₹25,000 avg treatment value floor) check could not be directly confirmed for any clinic — all recorded as Unknown, not inferred.
- Vitals Klinic's flagged "posting every ~2 days at 14:00 UTC suggests an agency" hypothesis was **not corroborated** — only a website-build vendor (VBS Technologies) was found, which is a different function from social-media scheduling. The cadence itself remains unexplained.
- One Google Maps review-date extraction for Vitals Klinic returned an internally inconsistent pair of dates ("2 months ago" label alongside an absolute date of 2026-03-17, which is actually ~5 months out) — flagged explicitly in that dossier as needing manual confirmation rather than trusted as-is.

## Mystery-shop tests to run per clinic

**Vitals Klinic** — send an enquiry referencing the current live hair-loss ad (started 2026-07-24) via WhatsApp during business hours; check whether the reply asks about concern/treatment/timeline (test #1, Qualification) or just answers the question. Separately, send a second enquiry after 8pm to test after-hours handling (test #4) — there's no chat widget on the site, so this checks whether anything catches an after-hours lead at all.

**Krity 360** — before any wedge testing, **first resolve the business-age flag** (ask directly, or have Tilak check GBP reviews sorted oldest-first). If cleared: go silent after the first WhatsApp reply and count follow-ups over 7–14 days (test #2, Persistence) — reviews suggest a clinic that proactively calls patients post-treatment, so the open question is whether that same proactivity extends to a brand-new, not-yet-booked enquiry.

**D White Feather** — ask for a price on hair transplant or a laser package, receive it, then go quiet and track whether the quote is chased (test #3, Quote decay) — directly motivated by the one confirmed negative review calling pricing "highly overpriced," which makes a quote-chasing test the most decision-relevant here. Also worth a basic qualification check (test #1) given two doctors are on staff — confirm whether enquiries get routed to the right one or just whoever's free.

**Dr AG Skin & Hair** — start with the simplest test: send a WhatsApp enquiry via the booking number (98450 10149) and check whether anything beyond "when can you come in" is asked before booking (test #1, Qualification) — this clinic has the fewest usable signals in the batch, so establishing the baseline response behavior is the priority before any more specific test.

**Project Skin** — submit the plain contact-form enquiry (Name/Number/Email only, no WhatsApp path exists) and observe: (a) whether anyone asks what treatment/concern before calling (test #1, Qualification), and (b) how long it takes, since there's no auto-capture mechanism to fall back on if it's submitted after hours (test #4, After-hours) — this combination is what would confirm or rule out the "strong reputation, weak digital front door" wedge hypothesis in that dossier.

## Scrapegraph credit usage

Started at 500 credits (Free Plan). Ended this research pass at **255 remaining (245 used)** across all five clinics, including several failed/empty extraction attempts (Google Ads Transparency Center failed uniformly; two guessed Practo URLs failed; one wasted ~76k-token Meta Ad Library extraction on Project Skin that returned nothing before a targeted screenshot retry succeeded). The `crawl` job (limit 1 for the whole plan) was **not used** — all data was gathered via individual `extract`/`scrape`/`search` calls per the task's budget constraint.
