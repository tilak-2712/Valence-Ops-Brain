#!/bin/zsh
# Continuously snapshot Apify datasets to disk while runs are in progress.
# Protects against the dataset-lock that occurs when the monthly usage limit is hit.
# Usage: ./autosave.sh <datasetId>:<name> [<datasetId>:<name> ...]

export APIFY_TOKEN=apify_api_u3dhjX6ixUC25kXOcgJF8B2uf418Pt36zjtY
OUT="/Users/stilak/Documents/Valence-Ops-Sales/se-bangalore-scrape/raw"
mkdir -p "$OUT"

for i in {1..90}; do
  alldone=1
  for pair in "$@"; do
    ds=${pair%%:*}; nm=${pair##*:}
    body=$(curl -s "https://api.apify.com/v2/datasets/$ds/items?token=$APIFY_TOKEN&clean=true&format=json")
    # Only overwrite when we got a real JSON array (not a lock/error object)
    echo "$body" | python3 -c "
import sys,json
raw=sys.stdin.read()
try:
    d=json.loads(raw)
except Exception:
    sys.exit(1)
if isinstance(d,list) and len(d)>0:
    open('$OUT/$nm.json','w').write(raw)
    print('$nm snapshot: %d' % len(d))
    sys.exit(0)
sys.exit(1)
" 2>/dev/null
  done
  # check if all runs still active
  sleep 20
done
