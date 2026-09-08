---
date_created: 2026-08-22
date_modified: 2026-08-22
status: active
---
# SkinFit proposal — build kit

`proposal.html` + `style.css` + `fonts/` produce
`../../SkinFit Wellness - Patient Communications Proposal.pdf`.

Design system is reverse-engineered from `../../SkinFit Wellness - Enquiry Handling Review.pdf`:
Poppins 400/500/600 + Menlo, A4 (794x1123 CSS px), 82px side margins,
palette `#FBF9F5 / #F3F0E9 / #E4DFD6 / #14171A / #3C4147 / #7A7F84 / #0E7C5F / #4FBF9A / #8FCDB8 / #0B1F19`.

Rebuild:

    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
      --headless --disable-gpu --no-pdf-header-footer \
      --print-to-pdf=out.pdf --virtual-time-budget=6000 proposal.html

Each `<div class="page">` is one printed page. Page breaks are manual, so after
any copy edit re-render and check every page for overflow at the footer.
