#!/usr/bin/env python3
"""Google Ads Transparency recency pass.

The SearchSuggestions RPC gives lifetime ad counts but no dates. This adds the
recency dimension (firstShown / lastShown per creative) for every clinic that
had a plausible India-based advertiser match, via solidcode/ads-transparency-scraper.

One Apify run per clinic, in parallel. Results cached per-id so reruns are free.
"""
import json, os, sys, urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / "gads_detail"
OUT.mkdir(exist_ok=True)
TOK = os.environ["APIFY_TOKEN"]
ACT = "solidcode~ads-transparency-scraper"
URL = f"https://api.apify.com/v2/acts/{ACT}/run-sync-get-dataset-items?token={TOK}"

# Query per clinic id: the advertiser name as it actually appears in the
# transparency centre, taken from the SearchSuggestions pass.
QUERIES = {
    1:  "The Aesthetic Edge",
    3:  "Auguste Skin",
    5:  "Aurilueur Esthetic Clinic",
    6:  "Metphi Clinic",
    7:  "Keza Skin and Hair Clinic",
    9:  "New Look Skin Care",
    10: "Sutvacha Skincare",
    11: "Seoulful",
    14: "Pigment Plus Skin and Hair Clinic",
    16: "Regenique",
    20: "Skinray Clinic",
    26: "Richmond Dental and Aesthetic Centre",
    28: "Radiant Aesthetics",
    30: "Hairline",
    35: "Divine Aesthetics",
    36: "The Aesthetic Co",
    39: "Anil Abraham",
    40: "Moon Aesthetic",
}


def one(item):
    cid, q = item
    dest = OUT / f"{cid}.json"
    if dest.exists() and dest.stat().st_size > 2:
        return f"skip {cid} (cached)"
    body = json.dumps({"searchQuery": q, "region": "IN", "maxResults": 25}).encode()
    req = urllib.request.Request(
        URL, data=body, headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=600) as r:
            data = r.read()
    except Exception as e:                                      # noqa: BLE001
        return f"FAIL {cid} ({q}): {type(e).__name__} {str(e)[:60]}"
    dest.write_bytes(data)
    try:
        n = len(json.loads(data))
    except Exception:                                           # noqa: BLE001
        n = "ERR"
    return f"done {cid:>3} {q[:34]:<34} -> {n} creatives"


def main():
    items = sorted(QUERIES.items())
    with ThreadPoolExecutor(max_workers=9) as ex:
        for line in ex.map(one, items):
            print(line, flush=True)


if __name__ == "__main__":
    main()
