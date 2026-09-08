---
date_created: 2026-08-15
date_modified: 2026-08-15
status: reference
---
# Mystery-shop queue — new_leads_1

**Generated** 2026-08-15 · **Source** `results.json` · **Cohort** 42 clinics
**Detail for positions 11–20:** `Shop Queue 11-20 2026-08-15.md`

**Nothing here is shoppable today.** Three blockers apply to every row: no phone/WhatsApp number
exists for any of the 42; no published hours were captured, so §2.0 admissibility cannot be checked;
and Gate A (hard kill #10) has never been run on this cohort. One Google Maps pull on all 42 clears
the first two and returns review count + oldest review date (hard kill #2) as a free by-product.

Queue size is 20 because `wedge-signal-entry.md` §2 sets the sitting at ~20 shops in 40 minutes,
then research only the threads that come back interesting.

**Notion checked 2026-08-15** — Batch 1 (19 rows) and Batch 2 (12 rows). **None of the 42 appear in
either.** No double-shopping risk; nothing here has been contacted.

---

## The queue

Tier 1 = live paid spend confirmed, the only clinics where *"you are paying for enquiries right
now"* is admissible under `CLAUDE.md` §5. Tier 2 = real audience, no paid trail — which removes one
wedge, not the clinic (`wedge-signal-entry.md` §1.3).

| # | Clinic | Instagram | Paid evidence (dated 15 Aug) | Tier |
|---|---|---|---|---|
| 1 | The aesthetic Co.Skin | 20,893 | Google 25 creatives, live 2026-08-14 · Meta 23 ads, 8 in 30d, last 2026-08-13 | Tier 1 |
| 2 | Promed aesthetics | 17,462 | Meta 2 ads, 2 in 30d, last 2026-08-08 | Tier 1 |
| 3 | The Aesthetic Edge | 12,375 | Google 25 creatives, live 2026-08-14 | Tier 1 |
| 4 | Aurilueur Esthetic Clinic | 7,777 | Google 7 creatives, live 2026-08-14 · Meta 3 ads, 2 in 30d, last 2026-08-14 | Tier 1 |
| 5 | SUTVACHA | 6,881 | Google 1 creatives, live 2026-08-14 · Meta 1 ads, 0 in 30d, last 2026-04-20 | Tier 1 |
| 6 | Augusté Skin | 5,075 | Meta 1 ads, 1 in 30d, last 2026-08-14 | Tier 1 |
| 7 | Richmond Dental & Aesthetic Center | 4,555 | Google 2 creatives, live 2026-08-13 | Tier 1 |
| 8 | KEZA Skin And Hair Clinic | 1,604 | Google 9 creatives, live 2026-08-13 | Tier 1 |
| 9 | Seoulful Aesthetic Clinic | 1,017 | Google 22 creatives, live 2026-08-14 | Tier 1 |
| 10 | Metphi Clinic | 829 | Google 17 creatives, live 2026-08-14 | Tier 1 |
| 11 | divine aesthetics | 622 | Meta 4 ads, 1 in 30d, last 2026-08-12 · Google unconfirmed (`DIVINE AESTHETICS SURGERY`) | Tier 1 |
| 12 | moon aesthetic | 466 | Google 25 creatives, live 2026-08-14 | Tier 1 |
| 13 | REGENIQUE — Whitefield | 265 | Google 13 creatives, live 2026-08-14 | Tier 1 |
| 14 | Dr. Sneha Sood / Sood Aesthetics | 215 | Meta 2 ads, 2 in 30d, last 2026-08-10 | Tier 1 |
| 15 | Sun Light Skin Clinic | 166 | Meta 3 ads, 3 in 30d, last 2026-08-12 | Tier 1 |
| 16 | Maya Medi Spa | 25,632 | none found | Tier 2 |
| 17 | Aestheticaa by Dr Madhulika | 15,205 | none found | Tier 2 |
| 18 | Elixir Advanced Aesthetics | 14,571 | none found | Tier 2 |
| 19 | bodyscience_clinic | 13,420 | none found | Tier 2 |
| 20 | dermo glamm | 8,349 | none found | Tier 2 |

---

## Not in the queue

| Clinic | Why |
|---|---|
| Dr. Anil Abraham's Skin & Hair Clinic (67,202 IG) | §1.2 mega-founder-brand — deferred to post-Case-Study-#1 by the 2026-07-22 decision |
| Hairline International, Richmond Town | Its *Spending now* state came from `HAIRLINE DIAGNOSTICS AND HEALTH CARE PVT LTD`, an unconfirmed different entity. Own Meta page: 1 lifetime ad, 0 in 30d. Multi-branch, so hard kill #5 also applies |
| The remaining 20 | No paid trail and under ~5,000 Instagram followers. Later, not killed |

## Standing constraints on what follows a shop

- `SALES_MOTION.md` §7 — no new Day-0 batch until the walkthrough video and the How We Work PDF
  exist as files. Neither does. Shop evidence perishes; a quote-decay finding is stale within weeks.
- `OUTBOUND_MEMORY.md` §6 (2026-08-04) — a warm reply outranks the send quota. Sapphire and
  Aesthetica Veda are both still open.
- `wedge-signal-entry.md` §4 — no wedge can be assigned from scraped data. The shop decides.
