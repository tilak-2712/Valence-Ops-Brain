#!/usr/bin/env python3
"""Normalize new_leads_1 inputs into a single targets.json.

Inputs
  zone-leads.md  — 19 clinics, "Central zone", markdown link soup
  Clinic_Directory_Template ... .csv — 24 rows (Aurilueur duplicated)

Output
  targets.json — one record per unique clinic
"""
import csv, json, re, unicodedata
from pathlib import Path

HERE = Path(__file__).resolve().parent
CSV = HERE / "Clinic_Directory_Template csv 3b771d3ba7f680e0b00acf18a11921d5.csv"
MD = HERE / "zone-leads.md"


def clean_url(u):
    """Strip markdown backslash-escapes and tracking params; fix doubled URLs."""
    if not u:
        return None
    u = u.replace("\\", "").strip()
    # the Aesthetics Plus case: two absolute URLs concatenated
    m = re.match(r"(https?://.+?)(https?://.+)$", u)
    if m:
        u = m.group(1)
    return u or None


def ig_handle(u):
    """Extract the bare handle from any instagram URL form."""
    if not u:
        return None
    u = clean_url(u)
    m = re.search(r"instagram\.com/([A-Za-z0-9._]+)", u)
    if not m:
        return None
    h = m.group(1)
    if h in {"p", "reel", "explore", "stories"}:
        return None
    return h.lower()


def norm_name(n):
    n = unicodedata.normalize("NFKD", n)
    n = "".join(c for c in n if not unicodedata.combining(c))
    n = re.sub(r"[^a-z0-9]+", " ", n.lower()).strip()
    return n


records = []

# ---- CSV ----------------------------------------------------------------
with CSV.open(encoding="utf-8-sig") as f:
    for row in csv.DictReader(f):
        name = (row["Clinic Name"] or "").strip()
        if not name:
            continue
        records.append({
            "clinic": name,
            "source": "csv",
            "website": clean_url(row["Clinic Website"]),
            "ig": ig_handle(row["Insta Handle"]),
            "linkedin": clean_url(row["LinkedIn"]),
        })

# ---- zone-leads.md ------------------------------------------------------
# Entries start with "<n>." / "<n> " at line start. Collect the block, then
# pull the name (first non-URL text) and every URL in it.
text = MD.read_text(encoding="utf-8")
blocks = re.split(r"\n(?=\s*\d+\s*\\?[.\s])", text)
for b in blocks:
    urls = [clean_url(u) for u in re.findall(r"\((https?://[^)]+)\)", b)]
    urls = [u for u in urls if u]
    if not urls:
        continue
    # name: strip the leading number, markdown syntax and any URLs
    head = b.strip()
    head = re.sub(r"^\s*\d+\s*\\?\.?\s*", "", head)
    head = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", head)  # links -> label
    head = head.replace("*", "").replace("\\", "")
    name = next((l.strip() for l in head.splitlines() if l.strip()), None)
    if not name:
        continue
    ig = next((h for h in (ig_handle(u) for u in urls) if h), None)
    site = next((u for u in urls if "instagram.com" not in u), None)
    records.append({
        "clinic": name,
        "source": "zone-leads (Central)",
        "website": site,
        "ig": ig,
        "linkedin": None,
    })

# ---- dedupe -------------------------------------------------------------
seen, out, dupes = {}, [], []
for r in records:
    key = r["ig"] or norm_name(r["clinic"])
    if key in seen:
        dupes.append(r["clinic"])
        continue
    seen[key] = r
    r["key"] = key
    out.append(r)

for i, r in enumerate(out, 1):
    r["id"] = i

(HERE / "targets.json").write_text(json.dumps(out, indent=2, ensure_ascii=False))

print(f"csv rows + md rows  : {len(records)}")
print(f"unique clinics      : {len(out)}")
print(f"dropped duplicates  : {dupes}")
print(f"no website          : {[r['clinic'] for r in out if not r['website']]}")
print(f"no instagram        : {[r['clinic'] for r in out if not r['ig']]}")
