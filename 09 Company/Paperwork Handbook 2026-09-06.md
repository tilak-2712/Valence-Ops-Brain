---
date_created: 2026-09-06
date_modified: 2026-09-06
status: active
---
# Paperwork Handbook — every document, what it does, how long it lives

**Written 2026-09-06.** Written for someone new to the agency side. Plain language, examples, no assumed knowledge.
**Not legal advice.** Three items need a CA or a lawyer to sign off and are flagged inline.

**Related existing file:** `Legal and Commercial Doc Set.md` (written 2026-08-20) already covers the entity position, GST analysis and stage-by-stage document list in more depth. This handbook is the beginner-level explainer and the format audit of what has already been sent. Where the two overlap, that file is more detailed and this one is more readable.

---

## 0 · The one mental model that makes all of this simple

Every agency contract set is **two layers**.

**Layer 1 — the rules layer.** How we work together, whatever the job is. Payment terms, who owns what, what happens if it goes wrong, how either side exits. Signed **once** per client. Almost never changes.

**Layer 2 — the job layer.** What we are actually building this time, for how much, by when. Signed **per project**. Changes often.

The whole point of separating them is that when the clinic asks for a second system in March, you write one new job-layer page and send it. You do not reopen the contract, and nobody's lawyer gets involved again.

**Analogy.** Layer 1 is the rental agreement for a shop — deposit, notice period, who fixes the plumbing. Layer 2 is what you sell in the shop this month. You do not renegotiate the lease to change the stock.

Everything below is either Layer 1, Layer 2, or a supporting document that hangs off one of them.

---

## 1 · Answer: do proposals need a serial number?

**Not mandatory. Nothing legal turns on it. The three already sent are fine and do not need reissuing.**

The confusion is worth clearing up because two different documents get called "a number":

| | **Invoice number** | **Proposal reference** |
|---|---|---|
| Required by law? | **Yes** — must be sequential and unbroken | **No** — purely your own convenience |
| Why | It is an accounting record. Tax authorities expect an unbroken series | Version control only |
| Consequence of not having it | Real, at audit | You lose track of which version is live |

**But you should start using one anyway, and here is the actual reason — not a legal one.**

SkinFit has received, between 22 and 30 August, documents titled:

- Patient Communications Proposal
- Scope of Work
- Patient Communications Proposal v2
- Enquiry System Strategy
- Patient Conversion System
- Patient Conversion and Intelligence System
- Patient Conversion Proposal

Seven differently-named documents to one clinic in nine days. **Right now neither you nor SkinFit can say which one is the live offer.** If they come back in October saying "you quoted us ₹65,000," you have no way to point at a specific document and say *this* one, dated *this*, superseded by *that* one. That is the problem a reference number solves.

**Suggested format**, and keep the three series completely separate so they never get confused:

```
Proposals:  VO-P-2026-004
Contracts:  VO-A-2026-002
Invoices:   VO/2026-27/001
```

Invoices restart at 001 each financial year (1 April). Proposals and contracts can run continuously.

**Where it goes on the page:** small, in the footer or under the date on the cover. Alongside it put a version line — *"Version 2 · supersedes VO-P-2026-002 dated 22 August 2026."* One line, and the ambiguity disappears permanently.

**Do:** put the number on the cover and in the footer of every page.
**Don't:** reuse a number for a revised version. A revision gets a new number and names what it supersedes.
**Don't:** number proposals in the same series as invoices. An accountant seeing "Invoice 004" and "Proposal 004" will assume they are related.

---

## 2 · Format review of the three proposals actually sent

### 2.1 Is the commercials section in the right place?

**Yes. Do not move it. It is already correct in all three.**

Checked against the documents themselves:

| Proposal | Total pages | Commercials on page | What follows it |
|---|---|---|---|
| Aurilueur | 9 | 8 | Next steps |
| SkinFit v2 | 9 | 7 | What it runs on, next steps |
| RUA | 11 | 8 | What it runs on, usage costs, next steps |

So the price is not on the last page in any of them — it is near the end with a next-step page after it. **That is the right structure and it is worth understanding why**, because it is a real principle rather than a formatting preference.

A price read before the value is understood is just a number, and the reader's only available reaction is "that seems like a lot." A price read after seven pages describing the work has context. And the page *after* the price matters just as much: if the price is the last thing on the page, the last emotion is cost. If a "here's what happens next" page follows it, the last emotion is momentum.

**Keep this shape:** what we found → what we would build → how we start → what it costs → what happens next.

### 2.2 What is actually wrong — seven fixes, ordered by how much they cost you

**1 · No payment terms anywhere. This is the biggest gap by a distance.**

Not one of the three says when money is due. Aurilueur has a real, acceptable number — ₹40,000 one-time and ₹18,000 a month — and if they say yes tomorrow, nobody knows whether the ₹40,000 is due on signature, on go-live, or split.

That question then gets negotiated **after** the yes, which is the worst possible moment: you have psychologically already won, so you concede. Decide it now and print it.

Standard and defensible for your size:

> Setup fee: 50% on signing, 50% on the first system going live.
> Monthly fee: billed in advance on the 1st, payable within 7 days.
> Payment by bank transfer to the account named on the invoice.

**2 · No validity date on two of three.** Aurilueur says *"Valid until 30 September 2026"* — correct. SkinFit and RUA say nothing. An offer with no expiry stays open. If RUA resurfaces in February and says "we'll take the ₹65,000 one," you are in an argument you should never have been able to have. Every proposal gets an expiry, 21 to 30 days out. It also creates honest urgency without a single pushy sentence.

**3 · No legal identity block.** None of the three states who you legally are. "Valence Ops" appears as a brand name in a header and nowhere else. Missing: the proprietor's name, the registered address, PAN, Udyam number, phone, email.

This matters at a specific moment. When a clinic says yes, their accountant opens you as a vendor and needs exactly these fields. If they are not in the proposal, someone emails you asking, and you look like you have not done this before. **Add a small block on the back page:**

> Valence Ops · Proprietor: S Tilak
> [registered address]
> PAN: XXXXXXXXXX · Udyam: UDYAM-KR-03-0707297
> [email] · [phone]

Note that this is a sole proprietorship, so the PAN is Tilak's personal PAN. That is correct and normal — it is not a gap, and putting it on the document pre-empts the question. There is **no CIN**, because there is no company. Never let a template print one.

**4 · Inconsistent tax wording.** Aurilueur says *"exclusive of GST and other applicable taxes."* SkinFit and RUA say *"exclusive of applicable GST."*

Use the Aurilueur wording everywhere. The longer phrase covers you if any other levy applies, and — more importantly — if you register for GST in the middle of an engagement, you can start adding it to the invoice without renegotiating the price. The narrow version invites the argument.

**5 · No exit or notice terms on the monthly fee.** A recurring fee with no stated notice period is ambiguous in both directions: they may think they can stop instantly, you may think you are owed the month. One line fixes it: *"Monthly, no lock-in. Either side may end with 30 days' written notice."* The absence of a lock-in is a selling point — say it out loud rather than leaving it unsaid.

**6 · Two of three are not actually quotes, and it is worth being clear-eyed about that.** SkinFit and RUA give ranges (₹65,000–₹1,00,000 build; ₹25,000–₹45,000 monthly) and explicitly say *"preliminary estimates, not a quotation."* That is honest and correct for their stage. But it means **only Aurilueur has a number that can be accepted.** Do not count three live quotes in your own head when you have one.

**7 · The Aurilueur discount framing — this one is a judgement call and I think it is wrong.**

The page currently reads: **Listed ₹90,000 · Founding client waiver −₹50,000 · ₹40,000 one time.**

Three problems.

- **A 56% discount makes the ₹90,000 not credible.** A number nobody has ever paid is not a list price, and a reader who senses that starts wondering what else is padded.
- **You have anchored yourself at ₹40,000 for every clinic that Aurilueur ever speaks to.** Indiranagar clinic owners know each other. The founding-client rate becomes the rate.
- **A discount given for nothing reads as needing the deal.** A discount given *in exchange for something* reads as a trade between equals.

**The fix, and it is a small edit:** keep the ₹40,000, drop the strike-through, and attach a condition. *"₹40,000 as our founding client rate. In exchange we would ask for a reference call with one clinic and permission to describe the results once the systems have been running three months. This rate holds until 30 September."* Same money. Completely different signal — and you get an asset you currently have none of, which is a reference.

If Tilak has already sent this and wants to keep the waiver framing, that is his call and it does not need undoing mid-conversation. It applies from the next proposal.

### 2.3 One thing already right that should be protected

Aurilueur ends the commercials page with: *"Full scope and terms would be set out separately before anything starts."*

Keep that sentence in every proposal from now on. It is the hinge that lets the proposal stay readable and short while the contract does the heavy work. Without it, a clinic can reasonably argue the proposal *was* the whole agreement.

---

## 3 · Every document, explained from zero

For each: what it is, an example, who signs, when, how long it lasts, what is locked and what can move.

### 3.1 Proposal / Quote — *Layer 2, pre-signature*

**What it is.** An offer. "Here is what we would build, and what it would cost." It is a sales document, not an accounting document and not a contract. Nobody owes anybody anything because a proposal exists.

**When it becomes binding.** The moment they accept it in writing *and* it is attached to a signed contract. Until then it is a document you can withdraw or revise freely.

**Lifespan.** Until the validity date. That is the entire reason the validity date exists.

**Locked once accepted:** the price, the scope, the timeline commitments.
**Free to change before acceptance:** everything. Revise as often as you like — just issue a new reference number that names what it supersedes.

**Do:** one price, one validity date, one clear next step.
**Don't:** put payment mechanics in a proposal and nowhere else — they need to end up in the contract too, and the contract wins if they disagree.
**Don't:** let a proposal do the contract's job. It cannot cap your liability, protect your IP, or govern data.

### 3.2 NDA — *supporting, usually pre-contract*

Covered fully in §4 below, since you asked about it specifically.

### 3.3 Services Agreement / MSA — *Layer 1*

**What it is.** The rulebook. Signed once per clinic, covers every project you ever do for them.

"MSA" stands for Master Services Agreement. "Master" only means *it sits above the individual jobs*. It does not mean long or complicated. Six readable pages beats twenty that go to a lawyer and come back in three weeks.

**Analogy.** The terms and conditions of a mobile network. You sign them once. You then change your plan every year without re-signing them.

**Who signs.** You: *"S Tilak, Proprietor, for Valence Ops."* Them: **someone with authority to bind the clinic** — a director, a partner, or the proprietor. This matters more than it sounds. If a marketing head signs without authority, you may hold a contract you cannot enforce against the clinic. Ask, politely, who signs — it is a normal question.

**Lifespan.** From the effective date until either side terminates. Typically monthly rolling with 30 days' notice, so it just continues until somebody stops it.

**What must be inside it, in plain terms:**

| Clause | What it actually means |
|---|---|
| Parties | Exactly who is contracting. Ask for the clinic's legal entity name — it is often different from the brand on the door |
| Term and notice | How long, and how either side gets out |
| Fees and taxes | Amounts, when due, "exclusive of GST and other applicable taxes" |
| TDS | They will deduct tax at source and must give you the certificate. See §6 |
| Late payment | Interest after N days, and your right to pause the service |
| Third-party costs | Meta charges, hosting, AI usage. Whose card, and passed through at cost |
| IP and ownership | **Their data is theirs. Your system is yours, licensed to them for the term.** Do not hand over IP on client one |
| Confidentiality | Mutual, and it survives the contract ending |
| Compliance | You operate within Meta and WhatsApp policy; they warrant the contacts they give you were lawfully obtained. This clause is what protects you if a clinic hands you a bought list |
| Medical disclaimer | Nothing automated gives medical advice. No message goes out in a doctor's name without approval. Non-negotiable in this vertical |
| Liability cap | Your maximum exposure, capped at fees paid in the last N months. **The single most important clause in the document for you** — see the warning below |
| No outcome guarantee | You promise what you will *do*, never a patient count or a revenue number |
| Termination | For convenience with notice; for cause on breach with a chance to fix it first |
| Exit | Data export format, deletion timeline, access revoked. Write the divorce while everyone is friendly |
| Governing law | Bengaluru, Karnataka |

**The liability warning.** Valence Ops is a sole proprietorship, which means there is no company shell between the business and Tilak personally. An uncapped liability runs straight at his own assets. So the liability cap is not boilerplate — it is the only protection there is. If a clinic's lawyer sends back a redline removing or widening it, that is not a small change and it should not be waved through.

**Locked — changeable only by a signed written amendment:** parties, fees, term and notice, IP ownership, liability cap, governing law, medical disclaimer, confidentiality.
**Not locked:** the scope. Scope lives in the SOW precisely so it can move without touching this.
**How to change it:** a one-page "Amendment No. 1," signed by both, saying which clause is replaced and with what. You do not rewrite and re-sign the whole agreement.
**How often it should change:** almost never. If you are amending an MSA more than once a year, something is in the wrong layer.

**Two terms worth knowing:**
- **Survival.** Some clauses keep working after the contract ends — confidentiality, data deletion, liability. That is deliberate.
- **Entire agreement clause.** Standard wording saying the signed documents are the whole deal and nothing said in a meeting counts. This is precisely why the proposal must be *attached* to the contract. If it is not attached, the entire agreement clause quietly deletes it.

**Stamp duty.** In Karnataka an agreement like this typically needs a small e-stamp (in the region of ₹200). Unstamped does not make the contract void, but it cannot be produced as evidence in court until the duty and a penalty are paid. Cheap to do, annoying to fix later. `verify` the current amount with your CA or the e-stamping portal.

### 3.4 Scope of Work / SOW — *Layer 2, the workhorse*

**What it is.** What you are building, for how much, by when, and what you are explicitly *not* building. It attaches to the MSA as "Schedule A."

**"Schedule" and "Annexure" mean the same thing:** an attachment that is legally part of the contract. The value of the structure is that you can replace Schedule A without reopening the agreement.

**Example.** Aurilueur signs an MSA once. Schedule A covers the three systems in the current proposal. In February they want quote follow-ups added — that is **Schedule A-2**, one page, signed. The MSA is untouched.

**Usually the SOW just *is* the proposal**, attached and signed. That is normal practice and it saves you writing the same thing twice.

**Lifespan.** Until the work in it is delivered and accepted.

**The most important section is the out-of-scope list**, and beginners always underweight it. Name explicitly: no medical advice, no changes to their patient records system, no ad creative or media buying, no clinical content, no managing their availability. Every item on that list is an argument you have pre-won.

**Locked:** deliverables, price, timeline, dependencies.
**Changeable:** only through a change request (§3.8) or a new SOW. Never by a WhatsApp message saying "sure, we can add that."

### 3.5 Assumptions Schedule — *Layer 2, attached to the SOW*

**What it is.** A list of every fact you were told but have not personally verified, and which the price depends on.

**Why it exists.** Look at the Aurilueur proposal — it already contains this paragraph: *"What this assumes: that your WhatsApp line can sit on the official WhatsApp Business platform, that we are given access to your Meta business accounts, that your CRM allows us to read and write to it..."*

That is an assumptions schedule already written. It just needs to become a signed page instead of a paragraph.

**The mechanism, and this is the part that matters.** Pair the list with a **re-scope trigger**: *"If any listed assumption is materially different at onboarding, scope and price are revisited before build starts. Both sides have five working days to agree a revision, and either side may exit cleanly if we cannot."*

Without that clause you have fixed a price against facts nobody checked. If Aurilueur's CRM turns out to be read-only, the automated CRM entry — one of three systems you sold — cannot be built, and you are contractually obliged to deliver it for ₹40,000.

**Lifespan.** Dies at the end of onboarding, once each assumption is confirmed or corrected. Keep the signed copy.

### 3.6 DPA — *Layer 1, attached as a schedule*

Covered fully in §5.

### 3.7 SLA — *Layer 1, attached as a schedule*

**What it is.** Service Level Agreement. The promises about responsiveness, in both directions.

**Your side:** support hours, how fast you respond to a broken system, escalation contact and number.
**Their side — and do not skip this:** the clinic must reply to routed patient messages within a stated window, say four business hours.

**Why theirs matters more than yours.** Your system hands a booking request to their front desk. If the desk ignores it for two days, the patient's experience is worse than before you existed, and it will be described as "your system not working." The SLA is where you write down that the human step is theirs.

Pair it with a **stop clause**: three routed patient replies unanswered beyond 48 hours pauses the service. That protects both sides — you from being blamed, them from a silent failure running for weeks.

**Lifespan.** Same as the MSA.
**Revisable:** yes, and more easily than the MSA, because it is a schedule. Realistic thresholds are hard to guess before client one; expect to revise after the first three months. Say so in the document — *"reviewed at the end of the first quarter"* — so revising it later is planned rather than a climbdown.

### 3.8 Change Request — *Layer 2, ongoing*

**What it is.** One page. What is being added, what it costs, what it does to the timeline, signed by both. Then it gets built.

**The example that makes it obvious.** Month two, the clinic asks: "Can it also message people who came for a consultation last year?" That is reactivation — a system that is explicitly *not* in the Aurilueur scope. Without a change request, you either say no and look rigid, or say yes and do a week of unpaid work. With one, you say "yes, here's the page, ₹X, adds two weeks" and it becomes a normal business decision instead of a favour.

**The mechanism to actually make it work:** everything outside Schedule A gets logged, priced and signed **before** it is built. Not after. Once built, you have no leverage.

**Lifespan.** Once signed it becomes part of the SOW permanently.

**Do:** use it even for free changes — write ₹0 and note why. It records that a thing had a value and you chose to give it.
**Don't:** accept scope changes over WhatsApp voice notes. Repeat it back in writing at minimum.

### 3.9 Acceptance / Go-live sign-off — *Layer 2, one moment*

**What it is.** A short written confirmation from the clinic that what was promised is delivered and working.

**Two jobs.** It triggers the final payment milestone, and it closes the door on "just one more tweak" continuing forever.

**Do:** make it a friendly email they reply to, not a formal form. *"System 01 is live as of today, here's what it does, please confirm this matches what we agreed."* A reply saying "yes, looks good" is enough.
**Don't:** let a build stay open-ended. Unclosed projects are how a fixed-fee build turns into six months of unpaid support.

### 3.10 Invoice — *the money document*

Covered fully in §6.

### 3.11 Meta / WhatsApp authorisation letter — *supporting, at onboarding*

**What it is.** A letter on the **clinic's** letterhead, signed by them, stating that Valence Ops is authorised to manage their WhatsApp Business Account and Meta assets on their behalf.

**When you will wish you had it.** The WhatsApp number gets restricted on a Sunday. You contact the provider. The first thing they ask is whether you are authorised to act for that business. Without the letter, only the clinic can raise the ticket, and the clinic is closed.

**Do:** collect it at onboarding with everything else, not when something breaks.
**Do:** get written confirmation of **who owns the WhatsApp number and the Facebook page.** If a previous agency owns those assets, you want to discover that in week zero, not week two.

### 3.12 Runbook / handover doc — *delivery, ongoing*

**What it is.** Written instructions: how the system works, what to do when it breaks, who owns what.

**Why it is commercial and not just tidy.** Front desk staff turn over constantly at clinics. Six months in, the person you trained has left, the new person does not know the system exists, and the clinic concludes it does not work. The runbook is what survives staff turnover — and it is also the concrete thing that justifies charging ₹18,000 a month rather than a one-time build fee.

**Lifespan.** Living document, updated whenever the system changes.

### 3.13 Case study / logo consent — *after go-live*

**What it is.** Written permission to name the clinic and describe results publicly.

**When to ask:** at go-live, or at the first good result, while goodwill is at its peak. Six months later, in a quiet month, the answer is often no.

You currently have zero references and zero case studies, which is the single biggest missing asset in every sales conversation. Getting one is worth more than a price increase.

---

## 4 · The NDA question — who issues it?

**Either side. It makes no legal difference who drafts it. Both approaches are completely normal.**

**If the clinic has their own:** use theirs. Accepting a counterparty's paper on a low-stakes document is good practice — it costs nothing and it signals you are not difficult. Have it checked, and check these five things specifically:

1. **Is it mutual or one-way?** A one-way NDA protects only *their* information. You are also sharing something — your method, your pricing, how the system works. If it is one-way against you, ask for it to be made mutual. That is a routine request and nobody takes offence.
2. **How is "confidential information" defined?** It should carve out things you already knew, things that are public, and things you develop independently. Without those carve-outs you can theoretically breach it by knowing something you knew before you met them.
3. **How long does it run?** Two to three years after the relationship ends is normal. Perpetual is a red flag — except for patient data, where perpetual is correct and you should not argue.
4. **Is there a non-solicit hiding in it?** A clause saying you cannot hire their staff. Usually harmless, but know it is there.
5. **Is there a non-compete disguised as an NDA?** Wording that stops you working with other clinics, or other clinics in the same area. **Refuse this.** It is not what an NDA is for, and accepting it would end your business. It is rare but it does appear in templates.

**If they do not have one:** you issue a two-page mutual NDA. Get a template drafted once by a lawyer and reuse it forever — this is one of the cheapest legal spends there is.

**Small advantage in drafting it yourself:** whoever writes it sets the defaults. But it is genuinely small, and it is not worth creating friction over.

**Timing — and this is the part people get wrong.** Do not lead with an NDA. Sending one to a clinic that has not agreed to anything reads as a vendor protecting itself before doing any work, and it introduces a document into a conversation that was going fine.

**Send it when either of these is true:** they ask for one, or you are about to receive something genuinely sensitive from them — their conversion rates, pricing structure, staff costs, or access to their systems.

**Once the MSA is signed, the NDA becomes mostly redundant**, because the MSA has its own confidentiality clause covering the same ground. That is fine. It is a bridge document for the gap between "interested" and "signed."

**Correcting what I said last message:** I put the NDA in Tier 1 as something to have before your first client. More precisely — **have it drafted and ready, but do not send it by default.** Ready is Tier 1; sending is on demand.

---

## 5 · DPA, explained properly

### 5.1 What it is

**Data Processing Agreement.** A written agreement about how you handle personal data that belongs to someone else's customers.

**The analogy.** The clinic owns a filing cabinet full of patient details. They hire you to sort and organise it. The DPA is the written instruction sheet taped to the cabinet: which drawers you may open, which you may not, what you may do with what you read, who else you may show it to, and what happens to your key when the job ends.

### 5.2 Why it is not optional

India's **Digital Personal Data Protection Act 2023 (DPDP)** defines two roles:

- **Data Fiduciary** — the party that decides *why* personal data is collected. That is the clinic.
- **Data Processor** — the party that handles it on the Fiduciary's instructions. That is you.

The Act says a Fiduciary may engage a Processor **only under a valid contract**. So the DPA is not politeness — without it, the clinic's use of you is not compliant. You are handing them the thing they need to be legal.

`verify` the current phase-in position with counsel. The Act is in force with obligations rolling in, and the older IT Act rules still treat health data as sensitive personal data today. The direction is not in doubt; the exact deadlines are.

**And the sales point, which is real:** almost no small agency in this space hands a clinic a DPA unprompted. Doing it makes you the serious option in a category where the alternative is a freelancer with a chatbot. It is the cheapest credibility you can buy.

### 5.3 What actually goes in it

**1 · Categories of data.** Names, phone numbers, message history, stated treatment interest, appointment status.

**And explicitly: not medical records.** This one sentence is the most reassuring thing in the whole document to a doctor. Say it in the proposal too. The Aurilueur proposal already says the system "does not give medical advice" — this is the data-side twin of that sentence.

**2 · Purpose limitation.** The data is used only to operate the enquiry-handling system for that clinic. Nothing else.

**Include one sentence that will become important:** you do not use their patient data to train models, to build anything for another client, or for your own purposes. Write it plainly. If a clinic ever asks whether their data is training an AI, "no, and here is the clause" is a much better answer than an explanation.

**3 · Sub-processors, named.** Everyone else who touches the data. From the proposals already sent, that list is roughly: Meta / WhatsApp, the BSP if one is used, Supabase, Hostinger, Sarvam, and Exotel where voice is in scope.

**Why naming them matters:** a clinic will eventually ask "where does our patient data actually sit?" and "I'm not sure" is a bad answer to a doctor about patient information. Writing the list once means you never have to improvise it.

**Include an add-notice clause:** *"We will notify you 14 days before adding a new sub-processor."* This is the DPA's main revision trigger, and this clause is what lets you change your stack without renegotiating.

**4 · Cross-border position.** Some of that stack is hosted outside India. Say so honestly. DPDP permits transfer except to territories the government restricts, so this is not a problem — it is only a problem if you are vague about it and their lawyer finds it.

**Do not** promise data stays in India unless your entire stack is Indian. It is not, and it is an easy promise to break by accident.

**5 · Security measures.** Access control, encryption in transit, and who on your side can see what. Keep it honest and specific to what you actually do. An overstated security section is worse than a modest one, because it is a warranty.

**6 · Breach notification.** If something goes wrong, you tell them within N hours of becoming aware. 24 or 48 hours is normal. Pick one you can actually meet.

**7 · Retention and deletion.** How long you hold data, and what happens at the end.

**The trap here:** do not agree to delete within 24 hours if your backups run on a 30-day cycle. You will breach it without knowing. Write what your systems actually do — *"deleted from live systems within 7 days, purged from backups within 30."*

**8 · Their rights.** They can ask for a report on how their data is handled, and they can ask you to delete it. Both are reasonable and cost you nothing to grant.

**9 · Their warranty back to you — do not leave this out.** The clinic warrants that the contacts they hand you were lawfully obtained and have a basis for being messaged.

**Why:** if a clinic gives you a purchased list of 5,000 numbers and you message them, the exposure lands on you. This clause moves it back where it belongs. It is the DPA clause that protects *you* rather than them, and it is the one most often missing.

**10 · What happens on exit.** Their data is exported to them in a usable format, your access is revoked, and their copy is deleted on the stated timeline.

### 5.4 Lifecycle

**Signed:** with the MSA, as Schedule B. Same signature, same moment.
**Lasts:** as long as the MSA, plus a tail — the deletion and confidentiality obligations survive termination. That survival is the point.
**Revised when:** you add or change a sub-processor (the common case), your security setup materially changes, or the law changes. Not on a schedule.
**Locked:** the purpose limitation, the no-independent-use clause, and the deletion commitments. These should never loosen over time.
**Movable:** the sub-processor list, security specifics, notification windows.

---

## 6 · Billing with no GST registration — quote vs bill vs invoice

### 6.1 Three different documents at three different moments

New people conflate these constantly. They are not versions of each other.

| | **Quote / Proposal** | **Invoice** | **Receipt** |
|---|---|---|---|
| What it says | "This is what it would cost" | "This amount is now due" | "We received your money" |
| When | Before yes | After yes | After payment |
| Is it an accounting record? | No | **Yes** | Minor |
| Numbering required? | No | **Yes — unbroken sequence** | No |
| Can it be revised? | Freely | **Never — issue a credit note instead** | No |

**"Bill" and "invoice" mean the same thing** in ordinary Indian usage. Under GST, an unregistered seller's document is formally called a **Bill of Supply** rather than a Tax Invoice — but titling it "Invoice" is fine and universally understood.

### 6.2 The direct answer to your question

**Keep the commercials inside the proposal. That is your quote. It is working. Do not split it.**

**Then, when they say yes, raise a separate invoice.** Not because the proposal is wrong, but because a proposal structurally cannot be an invoice: an invoice has to be numbered, dated, addressed to a legal entity, and bookable by their accountant. A nine-page design document is none of those things, and their accounts team cannot process it.

So the flow is:

```
Proposal (with commercials inside)  →  they say yes
     →  MSA + SOW signed
     →  Invoice #1 raised for the setup fee
     →  payment received  →  receipt
     →  monthly invoices from go-live
```

Three documents, three moments. The proposal never becomes the invoice.

### 6.3 What the invoice must look like without GST registration

**Must have:**
- Title: **"Invoice"** or **"Bill of Supply."** **Not "Tax Invoice"** — that phrase is reserved for registered sellers.
- Invoice number, sequential and unbroken. Suggested: `VO/2026-27/001`, restarting at 001 each 1 April.
- Date.
- Your details: *Valence Ops (Proprietor: S Tilak)*, registered address, PAN, Udyam number, email, phone.
- Their details: the clinic's **legal entity name** and address — not the brand on the signage.
- Description of what is being charged, and the period it covers.
- Amount, in words and figures.
- Bank details for payment.
- The line: **"Not registered under GST."**

**Must NOT have:**
- Any GST amount. Any GST percentage. Any GSTIN.
- The words "Tax Invoice."

**This one is not a formatting nicety.** Charging or showing GST without a registration is an offence, not a technicality. Never let a template carry a tax line "for now."

**Two things worth adding deliberately:**

**PAN.** It is Tilak's personal PAN because a proprietorship has no separate one. An accountant expecting a company PAN may query it — putting it on the invoice labelled clearly as *"Valence Ops (Proprietor: S Tilak) · PAN: XXXXXXXXXX"* means the question never arises.

**Udyam number.** Registered micro-enterprise status obliges the buyer to pay within 45 days under the MSMED Act. Printing the number on the invoice is free leverage with a clinic that drifts on payment, and it costs you a line of text.

### 6.4 TDS — the thing that will confuse you on the first payment

You will invoice ₹40,000 and roughly ₹36,000 will arrive. **Nothing has gone wrong.**

The clinic is legally required to deduct tax at source and deposit it with the government against your PAN. That deducted amount is your tax credit — it appears in your Form 26AS and reduces what you owe at year end. It is not a discount and not a shortfall.

**What to do:**
- Expect roughly 10% deduction. `verify` with a CA whether your service falls under Section 194J (professional/technical) or 194C (contract) — the rates differ materially and it affects what you should expect.
- Put a clause in the MSA requiring them to issue **Form 16A** quarterly. That is the certificate proving the deduction was actually deposited.
- Chase it. Reconstructing a missing Form 16A a year later is a genuine cost in time.

### 6.5 One flag worth knowing about, out of scope here

The existing file `Legal and Commercial Doc Set.md` §9 argues for registering for GST voluntarily even below the ₹20 lakh threshold. The short version of the argument: while unregistered, the 18% you pay on foreign platforms — Meta, hosting, AI APIs — is an unrecoverable cost, whereas registered you claim it back. Being unregistered is costing you money rather than saving it.

That is a decision for a CA conversation, not a paperwork decision. But it is directly relevant the moment real monthly platform spend starts.

---

## 7 · The Tier 2 and Tier 3 documents, in plain English

Same documents as before, with the jargon stripped out and the moment each one saves you named.

| Document | In one plain sentence | The day it saves you |
|---|---|---|
| **Onboarding / access checklist** | The list of logins, numbers and accounts you need before you can build anything | Day one. Without it you discover in week two that the WhatsApp number is registered on the personal app and cannot be migrated for ten days |
| **WhatsApp authorisation letter** | A letter from the clinic saying you are allowed to manage their WhatsApp and Meta accounts | The Sunday the number gets restricted and the provider asks who you are. Without it, only the clinic can raise the ticket, and the clinic is closed |
| **Change request form** | One page saying "you asked for X, it costs Y, it adds Z weeks — sign here" | Month two, when they ask for a fourth system. Turns a favour into a decision |
| **Go-live sign-off** | An email where they confirm the thing works as agreed | When you want the final payment, and when you want the tweaking to stop |
| **SLA** | Written promises about speed — yours to them, and theirs to patients | The month a booking request sits unread at the front desk for two days and the clinic says your system does not work. The SLA is where it says the human step was theirs |
| **Runbook** | Written instructions for how the system works and what to do when it breaks | Six months in, when the staff member you trained has left and the new one does not know it exists |
| **Offboarding terms** | What happens to their data and your access when it ends | The day someone leaves. Best written while everyone still likes each other |
| **Case study consent** | Written permission to say who they are and what happened | Every future sales conversation. You currently have zero references, which is the single biggest missing asset in the pitch |

---

## 8 · Locked vs revisable — the summary table

| Thing | Locked or movable | How it changes | When |
|---|---|---|---|
| Parties, legal names | **Locked** | Signed amendment | Only if the entity changes |
| Fees for the current term | **Locked** | Signed amendment | Not mid-term on client one |
| Fees at renewal | Movable | 30 days' written notice before renewal | Once a year, at most |
| Term and notice period | **Locked** | Signed amendment | Rarely |
| IP ownership | **Locked** | Signed amendment | Never, ideally |
| Liability cap | **Locked** | Signed amendment | Never accept a widening without understanding it |
| Medical disclaimer | **Locked** | — | Never |
| Governing law | **Locked** | Signed amendment | Never |
| Scope of work | Movable | New SOW or change request | As often as needed |
| Message wording and flows | Movable | Just agree it — it is operational | Continuously |
| SLA thresholds | Movable | Schedule replacement | Review after the first quarter |
| Sub-processor list | Movable | 14 days' notice to the client | When the stack changes |
| Rate card for extras | Movable | Notice at renewal | Annually |
| A proposal not yet accepted | Movable | New reference number, naming what it supersedes | Freely |
| A proposal already accepted | **Locked** | It is now the SOW; use a change request | — |
| An issued invoice | **Locked** | Credit note, then a fresh invoice | Never edit or delete one |

**Two rules underneath the whole table:**

1. **Nothing changes retroactively.** Not an invoice, not an accepted proposal, not a signed scope. You supersede forward with a new document that names the old one. You never quietly alter the old one.
2. **Price is fixed for the term you sold, and revisable at renewal.** Do not put a mid-term escalation clause in your first client contract. It buys you very little and it reads badly.

---

## 9 · What is actually urgent

Ordered by consequence, not by tidiness.

| # | Do this | Why now |
|---|---|---|
| 1 | **Decide the payment terms and put them in the next proposal** | Aurilueur has a live quote valid until 30 September. If they say yes, you are negotiating money terms from the weak side of a "yes" |
| 2 | **Get an MSA + SOW + DPA drafted and reviewed once by a lawyer** | Same reason. A yes from Aurilueur today meets an empty shelf. This is roughly two weeks including a review pass |
| 3 | **Build the unregistered invoice template** | You cannot take the first payment cleanly without it. Half a day |
| 4 | **Start proposal reference numbers, and add a validity date + identity block to the template** | Cheap, permanent, and fixes the SkinFit version confusion going forward |
| 5 | **Decide whether to keep the Aurilueur discount framing** | Applies from the next proposal, not retroactively |
| 6 | **Draft a two-page mutual NDA and leave it in a folder** | Zero urgency, but you never want to be writing one while a clinic waits |

**One honest note on sequencing.** Items 1–3 are the real work and they are the only things standing between a yes and a mess. Items 4–6 are improvements. If time is short this week, doing 1–3 properly and none of the rest is the right call.


---
Related: [[09 Company/Legal and Commercial Doc Set|Legal and Commercial Doc Set]] · [[04 Clients/SkinFit Wellness/SkinFit Wellness|SkinFit Wellness]] · [[04 Clients/Aurilueur Esthetic Clinic/Aurilueur Esthetic Clinic|Aurilueur Esthetic Clinic]] · [[04 Clients/RUA Skin and Hair Center/RUA Skin and Hair Center|RUA Skin and Hair Center]]
