# OUTBOUND_MEMORY.md — Valence Ops Living Outbound Memory
**Status:** v2 · seeded 22 Jul 2026 from the 20-clinic audit dataset · revised 13 Aug 2026 (folder self-audit).
**Evidence state:** 6 sends logged, all no-reply · ~40–65 actual touches · 2 replies · **0 calls held · 0 pilots.**
Everything in §2 is still **hypothesis-ranked** — 6 logged sends cannot rank anything. Re-rank only from real outcome data, and note that at this volume no copy-level ranking is statistically possible at all (see §2 header).

---

## 1 · TRIPWIRE (non-negotiable — read at every weekly review)

> **If 100 touches OR 45 days pass from the first logged send with ZERO pilot agreements, the clinics-only bet must be loudly re-examined.** Adjacent verticals (coaching/study-abroad consultancies, real estate) re-enter the plan at that point. This is not a suggestion to feel bad about — it is a scheduled decision.

**⚠️ Counter as of 2026-08-13 — never filled in once since the tripwire was installed on 2026-07-22.**
**The touch number below was revised upward the same day, after reading Notion instead of this repo.**

| | |
|---|---|
| First send (Day 0) | **≈2026-07-25** — Cozmo Blis touches 1–3 were reported retroactively with no dates; 2026-07-28 is the first *dated* send. 07-25 used as the conservative Day 0. |
| **Days elapsed** | **≈19 / 45** |
| Touches in `SEND_LOG.csv` | 6 — *frozen fragment, not the ledger* |
| **Touches actually sent** | **≈70–90 / 100**, counted from Notion Batch 1 + Batch 2 `Status` and `DM status` fields on 2026-08-13. A first-pass estimate of 40–65 was made from repo files alone and was too low. |
| Replies | 2 (Sapphire, Aesthetica Veda) |
| Calls held | **0** |
| Pilot agreements | **0** |

**How that 70–90 was derived, so it can be checked:** most Batch-1 rows carry a "Follow up 4" or "Follow up 5" marker across multiple named POCs at the same clinic — Clinic Next Face alone reads DM-3 to Praharsh + DM-2 to Sharanya + DM-3 to Karan Singh + Email-2 with doc, roughly ten touches. Batch 2 adds ~9 IG DM-1 sends. Mystery shops are excluded — they are tests, not touches.

> ### 🔴 The tripwire is close to firing, and may already have fired.
> At ~70–90 of 100 touches and ~19 of 45 days with **zero pilots**, the touch counter — not the calendar — is the binding constraint, and it is 70–90% spent. This is a **scheduled decision**, not a mood: at 100 touches with zero pilot agreements, the clinics-only bet gets loudly re-examined and adjacent verticals re-enter the plan.
>
> **Do this before the next batch ships, not after:** count the touches properly from Notion rather than estimating, fix an honest Day 0, and write the number here. If the count lands over 100, the tripwire has fired and the re-examination is owed. If it lands at 80, there are twenty touches left before it does — which is roughly one batch, so plan the next batch knowing it is the last one before the decision.
>
> `ONE-PAGER-AUDIT-AND-TEST-PLAN.md` §7 called this exactly: *"the tripwire will fire during this test. Plan for that now rather than discovering it."*

**Second tripwire (added 2026-08-04):** if 3 clinics reach the operations call and none reach a pilot, the problem is the offer or the call — stop tuning DMs and rebuild the call. Currently at **0 of 3** — no clinic has reached an operations call yet.

---

## 2 · Current best-performing hooks by clinic subtype
*(**HYPOTHESIS ranking — derived from audit patterns, not outcomes.** Nothing below has ever been validated by a reply.)*

> **Standing caveat added 2026-08-13.** At 40–65 lifetime touches, a hook-level performance ranking is not achievable — separating an 8% base rate from 16% needs several hundred sends per arm (`ONE-PAGER-AUDIT-AND-TEST-PLAN.md` §4). Treat this section as a **prompt list for what to look for**, never as a claim about what works. The only ranking signal available at this volume is a hook that draws an explicit reaction, and the only metric worth optimising is **calls held** — currently 0.
>
> **Every hook must pass the rebuttal test before it ships** (`wedge-signal-entry.md` §0.1): write the one sentence the doctor says back. "You run 25 ads" → *"And?"* → dead. This kills most of what the dossiers surface. That is the point.

**Skin/Derm/Cosmetology**
1. Unanswered or 2+ day-late comment asking price/location/booking, with post link + date (rarest to find, hardest to rebut).
2. Ads actively running (Ad Library, with duration) + any visible reply lag — "paying for enquiries that go quiet" framing.
3. Stale Google review date (≥3 months) at an otherwise active clinic → review-revival wedge.
4. Business-hours mystery-shop no-reply (first-hand, dated) — **post-reply/touch-3+ asset, not Day 0**.

**Hair transplant**
1. Ads running + long decision cycle framing ("the people who asked for a transplant quote and went quiet") — audit pattern: hair is the most comparison-shopped vertical.
2. Unanswered comment hook (same as skin).

**Dental**
1. Practo/Google activity + no responsive channel — thin IG presence is common; verify reachability first (2 of 2 dental audits were IG-unreachable).

**Cross-subtype pattern bank (from the 20 audits — usable as background, never as unverified claims to a specific clinic):**
- 18/20: acquisition solved, conversion leaking (no-show recovery, quote follow-up, dormant reactivation missing).
- Late-night enquiries die everywhere — but **only business-hours tests produce usable hooks**.
- Ad spend ≠ operational maturity (28-ad clinics leak like 0-ad clinics).
- WhatsApp automation, where present, stops at the greeting — "upgrade the depth" pitch, not "install from scratch."
- IG DM handling lags WhatsApp handling almost everywhere → the IG→WhatsApp handoff is a nameable gap.

---

## 3 · Banned phrases & moves (violations = fix before send, no exceptions)
- **Vocabulary:** leads, funnel, pipeline, conversion, ROI, lead generation, RevOps, infrastructure, "scale your practice", "growth" — use *patients, enquiries, consult, booking, follow-up, walk-in*.
- **"AI" as a lead** — outcomes first; AI only if they ask how it works.
- **Any guaranteed patient/lead number, ever.** ("X patients in 30 days" = the scam script this market detects.)
- **Rev-share at cold stage** — banned. Free pilot + named guarantee + completion agreement only.
- Superlatives (best/#1/leading/guaranteed), generic compliments ("love your page!"), stacked asks, greeting filler ("hope you're well").
- Fabricated case studies, portfolios, or results — none exist yet; say so if asked.
- Hinglish/slang initiated by us (mirror only after they set the register).
- Presumptive psychology said out loud ("clinics like yours get burned by agencies") — shapes tone, never appears in copy.
- Third IG-DM-only follow-up — touch 3+ moves to WhatsApp where public.
- Cold "proposal" PDFs — always the 5-line WhatsApp breakdown instead.
- **Enquiries sent outside the clinic's own published Google hours, as hooks.** *(Revised 2026-08-13 — replaces the flat "midnight" ban and the "Tue–Thu 11am–4pm" window, both retired. The rule is now published-hours admissibility: see `wedge-signal-entry.md` §2.0. It kills midnight permanently while opening Saturday, Sunday and weekday evenings — and it also kills some existing "business-hours no reply" findings that landed on split-shift closed time. Re-check any such finding before shipping it.)*
- **Identical text to more than one person at the same clinic.** The same message went to all three Glow Clinic POCs on 28/7. In a market where they compare notes, that is a self-inflicted burn.
- **Asking a doctor for a call as the *first* ask.** 25 one-pagers → 2 replies → 0 calls. A call is the most expensive thing you can ask of a clinician. Lead with something that costs them nothing — a number they can message themselves, or a ten-minute drop-in.
- **Any claim of a "gap" the doctor can rebut in one sentence.** See the rebuttal test, §2.
- **Any ad claim not traced to a creative someone has actually opened and read.** *(Added 2026-08-23.)* An advertiser record proves that money moved; it does not tell you what the ad said, when that specific creative started, or what number is printed on it. `new_leads_1/gads_detail/*.json` stores creative IDs and image URLs only — **no copy** — and a resolved Facebook Page with `total: 0` means zero ads ever, not "unchecked." Batch 9's v2 Day-0 drafts invented a Maya "Fotona / Book now ad running since the 10th" and a Regenique "exosome hair-fall ad live since the 1st with the number printed on it" against pages that have never run an ad. Neither was caught by any existing rule. **Advertiser entity must also match the clinic** — `REGENIQUE MULTISPECIALTY CENTER` and `Pure Dermacare` are the standing examples.

## 4 · Tone rules
*Renamed from "Tone learnings" on 2026-08-13. Nothing in this section was ever derived from an outcome — calling them learnings made five stylistic judgments read as evidence. Split below by what they actually are.*

**Doctrine — reasoned, consistently applied, low risk if wrong:**
- Founder-to-founder, personal account, first person singular. One observation, one ask. 30–125 words.
- Competence (the fact) before warmth (the identity line) — both required; fact alone reads as surveillance.
- Decline handling: accept cleanly, zero push, no "can I ask why."

**[UNPROVEN — zero evidence either way, do not cite as fact]:**
- *"Made this after going through a few clinics here" honesty on pattern videos beats fake bespoke-ness.* **No pattern video has ever been sent.** Reasonable instinct; untested.
- *In-person offers convert unusually well with clinic owners.* **Zero in-person meetings have been held, and zero calls.** This one matters because it spread: it is cited as established fact in `personalized-outbound-v2.md`, `01 Playbooks/Sales Motion/01 Reply to Call.md`, and as the evidence base for `Outbound Process Changes 2026-08-11.md` §1.1's headline recommendation to stop asking doctors for calls. **Status as of 2026-08-13 (Tilak, direct): calls and in-person meetings are being actively pursued; nothing has landed yet.** Keep offering it — the reasoning is sound — but never write it as a proven pattern, and update this line the moment one is held.

## 5 · Offer-framing preferences (settled)

**The commercial shape [confirmed by Tilak 2026-08-13]:** **the audit and the strategy document are free. Building and running the system is paid.** Anything charged before the strategy doc has been read contradicts this.

- **Cold instrument:** free audit → free strategy/findings document. Risk 100% on Valence Ops.
- **Named guarantee (compliant pattern):** "If we don't recover [modest, specific outcome], you owe nothing and I'll show you exactly where it stalled." Never a number of patients.
- **Completion mechanism (at pilot agreement):** ① named point-of-contact + 4-business-hour reply SLA on routed patient responses; ② end-of-pilot review call booked BEFORE launch; ③ stop-clause: 3 routed replies unanswered >48h pauses the pilot.
- **④ ₹2,000 refundable token deposit — re-engagements / prior ghosts ONLY. Never a first cold clinic, and never in client-facing copy as a universal ask.** It was universal in `HOW-WE-WORK.md` and unqualified in `SALES_MOTION.md` §3/Stage 4 until 2026-08-13; both corrected.
- **Paid path:** ₹20k setup / ₹40k month, one month's notice, no lock-in. That conversation happens after the free document, never before.
- **✅ RESOLVED 2026-09-05 (Tilak) — there is no free pilot. It is a paid build plus paid operating, the same shape quoted to SkinFit.** The free 2–3 week pilot on the clinic's backlog is retired as a step; the audit and the strategy/findings document remain free, and everything from the build onward is paid. This closes the contradiction recorded below and the matching open item in `Pricing and Build Cost 2026-08-21.md` §7. The superseded entry is kept for the record:
- **~~⚠️ UNRESOLVED — the free-pilot / paid-implementation boundary.~~** `OUTBOUND_MEMORY` §5 has always specified a *free 2–3 week pilot run on the clinic's existing backlog*. Tilak's 2026-08-13 clarification is *"the audit is free, implementation is paid."* Both describe running a flow against real patients, so it is not clear whether the free pilot still exists as a step or has collapsed into the free audit + document. **Ask before quoting a price or describing step 3 to any clinic.** Flagged in `HOW-WE-WORK.md` Step 3 too.
- Sell one wedge only. Cluster expansion comes from delivery data, never from the cold message.

## 5b · What can and cannot be demonstrated [confirmed by Tilak 2026-08-13]

The demo is **built and live** — a WhatsApp automation with lead qualification and booking. The build-order item in `SALES_MOTION.md` §7 that called it unbuilt is closed.

| Capability | How it's shown |
|---|---|
| Instant reply · qualification · booking into the diary | **Live. Hand them the number and let them message it themselves.** This is the only real evidence a company with no clients has — a claim they can test is not a claim. |
| No-show recovery · quote-decay chase · dormant reactivation | **Walked through as the actual message sequences**, not demoed live. |

**Say the second row out loud rather than letting them discover it.** Those flows need real CRM state and a real missed appointment to mean anything; staging one per clinic isn't scalable and a staged no-show proves nothing. Framed honestly — *"I'm not going to fake this one for you"* — the limitation reads as method transparency, which §1 of `SALES_MOTION.md` names as the only honest differentiation available. Framed badly, a founder messages the demo asking about no-shows and finds nothing.

## 6 · Decisions made and why (append-only)
| Date | Decision | Why |
|---|---|---|
| 2026-07-22 | Tiered personalization: ≤10-min light research for Day 0; full audit only after reply signal | 45–90 min/prospect produced 20 dossiers and 0 sends; touches/week is the binding constraint |
| 2026-07-22 | Mystery shop = background/post-reply asset, business hours only, never a send gate | 24–72h blocking dependency; midnight tests produced rebuttable false "gaps" |
| 2026-07-22 | 4 touches / 2 channels (IG ×2 → WhatsApp ×2) before 60–90-day park | 2-touch parking ≈ invisible in this market; retired |
| 2026-07-22 | Rev-share struck from skill; free + guarantee + completion agreement | Settled verdict #5; free clients ghost → completion mechanism added |
| 2026-07-22 | ICP prestige scores retired as targeting tool; kill-filter (reachability + leak evidence) replaces them | 20/20 scored 7.5–10 incl. two IG-unreachable clinics — a filter everyone passes filters nothing |
| 2026-07-22 | Mega founder-brands (DNA, Karishma, Anew, Sculpt) deferred to post-Case-Study-#1 | Gatekeepers + incumbent agencies; client #1 odds are in founder-run mid-tier |
| 2026-07-22 | Tripwire installed: 100 touches / 45 days / 0 pilots → re-open verticals | Prevents the clinics-only bet from becoming unexamined sunk cost |
| 2026-08-04 | **A warm reply outranks the send quota.** With 3+ live conversations, new Day-0 sends pause until they clear Stage 2 of `SALES_MOTION.md`. The touches/week metric in §8 stays, but loses any conflict | A clinic replied asking for a company profile; nothing existed to send and the reply cooled while it was built. Sends are infinitely repeatable; a warm reply happens rarely and expires. Optimizing touches/week is what made the missing back half invisible |
| 2026-08-04 | **`08 Collateral/Audit Call Docs/02_data_intake_requirements.md` re-staged to Stage-4 kickoff**, delivered in a live 45-min setup session rather than as a document. At the findings stage the ask is exactly one item, producible in ten minutes | Raw CRM export + Meta read-only + WhatsApp history + billing counts + staff list, requested from a clinic that hasn't agreed to anything, asks strangers to be handed patient data. Good document, wrong point in the sequence |
| 2026-08-04 | **Second, earlier tripwire added alongside §1:** if 3 clinics reach the operations call and none reach a pilot, the problem is the offer or the call — stop tuning DMs and rebuild the call | The existing 100-touch/45-day tripwire only measures the cold half. It would keep pointing at outbound while the actual failure sat after the reply |
| 2026-08-04 | **`files/REPLY_LOG.csv` added** as a second ledger (reply type, hours-to-response, packet sent, call booked/held, findings sent, pilot agreed, stage lost at, their words) | `SEND_LOG.csv` has no column for anything past a reply. Four numbers matter more than reply rate: hours to first response, reply→call-held, call-held→findings-accepted, and which stage conversations die at |
| 2026-07-25 | Added `opening_archetype` column to `SEND_LOG.csv`, separate from `hook_category` | `hook_category` tracks *which fact* anchors a message; it doesn't capture *how the opening is framed*. Batch fanned across parallel subagents converged on one shared opening skeleton for 11/19 Day-0 DMs — variety needs to be deliberate and tagged. **↯ Reversed 2026-08-13, see below.** |

### Decisions taken in the folder self-audit — 2026-08-13

| Date | Decision | Why |
|---|---|---|
| 2026-08-13 | **Published-hours admissibility replaces the "Tue–Thu 11am–4pm" window and the flat midnight ban.** An enquiry is admissible as a hook if it lands inside the hours the clinic publishes on its own Google profile. *(Adopts `Outbound Process Changes 2026-08-11.md` §3.5.)* | Broader and stricter at once. Kills midnight permanently without a separate ban, opens Saturday (92% published-open — the highest slot in the dataset) and weekday evenings (Tue 6pm at 88% beats Tue 2pm at 78%), and kills tests the old window permitted: many of these clinics run split shifts, so 11–4 sat on top of the midday closure. Costs nothing — the hours are already scraped. **Was already being applied in the Sapphire brief while written nowhere canonical.** |
| 2026-08-13 | **Mystery shop cut from six tests to two: #1 Qualification and #3 Quote decay.** *(Adopts §2.2.)* Retired: #2 persistence, #4 after-hours, #5 cross-channel, #6 booking friction. | Both surviving tests fire inside a single thread from one message. #4 contradicted this file's own ban on inadmissible-hours findings — running a test whose output is banned is paying for unusable data. #5 is a retired wedge (`MEMORY.md` §2 — WhatsApp is the channel that matters). #2 takes 7–14 days and mostly tells you what quote decay tells you sooner. #6 requires actually booking, which is expensive and burns the test identity. On a ₹49,999–₹1.5L procedure, an unchased quote is the most expensive silence you can prove. |
| 2026-08-13 | **The mystery shop now opens the batch, not closes it.** Monday: ~20 shops in one sitting. Tue–Thu: research only the clinics whose threads came back interesting. *(Adopts §2.1.)* | It is the only 24–72h async dependency in the process and it was scheduled *after* the most expensive step. Batch 7 produced 25 dossiers and **0 shops**. This also structurally enforces the ≤10-min research decision of 2026-07-22 that `Process Map.md` B4 admits isn't being followed — you cannot over-research a clinic you haven't shopped. |
| 2026-08-13 | **`SEND_LOG.csv` shrunk from 11 columns to 6.** Dropped: `subtype`, `hook_category`, `opening_archetype`, `personalization_depth`, `send_time`. *(Adopts §2.5; reverses the 2026-07-25 archetype-column decision.)* Existing row data was preserved into `notes`, not discarded. | At 40–65 lifetime touches these columns collect data that cannot answer anything — which is precisely why they went unfilled. Track what is countable: touches, replies, calls held, pilots. **Opening archetypes remain a drafting discipline recorded in the draft files** — they are retired as a metric, not as a craft rule. |
| 2026-08-13 | **Every candidate hook carries a rebuttal column.** One sentence: what does the doctor say back? If a plausible one-sentence rebuttal exists, the hook doesn't ship. *(Adopts §1.3.)* | Generalises the midnight-shop lesson already paid for. Kills most of what the dossiers currently surface — that is the intent, not a side effect. |
| 2026-08-13 | **Evidence bar raised: a first-party test, OR ≥2 independent instances.** Single-incident review quotes don't ship. Review pulls must be **chronological, 25+**, reporting negatives per 100 rather than quoting one. *(Adopts §1.4.)* | The strongest batch-7 findings were patterns, not incidents. And `Findings Batch 11-15.md` caveats samples of 5–8 on Google's *relevance* sort — which makes "no complaints found" worthless as currently produced. |
| 2026-08-13 | **Founder-unidentifiable clinics are killed at Gate A**, alongside reachability. *(Adopts §2.4.)* | Project Skin got a complete dossier and was then blocked with "no founder found anywhere — no personalization possible." Dermatonik and Haircosmos have no doctor named either. A two-minute check was sitting after the most expensive step. On batch-7 evidence: 3 of 10 dossiers need never have been written. |
| 2026-08-13 | **REJECTED — the ₹7,500 paid diagnostic (Arm C of `ONE-PAGER-AUDIT-AND-TEST-PLAN.md` §5).** §5 of this file stands unchanged: the cold instrument is a free, time-boxed pilot. | Tilak's explicit call. Logged here so it is not silently re-adopted from the Aug-5 audit doc, which still describes it as a live arm. **The audit's diagnosis of the CTA problem is still accepted** — the doc gives away the audit and then asks for the audit. Fix the ask, not the price. |
| 2026-08-13 | **The faceless-firm rule is suspended for outbound one-pagers** — named human sender, plus a line inviting correction. *(Adopts `ONE-PAGER-AUDIT-AND-TEST-PLAN.md` §8.4.)* | A faceless case file from an unknown firm invites exactly one question — "who are you?" — which is the question Sapphire actually asked. The one document that broke the format, Clinic Next Face, signed off *"— Tilak, Valence Ops"* and added *"happy to be told where it's wrong"*: the most disarming register in the folder, abandoned when the format was standardised. **Reversible — flag it if you disagree.** |
| 2026-08-13 | **ICP scores may never appear in a sentence that justifies a priority or an effort level.** Metadata only. | Retired as a targeting tool on 2026-07-22, still opening the Sapphire brief three weeks later as the reason not to rush the clinic. A deprecated metric keeps steering decisions until it is deleted from the arguments, not just from the scoring step. |
| 2026-08-13 | **An audit is not complete until its accepted findings are merged into the governing docs and its rejected findings are logged here as rejected.** | Three audits, ~22 days, and the five fixes the first one costed at 5–15 minutes each were still unapplied. The folder held both the rule and its refutation, so drafting could pick up either. |
| 2026-08-14 | **The one-pager sign-off block is removed — both the name line and the correction line. The document ends on the CTA.** *(Tilak, direct. Reverses the 2026-08-13 entry below, which had itself reversed the original faceless-firm rule — this line has now flipped twice.)* Applied to `one-pager-handoff/CLAUDE.md`, `COPY_STANDARD.md` §7/§9/§10.5, and both copies of `diagnostic_doc_playbook.md`. First built without it: **Akera Health, 2026-08-14.** | The document is attached to a DM that already comes from a named person, so the name inside repeats what the reader has; and masthead + sign-off + footer put the wordmark on the page three times, against "brand exactly twice" (`BUILD_GUIDE.md` §3). **⚠️ The risk this re-opens, stated at the time and not resolved:** the 2026-08-13 rule existed because a faceless case file invites exactly one question — *"who are you?"* — which is the question Sapphire, the one real warm lead in this project's history, actually asked. **Trigger to revisit: any clinic replying to one of these asking who Valence Ops is.** |

---

## 7 · UPDATE RITUAL (after every reported batch of outcomes)

**What the founder reports per send outcome (≤2 min each — voice note or one line):**
`clinic | touch # | outcome (no-reply / reply / positive / decline) | if reply: their exact words (paste/screenshot) | anything odd`
That's it. No analysis, no self-review — the analysis happens here.

**What gets updated on receipt:**
1. Append a row to `SEND_LOG.csv` — **6 columns: `date,clinic,channel,touch_num,outcome,notes`.** No new columns without a decision entry in §6. Everything qualitative goes in `notes` as prose.
2. If it's a reply → also open a row in `REPLY_LOG.csv` and start the ≤4-business-hour clock (`SALES_MOTION.md` Stage 0).
3. Any decline pattern → note in `LEARNINGS_LOG.md`.
4. If a phrase drew a negative/spam-flavored reaction → add to §3 banned list.
5. If a line was changed mid-conversation and worked → promote it into `personalized-outbound-v2.md` and log the decision in §6.

## 8 · WEEKLY REVIEW RITUAL (20 min, fixed agenda — no strategy meetings)

*Revised 2026-08-13. The old agenda spent 10 of its 30 minutes killing and doubling hook categories on a sample that can never support the verdict, and its own rule (≥8 sends before a verdict) meant those two steps could never legally run. They are cut.*

1. **(5 min) The four numbers.** Touches sent · replies · **calls held** · pilots. Cumulative, not weekly. Derive touches from Notion status changes, not from memory. Calls held is the metric — reply rate is already at category benchmark and optimising it further changes nothing.
2. **(5 min) Where did conversations die?** Read `REPLY_LOG.csv` `stage_lost_at`. Where they die is more informative than how many die.
3. **(5 min) One experiment for next week** — exactly one variable, and only something that could plausibly *triple* the rate: format, offer, or asset type. Never a sentence or a headline. Write it in `LEARNINGS_LOG.md` before running it.
4. **(5 min) Tripwire check — out loud, both tripwires, counters written into §1.** If ≥70 touches or ≥32 days with zero pilots, pre-draft the vertical-reopen note now so day 45 isn't a surprise. **This step was skipped every week from 2026-07-22 to 2026-08-13. It is the one step that cannot be skipped.**
5. **Standing check, no timebox:** is any clinic sitting at "replied, no call booked"? If yes, nothing else on this list matters and no new sourcing happens.
