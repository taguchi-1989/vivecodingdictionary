#!/usr/bin/env python3
"""
☆ 違反のうち「status: drafting + 著者欄に記入あり」のエントリを needs_review に昇格する。

validator のルール:
- status: drafting のあいだは「非エンジニアのつまずき」「私のコメント」は空スケルトンのまま
- 著者本人 or モバイル inbox から記入が入った時点で、status を needs_review に上げる運用

本スクリプトはその運用を一括で実施する。dry-run で対象確認してから本番。

Usage:
    python3 scripts/promote_authored_drafting.py --dry-run
    python3 scripts/promote_authored_drafting.py
"""

from __future__ import annotations

import argparse
import io
import re
import sys
from pathlib import Path

if sys.platform == "win32" and hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", line_buffering=True)

ROOT = Path(__file__).resolve().parent.parent
ENTRIES_DIR = ROOT / "content" / "entries"

# 私のコメントの 4 ラベル（記入があるかチェックする）
COMMENT_LABELS = ["第一印象", "良い点", "ダメな点", "誰向けか"]


def split_frontmatter(text: str) -> tuple[str, str] | None:
    """frontmatter とボディを分離。`---\\n...\\n---\\n` 形式のみ対応。"""
    m = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n", text, re.DOTALL)
    if not m:
        return None
    return m.group(1), text[m.end():]


def get_status(fm_text: str) -> str | None:
    m = re.search(r"^status:\s*(\S+)\s*$", fm_text, flags=re.MULTILINE)
    return m.group(1).strip() if m else None


def section_text(body: str, heading: str) -> str:
    """## heading 直下の本文を返す（次の ## まで）。HTML コメントは剥がす。"""
    m = re.search(re.escape("## " + heading) + r"\s*\n(.*?)(?=\n## |\Z)", body, flags=re.DOTALL)
    if not m:
        return ""
    body_part = m.group(1)
    body_part = re.sub(r"<!--.*?-->", "", body_part, flags=re.DOTALL)
    return body_part


def has_tsumazuki_content(body: str) -> bool:
    """## 非エンジニアのつまずき に箇条書きの中身が 1 つでもあるか。"""
    sec = section_text(body, "非エンジニアのつまずき")
    for line in sec.splitlines():
        line = line.strip()
        if not line.startswith("-"):
            continue
        rest = line[1:].strip()
        if rest:
            return True
    return False


def has_comment_content(body: str) -> bool:
    """## 私のコメント の 4 ラベルどれかにコロン後の本文が入っているか。"""
    sec = section_text(body, "私のコメント")
    for line in sec.splitlines():
        line = line.strip()
        if not line.startswith("-") or ":" not in line:
            continue
        # 例: `- 🙂 第一印象: 微細化での高性能化が…`
        if not any(label in line for label in COMMENT_LABELS):
            continue
        after = line.split(":", 1)[-1].strip()
        if after:
            return True
    return False


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true", help="対象を表示するだけ、書き換えない")
    args = ap.parse_args()

    candidates: list[tuple[Path, str, str]] = []
    for path in sorted(ENTRIES_DIR.rglob("*.md")):
        try:
            text = path.read_text(encoding="utf-8")
        except Exception:
            continue
        split = split_frontmatter(text)
        if not split:
            continue
        fm_text, body = split
        status = get_status(fm_text)
        if status != "drafting":
            continue

        tsum = has_tsumazuki_content(body)
        comm = has_comment_content(body)
        if not (tsum or comm):
            continue

        reasons: list[str] = []
        if tsum:
            reasons.append("つまずき記入")
        if comm:
            reasons.append("コメント記入")
        candidates.append((path, ",".join(reasons), text))

    print(f"対象: {len(candidates)} 件\n")

    flipped = 0
    for path, reason, text in candidates:
        rel = path.relative_to(ROOT).as_posix()
        if args.dry_run:
            print(f"  [dry-run] {rel} ({reason})")
            continue

        # status: drafting → needs_review（fm 内の 1 つ目だけ）
        new_text, n = re.subn(
            r"(?m)^status:\s*drafting\s*$",
            "status: needs_review",
            text,
            count=1,
        )
        if n != 1:
            print(f"  SKIP: status 行が 1 つだけ見つかりませんでした: {rel}")
            continue
        path.write_text(new_text, encoding="utf-8")
        print(f"  promoted: {rel} ({reason})")
        flipped += 1

    print(f"\n=== promoted {flipped} / {len(candidates)} ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
