#!/usr/bin/env python3
"""
content/entries/**/*.md のファイル名末尾に「次のアクション」タグを 1 つ付ける／更新する。

タグは必ず 1 個だけ。誰の番か × 何の作業かが瞬時に読めるように、コロン区切りで
「主体:作業」を 2 文字で表す（B-1 方式、2026-05-04 採用）。

  [私:未]   skeleton / candidate
            → 著者の番。AI に初稿生成を依頼する
  [AI:直]   drafting + ☆ 違反あり
            → AI の番。構造崩れ・字数 100 字超などを直す
  [AI:整]   drafting + 警告のみ（または全パスなのに昇格漏れ）
            → AI の番。字数の丸めや LLM 整文など軽い手当て
  [私:書]   needs_review
            → 著者の番。「非エンジニアのつまずき」「私のコメント」を書く
  [済]      ready
            → 完成（著者欄まで埋まった）
  [凍]      archived / sample
            → 参照用、触らない

例:
  C-1_openai[ready][comment].md → C-1_openai[済].md
  C-5_xai[drafting][comment].md → C-5_xai[AI:整].md  （警告のみの場合）
  C-50_sam_altman[needs_review].md → C-50_sam_altman[私:書].md

使い方:
    python3 scripts/apply_status_markers.py --dry-run
    python3 scripts/apply_status_markers.py
    python3 scripts/apply_status_markers.py --filter content/entries/service

なぜ絵文字ではなくテキストか:
  Obsidian Mobile + Git の同期で、絵文字付きファイル名が安定しなかった
  （古いキャッシュが上書きで戻る事故が発生）。テキストの [...] 形式は
  クロスプラットフォームで安全。
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ENTRIES_DIR = ROOT / "content" / "entries"

# 兄弟スクリプトを import 可能に
sys.path.insert(0, str(Path(__file__).resolve().parent))
from validate_entry import (  # noqa: E402
    Report,
    parse_frontmatter,
    check_yaml,
    check_structure,
    check_author_fields_empty,
    check_char_counts,
    check_tone,
    check_sources_date,
)


# 直接決まる status → タグ
STATUS_TAG_DIRECT = {
    "skeleton":     "[私:未]",
    "candidate":    "[私:未]",
    "needs_review": "[私:書]",
    "ready":        "[済]",
    "archived":     "[凍]",
    "sample":       "[凍]",
}

# 全タグ（剥がし対象）
NEW_TAGS = ["[私:未]", "[AI:直]", "[AI:整]", "[私:書]", "[済]", "[凍]"]

# 旧テキストタグ（剥がし対象）
LEGACY_TEXT_TAGS = [
    "[skeleton]",
    "[drafting]",
    "[needs_review]",
    "[ready]",
    "[archived]",
    "[comment]",
]

# 旧絵文字マーカー（互換のため、付いていたら剥がす）
LEGACY_EMOJI = ["⬜", "✏️", "👁", "✅", "🗄", "💬"]

ALL_STRIP = NEW_TAGS + LEGACY_TEXT_TAGS + LEGACY_EMOJI


def strip_existing_marker(stem: str) -> str:
    """末尾の「既知タグの並び」を取り除く。"""
    while True:
        prev = stem
        s = stem.rstrip()
        for tag in ALL_STRIP:
            if s.endswith(tag):
                s = s[: -len(tag)]
                break
        if s == prev:
            break
        stem = s
    return stem.rstrip()


def silent_validate_for_drafting(path: Path, fm: dict, body: str) -> tuple[int, int]:
    """drafting 用に ☆ と ⚠ の件数だけ返す（出力なし）。

    validate_entry.py の main と同じ順で呼んで、件数を判定に使う。
    """
    r = Report(path)
    check_yaml(fm, r)
    check_structure(body, r)
    check_author_fields_empty(body, "drafting", r)
    check_char_counts(body, r)
    check_tone(body, r)
    check_sources_date(body, fm, r)
    return len(r.star_fails), len(r.warnings)


def compute_new_name(path: Path, text: str) -> str | None:
    fm, body = parse_frontmatter(text)
    status = str(fm.get("status", "")).strip()
    if not status:
        return None

    if status in STATUS_TAG_DIRECT:
        tag = STATUS_TAG_DIRECT[status]
    elif status == "drafting":
        stars, warns = silent_validate_for_drafting(path, fm, body)
        if stars > 0:
            tag = "[AI:直]"
        else:
            # 警告ありでも全パスでも、AI の手当て待ちなので [AI:整]
            # （全パスなら本来は validator が needs_review に昇格させているはず。
            #  もし漏れていても次回 validate でリカバリされる）
            tag = "[AI:整]"
    else:
        return None  # 未知 status

    base = strip_existing_marker(path.stem)
    return f"{base}{tag}.md"


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
        fm, _ = parse_frontmatter(text)
        status = str(fm.get("status", "")).strip()
        if not status:
            skipped_no_status.append(md)
            continue
        new_name = compute_new_name(md, text)
        if new_name is None:
            unknown_status.append((md, status))
            continue
        if new_name != md.name:
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
