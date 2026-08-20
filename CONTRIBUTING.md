# Contributing

Contributions that keep the framework alive are welcome:

- **Link rot** — a course moved, an exam-guide PDF changed: PR straight away (the weekly link-check Action files an issue when it catches one first).
- **Dataset menus** — new vetted options for a satellite's menu in [`reference/DATASETS.md`](reference/DATASETS.md) / the prompt catalog: PR with size, link, and why it fits the satellite's fixed objectives.
- **Prompt & skill improvements** — better scenario rules or catalog blocks in [`prompts/`](prompts/), or refinements to the skills in [`.claude/skills/`](.claude/skills/): PR.
- **Glossary terms** — PRs must keep the strict format (one `` `[P#]` `` tag per line); CI runs `tools/glossary_check.py` and will tell you if a line breaks the grammar.
- **Your run** — if you ran the framework from a fork, an issue linking your gate evidence and what you'd change is the most valuable feedback there is.

**Curriculum changes** (phase content, gates, tool verdicts, cert strategy) need an **issue first** — every existing choice traces to the research in [`sources/research/`](sources/research/) and the decisions in [`CHANGELOG.md`](CHANGELOG.md), so a change proposal should engage that evidence, not just preference. Gate criteria and satellite objectives are the framework's level guarantee; PRs that lower a bar without an agreed issue won't merge.

Workflow: branch → PR → squash-merge (the same rule the framework itself teaches from Phase 1).
