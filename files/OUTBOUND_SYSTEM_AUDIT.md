# Valence Ops — Outbound System Audit & Redesign

> ## 📕 HISTORICAL RECORD — resolved 2026-08-13. Do not draft or decide from this file.
> Everything here that became a rule now lives in `wedge-signal-entry.md`, `files/OUTBOUND_MEMORY.md`
> and `personalized-outbound-v2.md`. Read it to understand *why* a rule exists, never to find out
> what the rule is.
>
> **Its five "top fixes by impact-per-hour," each costed at 5–15 minutes, sat unapplied for 22 days.**
> Three were still live contradictions on 2026-08-13: rev-share in the drafting skill, the 2-touch
> cap in the drafting skill, and the mystery-shop Go/No-Go still blocking every send. All are now
> fixed. Several statements below are also simply out of date — "zero sends," "no send log,"
> "Tue–Thu 11am–4pm," "six speed-to-lead tests," and the ICP-score discussion have all moved on.

**Date:** 22 Jul 2026 · **Goal:** first paying clinic · **Files audited:** 16 project files + `personalized-outbound` skill + master business context (extracted from valenceops_context_1)

---

## VERDICT

**No — the system as it stands cannot produce the first client, because it does not produce sends.**

Single biggest blocker: **the pipeline terminates at research, not at outreach.** Twenty full clinic audits exist (15–30 hours of work at 45–90 min each). Zero drafted Day 0 DMs exist. Zero logged sends exist. And — the fatal detail — **none of the 20 audits captured the one field the Day 0 DM template requires**: the specific, dated, unanswered comment/post hook (Checklist Section 1). Every audit filled in ICP scores, founder bios, ad counts, and review themes; every audit left the hook field empty. The machine is optimized to produce dossiers about clinics, not messages to clinics.

Message craft (the skill's templates) is genuinely top-decile. The verdict that craft is not the bottleneck is confirmed. The bottleneck is that nothing gets sent.

---

## SCORECARD

| Asset | Sequence stage | Craft /10 | Fact-discipline | Offer /10 |
|---|---|---|---|---|
| Skill — Day 0 DM template + worked example | Day 0 | **9** | PASS (checklist-bound) | — |
| Skill — video script framework (4 beats) | Post-reply | **8** | PASS | — |
| Skill — WhatsApp bridge line | Post-reply | **9** | PASS | — |
| Skill — pilot offer template | Offer | **8** | PASS | **7** — see violations: rev-share option banned; no completion mechanism |
| Skill — silence bump | Touch 2 | **8** | PASS | — but sequence caps at 2 touches (contradicts settled verdict #4) |
| Skill — decline response | Decline | **9** | PASS | — |
| elective-clinics-sales1 — sample cold intro email | Day 0 (email) | **3** | **FAIL** — fabricated case study ("Clinic XYZ saw 20% rise") | — |
| elective-clinics-sales1 — objection library | Reply handling | **5** | n/a | — wrong stage (discovery-call, not DM), wrong voice (consultant-generic: "ROI," "CRM," "our platform") |
| clinic-audit-checklist.md | Pre-send | good doc, wrong gate | n/a | — mystery-shop is a hard Go/No-Go gate (contradicts settled verdict #3) |
| Clinic Research Sources.md | Pre-send | good doc, over-budget | n/a | — 12–15 min "default" + mystery shop exceeds the 10-min ceiling |
| 20 clinic research summaries (OUTREACH_document + outreach_-2) | Research | — | **PARTIAL FAIL** — speculative claims written as findings; hook field empty in 20/20 | — |
| valence-ops-clinic-intelligence-os.md | Memory layer | strong | PASS | — no outcome/send tracking at all; ICP scoring is inflated (see below) |
| Clinics-Revenue-OS.md | Internal delivery map | fine internally | — | never show a prospect: it's wall-to-wall "leads / funnel / lead scoring" vocabulary |
| Master business context (pdf/zip) | Offer architecture | strong | PASS | ₹5k audit + ₹20k setup + ₹40k retainer is a **paid** cold offer — contradicts settled verdict #5 (free pilot). See violations. |

**Stages with NO asset at all:** reply-handling for the six standard replies (built below, Part 2 §10) · pilot-completion mechanism (built below) · touches 3–4 (didn't exist — sequence stopped at 2) · founder-profile standard (built below) · send log / outcome tracking (built below, Part 3).

---

## CRITICAL VIOLATIONS (things that torch trust with this buyer)

1. **Fabricated case study in the sample cold email** (elective-clinics-sales1): *"Clinic XYZ in Bangalore saw a 20% rise in revenue in 6 months."* Valence Ops has zero clients. This is the exact script the agency-burned buyer is trained to detect, and it's a skill anti-pattern ("Fabricating a portfolio, case study, or result that doesn't exist yet"). Rewrite of the weakest line: replace the invented case study + "15 minutes next week?" with a verified fact + tiny ask — *"I sent your front desk a WhatsApp enquiry Tuesday 2:10pm and got the first reply Thursday morning — want me to send the 2-line breakdown of what I think is happening?"*
2. **Rev-share language inside the live skill.** Risk Reversal Standard says "Free **or performance/revenue-share**" and sequence step A3 says "free/rev-share." Settled verdict #5 bans rev-share at cold stage. Mechanical fix: strike both; replace with "free + named guarantee + completion agreement."
3. **Mystery shop as a Day 0 gate.** Checklist Go/No-Go: *"I have not skipped the mystery shop… don't send yet."* This makes every send wait 24–72h on a reply that may never come. Contradicts settled verdict #3. Delete the line; mystery shop becomes a background/post-reply asset (design below).
4. **Two-touch parking hard-coded in the skill.** "If still silent +4–5 days: stop, no third message" + anti-pattern "A third follow-up message after two unanswered touches." Contradicts settled verdict #4 (4 touches, 2 channels). Fix below.
5. **Midnight mystery shops manufacture false hooks.** 9 of the shops were sent between 9 PM and 1 AM ("12:40 AM," "11:33 PM," "12 AM"). A clinic replying at 9:20 the next morning to a midnight message is *behaving normally.* Leading a DM with that "gap" hands the doctor an instant, correct rebuttal — and reads as a gotcha. Only business-hours no-replies (Vtiara-style 2 PM tests) are undeniable. Several logged "gaps" are not usable hooks.
6. **Speculative claims written as findings** in the research summaries: "Website… likely generates organic enquiries," "High inbound volume expected," "DNA likely has thousands of past enquiries." Fine as internal hypotheses; a CRITICAL violation the moment any reaches a DM. None have yet — because no DMs exist — but the summaries don't separate verified from assumed, so drafting from them today would launder assumptions into "facts."
7. **ICP scoring is not a filter.** 20/20 clinics score 7.5–10. Two clinics scored 9+ with **no Instagram at all** (Dr. Utkarsha's, Dr. Keshav's) — undeliverable on the primary channel. Skinology (1-min human reply + qualifying question — the best front door in the dataset) still sits at 8.8 and on the priority list, when the speed-to-lead wedge is dead for them. A score where everyone passes is decoration.
8. **Offer contradiction between the master context and the settled strategy.** The master context's founding offer is paid at cold stage (₹5,000 audit → ₹20,000 setup → ₹40,000/mo). The settled verdict is free time-boxed pilot + named guarantee. Flagged per the rules; resolution (not a re-litigation): the free pilot is the *cold conversion* instrument for client #1; the ₹5k/₹20k/₹40k structure is the *post-pilot commercial path* the pilot converts into. The refundable-₹5k idea from the paid path is recycled below as the pilot-completion mechanism.
9. **"Guaranteed numbers":** none found in outbound-facing assets — clean. The reply guarantee ("zero engaged responses in 14 days → refund") is a named guarantee, not a patient-count promise — compliant. Keep it that way.

---

## THINKING CORRECTIONS

1. **"Research depth = credibility"** → Only the one verified fact ever reaches the prospect; the other 40–80 minutes are invisible to them. Credibility is the *sharpness* of one fact, not the thickness of the dossier. Research beyond the hook happens after a reply signal.
2. **"Finish the audit before contact"** → The audits produced everything *except* the hook. Invert the priority: hunt the single screenshot-able fact first (≤10 min); everything else is post-reply.
3. **"Mystery shop first — it's the strongest data point"** → It's the strongest *post-reply* asset ("I messaged Tuesday 2pm, first reply Thursday" lands hardest in the video/WhatsApp stage). Pre-send, it's a 24–72h blocking dependency with a false-positive problem at midnight. Run it in parallel, business hours only, never as a gate.
4. **"High ICP score = good target"** → The score measures how impressive the clinic is, not how winnable it is. Fast responders and no-IG clinics are low-probability regardless of prestige. Filter on reachability + verified leak evidence, not on how good their business looks.
5. **"Biggest founder brands first" (DNA 1.5M followers = priority)** → Mega-brands have DM gatekeepers, existing agencies (Karishma's ads run via Growthmax), and the founder never reads cold DMs. Client #1 statistically comes from founder-run mid-tier clinics (1k–30k followers) where the doctor still opens Instagram. Mega-brands go on the post-Case-Study-#1 list.
6. **"Two touches then park is respectful"** → In a feed saturated with agency spam, two touches ≈ never seen. Four touches across two channels, each with a new fact, is persistence with substance — the settled verdict. Parking after two was polish over probability.
7. **"Sell the system" (10-stage Patient Revenue OS)** → The OS map is delivery architecture. Cold outbound sells exactly one thing: the patients who already messaged and went quiet. One wedge, one outcome, one ask.
8. **"20/500 clinics logged" as progress** → Audits logged is a vanity metric; it measures input. The only progress metrics before client #1 are touches sent and replies received. The 500-clinic database is a Phase 2 asset being built in Phase 0.

---

## THROUGHPUT MATH

- **Current documented throughput: 0 Day 0 sends/week.** Not derivable whether any DMs were sent outside the repo — no send log, no drafts, no outcomes recorded anywhere. What *is* derivable: ~20 audits at 45–90 min each = **15–30 hours of research producing zero recorded touches.**
- **Target:** 25–40 Day 0 sends/week at ≤10 min research per send = **4.2–6.7 hrs/week** of research+drafting, plus ~2 hrs sending/logging, plus ~2 hrs reply handling. Total ≈ **8–11 hrs/week** — less than the time the audit habit was already consuming.
- **What the redesign changes:** kill-filter (≤2 min) removes ~30–40% of prospects before any research minutes; light checklist v2 caps research at 10 min; mystery shop unblocked from Day 0; drafting batched through the skill (5 min/DM with a filled v2 checklist); the 20 existing audits become a **free head start** — a 10-min hook-harvest pass per sendable clinic converts sunk research into this week's first batch (~12 clinics are sendable; see build list).

---

## THE REDESIGNED WEEKLY OPERATING CADENCE

Quality is held by the checklist and the skill, not by time spent. Perfectionism is rejected by design: every mode has a hard timebox, and a send blocked by "could be better" ships anyway if it passes the v2 checklist.

| Day | Mode | Time | Output |
|---|---|---|---|
| Mon | **Prospecting + kill-filter batch** | 60 min | 20–25 raw names → 12–15 qualified (≤2 min each, §8 filter) |
| Mon | **Reply-handling window #1** | 30 min | All open replies answered same-day using §10 frameworks |
| Tue | **Light-research batch** | 90 min | 10–12 filled v2 checklists (≤10 min each, §9) — stop at 10 min even if the hook is only "good," not "perfect" |
| Tue | *(background)* Fire business-hours mystery shops at this week's targets — 2 min each, never blocks anything | 15 min | Shops in flight; results harvested post-reply |
| Wed | **Drafting batch** (via `personalized-outbound` skill) | 60 min | 10–12 Day 0 DMs drafted, ≤5 min each; self-check only — no second polish pass |
| Wed | **Send batch #1** + log | 45 min | 10–12 Day 0 sends, each logged in SEND_LOG within 2 min |
| Thu | **Reply-handling window #2** | 45 min | Replies handled; positive replies → bridge → offer same day |
| Thu | **Touch batch** (touches 2–4 for prior cohorts) | 45 min | Bumps + channel-2 touches per §sequence, logged |
| Fri | **Send batch #2** + log | 45 min | Remaining 8–15 Day 0 sends → weekly total lands 25–40 |
| Fri | **Reply-handling window #3** | 30 min | Close the week with zero unanswered replies |
| Sat/Sun | **Weekly review ritual** | 30 min fixed | §Part 3 agenda: aggregates, kill/double, one experiment, memory update, tripwire count |

Rules: replies always outrank new sends (a warm reply decays in hours; a cold prospect keeps). No mode bleeds into another — when the timer ends, the batch ships as-is.

**The 4-touch / 2-channel sequence (replaces the skill's 2-touch cap):**
- **T1 (Day 0):** IG DM — hook + identity + tiny ask.
- **T2 (Day 2–3):** IG DM bump — one NEW fact (never "just bumping"), or the category video.
- **T3 (Day 5–7):** WhatsApp/front-desk number, only where publicly listed — *"Tried you on Instagram — I'm Tilak, noticed [same hook, restated fresh]. Easier here? Happy to send the 2-line breakdown."* New channel, same single ask.
- **T4 (Day 10–12):** WhatsApp — the strongest remaining fact (by now the business-hours mystery-shop result is usually in: first-hand, dated, undeniable). Then park 60–90 days / until Case Study #1.
- Decline at any touch → skill's decline response, park, log.

---

## §8 PROSPECT KILL-FILTER (≤2 minutes, BEFORE any research)

Open IG profile + Meta Ad Library side by side. Any single ❌ = kill, log one line, next name.

1. **Reachable?** Active IG account OR publicly listed WhatsApp/front-desk number. No channel = kill (this alone would have killed 2 of the 20 audits).
2. **Alive?** Posted within 60 days. Dead IG + no ads = kill.
3. **Volume signal?** At least ONE of: active/past Meta or Google ads · 1k+ IG followers with comment activity · 100+ Google reviews · Practo listing with recent activity. No inbound volume = nothing to reactivate = kill.
4. **Not solo-subscale?** Solo practitioner with <500 followers, no ads, no reviews momentum = kill (real pain, no pipeline to run on — mirrors the master-context ICP floor of ~20 leads/mo).
5. **Front door not already excellent?** If a <5-min human reply with a qualifying question is already known (e.g., Skinology) → do NOT kill outright, but **switch wedge** to quote-follow-up/no-show recovery, or park if no evidence for that wedge. Speed-to-lead hooks are dead here.
6. **No visible happy agency lock-in?** "Powered by [agency]" + polished automation + active management = park.

Pass 4+ with no ❌ → goes to the light-research batch.

---

## §9 LIGHT-RESEARCH CHECKLIST v2 (≤10 min, Day 0 fields ONLY)

Everything else from checklist v1 moves to POST-REPLY. Fill only:

```
CLINIC: ___  IG: ___  AREA: ___  SUBTYPE: skin/derm | cosmo | hair | dental
FOUNDER NAME (if visible): ___          FOUNDER-RUN? Y/N/unclear (30-sec read)

THE HOOK (mandatory — no hook, no send):
  One dated, screenshot-able, public fact. In priority order, take the FIRST found:
  1. Unanswered/late-answered price-location-booking comment (post link + exact text + date)
  2. Ads running ≥X weeks (Ad Library) + any visible reply lag on IG
  3. Most recent Google review ≥3 months old despite active treatments
  4. Other verified public fact a stranger couldn't write
  HOOK: ___________________________  SOURCE LINK: ___________

WEDGE (pick one): dead-enquiry reactivation | no-show/booking recovery | review revival
WHATSAPP/FRONT-DESK NUMBER PUBLIC? Y/N (enables touches 3–4)
KILL-SWITCH NOTE (anything that says pause): ___
```

**Moved to post-reply:** mystery shop write-up, full review mining, competitive snapshot, website view-source, Practo Q&A, tone-register notes, founder LinkedIn. **Moved to background:** the mystery shop itself — fire it (business hours only, Tue–Thu 11am–4pm) the same week, harvest the result at touch 3–4 or in the video.

---

## §10 REPLY-HANDLING LAYER (the missing stage — six frameworks)

**1. "How much?" / "What are your charges?"**
- *Goal:* don't price a cold DM; convert price-curiosity into the pilot frame.
- *Template:* "For the first pass — nothing. I want to run it on the enquiries already sitting in your DMs/WhatsApp, 2–3 weeks, and if it doesn't bring back real bookings you owe nothing and I'll show you exactly where it stalled. Easier to walk you through on WhatsApp — what's a good number?"
- *Next:* bridge → offer → call. Log outcome.

**2. "We already have someone / an agency."**
- *Goal:* don't compete with the agency; occupy the gap agencies don't touch.
- *Template:* "Makes sense — and I'm not touching ads or content, that's their lane. This is only the enquiries that already came in and went quiet — the part nobody's usually assigned to. If your agency covers that too, genuinely all good."
- *Next:* if any opening → bridge to WhatsApp; if firm → decline response, park 60–90 days, log.

**3. "Send me a proposal / send details."**
- *Goal:* a PDF to a cold prospect = death. Trade the "proposal" for a 5-line WhatsApp breakdown.
- *Template:* "Will do — it's short, 5 lines, specific to what I saw on your page, not a brochure. Easier on WhatsApp so you can read it between patients — what's a good number?"
- *Next:* send the breakdown as text (hook fact → what it costs them in plain terms → the free 2–3 week pilot → guarantee → single question). Log.

**4. "We tried this before, got burned."**
- *Goal:* validate, differentiate on risk structure — never on skill claims.
- *Template:* "Honestly the most common thing I hear from doctors here — usually someone promised a patient count and delivered junk. That's exactly why this is free, on your existing enquiries, with it in writing that if nothing real comes back you owe nothing and I'll tell you why. No numbers promised — I don't do that."
- *Next:* offer the breakdown; if warm → bridge. This is also where the completion agreement (below) reads as protection *for them*. Log.

**5. "Not now / maybe later / after Diwali."**
- *Goal:* accept cleanly, earn the future slot, create one dated re-entry.
- *Template:* "No problem at all. One thing — the enquiries sitting in your inbox from the last couple of months lose value every week they sit. I'll check back in [named month]; if it's useful sooner, just reply here."
- *Next:* log with a revisit date in SEND_LOG notes; no further touches until then.

**6. Enthusiastic-but-vague ("sounds great!", "interesting, tell me more").**
- *Goal:* enthusiasm ≠ commitment; convert to ONE concrete next step immediately.
- *Template:* "Glad it landed. Fastest way to make this real: mind if I move this to WhatsApp and send the 5-line breakdown of what I'd do first on your existing enquiries? What's a good number?"
- *Next:* bridge same day — vague enthusiasm decays in 48h. If number given → breakdown → offer → call/coffee ask. Log.

---

## PILOT-COMPLETION MECHANISM (settled verdict #5 — designed)

Problem: free pilots get ghosted mid-way; nothing currently protects completion. Design — **the Pilot Completion Agreement**, one page, signed (or WhatsApp-confirmed line by line) before launch:

1. **Response-SLA clause:** clinic names ONE point of contact who replies to routed patient responses within 4 business hours. *"The system only works if revived patients hear back — that's the one thing I need from your side."*
2. **Pre-booked finish line:** the 20-minute end-of-pilot review call is scheduled **before** the pilot starts, in the calendar, at launch. Ghosting now means cancelling a named meeting, not letting silence drift.
3. **The stop-clause (protection framing):** "If 3 routed patient replies go unanswered past 48h, the pilot pauses and we talk — I won't burn your revived patients' goodwill." Reads as Valence Ops protecting the clinic's reputation; functions as a completion enforcement tripwire.
4. **Escalation variant only for re-engagements or prior ghosts:** ₹2,000 token deposit, refunded in full at the review call (adapted from the master context's refundable ₹5k audit fee). Not used on first cold pilots — friction beats ghost-risk there.

This preserves "risk fully on Valence Ops" (no money at stake by default) while making completion the path of least resistance.

---

## §11 FOUNDER-PROFILE CHECKLIST (Tilak's IG + LinkedIn, before the next batch)

The prospect's first move after a cold DM is opening the sender's profile. It must answer "real person, works with clinics here, not an agency page" in 5 seconds.

- [ ] **Personal account, real name + face.** Not a Valence Ops brand page (skill hard rule). Bio line pattern: *"Helping Bangalore skin & dental clinics bring back the patients who enquired and went quiet"* — patients vocabulary, no "AI," no "growth/leads/funnel."
- [ ] **Bangalore visibly anchored** — location in bio, at least one recognizably local post.
- [ ] **3–6 substance posts** before the batch: one pattern observation from the 20 audits (anonymized, no clinic named), one "how I check a clinic's front door in 10 minutes," one honest build-in-public note. No fabricated wins, no client claims.
- [ ] **Zero agency-smell:** no stock graphics, no "DM 'GROWTH'" CTAs, no follower-buying, no motivational carousels.
- [ ] **Follows/engages** the 20 audited clinics + Bangalore derm/dental community — makes the DM arrive from a familiar-adjacent account.
- [ ] **Highlights:** one "What I do" (30-sec talking head, same 4-beat structure as the category video) — doubles as the pattern video for prospects who check the profile before replying.
- [ ] **LinkedIn mirrors it:** same photo/name/positioning; headline in patient-vocabulary; the section_8 hook patterns (number/provocation/confession) feed future posts — Legacy-tier and operator-led prospects (Ishmeet Singh, Navin Koushik, Rohit Reddy) check LinkedIn first.
- [ ] **WhatsApp Business profile** set with the same name/photo — touches 3–4 land there.

---

## MISSING-ASSET BUILD LIST (ordered by what unblocks sends fastest)

| # | Asset | Effort | Unblocks |
|---|---|---|---|
| 1 | Adopt kill-filter + v2 checklist (both written above — copy into workflow) | 30 min | Every future send |
| 2 | **Hook-harvest pass on the ~12 sendable audited clinics** (Aura Cutisurg, Clinic Next Face, Dr. Swetha's, Dr. Juvita, Vtiara, Iridescent, Dr. Tina's, Cozmo Blis, Ministry of Skin, Dr. Dixit, Dr. Ritika, AvatarLuxe) — 10 min each to find the missing comment/date hook; existing research supplies everything else | 2 hrs | **First 12 sends this week** — converts 15–30 hrs of sunk research into batch #1 |
| 3 | Skill file edits: strike rev-share (2 places), replace 2-touch cap with 4-touch/2-channel branch, delete mystery-shop Go/No-Go from checklist v1, add business-hours-only mystery-shop rule | 30 min | Removes the 3 contradictions from the live drafting engine |
| 4 | Internalize the six reply frameworks (§10) | 1 hr | Every reply from batch #1 |
| 5 | Founder IG/LinkedIn fix per §11 | 2–3 hrs | Reply rate on all batches (profile is checked before replying) |
| 6 | Pilot Completion Agreement one-pager | 1 hr | Pilot conversion + completion |
| 7 | Two category pattern videos (skin/derm + hair transplant; dental waits) — 60–90s, 4-beat skill structure | 2–3 hrs | Touch 2 upgrade + post-reply asset; NOT a send blocker |
| 8 | SEND_LOG / memory files (created in this repo) | done | The compounding layer |

Note on the ~12: Dr. Utkarsha's and Dr. Keshav's are killed (no IG — unreachable on primary channel); Skinology parked-or-rewedged (front door already excellent); The Glow Clinic re-wedged (5-min WA reply — speed hook dead; quote-follow-up angle only); DNA/Karishma/Anew/Dr. Sculpt moved to the post-Case-Study mega-brand list (gatekeeper problem).

---

## TOP 5 FIXES BY IMPACT-PER-HOUR (mechanical only)

1. **Delete the mystery-shop Go/No-Go line** from clinic-audit-checklist.md — 5 min — unblocks every send permanently.
2. **Strike "rev-share" from the skill** (Risk Reversal Standard + step A3) — 5 min — removes a banned offer from the live drafting engine.
3. **Replace the skill's 2-touch stop with the 4-touch/2-channel branch** — 15 min — roughly doubles touches per prospect at zero research cost.
4. **Write the business-hours-only rule into the mystery-shop instructions** (Tue–Thu, 11am–4pm) — 5 min — stops manufacturing rebuttable midnight "gaps."
5. **Run the hook-harvest pass on the 12 sendable clinics** — 2 hrs — produces the entire first send batch from already-sunk research.

---

## MEMORY FILES

Created alongside this report, populated from the files, ready for the first update cycle:
- `OUTBOUND_MEMORY.md` — hooks by subtype (hypothesis-ranked; no send data exists yet), banned phrases, tone rules, offer framing, decisions log, **the tripwire**.
- `SEND_LOG.csv` — schema live, empty (zero sends derivable from files — the log starts at true zero).
- `LEARNINGS_LOG.md` — seeded with what the 20 audits actually taught, dated.

Update ritual and weekly review agenda are written into OUTBOUND_MEMORY.md so they travel with the file.
