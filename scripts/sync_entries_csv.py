#!/usr/bin/env python3
"""
entries.csv の path 列を content/entries/**/*.md の実ファイル位置と同期する。

- md ファイルのフロントマター `id:` を読み、entries.csv の new_id とマッチング
- マッチした行の `path` 列をリポジトリルートからの相対パスで埋める
- 対応する md ファイルが無い行は path 空欄のまま（= 候補、未執筆）
- `path` 列が無ければ追加し、既存の列順を崩さない

Usage:
    python scripts/sync_entries_csv.py
    python scripts/sync_entries_csv.py --dry-run
"""

from __future__ import annotations

import argparse
import csv
import io
import re
import sys
from pathlib import Path

if sys.platform == "win32" and hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", line_buffering=True)

ROOT = Path(__file__).resolve().parent.parent
CSV_PATH = ROOT / "ledgers" / "entries.csv"
ENTRIES_DIR = ROOT / "content" / "entries"


def parse_id_from_md(path: Path) -> str | None:
    try:
        text = path.read_text(encoding="utf-8")
    except Exception:
        return None
    m = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n", text, re.DOTALL)
    if not m:
        return None
    for line in m.group(1).splitlines():
        mm = re.match(r"^id:\s*(\S+)\s*$", line)
        if mm:
            return mm.group(1).strip().strip('"').strip("'")
    return None


def scan_md_paths() -> dict[str, str]:
    """md ファイルを走査して {id: relative_path}"""
    result: dict[str, str] = {}
    if not ENTRIES_DIR.is_dir():
        return result
    for p in sorted(ENTRIES_DIR.rglob("*.md")):
        entry_id = parse_id_from_md(p)
        if not entry_id:
            continue
        rel = p.relative_to(ROOT).as_posix()
        if entry_id in result:
            print(f"WARN: id '{entry_id}' is duplicated: {result[entry_id]} と {rel}", file=sys.stderr)
            continue
        result[entry_id] = rel
    return result


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    if not CSV_PATH.exists():
        print(f"not found: {CSV_PATH}", file=sys.stderr)
        return 2

    id_to_path = scan_md_paths()
    print(f"md ファイル {len(id_to_path)} 件から id を取得")

    with CSV_PATH.open(encoding="utf-8", newline="") as f:
        reader = csv.reader(f)
        rows = list(reader)
    if not rows:
        print("CSV 空", file=sys.stderr)
        return 2
    header = rows[0]
    body = rows[1:]

    if "path" not in header:
        header.append("path")
        # 既存行に空 path を詰める
        for r in body:
            while len(r) < len(header):
                r.append("")
        print("path 列を追加")

    path_idx = header.index("path")
    id_idx = header.index("new_id")

    updated = unchanged = missing = 0
    for r in body:
        while len(r) < len(header):
            r.append("")
        entry_id = r[id_idx].strip()
        if not entry_id:
            continue
        new_path = id_to_path.get(entry_id, "")
        old_path = r[path_idx].strip()
        if new_path and new_path != old_path:
            r[path_idx] = new_path
            updated += 1
        elif not new_path and old_path:
            # 既存の path が md 実体なし -> クリア（archived 等でファイル消失ケース）
            r[path_idx] = ""
            missing += 1
        else:
            unchanged += 1

    if args.dry_run:
        print(f"[dry-run] updated {updated} / missing {missing} / unchanged {unchanged}")
        return 0

    # 書き戻し（lineterminator="\n" で LF 固定）
    with CSV_PATH.open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, lineterminator="\n")
        writer.writerow(header)
        writer.writerows(body)

    print(f"updated {updated} / cleared {missing} / unchanged {unchanged}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
