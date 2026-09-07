# Build Guide — Revenue Diagnostic One-Pagers

Technical spec. Everything here was arrived at by correction — the values are not
arbitrary. Do not "improve" them without being asked.

---

## 0. Workflow

1. Pick the closest `examples/*.html` (see §7) and **copy it**. Never rebuild the
   CSS from scratch — the embedded fonts and design tokens must survive intact.
2. Swap the body content.
3. Calibrate the page height (§4).
4. Export PDF → PNG → JPG (§5).
5. Verify (§6).

---

## 1. Design tokens (fixed — do not change)

```css
--ink:#17181a;         /* headings, emphasis */
--ink-soft:#33353a;    /* body copy */
--ink-faint:#5c5f64;   /* labels, captions */
--accent:#0e9f7b;      /* rules, markers, timeline dots */
--accent-deep:#0a7a5f; /* label text, CTA emphasis, brand */
--rule:#e2e1dd;        /* dividers */
--paper:#ffffff;
```

**Contrast history:** `--ink-faint` was originally `#8a8d92` and `--ink-soft` was
`#4a4d52`. Both looked fine on a calibrated monitor and **disappeared on a phone
screen**. They were darkened to the values above. Do not lighten them back.

**Type scale** — everything sits on these three, deliberately:

```css
--fs-label:11.5px;  /* all uppercase mono labels — ONE size everywhere */
--fs-body:13.5px;   /* body, bucket lists, asides — ONE size everywhere */
--fs-emph:15px;     /* core insight + close block only */
```

Only the clinic name (~27px), tagline (~16px), and subtitle (13.5px italic) step
outside this. An earlier version had roughly six different sizes floating around
and read as visually inconsistent — "the heading is too big and the content is
too small" — which was corrected to this unified scale. Keep headings and their
body copy in proportion.

---

## 2. Typography

- **Poppins** for everything except labels and timestamps.
- **Mono** (`SF Mono` / `JetBrains Mono`) for uppercase labels, the case-ref
  block, and timeline keys. This is the "clinical case file" cue — a doctor reads
  diagnostic reports all day, and the format speaks her professional language
  back to her. It is load-bearing, not decorative.
- Poppins is **embedded as base64 woff2 inside the HTML**, not linked. This is
  deliberate: a linked webfont silently falls back to a system font during PDF
  export or offline viewing, which breaks the entire look with no error. Five
  weights are embedded: 400, 500, 600, 700 normal + 500 italic.
- The italic is a **real italic weight**, not a browser-synthesized slant.

**To recover the font CSS** if it's ever lost — extract from any existing doc:

```bash
python3 -c "
import re
s = open('examples/The Glow Clinic - Revenue Diagnostic.html').read()
open('poppins.css','w').write('\n'.join(re.findall(r'@font-face\{.*?\}', s, re.S)))"
```

**To regenerate from scratch** (only if all examples are lost):

```bash
curl -s -A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15" \
  "https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,400;0,500;0,600;0,700;1,500&display=swap"
```

Keep only the `latin` subset blocks (the ones whose `unicode-range` includes
`U+0000-00FF`), download each woff2, base64-encode it, and inline it as
`src:url(data:font/woff2;base64,...) format('woff2')`.

---

## 3. Branding

- **Text wordmark only** — `Valence` in `--ink` + `Ops` in `--accent-deep`.
- **Do not attempt to recreate the logo mark.** An SVG approximation of the
  asterisk-and-arrow logo was tried and explicitly rejected. The text wordmark is
  the settled decision.
- Brand appears **exactly twice**: masthead (top-left) and footer (bottom-right).
  Never more.
- A 5px accent gradient bar runs across the very top of the sheet.
- **The clinic's name is the largest element on the page**, directly under a small
  "PREPARED FOR" mono eyebrow. This creates instant personalization — an earlier
  version led with an abstract headline and buried the clinic name in a small
  eyebrow line, which was rejected for exactly that reason.
- Case-ref block (top right): `Revenue Diagnostic` / `Case Ref <CODE> / <MON-YEAR>`
  / locations. Use a short uppercase code per clinic (DIXIT, GLOW, MOS, VTIARA,
  JUVITA, SWETHA, DNA).

---

## 4. Page height calibration ← the fiddly part

The sheet is **210mm wide** (A4 width) but a **custom height** — a single tall
continuous page, *not* a 2-page A4 PDF. A 2-page PDF with a half-empty second
page looks broken and was explicitly rejected.

**Target: 430–445mm** (~1.45–1.5 × A4). **Hard ceiling ~1.5 pages.**

> Explicit instruction from Tilak: *"if fitting it into a single page regardless
> compromises the content, I'd rather extend to 1.5 pages"* — breathable and
> skimmable beats compact and clumsy.
>
> **Never solve overflow by crushing spacing.** That was done once and the result
> was rejected as "bloated, no little space also, looks clumsy." Trim copy first;
> only then adjust height.

Two places must always match:

```css
.sheet { min-height:438mm; }            /* and */
@page  { size:210mm 438mm; margin:0; }
```

**Calibration loop** — binary-search the smallest height that yields exactly 1 page:

```bash
FILE="Dr. Example - Revenue Diagnostic.html"
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

for H in 430 440 450; do
  python3 - <<EOF
import re
p = "$FILE"; s = open(p).read()
s = re.sub(r"min-height:\d+mm;", "min-height:${H}mm;", s)
s = re.sub(r"@page\{ size:210mm \d+mm; margin:0; \}", "@page{ size:210mm ${H}mm; margin:0; }", s)
open(p,"w").write(s)
EOF
  "$CHROME" --headless=new --disable-gpu --no-sandbox \
    --print-to-pdf="/tmp/t_$H.pdf" --no-pdf-header-footer "file://$PWD/$FILE" 2>/dev/null
  echo "$H -> $(pdfinfo /tmp/t_$H.pdf | grep -i '^Pages')"
done
```

Pick the smallest height reporting `Pages: 1`, then narrow with a second pass
(e.g. 436 / 440 / 444). If the smallest 1-page height is above ~445mm, **trim
copy** and re-run rather than accepting a taller page.

**Why the thresholds jump in steps rather than smoothly:** `break-inside:avoid`
on `section`, `.bucket`, `.insight-block`, and `.close-group` keeps those blocks
atomic, so an entire block moves to page 2 at once. That's intended — a bucket
split across pages looks broken.

**Browser preview height ≠ print height.** Only trust Chrome's print engine.

Reference heights actually used: Dixit 297mm (the one true single-page doc),
Swetha's 426mm, Juvita 431mm, Glow 435mm, Ministry 438mm, DNA 444mm,
Vtiara 456mm (slightly over — it carries a fourth confirmed bullet).

---

## 5. Export pipeline

> **Platform note:** the commands below are written for **macOS**. `sips` is
> macOS-only and the Chrome path is macOS-specific.
>
> **On Linux/Windows**, two substitutions:
> - Chrome: use `google-chrome` / `chrome.exe` (the `--headless=new
>   --print-to-pdf` flags are identical on every platform).
> - `sips` → ImageMagick: `magick "$BASE.png" -quality 60 "$BASE.jpg"`
>
> `pdftoppm` and `pdfinfo` come from **poppler**, which exists on all three
> (`brew install poppler` / `apt install poppler-utils` / bundled with the
> Windows poppler release). Nothing else changes — the HTML and its embedded
> fonts are fully portable.

```bash
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
BASE="<Clinic Name> - Revenue Diagnostic"

# HTML → PDF  (Chrome's print engine — honours the @page rule exactly)
"$CHROME" --headless=new --disable-gpu --no-sandbox \
  --print-to-pdf="$BASE.pdf" --no-pdf-header-footer "file://$PWD/$BASE.html"

# PDF → PNG  (226 dpi ⇒ 1868px wide, matches the existing set)
pdftoppm -png -r 226 -singlefile "$BASE.pdf" "$BASE"

# PNG → JPG  (the WhatsApp-send format; 'low' keeps text crisp at ~350–500KB)
sips -s format jpeg -s formatOptions low "$BASE.png" --out "$BASE.jpg"
```

Chrome may print harmless `IPH_BatterySaverMode` errors to stderr — ignore them;
check the "N bytes written" line instead.

---

## 6. Verification (do all four)

```bash
pdfinfo "$BASE.pdf" | grep -iE "pages|page size"   # MUST say Pages: 1
```

1. **`Pages: 1`** — non-negotiable.
2. **Open the PDF and look at it.** Check the clinic name isn't wrapping badly and
   the case-ref block isn't overflowing. Long multi-city location lines may need a
   manual `<br/>` (Vtiara needed one for
   "Indiranagar · New BEL Road ·<br/>HRBR Layout, Bengaluru").
3. **Confirm Poppins actually rendered** — compare against an example JPG. If it
   looks like a generic system font, the embedded font block didn't survive.
4. **Run the §10 self-check in `COPY_STANDARD.md`.**

---

## 7. Which example to start from

| Evidence shape | Start from |
|---|---|
| A gap between two timed moments | `Ministry of Skin` |
| Fast reply, but manual / unqualified | `The Glow Clinic` |
| Same result across two channels | `Dr. Swetha's Cosmoderm Centre` |
| Several follow-ups in a row | `Dr. Juvita Aesthetics` |
| An external event (job posting etc.) as the "why now" | `Vtiara Hair & Skin Clinic` |
| No mystery shop — public signals only | `DNA Skin Clinic` |

- **`The Glow Clinic`** — the reference for tone.
- **`Ministry of Skin`** — the reference for compliment-then-pivot.
- **`DNA Skin Clinic`** — the reference for building without a verified test.

### ⚠️ Do not use `Dr. Dixit` as a template

It is included as a **content and copy reference only**. It was built *before* the
1.5-page decision was made, under a hard "must fit one A4 page" constraint that
was later abandoned. Its spacing was compressed to hit 297mm and the result was
explicitly rejected as *"bloated, no little space also, looks clumsy."*

Concretely, Dixit carries the **rejected** values:

| | Dr. Dixit (rejected) | Settled standard |
|---|---|---|
| sheet height | 297mm | 426–456mm |
| page padding | `7mm 15mm 3mm` | `14mm 18mm 12mm` |
| `section` margin | 5px | 15px |
| `hr.rule` margin | 4px | 15px |
| `.bucket` margin | 4px | 12px |
| `--fs-body` | 13px | 13.5px |
| `--fs-emph` | 14px | 15px |
| body line-height | 1.44 | 1.52 |

Copying it would silently reintroduce the exact cramped look that was rejected.
Its **copy** is still a good reference (it's the cleanest single-fact wedge in the
set) — just never inherit its CSS.

---

## 8. Known traps

- **Ampersands in filenames** (`Vtiara Hair & Skin Clinic`) break some file-URL
  tooling. Always quote paths; if a tool still chokes, copy to a temp name, build,
  and rename back.
- **PDF text extraction may merge words** (e.g. "CosmodermCentre"). That is a
  copy-layer artifact of the PDF, **not** a rendering bug — always confirm against
  the PNG before "fixing" anything.
- **Do not add a mobile breakpoint.** One was added and explicitly rejected. This
  is a fixed-dimension print document, not a responsive web page.
- **Do not add a viewport meta / max-width for phone viewing.** Same reason — the
  deliverable is a PDF/JPG, not a web page.
- **Don't reuse another clinic's "Can't Confirm" bullets.** They must reflect what
  is genuinely unknown about *this* clinic. Reused bullets are the fastest way to
  make the document feel templated.
