import json, glob, os, re

BASE = "/Users/stilak/Documents/Valence-Ops-Sales/se-bangalore-scrape"
d = json.load(open(os.path.join(BASE, "results.json")))

# raw lookup for phone + placeId
raw = {}
for f in glob.glob(os.path.join(BASE, "raw", "*.json")):
    for it in json.load(open(f)):
        t = it.get("title")
        if t and t not in raw:
            raw[t] = it

PARKED = {
    "pioneer": "dropped by Tilak 14 Aug",
    "akera": "dropped by Tilak 14 Aug",
    "ikya": "dropped by Tilak 14 Aug",
    "regina joseph": "dropped by Tilak 14 Aug",
    "neo max": "dropped by Tilak 14 Aug",
    "renu": "dropped by Tilak 14 Aug",
    "kliaro": "dropped by Tilak 14 Aug",
    "layers": "dropped by Tilak 14 Aug",
    "la densitae": "parked 14 Aug — large chain",
}

def parked_reason(name):
    low = name.lower()
    for k, v in PARKED.items():
        if k in low:
            return v
    return None

def short(name, cap=52):
    """Trim GBP keyword-stuffing tails for a readable display name.

    Full titles survive in the machine-readable block, so truncating here is lossless.
    """
    n = re.split(r"\s*[|:(]\s*|(?<!Dr)(?<!Mr)\.\s+", name)[0].strip().rstrip(".,-")
    n = re.split(r"\s+-\s+(?:The\s+)?(?:Best|Headed|Laser)\b", n)[0].strip()
    if len(n) > cap:
        n = n[:cap].rsplit(" ", 1)[0] + "…"
    return n

core = [c for c in d["qualified"] if not c["is_chain"] and not c["is_adjacent"]]
core.sort(key=lambda c: -c["reviews"])

web_or_ig = [c for c in core if c["website"] == "Y" or c["instagram"] == "Y"]
targets = [c for c in web_or_ig if not parked_reason(c["name"])]
parked = [c for c in web_or_ig if parked_reason(c["name"])]
no_presence = [c for c in core if c["website"] != "Y" and c["instagram"] != "Y"]

def ig_state(c):
    h = (c.get("handle") or "")
    if not h or h == "wix":
        return "N", "", ""
    if "UNVERIFIED" in h:
        return "personal", "@" + h.replace(" (UNVERIFIED)", ""), "not scraped"
    f = "{:,}".format(c["followers"]) if isinstance(c["followers"], int) else "not scraped"
    return "Y", "@" + h, f

L = []
w = L.append

w("# SE Bangalore — qualified outreach targets")
w("")
w("**Generated** 2026-08-14 · **Scrape date** 2026-08-10 · **Source** Google Maps via Apify")
w("`compass/crawler-google-places`, 251 raw records → 234 unique places → 82 qualified.")
w("")
w("Rebuilt from `results.json` in this same folder. Regenerate rather than hand-edit — the")
w("pipeline is `process.py`, which re-runs against `raw/` at zero API cost.")
w("")
w("---")
w("")
w("## Selection")
w("")
w("| Filter | Effect |")
w("|---|---|")
w("| 100+ reviews AND 4.0+ stars | applied at scrape-processing time |")
w("| Deduped by placeId | 251 raw → 234 unique |")
w("| Matched against the existing 80-clinic list | 19 excluded as already known |")
w("| National chains removed | 18 held back per the mega-brand rule |")
w("| Adjacent verticals removed | 12 dental-led / salon / homeopathy / hospital |")
w("| **Has a website or an Instagram** | **%d of the 52 core targets** |" % len(web_or_ig))
w("| Parked by Tilak, 14 Aug | %d removed |" % len(parked))
w("| **Working list** | **%d clinics** |" % len(targets))
w("")
w("**Note on the website/Instagram filter.** It is not the discriminator it looks like. This")
w("pipeline discovers an Instagram handle *by reading the clinic's own website*, so a clinic with")
w("Instagram but no website is structurally impossible to detect here — and indeed zero of the 82")
w("qualified clinics are in that state. \"Website or Instagram\" therefore resolves to \"has a")
w("website.\" The %d core clinics excluded by it have neither, listed in Appendix B." % len(no_presence))
w("")
w("**Corollary worth respecting:** an `IG = N` below means *no Instagram link was found on the")
w("clinic's website*. It does not mean the clinic has no Instagram. Do not build a \"you have no")
w("social presence\" hook on this column without checking by hand first — it will read as wrong to")
w("a founder who posts daily.")
w("")
w("---")
w("")
w("## Working list — %d clinics" % len(targets))
w("")
w("| # | Clinic | Rating (reviews) | Area | Phone | Website | IG | Handle | Followers |")
w("|---|---|---|---|---|---|---|---|---|")
for i, c in enumerate(targets, 1):
    r = raw.get(c["name"], {})
    ig, handle, fol = ig_state(c)
    w("| %d | %s | %s (%d) | %s | %s | %s | %s | %s | %s |" % (
        i, short(c["name"]), c["rating"], c["reviews"], c["areas"],
        r.get("phone") or "—", c["website"], ig, handle or "—", fol or "—"))
w("")
igs = sum(1 for c in targets if ig_state(c)[0] == "Y")
pers = sum(1 for c in targets if ig_state(c)[0] == "personal")
w("**Split:** %d with a clinic Instagram · %d with a personal-brand account · %d website-only."
  % (igs, pers, len(targets) - igs - pers))
w("")
w("---")
w("")
w("## Machine-readable")
w("")
w("Full GBP titles, place IDs and website URLs for the working list. `placeId` is the stable key —")
w("use it to re-scrape a specific clinic rather than re-running a whole area.")
w("")
w("```json")
rows = []
for c in targets:
    r = raw.get(c["name"], {})
    ig, handle, _ = ig_state(c)
    rows.append({
        "name": c["name"],
        "placeId": r.get("placeId"),
        "website": c.get("website_url"),
        "instagram": handle.lstrip("@") if handle else None,
        "followers": c["followers"] if isinstance(c["followers"], int) else None,
        "rating": c["rating"],
        "reviews": c["reviews"],
        "phone": r.get("phoneUnformatted") or r.get("phone"),
        "area": c["areas"],
        "category": c.get("cats"),
    })
w(json.dumps(rows, indent=1, ensure_ascii=False))
w("```")
w("")
w("---")
w("")
w("## Outstanding work that needs an API key")
w("")
w("Three jobs are queued against this list. All were blocked on 14 Aug because the Apify key in the")
w("working session could not reach the account that owns the 10 Aug runs.")
w("")
missing = [c for c in targets if ig_state(c)[0] == "Y" and ig_state(c)[2] == "not scraped"]
w("### 1. Missing follower counts (%d) — trivial cost" % len(missing))
w("")
w("These handles are confirmed and tied to the right business; only the follower number failed to")
w("fetch, because the handle came from a website link rather than an enriched profile record.")
w("")
w("| Clinic | Handle |")
w("|---|---|")
for c in targets:
    ig, handle, fol = ig_state(c)
    if ig == "Y" and fol == "not scraped":
        w("| %s | %s |" % (short(c["name"]), handle))
w("")
w("### 2. Two areas were never properly measured")
w("")
w("Sarjapur Rd and Bommanahalli returned 37 and 4 raw records off broken polygons — the geocoder")
w("degenerated them to tiny slivers. Clinics tagged to those areas in this file are real; the")
w("*absence* of a clinic there proves nothing. Corrected polygons, ready to run:")
w("")
w("**Sarjapur Rd** (Agara → Dommasandra corridor)")
w("```json")
w('{"type":"Polygon","coordinates":[[[77.63,12.855],[77.785,12.855],[77.785,12.945],[77.63,12.945],[77.63,12.855]]]}')
w("```")
w("")
w("**Bommanahalli**")
w("```json")
w('{"type":"Polygon","coordinates":[[[77.596,12.878],[77.65,12.878],[77.65,12.925],[77.596,12.925],[77.596,12.878]]]}')
w("```")
w("")
w("Estimated $1–2 at free-tier rates ($0.004/place scraped + $0.002/place contact enrichment).")
w("The 10 Aug run overshot its $10 cap and landed at $12.14 — cost scales with the number of map")
w("segments a polygon splits into, not with the per-term cap. Electronic City alone split into 20.")
w("Set the cap low and check segment count before committing.")
w("")
w("### 3. Chain re-check")
w("")
w("Chain detection in `process.py` is a hardcoded 11-name list. La Densitae passed straight through")
w("it and was only caught by eye on 14 Aug — it is a large chain and is parked in Appendix A. Other")
w("names in the working list that could be multi-location on the same basis, **unverified**:")
w("CLINIQUE / Dr Idris, Clinique Internationale, AHIS Aesthetics. A placeId-level brand-name count")
w("across `raw/` would catch this shape and costs nothing.")
w("")
w("---")
w("")
w("## Appendix A — parked, do not work")
w("")
w("| Clinic | Rating (reviews) | Reason |")
w("|---|---|---|")
for c in parked:
    w("| %s | %s (%d) | %s |" % (short(c["name"]), c["rating"], c["reviews"], parked_reason(c["name"])))
w("")
w("Also held back and **not** in this file: 18 national chains and 12 adjacent-vertical clinics.")
w("Both groups are in `NEW-CLINICS-TABLE.md` sections B and C, and in `results.json`.")
w("")
w("## Appendix B — core clinics with neither website nor Instagram (%d)" % len(no_presence))
w("")
w("Excluded from the working list by the filter, not by judgment. They clear the review bar and are")
w("not chains — a phone-first or walk-in approach would still reach them.")
w("")
w("| Clinic | Rating (reviews) | Area | Phone |")
w("|---|---|---|---|")
for c in no_presence:
    r = raw.get(c["name"], {})
    w("| %s | %s (%d) | %s | %s |" % (short(c["name"]), c["rating"], c["reviews"], c["areas"],
                                      r.get("phone") or "—"))
w("")
w("## Data-quality traps carried over from the 10 Aug run")
w("")
w("**Platform handles.** Instagram links scraped from website footers included `@wix` (880k, a")
w("\"built with Wix\" badge), `@tv` (Instagram's own account, 1.9M) and `@ekacarehq` (a healthtech")
w("vendor). These were discarded, not reported. Skin Xperts' *only* Instagram link was the Wix")
w("badge — it reads `IG = N` here and `IG = Y` in the older `NEW-CLINICS-TABLE.md`, which was built")
w("before the platform filter ran. This file is the corrected one.")
w("")
w("**Unrelated handles.** Where a website links an Instagram account bearing no relation to the")
w("clinic name, the follower count is withheld rather than attributed. One case survives in the")
w("working list, marked `IG = personal`: Clinique Internationale links `@drbhaveshgupta_`, the")
w("doctor's personal account rather than a clinic brand. Real presence, different outreach angle.")
w("")
w("**Degenerate geocoding.** A polygon that fails to resolve does not error — it silently shrinks")
w("and returns a near-empty result that looks like a genuine finding. Check the reported area of")
w("every polygon against what you intended before trusting a low count.")

out = os.path.join(BASE, "QUALIFIED-TARGETS-2026-08-14.md")
open(out, "w").write("\n".join(L) + "\n")
print("wrote", out)
print("targets", len(targets), "parked", len(parked), "no_presence", len(no_presence))
