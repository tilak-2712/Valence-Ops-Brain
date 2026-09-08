# _archive — retired files

Moved here 2026-08-13 during the folder self-audit. **Nothing in here is canonical. Do not read
these when drafting, researching, or deciding anything.** They are kept only so a decision can be
reversed or a fact recovered.

If you need something from here, move it back deliberately and update `CLAUDE.md` in the same edit.

---

| File | Why it was retired |
|---|---|
| `personalized-outbound-skill.md` | **Byte-identical** to `personalized-outbound-v2.md`. `CLAUDE.md` described it as "the prior draft" — that was wrong; it was a straight duplicate. Two copies of the drafting engine meant edits could land on the copy nobody reads. |
| `clinic-apify-research-skill.md` | **Byte-identical** to `.claude/skills/clinic-audit-research/SKILL.md`. Same drift risk: the loose root copy is not the one the skill loader reads. |
| `scrape-southeast-bangalore-RESUME.md` | Self-declared superseded by `SESSION-2026-08-10-se-bangalore-scrape.md` §14. Described a blocked Apify state that was resolved the same day. |
| `elective-clinics-sales1.md` | **Contains a fabricated case study** — *"Clinic XYZ in Bangalore saw a 20% rise in revenue in 6 months"* — flagged as CRITICAL VIOLATION #1 in `files/OUTBOUND_SYSTEM_AUDIT.md` on 2026-07-22 and never fixed. Also cites HIPAA (wrong jurisdiction) and runs an ROI/"our platform" objection library that violates the §3 banned vocabulary. Highest-risk file in the folder: it looked like a sales asset, so it was the most likely thing to get pattern-matched into a draft. |
| `Pre-outbound-research/batch3-aesthetic-audit.md` | Carried its own `⚠️ SUPERSEDED` banner pointing at `batch3-aesthetic-MASTER.md`. Kept for history, moved out of the live research folder. |
| `one-pager-handoff.zip` | Frozen packaged copy of `one-pager-handoff/`. The unpacked folder is live; the zip was a second, silently-diverging copy of the same rules and examples (~3 MB). |
| `Valence-Research-Intelligence/` | See below — this one is **not** what `CLAUDE.md` said it was. |

---

## On `Valence-Research-Intelligence/`

`CLAUDE.md` described this as "an earlier snapshot of the same research now superseded by
`Pre-outbound-research/`." That was only one-fifth true, and the inaccuracy is worth recording:

- `OUTREACH document.md` and `outreach -2.md` — **byte-identical duplicates** of the same files in
  `Pre-outbound-research/`. These are the only two files the "superseded snapshot" description fit.
- `section 1.md` … `section 8.md` (~700 KB) and `compass_artifact_…md` — **not duplicates of
  anything.** These are LLM-generated Bengaluru market-intelligence reports: patient-journey
  leakage, owner GTM psychology, objection intelligence, competitive dossier, and a LinkedIn
  hook/swipe library.

They are archived rather than deleted because §5 (objection intelligence) and §7 (competitive
dossier) may be worth mining later. They are archived rather than kept live because they carry the
same defect as `elective-clinics-sales1.md`: confident, unsourced market claims written in the exact
register the project's own rules ban, sitting one folder away from the drafting engine. Nothing in
them is clinic-specific and nothing in them is verified against a clinic in the tracker.

**If you mine them, mine them for questions to test — never for facts to state to a clinic.**

---

## Added 2026-08-13 (second pass)

| File | Why |
|---|---|
| `valence-ops-clinic-intelligence-os.md` | Retired by Tilak. Built over the first 20 scraped leads only, so its Master Database, segmentation and cross-clinic patterns are specific to that cohort — there are now ~150 clinics and far more outreach research. It also ran on **ICP scoring** (retired as a targeting tool 2026-07-22) and was headed *"Clinics logged: 20 / 500"* — the vanity metric the 22 Jul audit condemned as measuring input rather than progress. Tilak said it could be deleted; **archived rather than deleted because a replacement is planned** and §2 (segmentation framework) and §3 (cross-clinic patterns) are worth reading as seed material for it. Hard-delete freely if you'd rather start clean. |
| `_WRITE_POLICY.md` | Draft of the write policy (2026-09-08). Adopted verbatim into `CLAUDE.md` § "Write policy" the same day; kept only as the dated draft. |
