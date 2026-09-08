# Reorg manifest — amendments and Phase 3 scope (2026-09-08)

Companion to `_reorg_manifest.csv`. Records what changed from the original brief and why, so `_REORG_LOG.md` (Phase 5) can cite it.

## Amendments agreed 2026-09-08

| # | Change | Reason (Tilak) |
|---|---|---|
| 1 | `CLAUDE.md`, `MEMORY.md`, `taste-n-judgement.md`, `files/OUTBOUND_MEMORY.md` are **PROTECTED**: no move, no rename, no frontmatter injection, no body edits in any phase. | "Crucial… store niche insights and context… don't mess with those or delete or refactor anything that makes those lose its value." |
| 2 | `files/` stays intact at its current path (5 files). The proposed `02 Ledgers` folder is dropped. | Keeps every path in the `CLAUDE.md` precedence ladder and audit table true without editing `CLAUDE.md`. |
| 3 | `COHORT-INDEX.md` stays at root. | Index file; root is where indexes live. |
| 4 | Phase 3 frontmatter is reduced to `date_created`, `date_modified`, `status` — **no `tags`, no `_tag_registry.md`**. Protected files and `_archive/` get none. | Per-file tag maintenance is the friction Tilak wants removed; the write policy replaces the registry. |
| 5 | Phase 4 unchanged in rule (link only on a concrete shared reference) but the Map-of-Content files are limited to the five client folders and the Batch 7 cohort, where 3+ notes genuinely cluster. | Same friction argument; MOCs are read-only navigation, not sinks. |
| 6 | A write policy (adopted into `CLAUDE.md` § "Write policy" 2026-09-08; draft archived) and a session-close step (`.claude/skills/wrap/SKILL.md`) are added. The policy declares `files/SEND_LOG.csv`, `files/REPLY_LOG.csv`, `files/LEARNINGS_LOG.md` frozen as sinks. Files are not edited. | Replaces seven overlapping update rituals with one routing rule and one trigger. |

## Unchanged from the brief
No deletion, git mv only, link integrity in the same commit, orphans flagged not moved, merge candidates flagged not merged, existing frontmatter merged not duplicated, one commit per folder in Phase 3, reconciliation in Phase 5.

## Still open for Tilak
- 18 heavily cited notes keep their filenames (rows marked medium, reason "NAME KEPT"). Flip any row to rename.
- 41 byte-identical kit files kept in place (reason "KEPT"). Flip to consolidate if kit portability doesn't matter.
- Which of the three SkinFit "Patient Conversion" PDFs (30 Aug) was sent.
- The empty nested directory under `Resources/_source/skinfit-proposal-v2/` — git does not track it; removing it is a Tilak call.
