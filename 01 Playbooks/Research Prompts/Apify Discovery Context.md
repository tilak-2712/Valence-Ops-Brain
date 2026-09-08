---
date_created: 2026-08-06
date_modified: 2026-08-06
status: active
---
# MESSAGE 1 — CONTEXT PACK (paste this first, then wait for "ready")

You are about to run a lead-discovery + qualification scrape for **ValenceOps** using the Apify MCP connector. This message is context only. **Do not call any tool yet.** Read it, confirm you've understood, and wait for my next message which contains the actual run instructions.

---

## 1. Who we are and what we sell

ValenceOps sells **revenue-operations automation to Indian elective clinics**, primarily in **Bangalore (Bengaluru), Karnataka**.

We are **not** a marketing agency and we do **not** sell lead generation, ads, content, or website redesigns. We fix what happens **after an enquiry already lands**:

- Speed-to-lead (instant response, 24/7, across WhatsApp + Instagram DM)
- Lead qualification and scoring
- Follow-up / nurture cadence on leads that went quiet
- Quote-decay follow-up on high-ticket quotes that were never chased
- No-show recovery and rebooking
- Dead-lead / dead-patient reactivation from WhatsApp history

Buyer = the **founder-doctor or owner-operator** of a single clinic or a small 1–4 branch group. Deal only works if one person can say yes.

---

## 2. ICP — who qualifies

### 2.1 Verticals we WANT (strict)

Only these. An eligible clinic must be primarily one or more of:

- Dermatology clinic (independent, not a hospital department)
- Cosmetology / medical aesthetics clinic
- Skin & hair clinic
- Hair transplant / trichology clinic
- Aesthetic / cosmetic surgery practice (independent boutique practice, not a hospital)
- Medspa / aesthetic wellness clinic where the core service line is **medical aesthetic treatment**

### 2.2 Verticals we EXCLUDE — no compromise, no exceptions

Reject on sight, do not spend enrichment credit on:

- **Dental of any kind** — dental clinics, dental studios, orthodontics, implant centres, "smile" clinics, aesthetic dentistry. We are not working dental this round. If a clinic offers dentistry *alongside* skin/aesthetics, exclude it — the mixed model has already burned us.
- Beauty salons, parlours, unisex salons, nail/lash/brow studios, spas, massage centres
- Laser hair removal chains that are salon-model, not clinic-model
- Ayurveda, homeopathy, naturopathy, panchakarma, yoga/wellness-only centres
- Weight-loss / slimming-only centres, nutrition clinics
- IVF / fertility, gynaecology, ENT, ophthalmology, orthopaedics, physiotherapy, general practice
- Multispecialty hospitals, hospital chains, and any listing that is a **doctor's profile inside a hospital** rather than an independent clinic
- Pharmacies, diagnostic labs, aggregator/directory listings, coaching academies, training institutes

### 2.3 Corporate chains — auto-exclude (no single decision-maker)

Never return any of these or their branches:

Kaya Clinic / Kaya Skin Clinic · Oliva Skin & Hair Clinic · Kosmoderma · VLCC · Clove Dental · Apollo (any) · Fortis / Manipal / Aster / Narayana / Sakra / Columbia Asia / Cloudnine · DHI India · Richfeel · Advanced Hair Studio · Bodycraft · Enhance Clinics · Dr. Batra's · Skinnovation-type national franchises · Partha Dental · Praba's VCare / VCare · Cutis Academy · Dermalife · La Densitae (if surfacing as national franchise) · any clinic with **more than 5 branches** or branches in **more than 2 states**.

Rule of thumb: **more than 5 branches, or presence in 3+ states, or a corporate parent = exclude.**

### 2.4 Hard kills (disqualify immediately, don't enrich further)

One hard kill disqualifies a clinic:

1. No website **and** no Instagram **and** no Google Business Profile
2. **Operating under 12 months** — check the oldest Google review date. Under 12 months = kill (no dead pipeline to recover, no proven revenue to pay from)
3. **Fewer than 20 Google reviews total** — proxy for insufficient inbound volume
4. **No high-ticket procedure in the service mix.** Average treatment value must plausibly clear ₹25,000. Clinics that only do basic facials, cleanups, and general consults fail. Look for: hair transplant, laser resurfacing, HIFU, PRP/GFC, thread lift, fillers/botox, body contouring, CoolSculpting, Q-switch/laser toning packages, tattoo removal packages, scar/acne programme packages
5. Committee or multi-partner sign-off with no identifiable single owner
6. The listing is a chain outlet with a corporate parent (§2.3)

### 2.5 Instagram gate — MANDATORY, this is the quality filter

Every clinic returned must pass **all four**:

| # | Test | Threshold |
|---|---|---|
| 1 | A real clinic **or** founder Instagram account exists and is public | Yes |
| 2 | Follower count | **≥ 1,000** |
| 3 | Post count | **≥ 20** |
| 4 | Most recent post | **within the last 60 days** (account is alive, not abandoned) |

**Preferred band: 2,000 – 80,000 followers.**

- Under 1,000 followers → reject, no exceptions
- Over 100,000 followers → **flag as PARK tier**, do not count toward the 15–20 target. These are mega-founder-brands: gatekeepers, likely an incumbent agency, long cycle. We defer them until we have a case study. You may list them in a separate "PARK" section at the end, max 3, clearly labelled.

Engagement sanity check where the data allows: if recent posts average **under 0.5% engagement** (likes+comments ÷ followers), flag `engagement: suspect — possible bought followers`. Don't auto-reject, just flag it.

### 2.6 Park signals (not kills — flag, still return, mark priority lower)

- Clinic bio or website says "managed by @someagency" → incumbent vendor, note the agency handle
- Clinic already advertises AI/automation/instant-response as its own selling point → do not pitch generic ops automation; flag it
- Only reachable contact is a front desk line, no founder identifiable → access problem, flag it

### 2.7 NOT disqualifiers — do not reject for these

- Not running Meta ads (only removes one wedge — check Practo Prime / JustDial paid listing as substitute "paying for leads" signal)
- Missing one channel (no website OR no Instagram) as long as the IG gate in §2.5 still passes
- Strong surface reputation with no visible weakness — a polished clinic is still a valid lead

---

## 3. Geography

**Primary: Bengaluru, Karnataka.** Rotate discovery across these micro-markets so the batch isn't all from one road:

Indiranagar · Koramangala · HSR Layout · JP Nagar · Jayanagar · Whitefield · Marathahalli · Sarjapur Road · Bellandur · Malleshwaram · Rajajinagar · Basavanagudi · Banashankari · Hebbal · Yelahanka · Kalyan Nagar / HRBR · RT Nagar · Sahakar Nagar · Electronic City · Bannerghatta Road · Vijayanagar · Kammanahalli

**Overflow only if Bangalore yield falls short of 15:** Mysuru, Mangaluru, Hubballi-Dharwad. Never outside Karnataka. If a clinic's Google listing says Bangalore but its Instagram bio lists other cities as its real base, treat it as a geographic mismatch and exclude — this has caught us out before (a "Karnataka" lead turned out to be a Kolkata chain).

---

## 4. EXCLUSION LIST — clinics already in our pipeline

**None of the following may appear in the output.** Match loosely: ignore case, punctuation, "Dr."/"Dr", "Clinic"/"Clinics", branch suffixes, and the `&`/`and` difference. If a scraped name is a branch, alternate spelling, or obvious variant of anything below, **exclude it**. If you're unsure whether a match counts, exclude it and note it in the excluded log rather than risk a duplicate.

### 4.1 Active outbound / Notion tracker (contacted or drafted)

1. Aura Cutisurg Clinic
2. Anew Cosmetic Clinic
3. Clinic Next Face (JP Nagar, Banashankari, Sadashivanagar)
4. Dr. Sculpt Aesthetic Clinic
5. Dr. Keshav's Skin, Hair, Cosmetic & Laser Clinic
6. Ministry of Skin (Lavelle Road, Jayanagar)
7. Dr. Swetha's Cosmoderm Centre
8. Dr. Juvita Aesthetics
9. Vtiara Hair & Skin Clinic (Indiranagar, New BEL Road)
10. Dr. Utkarsha's Dental & Esthetic Centre
11. Dr. Ritika Shanmugam Skin, Hair & Aesthetic Clinic
12. DNA Skin Clinic (Kalyan Nagar, Whitefield)
13. AvatarLuxe
14. Cozmo Blis / Cozmo Bliss
15. Iridescent Aesthetics
16. Dr. Dixit Cosmetic Dermatology Clinic
17. Dr. Tina's Skin Solutionz
18. Dr. Karishma Aesthetics / K Aesthetics
19. The Glow Clinic
20. Idha Skin Clinic
21. LA CROWN Aesthetic Clinic
22. Contura Clinic
23. Umbrella Aesthetics
24. Sapphire Skin & Aesthetics Clinic
25. Evolve Skin and Aesthetics
26. Skinology Centre
27. Evenly Skin & Hair Clinic
28. Sanyukt Skin Clinic

### 4.2 Audited batch 1 & 2

29. Aesthetica Veda Clinic
30. Sparsha Skin Care Clinic
31. Pruthvi Children's and Skin Clinic
32. Pranav Skin and Cosmetology Clinic
33. Venkat Center for Aesthetic Health
34. DermaZeal Clinic
35. Dermaville Skin Clinic
36. Dr. Rai's Skin & Hair Clinic
37. Dr. K Srinivasa Murthy's Skin & Cosmetology Centre
38. Ridhi's Skin and Hair Transplant Clinic
39. CosMediQ Hair Transplant and Skin Clinic
40. Nishka Skin Clinic
41. ProSkincare Esthetics
42. Neo Follicle Hair Transplant Clinic
43. Skinmatics (Hennur, Whitefield)
44. Subodha Skin And Cosmetic Clinic
45. Dr. Saurav's Skin Clinic (Kalyan Nagar, Indiranagar)
46. Dr. Sowmya's Skin and Hair Clinic
47. Advanced Gro Hair & Glo Skin Clinic (all branches)
48. Artistry Clinics (Cunningham Road, Koramangala)
49. Cura Care
50. Aarha AesthetiQ
51. Siri Clinic
52. Wizderm

### 4.3 Audited batch 3 — aesthetic

53. Contour Cosmetic Clinic (BTM Layout / Hulimavu)
54. Koza Aesthetic Care (all branches)
55. SS Aesthetic Clinic (Indiranagar)
56. Sanssouci Wellness Clinic (Mysuru)
57. Sparha Advanced Aesthetic Studio (Indiranagar)
58. Feather Touch Aesthetic Clinic & Academy (Jayanagar, Mysore)
59. Skin and Recon (Jayanagar 4th Block)
60. SkinFit Wellness (Koramangala)
61. RUA Skin & Hair Center (all branches)
62. Advanced GroHair GloSkin (Jayanagar and all branches)

### 4.4 Earlier scrape cohort

63. Mister Hair Clinic (Sadashivanagar + branches)
64. Looks Hair and Skin Clinic (Thanisandra, Sarjapur)
65. The Derma Theory Hair and Skin Clinic (HSR, JP Nagar)
66. AMINTRI Skin & Hair Clinic (Arekere)
67. Vrudhii Aesthetics (Soundarya Layout)
68. Dermaqure (T. Dasarahalli)
69. Beeyens Skin and Laser Clinic (Vidyaranyapura)
70. CLINIQUE Hair Transplant Centre / Dr. Idris (JP Nagar)

### 4.5 Dental cohort — excluded both as duplicates AND as out-of-vertical

Chisel Dental Clinic · Sky Dental Clinic · Dr Tanisha's Emerge Dental Studio · Aspen Dental Care · Reneu Dental Studio · Smiley House · Small Bites · Amaya Dental Clinic · Smile Xpressions · The Dental Axis · Aesthete Lifestyle Dentistry · Nikhilesh Dental Clinic · Smile World Dental Clinic · Tooth & Root Dental Clinic

### 4.6 Previously investigated and rejected — do not resurface

- **Rejuvaderm Skin Hair & Cosmetic Clinic / Dr. Aasawari Jachak** — Google listing claims HSR Layout but the doctor's real practice is in Nagpur; likely a cloned/spam listing. Website does not resolve.
- **Praba's VCare / Praba's Vcare Health Clinic Pvt Ltd** — large chain, 5,000+ Google Ads, multiple reviews alleging negligence with legal notices. Flagged do-not-pursue.

### 4.7 Known-eligible seed pool (surfaced in an earlier discovery pass, never audited)

These were seen once and set aside only because that batch had a per-vertical cap. They are **not excluded** — they are fair game and count toward your target if they pass every gate in §2.

**Hair transplant:** AK Clinics · Hair O Craft · DHT Hair Transplant · Haircosmos International Clinic · Dr Pais Hair Transplantation & PRP Clinic · Ultra Bio Hair Transplant Clinic · Asian Hair Transplant and Cosmetic Clinic · New Roots Skin Laser & Hair Transplant Clinic · Perfect U Hair Transplant & Skin Clinic

**Cosmetology / aesthetics:** Dr. Rekha's Vevili Cosmetology · Aura Skincare Clinic · Aesthetic+ Clinic · Dr. Akhil's Advanced Skin Hair & Cosmetic Clinic · Surakshaa Skin Hair & Cosmetology Clinic · KARO Aesthetic Clinic · Chitra's Lifeline Clinic · Dr. Harsha's ZIVA · Refom Advanced Cosmetology Center · NYRAA · Glow Up Skin & Wellness Clinic

**Dermatology:** iSkin Clinic · Vitals Skin and Hair Clinic · Skinray Skin & Hair Clinic · DERMA ELITE · Pigment Skin And Hair Clinic · Dr. Prithvi Raj – Aroha Skin and Hair Clinic

**Important:** do not simply hand these names back as your answer. They must go through the same discovery, verification, and gating pipeline as anything else, and they must not make up more than about half the final list. Run genuine discovery first; use this pool to fill gaps.

---

## 5. Apify operating rules (learned the hard way — follow these exactly)

### 5.1 Verified actor roster

| Purpose | Actor | Notes |
|---|---|---|
| Google Maps discovery + GBP + reviews + contacts + socials | `compass/crawler-google-places` | The workhorse. Returns metadata, phone/email/IG/FB/LinkedIn, reviews, review distribution. **Batch 5–6 clinics per call, set `timeout: 600`.** A 13-clinic run with 120 reviews each timed out at 500s having completed only 17 places. |
| Instagram profile | `apify/instagram-profile-scraper` | Returns bio, followers, post count, external URL, **and per-post like/comment counts in `latestPosts`** — read that nested field, it is free engagement signal. |
| Meta ads | `apify/facebook-ads-scraper` | One Ad Library search URL per clinic, `active_status=all`, batched. |
| Google ads | `scrapesage/google-ads-transparency-scraper` | `resultType: "advertisers"`. **Never skip this** — a Meta-only check has wrongly reported "no ads" in every single batch so far. |
| Website content | `apify/website-content-crawler` | **Cap at 5–8 pages per site.** An uncapped run hit 205 pages and timed out. Prioritize `/team`, `/about`, `/doctors`, `/services`, `/contact`. |

**Banned:** `s-r/google-maps-contact-details` — silently rate-limits (HTTP 429, 0 items) while still reporting SUCCEEDED.

**Off by default:** `apify/instagram-comment-scraper` — WhatsApp is the real booking engine for these clinics; commenters are a small minority. Post-level like/comment counts from the profile scraper are a sufficient proxy.

**Skip entirely this run:** any LinkedIn actor. `harvestapi/linkedin-profile-search` has its own daily free-tier cap (~10 calls) **separate from account credit**, and it fails *silently* with `statusMessage: "free user run limit reached"` while reporting SUCCEEDED. Not worth the budget on a discovery run.

### 5.2 Verification loop — run after EVERY actor call, no exceptions

Apify `SUCCEEDED` means "the code exited," **not** "the data is real."

1. **Coverage** — item count vs. inputs submitted. A silent drop is the strongest failure signal, stronger than any status field.
2. **Read the full `statusMessage`**, not just SUCCEEDED/FAILED. This is where `"free user run limit reached"` and `"Reached limit of max crawled places"` appear.
3. **Check the key-value store** for an `errors` or `summary` record — many actors write their real failure there.
4. **Field completeness with quirk awareness.** Wix/WordPress placeholder socials (`instagram.com/wix`, `facebook.com/ThemeRexStudio`, `info@mysite.com`) are a real finding about an unconfigured site — report them as such, don't mistake them for the clinic's real accounts.
5. **Cross-source corroboration** — where two pulls should agree (follower count, website URL), check that they do.
6. **Manual tie-break on load-bearing claims** — anything that reverses a prior finding, or is high-stakes, gets one direct check before being stated as fact.

**On a partial or timed-out run:** harvest what completed, then re-run only the missing slice. Never present partial coverage as complete.

### 5.3 Identity resolution

- **Generic names** ("Siri Clinic", "Aura Skincare") → set `maxCrawledPlacesPerSearch ≥ 2` and report candidates **with an explicit confidence level**. Never silently pick one.
- **Multi-branch** — 2+ distinct places for one query means a chain. Count branches; 2–4 branches is fine, 6+ is an auto-exclude. Branches diverge sharply — one clinic we audited had 9.4% negative reviews at one branch and 13.3% at the other.
- **Corporate-brand collisions** — if a search resolves to a large hospital/chain brand, confirm scale from its own Instagram bio or ad copy before treating it as a solo practice.
- **Geographic mismatch** — verify the clinic is actually in Karnataka. Same-name-different-city is common.

### 5.4 Cost discipline

- Budget is a **$5.00 Apify free-tier credit**. Confirm actual remaining balance before spending (read `https://api.apify.com/v2/users/me/limits` as an MCP resource).
- Set **`maxTotalChargeUsd` on every single call** so a runaway run errors out instead of quietly draining credit.
- Multi-branch chains multiply place count — budget for more places than clinic names.
- If remaining credit looks tight for the batch size, say so **before** running, with the estimate.

### 5.5 Anti-patterns — do not do these

- Substituting web search for a real scraper where a reliable one exists. (Web search *is* fine and encouraged for identity disambiguation, finding additional branches, and news/legal findings.)
- Reporting ad status from Meta alone, or skipping the Google Ads Transparency check.
- Treating `SUCCEEDED` as proof of data.
- Reporting review counts and star ratings without reading the actual negative review text.
- Inventing a wedge, or making "weak social presence" the wedge. Presence is not the product.
- Reporting a contact without a confidence label, or inferring one from a bare name match.
- Quoting patient names or clinical details beyond what the business finding requires.

---

## 6. Review reading — how we actually use it

Do not report averages. Averages hide everything.

- Pull the **distribution** (count of 5★/4★/3★/2★/1★ and the 1★ percentage), not just the mean.
- **Read the text of the lowest-rated reviews**, not just the ratings.
- The dominant complaint shape across every batch so far is **"paid in full upfront, then silence"** — package sessions not delivered, refunds ignored, no follow-up after payment. It recurred independently at four different clinics. It's the most screenshot-provable failure available to open an outbound conversation on. Look specifically for it.
- Also flag: **unanswered negative reviews** (owner never replied), and **recent** 1★ reviews left unanswered — these are the sharpest signals.

---

## 7. Wedge routing — how we turn a signal into an offer

For each qualified clinic, name **one** entry wedge, diagnosed from evidence. Never default to dead-lead reactivation. Priority when multiple breaks exist: whichever is (1) screenshot-provable, (2) closest to money already spent, (3) fastest to show a visible win.

| Signal combination | Entry wedge |
|---|---|
| Runs ads · response slow or none | Dead-lead reactivation |
| Runs ads · fast first reply · no qualification, no follow-up | Follow-up / nurture engine |
| Runs ads · greeting-only auto-reply, no qualification questions | Qualification + scoring upgrade |
| Runs ads · no website · thin GBP · fast human reply | Review engine first, infra second |
| No ads · website ✓ · high reviews · slow or no response | Instant response + organic capture |
| No ads · high review count but last review months old | Review reactivation |
| No ads · multi-session treatments (PRP, laser, packages) · 12+ months operating | Dead-patient reactivation |
| Practo Prime / JustDial paid listing · slow response | Dead-lead reactivation (aggregator) |
| WhatsApp fast · Instagram DMs slow or silent | IG → WhatsApp handoff automation |
| Reviews mention booking friction, waits, or ghosting after payment | No-show recovery |
| High-ticket quote given, never chased | Quote-decay follow-up |
| Fast human responder · manual chasing · one person holds it all | Systematize the hustle (keep the closer, remove the chasing) |
| Mega founder brand · overflow signals | Founder capacity protection — PARK tier |

**Mark the wedge as `HYPOTHESIS` unless it is provable from scraped evidence.** We run the mystery shop ourselves; you do not have response-time data, so any wedge that depends on how fast they reply is a hypothesis, not a finding. Say so explicitly.

---

**Confirm you have read and understood this. Do not call any tools yet. Reply with a one-paragraph confirmation of the ICP boundary and the exclusion rule, then wait for my run instructions.**
