# Write Policy — DRAFT for review

**Status: provisional (2026-09-08).** Not yet in force. Once approved, the "Rules" block is pasted into `CLAUDE.md` as a new section (on Tilak's explicit yes, since `CLAUDE.md` is protected) and this file moves to `_archive/`.

**What it replaces.** Seven sinks, each with its own "update every session" ritual: `MEMORY.md`, `taste-n-judgement.md`, `files/OUTBOUND_MEMORY.md` §7, `files/LEARNINGS_LOG.md`, `files/SEND_LOG.csv`, `files/REPLY_LOG.csv`, Notion. The audits show the ritual model under-records reality (6-row send log, 2-row reply log) while the insight files grow without bound. The four insight files keep their value and their own maintenance rules; what changes is that every new fact has exactly one home, drafts are never stored, and writing happens at one trigger with one notification.

---

## Rules

### 1 · Sinks — one home per fact

| Sink | Holds | Written |
|---|---|---|
| **Notion tracker** | Per-clinic outbound state: sends, follow-up dates, shop results, wedges, notes | By Tilak, live. Unchanged. Never duplicated into the repo. |
| **`CLAUDE.md`** | Operating contract, precedence, folder map | Only on Tilak's explicit yes |
| **`MEMORY.md`** | How to work with Tilak; confirmed vs provisional calibration; live project threads | At wrap, per its own maintenance block |
| **`taste-n-judgement.md`** | How Tilak judges work: copy, tone, design, evidence, commercials | At wrap, same session as the feedback |
| **`files/OUTBOUND_MEMORY.md`** | Tripwires, hook rankings, banned phrases, offer terms, §6 decision log — **§6 now also takes tried → happened → changed entries** | At wrap |
| **`04 Clients/<client>/`** | Anything sent to or produced for a named client, dated in the filename | When produced |
| **`05 Prospects/<cohort>/`** | Research and mystery-shop artefacts for a cohort; new cohort ⇒ a row in `COHORT-INDEX.md` | When produced |
| **`03 Audits and Reviews/`** | Dated review documents | When produced |

**Routing test, in order:** Is it a fact about one clinic? → Notion. Is it Tilak's judgement about work quality? → taste. Is it about how we work together, or a live thread? → MEMORY. Is it an outbound rule, phrase, term or decision? → OUTBOUND_MEMORY. Is it a deliverable? → client or cohort folder. If it fits two, it goes to the higher one in the precedence ladder and nowhere else. No cross-posting.

**Frozen — read, never written:** `files/SEND_LOG.csv`, `files/REPLY_LOG.csv`, `files/LEARNINGS_LOG.md`, `_archive/`, `Project-Hand-Off/`.

### 2 · Never stored
- Pre-drafts, drafts, and unsent variants. Only the **sent** version, dated, in the client or cohort folder.
- Anything already in Notion.
- Chat reasoning, option surveys, session summaries. `git log` is the session summary.
- A restatement of a rule that already exists. Cite it instead.
- A hypothesis without its label.

### 3 · Entry discipline (the existing `MEMORY.md` rule, made universal)
- **Supersedes an entry and has real-world proof** → amend: append a dated correction beneath the old entry. Do not rewrite the old prose.
- **Genuinely new** → append.
- **Already covered** → skip.
- Every entry carries `confirmed` / `provisional` / `hypothesis`. Field use does not promote.
- An entry is ≤150 words. A new section in any insight file names what it replaces or why nothing covers it.

### 4 · The wrap — one trigger, one notification
Runs on `/wrap`, or when Tilak says the session is done.
1. Collect every candidate fact from the session. Route each by §1, or drop it by §2.
2. Post the changeset in chat as a table: **file · add/amend · one line · label.** Nothing else.
3. Unless Tilak objects, write, then `git commit -m "wrap: YYYY-MM-DD <topic>"`.
4. Objection after the fact → `git revert` the wrap commit. Git is the undo.

**Always waits for a yes, never proceeds by default:** any `CLAUDE.md` change; any edit that removes or rewrites an existing entry in the four insight files; a new top-level folder; anything touching `_archive/`.
