---
date_created: 2026-08-15
date_modified: 2026-08-15
status: reference
---
# The remaining 22 — everything outside shop-queue positions 1–20

**Generated** 2026-08-15 · **Cohort** `new_leads_1` (42 clinics) · **Source** `results.json`
**Companions** `Shop Queue 01-10 2026-08-15.md` · `Shop Queue 11-20 2026-08-15.md` · `Open Checks 2026-08-15.md`

**Epistemic status:** `confirmed` for Instagram, Meta page-level ad counts and Google advertiser-name
matches, all dated 15 Aug and reproducible. Everything under *What clears it* is a proposed action,
not a finding.

---

## Read this before the table — two things it would be easy to get wrong

**1. Only 11 of these 22 have anything flagged.** The other 11 are fully settled on all three
layers. They are outside the queue because they have no paid trail and a smaller audience, not
because something is pending. There is nothing to resolve on them.

**2. Clearing an ads flag does not make a clinic shoppable.** The three blockers from the queue docs
apply to all 22 regardless: **no phone/WhatsApp number on file, no published hours captured (§2.0
admissibility), Gate A / hard kill #10 unrun.** Ad status is touch-2 material — it decides *what you
can say*, not *whether you can shop*. Resolving all 11 flags and shopping nobody is the failure mode
here.

---

## Group 1 — has an open flag (11)

| # | Clinic | IG followers | Meta ads | Google ads | Flag |
|---|---|---|---|---|---|
| 21 | Dr. Anil Abraham's Skin & Hair Clinic | **67,202** · 240 posts · last post 30/7 | Unresolved — `/docanilabe` returned no page | Unconfirmed — `ANIL ABRAHAM`, 1 creative, last 27/7 | Identity + §1.2 park |
| 22 | Hairline International, Richmond Town | 3,168 · 504 posts · last post 10/8 | Yes — page confirmed, **1 lifetime ad, no date** | Unconfirmed — `HAIRLINE DIAGNOSTICS AND HEALTH CARE PVT LTD`, 23 creatives, last 9/8 | Wrong-entity verdict + kill #5 |
| 23 | dr_shettys_cosmetic_centre | 2,965 · 517 posts · last post 30/7 | Unresolved — `no_items` on their own linked page | No | Near-settled |
| 24 | Rock Aesthetics Clinic | 1,822 · 199 posts · last post 14/8 | Unresolved — `no_items` on their own linked page | No | Near-settled |
| 25 | Calyx Skin Lab — Indiranagar | 899 · 100 posts · last post 14/8 | Unresolved — no Facebook page found | **No** — but the source URL is a paid landing page | Contradicted by evidence |
| 26 | New Look Skin Hair & Laser | 639 · 270 posts · last post 11/8 | No — page `Wellness at New Look Health & Skin Clinic` confirmed, 0 ads | Unconfirmed — `New Look Skin Care Ltd`, 9 creatives, last **8/4 (129d)** | Dormant either way |
| 27 | the radiant clinic | 432 · 37 posts · last post 13/8 | No — page `The Radiant Clinic` confirmed, 0 ads | Unconfirmed — `Radiant Aesthetics`, 2 creatives, last **23/11/25 (265d)** | Dormant either way |
| 28 | Masa aesthetics | 428 · 170 posts · last post 4/8 | Unresolved — no page located | No | Meta half unknown |
| 29 | Pigment Skin And Hair Clinic | 318 · 80 posts · last post 1/7 | Unresolved — no page located | Unconfirmed — `PIGMENT PLUS SKIN AND HAIR CLINIC`, 1 creative, last **14/10/25 (305d)** | Dormant either way |
| 30 | Meraki Aesthetics | 276 · 129 posts · last post 8/8 | Unresolved — no page located | No | Meta half unknown |
| 31 | cradle of youth | 500 · 93 posts · **last post 1/1 (226d)** | Unresolved — no page located | No | Possibly inactive |

### What is flagged, and what clears it

**21 · Dr. Anil Abraham's** — Google shows a bare personal name, `ANIL ABRAHAM`, one creative. That
is the exact `Mradula Singh` shape from the SE cohort: verified, India-based, uncommon name, and
still the wrong person. Meta returned `Doctors.co.in`, a directory, rejected.
→ **Clears when:** the `ANIL ABRAHAM` advertiser page is opened and the ad's landing domain is
recorded. If it points at his clinic, he moves to a confirmed advertiser; if not, he's a clean No.
**But this does not put him in the queue** — 67,202 followers makes him a §1.2 mega-founder-brand,
deferred to post-Case-Study-#1 by the 2026-07-22 decision. Only a reversal of that decision moves him.

**22 · Hairline International** — filed *Spending now* on an advertiser that is a different legal
entity. Its own confirmed Meta page holds 1 lifetime ad with no date. Also rejected during the run:
`Hairline Clinic Brisbane Pty Ltd`, an Australian advertiser that surfaced inside an India query.
→ **Clears when:** the Hairline Diagnostics advertiser page is checked for `Based in:` and landing
domain. If it resolves to hairline.co.in it is genuinely a live spender and belongs in Tier 1; if
not, it drops to barely-advertising. **Separately blocked on hard kill #5** — multi-branch chain,
sign-off structure unknown. Both must clear before it's worth a shop.

**23 · dr_shettys_cosmetic_centre** and **24 · Rock Aesthetics** — both link a Facebook page from
their own website, so the page is theirs; the Ad Library then returned `no_items`, which for a page
that demonstrably exists most likely means *never advertised* rather than *lookup failed*.
→ **Clears when:** each page's *Page transparency → Ads* tab is opened. **One minute each.** Expected
outcome is a clean **No** on both. Low value, high confidence — worth doing only because it's cheap.

**25 · Calyx Skin Lab** — the most likely miss in the cohort. No advertiser named Calyx exists in the
transparency centre, but the source URL is a paid landing page carrying `gclid`,
`gad_campaignid=22135492301` and `utm_medium=ppc`. Somebody clicked a **live Google ad** to generate
that URL. The audit says Unresolved; the URL says Spending now.
→ **Clears when:** the transparency centre is searched for the parent or legal entity from the site
footer / GBP listing rather than the trading name. **If it lands, Calyx moves straight into Tier 1** —
it would be the only clinic in this group to do so.

**26 · New Look**, **27 · the radiant clinic**, **29 · Pigment** — each has a near-name Google
advertiser, and in all three the last ad is 129, 265 and 305 days old.
→ **Clears when:** the advertiser's landing domain is compared against the clinic's. **Don't bother.**
Even if the advertiser *is* them, they are not buying enquiries today, so the verdict is the same
either way. `wedge-signal-entry.md` §0.1 also rules out building a hook on a paused account —
*"it got expensive"* and *"the campaign ended"* are always available rebuttals.

**28 · Masa aesthetics** and **30 · Meraki** — no Facebook page located, so "no Meta ads" is unknown,
not zero. The only FB link on Masa's site was the `2008/fbml` XML namespace, not a page; Meraki's
search returned `Sabina's Cravings`, a blogger, rejected.
→ **Clears when:** Facebook is searched directly for the clinic name, the page confirmed theirs by
address/phone/website match, then *Page transparency → Ads*. At 428 and 276 followers the payoff is
small either way.

**31 · cradle of youth** — no website at all, and Instagram has been silent since **1 January, 226
days**. Meta search returned `Cradle Children Hospital`, rejected.
→ **Clears when:** the GBP listing is checked for whether the clinic is still trading. **Confirm it
is alive before spending any further minutes on it** — this is a possible hard kill #1 (no website,
no reachable channel), not an ads question.

---

## Group 2 — nothing flagged, settled on all three layers (11)

All three layers resolved on 15 Aug. No open check, nothing to clear. They sit outside the queue on
priority alone: no live paid spend means no *"you're paying for enquiries right now"* fact and no
dead-lead-reactivation wedge — which removes one wedge, **not** the clinic (`wedge-signal-entry.md`
§1.3 is explicit that not running ads is never a disqualifier).

| # | Clinic | IG followers | Meta ads | Google ads | State |
|---|---|---|---|---|---|
| 32 | mantras clinic | ✅ 10,831 · last post 27/6 | No — page `MAAC` confirmed, 0 ads | No | No paid presence |
| 33 | Pearl Aesthetic | 4,705 · last post 7/8 | Yes but stale — 1 ad, last **20/11/2024** | No | Dormant |
| 34 | Facial Aesthetics Center — Dr Nisha Shetty | ✅ 4,204 · last post 10/8 | No — page confirmed, 0 ads | No | No paid presence |
| 35 | Livglam Anti-Ageing Clinic | 4,012 · last post 16/6 | No — page `Livglam Clinics` confirmed, 0 ads | No | No paid presence |
| 36 | Skinray Clinic, Dommasandra | 2,622 · last post 14/5 | No — page confirmed, 0 ads | Yes but stale — 1 creative, last **27/6 (49d)** | Dormant |
| 37 | Aesthetics Plus — DrSurindher | 2,249 · **858 posts** · last post 18/7 | No — page `Aesthetics PLUS - Cosmetic Surgery Clinics` confirmed, 0 ads | No | No paid presence |
| 38 | Dr. Sunaina Hameed | 2,151 · last post 22/7 | No — page `Your Family Dermatologist` confirmed, 0 ads | No | No paid presence |
| 39 | ZIUR Skin, Hair & Laser | 1,613 · last post 11/8 | No — page confirmed, 0 ads | No | No paid presence |
| 40 | DermaGlo Laser Skin Clinic | 1,296 · last post 14/8 | No — page confirmed, 0 ads | No | No paid presence |
| 41 | skinwork | 635 · last post 13/7 | No — page `theskinwork` confirmed, 0 ads | No | No paid presence |
| 42 | Avance Derma Skin, Hair & Laser | 492 · **last post 24/4/2025 (478d)** | No — page confirmed, 0 ads | No | No paid presence |

### Notes on this group

- **33 · Pearl Aesthetic** and **36 · Skinray** are the cohort's two dormant advertisers. §0.1
  applies: a paused ad account is not evidence of a conversion problem. **Do not build a hook on
  either.** They are ordinary no-spend clinics for hook purposes.
- **34 · Facial Aesthetics Center** and **37 · Aesthetics Plus** have **no website on file** —
  Instagram is the only channel. Reachability has to be settled at Gate A before either can be
  worked at all.
- **34 · Facial Aesthetics Center — Dr Nisha Shetty (Maxillofacial Surgeon)** is a surgical practice
  rather than an elective skin clinic. Worth a scope check against the ICP before investing.
- **35 · Livglam** also appears on the 9-clinic list supplied on 15 Aug — same clinic, already
  checked here. Nothing further to run on it.
- **42 · Avance Derma** last posted **24 April 2025**. Like cradle of youth, confirm it is still
  trading before spending anything on it.
- **32 · mantras clinic** is the largest audience in this group at 10,831 and fully settled. If the
  Tier 2 slots need topping up after Gate A cuts, it is the first name to pull from here.

---

## What would actually move any of these into the shop queue

In priority order, and only the first is likely to change anything:

1. **Calyx** — find the legal entity behind the paid landing page. The only clinic here that could
   land in Tier 1.
2. **Gate A across all 22** — a named decision-maker on a personal channel is worth more than any
   ads verdict in this file, because it decides whether a message can be written at all.
3. **The GBP pull** — phone, published hours, review count, oldest review. Review count is the
   nearest available proxy for hard kill #3 (under ~20 enquiries/month), which is currently
   `undetermined` on all 42 and must not be guessed.
4. **Everything else in Group 1** — resolvable, but resolving it changes no verdict that matters.
