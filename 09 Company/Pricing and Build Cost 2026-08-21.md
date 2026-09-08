---
date_created: 2026-09-05
date_modified: 2026-09-08
status: active
---
# Build cost and pricing model — the six-system stack

**Date:** 21 August 2026 · **Status:** `provisional` throughout except the vendor rates in §2, which are `confirmed` from published price lists (sources at the end). Nothing here has been tested on a client. **Zero calls held, zero pilots, one live proposal.**

**Revised 2026-08-22 (Tilak, decisions on the Codex draft quote) — see §7 for what's now resolved.** Confirmed: Hostinger and Supabase absorb into the retainer/build fee, not billed to the client (the original §2.1 fixed/volume split holds, not Codex's version). No CRM naming or mapping in the build — integration is via the client's own CRM API key, whatever the CRM is, which also sidesteps the Cliniko-naming risk entirely rather than just avoiding the word. Sarvam is the confirmed conversational-AI vendor for the qualification bot and for user-initiated Instagram/Messenger conversations — this also confirms Messenger + Instagram DM are in scope (§7 open item, resolved). GST: quote language is "exclusive of GST and other applicable taxes" everywhere, never a flat "+ GST" line. **Still open, to flag at the end:** whether the retainer runs at a reduced rate for the first 12 weeks before ₹40,000 takes effect — Codex proposed this, it contradicts §4.2's "don't touch the monthly" reasoning below, and Tilak has deferred the call rather than decided it.

---

## 0 · Three things to settle before any number is useful

### 0.1 · A price already exists in the field, and the scope just grew past it

`Proposals/SkinFit Wellness - Proposal and Quote.md` §05 quotes **₹20,000 setup / ₹40,000 monthly**, and `files/OUTBOUND_MEMORY.md` §5 records that as the settled paid path. That quote covers **four** systems: immediate reply, qualification, booking + reminders, no-show recovery.

The six now named add **CRM logging/intake** and **follow-up past the first silence**. The proposal did not merely omit those — §02 names follow-up as one of three things *"deliberately not priced here,"* and CRM write-back is not in the document at all. §06 assumption 3 explicitly allows for a paper diary, i.e. **no CRM integration was assumed or priced.**

Arithmetic: four priced systems become six, and the two added are the two with the highest integration variance. That is roughly **+50% scope at +0% price**, and the added half is the half that touches software nobody has confirmed the name of (`SkinFit Technical Brief.md` §7, §9).

**If the six-system stack is now the standard build, ₹20,000 / ₹40,000 is not a price for it.**

### 0.2 · Three defects in the current quote, worth fixing before it goes anywhere else

| # | Defect | What it costs | Fix |
|---|---|---|---|
| 1 | §05 says **"₹40,000"** with no tax wording | `money-and-tax-explainer.html` costs this exactly: if the fee is read as tax-inclusive and you register in month three, ₹40,000 becomes ₹33,898 + ₹6,102 GST. **₹6,102 absorbed every month, permanently** | Write **"₹40,000 per month, exclusive of applicable taxes"** |
| 2 | Setup is **flat ₹20,000** while §06 lists four assumptions, any of which can double the build | The one number carrying all the unknown risk is the smallest number in the deal, and has no variance in it | Tier the setup by integration surface (§3) |
| 3 | **"One month's notice, no lock-in"** on top of a ₹20,000 setup | Worst realistic case: they pay ₹20,000 + one month's ₹40,000 = **₹60,000 total** for a build that is 20–30 person-days. Below the labour cost | A minimum term on the founding deal only (§4) |

### 0.3 · Check whether the quote has actually left

There is still **no SkinFit row in Notion** — searched 21 Aug, nothing. `SkinFit Tech Handoff 2026-08-18.md` §12 lists creating it as an open action. The Proposal and Quote file is marked *"Not yet laid out."*

If it has not gone out, defects 1–3 are still free to fix. If it has, **₹20,000 / ₹40,000 is now a fact in the Bangalore market that we chose** — Gino and Israni came out of an agency that shut down, and that network talks. Price client #2 accordingly, knowing #1's number may travel.

---

## 1 · What "build cost" actually is — two numbers, not one

This is already his own distinction, recorded in `taste-n-judgement.md` §7:

> *"We don't know their tools yet" is a pricing objection he will raise, and the answer is to separate the two numbers. The monthly fee prices running the service and does not move with their stack. The setup fee is where their stack actually bites.*

Applied honestly, that means **the setup fee is the variable one and the retainer is the stable one** — which is the opposite of how the current quote is shaped. A flat ₹20,000 setup says the integration surface doesn't matter. It is the only thing that matters.

**What actually drives the setup number, in order of variance:**

| Driver | Cheap end | Expensive end |
|---|---|---|
| Booking | Held on our side, desk copies across | Write into their practice software, no documented API |
| Channels | WhatsApp only | WhatsApp + Messenger + Instagram DM + Meta lead forms, one inbox |
| Locations | One | Two, with routing and two availability sets |
| CRM/intake | A structured log they can read | Field-mapped write into a system we have not seen |
| Language | English | Hindi and Kannada handling |
| Attribution | None | Ad referral parameter carried through to a booked appointment |

Every one of the expensive-end items is live at SkinFit. Their entire ad spend lands in **Messenger**, not WhatsApp (`SKINFIT-TECH-HANDOFF` §4), and §9 asks openly whether we even support that channel yet.

---

## 2 · Cost floor — what it costs us to run one client

### 2.1 · Vendor cost, split by whether it scales with the client's own volume

This split is the correction already logged in `taste-n-judgement.md` §5: **fixed infrastructure absorbs into the fee; per-conversation and per-inference charges go on the client's card**, because the whole pitch is that enquiry volume rises, and a volume-linked cost inside a flat retainer means a successful month costs us money.

**Fixed — absorb into the retainer:**

| Item | Monthly | Source |
|---|---|---|
| BSP platform (AiSensy ₹1,500 / Wati ₹2,499 / Gallabox ₹2,999 / Interakt ~₹2,142) | ₹1,500–₹3,000 | published |
| Hosting and orchestration | ₹1,000–₹2,500 | Hostinger invoice, per the tax explainer |
| Monitoring and logging | ₹500–₹1,000 | estimate |
| **Total fixed** | **₹3,000–₹6,500** | |

**Volume-linked — the clinic's account, the clinic's card:**

Meta's India rates from 1 July 2026: **marketing ₹0.8631, utility ₹0.1150, authentication ₹0.1150 per message, plus 18% GST.** Service messages free, and utility free inside an open 24-hour window — **both become chargeable from 1 October 2026**, which is six weeks away and changes the arithmetic below.

Worked at SkinFit-like volume (~10 enquiries/day ≈ 300/month, ~6 utility + 1 marketing message each):

| Item | Monthly |
|---|---|
| Utility: 1,800 × ₹0.115 | ₹207 |
| Marketing: 300 × ₹0.8631 | ₹259 |
| Model inference, ₹5–₹15 per conversation | ₹1,500–₹4,500 |
| **Total volume-linked, +18% GST** | **≈ ₹2,300–₹5,900** |

**The point is not today's figure — it is the slope.** At 300 enquiries this is 6–15% of a ₹40,000 retainer and invisible. At ten times the volume it is ₹23,000–₹59,000 a month, which is the entire retainer, arriving precisely in the month the system is working. Putting it on their card is not margin protection; it is the only structure where a good month is not punished.

It is also the cleanest tax position, and it is **already promised in writing** (`money-and-tax-explainer.html`, "Whose card"). Condition: **their account from the start.** Sign up on our card and rebill, and it becomes an import of services by us, taxable on top.

### 2.2 · Labour — the real cost, and the one the setup fee ignores

`hypothesis` — no build of this size has been delivered, so this is an estimate, not a measurement.

| Phase | Person-days |
|---|---|
| Access, audit, thread review | 2–3 |
| Systems 1–2 (reply + qualification, multi-channel) | 6–9 |
| System 3 (booking, branch routing, reminders) | 4–7 |
| System 4 (no-show recovery) | 2–3 |
| Systems 5–6 (CRM intake + follow-up past silence) | 5–8 |
| Copy, flow review, client sessions | 3–4 |
| **First client total** | **22–34** |
| Ongoing, per month | 2–4 |

At even a notional ₹3,000/day of founder time, the first build is **₹66,000–₹1,02,000 of labour against a ₹20,000 setup fee** — recovery of roughly 20–30%.

That is a defensible thing to do on purpose for client one, because most of those days are R&D that clients 2–5 inherit for free. It is not defensible as a **list price**, because a list price is permanent and R&D is not.

---

## 3 · What competitors charge — the actual comparison set

Two markets are being confused when people quote a number in this space. Software is not what we sell, and the price gap between the two rows below is the entire commercial opportunity.

| Layer | Who | What they charge | What they do not do |
|---|---|---|---|
| **BSP / messaging platform** | AiSensy ₹1,500/mo · Wati ₹2,499/mo · Gallabox ₹2,999/mo · Interakt ~₹2,142/mo | ₹1,500–₹3,000/mo + Meta per-message | Ship a toolbox. Somebody at the clinic still has to build, write, monitor and fix the flows. Nobody at a two-receptionist clinic does |
| **Clinic software** | Practo Ray | ~₹2,000/mo base, real cost commonly 50–100% higher with per-booking marketplace fees; reported range ₹1,000–₹4,000+ | Records, diary, SMS reminders. Does not answer an Instagram DM at 9:38 PM |
| **Aesthetic/med-spa suite** | Zenoti | $300–$600/mo per location; single location ~$200–$350; implementation $2,000–$5,000 | Enterprise chain software. Same gap: it manages the appointment, not the enquiry that never became one |
| **Voice AI** | ConnectAI ₹800/mo + ₹4/min; market ₹2–₹12/min all-in + platform from ₹2,999/mo | ₹3,000–₹15,000/mo typical | Phone only. Their ad spend lands in Messenger |
| **WhatsApp bot agencies** | Indian agencies, published cards | Discovery sprint ₹35,000 · Tier-2 build ₹75,000–₹1,25,000 · Tier-3 AI agent build ₹2,75,000–₹4,75,000 · retainer ₹8,000–₹18,000 | Build once, then a thin "maintenance" retainer. Not operating anything |
| **AI automation agencies, India** | Indian shops serving domestic + global | Single workflow ₹40,000–₹80,000 · multi-workflow with integrations ₹1,50,000–₹3,00,000 · complex agents ₹3,00,000–₹8,00,000. WhatsApp AI agent: **₹2–5L setup + ₹15,000–₹50,000/month** | Horizontal. No clinic vocabulary, no mystery-shop evidence, no idea what a tripwire offer does to show-up rate |

**Three readings that matter:**

1. **₹40,000/month sits in the upper-middle of the Indian managed band (₹15,000–₹50,000) and is defensible.** Don't move it. The number that is wrong is the setup fee.
2. **₹20,000 setup is below the cheapest published discovery sprint in the country (₹35,000)** and roughly a quarter of the low end of a multi-workflow integration build. We are pricing a six-system build below what agencies charge to *scope* one.
3. **The hybrid — fixed build fee, then a monthly for running it — is the 2026 default**, so it needs no explaining to a buyer. What is unusual is the second half: almost everyone charges a thin ₹8,000–₹18,000 "maintenance" retainer because they hand over and leave. We charge 2–4× that because we run it. **That difference has to be visible in the words, or the number looks like a markup on maintenance.**

Which is the second correction already in `taste-n-judgement.md` §5: *"maintenance and optimization" is how a retainer dies.* By month four nothing is visibly breaking and they start asking what they are maintaining. The proposal's §05 wording is already close to right — *running the four systems, changes to wording and flow, and a monthly account of what came in, what was answered, what was booked, what was recovered.* Keep naming it by what it delivers each month. Never by the category of work.

---

## 4 · Recommendation

### 4.1 · List card — publish this internally, quote from it

| Tier | Integration surface | Setup |
|---|---|---|
| **A** | Channels only. Reply, qualify, book on our side, remind, recover. Nothing written into their software. One location | **₹60,000** |
| **B** | A + intake written into an existing CRM/PMS with a documented API, or multi-channel across WhatsApp + Messenger + IG + lead forms | **₹90,000** |
| **C** | B + two-branch routing, or ad-attribution carried through to a booked appointment, or Hindi/Kannada handling | **₹1,35,000** |
| **D** | No documented API, on-prem or desktop-only software | **Paid discovery ₹25,000**, credited in full against whichever tier follows |

**SkinFit as specified is Tier C.** Messenger-first, two branches, unknown practice software, and the attribution card that `SKINFIT-TECH-HANDOFF` §9 calls potentially our strongest.

**Monthly: ₹40,000, exclusive of applicable taxes, all tiers, both branches.** Starts the month the first system goes live. Vendor accounts in the clinic's name and on their card from day one.

### 4.2 · The founding-client deal — discount the one-time, never the recurring

This is the single structural recommendation. **A low list price is permanent; a named waiver is not.** ₹20,000 as a list price cannot be raised to ₹90,000 for client #2 without either lying about #1 or explaining why the price quadrupled in a market where these owners know each other.

| Term | Founding client |
|---|---|
| Setup, listed | ₹90,000 (Tier B) or ₹1,35,000 (Tier C) |
| **Founding waiver** | **−₹65,000**, stated as a waiver, on the invoice |
| **Setup payable** | **₹25,000** |
| Monthly | ₹40,000, exclusive of applicable taxes |
| Minimum term | **12 weeks**, then one month's notice |
| Price lock | 12 months from go-live |
| Vendor charges | Their account, their card |

**What the waiver buys, written into the agreement:**
1. A named case study with the clinic's name and numbers.
2. A reference call for our next two prospects.
3. Access and the two 30-minute sessions delivered on the agreed dates. *(This one matters more than it looks — it is the completion mechanism from `OUTBOUND_MEMORY.md` §5, and it is the thing that actually kills first builds.)*
4. **Clawback:** cancel inside 12 weeks and the waived amount becomes payable, pro-rated.

The clawback is what makes the discount real rather than decorative, and it closes defect 0.2#3: worst case moves from ₹60,000 to ₹1,45,000, which is above the labour cost.

**Why the monthly is not touched:** it is the number every future client anchors to, the number that compounds, and the number already in writing. A waived one-time reads as a one-time to everybody. A discounted retainer is a discounted retainer forever.

### 4.3 · Two founding terms to name as founding terms, not policy

The current proposal gives both away silently, which means they cannot be charged for later:

- **Both branches at no extra charge.** Say it is a founding term.
- **The audit at no cost.** Already correctly worded (*"at no cost,"* never *"free"* — `taste-n-judgement.md` §5).

---

## 5 · Pricing models considered, with verdicts

| Model | Shape | Verdict |
|---|---|---|
| **Fixed setup + fixed monthly** | Tiered build fee, flat retainer | **Adopt.** The only model that works with zero conversion data, and the 2026 category default so it needs no defending |
| **Per-module, billed as each goes live** | Pay for system 1, then 2, then 3 | **Use as the build order, not the price structure.** It matches *"controlled execution, not instant rollout"* (`taste-n-judgement.md` §7) and the proposal §04 already sequences this way. But splitting the invoice invites cherry-picking, and the two systems they would drop are follow-up and no-show recovery, which are where the money actually is |
| **Per booked consultation** | ₹X per booking, or per show | **Reject for the founding client, on a specific ground.** The likely headline finding of the audit is that their enquiry count is wrong — `SKINFIT-TECH-HANDOFF` §4 has 27–50 estimated conversations a day against 10 logged. **You cannot bill against a denominator you are about to prove is broken.** Attribution is the thing they cannot do today; that is why they are buying. Revisit at client #4, once the system itself is the counter |
| **Revenue share** | % of treatment revenue | **Reject.** Already banned at cold stage (`OUTBOUND_MEMORY.md` §5), needs their billing data, and puts us inside a clinical P&L we have no visibility into |
| **Setup + usage-based monthly** | Retainer scaling with enquiry volume | **Reject for now.** Correct in theory and it is the eventual shape, but it prices in a currency neither side can measure yet. The volume split in §2.1 already gets the economics right without it |

---

## 6 · The value check — the sentence that has to survive their arithmetic

Their disqualification floor is an average treatment value of **₹25,000** (`wedge-signal-entry.md` §2), and the procedures the wedge is built on run **₹49,999–₹1.5L**.

At ₹40,000/month: **one additional converted patient a month at ₹25,000 covers 62% of the fee. Two cover it with change.** At the ₹49,999–₹1.5L end, one covers it outright.

That is the whole commercial argument and it is checkable by them, which is why it works. It is also why it must never be dressed up with a projected uplift percentage — `taste-n-judgement.md` §4: *can the reader check this, and what happens if they do?* State the break-even. Let them do the multiplication.

---

## 7 · What is unresolved

- ~~**`OUTBOUND_MEMORY.md` §5 free-pilot boundary is still open.**~~ **Resolved 2026-09-05 (Tilak): paid build plus paid operating, no free pilot.** The audit and strategy document stay free; everything from the build onward is paid. This card's assumption was correct and now stands confirmed.
- **Whether the SkinFit quote has been sent.** Decides whether §0.2 is a fix or a precedent.
- ~~Whether we support Messenger and Instagram DM at all~~ **Resolved 2026-08-22 — yes.** Sarvam is the confirmed conversational-AI vendor for user-initiated Instagram/Messenger conversations, alongside the WhatsApp qualification bot. Tier B/C pricing in §4.1 is no longer blocked on this.
- **1 October 2026:** service messages and in-window utility messages stop being free. Six weeks out, and it lands on the follow-up and no-show systems hardest. Whoever signs a 12-month price lock should have this in view — it moves the client's card, not ours, which is the argument for the split in §2.1 arriving before October rather than after.
- **First-12-weeks reduced retainer (₹35,000 vs. ₹40,000)** — raised via the Codex draft quote, 2026-08-22. Contradicts §4.2's stated reasoning that the monthly fee should never be discounted because it's the number every future client anchors to. Tilak has deferred this, not decided it — **flag again before the SkinFit quote is finalised.**

---

## Sources — competitor and vendor pricing

- [WhatsApp Business API Pricing in India (2026) — AiSensy](https://aisensy.com/pricing)
- [Best WhatsApp API Providers in India 2026: Pricing, Features & Verdict — Yazz](https://www.yazz.in/blog/top-6-whatsapp-api-providers-in-india-pricing-feature-comparison-2026)
- [WhatsApp API Pricing India (Jul 2026): ₹ Rate Card — Whautomate](https://whautomate.com/whatsapp-business-api-pricing-india)
- [WhatsApp Business API Pricing in India 2026 (Per Message) — ChatMaxima](https://chatmaxima.com/whatsapp-api-pricing/india/)
- [Meta Raised India WhatsApp Marketing Rates 10% — RichAutomate](https://richautomate.in/blog/whatsapp-meta-india-rate-hike-january-2026-marketing-cost-impact)
- [WhatsApp Business API Pricing in 2026: Categories, Costs, What Changed — Blueticks](https://blueticks.co/blog/whatsapp-business-api-pricing-2026)
- [How to price your WhatsApp bot agency services in 2026 — CodeWords](https://www.codewords.ai/blog/how-to-price-whatsapp-bot-agency-services)
- [WhatsApp Chatbot Pricing in India 2026 — Hyperleap](https://hyperleap.ai/blog/whatsapp-chatbot-pricing-india-2026)
- [AI Automation Agency Pricing: What to Charge in 2026 — Taskip](https://taskip.net/ai-automation-agency-pricing/)
- [AI Agency Pricing Guide 2026 — Digital Agency Network](https://digitalagencynetwork.com/ai-agency-pricing/)
- [Practo Ray Pricing 2026: The Hidden Per-Booking Fees — Cufront](https://www.cufront.com/blog/practo-ray-pricing-india-worth-it-2026)
- [Clinic Management System Cost in India 2026 — ICG](https://ichelonconsulting.com/clinic-management-system-cost-india-2026)
- [Zenoti Pricing: Plans, Costs & Hidden Fees (2026) — Pabau](https://pabau.com/blog/zenoti-pricing/)
- [Best AI Receptionist for Clinics in India (2026) — ConnectAI](https://www.connectai.care/learn/best-ai-receptionist-for-clinics-india)
- [Voice AI Agent Cost in India 2026 — Ravan.ai](https://www.ravan.ai/blog/voice-ai-agent-cost-india-2026)


---
Related: [[files/OUTBOUND_MEMORY|OUTBOUND_MEMORY]] · [[04 Clients/SkinFit Wellness/SkinFit Technical Brief|SkinFit Technical Brief]] · [[04 Clients/SkinFit Wellness/SkinFit Tech Handoff 2026-08-18|SkinFit Tech Handoff 2026-08-18]] · [[taste-n-judgement|taste-n-judgement]] · [[01 Playbooks/wedge-signal-entry|wedge-signal-entry]] · [[04 Clients/SkinFit Wellness/SkinFit Wellness|SkinFit Wellness]] · [[05 Prospects/Batch 3 Remainder/08 SkinFit Wellness|08 SkinFit Wellness]]
