#!/usr/bin/env python3
"""Static consistency checks for ai-metacognitive-core."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path("/Users/liming/.codex/skills/ai-metacognitive-core")
SKILL_MD = ROOT / "SKILL.md"
REQUIRED_FILES = [
    ROOT / "agents/openai.yaml",
    ROOT / "references/cognitive-core.md",
    ROOT / "references/immune-organ-map.md",
    ROOT / "references/situation-map.md",
    ROOT / "scripts/ai_metacognitive_core.py",
    ROOT / "scripts/doctor.py",
]
REQUIRED_SUBSKILLS = [
    "intent-grounding",
    "human-ai-collab-loop",
    "skill-router",
    "jiyao-youyao-haiyao",
    "evidence-gate",
    "closure-evolution",
]
MARKDOWN_LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def check_exists(path: Path, errors: list[str]) -> None:
    if not path.exists():
        errors.append(f"missing: {path}")


def resolve_link(source: Path, target: str) -> Path | None:
    if target.startswith("http://") or target.startswith("https://"):
        return None
    if target.startswith("/"):
        return Path(target)
    return (source.parent / target).resolve()


def check_markdown_links(path: Path, errors: list[str]) -> None:
    text = path.read_text(encoding="utf-8")
    for target in MARKDOWN_LINK_RE.findall(text):
        if target.startswith("#"):
            continue
        resolved = resolve_link(path, target)
        if resolved is None:
            continue
        if not resolved.exists():
            errors.append(f"broken link in {path}: {target} -> {resolved}")


def main() -> int:
    errors: list[str] = []

    check_exists(ROOT, errors)
    check_exists(SKILL_MD, errors)
    for path in REQUIRED_FILES:
        check_exists(path, errors)

    for name in REQUIRED_SUBSKILLS:
        check_exists(Path("/Users/liming/.codex/skills") / name / "SKILL.md", errors)

    if SKILL_MD.exists():
        check_markdown_links(SKILL_MD, errors)

    for path in REQUIRED_FILES:
        if path.suffix == ".md" and path.exists():
            check_markdown_links(path, errors)

    if errors:
        print("FAILED")
        for item in errors:
            print(f"- {item}")
        return 1

    print("OK")
    print(f"root: {ROOT}")
    print(f"subskills: {len(REQUIRED_SUBSKILLS)}")
    print(f"checked files: {len(REQUIRED_FILES) + 1}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
