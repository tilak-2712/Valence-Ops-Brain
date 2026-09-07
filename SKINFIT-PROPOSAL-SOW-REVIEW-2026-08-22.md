# SkinFit Wellness — Proposal & SOW Review

**Reviewed 2026-08-22.** Sources: `SkinFit_Wellness_Proposal.docx`, `SkinFit_Wellness_SOW.docx` (both drafts, pricing/dates left blank on purpose). Compared against `Proposals/SkinFit Wellness - Enquiry Handling Review.pdf` (already sent to Gino), `SKINFIT-TECH-HANDOFF-2026-08-18.md`, `PRICING-BUILD-COST-2026-08-21.md`, `LEGAL-AND-COMMERCIAL-DOC-SET.md`, `taste-n-judgement.md`. Content only — design/formatting explicitly out of scope for this pass.

---

## 0 · Verdict

**Structurally these are the right two documents, in the right relationship to each other, and the "what we found" section is strong — it correctly carries forward what Gino has already read and responded to.** The problem is not shape. It's that the scope quietly changed between the document Gino has and the document you're about to send him, and the SOW makes one compliance claim that looks unearned.

**The one fix that matters most: the proposal drops the single system the sent document promised hardest, and adds three it explicitly said would come later.** Everything else here is real but secondary to that.

---

## 1 · The scope swap — the finding that matters most

The PDF already in Gino's hands (`Enquiry Handling Review`, §06) names **four** systems, in this order, each with a "why here":

| # | System (as sent to Gino) | In the new Proposal/SOW? |
|---|---|---|
| 01 | Every enquiry answered immediately | Folded into "AI Lead Qualification Bot" — present |
| 02 | The concern captured before anyone picks up the phone | Folded into "AI Lead Qualification Bot" — present |
| 03 | **A held appointment instead of a promise to call** | **Absent. No booking system anywhere in either document.** |
| 04 | Missed consultations chased the same day | Present as "No-Show Recovery System" |

The same PDF then names three more **explicitly deferred** — "**Three more, once those hold**": follow-up past the first silence, reviews at the right moment, earlier enquiries revisited. All three now appear in the Proposal/SOW as full, equally-weighted, priced systems — one of them (**Dead Pipeline Reactivation**) leads the list at System #1.

**Why this is the finding, not a nitpick:**

- **#03 was the load-bearing promise, in the sent document's own words:** *"Most people are lost in the gap between 'we'll call you' and someone actually being reached. Removing the step removes the loss."* That's the sharpest single line in the review. It's gone from the proposal.
- **It also breaks the proposal's own internal logic.** Section 03 of the Proposal ("How It Works Together") says *"A booked appointment flows into no-show recovery if the patient doesn't show up"* — the pipeline assumes a booking exists, but no system in the document produces one. As written, an appointment still happens by someone on the qualification bot's handoff calling the patient — which is the exact "promise to call" step §03 was written to remove.
- **Gino can check this.** He has the PDF. `taste-n-judgement.md` §4's own test — *"can the reader check this, and what happens if they do?"* — applies directly. An agency creative director who read a five-page document carefully enough to reply to it is exactly the reader who will notice its headline fix disappeared and three deferred items took its place.
- **Reviews specifically was ruled out once already**, in `SKINFIT-INFORMATION-REQUEST-REVIEW.md` §4.1, on the grounds that it's "a different product line, it is not the wedge," and including it "makes the document read as a vendor scoping an upsell." That reasoning wasn't about the questionnaire only — it applies just as hard to the sales proposal.

**Decide, don't default:** either (a) add Booking back as its own priced system and re-sequence the other three as a named "Phase 2, once the first four are running" — which matches what was already promised — or (b) if Booking was cut deliberately (e.g. because writing into an unknown PMS is unresolved per tech handoff §9), say so explicitly in the document rather than silently dropping the one thing Gino is most likely to notice missing. Cheapest fix: even the low-variance version of booking — "held on our side, desk copies it across," no PMS write access needed — covers the promise without waiting on Adi.

---

## 2 · The PII/compliance claim in the SOW looks unearned

SOW, **Data & Compliance**:

> *"No personally identifiable information (names, phone numbers, emails) is stored in our systems — this data is either masked or never pulled in at the source."*

This doesn't hold up against the systems described two pages earlier. The Qualification Bot's own spec says it produces "a clear summary handed to the sales team" with the patient's requirement, budget, availability. No-Show Recovery has to know *which* patient missed *which* slot to text them. Quote Follow-Up has to know who to follow up with. None of that works without storing a name and a phone number somewhere.

This is the same failure mode `taste-n-judgement.md` §4 names directly — "a fact about our own company that nobody verified" — except it's landed in a signed Scope of Work rather than a sales deck, which is worse. `LEGAL-AND-COMMERCIAL-DOC-SET.md`'s own verdict on the tech handoff's commitment #3 applies here word for word: *"an inaccurate compliance sentence in a document to a founder is a bigger legal exposure than 18% IGST."*

**What the doctrine already says to write instead** (per the same legal doc, §3.1 and §5.2): you're the DPDP Data Processor, the clinic is the Data Fiduciary, data is processed under contract, access is controlled and logged, nothing is copied outside their systems, deletion happens on exit. That's true, checkable, and it's already the shape of the five commitments in the PDF Gino has. Swap the "no PII stored" line for a restatement of those five commitments — which also fixes §3 below.

**One more claim in the same section worth a second look before it ships:** *"A lead's journey is tracked from point of origin (ad click...) through... to final outcome."* Carrying the ad-referral parameter through to a booking is listed in `SKINFIT-TECH-HANDOFF` §9 as an open question to Adi — "potentially our strongest card," not yet confirmed as buildable. The SOW states it as delivered scope. Either confirm it's buildable first, or hedge it the same way the rest of the document correctly hedges the CRM/booking unknowns.

---

## 3 · The five commitments didn't travel into the SOW

The Enquiry Handling Review's strongest section (page 5, "How we would set this up safely") landed well in the room per the run-sheet. `LEGAL-AND-COMMERCIAL-DOC-SET.md` §5.1 item 9 already flags this exact risk: *"leaving them in a PDF and out of the contract wastes them."* The SOW's Data & Compliance section replaces them with a new, unverified, generic claim (§2 above) instead of restating them. Put the five back in, verbatim, in the SOW — it's free continuity and it fixes the PII problem at the same time.

---

## 4 · Two structural gaps against your own doctrine

| Gap | Where it's already required | Currently |
|---|---|---|
| **Assumptions Schedule** — every client-asserted fact the scope depends on (CRM name, whether booking can be written vs. only requested, official API vs. not, two-branch routing) | `LEGAL-AND-COMMERCIAL-DOC-SET.md` §3A.4, written specifically for this no-audit path SkinFit is on | Not present as a named schedule. The SOW's "Client Responsibilities" and "Timeline" footnote gesture at some of this but don't list the assumptions or attach consequences |
| **Re-scope trigger** — if a listed assumption is wrong at onboarding, scope/price get revisited within a stated window, with a clean exit | Same section, item 16, called *"the single most important commercial consequence of skipping the audit"* | Absent from both documents |

Without these two, you've fixed a scope against facts nobody has verified (practice software name, whether a booking can be written in, whether WhatsApp is on the official API) — exactly the situation `LEGAL-AND-COMMERCIAL-DOC-SET.md` was written to prevent for this specific deal.

**Also missing, smaller:** a validity date on the proposal (*"this proposal holds until [date]"* — §4.1 of the same doc). Without one it can sit indefinitely, which is the Sapphire document-stall shape again.

---

## 5 · Two smaller copy items (flagging now since they're cheap, even though design is a later pass)

| Item | Rule it breaks |
|---|---|
| Proposal cover: *"Confidential — prepared exclusively for the addressee."* | `taste-n-judgement.md` §3, standing format rule: **"no 'Confidential — prepared for X' footer."** Was explicitly rejected once already |
| Em dashes throughout both documents ("...moved to a call instead — the concern itself was never captured...", "...journey — from first enquiry through to review", etc.) | `taste-n-judgement.md` §1, banned outright: **comma, colon, or full stop instead** |

---

## 6 · What's actually good here — keep it

- **The two-document split (Proposal = why, SOW = precise scope) is the correct professional-services structure**, and Section 03 ("How It Works Together") is a genuinely good addition — most agency proposals don't bother showing how the pieces connect, and it reads as more credible than a flat feature list.
- **Section 01 ("What We Noticed") correctly carries forward, near-verbatim, what's already in the sent PDF** — the two mystery-shop findings and Gino's own quotes. That continuity is exactly right and should not change.
- **The SOW's Exclusions and Client Responsibilities sections are the right sections in the right document** — most first-draft SOWs skip both, and skipping them is what produces scope creep arguments later.
- **The delivery sequence (Section 04 of the Proposal) matches the "controlled execution, not instant rollout" instinct** already on record in `taste-n-judgement.md` §7.
- **No fabricated case studies, no named team bios inflating credibility** — correctly consistent with "you have none, say so" (`LEGAL-AND-COMMERCIAL-DOC-SET.md` §4.2) and "don't name individuals unnecessarily" (`taste-n-judgement.md` §1).

---

## 7 · Against the industry-standard professional-services proposal format

| Standard section | Present? | Note |
|---|---|---|
| Cover | ✅ | Both docs |
| Current-state / problem framing | ✅ strong | Section 01 — evidence-based, ties to what's already landed |
| Proposed solution / deliverables | ⚠️ | Present but scope has drifted from what was promised — see §1 |
| Methodology / delivery process | ✅ | Section 04 — standard 5-step shape, good |
| Timeline | ✅ (SOW only) | Specific, dependency-flagged. Fine to omit from the Proposal |
| Team / credentials / case studies | — (deliberate) | None exist; correctly not fabricated. Standard practice would be one honest line ("we're early — here's how that shapes the terms") rather than silence, matching the "volunteered, not extracted" positioning already in `SALES_MOTION.md` |
| Commercials | *(deferred — out of scope for this pass)* | — |
| Assumptions / dependencies | ❌ | Required by your own doctrine for this specific deal — see §4 |
| Out-of-scope / exclusions | ✅ | SOW Exclusions section — correctly present, often skipped by agencies |
| Client responsibilities | ✅ | SOW — good, standard, often skipped |
| Validity / expiry | ❌ | Missing — see §4 |
| Terms (liability, IP, confidentiality, medical disclaimer, indemnity) | — | Correctly belongs in a separate Services Agreement per `LEGAL-AND-COMMERCIAL-DOC-SET.md` §5, not the SOW. **Confirm that document exists or is in progress** — a signed Proposal + SOW with no MSA behind it leaves the liability cap and medical disclaimer unwritten, which matters more than usual given Valence Ops is a sole proprietorship with personal, unlimited liability |
| Next steps / signature | ✅ | Both — clean |

**Overall shape is closer to standard practice than most first drafts get, particularly the exclusions and client-responsibilities sections.** The gaps are concentrated in the two places that carry real risk if you ship them as-is: the scope that quietly moved (§1), and the compliance claim that isn't backed by how the systems actually work (§2).

---

## 8 · Recommended order of fixes

| # | Fix | Cost |
|---|---|---|
| 1 | Decide on Booking — add it back priced, or state explicitly why it's deferred | Real decision, not a copy edit |
| 2 | Replace the PII/DPDP paragraph with the five commitments from the sent PDF, verbatim | 10 minutes |
| 3 | Hedge or confirm the attribution claim before it ships as delivered scope | Needs Adi's answer either way |
| 4 | Decide whether Reactivation/Quote-Follow-up/Reviews ship now as priced systems or move to a named "Phase 2" | Real decision |
| 5 | Add an Assumptions Schedule + re-scope trigger (can be one page, attached to the SOW) | 30–45 minutes, template exists in `LEGAL-AND-COMMERCIAL-DOC-SET.md` §3A.4 |
| 6 | Add a validity date to the Proposal | 1 line |
| 7 | Confirm a Services Agreement is being drafted alongside this, or flag it as the next document | Scheduling, not drafting |
| 8 | Em dashes, "Confidential" footer — batch into the design pass | Cheap, can wait |
