# Lead Prioritization Method — how the 20-clinic priority table was actually produced

**Written:** 2026-07-29 · **Source:** the process used to produce the Batch 1 priority table (Ministry of Skin → Skinology Centre)
**Purpose:** a build spec for a deeper qualification skill. Phases are sequential; the rule tables inside them are the parts that should become skill sections verbatim.

**The core thesis of this method:** prioritization quality is not determined by judgment about clinics. It is determined by *what you let count as evidence* before any judgment happens. Get admissibility right and the ranking falls out semi-mechanically; get it wrong and no amount of thinking downstream recovers it. That is also why this scales — the expensive part is mechanical and can be standardized, and only a small named set of second-order overrides needs real judgment.

---

## PHASE 0 — Load the judgment framework BEFORE the data

1. **Read the routing/qualification playbook first** (`wedge-signal-entry.md`), before opening a single clinic dossier.
   **Why this order matters:** dossiers are persuasive documents. They foreground whatever the researcher found interesting. If you read them first, you pattern-match on dossier salience and then reach for the framework to *justify* what you already concluded. Loading the framework first means the framework defines what you're even looking for.

2. **Read the correction layer second** — the documents that record where previous analysis was wrong (`files/OUTBOUND_SYSTEM_AUDIT.md`, `MEMORY.md`, `OUTBOUND_MEMORY.md` §6 decision log).
   **I got this order wrong.** I read the raw research before the audit doc, and had to re-scan the research afterwards once the audit told me 9 of the shops were midnight false-positives. Cost: one full re-pass. In the skill, the correction layer is a Phase 0 input, not a Phase 3 input.

3. **Extract the standing decisions that pre-empt analysis** and write them down before scoring anything. In this run those were:
   - Mega founder-brands deferred to post-Case-Study-#1 (2026-07-22 decision) — an *access* judgment, already made, not to be re-litigated per clinic.
   - The IG-slower-than-WhatsApp comparison is a retired wedge (MEMORY §2).
   - Business-hours-only mystery shops; midnight results are not hooks.
   - Never build on "Potential Missing Layers" checklist items.

   These are load-bearing. Three of the twenty rankings changed because of them.

---

## PHASE 1 — Establish the denominator before any analysis

4. **Pull the authoritative list first** (Notion tracker), not the research folder. The research folder is a superset and a different vintage; the tracker is what's actually being worked.

5. **Confirm every name on the list maps to a dossier, by grep on section headers — not by memory or assumption.** I grepped all three research files for clinic headers and found `outreach 3.md` contains 7 clinics that are *not* in the tracker (Idha, LA CROWN, Contura, Umbrella, Evolve, Sapphire, Evenly). Without that check I might have scored a clinic from the wrong cohort, or silently dropped one from the right cohort.

6. **Check for a second source of per-clinic state that the dossiers don't have.** Here: Notion `Status` (touch count, what was sent, on-hold flags) and the `One-page-docs/` folder (which clinics have a diagnostic built). Both changed rankings. Dossiers describe the clinic; they say nothing about the state of the relationship.

7. **Note the coverage gaps rather than papering over them.** Notion's `Files` column is empty on all 20 rows, and `CLAUDE.md` references a `Google Docs` property that no longer exists in the live schema. So doc-to-clinic linkage had to be done manually from the folder listing.

---

## PHASE 2 — Build a per-clinic evidence ledger, with verified and asserted kept apart

8. **For each clinic, extract into fixed buckets.** Do not summarize — extract. Summarizing is where hypotheses get laundered into facts.

   | Bucket | What goes in | Why it's separate |
   |---|---|---|
   | `test_evidence` | Mystery shop: channel, **exact timestamp**, day of week, what happened, latency | The only first-hand evidence; admissibility depends entirely on the timestamp |
   | `spend_evidence` | Active ad count + platform | Establishes "money already spent" — the proximity axis |
   | `volume_evidence` | Google review count, Practo story count, follower counts | Establishes whether there is pipeline for a system to act on |
   | `patient_voiced` | Direct review complaints, ideally verbatim | Strongest non-test evidence; it's the clinic's own patients, so it can't be rebutted as our misreading |
   | `access_state` | Which channels are live, personal vs brand account, gatekeeper signals, agency signals | Determines whether a good wedge can even be delivered |
   | `relationship_state` | Notion status, touch count, doc sent, on-hold flag | Determines whether this is an opening problem or a closing problem |
   | `ASSERTED — discard` | Everything under "Potential/Possible Missing Layers", "Unknown", "❓" | These are template lists of what *might* be missing at any clinic. They are not findings about this clinic. |

9. **Record the timestamp even when the source didn't.** Three dossiers logged a mystery shop with no time (Dr. Swetha's "Wednesday", Clinic Next Face "friday", Dr. Juvita "8/7/26"). Mark these `time_unrecorded` explicitly rather than treating them as either admissible or inadmissible — they need a different rule (see #14) and they generate a data-gap flag in the output.

10. **Resolve attribution ambiguity in the raw notes.** Research notes like "Follow up wednesday 12:30pm, 2:30pm" are ambiguous: did the *clinic* follow up, or did *our tester*? This inverts the verdict. The tell in this dataset was the verb — "**Got** one followup on text same day night 10 pm" (Aura) means clinic-initiated; a bare "Follow up wednesday 12:30pm" in a list of our own actions means tester-initiated. Where it's genuinely unresolvable, mark it and don't score on it.

---

## PHASE 3 — Apply evidence-admissibility filters (highest-leverage step in the whole method)

This is the step that most changes the answer. In this run it disqualified the primary evidence for **11 of 20 clinics**.

11. **Filter A — Timestamp.** Any mystery shop sent between roughly 9pm and 1am is **inadmissible as a response-speed hook.** A clinic replying at 9:20am to a midnight message is behaving normally; leading with it hands the founder an instant, correct rebuttal and reads as a gotcha.
    Discarded on this rule: Dr. Utkarsha's (12AM), Dr. Sculpt (12:40am), DNA (10:57pm/11pm), Dr. Ritika (9:00/9:09pm), Dr. Dixit (9:32/9:36pm), Anew (12:41am), Iridescent (11:33pm), Dr. Tina's (12:02am/12am), Cozmo Blis (12:28am), Aura (9pm WhatsApp leg), Ministry (Sat 9:30pm IG leg).

12. **Filter A carve-outs — three kinds of failure survive the clock.** This is the subtle part and it's where most of the value was:
    - **(a) Broken self-declared SLA.** Ministry of Skin's own automation said "one of our team members will get back to you during working hours," and nobody did. That is *their* stated commitment failing, not our expectation failing. Time of night is irrelevant to it. This turned Ministry's discarded after-hours test into the single best hook in the dataset.
    - **(b) Structural / qualification failure rather than latency failure.** Aura Cutisurg's Instagram auto-reply fires, the tester asks the consultation cost, the thread dies. Dr. Juvita's auto-reply fires with zero qualification, segmentation or data capture. Neither of those is a "you were slow" claim — they're "your system has no second step," which is true at any hour.
    - **(c) Multi-day silence.** Clinic Next Face: Friday enquiry, no response through the following Wednesday. Five days of silence is not explained by what hour Friday it was sent.

    **Rule for the skill:** before discarding an after-hours test, check whether the failure is *latency* (discard) or *structure / broken promise / multi-day* (keep).

13. **Filter B — Source class.** Anything sourced from a "Potential Missing Layers", "Unknown / Possible Missing", or `❓` section is a hypothesis to test, never a finding to assert. These sections are boilerplate that appears near-identically across all 20 dossiers — which is itself the tell.

14. **Filter C — Hedge words.** "likely", "expected", "may", "possible", "probably" in the source research means the researcher was inferring. Such lines can shape *what to investigate*; they cannot appear as evidence. (E.g. Cozmo Blis's "high-value opportunities can go cold without structured follow-up" is a category truism about cosmetic surgery, not an observation about Cozmo Blis.)

15. **Filter D — Time-unrecorded tests.** Treat as admissible *only* if the finding is time-independent under #12 (structural failure or multi-day). Dr. Swetha's Wednesday test qualifies because the finding was "no automation, no qualification on either channel" — structural. But flag the missing timestamp as a data gap in the output, because the *sharper* version of the hook (an exact dated timestamp) can't be written until it's filled.

16. **After filtering, ask per clinic: is there anything admissible left?** For several clinics the honest answer was no — Dr. Utkarsha's, Dr. Ritika. That is a finding, not a failure, and it produces a specific instruction ("run a business-hours test before this earns a slot") rather than a vague low ranking.

---

## PHASE 4 — Rank on winnability, not impressiveness

17. **Explicitly discard the ICP score as a ranking input.** All 20 clinics scored 7.5–10.0. A filter everyone passes filters nothing; it measures how impressive the business is, not how winnable it is. The pre-existing priority list in `valence-ops-clinic-intelligence-os.md` §5 was ordered by ICP score, which is why it put Cozmo Blis 4th and Skinology 8th — both of which invert under this method.

18. **Score on five axes instead.** Priority is roughly their product, not their sum — a zero on axis 3 (door) caps the whole thing regardless of axes 1 and 2.

    | # | Axis | Question | What moves it |
    |---|---|---|---|
    | 1 | **Provability** | Is there an admissible, screenshot-able break that survives Phase 3? | Broken SLA > patient-voiced review > business-hours test > structural failure > nothing |
    | 2 | **Proximity to spent money** | How close is the break to money already committed? | Active ad count, aggregator/Practo spend, paid-listing dependence |
    | 3 | **Door openness** | Can this message actually reach a person who can say yes? | Personal founder account live · mid-tier follower band · no gatekeeper · no agency lock-in · single decision-maker |
    | 4 | **Wedge availability** | Is there a fresh fact left to lead with? | Facts already spent across prior touches subtract from this |
    | 5 | **Volume floor** | Is there enough inbound for any system to act on? | Review count, Practo stories, ad presence, follower activity |

19. **Route the wedge from the signal combination, not from the clinic's category.** Every clinic's entry service came from matching its admissible signal set against the `wedge-signal-entry.md` §3 routing table, and the row it matched is what set the base priority tier. Priority and wedge are the same decision, made once — not two separate judgments.

19a. **Volume is a multiplier on axis 1 and axis 4's output, never a sixth standalone axis.** This was underused in the first pass and is worth stating as an explicit rule, because getting it wrong reopens the exact trap axis-discard (#17) was built to close.

   - **Confidence multiplier:** a mystery shop is n=1. At high volume (double-digit ad count, five-figure follower count), a single observed break is very likely representative — the tester's interaction wasn't meaningfully different from the dozens/hundreds happening concurrently. At low volume, the same single break could be a one-off (the doctor was mid-consult that one time). Weight test evidence accordingly: high-volume + one failed test ≈ systemic; low-volume + one failed test ≈ suggestive only.
   - **Magnitude multiplier:** the same admissible break is worth more at a high-volume clinic because the provable recovery number (and the case-study material it produces) scales with it. "Recovered N bookings out of 300 dormant enquiries" is a stronger proof-of-value than the same N out of 20 — same effort, bigger number, and with ad spend attached, an actual rupee figure to lead the pitch with.
   - **The failure mode this guards against — do NOT let volume alone raise priority.** A clinic can have real volume and no gap (Skinology: 16 ads, 1-minute human reply with a qualifying question — volume plus a passed test is not an opportunity). Making volume a standalone axis reintroduces ICP-score thinking (bigger/more-impressive clinic ranks higher) through the back door. Volume only matters *multiplied onto* an already-admissible break from axis 1 — never on its own.
   - **The corollary — low volume caps a real break's priority, it doesn't disqualify it.** Dr. Juvita's automation gap (greeting-only, no qualification — a genuine top-of-funnel break) sits at zero ad spend and 5,722 followers, the lowest volume in the Very-High tier in the original pass. Even though the break is real, the absolute size of what's being lost is probably small, which caps both how much a pilot could visibly recover and how confidently the single test generalizes. This was a real scoring error in the original table — Juvita's tier was set as if the break's *existence* was the whole story, without discounting for how little volume there is for it to act on.
   - **Don't stack findings from different funnel stages as if they're two confirmations of the same break.** Re-checking Juvita: the automation gap is top-of-funnel (DM/WhatsApp intake). The "entire clinic depends on one single doctor" review complaint is mid-funnel (in-clinic consultation/appointment delays for patients already booked). These are two separate, real problems at different stages — treating them as mutually reinforcing evidence for one wedge inflated the confidence in the ranking beyond what either finding supports alone.

19b. **Team-capacity is the genuine blind spot, and it's currently near-zero data across all 20 audits.** None of the dossiers capture staff headcount, so "is this volume actually within manual capacity" can only be proxied, never confirmed, from what's on file:
   - Multiple listed contact numbers per location (Glow: 3 numbers across cities; Karishma: 4 numbers) weakly suggests distributed front-desk staff rather than the founder alone.
   - Reviews that mention "reception"/"staff"/"team" as distinct from "the doctor" suggest some distributed capacity.
   - Reviews that name only the doctor as the point of friction, with no staff ever mentioned, suggest capacity is not distributed at all — which argues a break is more likely to be real, but doesn't tell you its size.
   - **For the skill: add `staff_capacity_signal` (proxy, not confirmed) as an audit field**, and treat any priority built on high perceived volume without this field as provisional — flag it the same way an unresolved timestamp or attribution ambiguity gets flagged (#9, #10), not treated as settled.

---

## PHASE 5 — Second-order overrides (the catalogue — this is the reusable part)

Rules 1–19 produce a defensible ranking. These are the checks that *changed* it. Each one is a pattern to look for, not a one-off.

20. **Label vs. reality mismatch.** Ministry of Skin was tagged "Mega Founder-Brand" in the intelligence doc and therefore sat behind the mega-brand deferral. Actual follower count: 3,752 — mid-tier, no gatekeeper, founder opens her own DMs. The label was doing work the underlying number didn't support. **Check: does the classification survive its own data?**

21. **Stale conclusion from a since-retired rule.** Vtiara was marked "On hold — didn't really find a wedge." That conclusion came from the Instagram-slower-than-WhatsApp comparison, which `MEMORY.md` §2 retired as invalid. The conclusion outlived its reasoning. **Check: when a clinic is parked, re-derive *why*, and confirm the reason is still a live rule.**

22. **Praised-strength inversion.** AvatarLuxe's reviews repeatedly praise pre-surgery counselling and post-treatment follow-up — "patients consistently praise follow-up support." Follow-up is the thing we sell. Public praise for your own product category is a wedge *kill*, and it's easy to miss because it sits in the "Strengths" section that a gap-hunting read skims past. **Check: read the strengths section specifically for praise of the service we intend to sell.**

23. **Good operations is a finding, not an absence of one.** Skinology replied in 1 minute, human, with a qualifying question, and its reviews explicitly note *no* consistent scheduling complaints. That is a tested pass, and the correct output is a confident park with a named re-entry condition — not a lower-confidence "we didn't find much."

24. **Facts-spent ledger.** Cozmo Blis is four touches deep and its two usable facts (the midnight gap, the 28 ads) were fully consumed across 3 WhatsApp messages plus the one-pager. A clinic with a strong profile and no unspent fact is approaching park, not escalation. **Check: subtract already-used hooks from wedge availability before ranking.**

25. **Third-party ownership of the pipeline.** Dr. Sculpt's acquisition, EMI financing and patient routing run through Medfin; Dr. Karishma's ads run through Growthmax Agency LLP. In the first case a chunk of the pipeline may not be theirs to act on, so reactivating it isn't even their decision. In the second, an incumbent already owns the surface we'd touch. **Check: who actually owns the leads before assuming the clinic can act on them.**

26. **Role-as-buyer signal can invert a structural risk.** Three co-founders normally reads as committee sign-off risk (a hard-kill signal). At The Glow Clinic, one of the three is Rohit Reddy, **Operations** co-founder — a named person whose job title is the problem we solve. Same structural fact, opposite implication. **Check: read founder roles individually, not just founder count.**

27. **Buyer sophistication cuts both ways.** Clinic Next Face's founder has an SEO/digital-marketing background. Archetype logic says operator-led closes fastest — but he is also the single person most likely to spot generic outreach instantly and to have already thought about this gap. Records as high ceiling *and* highest message bar, not simply "easy win."

28. **Separate fit from door, and say which one is capping the ranking.** DNA Skin has arguably the strongest patient-voiced evidence in the set ("multiple calls needed to reach the clinic"). Dr. Keshav's has 1,255+ Practo stories and exactly the right review complaints. Both are capped by access, not diagnosis. Stating that explicitly makes the ranking actionable — it names what would have to change to promote them.

29. **Relationship warmth can outrank evidence quality.** Iridescent's only mystery-shop data is an inadmissible 11:33pm no-reply, but the diagnostic doc is sent and it's at touch 3. That's a closing problem, not an opening problem, and it ranks on the open thread rather than on the wedge. **Check: an open thread changes what the clinic needs from you.**

30. **Volume floor as a ceiling.** Aura Cutisurg has the cleanest time-independent hook in the set (auto-reply dies on a direct question) — and 94 Google reviews, ~500 followers, zero ads. The kill-filter's volume threshold is 100+ reviews. Real problem, possibly insufficient pipeline for the system to act on. **Check: a great hook at a clinic with no volume is still a bad target.**

---

## PHASE 6 — Self-audit before shipping (run every one of these; do not skip on confidence)

31. **Consistency sweep on the primary filter.** I re-walked all 20 clinics and re-checked the timestamp decision on each, one at a time, confirming both the discards and the three carve-outs were applied the same way everywhere. Inconsistent application of the strongest filter is the highest-probability failure mode, because it happens gradually as you tire.

32. **Rule-based check: did the method actually override the prior ranking?** If the output largely reproduces the existing ICP-ordered list, the method didn't do any work. Here it inverted five positions (Ministry up, Vtiara off hold, Cozmo down, AvatarLuxe down, Skinology confidently parked), which is evidence the filters bit.

33. **Fabrication trace.** Walk each specific claim in the output back to a source line: "Growthmax Agency LLP" → Karishma ads section; "1,255+ patient stories" → Keshav Practo line; "94 reviews vs the 100 threshold" → Aura basic info + kill-filter §8.3. Anything that can't be traced gets cut or re-labelled as an inference.

34. **Distribution suspicion.** My first pass produced an exactly even 4/4/4/4/4 split across five tiers. Neat distributions usually mean the tiers were fitted to look balanced. I re-checked Cozmo Blis against my own stated rule (provability drives priority; it has none and its facts are spent), moved it from Medium to Low, and the distribution became uneven — which is the more trustworthy outcome.

35. **Differentiation check on adjacent calls.** Iridescent and Cozmo Blis both have 28 ads and both have only an inadmissible midnight test. They land in different tiers, so the differentiator must be nameable: Iridescent has an open thread and a sent doc; Cozmo's thread is cold and its facts are spent. If you can't name the differentiator, the two clinics belong in the same tier.

36. **Caveat honesty pass.** Flag anything the output depends on that isn't solid — Ministry's "Didn't connect later" is a terse note carrying the highest-ranked hook in the set, so it's flagged for re-confirmation before it reaches copy. Ad counts came from the dossiers and were not independently re-verified, which the standing Apify lesson says is a real risk.

---

## PHASE 7 — Output discipline

37. **Three columns, and the reason column does real work.** Every reason contains: the admissible evidence with its number/timestamp → the routing-table row it maps to → the counter-consideration or caveat. A reason with no counter-consideration is usually a reason that skipped Phase 5.

38. **Say what's inadmissible and why, inside the reason.** "Both shops were 9:32/9:36pm and are discarded, so the case rests on reviews alone" is more useful than silently omitting the shops — it tells the reader how much weight the ranking can bear.

39. **Separate data gaps from findings.** Dr. Swetha's missing test timestamp is an action item, not a demerit.

40. **Surface the ranking changes that require a decision** rather than burying them in a table cell — Vtiara coming off hold and Ministry's mislabel were called out above the table because both change what gets worked this week.

---

## What would make this cheaper to run at scale

41. **The expensive part was re-deriving the evidence ledger from prose.** Roughly 90KB of dossier text had to be read in full because the dossiers were written to describe clinics, not to be queried for admissibility. If the Phase-2 ledger fields (especially `test_timestamp`, `test_day_of_week`, `failure_type: latency|structural|broken-SLA|multi-day`, `initiated_by: clinic|tester`, `facts_spent[]`) are captured **at audit time**, Phases 2–3 collapse from a full read into a table scan.

42. **`failure_type` is the single highest-value field to add to the audit template.** It is what determines admissibility, and it currently has to be reconstructed by interpretation from free text.

43. **`facts_spent[]` needs to live per clinic and be appended on every send** — otherwise wedge availability (axis 4) can only be reconstructed by reading old drafts and memory files, which is what happened here.

44. **The second-order override catalogue (Phase 5) is the part that should be a checklist, not a judgment.** Each of the eleven is a yes/no question against the ledger. Running eleven cheap checks beats hoping the pattern gets noticed.

45. **Re-derive parked clinics on every batch.** Two of the twenty had stale park decisions. Park reasons decay when the rules behind them change, and nothing currently forces a re-check.
