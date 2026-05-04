#!/usr/bin/env python3
"""
content/entries/**/*.md のファイル名末尾にステータス絵文字を付ける／更新する。

ステータス（YAML フロントマター status: から決定、必ず 1 つ付く）:
  ⬜ skeleton / candidate
  ✏️ drafting
  👁  needs_review
  ✅ ready
  🗄 archived / sample

著者コメント（追加で付く）:
  💬 「## 私のコメント」節に著者の記入がある（プレースホルダー以外の非空文字）

例:
  B-1_gemini.md  →  B-1_gemini ✅💬.md
  B-3_chatgpt.md →  B-3_chatgpt ✏️.md
  G-7.md          →  G-7 🗄.md

Usage:
    python3 scripts/apply_status_markers.py --dry-run
    python3 scripts/apply_status_markers.py
    python3 scripts/apply_status_markers.py --filter content/entries/service
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ENTRIES_DIR = ROOT / "content" / "entries"

STATUS_EMOJI = {
    "skeleton": "⬜",
    "candidate": "⬜",
    "drafting": "✏️",
    "needs_review": "👁",
    "ready": "✅",
    "archived": "🗄",
    "sample": "🗄",
}

COMMENT_EMOJI = "💬"

ALL_MARKERS = ["⬜", "✏️", "👁", "✅", "🗄", "💬"]


def parse_frontmatter(text: str) -> dict[str, str]:
    m = re.match(r"^---\r?\n(.*?)\r?\n---", text, re.DOTALL)
    if not m:
        return {}
    fm: dict[str, str] = {}
    for line in m.group(1).splitlines():
        mm = re.match(r"^([A-Za-z_][\w-]*):\s*(.*?)\s*$", line)
        if mm:
            fm[mm.group(1)] = mm.group(2).strip().strip('"').strip("'")
    return fm


COMMENT_SECTION_RE = re.compile(r"##\s*私のコメント\s*\n(.*?)(?=\n##\s|\Z)", re.DOTALL)
COMMENT_LINE_RE = re.compile(r"^-\s*[🙂👍👎👥][^:]*:\s*(.+?)\s*$")


def is_comment_filled(text: str) -> bool:
    m = COMMENT_SECTION_RE.search(text)
    if not m:
        return False
    for line in m.group(1).splitlines():
        mm = COMMENT_LINE_RE.match(line)
        if mm and mm.group(1).strip():
            return True
    return False


def strip_existing_marker(stem: str) -> str:
    """末尾の「空白＋既知マーカーの並び」を取り除く（複数回 OK）。"""
    while True:
        prev = stem
        s = stem.rstrip()
        for marker in ALL_MARKERS:
            if s.endswith(marker):
                s = s[: -len(marker)]
                break
        if s == prev:
            break
        stem = s
    return stem.rstrip()


def compute_new_name(path: Path, fm: dict[str, str], comment_filled: bool) -> str | None:
    status = fm.get("status")
    if not status:
        return None
    emoji = STATUS_EMOJI.get(status)
    if emoji is None:
        return None
    base = strip_existing_marker(path.stem)
    suffix = f" {emoji}"
    if comment_filled:
        suffix += COMMENT_EMOJI
    return f"{base}{suffix}.md"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dry-run", action="store_true", help="変更内容を表示するだけ")
    ap.add_argument(
        "--filter",
        default=None,
        help="リネーム対象を絞る（content/entries 配下の相対 or 絶対パスを部分一致）",
    )
    args = ap.parse_args()

    if not ENTRIES_DIR.is_dir():
        print(f"ERROR: {ENTRIES_DIR} not found", file=sys.stderr)
        return 1

    renames: list[tuple[Path, Path]] = []
    skipped_no_status: list[Path] = []
    unknown_status: list[tuple[Path, str]] = []

    for md in sorted(ENTRIES_DIR.rglob("*.md")):
        if args.filter and args.filter not in str(md):
            continue
        try:
            text = md.read_text(encoding="utf-8")
        except Exception as e:
            print(f"  read failed: {md}: {e}", file=sys.stderr)
            continue
        fm = parse_frontmatter(text)
        status = fm.get("status")
        if not status:
            skipped_no_status.append(md)
            continue
        if status not in STATUS_EMOJI:
            unknown_status.append((md, status))
            continue
        comment_filled = is_comment_filled(text)
        new_name = compute_new_name(md, fm, comment_filled)
        if new_name and new_name != md.name:
            renames.append((md, md.parent / new_name))

    # collision check
    new_paths: dict[Path, Path] = {}
    collisions: list[tuple[Path, Path]] = []
    for old, new in renames:
        if new.exists() and new != old:
            collisions.append((old, new))
        if new in new_paths:
            collisions.append((old, new))
        new_paths[new] = old

    print(f"対象ディレクトリ: {ENTRIES_DIR.relative_to(ROOT)}")
    print(f"リネーム候補: {len(renames)} 件")
    if skipped_no_status:
        print(f"  status 不明でスキップ: {len(skipped_no_status)} 件")
    if unknown_status:
        print(f"  未知 status でスキップ: {len(unknown_status)} 件")
        for p, s in unknown_status[:5]:
            print(f"    - {p.relative_to(ROOT)} (status={s!r})")
    if collisions:
        print(f"  ⚠️ 衝突: {len(collisions)} 件 — リネーム中止")
        for old, new in collisions:
            print(f"    - {old.name} → {new.name} (既存 or 重複)")
        return 2

    print()
    for old, new in renames:
        print(f"  {old.relative_to(ROOT)}")
        print(f"    → {new.name}")

    if args.dry_run:
        print("\n--dry-run のため実際のリネームはしませんでした。")
        return 0

    print()
    for old, new in renames:
        old.rename(new)
    print(f"✅ {len(renames)} 件をリネームしました。")
    print("次に: python3 scripts/sync_entries_csv.py で entries.csv の path 列を同期してください。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
