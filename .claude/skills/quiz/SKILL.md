---
name: quiz
description: Run a retrieval checkpoint for a phase (all its glossary terms + 10 random earlier terms). Use when the learner asks for a quiz, a retrieval checkpoint, or the gate's terminology check.
---

# Retrieval Checkpoint Quiz

## Setup

1. Phase number from the invocation args (0-6). If missing, ask.
2. Parse `GLOSSARY.md`. Entries are bullet lines of the form: bold term, a `[P#]` phase tag in backticks, an em-dash, the definition, usually with an italic *Contrast:* clause. Collect two pools:
   - every term tagged with the target phase;
   - 10 terms chosen at random from all earlier phases. Use genuine randomness (e.g., pipe the earlier-phase term list through `shuf -n 10` in Bash), not the first ten. For phase 0 there are no earlier phases: the quiz is just the P0 terms.
3. Shuffle the combined list. Announce the total question count and the pass threshold (80%) before the first term. Do not show the term list.

## Quiz loop — one term per message

For each term in order:

1. Show ONLY the term (with its phase tag). No definition, no hints, no preview of later terms. Ask the learner to define it in their own words, including the contrast where one exists.
2. Wait for the answer.
3. Reveal the glossary definition and its contrast, then score:
   - **correct** (1.0) — core meaning and the distinguishing contrast are right; wording may differ freely.
   - **partial** (0.5) — the gist without the distinction, or a sound definition with a wrong or missing contrast.
   - **missed** (0) — wrong, blank, or the term confused with its contrast partner.
   State the score with a one-line reason, then move to the next term.

Never reveal upcoming terms, even if asked. If the learner stops early, score what was answered and note the checkpoint is incomplete — an incomplete checkpoint is not a pass.

## Wrap-up

1. Report the score as a percentage (points / terms). Pass is >= 80%.
2. List every missed and partial term with its glossary definition — this is the re-study list.
3. Instruct the learner to log the result in `PROGRESS.md` under "Retrieval-checkpoint log (spaced repetition)": today's date, phases sampled, score, weak terms to revisit. Offer to make that edit for them.
