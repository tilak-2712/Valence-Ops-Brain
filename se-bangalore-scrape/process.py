#!/usr/bin/env python3
"""Merge, filter, dedupe and exclusion-match the SE Bangalore clinic scrape."""
import json, re, glob, os
from difflib import SequenceMatcher

RAW = os.path.join(os.path.dirname(__file__), "raw")

AREA_FILES = {
    "HSR Layout": "hsr.json",
    "Electronic City": "eleccity.json",
    "Bannerghatta Rd": "bannerghatta.json",
    "Sarjapur Rd": "sarjapur_partial.json",
    "Bommanahalli": "bommanahalli_partial.json",
}

ALREADY_SCRAPED = [
"Aura Cutisurg Clinic","Clinic Next Face","Dr. Sculpt Aesthetic Clinic",
"Dr. Keshav's Skin, Hair, Cosmetic & Laser Clinic","Ministry of Skin","DNA Skin Clinic",
"Dr. Karishma Aesthetics","Dr. Ritika Shanmugam Skin, Hair & Aesthetic Clinic",
"Dr. Dixit Cosmetic Dermatology Clinic","Anew Cosmetic Clinic","Dr. Swetha's Cosmoderm Centre",
"Dr. Juvita Aesthetics","Vtiara Hair & Skin Clinic","Iridescent Aesthetics",
"Dr. Tina's Skin Solutionz","Cozmo Blis","The Glow Clinic","Skinology Centre",
"AvatarLuxe Aestheticians","Idha Skin, Hair & Laser Clinic","LA CROWN Dermatology Aesthetic Clinic",
"Aesthetica Veda Clinic","Sparsha Skin Care Clinic","Pruthvi Children's and Skin Clinic",
"Pranav Skin and Cosmetology Clinic","Venkat Center for Aesthetic Health","DermaZeal Clinic",
"Dermaville Skin Clinic","Dr. Rai's Skin & Hair Clinic",
"Dr K Srinivasa Murthy's Skin & Cosmetology Centre","Ridhi's Skin and Hair Transplant Clinic",
"CosMediQ Hair Transplant and Skin Clinic","Nishka Skin Clinic","ProSkincare Esthetics",
"Neo Follicle Hair Transplant Clinic","Skinmatics","Subodha Skin And Cosmetic Clinic",
"Dr. Saurav's Skin Clinic","Dr. Sowmya's Skin and Hair Clinic","Advanced Gro Hair & Glo Skin Clinic",
"Artistry Clinics","Cura Care","Praba's Vcare Health Clinic","Aarha AesthetiQ",
"Contour Cosmetic Clinic","Koza Aesthetic Care","SS Aesthetic Clinic","Sanssouci Wellness Clinic",
"Sparha Advanced Aesthetic Studio","Feather Touch Aesthetic Clinic & Academy","Skin and Recon",
"SkinFit Wellness","RUA Skin & Hair Center","Advanced GroHair GloSkin","Chisel Dental Clinic",
"Sky Dental Clinic","Dr Tanisha's Emerge Dental Studio","Aspen Dental Care","Reneu Dental Studio",
"Smiley House","Small Bites","Amaya Dental Clinic","Smile Xpressions","The Dental Axis",
"Aesthete Lifestyle Dentistry","Gejje's Marvella","Haircosmos International","Ara Skin Clinic",
"Dr. Priya's Skin & Hair Clinic","Akera Health","Derma Solutions","Routines by Dr. Apoorva",
"Theory of Skin","Dermatonik","VIDA Skin & Hair Transplant","Vitals Klinic","Krity 360",
"D White Feather","Dr AG Skin & Hair Clinic","Project Skin",
]

# Categories that are on-target for skin / aesthetic / derm / cosmetology / hair
RELEVANT_KEYWORDS = [
    "dermatolog","skin","hair","aesthetic","cosmet","laser","plastic surgeon","plastic surgery",
    "tricholog","medical spa","med spa","beauty","wellness","weight loss","surgeon","clinic",
]
# Categories to drop outright as noise
NOISE_KEYWORDS = [
    "dental","dentist","orthodont","hospital","general practitioner","pediatrician","paediatric",
    "gynecolog","physiotherap","ayurved","pharmacy","diagnostic","veterinar","eye care",
    "optician","ophthalmolog","nutritionist","dietitian","gym","fitness","salon","spa","barber",
    "massage","nail","tattoo","yoga","gastroenterolog","orthoped","ent ","psychiatr","gramtoolkit",
]

# Instagram handles belonging to platforms/vendors, not the clinic — picked up from website
# footers ("built with Wix"), embedded IG widgets, and healthtech vendor badges.
PLATFORM_HANDLES = {
    "tv","wix","instagram","facebook","meta","wordpress","squarespace","godaddy","shopify",
    "google","youtube","whatsapp","practo","ekacarehq","justdial","linkedin","twitter",
    "zoho","hubspot","canva","explore","reels","wixstudio",
}

# Business types outside the skin/aesthetic/derm/cosmetology/hair brief
ADJACENT_PATTERNS = [
    "salon","makeup","school of beauty","academy","homeopathy","ayurved","panchkarma",
    "allergy","asthma","pulmonolog","hospital","diagnostic","dental","dentist",
    "electrolysis","physiotherap",
]

# Large national / multi-city chains — MEMORY.md defers mega-brands until Case Study #1 exists
CHAIN_PATTERNS = [
    "kaya clinic","oliva","kosmoderma","vlcc","batra","bodycraft","cutis international",
    "rxdx","apollo","looks studio","partha dental",
]

def norm(s):
    s = (s or "").lower()
    s = s.replace("&", " and ")
    s = re.sub(r"[^a-z0-9]+", " ", s)
    s = re.sub(r"\b(dr|drs|the|clinic|clinics|klinic|centre|center|by|and|in|at|bangalore|"
               r"bengaluru|hsr|layout|jp|nagar|jayanagar|electronic|city|health|healthcare)\b", " ", s)
    return re.sub(r"\s+", " ", s).strip()

# Clinics known to be in Batch 1 / the Notion tracker per CLAUDE.md + MEMORY.md, but absent from
# the 80-name list supplied this session. Treated as already-known so they aren't sold as "new".
TRACKER_EXTRAS = ["Evenly Skin and Hair Clinic", "Sapphire Skin & Aesthetics Clinic"]

NORM_EXCLUDE = [(n, norm(n)) for n in ALREADY_SCRAPED + TRACKER_EXTRAS]

# Instagram handle -> exclusion-list clinic, for cases where the GBP title differs from the
# known name but the social account proves identity (e.g. "Vitals Hair and Skin" -> @vitalsklinic).
HANDLE_ALIASES = {
    "vitalsklinic": "Vitals Klinic",
    "adgrohairclinicofficial": "Advanced GroHair GloSkin",
    "akerahealth": "Akera Health",
}

# Words too generic to prove two clinics are the same business.
GENERIC = {
    "skin","hair","aesthetic","aesthetics","derma","dermatology","dermatologist","cosmetic",
    "cosmetics","cosmetology","laser","lasers","care","beauty","studio","surgery","transplant",
    "solutions","wellness","advanced","best","super","speciality","specialist","body","face",
    "glow","medical","aesthetica","clinique","international","hospital","multispeciality",
}

def distinctive(s):
    return {w for w in s.split() if len(w) >= 3 and w not in GENERIC}

def excluded_match(title):
    t = norm(title)
    if not t:
        return None
    dt = distinctive(t)
    for orig, n in NORM_EXCLUDE:
        if not n:
            continue
        if t == n:
            return orig, "exact"
        dn = distinctive(n)
        # A non-exact match must share at least one distinctive (non-generic) word,
        # otherwise "Dr Pai Skin & Hair" wrongly matches "Dr AG Skin & Hair".
        if not (dt & dn):
            continue
        if len(t) >= 8 and len(n) >= 8 and (t in n or n in t):
            return orig, "substring"
        if SequenceMatcher(None, t, n).ratio() >= 0.88:
            return orig, "fuzzy"
    return None

def is_noise(cats, title):
    blob = " ".join(cats).lower() + " " + (title or "").lower()
    if any(k in blob for k in NOISE_KEYWORDS):
        if not any(k in blob for k in ["dermatolog","skin","hair transplant","aesthetic","cosmetolog"]):
            return True
    return False

# ---- load & merge ----
records, seen_place = {}, {}
for area, fn in AREA_FILES.items():
    path = os.path.join(RAW, fn)
    if not os.path.exists(path):
        continue
    data = json.loads(open(path).read(), strict=False)
    for it in data:
        pid = it.get("placeId") or it.get("title")
        if pid in records:
            records[pid]["areas"].add(area)
            continue
        it["areas"] = {area}
        records[pid] = it

print(f"merged unique places: {len(records)}")

qualified, excluded, below_bar, noise = [], [], [], []
for pid, it in records.items():
    title = (it.get("title") or "").strip()
    rc = it.get("reviewsCount") or 0
    ts = it.get("totalScore") or 0
    cats = it.get("categories") or ([it.get("categoryName")] if it.get("categoryName") else [])
    cats = [c for c in cats if c]
    if it.get("permanentlyClosed") or it.get("temporarilyClosed"):
        continue
    if is_noise(cats, title):
        noise.append((title, ", ".join(cats[:2]), rc))
        continue
    if rc < 100 or ts < 4.0:
        below_bar.append((title, ts, rc))
        continue
    web = it.get("website")
    igs = it.get("instagrams") or []
    profs = it.get("instagramProfiles") or []
    followers, handle = None, None
    cands = []
    for p in profs:
        u = (p.get("username") or "").lower()
        if not u or u in PLATFORM_HANDLES:
            continue
        cands.append((u, p.get("followersCount")))
    for u in [i.rstrip("/").split("/")[-1].lower() for i in igs]:
        if u and u not in PLATFORM_HANDLES and u not in [c[0] for c in cands]:
            cands.append((u, None))
    # prefer a handle that shares a word-stem with the clinic name
    def affinity(u):
        nm = set(re.findall(r"[a-z]{4,}", norm(title)))
        return any(w[:5] in u for w in nm) or any(u[i:i+5] in norm(title).replace(" ","") for i in range(max(1,len(u)-4)))
    if cands:
        matched = [c for c in cands if affinity(c[0])]
        pick = matched[0] if matched else cands[0]
        handle, followers = pick[0], pick[1]
        if not matched:
            handle, followers = pick[0] + " (UNVERIFIED)", None

    # Exclusion check: by name, or by Instagram handle when the GBP title differs from the
    # known clinic name but the social account proves they are the same business.
    m = excluded_match(title)
    if not m:
        h = (handle or "").replace(" (UNVERIFIED)", "")
        if h in HANDLE_ALIASES:
            m = (HANDLE_ALIASES[h], "instagram-handle")
    if m:
        excluded.append((title, m[0], m[1], ts, rc))
        continue

    qualified.append({
        "name": title,
        "rating": ts,
        "reviews": rc,
        "website": "Y" if web else "N",
        "website_url": web or "",
        "instagram": "Y" if (igs or profs) else "N",
        "handle": handle or "",
        "followers": followers,
        "areas": ", ".join(sorted(it["areas"])),
        "cats": ", ".join(cats[:2]),
    })

for q in qualified:
    low = q["name"].lower()
    q["is_chain"] = any(c in low for c in CHAIN_PATTERNS)
    q["is_adjacent"] = any(a in low for a in ADJACENT_PATTERNS)

core     = [q for q in qualified if not q["is_chain"] and not q["is_adjacent"]]
chains   = [q for q in qualified if q["is_chain"]]
adjacent = [q for q in qualified if q["is_adjacent"] and not q["is_chain"]]

for lst in (core, chains, adjacent):
    lst.sort(key=lambda x: -x["reviews"])
qualified.sort(key=lambda x: (-(x["followers"] or 0), -x["reviews"]))

out = {"qualified": qualified, "excluded": excluded, "below_bar": below_bar, "noise": noise}
json.dump(out, open(os.path.join(os.path.dirname(__file__), "results.json"), "w"), indent=1)

print(f"CORE targets (new)        : {len(core)}")
print(f"Chains (defer per MEMORY) : {len(chains)}")
print(f"Adjacent / other business : {len(adjacent)}")
print(f"EXCLUDED (already on list): {len(excluded)}")
print(f"below 100 rev / 4.0       : {len(below_bar)}")
print(f"category noise            : {len(noise)}")

def shorten(n):
    n = re.split(r"\s*[|:]\s*", n)[0]
    return n[:58].strip()

def table(rows, heading):
    print(f"\n### {heading}\n")
    print("| # | Clinic | Rating & Reviews | Web | IG | Followers | Area |")
    print("|---|---|---|---|---|---|---|")
    for i, q in enumerate(rows, 1):
        if q["followers"] is not None:
            f = f"{q['followers']:,}"
        elif q["instagram"] == "N":
            f = "—"
        else:
            f = "unconfirmed"
        print(f"| {i} | {shorten(q['name'])} | {q['rating']} ({q['reviews']}) | {q['website']} | {q['instagram']} | {f} | {q['areas']} |")

table(core, "A. CORE NEW TARGETS")
table(chains, "B. NATIONAL CHAINS — defer per MEMORY.md mega-brand rule")
table(adjacent, "C. ADJACENT (dental-led / salon / homeopathy / hospital) — your call")

print("\n### D. EXCLUDED as already on your list\n")
for t, m, how, ts, rc in excluded:
    print(f"  {shorten(t)}  ->  {m}  [{how}]  {ts} ({rc})")
