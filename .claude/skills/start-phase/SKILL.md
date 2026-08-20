---
name: start-phase
description: Walk a phase step by step (the phase loop, interactively). Use when the learner starts a new phase or wants guided passage through the current one.
---

# Start Phase

Guide the learner through a phase's loop interactively — one step per message, waiting for the learner between steps. Never dump the whole plan at once; each message covers the current step only.

## Setup

- Phase from the invocation args; otherwise infer the current phase: the first section in `PROGRESS.md` with unchecked boxes.
- Read that phase's README in full (`phases/phase-<n>-*/README.md`) before step 1. It is the script; quote it rather than paraphrasing loosely.
- If PROGRESS.md shows some of the phase already done, say so and offer to jump to the first incomplete step.

## The loop — one message per step, wait for a go-ahead between steps

1. **Orientation:** the phase header line (duration, hours budget, cost posture) and the Objectives, verbatim. Ask when the learner is ready.
2. **Re-verify:** the README's "Before starting, re-verify" checks — facts that may have changed since the framework was written. Have the learner confirm each one before proceeding.
3. **Terminology:** list the phase's terms from the "New terminology" section, pointing at `GLOSSARY.md`. Offer to run the `quiz` skill now instead of passive reading.
4. **Learn table, row by row:** for each row in order — the resource, its scope (what to cover, what to skip), and the "Pinned by" exercise that pins it. One row (or one coherent group) per message; advance when the learner reports it done. If the phase has a **video-lane table** (an optional-swap table after the default one, catalogued in `reference/COURSES.md`), ask which lane the learner picks for each row it names *before* walking that row — one lane per row, the other lane is the fallback, never both; the "Pinned by" exercise is identical in both lanes.
5. **Build steps, in order:** one numbered platform build step per message — the step, its done-condition, and any AI-rule note (what must be hand-written vs delegated). Help with the actual work when asked.
6. **Prove-it:** the Prove-it assignment and its explicit done-condition.
7. **Satellite:** the satellite build for this phase. Offer the `satellite-brief` skill for a generated unique brief instead of the default spec.
8. **Gate:** offer the `gate-check` skill to audit readiness item by item.
9. **Log:** tick the phase's completed boxes in `PROGRESS.md` with evidence links, and run the phase's retrieval checkpoint (the `quiz` skill).
10. **Publish:** the Publish checkpoint — what this phase's post(s) should show and why.
11. **Hand-off:** link the next phase's README and stop.

## Rules

- Wait for an explicit go-ahead between steps; a question about the current step stays on the current step.
- Track position across the conversation — after a digression, restate which step is current before continuing.
- If the learner disappears mid-phase and returns after a break, suggest the `resume` skill rather than restarting the loop.
