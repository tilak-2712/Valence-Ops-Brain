# Aurilueur proposal — build kit

`proposal.html` + `style.css` + `fonts/` produce
`../../../04 Clients/Aurilueur Esthetic Clinic/Aurilueur Esthetic Clinic - Enquiry and Appointment Systems Proposal.pdf`.

Design system copied from `../skinfit-proposal-v2` so a client who has seen one
Valence Ops document recognises the next: Poppins 400/500/600 + Menlo, A4
(794x1123 CSS px), 82px side margins, palette
`#FBF9F5 / #F3F0E9 / #E4DFD6 / #14171A / #3C4147 / #7A7F84 / #0E7C5F / #4FBF9A / #8FCDB8 / #0B1F19`.

Rebuild:

    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
      --headless --disable-gpu --no-pdf-header-footer \
      --print-to-pdf=out.pdf --virtual-time-budget=6000 proposal.html

Each `<div class="page">` is one printed page. Page breaks are manual, so after
any copy edit re-render and check every page for overflow at the footer.
