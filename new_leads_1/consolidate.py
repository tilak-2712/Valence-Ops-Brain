#!/usr/bin/env python3
"""Merge the Google / Meta / Instagram passes into one per-clinic record.

Verdict vocabulary is deliberately the same as ADS-PRESENCE-2026-08-14.md:
  Yes          advertiser (Google) or page (Meta) name-matches the clinic
  Unconfirmed  a near-name match exists but could be a different business
  No           no advertiser/page bearing this clinic's name was found
  Unresolved   the check could not be completed (page never located)
"""
import json, datetime as dt
from pathlib import Path

HERE = Path(__file__).resolve().parent
TODAY = dt.date(2026, 8, 15)

targets = {r["id"]: r for r in json.loads((HERE / "targets.json").read_text())}

# ---- Google: advertisers whose identity is NOT settled by name alone --------
# Personal names and differently-named legal entities. Kept separate because
# "name rarity is not identity" (the Mradula Singh false positive, SE cohort).
GOOGLE_UNCONFIRMED = {
    9:  "'New Look Skin Care Ltd' — generic name, could be any of several businesses",
    14: "'PIGMENT PLUS SKIN AND HAIR CLINIC' — clinic is 'Pigment Skin And Hair Clinic'; 'Plus' differs",
    28: "'Radiant Aesthetics' — clinic is 'The Radiant Clinic'; different trading name",
    30: "'HAIRLINE DIAGNOSTICS AND HEALTH CARE PVT LTD' — clinic is 'Hairline International'; different entity",
    35: "'DIVINE AESTHETICS SURGERY' — surgery practice; clinic IG is @divineaestheticblr, 622 followers vs 500 lifetime ads",
    39: "'ANIL ABRAHAM' — personal name only; identity not established",
}

google = json.loads((HERE / "google-ads-recency.json").read_text())
meta = json.loads((HERE / "meta-ads-summary.json").read_text())
meta += json.loads((HERE / "meta-ads-summary-round2.json").read_text())
# Round 3 pages were auto-accepted on a shared token with the returned page
# name; 'Cradle Children Hospital' passed on "cradle" alone and is a
# children's hospital, not the aesthetic clinic 'Cradle of Youth'.
meta += [r for r in json.loads((HERE / "meta-ads-summary-round3.json").read_text())
         if r["id"] != 27]
insta = {r["id"]: r for r in json.loads((HERE / "instagram-summary.json").read_text())}
searched = {o["id"]: o for o in json.loads((HERE / "fb_search_results.json").read_text())}

# Advertisers that name-match but are demonstrably a different business.
# 'Hairline Clinic Brisbane Pty Ltd' surfaced in an India-region query and is
# Australian — the same failure mode as the UAE 'DERMA ELITE POLYCLINIC L.L.C'
# in the SE cohort. Foreign entity, name-identical, wrong business.
GOOGLE_REJECT_ADVERTISERS = {
    "Hairline Clinic Brisbane Pty Ltd",
    "Hairline Design",
}

# ---- fold Google -----------------------------------------------------------
g_by = {}
for r in google:
    if r["advertiser"] in GOOGLE_REJECT_ADVERTISERS:
        continue
    cur = g_by.get(r["id"])
    if cur is None or (r["days_since"] is not None and
                       (cur["days_since"] is None or r["days_since"] < cur["days_since"])):
        g_by[r["id"]] = r

# ---- fold Meta (prefer a resolved page over an unresolved one) --------------
m_by = {}
for r in meta:
    if r.get("id") is None:
        continue
    cur = m_by.get(r["id"])
    if cur is None or (cur["state"] != "PAGE_FOUND" and r["state"] == "PAGE_FOUND"):
        m_by[r["id"]] = r
# a page whose returned name does not corroborate the clinic is not that clinic
NAME_REJECT = {40: "resolved page is 'Chaser Aspira' — not the clinic"}

out = []
for cid, t in sorted(targets.items()):
    g, m = g_by.get(cid), m_by.get(cid)

    # Google verdict
    if g is None:
        g_verdict, g_detail = "No", None
    elif cid in GOOGLE_UNCONFIRMED:
        g_verdict = "Unconfirmed"
        g_detail = GOOGLE_UNCONFIRMED[cid]
    else:
        g_verdict, g_detail = "Yes", None

    # Meta verdict
    if cid in NAME_REJECT:
        m_verdict, m_detail = "Unresolved", NAME_REJECT[cid]
    elif m is None:
        m_verdict = "Unresolved"
        m_detail = "no Facebook page located (site had no FB link; search found none)"
    elif m["state"] != "PAGE_FOUND":
        m_verdict = "Unresolved"
        m_detail = f"page /{m['slug']} returned no_items (page absent or private)"
    elif (m.get("total") or 0) == 0:
        m_verdict, m_detail = "No", f"page '{m['fb_page_name']}' confirmed, 0 ads in library"
    else:
        m_verdict, m_detail = "Yes", None

    def age(v):
        return None if v is None else (TODAY - dt.date.fromisoformat(v)).days

    g_last = g["last"] if g else None
    m_last = m["newest"] if m and m.get("newest") else None
    ages = [a for a in (age(g_last), age(m_last)) if a is not None]
    recency = min(ages) if ages else None

    if g_verdict == "Yes" or m_verdict == "Yes":
        if recency is not None and recency <= 30:
            state = "SPENDING NOW"
        elif recency is not None:
            state = "DORMANT"
        else:
            state = "RECENCY UNKNOWN"
    elif g_verdict == "Unconfirmed" or m_verdict == "Unresolved":
        state = "UNRESOLVED"
    else:
        state = "NO PAID PRESENCE FOUND"

    ig = insta.get(cid, {})
    out.append({
        "id": cid, "clinic": t["clinic"], "source": t["source"],
        "website": t["website"], "ig_handle": t["ig"],
        "google": {"verdict": g_verdict, "advertiser": g["advertiser"] if g else None,
                   "creatives_seen": g["creatives_seen"] if g else 0,
                   "last_shown": g_last, "days_since": age(g_last), "caveat": g_detail},
        "meta": {"verdict": m_verdict, "page_name": m["fb_page_name"] if m else None,
                 "page_id": m.get("page_id") if m else None,
                 "total_ads": m.get("total") if m else None,
                 "newest_ad": m_last, "days_since": age(m_last),
                 "ads_last_30d": m.get("d30") if m else None, "caveat": m_detail},
        "instagram": {"handle": ig.get("handle"), "followers": ig.get("followers"),
                      "posts": ig.get("posts"), "verified": ig.get("verified"),
                      "last_post": ig.get("newest_post"),
                      "days_since_post": ig.get("days_since_post"),
                      "followers_per_post": ig.get("ratio")},
        "state": state, "recency_days": recency,
    })

(HERE / "results.json").write_text(json.dumps(out, indent=1, ensure_ascii=False))

from collections import Counter
print(Counter(o["state"] for o in out))
print()
order = {"SPENDING NOW": 0, "DORMANT": 1, "RECENCY UNKNOWN": 2, "UNRESOLVED": 3,
         "NO PAID PRESENCE FOUND": 4}
for o in sorted(out, key=lambda x: (order[x["state"]], x["recency_days"] if x["recency_days"] is not None else 999)):
    print(f"{o['id']:>3} {o['clinic'][:30]:<30} G:{o['google']['verdict']:<12} "
          f"M:{o['meta']['verdict']:<12} IG:{str(o['instagram']['followers'] or '-'):>6}  {o['state']}")
