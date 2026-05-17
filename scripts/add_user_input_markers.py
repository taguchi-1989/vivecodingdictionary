#!/usr/bin/env python3
"""
RepoEdit 用 user-input マーカー埋め込みスクリプト

content/entries/**/*.md の著者記入欄
  - ## 非エンジニアのつまずき  (key="stumble")
  - ## 私のコメント            (key="my_comment")
に対して、本文を `<!-- user-input:start key="..." -->` ... `<!-- user-input:end key="..." -->`
で包む。RepoEdit（Cloudflare Worker + PWA、Taguchi-1989/RepoEdit）が
スマホから著者欄だけを編集できるようにするための前処理。

特徴:
- べき等。すでにマーカーが入っているセクションはスキップ
- 著者欄以外には触らない。HTML コメント（節冒頭の guidelines 等）は外側に残す
- 字数・絵文字ラベル等の中身は変更しない

使い方:
  python3 scripts/add_user_input_markers.py              # 全エントリに適用
  python3 scripts/add_user_input_markers.py --dry-run    # 差分のみ表示
  python3 scripts/add_user_input_markers.py path/to.md   # 単発
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ENTRIES_DIR = ROOT / "content" / "entries"

# (見出し, RepoEdit ブロック key)
BLOCKS = [
    ("非エンジニアのつまずき", "stumble"),
    ("私のコメント", "my_comment"),
]


def wrap_section(lines: list[str], heading: str, key: str) -> tuple[list[str], bool]:
    """指定 H2 セクションの本文を user-input マーカーで包む。

    戻り値: (新しい lines, 変更があったか)
    """
    start_marker = f'<!-- user-input:start key="{key}" -->'
    end_marker = f'<!-- user-input:end key="{key}" -->'

    # 既に埋め込み済みなら何もしない
    if any(start_marker in ln for ln in lines):
        return lines, False

    heading_line = f"## {heading}"
    try:
        h_idx = next(i for i, ln in enumerate(lines) if ln.rstrip("\n") == heading_line)
    except StopIteration:
        return lines, False

    # 本文開始: 見出し直後から、blank と HTML コメントを読み飛ばした最初の非空行
    i = h_idx + 1
    n = len(lines)

    def is_boundary(ln: str) -> bool:
        s = ln.rstrip("\n")
        # 次の H2、AUTHOR コメント、装飾セパレータ、裏台帳セパレータ、ファイル末尾近く
        if s.startswith("## "):
            return True
        if s.startswith("<!-- AUTHOR:"):
            return True
        if s.startswith("<!-- ━"):
            return True
        return False

    # 本文最初の非コメント・非空行
    body_start = None
    while i < n and not is_boundary(lines[i]):
        s = lines[i].rstrip("\n")
        if s == "" or s.startswith("<!--"):
            i += 1
            continue
        body_start = i
        break

    if body_start is None:
        # 本文が空でも、空 bullets を包めるようにする: 直前の空行までさかのぼる
        # ヒューリスティック: 見出し直後の最初の空行の次から境界の前までを包む
        j = h_idx + 1
        # 先頭の HTML コメント＋空行はスキップ
        while j < n:
            s = lines[j].rstrip("\n")
            if s.startswith("<!--"):
                # コメント終端まで読み飛ばす
                while j < n and "-->" not in lines[j]:
                    j += 1
                j += 1
                continue
            if s == "":
                j += 1
                continue
            break
        body_start = j

    # 本文終端 = 次の境界の直前の最後の非空行の次
    j = body_start
    last_content = body_start - 1
    while j < n and not is_boundary(lines[j]):
        if lines[j].strip() != "":
            last_content = j
        j += 1

    if last_content < body_start:
        # 本文が空（純粋にプレースホルダだけ）。包む範囲がないので body_start に空行を作って包む
        new_lines = (
            lines[:body_start]
            + [start_marker + "\n", end_marker + "\n"]
            + lines[body_start:]
        )
        return new_lines, True

    body_end = last_content + 1  # exclusive
    new_lines = (
        lines[:body_start]
        + [start_marker + "\n"]
        + lines[body_start:body_end]
        + [end_marker + "\n"]
        + lines[body_end:]
    )
    return new_lines, True


def process_file(path: Path, dry_run: bool) -> bool:
    original = path.read_text(encoding="utf-8")
    lines = original.splitlines(keepends=True)
    if lines and not lines[-1].endswith("\n"):
        lines[-1] = lines[-1] + "\n"

    changed_any = False
    for heading, key in BLOCKS:
        lines, changed = wrap_section(lines, heading, key)
        changed_any = changed_any or changed

    if not changed_any:
        return False

    new_text = "".join(lines)
    if dry_run:
        print(f"[DRY] would update: {path.relative_to(ROOT)}")
        return True
    path.write_text(new_text, encoding="utf-8")
    print(f"updated: {path.relative_to(ROOT)}")
    return True


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("paths", nargs="*", help="個別ファイル（省略で全エントリ）")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    if args.paths:
        targets = [Path(p).resolve() for p in args.paths]
    else:
        targets = sorted(ENTRIES_DIR.rglob("*.md"))

    changed = 0
    for path in targets:
        if not path.exists():
            print(f"skip (missing): {path}", file=sys.stderr)
            continue
        if process_file(path, dry_run=args.dry_run):
            changed += 1

    print(f"\n{'would update' if args.dry_run else 'updated'}: {changed} / {len(targets)} files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
