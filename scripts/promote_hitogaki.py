"""[人書] エントリのうち、著者欄が記入済みかつ字数が極端に超過していない
ものを ready に昇格し、ファイル名タグを [人書] → [済] にリネームする。

判定:
  - 著者欄が未記入（つまずき or 私のコメント 4 ラベルどれか空） → 残す
  - 字数が「あまりにも超過」しているもの → 残す
      私のコメント: 1 行 > 67 字（上限 45 の 1.5 倍）
      非エンジニアのつまずき: 1 項目 > 90 字（上限 60 の 1.5 倍）
  - それ以外 → ready 昇格 + [人書]→[済] リネーム

CSV(ledgers/entries.csv) の status と path 列も同期。
"""

from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from validate_entry import (  # noqa: E402
    is_author_fields_filled,
    parse_frontmatter,
)

MY_COMMENT_HARD = 67   # 45 * 1.5
TSUMAZUKI_HARD = 90    # 60 * 1.5


def has_severe_overflow(body: str) -> tuple[bool, list[str]]:
    """著者欄に「あまりにも字数オーバー」な行があるかを返す。"""
    LABEL_RE = re.compile(r"^([^\w]*[^\s:：]+)\s*[:：]\s*(.*)$")
    reasons: list[str] = []

    m = re.search(r"## 私のコメント\n(.*?)(?=\n## |\n<!--)", body, re.DOTALL)
    if m:
        for line in m.group(1).split("\n"):
            line = line.strip()
            if not line.startswith("- "):
                continue
            text = line[2:].strip()
            mm = LABEL_RE.match(text)
            content = mm.group(2).strip() if mm else text
            if len(content) > MY_COMMENT_HARD:
                head = mm.group(1) if mm else "?"
                reasons.append(f"私のコメント {head}={len(content)}字")

    m = re.search(r"## 非エンジニアのつまずき\n(.*?)(?=\n## |\n<!--)", body, re.DOTALL)
    if m:
        for line in m.group(1).split("\n"):
            line = line.strip()
            if not line.startswith("- "):
                continue
            content = line[2:].strip()
            if len(content) > TSUMAZUKI_HARD:
                reasons.append(f"つまずき={len(content)}字")

    return bool(reasons), reasons


def main() -> int:
    csv_path = ROOT / "ledgers" / "entries.csv"
    rows = list(csv.reader(csv_path.open(encoding="utf-8")))
    header, data = rows[0], rows[1:]

    promoted: list[tuple[str, str, str]] = []   # (id, old_path, new_path)
    kept_empty: list[tuple[str, str]] = []      # (id, title)
    kept_overflow: list[tuple[str, str, list[str]]] = []

    for row in data:
        new_id, _legacy, title, _cat, _sub, status, _notes, path_str = row
        if "[人書]" not in path_str:
            continue
        p = ROOT / path_str
        if not p.exists():
            print(f"  missing file: {path_str}", file=sys.stderr)
            continue
        text = p.read_text(encoding="utf-8")
        fm, body = parse_frontmatter(text)

        filled = is_author_fields_filled(body)
        severe, reasons = has_severe_overflow(body)

        if not filled:
            kept_empty.append((new_id, title))
            continue
        if severe:
            kept_overflow.append((new_id, title, reasons))
            continue

        # 昇格対象
        new_path_str = path_str.replace("[人書]", "[済]")
        new_p = ROOT / new_path_str
        # YAML status を ready に書き換え
        new_text = re.sub(
            r"^status:\s*(needs_review|drafting|ready)\s*$",
            "status: ready",
            text,
            count=1,
            flags=re.MULTILINE,
        )
        # ファイル書き換え→リネーム
        p.write_text(new_text, encoding="utf-8")
        if new_p != p:
            p.rename(new_p)
        # CSV 行も更新
        row[5] = "ready"
        row[7] = new_path_str
        promoted.append((new_id, path_str, new_path_str))

    # CSV 書き戻し
    with csv_path.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(header)
        w.writerows(data)

    print(f"\n=== 昇格 [人書]→[済] / ready: {len(promoted)} 件 ===")
    for i, _o, n in promoted[:10]:
        print(f"  {i}: {n}")
    if len(promoted) > 10:
        print(f"  ... 他 {len(promoted) - 10} 件")

    print(f"\n=== 残置（著者欄 未記入）: {len(kept_empty)} 件 ===")
    for i, t in kept_empty[:20]:
        print(f"  {i} {t}")
    if len(kept_empty) > 20:
        print(f"  ... 他 {len(kept_empty) - 20} 件")

    print(f"\n=== 残置（字数大幅超過）: {len(kept_overflow)} 件 ===")
    for i, t, rs in kept_overflow:
        print(f"  {i} {t} — {', '.join(rs)}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
