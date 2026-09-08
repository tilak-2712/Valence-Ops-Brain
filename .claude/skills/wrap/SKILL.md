---
name: wrap
description: Session-close changeset for the Valence Ops vault. Collects what this session learned or produced, routes each item to its single home per CLAUDE.md § Write policy, posts a one-table changeset, then writes and commits only after Tilak approves. Runs automatically via the Stop hook; also usable on demand as /wrap.
---

# /wrap — automatic since 2026-09-08

Normally fires by itself. A Stop hook (`.claude/hooks/wrap-check.py`) blocks the end of a turn once
enough has happened and hands over these instructions. Typing `/wrap` runs the same thing on demand.

Read `CLAUDE.md` § "Write policy" first. Then:

1. **Collect.** Every candidate from this session: a clinic fact Tilak reported, feedback or a
   judgement he gave, a working preference, a rule or decision, a deliverable produced, a thread
   opened or closed.
2. **Route or drop.** Apply the routing test in §1 of that section. Drop everything in §2, which now
   explicitly includes timestamps, follow-up counts and minor updates that decide nothing, and
   anything already captured in a state note or in git. Label each survivor
   `confirmed` / `provisional` / `hypothesis`.
3. **Propose. Never write yet.** Output only:

   | File | Add / Amend | What, in one line | Label |
   |---|---|---|---|

   Then a short "Waiting for your yes" list for anything in §4's always-ask set. If nothing durable
   survives, reply with exactly `Nothing durable to file.` and stop. **Then stop and wait.**
4. **Write, only after Tilak approves.** Append, or add a dated correction beneath an existing entry.
   Never rewrite existing prose. Never create a second frontmatter block. Record client and deal
   position as **stage** in the relevant `… Current State.md`, overwritten, never as a growing
   timeline. Dates only where the date is the evidence or something is scheduled. New cohort ⇒ add
   its row to `COHORT-INDEX.md`. Deliverables go to the client or cohort folder.
5. **Commit.** `git add` only the touched files, then `git commit -m "wrap: YYYY-MM-DD <topic>"`.
   Reply with the hash and one line.

**Division of labour.** Tilak reports real-world external events only: sends, replies, calls and
meetings, client and team. Everything else is inferred from the session. Never invent an external
event, never ask him to log anything else, and never treat silence as an event.

Never: delete a file, move a file, edit `CLAUDE.md` without a yes, touch `_archive/`, write to a
frozen ledger, store a draft, or write anything before the changeset is approved.
