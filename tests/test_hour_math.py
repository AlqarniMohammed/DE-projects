"""The published hour math must reconcile with the live phase budgets.

The phase READMEs' Budget headers are the source of truth; WHY.md and
GUIDE.md quote the sum. A phase edit that moves a budget without
re-truing the quoted totals is exactly the drift this pins down
(it happened once: v1.4's first cut left the v1.3 pace table in place).
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

BUDGET_RE = re.compile(r"\*\*Budget:\*\* ~(\d+) hours")
TOTAL_RE = re.compile(r"~(\d+) h(?:ours)?\b")


def phase_budgets():
    budgets = {}
    for readme in sorted(ROOT.glob("phases/phase-*/README.md")):
        m = BUDGET_RE.search(readme.read_text())
        assert m, f"no Budget header in {readme}"
        budgets[readme.parent.name] = int(m.group(1))
    return budgets


def test_seven_phases_have_budgets():
    assert len(phase_budgets()) == 7


def test_why_md_quotes_the_live_sum():
    total = sum(phase_budgets().values())
    why = (ROOT / "reference" / "WHY.md").read_text()
    m = re.search(r"phase budgets sum to \*\*~(\d+) hours\*\* \(([\d +]+)\)", why)
    assert m, "WHY.md hour-math sentence not found"
    assert int(m.group(1)) == total, f"WHY.md says {m.group(1)}, budgets sum to {total}"
    parts = [int(p) for p in m.group(2).split("+")]
    assert sorted(parts) == sorted(phase_budgets().values()), "WHY.md breakdown != phase headers"


def test_guide_pacing_recipe_quotes_the_live_sum():
    total = sum(phase_budgets().values())
    guide = (ROOT / "GUIDE.md").read_text()
    m = re.search(r"all seven sum to \*\*~(\d+) h\*\*", guide)
    assert m, "GUIDE.md pacing-recipe total not found"
    assert int(m.group(1)) == total, f"GUIDE.md says {m.group(1)}, budgets sum to {total}"


def test_progress_evidence_rows_match_gate_items():
    """Each phase's PROGRESS.md evidence table must have at least as many
    blank rows as the phase README has gate checklist items."""
    progress = (ROOT / "PROGRESS.md").read_text()
    gate_counts = {}
    for readme in sorted(ROOT.glob("phases/phase-*/README.md")):
        text = readme.read_text()
        gate = re.search(r"## Competency gate.*?(?=\n## |\Z)", text, re.S)
        assert gate, f"no gate section in {readme}"
        n = int(re.search(r"phase-(\d)", readme.parent.name).group(1))
        gate_counts[n] = len(re.findall(r"^- \[ \]", gate.group(0), re.M))
    sections = re.split(r"^## Phase (\d) ", progress, flags=re.M)
    for i in range(1, len(sections) - 1, 2):
        phase = int(sections[i])
        body = sections[i + 1].split("\n## ")[0]
        rows = len(re.findall(r"^\| +\| +\|$", body, re.M))
        assert rows >= gate_counts[phase], (
            f"Phase {phase}: {gate_counts[phase]} gate items but only {rows} evidence rows"
        )
