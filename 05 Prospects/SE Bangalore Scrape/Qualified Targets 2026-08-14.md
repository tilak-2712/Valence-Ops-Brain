---
date_created: 2026-08-14
date_modified: 2026-08-14
status: reference
---
# SE Bangalore — qualified outreach targets

**Generated** 2026-08-14 · **Scrape date** 2026-08-10 · **Source** Google Maps via Apify
`compass/crawler-google-places`, 251 raw records → 234 unique places → 82 qualified.

Rebuilt from `results.json` in this same folder. Regenerate rather than hand-edit — the
pipeline is `process.py`, which re-runs against `raw/` at zero API cost.

---

## Selection

| Filter | Effect |
|---|---|
| 100+ reviews AND 4.0+ stars | applied at scrape-processing time |
| Deduped by placeId | 251 raw → 234 unique |
| Matched against the existing 80-clinic list | 19 excluded as already known |
| National chains removed | 18 held back per the mega-brand rule |
| Adjacent verticals removed | 12 dental-led / salon / homeopathy / hospital |
| **Has a website or an Instagram** | **44 of the 52 core targets** |
| Parked by Tilak, 14 Aug | 9 removed |
| **Working list** | **35 clinics** |

**Note on the website/Instagram filter.** It is not the discriminator it looks like. This
pipeline discovers an Instagram handle *by reading the clinic's own website*, so a clinic with
Instagram but no website is structurally impossible to detect here — and indeed zero of the 82
qualified clinics are in that state. "Website or Instagram" therefore resolves to "has a
website." The 8 core clinics excluded by it have neither, listed in Appendix B.

**Corollary worth respecting:** an `IG = N` below means *no Instagram link was found on the
clinic's website*. It does not mean the clinic has no Instagram. Do not build a "you have no
social presence" hook on this column without checking by hand first — it will read as wrong to
a founder who posts daily.

---

## Working list — 35 clinics

| # | Clinic | Rating (reviews) | Area | Phone | Website | IG | Handle | Followers |
|---|---|---|---|---|---|---|---|---|
| 1 | iSkin clinic | 4.9 (2317) | Bannerghatta Rd | +91 96201 22122 | Y | N | — | — |
| 2 | SkinOcare- Skin & Hair Clinic | 4.9 (1363) | Bannerghatta Rd | +91 90368 53031 | Y | Y | @skinocare.co.in | not scraped |
| 3 | SKYE - Skin & Hair Sciences Clinics | 4.7 (564) | HSR Layout | +91 90355 77577 | Y | N | — | — |
| 4 | CLINIQUE — Hair Transplant Centre, Dr Idris Hair… | 5 (509) | Bannerghatta Rd | +91 99002 12223 | Y | N | — | — |
| 5 | Rejuvaderm Skin Hair & Cosmetic Clinic | 4.7 (508) | HSR Layout | +91 80506 05605 | Y | N | — | — |
| 6 | Dr Shishira R J - Skin Aura Clinic | 4.9 (498) | HSR Layout | +91 63635 66673 | Y | N | — | — |
| 7 | SkinChime - Skin, Hair, Laser, Aesthetic, And… | 4.9 (469) | Bannerghatta Rd | +91 63606 89336 | Y | Y | @skinchimeclinic | 5,531 |
| 8 | The New Body Perfect & Smile Lounge - Cosmetic… | 4.5 (462) | Bannerghatta Rd | +91 93808 78455 | Y | N | — | — |
| 9 | Smiles N Aesthetics | 4.8 (421) | HSR Layout | +91 96205 92555 | Y | N | — | — |
| 10 | DERMA ELITE SKIN CARE CLINIC | 4.7 (402) | HSR Layout | +91 63608 28564 | Y | Y | @derma_elite_skincare | 1,857 |
| 11 | Aiconic Skin Clinic | 4.7 (393) | HSR Layout | +91 99018 64404 | Y | N | — | — |
| 12 | Dr. Pai Skin, Hair & Healthcare Clinic | 4.8 (384) | Bannerghatta Rd | +91 91486 77450 | Y | Y | @dr.paiskin | 145 |
| 13 | Clinique Internationale - J P Nagar | 4.9 (362) | Bannerghatta Rd | +91 96110 00221 | Y | personal | @drbhaveshgupta_ | not scraped |
| 14 | Yogin's Clinic | 4.8 (331) | Bannerghatta Rd | +91 97415 41834 | Y | N | — | — |
| 15 | AMINTRI SKIN & HAIR CLINIC | 4.7 (329) | Bannerghatta Rd | +91 82963 93637 | Y | Y | @amintri.skin | 10,267 |
| 16 | SkinCure Clinic - Dr. Ashish B Shetty | 4.8 (329) | Bannerghatta Rd | +91 80884 67354 | Y | N | — | — |
| 17 | Dr Veena Rao’s Aviva Skin Aesthetic | 4.9 (314) | Bannerghatta Rd | +91 97404 08994 | Y | N | — | — |
| 18 | Dr Harini BS | 4.9 (287) | HSR Layout | +91 90357 79902 | Y | N | — | — |
| 19 | Zenith Aesthetic Care- Arekere | 4.3 (274) | Bannerghatta Rd | +91 96060 73177 | Y | N | — | — |
| 20 | Dr Mradula s Aesthetica Skin Hair and Cosmetic… | 4.8 (264) | Bannerghatta Rd | +91 87627 17141 | Y | N | — | — |
| 21 | Epiderma Skin and Hair Clinic | 4.8 (258) | Bannerghatta Rd | +91 63648 46162 | Y | Y | @epidermaskinclinic | 201 |
| 22 | Tricho Derma Clinic | 4.6 (246) | Bannerghatta Rd | +91 97393 07939 | Y | N | — | — |
| 23 | The Derma Theory Hair and Skin Clinic | 4.7 (243) | HSR Layout, Sarjapur Rd | +91 98456 22511 | Y | Y | @thedermatheory | 5,996 |
| 24 | Skin Xperts Super-speciality Skin Hair Laser Clinics | 4.7 (240) | Bannerghatta Rd | +91 99001 02030 | Y | N | — | — |
| 25 | Vahin Wellness Centre | 4.1 (236) | HSR Layout | +91 80 4865 6537 | Y | N | — | — |
| 26 | Cutis Epicorium Skin Clinic HSR | 4.7 (235) | HSR Layout | +91 89708 22333 | Y | N | — | — |
| 27 | DYU Aesthetics | 4.9 (217) | HSR Layout | +91 74117 59852 | Y | Y | @dyuaesthetics | 15,944 |
| 28 | AHIS Aesthetics - The Hair Transplant Specialist in… | 5 (207) | HSR Layout | +91 72183 85814 | Y | N | — | — |
| 29 | Maira Wellness Clinic - HSR Layout | 4.6 (195) | HSR Layout | +91 90362 47272 | Y | N | — | — |
| 30 | Aesthetic Grandeur Multispeciality Clinic | 4.9 (172) | Electronic City | +91 63627 61736 | Y | Y | @aesthetic_grandeur_clinic | 12,837 |
| 31 | Arvique Aesthetics clinic | 4.9 (154) | Bannerghatta Rd | +91 83104 41523 | Y | Y | @arviqueclinic | 1,039 |
| 32 | Vivaa Wellness Center HSR Layout | 4.4 (142) | HSR Layout | +91 81230 02386 | Y | N | — | — |
| 33 | Krian Healthcare | 4.6 (140) | Bannerghatta Rd | +91 94831 82699 | Y | N | — | — |
| 34 | Allure Skin Hair Laser Clinic | 4.9 (139) | HSR Layout | +91 63663 53418 | Y | N | — | — |
| 35 | Dr Jyothshna's Skin Hair & Laser Clinic | 4.6 (134) | Electronic City | +91 89510 35430 | Y | N | — | — |

**Split:** 10 with a clinic Instagram · 1 with a personal-brand account · 24 website-only.

---

## Machine-readable

Full GBP titles, place IDs and website URLs for the working list. `placeId` is the stable key —
use it to re-scrape a specific clinic rather than re-running a whole area.

```json
[
 {
  "name": "iSkin clinic",
  "placeId": "ChIJfWimrRgVrjsRFp_PQuav3gU",
  "website": "https://www.iskinclinic.in/",
  "instagram": null,
  "followers": null,
  "rating": 4.9,
  "reviews": 2317,
  "phone": "+919620122122",
  "area": "Bannerghatta Rd",
  "category": "Dermatologist, Hair transplantation clinic"
 },
 {
  "name": "SkinOcare- Skin & Hair Clinic",
  "placeId": "ChIJX7bVmeIVrjsRDi3eT1Dw7-o",
  "website": "https://skinocareapp.com/",
  "instagram": "skinocare.co.in",
  "followers": null,
  "rating": 4.9,
  "reviews": 1363,
  "phone": "+919036853031",
  "area": "Bannerghatta Rd",
  "category": "Skin care clinic, Beauty supply store"
 },
 {
  "name": "SKYE - Skin & Hair Sciences Clinics",
  "placeId": "ChIJK3qJ-TkVrjsRhM6tilmWka4",
  "website": "https://clinicia.com/calendar/book?u=sukeshms",
  "instagram": null,
  "followers": null,
  "rating": 4.7,
  "reviews": 564,
  "phone": "+919035577577",
  "area": "HSR Layout",
  "category": "Skin care clinic, Dermatologist"
 },
 {
  "name": "CLINIQUE — Hair Transplant Centre, Dr Idris Hair Transplant Surgeon in Bangalore, Hair Clinic in J P Nagar",
  "placeId": "ChIJ0cjC9r0_rjsRGLZfeTNFGQM",
  "website": "https://hairclinique.in/",
  "instagram": null,
  "followers": null,
  "rating": 5,
  "reviews": 509,
  "phone": "+919900212223",
  "area": "Bannerghatta Rd",
  "category": "Hair transplantation clinic, Cosmetic surgeon"
 },
 {
  "name": "Rejuvaderm Skin Hair & Cosmetic Clinic | Dr.Aasawari Jachak - Skin Specialist Bangalore",
  "placeId": "ChIJeWoh9nEVrjsRcrWEmrE5_rs",
  "website": "https://rejuvaderm.in/",
  "instagram": null,
  "followers": null,
  "rating": 4.7,
  "reviews": 508,
  "phone": "+918050605605",
  "area": "HSR Layout",
  "category": "Dermatologist, Cosmetic surgeon"
 },
 {
  "name": "Dr Shishira R J - Skin Aura Clinic",
  "placeId": "ChIJR5a7TGQVrjsRO6G4kUZ3wUI",
  "website": "https://skinauraclinichsr.com/",
  "instagram": null,
  "followers": null,
  "rating": 4.9,
  "reviews": 498,
  "phone": "+916363566673",
  "area": "HSR Layout",
  "category": "Dermatologist, Cosmetic surgeon"
 },
 {
  "name": "SkinChime - Skin, Hair, Laser, Aesthetic, And Cosmetic Clinic",
  "placeId": "ChIJqaZJU28VrjsR4RxN4_-40hk",
  "website": "https://www.skinchime.com/",
  "instagram": "skinchimeclinic",
  "followers": 5531,
  "rating": 4.9,
  "reviews": 469,
  "phone": "+916360689336",
  "area": "Bannerghatta Rd",
  "category": "Skin care clinic, Cosmetic surgeon"
 },
 {
  "name": "The New Body Perfect & Smile Lounge - Cosmetic Clinic",
  "placeId": "ChIJpw2QiwIVrjsRQIAfR4ROyXg",
  "website": "https://www.thebodyperfect.in/",
  "instagram": null,
  "followers": null,
  "rating": 4.5,
  "reviews": 462,
  "phone": "+919380878455",
  "area": "Bannerghatta Rd",
  "category": "Weight loss service, Electrolysis hair removal service"
 },
 {
  "name": "Smiles N Aesthetics",
  "placeId": "ChIJ70QqIbkVrjsRdYwHMvmhJL4",
  "website": "https://smilesnaesthetics.com/",
  "instagram": null,
  "followers": null,
  "rating": 4.8,
  "reviews": 421,
  "phone": "+919620592555",
  "area": "HSR Layout",
  "category": "Dental clinic, Cosmetic dentist"
 },
 {
  "name": "DERMA ELITE SKIN CARE CLINIC | Dermatologist in HSR Layout, Bengaluru - Dr. Shilpa YK",
  "placeId": "ChIJGeQ_RfoVrjsROMvAmEUyg4c",
  "website": "http://dermaelite.in/",
  "instagram": "derma_elite_skincare",
  "followers": 1857,
  "rating": 4.7,
  "reviews": 402,
  "phone": "+916360828564",
  "area": "HSR Layout",
  "category": "Doctor"
 },
 {
  "name": "Aiconic Skin Clinic: Skin, Hair and Cosmetic Dermatology",
  "placeId": "ChIJHR8_QGoVrjsRRjUS4r0whDo",
  "website": "http://drnamratasingh.com/",
  "instagram": null,
  "followers": null,
  "rating": 4.7,
  "reviews": 393,
  "phone": "+919901864404",
  "area": "HSR Layout",
  "category": "Dermatologist, Cosmetic surgeon"
 },
 {
  "name": "Dr. Pai Skin, Hair & Healthcare Clinic",
  "placeId": "ChIJb76fbXdrrjsRACx-D2ynPY4",
  "website": "https://www.drpaiskinhair.in/",
  "instagram": "dr.paiskin",
  "followers": 145,
  "rating": 4.8,
  "reviews": 384,
  "phone": "+919148677450",
  "area": "Bannerghatta Rd",
  "category": "Dermatologist, Skin care clinic"
 },
 {
  "name": "Clinique Internationale - J P Nagar",
  "placeId": "ChIJXzhwukM9rjsRYUuGaNOtFwM",
  "website": "https://www.cosmeticclinique.in/",
  "instagram": "drbhaveshgupta_",
  "followers": null,
  "rating": 4.9,
  "reviews": 362,
  "phone": "+919611000221",
  "area": "Bannerghatta Rd",
  "category": "Laser hair removal service"
 },
 {
  "name": "Yogin's Clinic",
  "placeId": "ChIJaYj7mSgVrjsRGXiwDsnCtII",
  "website": "https://yoginsclinic.com/",
  "instagram": null,
  "followers": null,
  "rating": 4.8,
  "reviews": 331,
  "phone": "+919741541834",
  "area": "Bannerghatta Rd",
  "category": "Skin care clinic"
 },
 {
  "name": "AMINTRI SKIN & HAIR CLINIC | DERMATOLOGIST | LASERS | AESTHETICS | DR. MITHILA RAVINDRANATH",
  "placeId": "ChIJQQg2CK8VrjsRvmvpw-Lz3yw",
  "website": "http://www.amintri.com/",
  "instagram": "amintri.skin",
  "followers": 10267,
  "rating": 4.7,
  "reviews": 329,
  "phone": "+918296393637",
  "area": "Bannerghatta Rd",
  "category": "Dermatologist, Doctor"
 },
 {
  "name": "SkinCure Clinic - Dr. Ashish B Shetty",
  "placeId": "ChIJs8O3INkUrjsRv8x7K-aKuoA",
  "website": "https://www.shettysskincure.com/",
  "instagram": null,
  "followers": null,
  "rating": 4.8,
  "reviews": 329,
  "phone": "+918088467354",
  "area": "Bannerghatta Rd",
  "category": "Dermatologist, Hair transplantation clinic"
 },
 {
  "name": "Dr Veena Rao’s Aviva Skin Aesthetic",
  "placeId": "ChIJ9zC9pXgVrjsR2idnvqYBhMA",
  "website": "http://www.avivaskinaesthetics.com/",
  "instagram": null,
  "followers": null,
  "rating": 4.9,
  "reviews": 314,
  "phone": "+919740408994",
  "area": "Bannerghatta Rd",
  "category": "Skin care clinic, Laser hair removal service"
 },
 {
  "name": "Dr Harini BS (Aesthetic International)",
  "placeId": "ChIJCx3Y1CkVrjsRAdn7m9JkVsc",
  "website": "https://consultdrharini.in/",
  "instagram": null,
  "followers": null,
  "rating": 4.9,
  "reviews": 287,
  "phone": "+919035779902",
  "area": "HSR Layout",
  "category": "Skin care clinic, Cosmetic surgeon"
 },
 {
  "name": "Zenith Aesthetic Care- Arekere",
  "placeId": "ChIJd_d5rPkVrjsRDskFIrxd9PE",
  "website": "https://zenithaesthetic.com/",
  "instagram": null,
  "followers": null,
  "rating": 4.3,
  "reviews": 274,
  "phone": "+919606073177",
  "area": "Bannerghatta Rd",
  "category": "Skin care clinic"
 },
 {
  "name": "Dr Mradula s Aesthetica Skin Hair and Cosmetic Clinic",
  "placeId": "ChIJEWveqUcVrjsRfelR5xcu_J4",
  "website": "http://aestheticaskinclinic.in/",
  "instagram": null,
  "followers": null,
  "rating": 4.8,
  "reviews": 264,
  "phone": "+918762717141",
  "area": "Bannerghatta Rd",
  "category": "Skin care clinic"
 },
 {
  "name": "Epiderma Skin and Hair Clinic",
  "placeId": "ChIJSf0kiRUVrjsROJLClGqTIPo",
  "website": "https://www.epiderma.in/",
  "instagram": "epidermaskinclinic",
  "followers": 201,
  "rating": 4.8,
  "reviews": 258,
  "phone": "+916364846162",
  "area": "Bannerghatta Rd",
  "category": "Dermatologist"
 },
 {
  "name": "Tricho Derma Clinic",
  "placeId": "ChIJ65Mz7wwVrjsRkMfle5OhCT0",
  "website": "https://www.trichodermaclinic.com/",
  "instagram": null,
  "followers": null,
  "rating": 4.6,
  "reviews": 246,
  "phone": "+919739307939",
  "area": "Bannerghatta Rd",
  "category": "Skin care clinic, Cosmetic surgeon"
 },
 {
  "name": "The Derma Theory Hair and Skin Clinic",
  "placeId": "ChIJB1t3mI8VrjsR-kypXLx4mcA",
  "website": "https://thedermatheory.care/gfc-treatment-in-bangalore/",
  "instagram": "thedermatheory",
  "followers": 5996,
  "rating": 4.7,
  "reviews": 243,
  "phone": "+919845622511",
  "area": "HSR Layout, Sarjapur Rd",
  "category": "Dermatologist, Cosmetic surgeon"
 },
 {
  "name": "Skin Xperts Super-speciality Skin Hair Laser Clinics - Headed by Professor Dr.Eshwari.L with 25 yrs experience",
  "placeId": "ChIJ30TdS7MVrjsRZlengoZaIWI",
  "website": "http://www.jayanagarskinxperts.com/",
  "instagram": null,
  "followers": null,
  "rating": 4.7,
  "reviews": 240,
  "phone": "+919900102030",
  "area": "Bannerghatta Rd",
  "category": "Skin care clinic, Cosmetic surgeon"
 },
 {
  "name": "Vahin Wellness Centre",
  "placeId": "ChIJD1LD640UrjsRfwFNjkrkXl8",
  "website": "http://vahinwellness.com/",
  "instagram": null,
  "followers": null,
  "rating": 4.1,
  "reviews": 236,
  "phone": "+918048656537",
  "area": "HSR Layout",
  "category": "Skin care clinic, Wellness center"
 },
 {
  "name": "Cutis Epicorium Skin Clinic HSR",
  "placeId": "ChIJb-h1pEMVrjsR7P-YqFqDt9Q",
  "website": "https://crm.cliniceo.app/clinic/patient-dashboard/appointments?businessId=686f940857bf7f0a06f6af3f",
  "instagram": null,
  "followers": null,
  "rating": 4.7,
  "reviews": 235,
  "phone": "+918970822333",
  "area": "HSR Layout",
  "category": "Dermatologist"
 },
 {
  "name": "DYU Aesthetics",
  "placeId": "ChIJ8adN3ZEUrjsRqIy3ifFYVuA",
  "website": "https://www.dyuaesthetics.com/",
  "instagram": "dyuaesthetics",
  "followers": 15944,
  "rating": 4.9,
  "reviews": 217,
  "phone": "+917411759852",
  "area": "HSR Layout",
  "category": "Skin care clinic"
 },
 {
  "name": "AHIS Aesthetics - The Hair Transplant Specialist in HSR Layout, Bangalore",
  "placeId": "ChIJ5_OSFAAVrjsR6NRIrh7udFU",
  "website": "https://ahisaesthetics.com/",
  "instagram": null,
  "followers": null,
  "rating": 5,
  "reviews": 207,
  "phone": "+917218385814",
  "area": "HSR Layout",
  "category": "Hair transplantation clinic, Dermatologist"
 },
 {
  "name": "Maira Wellness Clinic - HSR Layout",
  "placeId": "ChIJzxJUlDYVrjsRRzyGK0NEc9E",
  "website": "http://www.mairawellness.com/",
  "instagram": null,
  "followers": null,
  "rating": 4.6,
  "reviews": 195,
  "phone": "+919036247272",
  "area": "HSR Layout",
  "category": "Skin care clinic, Laser hair removal service"
 },
 {
  "name": "Aesthetic Grandeur Multispeciality Clinic",
  "placeId": "ChIJh648aNMVrjsReDZWL0MqbwY",
  "website": "http://aestheticgrandeurclinics.com/",
  "instagram": "aesthetic_grandeur_clinic",
  "followers": 12837,
  "rating": 4.9,
  "reviews": 172,
  "phone": "+916362761736",
  "area": "Electronic City",
  "category": "Skin care clinic, Dermatologist"
 },
 {
  "name": "Arvique Aesthetics clinic |SKIN|HAIR|LASER|BODY",
  "placeId": "ChIJre861KIVrjsRBmS6v0cpUtk",
  "website": "https://arvique.com/",
  "instagram": "arviqueclinic",
  "followers": 1039,
  "rating": 4.9,
  "reviews": 154,
  "phone": "+918310441523",
  "area": "Bannerghatta Rd",
  "category": "Skin care clinic, Dermatologist"
 },
 {
  "name": "Vivaa Wellness Center HSR Layout",
  "placeId": "ChIJD47iUOEVrjsRwUPCKrEhdR8",
  "website": "http://www.vivaawellnesscenter.com/",
  "instagram": null,
  "followers": null,
  "rating": 4.4,
  "reviews": 142,
  "phone": "+918123002386",
  "area": "HSR Layout",
  "category": "Skin care clinic, Hair removal service"
 },
 {
  "name": "Krian Healthcare (Formerly Dr.Sudheendra’s Skin & Hair clinic)",
  "placeId": "ChIJTdF03EYVrjsRtYKX5GUwVTk",
  "website": "https://krianhealthcare.com/",
  "instagram": null,
  "followers": null,
  "rating": 4.6,
  "reviews": 140,
  "phone": "+919483182699",
  "area": "Bannerghatta Rd",
  "category": "Skin care clinic, General practitioner"
 },
 {
  "name": "Allure Skin Hair Laser Clinic. Laser hair reduction, GFC, PRP, chemical peel, Co2, MNRF, pigmentation, Acne Scar",
  "placeId": "ChIJNfnciqYVrjsRX-6gj-qpkrE",
  "website": "https://allureskincare.co/",
  "instagram": null,
  "followers": null,
  "rating": 4.9,
  "reviews": 139,
  "phone": "+916366353418",
  "area": "HSR Layout",
  "category": "Skin care clinic, Cosmetic surgeon"
 },
 {
  "name": "Dr Jyothshna's Skin Hair & Laser Clinic( best dermatologist in Electronic City)",
  "placeId": "ChIJ5azn_6htrjsRGDFHst15vaE",
  "website": "https://www.instagram.com/dr_jyothshnaskinclinic?igsh=MXU5dXJpeWV5ejNmdw==",
  "instagram": null,
  "followers": null,
  "rating": 4.6,
  "reviews": 134,
  "phone": "+918951035430",
  "area": "Electronic City",
  "category": "Skin care clinic, Cosmetic surgeon"
 }
]
```

---

## Outstanding work that needs an API key

Three jobs are queued against this list. All were blocked on 14 Aug because the Apify key in the
working session could not reach the account that owns the 10 Aug runs.

### 1. Missing follower counts (1) — trivial cost

These handles are confirmed and tied to the right business; only the follower number failed to
fetch, because the handle came from a website link rather than an enriched profile record.

| Clinic | Handle |
|---|---|
| SkinOcare- Skin & Hair Clinic | @skinocare.co.in |

### 2. Two areas were never properly measured

Sarjapur Rd and Bommanahalli returned 37 and 4 raw records off broken polygons — the geocoder
degenerated them to tiny slivers. Clinics tagged to those areas in this file are real; the
*absence* of a clinic there proves nothing. Corrected polygons, ready to run:

**Sarjapur Rd** (Agara → Dommasandra corridor)
```json
{"type":"Polygon","coordinates":[[[77.63,12.855],[77.785,12.855],[77.785,12.945],[77.63,12.945],[77.63,12.855]]]}
```

**Bommanahalli**
```json
{"type":"Polygon","coordinates":[[[77.596,12.878],[77.65,12.878],[77.65,12.925],[77.596,12.925],[77.596,12.878]]]}
```

Estimated $1–2 at free-tier rates ($0.004/place scraped + $0.002/place contact enrichment).
The 10 Aug run overshot its $10 cap and landed at $12.14 — cost scales with the number of map
segments a polygon splits into, not with the per-term cap. Electronic City alone split into 20.
Set the cap low and check segment count before committing.

### 3. Chain re-check

Chain detection in `process.py` is a hardcoded 11-name list. La Densitae passed straight through
it and was only caught by eye on 14 Aug — it is a large chain and is parked in Appendix A. Other
names in the working list that could be multi-location on the same basis, **unverified**:
CLINIQUE / Dr Idris, Clinique Internationale, AHIS Aesthetics. A placeId-level brand-name count
across `raw/` would catch this shape and costs nothing.

---

## Appendix A — parked, do not work

| Clinic | Rating (reviews) | Reason |
|---|---|---|
| La Densitae Clinic Bangalore | 4.8 (519) | parked 14 Aug — large chain |
| Pioneer Advanced Hair Transplant Centre | 4.7 (324) | dropped by Tilak 14 Aug |
| Akera - Dermatologist, Skin & Hair Clinic - HSR… | 4.9 (315) | dropped by Tilak 14 Aug |
| Ikya skin clinic | 4.9 (160) | dropped by Tilak 14 Aug |
| Dr. Regina Joseph | 4.9 (131) | dropped by Tilak 14 Aug |
| Neo Max – Facial Aesthetics & Hair Transplant Centre | 5 (128) | dropped by Tilak 14 Aug |
| Dr.Renu's Skin & Hair Clinic | 4.5 (126) | dropped by Tilak 14 Aug |
| Kliaro Derma Clinic | 4.8 (111) | dropped by Tilak 14 Aug |
| Layers Skin & Hair Clinic HSR Layout, Bengaluru | 4.5 (109) | dropped by Tilak 14 Aug |

Also held back and **not** in this file: 18 national chains and 12 adjacent-vertical clinics.
Both groups are in `New Clinics Table 2026-08-10.md` sections B and C, and in `results.json`.

## Appendix B — core clinics with neither website nor Instagram (8)

Excluded from the working list by the filter, not by judgment. They clear the review bar and are
not chains — a phone-first or walk-in approach would still reach them.

| Clinic | Rating (reviews) | Area | Phone |
|---|---|---|---|
| 5 Elements - Skin, Hair, Laser, Cosmetology and… | 4.4 (305) | Bannerghatta Rd, HSR Layout | +91 73377 16622 |
| Dr Bhat Skin Clinic | 4.9 (258) | HSR Layout | +91 73494 95034 |
| Trichologist | 4.9 (212) | HSR Layout | — |
| Neo Hair and skin clinic | 4.7 (201) | Electronic City | +91 93796 66000 |
| Dr.Uday's advanced Skin Hair and ENT Clinic | 4.9 (184) | Bannerghatta Rd | +91 70223 73013 |
| Elara Glow Aesthetic Clinic | 4.7 (154) | Bannerghatta Rd | +91 63635 19679 |
| Dr Fiona Sequeira - Dermatologist | 4.7 (153) | HSR Layout, Sarjapur Rd | +91 98455 45555 |
| Advaya Skin Clinic | 4.5 (121) | Bannerghatta Rd | +91 63648 00547 |

## Data-quality traps carried over from the 10 Aug run

**Platform handles.** Instagram links scraped from website footers included `@wix` (880k, a
"built with Wix" badge), `@tv` (Instagram's own account, 1.9M) and `@ekacarehq` (a healthtech
vendor). These were discarded, not reported. Skin Xperts' *only* Instagram link was the Wix
badge — it reads `IG = N` here and `IG = Y` in the older `New Clinics Table 2026-08-10.md`, which was built
before the platform filter ran. This file is the corrected one.

**Unrelated handles.** Where a website links an Instagram account bearing no relation to the
clinic name, the follower count is withheld rather than attributed. One case survives in the
working list, marked `IG = personal`: Clinique Internationale links `@drbhaveshgupta_`, the
doctor's personal account rather than a clinic brand. Real presence, different outreach angle.

**Degenerate geocoding.** A polygon that fails to resolve does not error — it silently shrinks
and returns a near-empty result that looks like a genuine finding. Check the reported area of
every polygon against what you intended before trusting a low count.


---
Related: [[05 Prospects/SE Bangalore Scrape/New Clinics Table 2026-08-10|New Clinics Table 2026-08-10]] · [[05 Prospects/Scrape 2026-07-19/The Derma Theory|The Derma Theory]]
