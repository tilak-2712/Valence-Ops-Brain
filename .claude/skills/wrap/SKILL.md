---
name: wrap
description: Session-close changeset for the Valence Ops vault. Collects what this session learned or produced, routes each item to its single home per CLAUDE.md § Write policy, posts a one-table changeset in chat, then writes and commits. Use when Tilak says the session is done, asks to wrap up, or types /wrap.
---

# /wrap — adopted 2026-09-08

Read `CLAUDE.md` § "Write policy" first. Then:

1. **Collect.** List every candidate: a clinic fact, a piece of Tilak feedback, a working-preference, a rule change, a deliverable produced, a thread opened or closed.
2. **Route or drop.** Apply the routing test in §1 of that section. Drop anything in §2 of that section. Label each survivor `confirmed` / `provisional` / `hypothesis`.
3. **Changeset.** Post one table and nothing else:

   | File | Add / Amend | What, in one line | Label |
   |---|---|---|---|

   Items that need a yes (§4, last paragraph) go in a second short list headed "Waiting for your yes".
4. **Write.** Unless an objection arrived, apply the changes. In the four insight files: append or add a dated correction beneath; never rewrite existing prose; never create a second frontmatter block. New cohort ⇒ add its row to `COHORT-INDEX.md`. Deliverables go to the client or cohort folder with the date in the filename.
5. **Commit.** `git add` only the touched files, then `git commit -m "wrap: YYYY-MM-DD <topic>"`. Reply with the hash and one line.

Never: delete a file, move a file, edit `CLAUDE.md`, touch `_archive/`, write to a frozen ledger, store a draft.
