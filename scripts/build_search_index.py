#!/usr/bin/env python3
"""エントリ検索 UI 用のインデックス JSON を生成する。

content/entries/**/*.md を全件スキャンし、YAML フロントマターと
本文先頭の tagline を抽出して drafts/search/index.json に書き出す。

検索 UI（drafts/search/index.html）はこの JSON を fetch して使う。
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ENTRIES_DIR = ROOT / "content" / "entries"
OUTPUT = ROOT / "drafts" / "search" / "index.json"
HTML_PATH = ROOT / "drafts" / "search" / "index.html"
PLACEHOLDER = "__SEARCH_DATA_JSON__"

YAML_RE = re.compile(r"^---\n(.+?)\n---\n", re.DOTALL)
TAGLINE_RE = re.compile(r"^##\s*tagline\s*\n+\s*(.+?)(?:\n\s*\n|$)", re.MULTILINE | re.DOTALL)


def parse_simple_yaml(yaml_text: str) -> dict:
    """シンプルな YAML パーサ（ライブラリ不要、本書のスキーマ向け）。"""
    result: dict = {}
    current_list_key: str | None = None
    current_list: list = []

    for raw in yaml_text.splitlines():
        line = raw.rstrip()
        if not line or line.lstrip().startswith("#"):
            continue

        if current_list_key is not None and line.startswith("  - "):
            current_list.append(line[4:].strip())
            continue

        if current_list_key is not None:
            result[current_list_key] = current_list
            current_list_key = None
            current_list = []

        if ":" in line and not line.startswith("  "):
            key, _, value = line.partition(":")
            key = key.strip()
            value = value.strip()
            if not value:
                current_list_key = key
                current_list = []
            else:
                if (value.startswith('"') and value.endswith('"')) or (
                    value.startswith("'") and value.endswith("'")
                ):
                    value = value[1:-1]
                result[key] = value

    if current_list_key is not None:
        result[current_list_key] = current_list

    return result


def extract_entry(path: Path) -> dict | None:
    try:
        text = path.read_text(encoding="utf-8")
    except Exception:
        return None

    match = YAML_RE.match(text)
    if not match:
        return None

    yaml_data = parse_simple_yaml(match.group(1))
    body = text[match.end():]

    tagline_match = TAGLINE_RE.search(body)
    tagline = tagline_match.group(1).strip() if tagline_match else ""
    tagline = re.sub(r"\s+", " ", tagline)[:200]

    entry_id = yaml_data.get("id", "")
    title = yaml_data.get("title", "")
    if not entry_id or not title:
        return None

    related = yaml_data.get("related_terms", [])
    if isinstance(related, str):
        related = [related]

    return {
        "id": entry_id,
        "title": title,
        "title_reading": yaml_data.get("title_reading", ""),
        "category": yaml_data.get("category", ""),
        "subtype": yaml_data.get("subtype", ""),
        "reader_level": str(yaml_data.get("reader_level", "")),
        "importance": yaml_data.get("importance", ""),
        "status": yaml_data.get("status", ""),
        "evaluation_date": yaml_data.get("evaluation_date", ""),
        "tagline": tagline,
        "related": related,
        "path": str(path.relative_to(ROOT)).replace("\\", "/"),
    }


def main() -> int:
    if not ENTRIES_DIR.exists():
        print(f"entries directory not found: {ENTRIES_DIR}", file=sys.stderr)
        return 1

    entries = []
    for path in sorted(ENTRIES_DIR.rglob("*.md")):
        entry = extract_entry(path)
        if entry:
            entries.append(entry)

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    data_obj = {
        "generated_at": Path(__file__).name,
        "count": len(entries),
        "entries": entries,
    }

    # 1) 通常の JSON ファイル（外部ツール用）。indent=2 で人間も読める形に
    OUTPUT.write_text(
        json.dumps(data_obj, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"wrote {len(entries)} entries to {OUTPUT.relative_to(ROOT)}")

    # 2) index.html の <script id="searchData"> 内に JSON を埋め込む。
    # これで file:// で開いても fetch を使わずに動く。
    # 何度ビルドしても冪等になるよう、常に script タグの中身を丸ごと置換する。
    if HTML_PATH.exists():
        html = HTML_PATH.read_text(encoding="utf-8")
        compact = json.dumps(data_obj, ensure_ascii=False, separators=(",", ":"))
        # <script> タグ内では </script> が現れるとブラウザがパースを止めるためエスケープ
        compact = compact.replace("</", "<\\/")

        pattern = re.compile(
            r'(<script id="searchData" type="application/json">)(.*?)(</script>)',
            re.DOTALL,
        )
        new_html, n = pattern.subn(
            lambda m: m.group(1) + compact + m.group(3),
            html,
            count=1,
        )
        if n:
            HTML_PATH.write_text(new_html, encoding="utf-8")
            print(f"injected data into {HTML_PATH.relative_to(ROOT)} (script tag content)")
        else:
            print(
                f"WARNING: searchData script tag not found in {HTML_PATH.relative_to(ROOT)}.",
                file=sys.stderr,
            )
    else:
        print(f"WARNING: {HTML_PATH.relative_to(ROOT)} not found", file=sys.stderr)

    return 0


if __name__ == "__main__":
    sys.exit(main())
