#!/usr/bin/env python3
"""Lint ponchi prompt markdown scene briefs.

This intentionally uses lightweight text checks instead of a YAML dependency.
It catches missing pipeline fields before an image batch is generated.
"""
from __future__ import annotations

import argparse
import glob
import re
from pathlib import Path


REQUIRED_TOP_LEVEL = [
    "entry_id:",
    "title:",
    "subject_type:",
    "subject_stack:",
    "brand_asset:",
    "composition_family:",
    "composition_type:",
    "view_mode:",
    "scene_goal:",
    "main_symbols:",
    "avoid:",
]

REQUIRED_SUBJECT_STACK = [
    "entry_subject:",
    "visual_subject:",
    "supporting_subjects:",
    "logo_subject:",
    "excluded_subjects:",
]

STRICT_COLOR_TOKENS = [
    "#FFFFFF",
    "#F7F9FC",
    "#1A1A1A",
    "#6B7280",
    "#EAF1FB",
    "#D6E6FA",
    "#8DB7E8",
    "#3F7FD1",
    "#123E82",
]

REQUIRED_PROMPT_PHRASES = [
    "strict white/black/gray plus approved blue accents only",
    "Do not use yellow, green, red, purple, brown, orange, rainbow colors",
    "brand colors",
]

FORBIDDEN_LOOSE_COLOR_PHRASES = [
    "mostly black linework",
    "very pale blue-gray paper tones",
    "at most one subtle blue accent",
    "青系、青灰",
    "淡い水色",
    "ロゴ入り",
    "logo-bearing",
]


def extract_yaml_blocks(text: str) -> list[str]:
    return re.findall(r"```yaml\s*(.*?)```", text, flags=re.DOTALL)


def has_nonempty_field(block: str, field: str) -> bool:
    pattern = re.compile(rf"^\s*{re.escape(field)}\s*(.*)$", flags=re.MULTILINE)
    match = pattern.search(block)
    if not match:
        return False
    value = match.group(1).strip()
    return bool(value)


def lint_block(block: str, index: int) -> list[str]:
    errors: list[str] = []
    entry = "unknown"
    match = re.search(r"^\s*entry_id:\s*(.+)$", block, flags=re.MULTILINE)
    if match:
        entry = match.group(1).strip() or "unknown"

    for field in REQUIRED_TOP_LEVEL:
        if field not in block:
            errors.append(f"block {index} ({entry}): missing {field}")

    if "subject_stack:" in block:
        for field in REQUIRED_SUBJECT_STACK:
            if field not in block:
                errors.append(f"block {index} ({entry}): missing subject_stack.{field}")

    if not has_nonempty_field(block, "visual_subject:"):
        errors.append(f"block {index} ({entry}): subject_stack.visual_subject is empty")

    if "official_overlay" in block and "clearspace:" not in block:
        errors.append(f"block {index} ({entry}): official overlay entry needs clearspace")

    return errors


def lint_file(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    blocks = extract_yaml_blocks(text)
    if not blocks:
        return [f"{path}: no yaml scene brief blocks found"]

    errors: list[str] = []
    for index, block in enumerate(blocks, start=1):
        for error in lint_block(block, index):
            errors.append(f"{path}: {error}")

    for token in STRICT_COLOR_TOKENS:
        if token not in text:
            errors.append(f"{path}: missing strict color token {token}")

    for phrase in REQUIRED_PROMPT_PHRASES:
        if phrase not in text:
            errors.append(f"{path}: missing required color/brand phrase: {phrase}")

    for phrase in FORBIDDEN_LOOSE_COLOR_PHRASES:
        if phrase in text:
            errors.append(f"{path}: loose color phrase is forbidden: {phrase}")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="+", type=Path)
    args = parser.parse_args()

    paths: list[Path] = []
    for path in args.paths:
        if any(char in str(path) for char in "*?[]"):
            matches = [Path(match) for match in glob.glob(str(path))]
            paths.extend(matches or [path])
        else:
            paths.append(path)

    errors: list[str] = []
    for path in paths:
        if not path.exists():
            errors.append(f"{path}: file not found")
            continue
        errors.extend(lint_file(path))

    if errors:
        for error in errors:
            print(error)
        return 1

    print(f"ok: {len(paths)} file(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
