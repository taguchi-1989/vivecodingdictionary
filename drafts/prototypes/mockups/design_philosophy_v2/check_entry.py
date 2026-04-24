#!/usr/bin/env python3
"""
check_entry.py — エントリ markdown を writing_spec.md 準拠で検証する

Usage:
    python check_entry.py path/to/entry.md [path/to/entry2.md ...]
    python check_entry.py --dir content/entries/

仕様の真実は writing_spec.md §5 にある閾値。本スクリプトはその機械実装。
"""

from __future__ import annotations

import argparse
import io
import re
import sys
from pathlib import Path
from typing import Iterable

# Windows の日本語出力文字化けを回避
if sys.platform == "win32" and hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", line_buffering=True)
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", line_buffering=True)

# ---- 仕様（writing_spec.md §5 と同期させること） ----

SECTION_RULES: dict[str, dict] = {
    # 左ページ
    "tagline":               {"min": 25, "max": 45},
    "何をしてくれるか":       {"min": 60, "max": 200, "desumasu_required": True},
    "どこで出会うか":         {"min": 60, "max": 200, "desumasu_required": True},
    # 右ページ 6 視点
    "1. 役割":               {"min": 15, "max": 40},
    "2. うれしさ":           {"min": 15, "max": 40},
    "3. 注意点":             {"min": 15, "max": 40},
    "4. どこで役立つか":     {"min": 15, "max": 40},
    "5. はじめに":           {"min": 15, "max": 40},
    "6. 深掘り先":           {"min": 15, "max": 50},
}

REQUIRED_SECTIONS = [
    "tagline",
    "何をしてくれるか",
    "どこで出会うか",
    "関連用語",
    "この用語の見どころ",
    "開発フローでの位置",
    "非エンジニアのつまずき",
    "私のコメント",
]

YAML_REQUIRED = ["id", "title", "category", "figure_type", "page_layout", "evaluation_date"]

RELATED_TERMS_MIN = 3
RELATED_TERMS_MAX = 5

# 旧節名（互換警告用）: 新節名 → 旧節名
LEGACY_SECTION_MAP = {
    "どこで出会うか":     "バイブコーディングでの位置づけ",
    "4. どこで役立つか": "4. どこで効くか",
    "5. はじめに":       "5. 最初に理解する範囲",
}

# v2 で削除された節（残っていたら警告）
REMOVED_SECTIONS = ["ひとことで"]


# ---- パーサ ----

def parse_frontmatter(text: str) -> tuple[dict, str]:
    """簡易 YAML フロントマターパーサ（yaml 非依存、浅いキー:値 と リストのみ対応）"""
    m = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n", text, re.DOTALL)
    if not m:
        return {}, text
    raw = m.group(1)
    body = text[m.end():]
    fm: dict = {}
    current_list_key: str | None = None
    for line in raw.splitlines():
        # コメント行スキップ
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            current_list_key = None
            continue
        # リスト項目 "- foo"
        if stripped.startswith("- ") and current_list_key:
            fm[current_list_key].append(stripped[2:].strip())
            continue
        # key: value
        m2 = re.match(r"^(\S[^:]*?):\s*(.*)$", line)
        if m2:
            key = m2.group(1).strip()
            val = m2.group(2).strip()
            if val == "" or val == "[]":
                fm[key] = []
                current_list_key = key
            else:
                fm[key] = val.strip('"').strip("'")
                current_list_key = None
    return fm, body


def normalize_heading(h: str) -> str:
    """見出しから (必須) などの注記を除去して正規化"""
    return re.sub(r"\s*[（(][^）)]*[）)]\s*$", "", h).strip()


def extract_sections(body: str) -> dict[str, str]:
    """'## ' と '### ' 見出しと内容を dict に（正規化済みキー）"""
    sections: dict[str, str] = {}
    current: str | None = None
    buf: list[str] = []
    for line in body.splitlines():
        m2 = re.match(r"^## (.+?)\s*$", line)
        m3 = re.match(r"^### (.+?)\s*$", line)
        if m2 or m3:
            if current is not None:
                sections[current] = "\n".join(buf).strip()
            current = normalize_heading((m2 or m3).group(1).strip())
            buf = []
        else:
            buf.append(line)
    if current is not None:
        sections[current] = "\n".join(buf).strip()
    return sections


def strip_comments_and_whitespace(text: str) -> str:
    """HTML コメントと空白を除去して文字数カウント用に整形"""
    text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
    text = re.sub(r"\s+", "", text)
    return text


def count_chars(text: str) -> int:
    return len(strip_comments_and_whitespace(text))


def has_desumasu(text: str) -> bool:
    cleaned = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
    return bool(re.search(r"(です|ます|ました|でした|ません)(?=[。\n、]|$)", cleaned))


def tagline_echoes_title(tagline: str, title: str) -> bool:
    tag_clean = strip_comments_and_whitespace(tagline)
    if not title or not tag_clean:
        return False
    return tag_clean.startswith(title + "は") or tag_clean.startswith(title + "、")


def count_related_terms(section_text: str) -> int:
    """"- 用語A — 隣接メモ" 形式の行数をカウント"""
    lines = [l for l in section_text.splitlines() if l.strip().startswith("- ")]
    return len(lines)


# ---- 検証本体 ----

def validate_file(path: Path) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    try:
        text = path.read_text(encoding="utf-8")
    except Exception as e:
        return [f"読み込み失敗: {e}"], []

    fm, body = parse_frontmatter(text)

    # archived は v2 仕様の検証対象外（参照素材として凍結）
    if fm.get("status") == "archived":
        return [], []

    # YAML 必須フィールド
    for k in YAML_REQUIRED:
        if k not in fm or fm[k] in ("", [], None):
            errors.append(f"YAML: 必須キー '{k}' が未記入")

    # evaluation_date 書式
    if fm.get("evaluation_date") and not re.match(r"^\d{4}-\d{2}-\d{2}$", fm["evaluation_date"]):
        warnings.append(f"YAML evaluation_date 書式: '{fm['evaluation_date']}' (YYYY-MM-DD 想定)")

    sections = extract_sections(body)

    # 必須節チェック
    for s in REQUIRED_SECTIONS:
        if s not in sections:
            # 旧節名の可能性を探る
            legacy = LEGACY_SECTION_MAP.get(s)
            if legacy and legacy in sections:
                warnings.append(f"旧節名検出: '{legacy}' → '{s}' へのリネームを推奨（iter 16 仕様）")
            else:
                errors.append(f"必須節不在: ## {s}")

    # 削除された節の検出
    for s in REMOVED_SECTIONS:
        if s in sections:
            warnings.append(f"v2 で削除された節が残っている: ## {s}（tagline に統合済みのため削除推奨）")

    # 文字数 + 文体
    title = fm.get("title", "")
    for s, rule in SECTION_RULES.items():
        if s not in sections:
            continue
        c = count_chars(sections[s])
        mn, mx = rule.get("min"), rule.get("max")
        if mn is not None and c < mn:
            warnings.append(f"'{s}': {c} 字（< {mn} 下限）")
        elif mx is not None and c > mx:
            warnings.append(f"'{s}': {c} 字（> {mx} 上限）")
        if rule.get("desumasu_required") and not has_desumasu(sections[s]):
            warnings.append(f"'{s}': です・ます調の語尾が見当たらない")

    # tagline が title の単純な言い換えになっていないか
    if "tagline" in sections and title:
        if tagline_echoes_title(sections["tagline"], title):
            warnings.append(f"tagline が title の言い換えに見える（'{title} は…' で始まる）")

    # 関連用語の数
    if "関連用語" in sections:
        n = count_related_terms(sections["関連用語"])
        if n < RELATED_TERMS_MIN:
            warnings.append(f"関連用語: {n} 個（< {RELATED_TERMS_MIN} 下限）")
        elif n > RELATED_TERMS_MAX:
            warnings.append(f"関連用語: {n} 個（> {RELATED_TERMS_MAX} 上限）")

    return errors, warnings


def collect_paths(args: list[str], dir_path: str | None) -> list[Path]:
    paths: list[Path] = []
    if dir_path:
        d = Path(dir_path)
        if not d.is_dir():
            print(f"ディレクトリ不在: {dir_path}", file=sys.stderr)
            sys.exit(2)
        paths.extend(sorted(d.rglob("*.md")))
    for a in args:
        p = Path(a)
        if not p.exists():
            print(f"ファイル不在: {a}", file=sys.stderr)
            continue
        if p.is_dir():
            paths.extend(sorted(p.rglob("*.md")))
        else:
            paths.append(p)
    return paths


def main() -> int:
    ap = argparse.ArgumentParser(description="エントリ markdown を writing_spec v2 で検証")
    ap.add_argument("files", nargs="*", help="検証対象の .md ファイル（複数可）")
    ap.add_argument("--dir", help="ディレクトリ配下の *.md を再帰的に検証")
    ap.add_argument("--quiet", action="store_true", help="エラー・警告が無いファイルは出力しない")
    args = ap.parse_args()

    paths = collect_paths(args.files, args.dir)
    if not paths:
        ap.print_help()
        return 2

    total_errors = 0
    total_warnings = 0
    files_with_issues = 0

    for p in paths:
        errors, warnings = validate_file(p)
        if not errors and not warnings:
            if not args.quiet:
                print(f"  OK  {p}")
            continue
        files_with_issues += 1
        total_errors += len(errors)
        total_warnings += len(warnings)
        print(f"\n--- {p} ---")
        for e in errors:
            print(f"  E  {e}")
        for w in warnings:
            print(f"  W  {w}")

    print(f"\n=== {len(paths)} ファイル / "
          f"問題 {files_with_issues} 件 / エラー {total_errors} / 警告 {total_warnings} ===")
    return 1 if total_errors > 0 else 0


if __name__ == "__main__":
    sys.exit(main())
