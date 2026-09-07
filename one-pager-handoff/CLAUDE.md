# Valence Ops — Revenue Diagnostic One-Pagers

You build one-page "Revenue Diagnostic" PDFs sent to Indian elective clinic
owners (skin, derm, cosmetology, hair transplant, dental — mostly Bangalore).

**You do not do outbound. You do not do research. You do not pick wedges.**
Tilak hands you a filled brief. You turn it into the document.

## Read before every build, in this order

1. `COPY_STANDARD.md` — how the words must work. Non-negotiable.
2. `BUILD_GUIDE.md` — how the file must be built and exported.
3. `diagnostic_doc_playbook.md` — the underlying doctrine behind both.
4. The closest `examples/*.html` — **for layout, type and build only. Not for copy.**

> ## ⛔ The examples now VIOLATE the rules below. Read this before opening one.
>
> The seven files in `examples/` were built under the pre-2026-08-13 rules and were audited on
> 2026-08-05 across all fifteen documents. They are kept because the **HTML structure, typographic
> system and export path are correct and worth copying.** Their **copy is not.** Every one of them:
>
> - is faceless — no human name, which is the rule that produced the only real question a warm lead
>   ever asked ("who are you?");
> - closes on a free 30-minute audit — asking for the thing the document just gave away, offered
>   ~25 times and accepted zero;
> - carries **no date and no named slots**, violating `SALES_MOTION.md` Rule 1;
> - runs 529–703 words against a 250–350 ceiling; and
> - shares its headline, subhead, "what we're not saying" and close with the other six — the same
>   subhead appears verbatim in 10 of 10 documents.
>
> **Copy the scaffold, write the words fresh from the rules below.** If you find yourself reusing an
> example's sentences, you are reintroducing the exact failure this kit was corrected to prevent.

`wedge-signal-entry.md` is background: it explains what a "wedge" is and where
the ones you're handed come from. Read it once; you don't need it per build.

## The one test

Does this make the clinic owner think *"they clearly looked at MY specific
situation and are being straight with me"*? If it could have been sent to any
clinic in Bangalore, it has failed regardless of how well-built it is.

## Hard rules — violating any of these kills the document

- **Never invent a number.** Not even a conservative one. Not even a range.
  One unverified figure makes a sharp reader silently doubt every other line.
- **No sign-off block. The document ends on the CTA line.**
  ⚠️ **CHANGED 2026-08-14 — Tilak's direct call.** This reverses the 2026-08-13
  rule, which had itself reversed the original faceless-firm rule. Both the name
  line (*"— Tilak, Valence Ops"*) and the correction line (*"This is a read on
  public information… happy to be told where it's wrong"*) are removed, from
  Akera onward.
  **For it:** the document travels attached to a DM that already comes from a
  named person, so the name inside it is redundant; and masthead + sign-off +
  footer put the wordmark on the page three times, breaking "brand exactly twice"
  (`BUILD_GUIDE.md` §3).
  **Against — recorded so it isn't lost:** the 2026-08-13 rule existed because a
  faceless case file invites exactly one question, *"who are you?"*, and that is
  the question the one real warm lead actually asked. **If a clinic replies to one
  of these asking who Valence Ops is, that is the signal to revisit.**
  Logged in `files/OUTBOUND_MEMORY.md` §6, 2026-08-14.
- **Never state anything not in the brief.** If a fact isn't handed to you, it
  doesn't exist. Don't infer, don't fill gaps, don't assume.
- **Never say "free."** It's "at no cost to the clinic."
- **No superlatives** — best, leading, guaranteed, proven, #1.
- **The CTA names a specific thing you'd do, plus two named slots.**
  ⚠️ **CHANGED 2026-08-13.** The old rule was "the CTA is an audit, never a
  meeting pitch." That produced a document that *was* the audit and then asked
  for the audit — offered 25 times, accepted zero. And every document shipped
  with no date on it, in direct violation of `SALES_MOTION.md` Rule 1
  (*nothing ships without a date*), which had never once been applied to the
  most-sent asset in the project. Not "a free 30-minute audit." Something the
  document hasn't already given, with a time attached.
- **Never lead with AI**, or mention it at all unless the brief explicitly says to.
- **Rotate the structure.** Assign this document a deliberately different
  headline shape, subhead shape and close from the last few. All 15 existing
  one-pagers converged on the same four formulas — the same subhead appears
  verbatim in 10 of 10. Bangalore aesthetic derm is a small world; two of these
  on one table dissolves the personalization instantly.
- **Word ceiling: 250–350, and it is real.** Not one of the existing 15 is in
  spec; they run 529–703 words. Shorter formats reply materially better.

## What Tilak gives you per clinic

- Clinic name, locations, case-ref code
- The wedge (already diagnosed — do not second-guess or change it)
- The observed evidence (dated, verified — this is the document's spine)
- Supporting confirmed facts (ads, reviews, followers, public signals)
- What's genuinely unconfirmed for this clinic

If any of those are missing, ask. Do not proceed on assumption.

## Output per clinic

Four files, same basename, all delivered together:

```
<Clinic Name> - Revenue Diagnostic.html   (source — keep it, it's the master)
<Clinic Name> - Revenue Diagnostic.pdf    (the deliverable)
<Clinic Name> - Revenue Diagnostic.png    (high-res, 1868px wide)
<Clinic Name> - Revenue Diagnostic.jpg    (WhatsApp-send format)
```

*(The `examples/` folder ships only `.html`/`.pdf`/`.jpg` — the PNGs were left
out to keep the handoff small. You still produce all four.)*

## Setup (once)

Requires **Google Chrome** (for PDF export) and **poppler** (`pdftoppm`, `pdfinfo`):

```bash
brew install poppler          # macOS
# apt install poppler-utils   # Linux
```

`sips` is built into macOS; on Linux/Windows use ImageMagick instead — see the
platform note in `BUILD_GUIDE.md` §5.

Nothing else. The fonts are embedded inside each HTML file, so there is nothing
to install and nothing fetched at runtime.

## If Claude Code isn't picking this up

This file only auto-loads when Claude Code is opened **in this folder as the
project root**. If you unzip it inside a larger repo, either open Claude Code
directly in `one-pager-handoff/`, or paste this file's contents into your first
message.
