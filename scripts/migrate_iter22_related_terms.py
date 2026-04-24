#!/usr/bin/env python3
"""
iter 22 (2026-04-25) マイグレーション:
既存エントリの `## 関連用語` ブロックを
`## 開発フローでの位置（必須）` ブロックの直後（= `## 非エンジニアのつまずき` の直前）に移動する。

- status: archived はスキップ（凍結素材）
- 既に移動済み（関連用語が開発フローより下にある）場合もスキップ
- 移動対象ブロック = 見出し行 + 直後の空行 + 本文 + 末尾空行、次の `## ` 直前まで

Usage:
    python scripts/migrate_iter22_related_terms.py
    python scripts/migrate_iter22_related_terms.py --dry-run
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

REL_HEAD = "## 関連用語"
FLOW_HEAD = "## 開発フローでの位置（必須）"
NEXT_HEAD = "## 非エンジニアのつまずき"


def is_archived(text: str) -> bool:
    m = re.search(r"^status:\s*(\S+)", text, re.MULTILINE)
    return bool(m and m.group(1).strip() == "archived")


def split_h2_blocks(body: str) -> list[tuple[str, str]]:
    """本文を (heading_line, block_text_including_trailing_blank) のリストに分ける。
    先頭（最初の ## より前）は ("", 前文) として返す。"""
    parts: list[tuple[str, str]] = []
    current_head = ""
    buf: list[str] = []
    for line in body.splitlines(keepends=True):
        if line.startswith("## "):
            parts.append((current_head, "".join(buf)))
            current_head = line.rstrip("\n")
            buf = [line]
        else:
            buf.append(line)
    parts.append((current_head, "".join(buf)))
    return parts


def migrate(text: str) -> tuple[str, str]:
    """戻り値: (新テキスト, ステータスメッセージ)"""
    # フロントマター分離
    m = re.match(r"^(---\r?\n.*?\r?\n---\r?\n)", text, re.DOTALL)
    if not m:
        return text, "skip: no frontmatter"
    fm = m.group(1)
    body = text[m.end():]

    blocks = split_h2_blocks(body)

    # 現在位置のインデックスを探す
    rel_idx = flow_idx = next_idx = -1
    for i, (head, _) in enumerate(blocks):
        if head == REL_HEAD:
            rel_idx = i
        elif head == FLOW_HEAD:
            flow_idx = i
        elif head == NEXT_HEAD:
            next_idx = i

    if rel_idx < 0:
        return text, "skip: no ## 関連用語 section"
    if flow_idx < 0:
        return text, "skip: no ## 開発フローでの位置（必須）section"

    # 既に正しい位置（開発フロー直後）にあるなら何もしない
    if rel_idx == flow_idx + 1:
        return text, "already migrated"

    # ブロックを取り出して再配置
    rel_block = blocks.pop(rel_idx)
    # rel_idx の pop で flow_idx が後ろにずれる可能性があるので再計算
    new_flow_idx = next(i for i, (h, _) in enumerate(blocks) if h == FLOW_HEAD)
    blocks.insert(new_flow_idx + 1, rel_block)

    new_body = "".join(block_text for _, block_text in blocks)
    return fm + new_body, "migrated"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    if not ENTRIES_DIR.is_dir():
        print(f"not found: {ENTRIES_DIR}", file=sys.stderr)
        return 2

    targets = sorted(ENTRIES_DIR.rglob("*.md"))
    migrated = skipped = failed = 0

    for p in targets:
        try:
            original = p.read_text(encoding="utf-8")
        except Exception as e:
            print(f"  ERR  {p}: {e}")
            failed += 1
            continue

        if is_archived(original):
            print(f"  --   {p.relative_to(ROOT)} (archived)")
            skipped += 1
            continue

        new_text, status = migrate(original)
        if new_text == original:
            print(f"  --   {p.relative_to(ROOT)} ({status})")
            skipped += 1
            continue

        if args.dry_run:
            print(f"  DRY  {p.relative_to(ROOT)} → {status}")
            migrated += 1
        else:
            p.write_text(new_text, encoding="utf-8")
            print(f"  OK   {p.relative_to(ROOT)} → {status}")
            migrated += 1

    print(f"\n=== migrated {migrated} / skipped {skipped} / failed {failed} ===")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
