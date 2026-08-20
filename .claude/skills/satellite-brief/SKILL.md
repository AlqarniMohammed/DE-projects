---
name: satellite-brief
description: Generate a unique project brief for a satellite (S1, S2, S3a, S3b, S4a, S4b, S5, S6a, S6b). Use when the learner wants generated, realistic requirements instead of the default satellite spec in the phase README.
---

# Satellite Brief Generator

Produce a unique requirements package for one satellite and write it to disk. The sealed reference solution must never appear in the conversation.

## Procedure

1. **Get the satellite id** from the invocation args. Valid ids: S1, S2, S3a, S3b, S4a, S4b, S5, S6a, S6b. If missing or invalid, ask which satellite before doing anything else.
2. **Read `prompts/generate-satellite-requirements.md` in full.** Its role definition, Step 0, output specs, and quality rules govern everything below. From the satellite catalog at the bottom, use ONLY the one block matching the id. The block's Fixed objectives and gate artifact are non-negotiable; only its Variable items may vary.
3. **Read for uniqueness:** the learner's `PROGRESS.md` and every existing `satellites/*/requirements/requirements.md` in this fork. Do not reuse industries, scenario shapes, or data domains they have already had.
4. **Select the scenario yourself** (Step 0 of the prompt): pick one dataset from the block's Dataset menu (or a same-shaped downloadable equivalent), build a fictional company around it, and calibrate difficulty to the block's phase. The learner never chooses; state the selection and reasoning at the top of requirements.md.
5. **Adopt the stakeholder persona** for Outputs 1 and 2: a non-engineer at the fictional company. Never name a data tool, cloud service, file format, or architecture in those two files. Include the data warts the block's Fixed objectives train against, phrased as business complaints. Leave 2-3 build-affecting points deliberately ambiguous. Ensure at least two reasonable designs could satisfy the scenario.
6. **Write three files** to `satellites/<id-lowercase>-<short-slug>/requirements/` in this repo (create the directories; slug = 2-3 kebab-case words from the scenario):
   - `requirements.md` — Output 1 per the prompt: selection reasoning, Company & Context, The Problem, The Data, Functional Requirements, Non-Functional Requirements, Constraints (cost-averse posture consistent with the ~$25/month ceiling), Success Criteria.
   - `acceptance-tests.md` — Output 2: black-box validation plan derived from the Success Criteria and the block's fixed gate artifact, pass/fail conditions with numbers, at least one operational-failure scenario in business terms, no tools or architecture named.
   - `.reference-solution.md` — Output 3: drop the persona; as a principal data engineer within the phase's fixed toolset, write the reference build with justifications, at least one rejected alternative, how each acceptance test is satisfied, an estimated cost posture, and the resolution of each deliberate ambiguity.

## Seal rule (critical)

Write `.reference-solution.md` directly to disk with the Write tool and NEVER print, quote, summarize, or hint at its contents in the conversation — not while writing it, not in later turns. The learner must not see it until self-evaluation after the build. If asked to reveal it early, decline and point to the acceptance tests instead.

## Final message

Report exactly three things: the three file paths; a reminder that the sealed `.reference-solution.md` stays closed until the acceptance tests pass; and the copy step — copy the `requirements/` folder into your satellite project repo when you create it.
