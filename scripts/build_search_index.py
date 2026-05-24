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
# JSON を注入する対象 HTML（検索 UI と本のリーダー）
HTML_TARGETS = [
    ROOT / "drafts" / "search" / "index.html",
    ROOT / "drafts" / "book" / "index.html",
]
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

    # 本文：誌面に出る部分のみ（裏台帳メモ・ポンチ絵メモ・出典メモ・備考は除外）
    # 「<!-- ━━━━━━━━ 裏台帳メモ」より前を本文として扱う
    body_main_match = re.search(r"^(.*?)(?:<!--\s*━+\s*裏台帳メモ|$)", body, re.DOTALL)
    body_main = body_main_match.group(1) if body_main_match else body
    # HTML コメントを除去
    body_main = re.sub(r"<!--.*?-->", "", body_main, flags=re.DOTALL).strip()

    entry_id = yaml_data.get("id", "")
    title = yaml_data.get("title", "")
    if not entry_id or not title:
        return None

    # related は list を期待。文字列 1 個 → リスト化、それ以外（空リスト含む）はそのまま空
    related = yaml_data.get("related_terms", [])
    if isinstance(related, str):
        related = [related]
    elif not isinstance(related, list):
        related = []
    related = [str(r) for r in related if r]

    # 値があるはずだが YAML パーサがリストとして拾ってしまう場合があるため強制 str 化
    def s(key: str) -> str:
        v = yaml_data.get(key, "")
        if isinstance(v, list):
            return v[0] if v else ""
        return str(v) if v else ""

    return {
        "id": entry_id,
        "title": title,
        "title_reading": s("title_reading"),
        "category": s("category"),
        "subtype": s("subtype"),
        "reader_level": s("reader_level"),
        "importance": s("importance"),
        "status": s("status"),
        "evaluation_date": s("evaluation_date"),
        "tagline": tagline,
        "body": body_main,
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

    # 2) 各 HTML の <script id="searchData"> 内に JSON を埋め込む。
    # これで file:// で開いても fetch を使わずに動く。
    # 何度ビルドしても冪等になるよう、常に script タグの中身を丸ごと置換する。
    compact = json.dumps(data_obj, ensure_ascii=False, separators=(",", ":"))
    # <script> タグ内では </script> が現れるとブラウザがパースを止めるためエスケープ
    compact = compact.replace("</", "<\\/")

    pattern = re.compile(
        r'(<script id="searchData" type="application/json">)(.*?)(</script>)',
        re.DOTALL,
    )

    for html_path in HTML_TARGETS:
        if not html_path.exists():
            print(f"WARNING: {html_path.relative_to(ROOT)} not found", file=sys.stderr)
            continue
        html = html_path.read_text(encoding="utf-8")
        new_html, n = pattern.subn(
            lambda m: m.group(1) + compact + m.group(3),
            html,
            count=1,
        )
        if n:
            html_path.write_text(new_html, encoding="utf-8")
            print(f"injected data into {html_path.relative_to(ROOT)}")
        else:
            print(
                f"WARNING: searchData script tag not found in {html_path.relative_to(ROOT)}.",
                file=sys.stderr,
            )

    return 0


if __name__ == "__main__":
    sys.exit(main())
