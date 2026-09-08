---
date_created: 2026-07-18
date_modified: 2026-07-18
status: reference
---
# Gamma Deck Specification

Create a JSON file with this shape only after the user explicitly approves the proposed wording and one worked example. Unlike the personalization spec, the field *shape* is fixed (one cover line + 3 video title/brief pairs) — only the wording style is negotiable.

```json
{
  "approved": true,
  "approved_at": "2026-07-09T12:00:00+05:30",
  "cover_line_pattern": "A one-sentence framing tied to what the company actually does, e.g. '[Company] helps [audience] [core value prop] — here are 3 videos that could put that in front of more of them.'",
  "video_brief_pattern": "State the audience problem the company's target users face, then how a video demonstrating [Company]'s product would address it. 2-3 sentences, grounded in website evidence, no fabricated claims.",
  "max_characters_brief": 400,
  "approved_example_brief": "Sales teams doing manual LinkedIn outreach struggle to personalize at scale without burning hours per week. A video walking through how Acme's sequencing engine auto-personalizes opening lines from a prospect's recent posts would show viewers exactly how to get that time back.",
  "approved_example_title": "How To Stop Losing Warm Leads To Slow LinkedIn Follow-Up"
}
```

`approved_example_title` illustrates the title quality bar below (form only, not schema-enforced) — use it as the calibration example when drafting real titles.

Rules:

- `approved` must be `true`.
- `cover_line_pattern`, `video_brief_pattern`, and `max_characters_brief` are required.
- Video titles follow a "How To…" pattern per the Gamma template's card headings (e.g. "How To Automate LinkedIn Outreach Without Losing Personalization") — grounded in a real capability or problem the lead's audience faces, not the lead's own company.
- Video briefs describe the *lead's audience's* problem and how a video demonstrating the *lead's* product addresses it — not generic video-production notes or a topic outline.

### Title quality bar

Each of the 3 video titles must clear this bar — this is a judgment call per lead, not a formula:

- **Grounded, not generic.** The title must come from something specific the site actually shows — a real feature, workflow, integration, or use case. Titles that could apply to almost any company in the vertical (e.g. "How To Improve Your Sales Process") are too generic — reject and redraft.
- **Broad enough to have search/watch demand, not a niche feature tour.** A title naming an internal button or a feature only that company's existing users would recognize is too niche (e.g. "How To Use Acme's Webhook Retry Setting") — nobody searches for that. Anchor the title on the underlying problem or outcome a wider audience actually searches for, with the company's product as the vehicle for solving it (e.g. "How To Stop Losing Leads To Slow Follow-Up" rather than "How To Configure Acme's Auto-Reply Delay").
- **Viral/curiosity potential.** Prefer titles with a hook: a number, a contrast ("X without Y"), a surprising claim, a common mistake, or a before/after — the kind of phrasing that performs on YouTube search and suggested feed, not a dry feature-list heading.
- **The balance test**: if the title would make sense with the company name swapped out for almost any competitor, it's too generic. If it would only make sense to someone who already uses the product, it's too niche. Aim for the midpoint — a real, specific capability of this company, framed as a problem/outcome a broader relevant audience is already curious about.
- All 3 video ideas plus the cover line must be grounded in a fresh visit to the lead's website done specifically for this stage — not in the `company_description`/`evidence_summary` already on the sheet, which were gathered for fit-scoring and may be stale or too thin for video-idea material. No invented features or metrics.
- Cover line and all 3 video ideas must be written only for rows already qualified as non-`skip` with `research_status = success`.
- Leave all gamma fields blank for `skip` rows (`gamma_deck_status` = `skipped`).
- The example illustrates form only; never reuse its claims for unrelated companies.
