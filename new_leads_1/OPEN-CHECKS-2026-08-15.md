# new_leads_1 — the 16 open checks

**Generated** 2026-08-15 · companion to `ADS-PRESENCE-2026-08-15.md`
26 of 42 clinics are settled on all three layers. These 16 are not.

Ordered by **whether closing it changes a verdict**, not by clinic. Groups C and D can be skipped
without affecting how the list is worked; Group A cannot.

---

## Group A — closing this changes the verdict (5)

### 1. Hairline International — `SPENDING NOW` rests on a different company
- **Have:** Meta page `Hairline International Hair & Skin Clinic` — **1 ad, no date returned**.
  Google `HAIRLINE DIAGNOSTICS AND HEALTH CARE PRIVATE LIMITED`, 23 creatives, last **9 Aug**.
- **Problem:** the Google entity is not the clinic's name. Also rejected during the run:
  `Hairline Clinic Brisbane Pty Ltd` — an **Australian** advertiser that surfaced in an India query.
- **Check:** open <https://adstransparency.google.com/?region=IN>, search `Hairline`, and read the
  `Based in:` line plus the advertiser's website on the Hairline Diagnostics page. Does it resolve
  to hairline.co.in?
- **If not theirs:** drops from *Spending now* to Meta-only with 1 undated ad — i.e. barely advertising.

### 2. divine aesthetics — 500 lifetime ads against 622 IG followers
- **Have:** Meta page `Divine aesthetics` — **4 ads, newest 12 Aug** (this part is solid).
  Google `DIVINE AESTHETICS SURGERY` + `…LLP`, 24 creatives, last **14 Aug**.
- **Problem:** a *surgery* practice, and the ad volume is wildly out of scale with a 622-follower clinic.
- **Check:** same transparency page, search `Divine Aesthetics`, compare the advertiser's landing
  domain against divineaesthetics.in.
- **Either way it stays in *Spending now*** (Meta is confirmed) — but the Google volume must not be
  attributed to them in any message unless it checks out.

### 3. Calyx Skin Lab — almost certainly buying Google Ads, under a name we can't see
- **Have:** no advertiser named Calyx in the transparency centre. No Facebook page found. IG
  @calyx_skin_lab, 899 followers, posted **14 Aug**.
- **But:** the website URL in the source CSV is a paid landing page carrying
  `gclid=…`, `gad_campaignid=22135492301`, `utm_medium=ppc`, `utm_campaign=INDR_Dermatosurgery`.
  **Somebody clicked a live Google ad to generate that URL.**
- **Check:** search the transparency centre for the parent brand (`Calyx Health`, `Calyx Skin Lab`,
  or whatever legal entity appears in the site footer / GBP listing).
- **This is the most likely miss in the whole cohort.** Currently filed as *Unresolved*; the URL
  evidence says it belongs in *Spending now*.

### 4. moon aesthetic — Meta page never found, Google is heavy
- **Have:** Google `Moon Aesthetic`, 25 creatives, last **14 Aug** — confirmed, exact name match.
  Meta: the slug guess resolved to `Chaser Aspira` (rejected), search returned
  `newarkmissionofindia.autoraja` (rejected).
- **Check:** find their real Facebook page (site moonaesthetic.in has no FB link), then look at
  Page transparency → Ads.
- **Already in *Spending now* on Google**, so this only adds a second channel — lower priority than 1–3.

### 5. Dr. Anil Abraham — 67,202 followers, the biggest audience in the cohort
- **Have:** Google `ANIL ABRAHAM`, **1 creative**, last **27 Jul** (19d). No website in the source
  list. Meta: `/docanilabe` returned no_items; search returned `Doctors.co.in` (a directory, rejected).
- **Problem:** a bare personal name. This is exactly the `Mradula Singh` precedent from the SE
  cohort — identity-verified, uncommon name, ten live ads, and still the wrong person.
- **Check:** open the `ANIL ABRAHAM` advertiser page and see what the ad actually links to.

---

## Group B — near-settled, the evidence just isn't formally closed (2)

Both linked a Facebook page **from their own website**, so the page is theirs. The Ad Library then
returned `no_items` ("empty or private"), which for a page that demonstrably exists most likely
means *never advertised* rather than *lookup failed*.

| Clinic | Their own site links to | Ad Library said |
|---|---|---|
| **Rock Aesthetics Clinic** | `facebook.com/rockaestheticsclinic` | no_items |
| **dr_shettys_cosmetic_centre** | `facebook.com/DrShettysCosmeticCentre` | no_items |

- **Check:** open each page → *Page transparency* → *Ads*. One minute each.
- **Expected outcome:** both move from *Unresolved* to a clean **No**. Low value, high confidence.
- Also rejected for dr_shettys during the run: `BangaloreTimesOfficial`, `Triderma by Dr. Shetty` —
  neither is the clinic.

---

## Group C — dormant either way, cosmetic (3)

Settling identity here changes nothing operationally: even if the advertiser **is** them, the last
ad is months old, so the clinic is not buying enquiries today.

| Clinic | Candidate advertiser | Last ad | Meta |
|---|---|---|---|
| **New Look Skin Hair & Laser** | `New Look Skin Care Ltd` (9cr) | 8 Apr (129d) | page `Wellness at New Look Health & Skin Clinic` confirmed, **0 ads** |
| **the radiant clinic** | `Radiant Aesthetics` (2cr) | 23 Nov 2025 (265d) | page `The Radiant Clinic` confirmed, **0 ads** |
| **Pigment Skin And Hair Clinic** | `PIGMENT PLUS SKIN AND HAIR CLINIC` (1cr) | 14 Oct 2025 (305d) | page never found |

**Recommendation: leave these.** Not worth the minutes.

---

## Group D — Meta page genuinely never located (6)

No Facebook link on their website, and no name-corroborated page in search. Google is a clean **No**
for all six, so only the Meta half is open.

| Clinic | IG | Followers | Notes |
|---|---|---|---|
| **Seoulful Aesthetic Clinic** | @seoulful.korean_care | 1,017 | **Already *Spending now* on Google** (`SEOULFUL`, 22cr, 14 Aug) — Meta would only add a channel |
| **bodyscience_clinic** | @bodyscience_clinic | **13,420** | No website at all in source. Rejected: `The Skin and Body Science` |
| **dermo glamm** | @dermoglamm_laser_skin_hair | 8,349 | Rejected: page `61578140294899` (no name in title) |
| **Meraki Aesthetics** | @merakiaesthetics.in | 276 | Rejected: `Sabina's Cravings` (a blogger's post) |
| **Masa aesthetics** | @masa__aesthetics | 428 | Only FB link on site was the `2008/fbml` XML namespace, not a page |
| **cradle of youth** | @cradle_of_youth | 500 | No website. Rejected: `Cradle Children Hospital`. IG dead since **1 Jan (226d)** |

- **Check:** search Facebook directly for the clinic name, confirm the page is theirs (address /
  phone / website match), then *Page transparency* → *Ads*.
- **Priority within this group:** bodyscience (13.4k followers) and dermo glamm (8.3k) are the only
  two with an audience worth the time. cradle of youth is probably dead — no website, no posts in
  226 days.

---

## Also still open — and it is about the method, not a clinic

`Shortlist 2026-08-14.md` records **Augusté Skin: "Google ~43 total · 10/30d · 4/7d"**, sourced to
Tilak, marked `confirmed`. This run found **no Google advertiser named Augusté** — a region-IN query
for "Auguste Skin" returns exactly one advertiser, `SIDDANTH SARAF`.

If Augusté really does run ~43 Google ads under a name that a name search cannot reach, then **every
"No" in both cohorts is under-counting**, because both were produced by name search. That makes this
worth more than the 16 above.

**Check:** open the Augusté transparency page you used on 14 Aug and record the advertiser name
exactly as it appears there.

---

## Suggested order

1. **Calyx** — the `gclid` says they're spending; the audit says unresolved. Most likely miss.
2. **Augusté discrepancy** — tests the method itself.
3. **Hairline, divine aesthetics** — two clinics currently sitting in *Spending now* on an
   advertiser that isn't theirs.
4. **Rock + dr_shettys** — two minutes, converts two Unresolved into clean No.
5. **bodyscience, dermo glamm** — real audiences, Meta half unknown.
6. Skip Group C.
