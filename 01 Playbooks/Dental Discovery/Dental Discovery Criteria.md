---
date_created: 2026-08-09
date_modified: 2026-08-09
status: active
---
# Dental Discovery Criteria — Bangalore

**Status:** v1, drafted 2026-08-09. Untested — no dental clinic has been scraped under these rules yet.
**Relationship to existing docs:** this is a dental-specific overlay on `Apify Discovery Context.md`.
Where this file is silent, the parent doc governs. Where it contradicts the parent, the contradiction
is called out explicitly below rather than resolved silently.

**Blocking question before any of this runs:** `Apify Discovery Context.md` §2.2 says dental is a hard
zero *this round* ("we are not working dental this round … the mixed model has already burned us"),
while `CLAUDE.md` lists dental as a target vertical and `clinic-audit-checklist.md` §0 has Dental as a
category option. These disagree. The §2.2 reason as written points at **mixed skin+dental clinics**
(cf. Dr. Utkarsha's Dental & Esthetic Centre, exclusion list #10). If that was the whole reason, pure
dental is unaffected. If there was another reason, it isn't written down anywhere and this document
is void until it is.

---

## 0. Why the aesthetic criteria don't transfer unmodified

Three structural differences, each of which breaks a filter that works fine in aesthetic:

1. **Dental ATV is bimodal inside a single clinic.** The same practice runs ₹3,000 root canals and
   ₹3,00,000 full-arch cases. In aesthetic, the whole menu clears ₹25,000, so the clinic is a valid
   unit of qualification. In dental it is not — the *procedure mix* is.

2. **Review count stops working as a lead-volume proxy.** Dental review counts are inflated by
   routine cleanings and RCTs. A clinic can hold 800 reviews that are almost entirely ₹3,000 visits.
   The parent doc's "≥20 reviews" gate still tells you the business is real; it no longer tells you
   there are 20+ *high-ticket* enquiries a month.

3. **The two demand segments want different wedges.** Pain-driven leads (toothache, emergency,
   extraction) are urgent, convert fast, and are exactly where speed-to-lead bites hardest — but
   they fail the ATV bar. Deliberative leads (implants, aligners, smile makeover) clear the bar and
   behave like aesthetic: price-first enquiry, quote given, silence, no chase. **Only the
   deliberative segment is ICP.** Speed-to-lead being "stronger in dental" is true of the segment we
   can't sell to.

**And one thing we cannot use:** treatment-plan non-acceptance is dentistry's single largest revenue
leak, and it is **not screenshot-provable** — it happens in the chair, invisible to a mystery shop or
a GBP listing. `wedge-signal-entry.md` §0 requires the entry wedge to be provable. So dental gives us
*more clinics for our existing openers*, not a new opener. Plan accordingly.

---

## 1. Search terms

Procedure-led terms first — they self-select for ticket size. Entity-led terms return the
₹10K-ATV general practices we throw away at Gate B.

### 1.1 Primary (run these first)

```
dental implant clinic · dental implant centre · implantologist
all on 4 dental implants · full mouth rehabilitation · full mouth implants
smile makeover clinic · smile design clinic · dental veneers
cosmetic dentist · aesthetic dentistry clinic
clear aligners clinic · invisalign provider · orthodontist
prosthodontist · dental aesthetics clinic
```

### 1.2 Secondary (run only if primary yield falls short; expect a high reject rate)

```
dental clinic · dental studio · multispeciality dental clinic · dental care centre
```

### 1.3 Never run

`dentist near me` · `kids dentist` · `pediatric dental` · `emergency dental` ·
`teeth cleaning` · `root canal clinic` — these return the low-ATV segment by construction.

### 1.4 Batching and geography

4–6 terms per actor call, same as the parent prompt. Rotate against the §3 Bangalore micro-market
list in `Apify Discovery Context.md`. Karnataka only.

**Raw target: 250–350 place records** before filtering — higher than the aesthetic run's 180–250,
because Gate B will reject harder.

---

## 2. Qualification gates

Run in this order. Cheapest rejections first.

### Gate A — Hard kills (one fires, drop it, spend nothing further)

1. Name matches the exclusion list in `Apify Discovery Context.md` §4
2. No website **and** no Instagram **and** no Google Business Profile
3. Operating under 12 months (oldest Google review date)
4. Fewer than 20 Google reviews total *(business-is-real floor only — see Gate C for volume)*
5. Chain: more than 5 branches, or presence in 3+ states, or a corporate/DSO parent
6. **Kids-only or pediatric-only dentistry** — ATV cannot structurally clear ₹25,000
7. **Mixed skin/aesthetic + dental** — excluded per parent §2.2 until that decision is revisited
8. Committee or multi-partner sign-off with no identifiable single owner
9. Geographic mismatch — GBP says Bangalore but IG bio names another city as the real base

### Gate B — Procedure gate (does the high-ticket work exist)

Must confirm **at least one**, from the website services pages, IG bio/highlights, or GBP service list:

1. A **named premium implant system** — Nobel Biocare, Straumann, or equivalent
   *(Korean-only systems at ₹15–30K are borderline; log them, don't auto-pass)*
2. **Invisalign provider status** or a named clear-aligner brand partnership
3. **Smile design or veneers** as a distinct service page, not a buried line item
4. **Full-mouth rehabilitation / All-on-4 / All-on-6** named as a service
5. **Founder credential**: MDS Prosthodontist, Implantologist, or Orthodontist

**Auto-fail:** website and IG dominated by cleanings, fillings, RCT, extractions and check-ups with
no high-ticket service page anywhere.

### Gate C — Flow gate (is there evidence of high-ticket *demand*)

Gate B proves the clinic offers the procedure. It does not prove anyone is buying it. A clinic with
an All-on-4 page doing two arches a year has a ₹5L sticker price and no addressable pipeline.

**Both B and C must pass. Either alone is insufficient.**

Confirm **at least one**:

1. **Google Ads Transparency** shows active ads on high-ticket keywords — implant, aligner,
   Invisalign, smile makeover. *Ads on "dentist near me" or emergency terms do NOT count* — that's
   the pain segment.
2. **Practo Prime or JustDial paid listing** — counts fully as "already paying for leads"
3. **Review text names high-ticket procedures** — patients mentioning implants, aligners, veneers, or
   full-mouth work. This is the cheapest available proxy for real high-ticket throughput.
4. **Meta Ad Library** shows active ads on high-ticket procedures *(weaker signal in dental than in
   aesthetic — search intent dominates this category; treat as corroborating, not sufficient alone)*

Note the inversion from the aesthetic runs: **Google Ads is primary here, Meta is secondary.**

### Gate D — Instagram gate

Apply `Apify Discovery Context.md` §2.5 unchanged:

- A real clinic **or** founder Instagram account, public
- Followers ≥ 1,000 (preferred band 2,000–80,000; >100,000 → PARK tier)
- Posts ≥ 20
- Most recent post within 60 days

⚠️ **Unresolved contradiction, flagged not resolved.** §2.5 accepts a *clinic* account. But
`personalized-outbound-v2.md` requires a **personal founder account** for the Three Threads sequence,
and `MEMORY.md` §5 records this biting already (Dr Juvita, Vtiara, Sapphire — brand page only, flagged
before Day-0 send). Dental founders under-index on personal IG relative to aesthetic, so this will
fire far more often here. **Decision needed from Tilak:** does the sequence change, does the gate
change, or do brand-page-only clinics get parked? Until answered, mark them
`park — brand page only, sequence unconfirmed` rather than passing or killing them.

### Gate E — Decision-maker gate

1. A single named founder-dentist discoverable from GBP, IG bio, website team page, LinkedIn, or Practo
2. `"Dr. X's [Clinic Name]"` in the GBP title is a strong single-owner signal
3. A neutral brand name with no doctor attached anywhere is a warning, not yet a kill
4. Two-or-three-partner practices → **park**, don't kill; confirm which partner owns operations first
5. Front-desk-only contact → **park**, route via Practo doctor listing / website team page / LinkedIn

Expected failure rate: high. Our own `Batch 3 Dental Audit.md` found no named decision-maker on 5 of
11 clinics (Chisel, Sky Dental, Smiley House, both Amaya branches).

### Gate F — Review screen (dental-specific)

1. **Upselling and over-treatment complaints → exclude.** If patients already accuse the clinic of
   pushing unnecessary treatment, selling them automated follow-up makes the problem worse and puts
   our positioning behind a bad actor.
2. Complaints about waiting, billing surprises, rushed appointments, or no-shows are **usable wedge
   material**, not disqualifiers.
3. Last-review gap ≥ 3 months → review-reactivation signal, log it.

### Gate G — Park signals (flag, still return, lower priority)

Per parent §2.6, plus:

- Bio or site says "managed by @someagency" → incumbent vendor, note the handle
- Clinic already advertises AI / instant-response / automation as its own selling point
- Brand-page-only IG (see Gate D contradiction)
- Multi-partner practice with operations owner unconfirmed

---

## 3. Wedge pre-routing

Because treatment-plan follow-up isn't provable cold, these are the dental wedges we can actually
evidence. Tag each qualified clinic with `funnel_break_stage` and `recommended_entry_sku` per
`wedge-signal-entry.md` §4.

| Signal | Entry wedge | Provable via |
|---|---|---|
| High-ticket ads live · slow or no reply | Dead-lead reactivation | Google Ads + mystery shop |
| Implant/aligner quote given, never chased | **Quote-decay follow-up** — the strongest dental wedge | Mystery shop: ask implant or aligner price, go quiet 7–14 days |
| Fast reply · no qualification questions | Qualification + scoring layer | Mystery shop test 1 |
| After-hours enquiry unanswered or promise-only auto-reply | 24/7 capture + qualification | Mystery shop test 4 (10–11pm) |
| Reviews cite no-shows, missed appointments, rescheduling friction | **No-show recovery** — fits dental better than aesthetic | Review text |
| Good review volume, last review ≥3 months old | Review / recall reactivation — calendar-triggered, no aesthetic equivalent | GBP review dates |
| Practo Prime paid listing · slow response | Dead-lead reactivation (aggregator) | Practo + mystery shop |

**Mystery-shop advantage over aesthetic:** "What's the cost for a single implant?" is a completely
natural, low-suspicion question, and the answer simultaneously reveals the price tier *and* whether
they qualify the enquirer. No elaborate pretext needed.

---

## 4. Chain exclusion list — VERIFY, DO NOT ADOPT

The following were listed from general knowledge and **have not been verified** against Bangalore GBP
data, current operating names, or branch counts. Treat as a starting hypothesis to check during the
scrape, not as settled fact:

Clove Dental · Sabka Dentist · Partha Dental · Apollo White Dental · FMS Dental ·
Axiss Dental · Dentzz · National Dental Care · Dezy

Indian dental has more DSO-backed practices than aesthetic, and many don't look like chains from a
single GBP listing. **The ">5 branches or 3+ states" rule in parent §2.3 is what should actually be
doing the work here** — the named list is a shortcut, not the mechanism.

---

## 5. Output format

Per qualified clinic, report:

`clinic name · area · GBP category · founder (+ confidence) · IG handle/followers/last post ·
review count/rating/last-review gap · Gate B evidence (which procedure, where found) ·
Gate C evidence (which demand signal) · contact channels · funnel_break_stage ·
recommended_entry_sku · status (Qualified / Park + reason)`

Also report: raw place count, and count dropped at each gate with reasons.

**Target: 15–20 qualified.** If Gate C is rejecting more than ~70% of Gate-B passes, stop and report
— that's evidence the high-ticket dental population in Bangalore is thinner than assumed, and worth
knowing before spending the rest of the credit.

---

## 6. What is untested here

Everything. Marked per `MEMORY.md` maintenance rule.

- The B+C two-gate model has never been run
- The claim that Google Ads outperforms Meta as a dental spend signal is reasoning, not observation
- Review-text mention of high-ticket procedures as a throughput proxy is untested
- The upselling screen has never rejected a real clinic
- No dental mystery shop has been run — `Batch 3 Dental Audit.md` marks all 11 as PENDING

Nothing in this file gets promoted from hypothesis to settled until real scrape and send data exists,
per `OUTBOUND_MEMORY.md` §7.


---
Related: [[01 Playbooks/Research Prompts/Apify Discovery Context|Apify Discovery Context]] · [[CLAUDE|CLAUDE]] · [[01 Playbooks/clinic-audit-checklist|clinic-audit-checklist]] · [[01 Playbooks/wedge-signal-entry|wedge-signal-entry]] · [[01 Playbooks/personalized-outbound-v2|personalized-outbound-v2]] · [[MEMORY|MEMORY]] · [[05 Prospects/Batch 3 Aesthetic and Dental/Batch 3 Dental Audit|Batch 3 Dental Audit]] · [[files/OUTBOUND_MEMORY|OUTBOUND_MEMORY]] · [[04 Clients/Sapphire Skin and Aesthetics/Sapphire Skin and Aesthetics|Sapphire Skin and Aesthetics]]
