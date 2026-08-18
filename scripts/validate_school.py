#!/usr/bin/env python3
"""Validate the Noob2Builder skill package without network access."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "manifest.json"
REQUIRED = {
    "SKILL.md",
    "WALL.md",
    "agents/openai.yaml",
    "references/catalog.md",
    "references/lessons/shared/database-and-data-authority.md",
    "references/pedagogy.md",
    "references/state-schema.md",
    "references/sources.md",
}
SECRET_PATTERNS = {
    "OpenAI-style secret": re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
    "GitHub classic token": re.compile(r"\bghp_[A-Za-z0-9]{20,}\b"),
    "GitHub fine-grained token": re.compile(r"\bgithub_pat_[A-Za-z0-9_]{20,}\b"),
    "AWS access key": re.compile(r"\bAKIA[A-Z0-9]{16}\b"),
}
LINK_RE = re.compile(r"\]\(([^)]+)\)")
CODE_PATH_RE = re.compile(r"`((?:\.\.?/|references/)[^`\s]+\.md)`")
ALAN_WORKFLOW = [
    "brainstorming 发散探索",
    "GrillMe 需求访谈与收敛",
    "PRD v0（薄的需求初稿）",
    "构思 Design System",
    "Lovable 生成可见原型",
    "根据原型反写 PRD v1",
    "让 AI 产出技术 Spec",
    "敏捷开发一个端到端 MVP",
    "先验证可行性和用户核心动作",
    "再补工程质量、测试和跨模型 Review",
]
REQUIRED_METHOD_PHRASES = [
    "独立交接测试",
    "核心产品行为应该大差不差",
]
DATABASE_METHOD_PHRASES = [
    "数据只有一个逻辑权威源",
    "不要把不同维度放在一张候选表里直接比较",
    "不能只看 HTTP 200 或 Agent 的“成功”",
]


def fail(message: str, failures: list[str]) -> None:
    failures.append(message)


def validate_manifest(failures: list[str]) -> set[str]:
    try:
        data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"manifest.json cannot be read: {exc}", failures)
        return set()

    version = data.get("version")
    if not isinstance(version, str) or not re.fullmatch(r"\d+\.\d+\.\d+", version):
        fail("manifest version must use MAJOR.MINOR.PATCH", failures)

    files = data.get("files")
    if not isinstance(files, list) or not all(isinstance(item, str) for item in files):
        fail("manifest files must be a string list", failures)
        return set()

    listed = set(files)
    for path in sorted(REQUIRED - listed):
        fail(f"required file is not listed in manifest: {path}", failures)
    for path in sorted(listed):
        if not (ROOT / path).is_file():
            fail(f"manifest points to missing file: {path}", failures)

    packaged = {
        path.relative_to(ROOT).as_posix()
        for path in ROOT.rglob("*")
        if path.is_file()
        and ".git" not in path.parts
        and "__pycache__" not in path.parts
        and path.name != "manifest.json"
    }
    for path in sorted(packaged - listed):
        fail(f"packaged file is missing from manifest: {path}", failures)
    for path in sorted(listed - packaged):
        fail(f"manifest lists a non-packaged file: {path}", failures)
    return listed


def validate_skill(failures: list[str]) -> None:
    text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    if not text.startswith("---\nname: noob2builder\n"):
        fail("SKILL.md frontmatter or name is invalid", failures)
    if "description:" not in text.split("---", 2)[1]:
        fail("SKILL.md is missing its description", failures)
    cursor = -1
    for step in ALAN_WORKFLOW:
        position = text.find(step, cursor + 1)
        if position < 0:
            fail(f"Alan workflow step is missing or out of order: {step}", failures)
            break
        cursor = position
    for phrase in REQUIRED_METHOD_PHRASES:
        if phrase not in text:
            fail(f"Alan method requirement is missing from SKILL.md: {phrase}", failures)

    database_lesson = (
        ROOT / "references/lessons/shared/database-and-data-authority.md"
    ).read_text(encoding="utf-8")
    for phrase in DATABASE_METHOD_PHRASES:
        if phrase not in database_lesson:
            fail(f"database method requirement is missing: {phrase}", failures)


def validate_markdown(listed: set[str], failures: list[str]) -> None:
    for relative in sorted(listed):
        path = ROOT / relative
        if path.suffix != ".md":
            continue
        text = path.read_text(encoding="utf-8")
        if "[TODO" in text or "TODO:" in text:
            fail(f"placeholder remains in {relative}", failures)
        for label, pattern in SECRET_PATTERNS.items():
            if pattern.search(text):
                fail(f"possible {label} in {relative}", failures)
        for target in LINK_RE.findall(text):
            clean = target.split("#", 1)[0].strip()
            if not clean or clean.startswith(("http://", "https://", "mailto:")):
                continue
            resolved = (path.parent / clean).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                fail(f"relative link escapes skill root in {relative}: {target}", failures)
                continue
            if not resolved.exists():
                fail(f"broken relative link in {relative}: {target}", failures)
        for target in CODE_PATH_RE.findall(text):
            if "*" in target:
                continue
            if target.startswith("references/"):
                resolved = ROOT / target
            else:
                resolved = path.parent / target
            if not resolved.resolve().is_file():
                fail(f"broken referenced markdown path in {relative}: {target}", failures)


def main() -> int:
    failures: list[str] = []
    listed = validate_manifest(failures)
    validate_skill(failures)
    validate_markdown(listed, failures)

    if failures:
        print("Noob2Builder validation failed:")
        for item in failures:
            print(f"- {item}")
        return 1

    print(f"Noob2Builder validation passed: {len(listed)} packaged files")
    return 0


if __name__ == "__main__":
    sys.exit(main())
