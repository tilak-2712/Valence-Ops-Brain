# Memory — Valence Ops Outbound & Sales

Adaptive, cross-session memory for this project. Read at the start of any work here; update at the end of any session that produced a real learning.

**Maintenance rule (set by Tilak, 2026-07-25):**
- New learning that **overrides** an existing entry **and has real-world proof it worked** (feedback, a reply, a send outcome) → overwrite the entry, note what changed, why, and what the evidence was.
- **Genuinely new** thing, not covered by any existing entry → append as a new entry.
- **Same as something already here** → skip it. Do not re-write duplicates.
- Anything not yet proven — a hypothesis, a stylistic judgment call, an untested proposal — gets marked **[PROVISIONAL]** and stays that way until real feedback confirms or kills it. Don't let provisional entries quietly become treated as settled.

**Added 2026-08-13 (folder self-audit):** a provisional entry that has been *used in the field* is still provisional. Field use is not evidence. Only a reply, a booked call, or a stated preference from a clinic promotes anything.

---

## 1. How Tilak wants to work with Claude

- **Ambitious, large-scope requests are normal here** — e.g. drafting a full DM+2-follow-up sequence across 19 clinics, or 5 fully-researched cold emails, in one pass. Default to executing at that scale rather than scoping down unprompted.
- **Wants pushback, not just compliance.** Repeatedly and explicitly invited disagreement before a big rewrite — and the good-faith answer each time was to actually push back on the parts of the ask that were wrong or in tension with the existing docs, not to say yes and start drafting. **Escalated 2026-08-13: this is now the standing operating contract in `CLAUDE.md`, not a per-session preference.** He asked directly for outputs that "correct me if I'm wrong, push back, and give me feedback."
- **The feedback loop is meant to be real, not performative.** He will send real DMs/emails and come back with actual outcomes. The expectation is that this measurably changes future drafts — not just gets acknowledged. See §4.
- **Wants deliverables saved to files in this folder, not just left in chat.**
- **Compressed answers.** Verdict first, tables not paragraphs, depth pushed into a file rather than into the reply.
- Prefers direct, specific critique over hedged or diplomatic phrasing — expects the same back.

## 2. Feedback — confirmed (has evidence behind it)

**Mystery-shopping and review-reading** [confirmed prior session]
Tilak mystery-shops clinics himself — never send test DMs to clinics on his behalf, leave that field as "pending — user to mystery-shop." When auditing reviews, actually read a spread of them (recent/older, positive/negative) and report patterns and quotable lines, not just the aggregate rating — the review text is what makes an outbound hook credible instead of generic.

**Apify verification** [confirmed prior session]
An Apify run reporting "Succeeded" does not mean it retrieved real, complete data — confirmed when a Google Maps contact-enrichment actor silently returned 0 items after a mid-run rate-limit. After every actor call: check coverage (items returned vs. submitted), check for a separate errors/summary key, read `statusMessage` not just `status`, spot-check field completeness, cross-corroborate, and manually verify anything that reverses a prior finding before it goes into a report as settled fact.

**Fanning identical drafting prompts across parallel subagents causes template convergence** [confirmed 2026-07-25]
4 parallel subagents with near-identical instructions drafted DMs for 19 clinics. Two independently converged on the exact same opening skeleton for 11 of 19 Day-0 DMs — different clinics, different facts, different agents. Personalization at the fact level does not prevent structural homogenization.
**Confirmed again at the document layer, 2026-08-05:** the same thing happened to all 15 one-pagers — four formulas repeating across essentially every document (two-beat antithesis headline 9/10, the same subhead 10/10, the same "what we're not saying" 10/10, the same close 10/10). Nobody caught it because each doc was written and reviewed in isolation.
**How to apply:** structural variety must be *assigned*, never assumed — a named opening archetype per clinic, a named headline/subhead/close shape per document. And review any batch of assets **side by side**, never one at a time; convergence is invisible from inside a single document.

**Don't blindly adopt an external review's specific suggestions without checking them against this project's own docs** [confirmed 2026-07-25]
A GPT-authored review of the DM batch was largely right but also (a) cited wedge-diagnosis *labels* as if they were in the sent copy — they're internal reasoning notes, never shown to the clinic — and (b) recommended a "I've been looking at something similar across a few Bangalore clinics" framing, which directly contradicts the rule that a several-clinics framing signals mass-sender and is "worse than silence." Verify a critique's examples against the actual sent text, and check its fixes against the governing docs before adopting them.

**Research-recitation vs. felt-problem articulation** [confirmed 2026-07-25 — Tilak's own critique]
Messages that report a researched fact read as competent but don't land. Messages that name the *structural consequence* of a verified fact, stated as the founder's problem rather than as a research summary, do land. The bar: first line creates instant curiosity + recognition; the full message conveys real research depth; the net effect is the problem articulated more precisely than the founder would say it themselves.
**How to apply — the resolution to the apparent conflict with the "no invented pain points, no probably" rule:** never assert an unverified fact, or an unverified emotional/behavioral state about the founder ("you're probably frustrated"). It *is* fine — and is the actual craft skill — to state the necessary logical consequence of a *verified* fact plainly ("multi-visit treatments + no tracking system → some patients drop off invisibly" is a logical certainty from the audit, not an invented pain point). Ground the observation in evidence; let the framing carry the emotional precision.
**Tilak confirmed 2026-08-13 that this resolution matches what he meant.** No longer an open question.

**Voice notes get beats, never a script** [confirmed 2026-08-13 — Tilak narrated a written script and it failed]
A voice-note script drafted to the same quality bar as written copy sounded "scripted and recited like a poem" when actually narrated. The cause was the written devices, not the wording: three balanced triads back-to-back ("the phone, the walk-ins, and the WhatsApp queue" / "the fee follow-up, the next-session scheduling, the reminders" / "the patient in front of them, the reassurance before, the check-in after"), em-dash asides, and an aphoristic closer. Rule-of-three is a *writing* rhythm — nobody improvises three balanced items in a row, so consecutive triads scan as verse when spoken. Telling the speaker to "sound conversational, not read aloud" while handing him a verbatim script is a self-cancelling instruction; anything read aloud sounds read aloud.
**How to apply:** for any voice note or video, deliver **(a)** a numbered beat sheet in fragments, **(b)** a small table of anchor facts with the spoken phrasing (numbers get rounded for speech — "under half an hour", not "29 minutes"), and **(c)** recording method: stand/walk, three takes keep the second, leave disfluencies in, never list three balanced items. A verbatim sample take may be included **only** when explicitly labelled a texture reference that must not be read. The imperfections are the asset — an obviously one-pass human recording is precisely what outperforms the polished email and deck that already got ignored. Written-copy polish is an active liability in spoken channels.

**No vague referents — ever. Hard default.** [escalated 2026-07-29]
Phrases like "what I'd check first" or "probably not a one-off" leave the reader guessing. Every phrase pointing at an action or consequence must name the concrete thing it refers to — what breakdown, what fix, what happens to the patient. Treat as always-on.
**Also applies to accusatory tone:** don't lead a finding with "I tested it, nobody did" — open with what's working, then frame the miss as a shared/structural risk, not a verdict on their team.
**Validated shape:** Ministry of Skin touch 2 v2 in `outreach-drafts-ministry-of-skin.md` — compliment on what already works → the specific miss framed as a shared risk → the concrete mechanism (patient stops looking elsewhere and waits, so a broken promise costs a committed patient, not just a reply) → CTA naming exactly what's offered. Reference bar, alongside the Glow Clinic example.

**The outbound quality bar is a standing default, not something to re-brief each session** [confirmed 2026-07-25]
Every claim traces to a specific confirmed fact (a dated mystery-shop test, a direct review quote, a confirmed ad/digital-presence finding) — never a generic "possible gaps" checklist item, never an inferred behavior stated as fact. Lead with one concrete scene, state the "so what" explicitly, avoid abstract agency/SaaS words (patient journey, engagement, nurture, revenue leakage, decision window, operational continuity, "gap" as filler), and close with a CTA that is strictly diagnostic — never a fix promised before a reply.
**Why:** Tilak said explicitly he shouldn't have to restate this each time.

**Never treat a research doc's generic "Potential/Possible Missing Layers" checklist as a confirmed finding** [confirmed 2026-07-25]
Dr. Dixit's entire wedge was built on a boilerplate line from a generic "Potential Missing Layers" section — a template list of things that *might* be missing at any clinic. It repeated across all three messages before it was caught; the wedge had to be discarded.
**How to apply:** trace every claim to a specific line in that clinic's research. If the only source is marked "Potential," "Possible," "Unknown," or "❓," it's a hypothesis to test. Also watch for facts already fully spent in a prior touch or channel — repeating them on a new channel is re-running a pitch that already went unanswered, not a fresh angle.

**Don't build a wedge on a secondary channel's slowness when the primary channel is already fast** [confirmed via repetition, 2026-07-28]
Twice led with "Instagram is slower than WhatsApp" when WhatsApp is the channel Indian clinic patients actually use to enquire and book. Comparing channel speeds isn't a wedge — it only matters if the *slow* channel is the one that matters to the business.
**How to apply:** if the primary channel is already confirmed fast *and* manual/human-staffed, the real wedge is the time cost of that manual handling — staff hand-typing the same replies to routine enquiries instead of being with the patient in the room — not a cross-channel speed contest.

**Problem framing must read as something an Indian doctor-led clinic owner would say themselves, not enterprise/SaaS English** [confirmed 2026-07-28]
"Operational efficiency," "customer experience," "closing deals," "admin tasks" must be translated into a concrete, visual, doctor-relatable scene.
**Translation check:** could this line be said, in these words, by an Indian clinic owner describing their own day? If it sounds like a consultant's slide, rewrite it as a scene.
**Validated example:** The Glow Clinic follow-up — *"that's the same person typing out that same 'hi, what treatment are you looking for' reply to every single enquiry… every minute spent on that is a minute not spent with the patient actually sitting in your clinic."*

**An audit is not finished until its findings are merged into the governing docs** [confirmed 2026-08-13 — folder self-audit]
Three high-quality audits were written (22 Jul, 5 Aug, 11 Aug). Each named specific mechanical fixes. **Almost none were applied.** The 22 Jul audit listed five fixes it costed at 5–15 minutes each; three of them — rev-share still in the drafting skill, the 2-touch cap still in the drafting skill, the mystery-shop Go/No-Go still gating the checklist — were still unfixed 22 days later. Meanwhile the audits themselves sat in the folder reading as authoritative, so the folder contained both the rule and its own refutation, and drafting could pick up either.
**Why this is the most damaging pattern here:** writing the audit *felt* like fixing the problem. It is the same failure mode `SALES_MOTION.md` §0(c) names — the work that feels productive is the work with no exit.
**How to apply:** every audit ends with two things or it isn't done — (1) accepted findings written into the governing doc, (2) rejected findings logged as **rejected, with the reason**, in `OUTBOUND_MEMORY.md` §6. An unresolved "flagged for you to overrule" proposal is a live contradiction, not a polite deferral.

**A retired metric keeps steering decisions until it is deleted, not just deprecated** [confirmed 2026-08-13]
ICP prestige scores were formally retired as a targeting tool on 2026-07-22 ("a filter everyone passes filters nothing"). Three weeks later the Sapphire meeting brief still opened with *"ICP score 9.2/10, overall 9.0/10 — one of the best-fit clinics in the entire list."* The retired score was doing live argumentative work.
**How to apply:** when a metric is retired, strip it from every doc that uses it as a *reason*, not just from the scoring step. Scores may remain as database metadata; they may never appear in a sentence that justifies a priority or an effort level.

## 3. Feedback — provisional (awaiting real-world proof)

**[PROVISIONAL — craft discipline, no longer a tracked metric] Deliberate opening archetypes, one per clinic:**
1. Structural-inevitability · 2. Contrarian pattern-interrupt · 3. Compliment-then-pivot · 4. Review-quote / fact reframe · 5. Mystery-shop story · 6. Blunt question · 7. Seen-not-answered mirror

**Status change 2026-08-13:** `opening_archetype` was removed from `SEND_LOG.csv` as a tracked column. At 40–65 lifetime touches a copy-level attribution question needs several hundred sends per arm — the column could never have answered anything, which is why it went unfilled. **The archetypes stay as a drafting discipline** (assign one deliberately per clinic, record it in the draft file) and are retired as a measurement. Do not re-add the column without a decision entry.

**[PROVISIONAL — 2026-08-01, still no reply data] A promise-based automation gap is stronger framed as a wasted capture window than as a broken promise:**
When an after-hours auto-reply only *promises* a human callback, the deeper insight is that the window is being spent on a static promise instead of capturing what a rep needs to close: treatment interest, timeline, budget range, branch preference. Whoever calls back starts from zero.
**Why this is better, not just additive:** it holds regardless of whether the promised callback happened. A single mystery-shop data point about a missed callback is fragile — one data point, often ambiguous about whose follow-up it was (this exact ambiguity came up on Ministry of Skin). The capture-window framing sidesteps that.
**How to apply:** lead with the concrete broken/kept-promise fact if one exists, but build the "why this matters" around the missed-capture insight. First built into the Ministry of Skin one-pager, 2026-08-01. **No reply. Unproven.**

**[PROVISIONAL — designed 2026-08-04, still zero conversations run through it] The post-reply sales motion (`SALES_MOTION.md` + `01 Playbooks/Sales Motion/`):**
Five stages, each with an owner and a clock. Three governing rules: nothing ships without a date or two named slots; diagnosis and prescription never happen in the same conversation; a warm reply outranks the send quota.
**Three deliberate departures from Tilak's stated brief:** (a) no "company profile" — replaced with a method-and-terms "How We Work" doc; (b) the audit call is split into two conversations; (c) `08 Collateral/Audit Call Docs/02_data_intake_requirements.md` re-staged to Stage-4 kickoff.
**Positioning bet inside it:** with zero clients, "we're early" is volunteered rather than extracted under questioning. Unproven.
Nothing here has met a real clinic. **The Sapphire call is the first test of it** — do not treat any of it as settled until that conversation has actually run.

**[UNPROVEN — the five hypotheses this business actually rests on, as of 2026-08-13]**
Named together because no amount of document cleaning tests any of them, and each is currently written into the docs as reasoning rather than evidence:
1. **In-person drop-ins convert well with clinic owners.** Zero meetings held, zero calls held. Actively being pursued. The ladder Tilak runs: drop-in → call if that's too much commitment → on-site once the audit is agreed.
2. **"We're early" volunteered beats a portfolio.** Never tested on a live conversation.
3. **The demo converts a claim into something testable.** Now buildable — the WhatsApp qualification/booking flow is live — but no founder has messaged it yet.
4. **The five-stage post-reply motion works.** Designed 2026-08-04, zero conversations run through it.
5. **The free audit + strategy doc earns the paid implementation.** Free has been offered ~25 times and accepted zero times, though never yet in this exact shape.
**How to apply:** offer all five, cite none of them as patterns. One held call moves the project further than another audit pass.

**[PROVISIONAL — 2026-08-11, adopted as rule 2026-08-13 but untested] Weekend is prime shopping time in this market, not after-hours.**
Across the 171 aesthetic/derm clinics in the SE Bangalore scrape: Saturday 6pm is the highest published-open slot at 92%, ahead of Tuesday 11am (89%) and Tuesday 2pm (78%). 220 of 223 clinics with hours are open Saturday. The published-hours admissibility rule was adopted on this basis. **The underlying data is published hours, not verified staffing** — the rule is now canon, but the claim that Saturday shops produce better hooks has not been tested even once.

## 4. The feedback loop mechanism (use it, don't reinvent it)

`files/OUTBOUND_MEMORY.md` §7 defines the *format* for reporting outcomes → append to `SEND_LOG.csv` → tally → promote/demote hooks in §2 → log banned-phrase additions to §3 → log decisions to §6.

**⚠️ Corrected 2026-08-13, second pass — Notion is the ledger, not this repo.** Tilak stated it directly: he will never report sends in chat. Read the Notion "Valence Leads tracker" (Batch 1 + Batch 2) at the start of any session touching outbound state. Schemas and IDs in `CLAUDE.md`. **Notion overrides every file here on per-clinic outbound state.**

- `files/SEND_LOG.csv` — **frozen historical fragment, 6 rows.** Not the ledger. Never compute a rate from it.
- `files/REPLY_LOG.csv` — **2 rows, both open.** Sapphire (asked for a company profile, deck sent with no date, thread stalled, call being rescheduled) and Aesthetica Veda (handed over a decision-maker's email). Still useful — Notion has no good shape for post-reply stage tracking.
- **Real touch volume, counted from Notion Batch 1 + Batch 2 statuses on 2026-08-13: roughly 70–90, not the 40–65 estimated in the first pass, and not the 6 in the CSV.** Most Batch-1 rows sit at follow-up 4 or 5 across multiple named POCs; Clinic Next Face alone is at ~10 touches. **This puts the 100-touch tripwire close to firing and possibly already past it.** The count needs doing properly rather than estimating — see `OUTBOUND_MEMORY.md` §1.

**Repo presence ≠ contacted [confirmed 2026-08-13].** All clinic research is dumped into this folder, including leads neither Tilak nor Pratham will contact, because it is useful raw material to synthesize across. A clinic with a dossier but no Notion row has not been shopped and not been messaged — it is parked inventory for a future batch, chosen deliberately, not neglected work.

## 5. Project threads

**The two warm threads — the only ones that have ever existed [as of 2026-08-13]:**
- **Sapphire Skin & Aesthetics** — replied that the observation was good, asked for a company profile. A deck went out **with no date attached** and the thread stalled: the exact "document stall" failure mode in `SALES_MOTION.md` §4, on the best opportunity in the project's history. A meeting was prepped for 2026-08-13 (`MEETING-BRIEF-sapphire-2026-08-13.md`) — **not held yet, being rescheduled.** The brief stays live. **Not in the Notion tracker — create the row.**
- **Aesthetica Veda** — saw the one-pager, handed over a decision-maker's email. Open, unworked.
Both outrank any new sending. `OUTBOUND_MEMORY.md` §6 (2026-08-04): a warm reply outranks the send quota.

**The capacity failure that produced `SALES_MOTION.md` [confirmed 2026-08-04]:** a clinic replied and asked for a company profile; nothing existed to send and no idea existed of what the sales motion looked like past a positive reply. Tilak named the underlying feeling precisely — research, enrich, send, wait was monotonous but *felt* productive, so the missing back half stayed invisible until a reply exposed it. Two structural notes: (1) the diagnostic one-pager is the most effort-intensive asset and it ships cold, so the credibility ladder peaks at touch 2 with nothing above it to unlock on a reply; (2) ValenceOps sells speed-to-lead, so a slow response to a warm clinic is a live demonstration of failing at the thing being sold. **Build order agreed and still unmet: no new Day-0 batch until the 6-minute walkthrough video and the How We Work PDF exist as files.**

**Batch 1 (the Notion cohort) — 28 clinic rows**, cozmo bliss → Evenly Skin and Hair Clinic. Outbound sent through Dr. Karishma Aesthetics (clinics 1–15 in tracker order). **Dr. Ritika Shanmugam → Skinology Centre (7 clinics)** were rebuilt 2026-07-25 with deliberately varied opening archetypes, saved in `outreach-drafts-utkarsha-to-evenly.md` (sections marked "REBUILT 2026-07-25"), plus a rebuilt Dr Juvita email. **Remaining clinics after Skinology (idhaclinic → Evenly, 6 clinics + Sanyukt parked) are still in original, non-rebuilt draft form — apply the rebuild treatment before those go out.**

**Mega-founder-brand deferral:** `OUTBOUND_MEMORY.md` §6 (2026-07-22) defers mega-founder-brand clinics to *after* Case Study #1 — gatekeepers and likely incumbent agencies make them a worse bet for a first client than a founder-run mid-tier clinic. Sanyukt Skin Clinic (327K followers, professionally managed social, active paid ads) independently qualifies and was parked. Karishma, Sculpt and Anew were drafted anyway on direct instruction, each flagged inline — treat these three as lower priority regardless of what's drafted.

**Reachability gaps found during Batch 1 (check social presence before assuming an IG-first sequence works):**
- Dr. Utkarsha's and Dr. Keshav's: no usable Instagram at all — WhatsApp/email only.
- Dr. Sculpt: IG inactive — routes through LinkedIn.
- Dr Juvita, Vtiara, Sapphire: only brand-page IG or LinkedIn on file, no confirmed personal founder account — confirm before a Day-0 send.
- Clinic Next Face: listed phone numbers read as front-desk/booking lines, not founder Ishmeet Singh's personal WhatsApp.

**⚠️ OPEN DISAGREEMENT — the Saturday 15/8 after-hours sweep [raised 2026-08-13, awaiting Tilak's call].**
Notion Batch 2 notes schedule an after-hours test for **Sat 15/8 ~10:30 PM** on Ara, Gejje's, Krity 360, Theory of Skin, VIDA and Dermatonik. Three problems, in order of severity:
1. **It produces inadmissible evidence under the rule adopted 2026-08-13.** 10:30 PM Saturday is outside published hours for essentially every clinic on that list. By the published-hours admissibility rule, those findings cannot be used as hooks. The sweep would burn six test identities to generate material that is banned on arrival.
2. **His own Aug-11 §3.3 already argued for dropping genuine after-hours entirely** — the rebuttal ("we were closed") is correct, every clinic fails it so it discriminates nothing, and it costs a test identity plus a wall-clock day.
3. **Four of the six are fast responders, and the sweep is looking for slowness.** VIDA replied in 2 minutes and its own Notion note says *"Do NOT sell speed — they have it and are right to be proud of it."* Ara 18 min, Krity 1 min, Theory of Skin instant. Testing them after hours until a bad number appears is the forcing-the-speed-wedge-onto-fast-responders pattern, now flagged four times.
**The cheap fix: run the sweep at Saturday 6 PM instead of 10:30 PM.** Saturday 6 PM is the single highest published-open slot in the SE Bangalore dataset at 92%, the desk is thinnest then, and every finding is admissible. Same effort, same identities, usable evidence.
**The one genuine exception is Akera** (25 Meta + 29 Google running simultaneously) — it qualifies for the §2.2(c) heavy-spender carve-out. But Akera already has a confirmed 19-hour in-hours wedge, so the extra test buys little.

**SkinFit has left the audit path [confirmed 2026-08-20, Gino via Tilak].** Gino said an audit is not possible in the coming week or anytime soon, and asked instead for a proposal with costs and the systems that could be built. The team produced a 55-question self-report questionnaire (`~/Desktop/SkinFit-Information-Request.docx`) intended to stand in for the audit. **It cannot.** Reviewed in `SKINFIT-INFORMATION-REQUEST-REVIEW.md`: it answers 2 of the 8 audit objectives in the tech handoff §8 and misses every one that would produce a number — including the headline finding (Meta conversation count vs. their ~10/day sheet), which is unreachable by asking, because the answer comes from the same sheet. Good build-scoping document, bad diagnostic one.
**The request for the proposal and quote is now directly evidenced [confirmed 2026-08-21 from the recent WhatsApp screenshot].** After receiving the five-page `SkinFit Wellness - Enquiry Handling Review.pdf`, Gino said an audit could not happen soon and explicitly asked for a document showing “the proposal and the quote of what all is covered and offered,” with building the system and finding a process as the next step. We replied that a few questions about their tools and current operation were needed before sending the proposal and quote; he accepted that. Gino also said the material could be discussed with Drish, so the document is meant to travel internally through Gino to the founder. **Correction to the earlier internal reading:** Gino did ask for scope and costs; what remains unconfirmed is not whether he wants a proposal, but who will approve/sign it and what the unanswered operational questions are.
**The recovery, and it is cheap:** two screenshots Gino can take himself from his own Ads Manager — messaging conversations started, and the Leads Center list — plus **declared** (not covert) mystery shops now that a relationship exists. Those get the evidence with no access and no audit. Also: tier the questionnaire (~12 Tier-1 questions), split it by respondent because Gino cannot answer the front-desk sections, move the personal-number-vs-Cloud-API question to the top, add a "blur any patient names in screenshots" line, and attach a return date.
**Legal consequence, logged in `LEGAL-AND-COMMERCIAL-DOC-SET.md` §3A:** with no audit, the contract has to do the de-risking — an Assumptions Schedule signed with the SOW, a re-scope trigger if an assumption proves wrong at onboarding, a paid days-1–3 validation phase, and a migration contingency if WhatsApp turns out not to be on the official API. The audit access letter is no longer needed and has been dropped from the blocking set. **The free-pilot / paid-implementation boundary (`OUTBOUND_MEMORY.md` §5) is now actively blocking — Gino has asked for costs.**

**Legal entity — Valence Ops is a SOLE PROPRIETORSHIP [confirmed 2026-08-20 from the registration documents in `~/Documents/Valence-Ops-Legal/`].** Not a Pvt Ltd, not an LLP. Proprietor: S Tilak. Commenced 01-06-2026. **Already held:** Udyam UDYAM-KR-03-0707297 (Micro, Services, 04-06-2026) and Karnataka S&E registration 25/37/CE/0063/2026 (31-07-2026, valid to 31-12-2030, 3 employees declared). Those two are exactly the pair a proprietorship current account needs, so the account should open without friction. **Missing:** GST (not applied), Professional Tax position unclear.
Consequences that keep mattering: no CIN (never put one on a contract or letterhead); contracts signed *"S Tilak, Proprietor, trading as Valence Ops"*; the rubber stamp has no legal force, the signature binds; **liability is personal and unlimited**, so the liability cap and medical disclaimer in any client contract are real protection, not boilerplate; TDS lands in Tilak's personal 26AS and income is taxed at slab rates.
**Two document defects found and not yet fixed:** the S&E and Udyam certificates give different street names for the same building (Railway Station Rd vs Anjaneya Temple Street), and the NOC on file is a blank template naming a different property (867/35 Gokula) than the registered address (#35/2 JK Nilaya, Yeshwanthpura). Both must be fixed before a GST filing or the application goes to physical verification.
**GST correction:** the current account is **not** needed to apply — bank details are furnished post-registration under Rule 10A. File now. Tilak's worry that RCM on US platforms blocks operating without GST is inverted: unregistered means foreign suppliers charge 18% that cannot be reclaimed; registered means RCM with full input credit. The real trap is Section 24(iii) (mandatory registration at zero threshold for reverse-charge liability on *non-OIDAR* imports). Clean workaround for Meta spend: buy through an Indian BSP, which is needed anyway for the SkinFit commitment #3 to be true.
**The biggest unaddressed legal gap is internal, not client-facing:** four people are described as founders, but a proprietorship means Tilak legally owns 100% of the clients, IP and revenue and the other three own nothing. No founder agreement exists. Recommendation given: do not incorporate now (it would reset the bank account and GST by 3–4 weeks with SkinFit live), but write a founders' understanding this month; incorporate at the first signed paying client or first outside money.
Full stage-by-stage document set in `LEGAL-AND-COMMERCIAL-DOC-SET.md`. **Four client-facing legal documents still do not exist and block the SkinFit path: audit access letter, proposal/SOW template, services agreement + DPA, invoice template.**

**Parked inventory — NOT sprawl [corrected by Tilak, 2026-08-13].** I initially framed the ~150 clinics across eight cohorts as sourcing bias and "a tripwire on touches and none on inventory." That framing was wrong and is retracted. The cohorts not in Notion — the 52-clinic SE Bangalore scrape, batch1-2, batch 3, `Research-docs/`, `clinics/` — were **scraped and deliberately parked** as candidate inventory for a future batch. Nothing was started and abandoned; it was never begun. Tilak will say when to pick them up. `COHORT-INDEX.md` keeps them findable. The Aug-11 §4 critique still applies to *timing a new scrape* while a warm thread sits unworked — it does not apply to the existing pile.

**Batch 7 / Batch 2 — the shops HAVE been run [corrected 2026-08-13 from Notion].** My first-pass claim that this cohort had "zero mystery shops on any of 25 dossiers" was true of the repo and **false of reality.** Notion Batch 2 shows **12 clinics shopped on 10–11/8/26**, with:
- **5 wedges confirmed** — Dr. Priya's (systematize the hustle / manual dependency), Project Skin (dead-lead reactivation), Akera Health (dead-lead reactivation, 19-hour response, strongest evidence in the batch), Derma Solutions (enquiry deflection), Haircosmos (dead-lead reactivation, high-ticket).
- **2 tests running with clocks** — Krity 360 (quote decay from 10/8 + IG persistence to ~24/8) and Theory of Skin (quote decay + abandoned 12:30 slot, from 10/8). **Do not message either** — silence is the test.
- **4 retest-needed**, 1 pending screenshot review (Vitals Klinic).
- **DM-1 already sent** on IG to named founders at Dermatonik, Gejje's, Dr. Priya's, Project Skin, Ara, Haircosmos and Akera.
The sequencing lesson still stands — dossiers were written before shops. The evidence-gap claim does not. **This is the clearest possible demonstration of why Notion must be read first: the repo said zero, reality was twelve.**

## 6. Reference

- Notion "Valence Ops Leads Tracker" — see `CLAUDE.md` for URLs and schema. Covers Batch 1 only.
- `COHORT-INDEX.md` — which cohort is which, and where each clinic's dossier lives.
- Apify is connected and pre-authorized for this project's research. Free tier is $5/month and has been exhausted mid-batch before (`SESSION-2026-08-10-se-bangalore-scrape.md`).
