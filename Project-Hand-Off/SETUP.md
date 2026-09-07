# Setup — 4 minutes, once

*This file is for you, not for Claude. **Don't upload it** — it just tells you what to do with the rest.*

---

## Step 1 — Create the project

claude.ai → **Projects** → **Create project**. Name it something like **Valence Ops — GTM**.

## Step 2 — Paste the instructions

Open `PROJECT-INSTRUCTIONS-paste-this.txt`, copy everything **below the ═══ line**, and paste it into
the project's custom-instructions field ("What should Claude know about this project?").

**Don't upload that .txt as a knowledge file** — it belongs in the instructions box, where it applies
to every chat automatically.

## Step 3 — Upload these 7 files as project knowledge

```
00-START-HERE.md
01-STATE-OF-PLAY.md
02-BUYER-OFFER-AND-DEMO.md
03-DRAFTING-ENGINE.md
04-WEDGE-ROUTING.md
05-CLINIC-INVENTORY.md
06-DECISIONS-AND-LEARNINGS.md
```

## Step 4 — Turn on the Notion connector

Settings → Connectors → **Notion**. Make sure the **"Valence Leads tracker"** page is shared with it.
This is what keeps the project from going stale — the files carry the *reasoning*, Notion carries the
*state*.

## Step 5 — Test it

Open a chat and ask: **"Where do things stand, and what's the single most useful thing I could do
today?"**

You should get: the real numbers, the tripwire warning, both warm threads named, and a push toward
getting a call held rather than more research. If you get a generic answer, the instructions didn't
save — check step 2.

---

## Why it's built this way

**Seven files, not thirty.** Pro projects allow unlimited files but the total must fit the context
window; past that, Claude switches to RAG and retrieves only *fragments*. That's the failure mode to
avoid — it might pull a clinic fact and miss the operating contract, so it would answer confidently
without the rules that keep it honest. These seven are sized to stay comfortably in context, so
everything is always loaded.

**The files hold reasoning; Notion holds state.** Reasoning moves slowly and is safe to freeze. State
changes every time you send a DM, so freezing it would recreate the exact problem we just spent two
sessions fixing — a document confidently asserting something reality had already moved past.

---

## When to refresh

Most of this can drift for weeks. Re-export at the desk when:

| Trigger | Update |
|---|---|
| A call gets held, or a pilot starts | `01` — and several "unproven" items may finally become evidence |
| The tripwire is counted properly, or fires | `01` |
| The free-pilot / paid-implementation question is answered | `01`, `02`, `03` |
| A new batch gets worked, or shop results land | `05` |
| A rule changes at the desk | whichever of `02`–`04` owns it |

Nothing else needs touching. If you find yourself refreshing these weekly, that's the "work that feels
productive" failure mode — the files aren't the constraint.

---

## Known gaps in this handoff — stated so they don't surprise you

- **`05` is a snapshot.** Accurate to 13 Aug. Notion is live and wins. This is flagged at the top of
  the file and in the instructions, so Claude should check rather than assert.
- **No per-clinic dossiers for Batch 1.** You get status, priority and the notable caveats — enough to
  brainstorm and draft, not the full research. The Batch-2 clinics have their complete shop transcripts
  because those are the sharpest evidence you own.
- **The parked ~120 clinics are summarised, not carried.** Deliberate — they aren't being worked, and
  including them would push toward RAG for no benefit.
- **Nothing about Apify, scraping pipelines or file-hygiene rules.** Desk work; irrelevant on a phone.
