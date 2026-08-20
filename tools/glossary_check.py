#!/usr/bin/env python3
"""Glossary format guard — the framework's CI check for GLOSSARY.md, and the
reference implementation of the Phase-0 Anki-generator assignment's parsing
contract.

Every glossary entry is one line with this exact grammar:

    - **Term** `[P#]` — definition

where # is the phase number 0-6, the dash is an em-dash (—), and the
definition may end with an optional *Contrast:* tail. Exactly one `[P#]`
tag is allowed per line, anywhere in the line. Any line that starts with
"- **" and breaks the grammar makes this script fail loudly: it prints
file:line plus the reason and exits 1.

Warning: Building your own parser is the Phase-0 assignment — write yours
before reading this one.
"""

import re
import sys

# A glossary entry line must match this shape exactly:
#   "- **" term "** `[P" digit "]` — " definition
# The definition is "anything up to end of line", which naturally allows
# the optional *Contrast:* tail — it is just part of the definition text.
ENTRY_RE = re.compile(r"^- \*\*(?P<term>.+?)\*\* `\[P(?P<phase>[0-6])\]` — (?P<definition>.+)$")

# Used to count phase tags anywhere in the line (with or without backticks),
# so a stray second tag hiding in the definition is still caught.
TAG_RE = re.compile(r"\[P[0-6]\]")


def check_line(line):
    """Check one entry line. Returns (phase, reason).

    phase  -> int 0-6 when the line is valid, else None
    reason -> None when the line is valid, else a human-readable violation
    """
    # Rule 1: exactly one [P#] tag per line, anywhere in the line.
    tag_count = len(TAG_RE.findall(line))
    if tag_count != 1:
        return None, f"expected exactly one [P#] tag (P0-P6), found {tag_count}"

    # Rule 2: the whole line must match the entry grammar.
    match = ENTRY_RE.match(line)
    if not match:
        if " — " not in line:
            return None, "missing the em-dash separator ' — ' between tag and definition"
        return None, "does not match the grammar: - **Term** `[P#]` — definition"

    # Rule 3: term and definition must contain real text, not just spaces.
    if not match.group("term").strip():
        return None, "term is empty"
    if not match.group("definition").strip():
        return None, "definition is empty"

    return int(match.group("phase")), None


def check_file(path):
    """Check every entry line in the file at `path`.

    Returns (counts, violations):
    counts     -> dict {0: n, ..., 6: n} of valid entries per phase
    violations -> list of (line_number, reason) for every bad entry line
    """
    counts = {phase: 0 for phase in range(7)}
    violations = []

    with open(path, encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            line = line.rstrip("\n")
            # Only lines that start "- **" are glossary entries; headers,
            # prose, and blank lines are not checked.
            if not line.startswith("- **"):
                continue
            phase, reason = check_line(line)
            if reason is not None:
                violations.append((line_number, reason))
            else:
                counts[phase] += 1

    return counts, violations


def main(argv):
    path = argv[1] if len(argv) > 1 else "./GLOSSARY.md"
    counts, violations = check_file(path)

    if violations:
        # Fail loudly: every violation, then a non-zero exit for CI.
        for line_number, reason in violations:
            print(f"{path}:{line_number}: {reason}", file=sys.stderr)
        return 1

    total = sum(counts.values())
    print(f"{path}: {total} entries OK")
    for phase in range(7):
        print(f"  P{phase}: {counts[phase]}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
