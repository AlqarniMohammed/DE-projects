---
name: explain
description: Teach any term or tool from the framework, on demand. Use when the learner asks what something means, or how a term or tool fits this framework.
---

# Explain

Teach one term or tool, grounded in this repo's own definitions and platform.

## Procedure

1. **Term or tool from the invocation args.** If missing, ask what to explain.
2. **Look it up, in this order:**
   - `GLOSSARY.md` — find the entry (bullet lines: bold term, `[P#]` tag, definition, usually an italic *Contrast:* clause). Its definition and contrast are the backbone of the explanation; never contradict them.
   - `reference/TOOLS.md` — for tools: the verdict (CORE / AWARE / SKIP), phase placement, cert mapping, and the official-docs link.
   - The relevant phase README, when the term is the subject of a build step or satellite.
3. **Teach it in at most 300 words:**
   - what it is, in plain language;
   - the contrast that locates it — what it is NOT, or what it is most often confused with;
   - ONE concrete example grounded in this framework's platform, the taxi-data lakehouse platform (e.g., partitioning is the `year=/month=` layout the ingester writes; an incremental model is `fct_trips` processing only new trip months);
   - where the learner will use it: the phase and the specific build step, drill, or satellite.
   - For tools, include the official-docs link and the TOOLS.md verdict; if the verdict is SKIP, state the framework's reason for excluding it.
4. **One check-question.** End with exactly one question that tests the contrast (not trivia), then STOP and wait for the answer. When it arrives, confirm or correct in 2-3 sentences using the glossary's contrast as the yardstick. No second question unless asked.

## If the term is nowhere in the repo

Say plainly that it appears in neither `GLOSSARY.md` nor `reference/TOOLS.md`, teach it anyway with the same structure (a sensible contrast and a taxi-lakehouse example), and suggest adding it to `GLOSSARY.md` in the strict format — one tag per line — with a ready-to-paste entry:

```
- **Term** `[P#]` — definition. *Contrast:* what it is not.
```

Tag it with the phase where it would first be needed.
