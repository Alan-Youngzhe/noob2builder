#!/usr/bin/env python3
"""Validate WALL.md structure and catch common private or secret data."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
WALL = ROOT / "WALL.md"
HEADER = "| GitHub | 完成证据 | 作品 | 日期 | 一句话复盘 |"
SEPARATOR = "|---|---|---|---|---|"
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
PRIVATE_PATTERNS = {
    "email address": re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.I),
    "mainland China phone number": re.compile(r"(?<!\d)1[3-9]\d{9}(?!\d)"),
    "WeChat id": re.compile(r"\bwxid_[A-Za-z0-9_-]+\b", re.I),
    "OpenAI-style secret": re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
    "GitHub token": re.compile(r"\b(?:ghp_|github_pat_)[A-Za-z0-9_]{20,}\b"),
}


def main() -> int:
    text = WALL.read_text(encoding="utf-8")
    lines = text.splitlines()
    failures: list[str] = []

    for label, pattern in PRIVATE_PATTERNS.items():
        if pattern.search(text):
            failures.append(f"possible {label} in WALL.md")

    try:
        header_index = lines.index(HEADER)
    except ValueError:
        failures.append("wall table header is missing or changed")
        header_index = -1

    entries = 0
    if header_index >= 0:
        if header_index + 1 >= len(lines) or lines[header_index + 1] != SEPARATOR:
            failures.append("wall table separator is missing or invalid")
        for line_number, line in enumerate(lines[header_index + 2 :], header_index + 3):
            if not line.strip():
                continue
            if not line.startswith("|"):
                failures.append(f"unexpected content after wall table at line {line_number}")
                continue
            cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
            if len(cells) != 5:
                failures.append(f"wall row at line {line_number} must have 5 columns")
                continue
            entries += 1
            github, evidence, work, date, reflection = cells
            if not github or not evidence or not work or not reflection:
                failures.append(f"wall row at line {line_number} has an empty required field")
            if not DATE_RE.fullmatch(date):
                failures.append(f"wall row at line {line_number} needs date YYYY-MM-DD")

    if failures:
        print("Wall validation failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print(f"Wall validation passed: {entries} entries")
    return 0


if __name__ == "__main__":
    sys.exit(main())
