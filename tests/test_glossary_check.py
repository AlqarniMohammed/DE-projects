"""Tests for tools/glossary_check.py — the glossary format guard.

Covers the parsing contract: a well-formed entry parses, and each of the
common breakages (malformed tag, duplicate tags, missing em-dash) fails
loudly. Finally, the real GLOSSARY.md at the repo root must pass.
"""

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "tools"))

import glossary_check


def test_well_formed_line_parses():
    line = "- **Data lake** `[P2]` — Object storage holding raw files. *Contrast:* data warehouse."
    phase, reason = glossary_check.check_line(line)
    assert reason is None
    assert phase == 2


def test_malformed_tag_fails_loudly():
    line = "- **Data lake** `[P1→P2]` — Object storage holding raw files."
    phase, reason = glossary_check.check_line(line)
    assert phase is None
    assert reason is not None


def test_two_tags_fail_loudly():
    line = "- **Data lake** `[P1]` — Object storage; see also `[P2]` for the lakehouse."
    phase, reason = glossary_check.check_line(line)
    assert phase is None
    assert reason is not None


def test_missing_em_dash_fails_loudly():
    line = "- **Data lake** `[P1]` Object storage holding raw files."
    phase, reason = glossary_check.check_line(line)
    assert phase is None
    assert reason is not None


def test_real_glossary_passes():
    glossary = REPO_ROOT / "GLOSSARY.md"
    counts, violations = glossary_check.check_file(glossary)
    assert violations == [], f"GLOSSARY.md has format violations: {violations}"
    assert sum(counts.values()) > 0, "GLOSSARY.md should contain at least one entry"
