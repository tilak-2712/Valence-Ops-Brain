# Batch 7 — Master Consolidated Record, All Clinics

*Assembled 2026-08-17 from every file in `Pre-outbound-research/batch7/`: `BATCH7-CONSOLIDATED-STATE.md`,
`BATCH7-WEDGE-BRIEF.md`, `BATCH7-FOLLOWUP2-MESSAGES.md`, `go-list-full-report.md`,
`batch-11-15-summary.md`, the 12 per-clinic dossiers, and the 10 shop screenshots in `mystery-shop-b7/`.
Root-level `findings-batch7-clinics-11-20.md` folded in for the #11–20 summary tables.*

**Purpose:** one file carrying mystery-shop results, research, wedges, follow-ups and blockers for every
batch-7 clinic, for use alongside other docs in a statistics pass.

---

## 0. Read this before computing anything from this file

| # | Caveat |
|---|---|
| 1 | **This is a repo assembly, not a fresh Notion read.** Notion (`collection://754da695-40e4-839a-a0e7-07e28a0a27d8`, tracked there as **"Batch 2"**) overrides every number here on per-clinic outbound state. All shop/DM state below is the **14/8/26 merge**, three days stale as of assembly. |
| 2 | **Two denominators, not one.** 12 clinics have a Notion row + dossier + shop. The folder also holds research on **Routines by Dr. Apoorva** (researched 8/8, never shopped, no Notion row) — Appendix A, do not count it in shop or send rates. |
| 3 | **Never compute rates from `files/SEND_LOG.csv`** (frozen 6-row fragment). Send counts here come from the Notion merge. |
| 4 | **Epistemic labels are load-bearing.** `confirmed` = real-world evidence exists. `provisional` = designed/observed but untested. `hypothesis` = a guess. A pre-shop dossier wedge tagged PROVISIONAL is *not* a confirmed wedge, even where the language is confident. |
| 5 | **Screenshot beats prose.** Where a shop screenshot and the Notion prose disagree, the screenshot wins — §4 lists every known disagreement. Three "Wedge confirmed" Notion entries are factually wrong. |
| 6 | **Two clinics have no screenshot at all** (Derma Solutions, Haircosmos). Their shop findings are Notion prose only — unverified, and blocked from shipping on that basis. |
| 7 | **Admissibility floor.** All shops ran ~3:00–4:45 PM on a weekday against clinics staffed to 8 PM. Every gap measured is a **best-case floor**. Two exchanges are explicitly **inadmissible** (after-hours) and must not appear in copy: Gejje's 9:40 PM → 8:07 AM, Dr. Priya's 9:39 PM → 11:14 AM. |
| 8 | **One clock has expired since assembly.** Theory of Skin's do-not-message date was **17/8/26 — today.** Krity 360's 14-day review lands **~24/8/26.** |

### Precedence, if this file disagrees with another

Notion (per-clinic state) → `files/OUTBOUND_MEMORY.md` §3–§6 → `MEMORY.md` → `wedge-signal-entry.md` →
`personalized-outbound-v2.md` → this file → the pre-shop dossiers.

---

## 1. Roster and state — all 12

| # | Clinic | Area(s) | Priority | Shop status | DM status (as of 14/8) | Wedge state | Blocked on |
|---|---|---|---|---|---|---|---|
| 1 | **Dr. Priya's Skin & Hair** | Marathahalli | Very High | Wedge confirmed | DM-1 IG → Dr. Priya | confirmed | — fully unblocked |
| 2 | **Derma Solutions** | Marathahalli | Very High | Wedge confirmed | **email-1** → Dr. Sandeep | confirmed *(prose only)* | **No screenshot** |
| 3 | **Akera Health** | HSR + HRBR | Very High | Wedge confirmed | DM-1 IG → Dr. Lavina, Dr. Prabha | confirmed — strongest in batch | Founder/owner ID (MCA: Akera Healthcare Pvt Ltd) |
| 4 | **Project Skin** | HSR | Very High | Wedge confirmed | DM-1 IG → Abdulla Razack, Sandra Alexander · *not sent to Jayadarsan GS* | confirmed | Founder ID + single-vs-multi owner (MCA: ASJ Aesthetic Clinics LLP) |
| 5 | **Haircosmos International** | JP Nagar + Whitefield | Very High | Wedge confirmed | DM-1 IG → Dr. Saima Khan | confirmed *(prose only)* | **No screenshot + no principal named** |
| 6 | **Dermatonik** | HSR | High | Retest needed → *partly resolved by screenshot* | DM-1 IG → Dr. Saeema Shiraaz | confirmed on re-read | Addressee undecided (Saeema Shiraaz vs Anjali Sanghvi) |
| 7 | **VIDA Skin & Hair** | Whitefield | High | Retest needed → *resolved by screenshot* | DM-1 IG → VIDA brand account | confirmed (angle rebuilt) | — fully unblocked |
| 8 | **Gejje's Marvella** | Basavanagudi (+ Hospet) | Medium | Retest needed → *verified verbatim* | DM-1 IG → Dr. Somashekar · *"Send Email to Dr. Somashekar" reads as an open to-do* | confirmed | **Founder name uncorroborated — do not draft until verified** |
| 9 | **Ara Skin Clinic** | Shankarapura / Basavanagudi | Medium | Retest needed → *re-angled from screenshot* | DM-1 IG → Dr. Sonakshi | confirmed (new angle) | — fully unblocked |
| 10 | **Vitals Klinic** | BTM + E-City + Whitefield | *(unset)* | Pending review → **reviewed: HARD KILL #9** | DM-1 IG → Dr. Harish Prasad | **None (pass)** | **Do not send a diagnostic** |
| 11 | **Krity 360** | Kasavanahalli / Bellandur | Medium | **Test running** | — none | undecided, pending clock | **DO NOT MESSAGE.** Review 7d + 14d (~24/8/26) |
| 12 | **Theory of Skin** | Indiranagar | Medium | **Test running** | — none | undecided, pending clock | **Clock expired 17/8/26 — decide today** |

**Contact counts (14/8):** 9 of 12 contacted · **8 by IG DM, 1 by email** · 3 untouched (Krity + Theory of Skin
deliberately, Vitals partially/now killed for diagnostics).
**Replies logged from batch 7: zero.** `files/REPLY_LOG.csv` holds only Sapphire and Aesthetica Veda —
neither is a batch-7 clinic. Batch-7 DM-1 reply rate as of 14/8 = **0/9**.

---

## 2. Statistics layer — flat tables

### 2.1 Mystery shop, response mechanics (all 12)

Shops ran Mon **10/8/26** (openers), with follow-on exchanges 11–12/8. Screenshots captured 12/8.

| Clinic | Channel(s) | Enquiry sent | Auto-ack? | First human reply | Time to human | Qualifying question? | Price given | Price at | Unprompted follow-up? | Thread outcome |
|---|---|---|---|---|---|---|---|---|---|---|
| Dr. Priya's | WhatsApp (**personal account**) | 10/8 4:22 PM | No | 10/8 4:23 PM | **1 min** | Clarifying only (*"regarding ?"*, *"U r asking about procedure?"*) | Yes | 12/8 11:14 AM | No — 2 days | Priced, **no appointment ever offered** |
| Akera Health | WhatsApp (HRBR) | 10/8 4:23 PM | **None — only clinic of 12 with no acknowledgement of any kind** | 11/8 11:31 AM | **19 h 08 m** | Yes — *"may I know what treatment you are looking for?"* | Yes | 11/8 5:31 PM ⚠️ see §4.4 | No — 3 days | Priced, then silence |
| Project Skin | WhatsApp | 10/8 4:43 PM | Yes — **fired twice inside one minute** | 11/8 2:25 PM *(after patient re-messaged 2:24 PM)* | **60 s on 2nd attempt; ~22 h on the 1st** | No | Yes | 12/8 2:14 PM | No — 2 days | Priced only after patient chased |
| Derma Solutions | WhatsApp | 10/8 | — | 10/8, **60 s** | **60 s** | No | No | — | No | Link dump → dead |
| Haircosmos | WhatsApp | 10/8 4:19 PM | — | 10/8 4:22 PM | **3 min** | No | No | — | No | Treatment answer took **2 h 26 m** (6:48 PM) |
| Dermatonik | WhatsApp | 10/8 4:34 PM | Yes — **same minute** | 10/8 4:37 PM | **3 min** | **No — zero questions in 3 days** | Yes | 11/8 4:34 PM (3 min after ask) | No — 3 days | Generous outward, nothing inward |
| VIDA | WhatsApp | 10/8 ~4:37 PM | Yes | 10/8 4:39 PM ("Indira") | **2 min** | **Yes — named + asked treatment** | Range only | 11/8 6:08 PM (45 min after ask) | No — 3 days | *"It start from 3500 to 6500"*, no brochure |
| Gejje's Marvella | WhatsApp | 10/8 3:00 PM | Yes — **best auto-reply in batch** | 10/8 3:56 PM | **56 min** | No — never re-asked any of the 3 things its own bot requested | Refused (defensibly) | 11/8, + 8:07 AM 12/8 *(inadmissible)* | No | *"Yes . Treatment available"* / *"Visit the clinic"* |
| Ara Skin | WhatsApp | 10/8 4:22 PM | Yes | 10/8 4:39 PM | **18 min** | No — quoted the message back and re-asked it | No | — | No — 3 days | 11/8: offered a call in **2 min**, patient declined twice → thread ended |
| **Vitals Klinic** | WhatsApp (**+91 92068 69610**, not the number on file) | 12/8 | Yes | **1 min** (AI) | **1 min** | **Yes** | Yes — ₹2,500 / ₹8,000, itemised w/ strike-throughs | 12/8 3:17 PM | **YES — unprompted, ~1 h later (5:39 PM)** | **Cold → bookable in 4 min.** Product card + "I'm interested" + branch routing + doctor named + native booking form |
| **Krity 360** | Instagram **and** WhatsApp | IG 1:48 PM · WA 4:20 PM | Yes, instant on both | IG 2:13 PM (**25 min**) · WA **1 min** | **1 min (WA)** | **Yes, discriminating** — *"is it acne or acne scars?"* | Yes — full, unhedged | WA 4:28 PM | Clock still running | **Cold → priced in 8 min.** Correct treatments for scars |
| **Theory of Skin** | WhatsApp | 10/8 4:31 PM | Yes — Meta AI, instant, listed treatments + asked concern | Human 4:54 PM | ~23 min | **Yes (by bot)** | Yes — ₹750 consult, peel from ₹4,500 | 10/8, instant on "Acne" | **Called 6:11 PM — the only call anyone in the batch made. Missed, never retried** | 12:30 slot confirmed, unclaimed |

### 2.2 Prices quoted, and who chased them

From `BATCH7-WEDGE-BRIEF.md` §0.4 — *identical three-step script at all ten screenshot-backed clinics.*

| Clinic | Price quoted | Quoted at | Chased? |
|---|---|---|---|
| Akera | ₹4,500 / ₹18,000 / **₹28,000** per session | 11/8 5:31 PM | No — 3 days |
| Dr. Priya's | MNRF ₹9.5k / dermapen ₹10k / MDF ₹8.5k per session | 12/8 11:14 AM | No — 2 days |
| Project Skin | ₹3,000 / ₹6,000 per session | 12/8 2:14 PM | No — 2 days |
| VIDA | *"It start from 3500 to 6500"* | 11/8 6:08 PM | No — 3 days |
| Dermatonik | *"Starting 5500/-"* | 11/8 4:34 PM | No — 3 days |
| **Vitals** | ₹2,500 / ₹8,000 + booking link | 12/8 3:17 PM | **Yes — unprompted** |
| *(clock running)* Krity 360 | microneedling ₹8–9k/session · exosomes ₹10–12k · boosters from ₹14k | 10/8 4:28 PM | TBD — 14d review ~24/8 |
| *(clock running)* Theory of Skin | ₹750 consult · chemical peel from ₹4,500 | 10/8 | Called once 6:11 PM, missed, never retried |

⚠️ **The brief's own summary line reads "Seven gave a price. One followed up." Its table lists six rows.**
Counting Krity and Theory of Skin gives eight. Do not carry "7" forward without re-deriving — see §4.5.

**Derived (screenshot-backed 10 only, excluding the two live clocks):** 6 of 10 quoted a price · **1 of 10
followed up unprompted** · 4 of 10 asked any qualifying question · **1 of 10 offered a booking mechanism.**

### 2.3 Reviews, ratings, engagement (research pass, 8/8/26)

| Clinic | Branch | Rating | Reviews | 1★ count / rate | Newest review | Staleness | Negatives sampled | Owner reply rate (neg) |
|---|---|---|---|---|---|---|---|---|
| Dr. Priya's | Marathahalli | 4.7★ | **1,613** | 74 / 4.6% | 2026-08-07 | 0–1 d | 7 | ~1/7 (14%) |
| Derma Solutions | Marathahalli | 4.6★ | **1,241** | **89 / 7.2% — highest in batch** | 2026-08-07 | 0–1 d | 10 | **0/10 (0%)** |
| Vitals Klinic | BTM | 4.7★ | **1,892** ⚠️ *(earlier pass wrongly said 272)* | 70 / 3.7% | 2026-08-07 | 1 d | 4 detailed | 2/4, both curt; 2 most detailed unreplied |
| Vitals Klinic | Whitefield | 4.3★ | 6 | — | 2026-07-29 | 10 d | 1 | 1/1 |
| Vitals Klinic | BEL/Bedarahalli | 4.6★ | 14 | — | — | **PERMANENTLY CLOSED** | — | — |
| Gejje's Marvella | Basavanagudi | **5.0★** | 870 | 2 in 120-sample | 2026-08-08 | 0 d | 2 | 1/2 (50%) |
| Haircosmos | Whitefield | 4.9★ | 499 | 8 | 2026-08-02 | 5 d | 6 | **0/6 (0%)** |
| Haircosmos | JP Nagar | 4.9★ | 169 | 3 | 2026-06-28 | **40 d** | 2 | **0/2 (0%)** |
| Ara Skin | Shankarapura | 4.8★ | 294 | 8 | 2026-08-05 | 2 d | 4 | **4/4 (100%) — best in batch** |
| Akera Health | HSR | 4.9★ | 315 | 5 | 2026-08-08 | 0 d | 6 | 1/6 (17%) |
| Akera Health | HRBR | 4.9★ | 361 | 2 | 2026-07-29 | 9 d | 2 | 1/2 (50%) |
| Theory of Skin | Indiranagar | 4.6★ | 215 | **19 / 8.8% — 2nd highest** | **2026-04-03** | **126 d — stalest in batch** | 14 | 2/14 (14%) |
| Dermatonik | HSR | 4.8★ | 304 | 15 | 2026-08-06 | 1 d | 10 | 2/10 (20%) |
| VIDA | Whitefield | 4.8★ | 390 | 15 | 2026-08-03 | 4 d | 5 | 3/5 (60%) |
| Krity 360 | Kasavanahalli | **4.9★** | 157 *(full census)* | 2 / 1.3% | 2026-08-04 | 4 d | 2 | High, both polarities, signed "Team Krity 360" |
| Project Skin | HSR | **5.0★** | 102 *(full census)* | **0 / 0% — zero negatives** | 2026-08-08 | 0 d | 0 | n/a |

### 2.4 Paid spend, confirmed as of 8/8/26

| Clinic | Meta ads | Google ads | Practo | Advertiser entity on record | Read |
|---|---|---|---|---|---|
| Akera Health | **25 active** | **29 active** | Listed, **no Prime** | Akera Healthcare Private Limited | Heaviest confirmed volume in batch; 100% direct ad spend |
| Dermatonik | **4 active** ("Upto 50% OFF") | **Heaviest by duration** — ~1 yr near-continuous, 2 entities | Undetermined | Anjali Sanghvi LLP + a cased duplicate | Longest sustained spend |
| Haircosmos | **3 active** — transplant from **₹49,999**, patch ₹9,999, 0% EMI | 1 creative, **lapsed Dec 2025** | Undetermined | Haircosmos Diagnostic & Health Care Pvt Ltd | Meta is now the only paid tap; highest ₹/lead |
| VIDA | 0 | **12 active**, last shown 2026-08-07 | **Prime confirmed** — 302 stories, 90% recommended | "Jigisha jalu" | Two paid channels, zero Meta |
| Dr. Priya's | 0 | 0 | **Prime confirmed** — 5,966 stories, 98% recommended | — | Practo *is* the acquisition strategy |
| Derma Solutions | 0 | 0 | **Prime confirmed ×2 doctors** — 1,649 stories, Practo 4.0★ vs Google 4.6★ | — | Practo-only |
| Project Skin | 0 (verified) | **11 creatives, continuous since 2025-06-05**, one live 2026-08-07 | Not located | **ASJ Aesthetic Clinics LLP** | ~14 months continuous; reverses the earlier "organic-only" read |
| Ara Skin | Undetermined (no page resolvable) | 19 creatives, Sept 2023→current ⚠️ **billed to "Pure Dermacare"** | Listed, **no Prime** (2 stories) | "Pure Dermacare" — **no link established** | **Do not state Ara runs these ads** |
| Theory of Skin | 0 | 5 creatives, **paused ~2026-06-01** | Listed, no Prime (74 stories) | "Sanjana Shivashankar" | Was spending, isn't now — no live spend to pitch against |
| Gejje's Marvella | 0 | 0 | Undetermined | — | Zero spend anywhere — **no money-at-stake framing available** |
| Krity 360 | 0 (no FB page at all) | 0 | Not located | — | Zero paid channel; growth organic |
| Vitals Klinic | **0 — verified twice by Apify** ⚠️ contradicted by ScrapeGraph | 0 | **Prime confirmed** — 146 stories, ₹1,000 consult | — | Prime is the only confirmed paid channel |

### 2.5 Founder / decision-maker reachability

| Clinic | Named principal | Confidence | Channels on file |
|---|---|---|---|
| Dr. Priya's | **Dr. Priya J Talageri** — MD Derm, Gold Medalist | **confirmed** | IG @drpriyaskinandhairclinic (9,660) · phone/personal WA +91 97410 32946 · hello@drpriyaskinandhairclinic.com · LinkedIn malformed. Also Dr. Naveen M Nayak (nephrologist, role unverified) |
| Derma Solutions | **Dr. Sandeep Mahapatra** — LinkedIn title "Consultant"; own About says *"our 2 clinics"* | **confirmed contact, likely owner-operator** | LinkedIn `/in/dr-sandeep-mahapatra-315411112` · **personal mobile +91 99164 24736** · **sandip.derm@gmail.com** · clinic WA +91 97412 23217 · IG @dermasolutionsskinclinic (159). 2nd doctor: Dr. Thyagaraj J. 2nd brand "Neo Follicle" not audited |
| Ara Skin | **Dr. Sonakshi Sunil** — MBBS, MD (DVL), own IG bio | **confirmed** | IG @ara_skin_clinic (4,758) · +91 98898 82246 · glow@araskinclinic.com |
| VIDA | **Dr. Jigisha N. Jalu** — MBBS, MD (Skin & VD), FRGUHS | **confirmed** | Clinic +91 70325 82393 · WA shopped +91 93801 90502 · IG @vida_skin_clinic (1,165) · rep "Indira" |
| Vitals Klinic | **Dr. Harish Prasad B.R** — MD Derm, LinkedIn verified, sole named doctor / single decision-maker | **confirmed** | WA +91 97404 84793 *(shop used +91 92068 69610)* · vitalsklinic@gmail.com · contact@vitalsklinic.com · IG @vitalsklinic (8,100) · LinkedIn company + personal |
| Krity 360 | **Dr. Kavita Raghotham** | **confirmed** | WA +91 93807 89495 · IG @krity.360 (456) · kritywellness@gmail.com · LinkedIn /company/krity360. 2nd clinician "Dr. Teju"/"Dr. Mishali" unresolved |
| Theory of Skin | **Dr. Sanjana Shivashankar** — MBBS, MD Derm, FRGUHS | **confirmed** | +91 96862 37333 · IG @theoryofskin_dermatology (15,552, **verified**) · contactus@theoryofskin.co.in |
| Dermatonik | **Anjali Sanghvi** — likely owner/operator on 3 signals (GBP secondary email, on-site PMU credit, Google Ads entity). **No evidence she treats.** No dermatologist named anywhere on site | **likely, business-side only** | Dr. Saeema Shiraaz (DM-1 target) · dermatonik@gmail.com · Info@anjalisanghvi.com · +91 89510 11944 |
| Gejje's Marvella | **Dr. Somashekar Gejje — WEAK / UNCORROBORATED**, user-supplied list only. Own auto-reply says *"board-certified specialists"* — plural, and names nobody | **weak** | +91 98865 31646 / +91 99162 49637 · gejje.somashekar@gmail.com · gejjesmarvella@gmail.com (+ `gejjesmarvellahosapete@gmail.com`) |
| Akera Health | **NOT IDENTIFIED.** 3 Practo derms: Dr. Lavina Mittal, Dr. Smruthi T, Dr. Champati Prabhavathi. Entity: Akera Healthcare Pvt Ltd | **not_found** | HSR +91 72044 84955 · HRBR/shopped +91 72044 88355 · IG for Lavina, Prabha, Smruthi |
| Project Skin | **NOT NAMED ANYWHERE** — website, LinkedIn, GBP, targeted search all clean. Entity: **ASJ Aesthetic Clinics LLP** ("ASJ" plausibly founder initials); a JustDial listing may carry a proprietor name | **not_found** | WA shopped +91 81233 55968 · info@projectskin.in · IG: @jayadarsan_jd, @abdu._.lla, @_sandra_alexander_ |
| Haircosmos | **NONE NAMED ANYWHERE** — hardest access in batch. LinkedIn page abandoned (blank headline, 0 connections, 1 follower) | **not_found** | Dr. Saima Khan (IG follower, DM-1 target, **not a confirmed principal**) · JP Nagar +91 72049 92757 · Whitefield +91 73491 87047 |

### 2.6 Programme-level counters (tripwire arithmetic)

| Metric | Value | Source |
|---|---|---|
| Touches spent, programme-wide | **~70–90 of 100** (70–90%) | `BATCH7-CONSOLIDATED-STATE.md` §6 |
| Days spent | ~19 of 45 | same |
| Calls held | **0** | same |
| Pilots run | **0** | same |
| Second tripwire | **0 of 3** — no clinic has reached an operations call | same |
| Batch-7 DM-1 sends inside that count | 9 (8 IG, 1 email) | Notion merge 14/8 |
| Batch-7 replies | **0** | `files/REPLY_LOG.csv` holds only Sapphire + Aesthetica Veda |
| One-pager asset record, programme-wide | ~25 sent → 2 replies → **0 calls** | `ONE-PAGER-AUDIT-AND-TEST-PLAN.md` |

---

## 3. Mystery shop — full findings per clinic

### 3.1 Akera Health — *Nothing was listening* · **strongest evidence in the batch**

- Enquiry **4:23 PM Mon 10/8** (HRBR number). First reply **11:31 AM Tue 11/8 — 19 h 08 m.**
- **No auto-reply, no bot, no holding message. Nothing at all in between.** The **only clinic of twelve
  where an enquiry produced no response of any kind.** Three staffed hours remained when it landed.
- Once picked up, handling was good: *"Hi may I know what treatment you are looking for?"* → 12 min to a
  treatment answer → 8 more to itemised pricing including a **₹28,000-per-session** procedure.
- Ads context: **25 active Meta + 29 Google creatives** across 2 branches. **Not** a Practo Prime payer —
  every rupee is direct ad spend. 4.9★ at both branches; owner replies thoughtful when they come (2/8, 25%).
- **The fact is the missing acknowledgement; the 19 hours is the consequence.** Lead on the fact —
  *"that was one bad evening"* answers the second and cannot answer the first.
- Screenshot: `mystery-shop-b7/akera-health.png`
- ⚠️ *"Do not burn this evidence on a front desk."* ⚠️ **Never lead with the ad count** — *"You run 25 ads" → "And?" → Kill.*
- ⚠️ **The twelve-clinic comparison is verified true and cannot be said to her** — a several-clinics framing signals mass-sender, which `MEMORY.md` §2 rates *"worse than silence."* Internal only.

### 3.2 Dr. Priya's Skin & Hair — *The price went out. Nothing asked him to come in.*

- Published clinic number is a **personal WhatsApp account** — profile reads `~Dr Priya J Talageri`, no
  business badge, video calling enabled, "No common groups."
- Replies: **4:23 PM (1 min)** *"hiii sir"* / *"regarding ?"* · 11/8 **7:07 PM** *"U r asking about
  procedure?"* · 7:14 PM · 12/8 **11:14 AM** a typed-out price list: *"mnrf per session 9.5 k / dermapen
  10 k per session / MDF 8.5 k per session."*
- **No appointment was offered at any point across three days.** Nothing captured who asked, what for, or
  what happened next — the outcome of that quote is not just unknown but unknowable.
- Volume: **5,966 Practo patient stories vs 1,613 Google reviews. Practo Prime confirmed** — the larger,
  paid channel. Zero Meta, zero Google ads.
- Screenshot: `mystery-shop-b7/dr-priya.png`
- ⚠️ **Compliment, not complaint** — fastest responder in the batch alongside Krity. Keep her as the closer,
  remove the chasing. ⚠️ **Do not claim she personally typed the replies** — the screenshot proves the
  account is personal, not who holds the phone. ⚠️ **Do not say "silence"** — she answered every message.
  ⚠️ **9:39 PM → 11:14 AM is after-hours and inadmissible.** ⚠️ Lead with the screenshot, **never** her
  reviews — her one reply on record to a critical Practo review was combative.
- Held in reserve: 1★ 14/7/26 *"there is no appointment system"*, 1 h 45 m wait after confirming a time.

### 3.3 Project Skin — *The message that promised, and the one that delivered.*

- 10/8 **4:43 PM** → automated reply the same minute, **fired twice inside one minute**:
  *"How can we help you?"* then *"Hey. Thanks for reaching out! We will get back to you soon."*
  **Nobody did that day.** Over three hours of working day remained.
- 11/8 **2:24 PM** patient messaged again → **2:25 PM, sixty seconds**, a human: *"Hi, chemical peels and
  carbon Laser works well for acne."* Full pricing 12/8 2:14 PM (₹3,000 / ₹6,000).
- **Provable claim is narrow:** the message said *soon*, and **22 hours** later nothing had come. Cannot
  claim nobody would *ever* have replied — the patient's second message ended the test.
- **Corrects the dossier:** it recorded *"no WhatsApp path at all, the only clinic in this batch with none."*
  It exists, on the clinic's own number — just not linked anywhere on the website. Paid search traffic gets
  a Name/Number/Email form; the one channel with an auto-responder is invisible to them.
- Website capture: Name/Number/Email only — **no treatment, concern or timeline field**, no chat widget, no
  after-hours path. IG dormant since 2026-06-24.
- Ads: **11 Google creatives continuous since June 2025**, one live the day before the shop.
- Screenshot: `mystery-shop-b7/project-skin.png`
- ⚠️ **Concede the 60 seconds explicitly** — claiming nobody replied is false and refutable in one scroll.
  ⚠️ **Double bot-fire is colour, not evidence** — two automations firing is a config artifact; leading on it
  reads as a gotcha. ⚠️ **§1.1 #5 risk:** a 5★ says *"the owners manage the clinic"* — plural — and the LLP
  structure fits multiple partners. MCA check before sending.

### 3.4 Derma Solutions — *A minute, and a link.* ⚠️ **NO SCREENSHOT**

- Notion prose, unverified: replied in **60 seconds** with *"Sure. Please visit our website it's all
  mentioned there"* + a link dump (site, Facebook, Instagram, YouTube).
- **No concern asked, no treatment asked, no booking offered, no price.** Not a speed problem — someone was
  live, fast, and had no script.
- **Practo Prime on 2 doctors, 1,649 patient stories** = paying per enquiry, then handing it back to the
  internet. Zero Meta/Google — Practo *is* the acquisition strategy.
- ⚠️ **BLOCKED on the screenshot.** §2.3: *"the timestamped image is the deliverable of the shop; prose is
  derived from it, never the reverse"* — paraphrase-as-evidence is why the Dr. Dixit wedge was discarded.
- ⚠️ Lead with the screenshot, **never** the reviews — the owner's one reply on record to a serious complaint
  was combative (*"Please don't spread misinformation"*). Hold **0/10 negative-reply rate** and **7.2% 1★
  (89 of 1,241, highest in batch)** in reserve.

### 3.5 Haircosmos International — *The wait grows with the stakes.* ⚠️ **NO SCREENSHOT**

- Notion prose, unverified: 10/8 4:19 PM → *"How can i help you"* in **3 min.** Then asked what treatments
  they offer — the one question needing real knowledge — and got *"we have"* / *"gfc exosome qr678 prp"* at
  **6:48 PM. 2 h 26 m.** Lowercase fragments, no price, no explanation, no next step.
- **Fast at greeting, slow at selling.** Greeting and answering look like two different jobs held by two
  different people — so the wait gets longer the more the question matters.
- **3 live Meta ads:** hair transplant from **₹49,999**, hair patch ₹9,999, 0% EMI. Google lapsed Dec 2025 —
  Meta is the only paid tap and it points straight at this inbox. **Highest rupee-per-lead in the batch.**
- Corroborating, 2 independent instances: **0/8 replies to negative reviews across both branches**, including
  an unresolved post-procedure scalp infection (1★ 28/7/26) and a doctor no-show (1★ 4/4/26).
- ⚠️ **BLOCKED twice** — no screenshot **and** no principal named. DM-1 went to Dr. Saima Khan, an IG
  follower, not a confirmed principal. JP Nagar GBP website field merges `drpiyushranjan.com` — unverified,
  likely a broken field, possibly a name lead.

### 3.6 Dermatonik — *Everything went out. Nothing came back.*

- 10/8 **4:34 PM** enquiry → **4:34 PM** auto-reply *"Please let us know your concern"* → **4:37 PM**
  before/after acne collages → 4:39 PM clinic photos + a Google profile card.
- 11/8 **4:31 PM** pricing request → **4:34 PM**: *"Starting 5500/-Once you come For Consultation with
  Doctor Accordingly I can help you better."*
- **Most generous first response of the twelve.** And in three days **not one question came back** — not what
  kind of acne, not how long, not what had been tried, not when they could come in. **The clinic's own welcome
  message asked for the concern; the patient answered "acne"; nobody ever picked it up.**
- Traffic is bought: **4 active Meta ads** ("Upto 50% OFF") + the **longest-running Google presence of the
  twelve**, near-continuous ~1 year across two advertiser entities, still live.
- Second independent instance: 1★ 29/6/26 — told by phone a dermatologist was available, arrived to find
  none, **charged ₹700 anyway**, no refund, no reply.
- Screenshots: `mystery-shop-b7/dermatonik-1.png` (opener), `dermatonik-2.png`
- ⚠️ Anticipated rebuttal *"we assess properly at the consultation"* is **correct** — do not appear to argue
  with it. The gap is knowing which enquiry is worth a call **before** anyone arrives.
  ⚠️ **Keep visibly distinct from Gejje's**: Gejje's withheld everything, Dermatonik gave everything and asked
  nothing. ⚠️ **Decide the addressee first.**

### 3.7 VIDA Skin & Hair — *He asked for something to look at. He got a starting figure.*

- 10/8 **4:39 PM**, two minutes after the enquiry: *"Hello Tilak sir / This is Indira from Vida skin and hair
  transplant clinic / What treatment you are looking for skin sir?"* — named, warm, right question. Four
  hand-typed messages in two minutes. **Fastest, most human handling in the batch.**
- 11/8 **5:23 PM**: *"could you send over a pricing/quote brochure or details for the treatments."*
  **6:08 PM**: *"It start from 3500 to 6500."* No brochure. No next step. Nothing since — three days.
- **Scope it honestly:** the message before it named acne clean-up and MNRF, so a reader *could* map the two
  numbers onto the two treatments. What is unarguable: he asked for a brochure, none was sent, and *"start
  from"* means the real number is still unknown.
- Money confirmed on two channels: 12 Google creatives active (advertiser *Jigisha jalu*, last shown 7/8/26)
  + Practo Prime, 302 stories, 90% recommended. Zero Meta.
- Screenshot: `mystery-shop-b7/vida-skin-n-hair.png`
- ⚠️ **Do NOT sell speed — they have it and are right to be proud of it. Sell fragility: one person holds this.**
  ⚠️ **Drop the 40/45-minute "degradation curve" entirely** — *"forty-five minutes is fast"* is a correct and
  complete rebuttal that takes the whole document with it. ⚠️ **Do not raise** the pricing-pressure reviews.
  ⚠️ DM-1 went to the brand account — consider addressing Dr. Jigisha N. Jalu by name.

### 3.8 Gejje's Marvella — *The welcome message asks three things. Nobody used any of them.* ✅ verified verbatim

- 10/8 **3:00 PM** → instant auto-reply listing specialties, board certification, 15+ years, **both
  locations**, website, closing: *"Kindly share your concern, preferred location, and photos (if comfortable)
  — our team will assist you."* **Best auto-reply in the batch.**
- The three human replies, in full: **3:56 PM (56 min)** *"Hlo... yes tell me"* · 11/8 4:34 PM info request →
  **5:01 PM (27 min)** *"Yes . Treatment available"* / *"Visit the clinic"* · *"It depends on the area and
  treatment. Kindly have a consultation, doctor will explain."*
- **No human returned to any of the three things the bot asked for** — never re-asked the concern, never asked
  which branch, never asked for the photos the clinic itself requested. **The bot does more work than the person.**
- Two things the screenshot added: the auto-reply says *"Led by board-certified specialists"* — plural, and
  **names no doctor even to its own patients**, independently corroborating the founder problem. It also
  confirms the second location — *"Bengaluru & Vijayanagara (Hospet)"* — previously only an unverified lead
  off a stray GBP email.
- Zero ads on Meta or Google — **no money-at-stake story available.** 870 reviews at 5.0★ is what this is
  built against.
- Screenshot: `mystery-shop-b7/gejjes-marvella.png`
- ⚠️ **BLOCKED — founder uncorroborated. Do not draft until verified** (two minutes of work).
  ⚠️ **The 9:40 PM → 8:07 AM exchange is after-hours and inadmissible — must not appear.**
  ⚠️ Don't lead on the 56- or 27-minute gaps, both rebuttable. ⚠️ **Never go near price** — *"pricing needs an
  examination"* is a complete and correct rebuttal.

### 3.9 Ara Skin Clinic — *The patient who said "just send it to me."*

- 10/8: auto-reply 4:22 PM → human **4:39 PM (18 min)** who quotes the original message back and re-asks it:
  *"Hi sir"* / *"How can we help you sir"*. **Eighteen minutes to transfer zero information.** Human-operated —
  the green Meta banner is Cloud API hosting, not Meta AI.
- 11/8 **4:33 PM**: *"could you provide me with more info on acne/scars treatment please"* → **4:35 PM**:
  *"Can we call you sir"* → **4:36 PM**: *"busy with work, could you drop the info here"* → **4:37 PM**:
  *"so that i could have a look"* → **nothing since — three days.**
- Two minutes when the reply offered a call; thread ended when the patient asked twice for it in writing.
  Nobody decided to let it go — **there just wasn't a next step once the call was declined.**
- Counter-context that must be stated: **4/4 negatives answered personally and substantively — best owner
  engagement of the twelve. Attention isn't what's missing here.**
- Screenshot: `mystery-shop-b7/ara-skin.png`
- ⚠️ **Do not use the 18-minute reply** — 18 min is fine and leading there trips §2.5.
  ⚠️ **Do not claim ad spend** — the 19 Google creatives are registered to *"Pure Dermacare"* with no
  established link; Practo is listed but not Prime (2 stories vs 294 on Google). Frame against the reputation
  they've earned, not money spent. ⚠️ *"No defined second path"* is a consultant's sentence — **name the
  patient, not the process.**

### 3.10 Vitals Klinic — **HARD KILL #9, functioning system already in place**

- 1-minute AI reply → qualifying question → **unprompted follow-up one hour later (5:39 PM)** → itemised
  pricing with strike-throughs (₹2,500 / ₹8,000) → product card with an **"I'm interested"** button → branch
  routing → treating doctor named → **native Book appointment form. Cold to bookable in four minutes.**
- **The only clinic of twelve that followed up on its own, before being asked.**
- **There is no honest observation here that isn't a compliment.** A diagnostic gets answered with a
  screenshot of their own bot. **Do not send a follow-up-2 document.**
- The honest move to keep it warm: a short message — tell them their handling was the best of those tested
  and ask what they built it on. Real opener, costs nothing, **not dressed as a one-pager.**
- Screenshots: `mystery-shop-b7/vital-skin-1.png`, `vital-skin-2.png`
- ⚠️ **Correct the record: the number shopped was +91 92068 69610, not the +91 97404 84793 on file.**

### 3.11 Krity 360 — **TEST RUNNING · DO NOT MESSAGE** · clocks from 10–11/8/26

- **Best-run funnel in the batch. No wedge found.** Shopped on BOTH channels:
  - **Instagram** 1:48 PM → instant auto-ack → human at **2:13 PM (25 min)**, used first name, asked the concern.
  - **WhatsApp** 4:20 PM → instant auto-ack → human in **1 minute** offering to call → qualification that
    actually discriminates (*"is it acne or acne scars?"*) → correct treatments for scars → **full unhedged
    pricing at 4:28 PM** (microneedling ₹8–9k/session, exosomes ₹10–12k, boosters from ₹14k).
    **Cold to priced in 8 minutes.**
- **TWO CLOCKS:** quote-decay from **4:28 PM (WhatsApp)** · persistence from **2:13 PM (Instagram)**.
- Review at 7 days (quote decay) and **14 days (~24/8/26**, IG persistence). They chase → likely **§1.1 #9
  hard kill, log and walk.** No chase → quote-decay wedge.
- **Watch the SHAPE, not just the fact:** a generic *"any update sir?"* is a nudge; one referencing acne scars
  or the quote is a system.
- Zero paid spend anywhere. Reviews prove real post-booking discipline — an owner reply reconstructs a
  1:14 PM confirmation + 2:21 PM and 4:41 PM chase calls with exact timestamps; multiple 5★ cite proactive
  follow-up calls. **157 reviews over 2.5 yrs ≈ 5/month — check §1.1 #3 lead volume before investing further.**
- Screenshot: `mystery-shop-b7/krity-360-wa.png`

### 3.12 Theory of Skin — **TEST RUNNING** · clock from 10/8/26 · **do not message before 17/8/26 (today)**

- **Best performer of the thirteen.** WhatsApp 4:31 PM: **Meta AI replied instantly**, listed treatments,
  asked the concern, then on *"Acne"* gave real prices (**₹750 consult, chemical peel from ₹4,500**) and
  pushed for a booking. A human confirmed a **12:30 slot at 4:54 PM** and **called at 6:11 PM — the only call
  anyone in the batch made. Missed, never retried.**
- Nobody chases the ₹4,500 quote or the unclaimed 12:30 slot → **quote-decay + no-show recovery wedge,
  sharpest possible version *because they did everything else right*.**
- They chase → **park**: Google Ads paused ~1/6/26 (advertiser "Sanjana Shivashankar", 5 creatives) — no live
  spend to build a pitch on. **Genuine near-pass.**
- §1.2 park signal: possible mega-founder-brand (15,552 verified IG, individually branded).
- Separate dossier finding: newest Google review was **126 days old** at research time — the stalest review
  flow in the batch — plus **two independent appointment-confirmation-failure reviews** (1★ 11/3/26 told on
  arrival the doctor *"does not even take appointments on Wednesday"*; 2★ 14/10/25 confirmed by phone an hour
  prior, told on arrival the doctor had stepped out for 90 minutes).
- Screenshot: `mystery-shop-b7/theory-of-skin.png`

---

## 4. Corrections and open contradictions — the register

Anything below is a live data-integrity issue. Do not average over it.

### 4.1 Three Notion "Wedge confirmed" entries are factually wrong

| Clinic | Notion says | Screenshot shows |
|---|---|---|
| **Dr. Priya's** | *"Then silence 24h+"* | **False.** Replies at 11/8 7:07 PM, 7:14 PM, 12/8 11:14 AM, ending in a full itemised price list. |
| **Project Skin** | *"Nobody did. 24h+"* | **False.** A human replied in **60 seconds** on 11/8 and later gave full pricing. |
| **Dermatonik** | *"No price"* + opener retest needed | **Partly false.** They quoted *"Starting 5500/-"*. Opener is in `dermatonik-1.png`: instant auto-reply, real content in 3 min. |

**Verified accurate:** Akera's 19 h 08 m with no acknowledgement · Project Skin's double bot-fire.

### 4.2 Vitals Klinic — three separate corrections

1. **Reviews: 1,892 / 4.7★ at BTM**, not the 272 / 4.6★ an earlier pass recorded and claimed "matched the
   source table exactly." The 272 figure matches no listing found — possibly the **Electronic City listing,
   which never surfaced** and remains uncaptured.
2. **A fourth listing exists at BEL Layout / Bedarahalli — PERMANENTLY CLOSED**, not previously known.
3. **Meta ads: direct contradiction, unresolved.** ScrapeGraph reported 1 active Meta ad (Library ID
   2055649615024286, started 24/7/26, FB+IG, "comment HAIR", described as screenshot-verified). Two clean
   Apify queries against the confirmed Page ID (317939428557405) returned **zero ads ever**, active or
   inactive, `isResultComplete: true` both times. **Both ran 8/8/26. Treat the "1 active ad" as unconfirmed;
   do not build a wedge on it.** Fix: check which Page name that screenshot shows.
4. Sample-depth lesson: the earlier pass sampled 8 of 272 reviews, found zero negatives, and concluded no
   wait-time complaints existed. At 165 reviews the booking-failure pattern is unmistakable. **Clearest
   demonstration in the batch that sample depth changes the answer.**

### 4.3 Project Skin — the "organic-only" read is overturned

Earlier pass: Google Ads `pending — manual check`, concluded growth ran *"almost entirely on organic
Google/reviews + word of mouth, with no visible paid acquisition."* **Wrong.** 11 creatives, advertiser
ASJ Aesthetic Clinics LLP (ID AR15654855403907317761), continuous 2025-06-05 → 2026-08-07, including video.
Also corrected: a WhatsApp path **does** exist (clinic's own number), just isn't linked on the website.

### 4.4 Akera's pricing timestamp does not reconcile

`BATCH7-CONSOLIDATED-STATE.md` and `BATCH7-WEDGE-BRIEF.md` §1.1 both say *"12 minutes to a treatment answer,
8 more to itemised pricing"* off an 11:31 AM first reply → **~11:51 AM**. The §0.4 price table says the price
landed **11/8 5:31 PM**. **These cannot both be right.** Re-read `akera-health.png` before using either.

### 4.5 The "seven gave a price" count does not match its own table

§0.4 asserts *"Seven gave a price. One followed up."* The table lists **six** rows. Counting the two
clock-running clinics (Krity, Theory of Skin) gives **eight**. Re-derive before publishing any rate.

### 4.6 Krity 360 — the age hard-kill was an artefact, now cleared

Earlier pass flagged a possible §1.1 #2 under-12-months kill because the oldest review it surfaced was
2025-11-17. A full 157-review chronological pull puts the oldest at **2024-03-11** (~2 yrs 5 mths). The
2025-11-17 date sits at **index 50 of 157** — where a relevance-sorted sample bottomed out, not the true
floor. **Kill risk was sample size, not signal. Unblocked.**

### 4.7 Ara Skin — Google Ads attribution unresolved

19 creatives (Sept 2023 → current) point at `araskinclinic.com`, but the advertiser reads **"Pure Dermacare."**
A targeted web search found no connection. Three readings: agency/reseller account · a Transparency Center
domain-mapping quirk · a genuinely unrelated entity. **Activity very likely real; ownership unconfirmed.
Do not state Ara runs these ads.**

### 4.8 Research-pass corrections (8/8/26)

| # | Correction |
|---|---|
| 1 | **Meta keyword search returned 139 false-positive "ads"** — Colgate India, Nestlé Nutrition Institute, unaffiliated derms in other cities. Re-run against confirmed FB Page URLs for 8 of 10; 2 unresolvable (Ara, Routines) reported `undetermined`, not guessed. |
| 2 | **Google Ads Transparency name-mode resolved only 1 of 10.** Caught via the run's `STATE` key-value record, not the dataset count. Domain-mode re-run surfaced active advertisers for 5 more (Ara, Haircosmos, Theory of Skin, Dermatonik, VIDA). |
| 3 | **`maxCrawlPages` is a GLOBAL cap, not per-site** — first website crawl covered only 6 of 10 sites. Re-run at 45, recovered all 10 (48 pages). |
| 4 | **Three clinics the source brief listed as having no website all had live sites** — Derma Solutions, Routines by Dr. Apoorva, Theory of Skin. Feed the corrected URLs back into the source list. |
| 5 | Practo false match: Routines resolved to *"Dr. Apoorva Singh"* in Ghaziabad — a different person in a different city. Dr AG Skin & Hair's Practo URL resolved to *"EastArise Aesthetics Clinic LLP"*. **Live name-collision risk.** |
| 6 | Data quirks kept as findings, not dropped: an Akera Meta ad legitimately renders `{{product.brand}}` (dynamic catalog placeholder) · Ara's GBP surfaced a Wix placeholder `info@domainname.com` alongside the real address · Haircosmos JP Nagar's GBP website field concatenates `drpiyushranjan.com`. |

### 4.9 Unverified fields, by clinic — the "do not assert" list

| Clinic | Still unverified |
|---|---|
| Gejje's Marvella | Founder name (**hard blocker**); Hospet branch operational status; LinkedIn; Practo listing |
| Haircosmos | Founder/owner identity (**hard blocker**); JP Nagar website-field anomaly; Practo; shop screenshot |
| Ara Skin | Google Ads attribution; Meta ads presence; LinkedIn |
| Dr. Priya's | LinkedIn (malformed); Dr. Naveen M Nayak's actual role; **who physically holds the WhatsApp phone** |
| Akera Health | Founder/owner identity (**blocker**); LinkedIn; whether branches share an inbox; whether 19 h is typical; daily enquiry volume |
| Derma Solutions | Founder-vs-consultant status; Dr. Thyagaraj J's affiliation depth; "Neo Follicle" relationship (not audited); shop screenshot |
| Theory of Skin | LinkedIn; reason for the Google Ads pause |
| Dermatonik | Treating dermatologist's identity (**never named**); Anjali Sanghvi's exact role; Practo; two-entity Google Ads reason |
| VIDA | LinkedIn; whether a brochure exists at all; whether "Indira" covers every channel |
| Vitals Klinic | Meta ad status (**direct contradiction**); Electronic City GBP listing; source of the "272" figure; JustDial |
| Krity 360 | Dental clinician identity/role ("Dr. Teju" vs "Dr. Mishali", employed vs partner); Practo; JustDial; chat widget |
| Project Skin | Founder name (**hard blocker**); single-vs-multi owner (§1.1 #5); Practo; JustDial paid-vs-free; whether IG dormancy is a pause or a deprioritisation |
| **All 12** | **§1.1 #4 avg treatment value ≥₹25,000 — no prices published on any website. Unknown, never inferred.** |

---

## 5. Wedges — confirmed vs. provisional, side by side

The **pre-shop** column is the 8/8 dossier hypothesis (PROVISIONAL by design). The **post-shop** column is
what the screenshot actually supports. Where they differ, the shop wins.

| Clinic | Pre-shop `funnel_break_stage` | Pre-shop entry SKU (PROVISIONAL) | Post-shop break | Confirmed wedge | Moved? |
|---|---|---|---|---|---|
| Akera Health | Response Speed | Dead-lead reactivation | Response Speed — **no acknowledgement exists** | Dead-lead reactivation | Held, sharpened |
| Dr. Priya's | Response Speed | Dead-lead reactivation (aggregator) | **Qualification** — priced, never booked | Systematize the hustle / manual dependency | **Moved** |
| Project Skin | Qualification | Dead-lead reactivation | **Qualification** — nothing re-surfaces an unanswered thread | Dead-lead reactivation | Held |
| Derma Solutions | Response Speed | Dead-lead reactivation (aggregator) | **Qualification** — fast, scriptless | **Enquiry deflection** | **Moved** |
| Haircosmos | **Booking / No-show** | No-show recovery | **Response Speed / Qualification** — slow on the question that matters | Dead-lead reactivation (high-ticket) | **Moved** |
| Dermatonik | Qualification | Qualification + scoring upgrade | Qualification — all outward, nothing inward | Qualification + scoring upgrade | Held |
| VIDA | Response Speed | Dead-lead reactivation (aggregator) | **Not timing** — pricing is not a routine | Fragility / capacity framing | **Moved** |
| Gejje's Marvella | Response Speed | Instant response + organic capture | Qualification — bot collects, nobody receives | Intake-handoff | **Moved** |
| Ara Skin | Response Speed | Dead-lead reactivation | Qualification — no second path when a call is declined | Written-path gap | **Moved** |
| Vitals Klinic | **Booking / No-show** | No-show recovery | **None (pass)** | **HARD KILL #9** | **Killed** |
| Krity 360 | None (pass) — candidate | Systematize the hustle (weakly supported) | TBD — clocks running | Quote-decay **or** hard kill #9 | Pending |
| Theory of Skin | **Reviews** | Review reactivation agent | TBD — clock expired today | Quote-decay + no-show recovery **or** park | Pending |

**Six of ten screenshot-backed wedges moved after the shop, one was killed outright.** That is the single
most useful statistic in this file about the value of the mystery shop relative to desk research.

### 5.1 What the stress test changed on 14/8, and why

Each observation was re-run against the §0.1 rebuttal test (*write the one sentence the doctor says back*)
and against `MEMORY.md` §2 (*could an Indian clinic owner say this, in these words, about their own day?*).

| Clinic | Failed on | Fix |
|---|---|---|
| **Akera** | *"That was one evening, we're normally quick"* — a complete rebuttal, off one data point | **Lead on the absence of any acknowledgement, not the 19 hours.** Not arguable; Akera is the only clinic of twelve with none |
| **VIDA** | *"Forty-five minutes is fast"* — correct, and it kills the whole degradation curve | **Drop the curve. Lead on the range with nothing attached.** Timing was never the failure |
| **Dr. Priya's** | Asserted she personally typed the replies — the screenshot doesn't prove it. Also *"no qualifying question"* fails: she asked *"regarding ?"* and *"U r asking about procedure?"* | State only what's verifiable — **no appointment was offered across three days.** Binary and checkable |
| **Ara** | *"No defined second path"* is a consultant's sentence, not hers | **Name the patient, not the process** |
| **Dermatonik** | Read almost identically to Gejje's — the §2.4 convergence problem | Separate them: **Gejje's withheld everything, Dermatonik gave everything and asked nothing** |
| **Project Skin** | Double bot-fire read as a gotcha | **Demoted to colour.** Two automations firing is a config artifact, not a business failure |

### 5.2 The batch pattern, and why it can't lead anywhere

Identical three-step script at all ten screenshot-backed clinics. But `ONE-PAGER-AUDIT-AND-TEST-PLAN.md` §2.4:
fifteen documents diagnosing one thing is *"the tell of a solution looking for a problem, and a sharp doctor
will feel it even if they can't name it."* **So the pattern leads nowhere and appears only as a second beat,
only where it is the sharpest thing present.**

---

## 6. Research dossiers — condensed, per clinic

*Research date 2026-08-08 unless noted. Pipeline: `clinic-audit-research` (Apify). All 12 Qualified at the
disqualification screen; zero hard kills at research time (Vitals' #9 kill came from the shop, not the desk).*

### 6.1 Dr. Priya's Skin & Hair Clinic · Marathahalli
1st Floor, CRM Sowbhagya Enclave, No:35/1, HAL Old Airport Rd, near Spice Garden Bus Stop, Lakshminarayana
Pura, Bengaluru 560037 · +91 97410 32946 · Skin care clinic · drpriyaskinandhairclinic.com ·
IG @drpriyaskinandhairclinic 9,660 · FB /drpriyaskinandhairclinic · X @PriyaSkin · LinkedIn truncated
(`linkedin.com/company/dr`, unusable). **1,613 reviews / 4.7★** — highest volume in batch. Distribution
1,350×5★ · 160×4★ · 18×3★ · 11×2★ · 74×1★. 90d: 89 sampled, 6 neg. Practo **Prime confirmed** — "Max. 60 mins
wait + Verified details", 98% recommended, **5,966 patient stories**. Zero Meta, zero Google.
**Recurring shape:** booking/appointment friction — multiple independent reviewers confirm a time then face
long unstructured waits (1★ 14/7/26: *"there is no appointment system"*, 1 h 45 m wait, procedure pushed out
20 days with unclear pricing — no reply). 2★ 5/8/26: acne treatment *"didn't work to great extent"*, products
*"super expensive"* — no reply. 1★ 10/6/26: *"lost my 5k in one month"* — **owner replied** with a clinical
explanation (chronic inflammatory scalp condition, possible minoxidil flare). An older Practo review describes
feeling dismissed and the doctor replying combatively.

### 6.2 Derma Solutions · Marathahalli
Number 3, 1st Floor, Scorpio House, near Marathahalli Bridge, opposite Purva Fountain Square, Bengaluru
560037 · +91 97412 23217 · Multi-speciality (Derm / Hair Transplant / Cosmetology) · dermasolutions.co.in
(**corrects the brief**, which said "WhatsApp link only") · IG @dermasolutionsskinclinic **159 — smallest in
batch**. **1,241 reviews / 4.6★.** Distribution 1,057×5★ · 85×4★ · 3×3★ · 7×2★ · **89×1★ = 7.2%, highest
negative rate in batch.** 90d: 64 sampled, 8 neg. **0/10 owner replies — flattest engagement in batch.**
Practo **Prime confirmed on both** Dr. Mahapatra and Dr. Thyagaraj J · 1,649 stories · **Practo 4.0★ vs
Google 4.6★ — a real cross-platform divergence.** Zero Meta, zero Google.
**Negatives:** 1★ 2/8/26 alleges untrained nursing staff and a *"messed up"* hair transplant fixed elsewhere,
*"mental trauma"* — no reply. 1★ 11/7/26 booked an evening appointment, waited an hour, never seen, left — no
reply. 1★ 25/6/26 consultation *"felt rushed"* — no reply. ~9 months ago: made to sign a consent form for a
**different, junior doctor** to perform a paid procedure without full agreement — **Dr. Mahapatra's own reply
was defensive** (*"Please don't spread misinformation... you were thankful at the end of the procedure"*).
**Caution note (Phase 5/6):** two independent reviews raise consent-process and procedure-quality concerns.
Below the hard-kill bar, but escalation-grade — and the one owner reply on record to a serious complaint was
combative. Relevant to how outreach lands. LinkedIn About names a second brand, **"Neo Follicle Hair
Transplant Clinic"** — not audited.

### 6.3 Akera Health · HSR Layout + HRBR Layout
Entity **Akera Healthcare Private Limited** · HSR: 2nd Floor, 112, 27th Main Rd, Sector 2, 560102,
+91 72044 84955 · HRBR: 2nd Floor, LV Plaza, HRBR 1st Block, 7th Main Rd, Banaswadi, 560043, +91 72044 88355 ·
Dermatologist · akerahealth.com · IG @akera.health 2,313 · FB /akerahealth. IG bio: *"Filters are great, but
great skin is better. Acne | Morpheus8 | Hair fall | Anti-Ageing."*
**Ads: 25 active Meta** (laser hair removal, chemical peels, GFC hair, laser toning; *"1000+ Happy Clients"*,
*"4.9★ Rated Clinic"* in copy) **+ 29 Google** (advertiser-mode confirmed). Practo listed, claimed, 4.5★,
26 stories, **no Prime on any of the 3 doctors** — all spend is direct.
**Reviews — HSR 315 / 4.9★** (306×5★, 3×4★, 1×2★, 5×1★), newest 8/8/26; 6 neg sampled, 1 replied (17%) —
2★ 13/2/26 consultation *"felt somewhat sales-driven, with a strong push"* toward packages, **owner replied**
referencing a follow-up call already had; 1★ 31/5/26 overpriced retail vs MRP, no reply.
**HRBR 361 / 4.9★** (349×5★, 9×4★, 1×2★, 2×1★), newest 29/7/26; 2 neg, 1 replied (50%) — 1★ 27/2/26
*"completed 12 months of treatment but did not see any improvement"*, **owner replied** empathetically.
Where owners reply the tone is constructive and specific — better than most of the batch — but 2/8 (25%) is
low against the ad scale. **Textbook "ads ✓, unknown response speed" profile.**

### 6.4 Project Skin Dermatology & Aesthetic Clinic · HSR Layout
Entity **ASJ Aesthetic Clinics LLP** · 952, 8th Cross Road, 27th Main Rd, 1st Sector, HSR Layout, 560102 ·
+91 81233 55968 · info@projectskin.in · projectskin.in · IG @projectskin.in 2,189, 140 posts, **last post
2026-06-24, 0 posts/30d** · LinkedIn /company/projectskin 546 followers · GBP Facebook field is a broken
placeholder (`facebook.com/share`). **Established 02-2025** — stated on JustDial, corroborated by the oldest
Google review (2025-02-19). **~18 months — youngest in batch.**
**Founder: not named anywhere.** Full website crawl, LinkedIn company page, GBP and a targeted search all
clean. About page ("Beyond the Surface") is pure brand copy — *"The quintessence of Project Skin can be
defined in layers, reflecting the architecture of skin itself"* — no named clinician, no credentials, no team
section. **Two live leads:** the LLP registry (ASJ plausibly founder initials) and the JustDial proprietor field.
**Ads: 11 Google creatives, ASJ Aesthetic Clinics LLP (AR15654855403907317761), 2025-06-05 → 2026-08-07
continuous, incl. video.** Meta 0 (verified). JustDial listing confirmed, paid status unknown. Practo not located.
Website: five pages, clean but thin. Enquiry form captures **Name / Number / Email only.** No chat widget.
Footer credits "Powered by WelkinWits" and "Copyright (C) 2024" — predates the Feb-2025 establishment, so it
reflects the site build, not the clinic.
**Reviews: 102 / 5.0★ — full census.** 101×5★ · 1×4★ · **0 negatives across the entire base.** Newest
2026-08-08 (five in 48 h). Oldest 2025-02-19. §1.1 #5 flag from a 5★: *"Post treatment consultation was also
quite organized because the **owners** manage the clinic and not just staff."* Fake-review check: steady
arrival over 18 months, specific varied text (hydrafacial, pigmentation, scars), no burst — reads organic,
but a 102/102 clean sheet is worth naming rather than glossing.

### 6.5 Haircosmos International · JP Nagar + Whitefield
Entity **HAIRCOSMOS DIAGNOSTIC AND HEALTH CARE PRIVATE LIMITED** · JP Nagar: 1st Floor, 15, 24th Main Rd,
Puttenahalli, JP Nagar 7th Phase, 560078, +91 72049 92757 · Whitefield: 32, Varthur Main Rd, opposite Sigma
Soft Tech Park, Ramagondanahalli, 560066, +91 73491 87047 · Hair transplantation clinic ·
haircosmosinternational.com · IG @haircosmos_international **18,525**, 568 posts · FB
/HaircosmosInternationtionalhairskinclinicbangalore · X @HaircosmosI. IG bio: *"#1 Hair Transplant &
Dermatologist Clinic. Awarded Best Hair Transplant Clinic by @businessmint."*
**No founder or doctor named anywhere** — not IG bio, not the website About Us (entirely generic), not GBP.
LinkedIn `/in/haircosmos-international-7006a7238` exists but is abandoned: blank headline, 0 connections,
1 follower. The Phase 4 ladder genuinely returned nothing — a phone/generic contact is the honest ceiling.
**Ads: 3 active Meta** (Independence Day laser hair removal bundle; hair patch from ₹9,999; hair transplant
from **₹49,999** with 0% EMI). Google: 1 creative, 2025-05-20 → 2025-12-04, **inactive ~8 months.** Practo
returned a category page — undetermined.
**Reviews — Whitefield 499 / 4.9★** (480×5★, 8×4★, 2×3★, 1×2★, 8×1★), newest 2/8/26; 90d 23 sampled, 4 neg;
**0/6 replies.** 1★ 28/7/26: relative's scalp infection after a procedure, unresolved *"one and half month"*,
staff deflecting onto the patient's own post-care — no reply. 1★ 12/5/26: *"went for 8 sessions as
suggested... saw no results... she said I should do 6 more and pay more"* — no reply.
**JP Nagar 169 / 4.9★** (166×5★, 3×1★), newest 28/6/26 — **40-day gap.** **0/2 replies.** 1★ 4/4/26: booked
appointment, *"the doctor never showed up"*, clinic nearly empty. 1★ 26/7/24: *"worst service"*, two named
treatments ineffective, no post-treatment follow-up. **Cross-branch shape: unresolved post-procedure issues
and no-shows, zero owner replies to any negative in either branch (0/8).**

### 6.6 Dermatonik Aesthetic Clinic · HSR Layout
2nd Floor, 1655, 27th Main Rd, opposite NIFT College, 1st Sector, HSR Layout, 560102 · +91 89510 11944 ·
Skin care clinic · dermatonik.com · IG @dermatonik_ 2,454 · FB profile.php?id=61558573610970.
**No dermatologist named anywhere** — the website describes services as delivered by *"your dermatologist"*
on every service page crawled. GBP surfaced `Info@anjalisanghvi.com` alongside `dermatonik@gmail.com`; the
site credits **Anjali Sanghvi** for **permanent makeup specifically**, not as medical director; the Google Ads
advertiser is **"Anjali Sanghvi LLP."** Three independent signals → **likely business owner/operator, no
evidence she treats.**
**Ads: 4 active Meta** (*"Limited-Period Special... Upto 50% OFF"* — HydraFacial, acne, pigmentation/melasma,
skin boosters) + **two Google advertiser entities** ("Anjali Sanghvi LLP" and a differently-cased duplicate),
**heaviest sustained presence in batch by duration** — near-continuous ~1 year, still active. Practo undetermined.
**Reviews: 304 / 4.8★** (281×5★, 5×4★, 2×3★, 1×2★, 15×1★), newest 6/8/26. 90d: 53 sampled, 2 neg. 180d: 91
sampled, 8 neg. **2/10 replies (20%), tone formulaic/defensive.** 1★ 29/6/26: called ahead, told a
dermatologist was available, on arrival **there was none**, still **charged ₹700**, no refund — no reply.
1★ 24/4/26: *"costly and not worth the money"* — owner replied defending pricing without addressing specifics.
1★ 3/4/26: no text; owner replied stating they checked records and found no matching appointment — defensive
framing, unverifiable from outside. **A pre-visit information-accuracy failure is a distinct funnel-break
signature from the booking/no-show pattern elsewhere in this batch.**

### 6.7 VIDA Skin & Hair Transplant Clinic · Whitefield
2, 75, Whitefield Main Rd, Giddens Layout, Narayanappa Garden, 560066 · +91 70325 82393 · Hair
transplantation clinic · vidaskinandhairclinic.com · IG @vida_skin_clinic 1,165 followers / **738 posts** —
content-heavy, modest following. Founder **Dr. Jigisha N. Jalu** confirmed via her own IG: *"MBBS, MD (Skin &
VD), FRGUHS [Fellow in Dermatosurgery and Hair Transplantation, B.M.C.R.I., Bengaluru]."*
**Ads:** Meta 0 · Google **12 creatives, advertiser "Jigisha jalu", active — last shown 2026-08-07** ·
Practo **Prime confirmed**, 302 stories, 90% recommended. **Unusual mix: Google + Practo, zero Meta.**
**Reviews: 390 / 4.8★** (361×5★, 10×4★, 2×3★, 2×2★, 15×1★), newest 3/8/26. **3/5 replies (60%) — among the
better rates.** **Recurring shape: three independent reviewers on different dates describe pricing pressure
and escalating costs** — 1★ 20/5/26 pricing *"very much high compared to other places"*, response felt
*"insulting"* (no reply) · 1★ 19/4/26 medicines only available in-house (~₹2,000), **owner replied** with a
named diagnosis and rationale · 1★ 9/11/25 *"very highly money minded clinic"*, charges *"keep increasing
every 2-3 months"*, persistent upsell — **owner replied**, detailed and non-defensive.
**Not a named §3 wedge** — service-quality/trust context that should inform framing, and per the shop notes
**must not be raised** in copy.

### 6.8 Gejje's Marvella · Basavanagudi (+ possible Hospet)
Level 4, Bangalore Superspecialty Center, New High School Rd, behind Metro Station National College,
Parvathipuram, Vishweshwarapura, Basavanagudi, 560004 · +91 99162 49637 · **Plastic surgery clinic (GBP)** ·
gejjesmarvella.com · IG @gejjesmarvella 6,933 / 523 posts · FB /GejjesMarvella. IG bio: *"Plastic Surgery,
Reconstructive Surgery, Aesthetic Surgery, Hair transplantation, Hand Surgery, Dermatology"* — **unusually
broad specialty mix for this batch.**
**Second location:** GBP returned `gejjesmarvella@gmail.com` **and** `gejjesmarvellahosapete@gmail.com`
(Hospet is ~330 km away). Originally an unaudited lead; **now corroborated by the clinic's own auto-reply
naming "Bengaluru & Vijayanagara (Hospet)."**
**Ads: 0 on Meta (confirmed page), 0 on Google (by domain).** Practo resolved to an unrelated pediatric
clinic — undetermined. **No paid spend anywhere → no money-at-stake framing available.**
**Reviews: 870 / 5.0★.** 120-newest sample: 2 negatives. Newest: same-day. 90d: 28 sampled, 0 neg. 180d: 39
sampled, 0 neg. **1/2 replies (50%)** — 1★ 8/1/26 *"Poor in medical consult"* no reply · 1★ 15/4/25 poor
consult + staff manner, **owner replied** acknowledging and inviting contact. Fake-review check: clean, no
burst, procedure- and staff-specific quotes. Genuinely strong reputation.

### 6.9 Ara Skin (and Hair) Clinic · Shankarapura, Basavanagudi
1st floor, Paras Vatika, 49/1, Shankar Mutt Rd, 560004 · +91 98898 82246 · Skin care clinic ·
araskinclinic.com · IG @ara_skin_clinic 4,758 / 711 posts. Founder **Dr. Sonakshi Sunil** confirmed via the
clinic's own IG bio: *"Best Dermatology clinic in Bengaluru by @dr.sonakshi_sunil MBBS, MD (DVL)
Dermatology."* GBP Facebook link is a broken placeholder (`facebook.com/share`); GBP also surfaced a leftover
Wix template email `info@domainname.com` alongside the real `glow@araskinclinic.com`.
**Ads:** Meta **undetermined** — keyword and page-name searches both returned unrelated pages ("Advanced
Grohair Clinic Puducherry", "Sikara Clinic"); no matching FB Page found. Google **19 creatives, Sept 2023 →
current, billed to "Pure Dermacare"** — see §4.7. Practo **confirmed, no Prime**, ₹750 consult, **2 patient
stories vs 294 on Google** — Practo is a largely unused secondary listing.
**Reviews: 294 / 4.8★** (264×5★, 19×4★, 3×2★, 8×1★), newest 5/8/26. 90d: 28 sampled, 0 neg. **4/4 replies
(100%) — strongest owner engagement in the batch**, all substantive and non-templated: 2★ 10/2/26 laser
showed no result after one session → a real clinical explanation of why single-session results are limited ·
2★ 28/7/25 acne scarring worsened after a prescribed tablet → disputed the causal claim but invited a
follow-up · two text-less 1★ → replied by name, asked what went wrong.

### 6.10 Vitals Klinic · BTM Layout + Electronic City + Whitefield
GBP names vary ("Vitals Skin and Hair Clinic", "Vitals skin Hair and laser klinic") · vitalsklinic.com —
40+ treatment SEO pages plus dedicated location pages for BTM, Electronic City and Whitefield, confirming
**3 active branches** · IG @vitalsklinic 8,100 / 595 posts, last post 6/8/26, 10 posts/30d, **2 comments
across the last 12 posts** · FB /vitalsklinic (page ID 317939428557405) · LinkedIn /company/vitals-klinic ·
vitalsklinic@gmail.com, contact@vitalsklinic.com. Founder **Dr. Harish Prasad B.R** — personal LinkedIn
verified, headline *"MD Dermatologist | Vitals Klinic, Bangalore"*, **sole named doctor across 3 branches →
single decision-maker.** Website has a `/team-of-qualified-dermatologist` page.
**Locations:** BTM (390, 7th Cross Rd, BTM 2nd Stage) **1,892 / 4.7★**, newest 7/8/26 · Whitefield (Arcadia
Grace #205A) 6 / 4.3★ · **BEL Layout / Bedarahalli 14 / 4.6★ — PERMANENTLY CLOSED.** Electronic City listing
**never surfaced.**
**Booking paths:** `/book-appointment/` page · WhatsApp click-to-chat (`api.whatsapp.com/send?phone=
+919740484793`) with a generic pre-filled greeting · "Request a Call Back" form. **No live chat widget. No
qualification questions at any entry point** (per the desk pass — the shop then found the live WhatsApp
number *does* qualify; see §4.2). Site builder VBS Technologies — a web-design vendor, not a social agency.
The "~2-day / 14:00 UTC posting cadence implies an agency" hypothesis remains **uncorroborated by both passes.**
**Ads:** Meta **0, verified twice** (active-only and all-status, `isResultComplete: true`, `pageIsDeleted:
false`, `hiddenAds: 0`) ⚠️ contradicted — §4.2. Google **0**. Practo **Prime confirmed** 4.5★, 146 stories,
₹1,000 consult. JustDial not located.
**Reviews: BTM 1,892 / 4.7★** — 1,649×5★ · 145×4★ · 15×3★ · 13×2★ · **70×1★ (3.7%)**. 165 newest sampled
(2026-01-19 → 2026-08-07) ≈ 165 in 7 months, fast healthy flow. **Cross-branch booking-failure pattern,
three independent reviewers:** 1★ 3/7/26 BTM *"Had got appointment for 12 PM. Doctor doesnt turn up till 1
PM. After I leave, I get a call from reception that the doctor has just reached"* → owner reply in full:
*"It was medical emergency so it was delayed"* · 1★ 15/7/26 Whitefield *"after Waiting for one hour doctor
did not came.. pathetic"* → *"Sir we called u so many times but there was no response since heavy traffic
doctor got late"* · 2★ BTM appointments at 11 am, seen 3–5 min *"almost 1 hour beyond the scheduled
time"*, plus pressure to buy in-house pharmacy *"well above online price options"* at ~₹4k/consult — **no
reply** · 1★ BTM receptionist dispute over a wrong serum against prescription — **no reply.**
**Reply asymmetry worth naming:** positives get long, warm, personalised replies (*"Hi Tanmaya, thank you for
the wonderful 5-star review!..."*); **the two most detailed negatives got nothing**, the two that did got one
curt line each. **Someone is actively working the review channel — but only the happy half of it.**

### 6.11 Krity 360 · Kasavanahalli / Bellandur
Aadeshwar Chambers, 34/5, 1st Cross Rd, Kasavanahalli, 560035 · krity.in (About, Services — skin
rejuvenation / concern-based / hair / **aesthetic dentistry** / permanent makeup — Blog, Contact) ·
IG @krity.360 456 / 130 posts, last post 4/8/26, 4 posts/30d, 6 comments across last 12 · LinkedIn
/company/krity360 · **no Facebook page found** · +91 93807 89495 · kritywellness@gmail.com. Founder
**Dr. Kavita Raghotham**; a second clinician **"Dr. Teju"** appears by name in a review performing a root
canal, and an earlier pass saw **"Dr. Mishali"** — one person or two, employed or partner, **still unresolved
(§1.1 #5 flagged, not a kill).**
Booking paths: WhatsApp click-to-chat via two links (`wa.me/919380789495` and a `wa.link/3vm0mv` shortener),
phone, email, contact page. Chat widget **unknown, not absent** — the extraction never returned yes/no.
**Ads: Meta 0** (`totalCount: 0`, `isResultComplete: true`; consistent with no FB page at all) · **Google 0**
for krity.in · Practo **not located — do not construct the URL** · JustDial pending. **No paid acquisition
channel found anywhere. Growth entirely organic.**
**Reviews: 157 / 4.9★ — full census.** 150×5★ · 5×4★ · 0×3★ · 0×2★ · **2×1★ (1.3%)**. Newest 4/8/26, oldest
**2024-03-11** (see §4.6).
**The single most informative artefact in the batch's research layer** — 1★ 2/8/26: *"They charged me Rs 750
consultation fee only to tell me that it their closing time and they will do treatment next day... So
basically no consultation was done. And still I was asked to pay Rs 750... And they kept calling again n
again."* Owner reply (abridged): *"Your appointment was scheduled for 1:30 pm, which we confirmed by message
at 1:14 pm. When you had not arrived, we called at 2:21 pm, during which you informed us that you were on
your way. We also reminded you that the clinic would be closing at 5:00 pm that day. As the closing time
approached, we called again at 4:41 pm. You arrived at 4:55 pm, five minutes before closing..."* — then a
clinical explanation of why a consultation precedes skin-tag removal.
**Why it matters:** that reply reconstructs a confirmation message and two chase calls with exact timestamps.
A clinic that can do that is already running — and logging — an appointment-confirmation and follow-up
process. The complaint is a patient who arrived 3.5 hours late. **This is evidence of a functioning process,
not a broken one.** Corroborating: multiple 5★ describe proactive post-treatment follow-up calls (*"she even
called me for follow up... The staff also called me later to check up on my health."*). Replies are
substantive and signed "Team Krity 360". **The mystery shop should be run to disprove #9, not to confirm a
pre-selected wedge.**

### 6.12 Theory of Skin Dermatology & Aesthetics · Indiranagar
578, 9th A Main Rd, 1st Stage, Defence Colony, Indiranagar, 560038 · +91 96862 37333 · Dermatologist ·
theoryofskin.co.in (**corrects the brief**, which said "None (Maps link)") · IG
@theoryofskin_dermatology **15,552, verified** · FB /theoryofskindermatology · contactus@theoryofskin.co.in.
Founder **Dr. Sanjana Shivashankar** confirmed via her own verified IG: *"MBBS, MD Dermatology, FRGUHS
Dermatosurgery."* **§1.2 park signal (Medium):** possible mega-founder-brand — route through the standard
playbook, not a founder-capacity pitch, unless the shop confirms overflow.
**Ads:** Meta 0 · Google advertiser "Sanjana Shivashankar", **5 creatives, last shown 2026-06-01 — paused
~2 months** · Practo confirmed, 74 stories, 4.0★, **no Prime.**
**Reviews: 215 / 4.6★** — 185×5★ · 7×4★ · 3×3★ · 1×2★ · **19×1★ = 8.8%, second-highest negative rate.**
**Newest review 2026-04-03 — a 126-day gap, stalest flow in the batch**, despite a verified 15.5K IG and
Google Ads running until ~2 months prior. 90d: 0 reviews. 180d: 5 sampled. **2/14 replies (14%).**
1★ 11/3/26: travelled to the clinic only to be told on arrival *"the doctor does not even take appointments
on Wednesday"* — **owner replied**, acknowledged the communication failure, apologised by name. 2★ 14/10/25:
confirmed by phone one hour prior, arrived on time, told the doctor had stepped out for a personal checkup
and would return in 90 minutes — no reply. **Two independent appointment-confirmation failures.**
**The stall itself is the headline finding** — per Phase 5, a pipeline quiet 4+ months amid active marketing
elsewhere is a signal, not evidence of health.

---

## 7. Follow-up-2 messages as drafted (14/8) — full text

*First person singular, one observation, one question, no service named, structure deliberately rotated so no
two share an opening shape. **Names in brackets are unresolved and must be settled before sending.***

**1 · Akera Health — [addressee unresolved: founder not identified]**
> I messaged the HRBR number on Monday at 4:23 in the afternoon, asking about acne scarring. The first reply
> came at 11:31 the next morning.
>
> The wait isn't really the thing. It's that nothing came in between — no automatic acknowledgement, nothing
> sitting on the enquiry until someone was free. And once a person did pick it up, the answers were good:
> twelve minutes to a treatment answer, then a full price list.
>
> So the question I'd want answered if this were mine — of the enquiries that came in last month, how many
> got a reply the same day? And is that written down anywhere?

**2 · Ara Skin Clinic — Dr. Sonakshi**
> I messaged the clinic on Monday asking about acne scars. Someone came back in two minutes, offering to call.
>
> I said I was at work and asked if they could send the details across instead. I asked twice. That was the
> last message in the thread.
>
> You reply personally to every negative review on your Google listing — all four of them, properly, not with
> a template. So this doesn't look like inattention to me. It looks like there's one route, and nothing behind
> it for the patient who can't take a call at half four on a working day.
>
> When someone says "just send it to me" — what's meant to happen next?

**3 · Dr. Priya's Skin & Hair — Dr. Priya**
> I asked about acne scar treatment last week and got a full price list back — MNRF 9.5k, dermapen 10k, MDF
> 8.5k. Clear, and quicker than most.
>
> What I noticed was what didn't happen. Nobody asked when I could come in. Not that day, not the next.
>
> With close to 6,000 patient stories on Practo, that's a lot of people receiving numbers. The part I'd want
> to know if it were my clinic: of the people quoted a price last month, how many actually booked — and where
> would you go to look that up?

**4 · VIDA Skin & Hair — Dr. Jigisha**
> I messaged the clinic on Monday and Indira came back within two minutes. She used my name, said who she was,
> and asked what I was actually looking for. That's better than most of what I see.
>
> Then I asked for a pricing brochure or some details, and what came back was a single line — "It start from
> 3500 to 6500."
>
> I'm not pointing at how long it took. It's that someone weighing up two or three clinics can't do much with
> a starting figure.
>
> When a patient asks what something costs, what does the person answering have in front of them?

**5 · Dermatonik — [addressee unresolved: Dr. Saeema Shiraaz or Anjali Sanghvi]**
> I messaged the clinic on Monday asking about acne. Within three minutes I had before-and-after photos of
> real patients — genuinely good ones. Next day I asked about pricing and had "starting 5500" back, again in
> three minutes.
>
> Nobody asked me anything.
>
> Your own welcome message asks the patient to share their concern. I answered it — acne — and over three
> days no one picked it up. Not what kind, not how long I'd had it, not when I could come in.
>
> Of the people who got a price last month, is there a way to tell which ones were serious?

**6 · Project Skin — [addressee unresolved: founder not named]**
> I messaged on Monday at 4:43. Two automatic replies came back inside the minute, the second one saying
> you'd get back to me soon.
>
> Nothing came that day. I messaged again the following afternoon and had a real answer in sixty seconds,
> with full pricing after that. So the team is quick when a message is actually in front of them.
>
> Which is what makes the first one worth looking at. I can't tell you nobody would ever have replied — I
> interrupted that by messaging again. What I can tell you is that twenty-two hours passed on a promise that
> was made automatically.
>
> If an enquiry got that welcome message and then nothing, where would it show up?

**7 · Gejje's Marvella — [addressee unresolved: founder uncorroborated]**
> Your automatic reply is the most thorough I've come across — specialties, board certification, both
> locations, the website, and then: share your concern, your preferred location, and photos if you're
> comfortable.
>
> I messaged on Monday. Over three days I got three replies. "Hlo... yes tell me." Then "Yes. Treatment
> available" and "Visit the clinic." Then a note that pricing depends on the area.
>
> None of the three mentioned my concern, which location, or the photos.
>
> Someone set that welcome message up knowing exactly what a patient should be asked. When a patient does
> send those three things — who receives them?

**8 · Derma Solutions — Dr. Sandeep** · ⚠️ *Screenshot missing. Do not send until the thread is produced — every fact below is from the Notion note, not from an image.*
> I messaged the clinic asking about acne and scarring and had a reply in under a minute — faster than almost
> anyone I've contacted.
>
> The reply was a link to the website, plus links to Facebook, Instagram and YouTube.
>
> I'd already read the website. That's where I found the number.
>
> With Practo Prime running on both you and Dr. Thyagaraj, those enquiries are paid for one at a time. So
> what I keep coming back to is — what does the person answering WhatsApp have to send that the site doesn't
> already say?

**9 · Haircosmos International — [addressee unresolved: no principal named]** · ⚠️ *Screenshot missing. Do not send until the thread is produced.*
> I messaged asking about hair treatment and had "how can I help you" back in three minutes.
>
> Then I asked what you actually treat. That answer took two and a half hours, and it was four words — "gfc
> exosome qr678 prp."
>
> I know what those are now. Someone weighing up a transplant across two or three clinics mostly won't.
>
> The bit that stayed with me: the easy question got a quick answer, and the one that decided whether I
> booked took longest. Who's meant to answer a treatment question — and what happens to it while they're with
> a patient?

**10 · Vitals Klinic — Dr. Harish** · *Not a diagnostic. Nothing attached, no ask. Send as a message only.*
> This isn't a pitch and there's nothing attached to it.
>
> I messaged your BTM number last week as a patient would, because I spend my time looking at how clinics
> handle enquiries. Yours replied in a minute, asked what I needed, followed up an hour later without being
> prompted, sent real pricing, and put a booking form in front of me. Four minutes from first message to
> bookable.
>
> I've not seen another clinic here do that.
>
> Genuinely curious — what did you build it on?

**Deliberately absent from all ten:** no "several clinics" framing anywhere (including Akera, where the
comparison is the strongest fact available and still cannot be said) · no call as the ask · no "free" · no
superlatives · no greeting filler · nothing about ads in any message.

**Krity 360 and Theory of Skin have no drafted message — both were under a live silence clock on 14/8.**

---

## 8. Ship order, blockers, and what each one needs

| # | Clinic | Leads on | Status | Unblocking action |
|---|---|---|---|---|
| 1 | **Akera Health** | The only clinic of twelve where an enquiry got no acknowledgement at all | Ready | MCA lookup: Akera Healthcare Pvt Ltd |
| 2 | **Ara Skin** | The patient who said "just send it to me" | **Fully unblocked** | — |
| 3 | **Dr. Priya's** | A full price list went out; no appointment was ever offered | **Fully unblocked** | — |
| 4 | **VIDA** | A brochure was asked for; a starting figure came back | **Fully unblocked** | — |
| 5 | **Dermatonik** | Everything sent outward, nothing asked back | Ready | Decide addressee: Dr. Saeema Shiraaz vs Anjali Sanghvi |
| 6 | **Project Skin** | The message that promises a callback is the one that didn't produce one | Ready | MCA: ASJ Aesthetic Clinics LLP + settle single-vs-multi owner (§1.1 #5) |
| 7 | **Gejje's Marvella** | The welcome message asks three things nobody uses | **Blocked** | Verify founder name — two minutes of work |
| 8 | **Derma Solutions** | Sixty seconds, and a link | **Blocked** | Produce the shop screenshot |
| 9 | **Haircosmos** | The wait gets longer the more the question matters | **Blocked ×2** | Screenshot **and** a named principal |
| — | **Vitals Klinic** | — | **Do not send a diagnostic** | Optional: send the short "what did you build it on?" message |
| — | **Krity 360** | — | **Do not message** | 14-day review **~24/8/26** — watch the *shape* of any chase |
| — | **Theory of Skin** | — | Clock **expired 17/8/26 — today** | Decide: did they chase the ₹4,500 quote or the 12:30 slot? |

### 8.1 What decides whether these convert — and it isn't the observation

The observations are genuinely stronger than the previous fifteen: first-party, dated, screenshot-backed,
each surviving a rebuttal attempt. **It is probably not the thing that converts.** The record on this asset is
~25 sent, 2 replies, **0 calls**, and the audit's diagnosis was that the **ask** fails, not the finding —
*"at the exact moment the reader is most impressed, the ask is: would you like more of what you just got, but
longer, and on a call with a stranger?"* Sharpening nine observations does not touch that.

Three things that plausibly do:

1. **The close.** Still undecided, and where the leverage is. The playbook now requires a specific named thing
   plus two named slots, not a free audit.
2. **Something they can test.** The WhatsApp qualification/booking demo is **built and live**, and not one of
   these nine documents uses it. `OUTBOUND_MEMORY.md` §5b: a claim they can test is the only real evidence a
   company with no clients has. Ending on *"here's a number — message it the way a patient would"* costs them
   twenty seconds and nothing else in the folder comes close.
3. **Whether she feels recognised or surveilled.** Nine of these say, however politely, *I tested you and
   found something.* Bangalore aesthetic dermatology is small — same conferences, same device reps, same
   WhatsApp groups. **Two of these landing on the same table dissolves the personalisation instantly.** Worth
   rotating structure hard, and worth deciding whether nine go out at once or in two waves.

### 8.2 Research-side next actions still open (from the 8/8 pass)

1. Confirm the **Ara Skin / "Pure Dermacare"** Google Ads attribution before treating that spend as theirs.
2. **MCA / LinkedIn / JustDial hunt** for a named decision-maker at Akera, Haircosmos and Project Skin — all
   three are blocked on identity, and two are among the batch's heaviest advertisers.
3. Feed the **corrected website URLs** (Derma Solutions, Routines, Theory of Skin) back into the source list.
4. Resolve the **Vitals Meta-ad contradiction** and capture the missing **Electronic City** GBP listing.
5. Produce the two **missing shop screenshots** (Derma Solutions, Haircosmos).

---

## 9. Standing rules that bind anything drafted for this batch

**Two blocks on a new Day-0 batch — both still unmet:**
1. `SALES_MOTION.md` §7 — no new Day-0 batch until the **walkthrough video** and the **How We Work PDF**
   exist as files.
2. `OUTBOUND_MEMORY.md` §6 (2026-08-04) — **a warm reply outranks the send quota.** Sapphire and Aesthetica
   Veda are both open.

**Every hook passes the rebuttal test** (`wedge-signal-entry.md` §0.1): write the one sentence the doctor says
back. If a plausible rebuttal exists, it doesn't ship.

**Evidence bar:** a first-party test **or** ≥2 independent instances. Single-incident review quotes don't ship.

**Admissibility:** all 12 shops ran 3:00–4:45 PM on a weekday against clinics staffed to 8 PM — every gap is a
**best-case floor**, and saying so (*"at 4:23 on a working Tuesday afternoon"*) removes the "we were closed"
defence. The **Sat 15/8 10:30 PM after-hours sweep** in the Notion notes produces **inadmissible** evidence
under the published-hours rule adopted 13/8 — `MEMORY.md` §5 flags this as an open disagreement; the cheap fix
is **Saturday 6 PM** (92% published-open, the highest slot in the SE Bangalore dataset).

**Never sell speed to a fast responder** (§2.5) — flagged four times and still happening. **Dr. Priya (1 min),
Krity (1 min), VIDA (2 min), Theory of Skin (instant), Derma Solutions (60 s), Vitals (1 min)** are all fast.
For these, sell fragility and cost: *"keep your closer, remove the chasing."*

**Banned:** leads / funnel / pipeline / conversion / ROI / lead-gen / RevOps / infrastructure / "scale your
practice" / "growth" · AI as a lead · any guaranteed patient number · rev-share at cold stage · superlatives ·
generic compliments · greeting filler · fabricated case studies · **identical text to more than one person at
the same clinic** (already burned once on Glow Clinic) · **asking for a call as the first ask** · **the
several-clinics / "twelve clinics tested" framing** (`MEMORY.md` §2: *worse than silence*).

**Format rules for the follow-up-2 documents** (from `one-pager-handoff/CLAUDE.md`, which reverses three older
rules — the files in `one-pager-handoff/examples/` violate all of them; copy the scaffold, not the words):
**250–350 words, enforced** (the previous fifteen ran 529–703) · sign with a real name, *"— Tilak, Valence
Ops"*, plus *"This is a read on public information and one test enquiry — not clinic data. Happy to be told
where it's wrong."* · **the close is the question, not a meeting ask** · never say "free" — "at no cost to the
clinic" · **never invent a number, not even a range** · rotate the structure (the same subhead ran verbatim in
10 of 10 previous documents) · no superlatives, brand name exactly once · nothing about the service —
confirmed / can't confirm / would check first, then the question.

**Offer shape:** free audit + free strategy document; **₹20k setup / ₹40k month** is the paid path and only
after the document. ⚠️ **Unresolved:** whether the free 2–3 week pilot still exists as a distinct step — ask
before quoting a price or describing step 3.

**Demo:** WhatsApp qualification + booking is **live and testable** — hand over the number. No-show recovery,
quote-decay chase and dormant reactivation are walked through **as message sequences only**; say that limit out
loud rather than letting a founder find it.

**Voice/video:** beats, never a script. Numbered fragments + an anchor-fact table with spoken phrasing +
recording method. Never three balanced items in a row.

**No entry names a service.** `recommended_entry_sku` in `wedge-signal-entry.md` §4 is an **internal routing
label**; `MEMORY.md` §2 records what happened when those labels drifted into client-facing copy. What gets
built is proposed after the audit, from the clinic's own data.

---

## Appendix A — In the folder, not in the batch

**Routines by Dr. Apoorva · Malleshwaram** — researched 8/8/26 in `go-list-full-report.md` §6.7, **no
per-clinic dossier file, no Notion row, never shopped, never contacted.** Parked inventory, not a backlog
item. **Exclude from every batch-7 denominator.**

No.285, 1st Floor, between 17th and 18th Cross, Sampige Rd, Malleshwaram, 560003 · +91 91102 61781 ·
Dermatologist · routinesbydrapoorva.com (**corrects the brief**, which said "None (Maps link)") ·
IG @routinesbydrapoorva 2,033 followers — **highest engagement-to-follower ratio in the batch** (54 comments
across 12 posts). Founder **Dr. Apoorva Bharadwaj** confirmed — the IG account is hers.
**Ads:** Meta undetermined (no page found, GBP returned no FB link) · Google 0 by domain · Practo **false
match** — resolved to "Dr. Apoorva Singh" in Ghaziabad, a different person in a different city.
**Reviews: 217 / 5.0★** — 212×5★ · 4×4★ · 0×3★ · 0×2★ · 1×1★. 90d: 40 sampled, **0 negative.** 180d: 85
sampled, **0 negative.** No recurring complaint shape exists in the data.
Pre-shop tag: `funnel_break_stage: Response Speed` · `Instant response + organic capture — PROVISIONAL` ·
**the thinnest-evidence wedge call of the eleven, stated honestly.** Per the playbook, "strong surface
reputation with no visible weakness" is **not** a disqualifier — the shop decides. A pass on all tests makes
this a legitimate **§1.1 #9 hard-kill candidate** ("functioning system already in place"), the same place
Vitals Klinic landed.

**Also referenced but not in this folder:** `23-d-white-feather.md` and `24-dr-ag-skin-and-hair.md` are named
in `batch-11-15-summary.md` but the dossier files are not present in `batch7/`. D White Feather: founded 2021
confirmed, 633 reviews, 1★ 13/1/26 *"Highly overpriced!... Avoid if you don't want to get overcharged"*, Meta
ad check **failed with a false "0 ads" reading** (results panel never rendered — explicitly not a confirmed
zero), founder Dr. Kanchan Chaudhary + associate Dr. Abhishek Ponathil, governance unresolved. Dr AG Skin &
Hair: founder Dr. Dinesh GG, single doctor, 32 reviews, website **found** (dragskinandhairclinic.com) despite
the source saying none, oldest review 2024-08-08 clearing the age concern, Practo listing **mismatched to a
different clinic** and ruled out. **Both are outside batch 7's 12 — do not count them.**

---

## Appendix B — Method and provenance

**Pipeline:** `clinic-audit-research` (Apify), research date 2026-08-08. Standard depth mode, all clinics.
Outcome at the desk: **all Qualified, 0 Park, 0 Disqualified.**

| Step | Actor | Coverage |
|---|---|---|
| GBP + reviews + contact enrichment | `compass/crawler-google-places` | 2 batched runs, 12 places (7+5 search terms), 120 newest reviews per place |
| Instagram profile refresh | `apify/instagram-profile-scraper` | All handles — bio, followers, posts, external URL (run `EesNLVkPYhlCqqs50`) |
| Meta ads | `apify/facebook-ads-scraper` | Keyword sweep first, then **8 re-run against confirmed FB Page URLs** after the sweep proved unreliable |
| Google Ads Transparency | `scrapesage/google-ads-transparency-scraper` | Brand-name query first, then **9 re-run by domain** after name-mode resolved only 1 of 10 |
| Practo paid-listing check | `apify/rag-web-browser` (site-scoped search) | All clinics |
| Website team/about/contact crawl | `apify/website-content-crawler` | All domains, 48 pages (all homepages + linked pages) |
| LinkedIn person (direct URL) | `harvestapi/linkedin-profile-scraper` | 2 of 10 — the only two where GBP surfaced a usable direct URL |
| LinkedIn person (name search) | **Not run** | Not prioritised against the daily free-tier cap |

**Actor-health preflight:** all confirmed live and non-deprecated before spending. `compass/crawler-google-places`
90% · `apify/facebook-ads-scraper` 99.2% · `scrapesage/google-ads-transparency-scraper` 99.4% ·
`apify/instagram-profile-scraper` 99.4% · `apify/website-content-crawler` 96.6%. No fallback substitution needed.

**Six-point verification loop applied after every call** — an Apify `SUCCEEDED` means "the code exited," not
"the data is real": ① coverage vs. inputs ② error/summary key-value records read (e.g. the Google Ads `STATE`
record, which is how the name-mode miss was caught) ③ full `statusMessage` read on every run ④ field
completeness with quirk awareness ⑤ cross-source corroboration (IG counts matched the supplied brief almost
exactly for all 10 — a trust signal on both) ⑥ manual tie-break on load-bearing/reversing claims, applied
twice (Meta keyword false positives; Ara's advertiser-name mismatch).

**Tool-health notes carried forward:** never trust a bare Meta keyword search — resolve a real FB Page URL
first (GBP contact enrichment is the cheapest source); `search_type=page` is a weak fallback, not a substitute.
Google Ads `advertisers` mode by brand name is unreliable (missed 9/10); **`ads` mode by domain is far more
reliable**, and `domains` input is not accepted in `advertisers` mode. **`maxCrawlPages` is a global cap
across all `startUrls`, not per-site.** No dedicated Practo/JustDial actor exists in the Store — the
`rag-web-browser` site-scoped search remains the best available method and remains inconsistent.

**ScrapeGraph budget (batch 11–15 pass):** started 500 credits, ended **255 remaining (245 used)**, including
several failed extractions — Google Ads Transparency failed uniformly, two guessed Practo URLs failed, and one
~76k-token Meta Ad Library extraction on Project Skin returned nothing before a targeted screenshot retry
succeeded. The `crawl` job (limit 1 for the whole plan) was **not used.**

**Review-quote policy:** Google reviews contain real patients' names and medical details. Quotes throughout
are **minimised deliberately** — they carry only what establishes the *business* finding. Reviewer names are
omitted; clinical specifics are reduced to the minimum needed to convey severity. Serious allegations are
stated **as allegations** and surfaced prominently rather than smoothed into surrounding prose.

**Screenshot inventory — `mystery-shop-b7/` (10 files, 12 clinics):**
`dr-priya.png` · `akera-health.png` · `project-skin.png` · `dermatonik-1.png` · `dermatonik-2.png` ·
`vida-skin-n-hair.png` · `gejjes-marvella.png` · `ara-skin.png` · `vital-skin-1.png` · `vital-skin-2.png` ·
`theory-of-skin.png` · `krity-360-wa.png`. **Missing: Derma Solutions, Haircosmos International.**
