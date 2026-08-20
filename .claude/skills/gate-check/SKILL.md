---
name: gate-check
description: Check what's missing before a competency gate. Use when the learner asks whether they are ready to gate a phase, or what remains before advancing.
---

# Gate Check

Audit a phase's competency gate against the evidence actually logged. Gates decide advancement, not the calendar; an item without evidence is not done.

## Procedure

1. **Phase:** from the invocation args if given. Otherwise infer the current phase: the first phase section in `PROGRESS.md` that still has unchecked boxes.
2. **Read the canonical checklist:** the "Competency gate" section of that phase's README (`phases/phase-<n>-*/README.md`). This list is the authority; `PROGRESS.md` mirrors it.
3. **Read the evidence:** the matching phase section in `PROGRESS.md` — checkbox states plus any links, dates, scores, or screenshot references filled in.

## Report — one line per gate item

Classify every item in the README's gate checklist:

- **DONE** — box checked in PROGRESS.md AND evidence present (link, date, score, or screenshot reference).
- **PARTIAL** — box checked but no evidence linked. State exactly what evidence the item asks for.
- **MISSING** — box unchecked. Give the concrete next action, naming the exact phase-README section that produces the artifact (e.g., "Build step 4", "Prove-it assignment", "Exam mini-labs", "Publish checkpoint").

Verify claims where cheap: if evidence is a path inside this repo, check the file exists; if it is an external URL, report it as "linked, not verified" rather than confirming it.

## Verdict

End with one line: **Ready to gate** (every item DONE) or **Not yet — N items remaining**, followed by the shortest path to ready: the remaining items ordered smallest-effort first, each with a rough effort estimate. Do not soften the standard, and do not suggest advancing with items open.
