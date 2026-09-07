#!/bin/bash
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126 Safari/537.36"
d="$1"
out=""
for p in "" "contact" "contact-us" "about" "about-us"; do
  h=$(curl -sL --max-time 10 -A "$UA" "https://$d/$p" 2>/dev/null \
      | grep -oiE 'instagram\.com/[A-Za-z0-9_.]{2,40}' \
      | sed -E 's#.*instagram\.com/##' | tr 'A-Z' 'a-z' \
      | grep -viE '^(p|reel|reels|explore|accounts|tv|wix|about|developer|legal|privacy|directory|instagram)$' \
      | sort -u | tr '\n' ',')
  out="$out$h"
done
echo "$d|$(echo $out | tr ',' '\n' | sed '/^$/d' | sort -u | tr '\n' ',')"
