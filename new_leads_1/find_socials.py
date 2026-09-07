#!/usr/bin/env python3
"""Fetch each clinic website and extract Facebook page + Instagram links.

Free (plain HTTP to the clinics' own sites). Feeds the Apify Meta step, which
queries by *page*, avoiding the ad-body keyword trap.
"""
import json, re, sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

HERE = Path(__file__).resolve().parent
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")

FB_RE = re.compile(
    r'https?://(?:www\.|m\.|web\.)?facebook\.com/([A-Za-z0-9._\-]+(?:/[A-Za-z0-9._\-]+)?)',
    re.I)
IG_RE = re.compile(r'https?://(?:www\.)?instagram\.com/([A-Za-z0-9._]+)', re.I)

SKIP_FB = {"sharer", "sharer.php", "share.php", "plugins", "tr", "dialog",
           "profile.php", "people", "pages", "groups", "login", "help", "policies"}


def fetch(url, timeout=20):
    req = Request(url, headers={"User-Agent": UA, "Accept": "text/html,*/*"})
    with urlopen(req, timeout=timeout) as r:
        raw = r.read(900_000)
    return raw.decode("utf-8", "ignore")


def one(rec):
    out = {"id": rec["id"], "clinic": rec["clinic"], "website": rec["website"],
           "fb": None, "fb_all": [], "ig_on_site": [], "err": None}
    if not rec["website"]:
        out["err"] = "no website in source list"
        return out
    html = None
    for url in (rec["website"], rec["website"].replace("https://", "http://")):
        try:
            html = fetch(url)
            break
        except (URLError, HTTPError, TimeoutError, OSError) as e:
            out["err"] = f"{type(e).__name__}: {str(e)[:60]}"
        except Exception as e:                                  # noqa: BLE001
            out["err"] = f"{type(e).__name__}: {str(e)[:60]}"
    if not html:
        return out

    out["err"] = None
    fbs, igs = [], []
    for m in FB_RE.finditer(html):
        slug = m.group(1).strip("/")
        first = slug.split("/")[0].lower()
        if first in SKIP_FB or first.endswith(".php"):
            continue
        if slug not in fbs:
            fbs.append(slug)
    for m in IG_RE.finditer(html):
        h = m.group(1).lower()
        if h not in igs and h not in {"p", "reel", "explore"}:
            igs.append(h)
    out["fb_all"] = fbs[:6]
    out["fb"] = fbs[0] if fbs else None
    out["ig_on_site"] = igs[:4]
    return out


def main():
    targets = json.loads((HERE / "targets.json").read_text())
    with ThreadPoolExecutor(max_workers=10) as ex:
        res = list(ex.map(one, targets))
    res.sort(key=lambda r: r["id"])
    (HERE / "socials.json").write_text(json.dumps(res, indent=1, ensure_ascii=False))

    got = [r for r in res if r["fb"]]
    print(f"websites fetched ok : {sum(1 for r in res if not r['err'])}/{len(res)}")
    print(f"facebook page found : {len(got)}")
    print()
    for r in res:
        flag = r["fb"] or ("— " + (r["err"] or "no fb link on page"))
        print(f"{r['id']:>2}  {r['clinic'][:34]:<34} {flag[:56]}")


if __name__ == "__main__":
    main()
