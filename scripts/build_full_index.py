#!/usr/bin/env python3
"""
巻末・全件索引（総目次）HTML 生成器

entries.csv の全エントリ（archived/sample を除く）を、章（A〜J）ごと・ID 順に
すべて列挙した「全部載った索引」を作る。前付けのミニ索引を廃止し、こちらに集約する。

- 出力: drafts/front_section/9_full_index.html（前付け下絵と同じ _common.css を使う）
- 1 ページ 750×1061px に収まるよう、エントリ数で機械的にページ分割する
- 章がページ境界をまたぐときは見出しに「（つづき）」を付ける
- galley では巻末（BACK_SECTION_ORDER）として綴じる

Usage:
    python scripts/build_full_index.py
"""

from __future__ import annotations

import csv
import io
import sys
from html import escape
from pathlib import Path

if sys.platform == "win32" and hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", line_buffering=True)

ROOT = Path(__file__).resolve().parent.parent
CSV_PATH = ROOT / "ledgers" / "entries.csv"
CHAPTERS_PATH = ROOT / "ledgers" / "chapters.yaml"
OUT = ROOT / "drafts" / "front_section" / "9_full_index.html"

SKIP_STATUSES = {"archived", "sample"}
PER_PAGE = 84  # 1 ページあたりの行数目安（3 列 × 28 行）。章見出しもこの枠を消費する。


def load_labels() -> dict[str, str]:
    labels: dict[str, str] = {}
    if not CHAPTERS_PATH.exists():
        return labels
    cur = None
    import re
    for line in CHAPTERS_PATH.read_text(encoding="utf-8").splitlines():
        m = re.match(r"\s*-?\s*letter:\s*([A-J])\s*$", line)
        if m:
            cur = m.group(1)
            continue
        m = re.match(r"\s*label:\s*(.+?)\s*$", line)
        if m and cur:
            labels[cur] = m.group(1)
            cur = None
    return labels


def load_entries() -> list[dict]:
    with CSV_PATH.open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    out = []
    for r in rows:
        eid = (r.get("new_id") or "").strip()
        if not eid or "-" not in eid:
            continue
        if (r.get("status") or "").strip() in SKIP_STATUSES:
            continue
        out.append({"id": eid, "title": (r.get("title") or "").strip(),
                    "letter": eid.split("-", 1)[0]})
    return out


def build_items(entries: list[dict], labels: dict[str, str]) -> list[dict]:
    """[章見出し, エントリ, エントリ, …] の平坦リストにする。"""
    items: list[dict] = []
    seen: set[str] = set()
    for e in entries:
        if e["letter"] not in seen:
            seen.add(e["letter"])
            items.append({"kind": "chap", "letter": e["letter"],
                          "label": labels.get(e["letter"], "")})
        items.append({"kind": "entry", **e})
    return items


def paginate(items: list[dict]) -> list[list[dict]]:
    """PER_PAGE ごとに分割。章がまたいだら継続見出しを補う。"""
    pages: list[list[dict]] = []
    cur: list[dict] = []
    cur_chap: dict | None = None
    for it in items:
        if it["kind"] == "chap":
            cur_chap = it
        if len(cur) >= PER_PAGE:
            pages.append(cur)
            cur = []
            # ページ頭がエントリから始まるなら継続見出しを足す
            if it["kind"] == "entry" and cur_chap is not None:
                cur.append({"kind": "chap", "letter": cur_chap["letter"],
                            "label": cur_chap["label"], "cont": True})
        cur.append(it)
    if cur:
        pages.append(cur)
    return pages


PAGE_HEAD = """<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<title>巻末 - 全件索引（総目次）</title>
<link rel="stylesheet" href="../prototypes/mockups/design_philosophy_v2/base.css">
<link rel="stylesheet" href="_common.css">
<style>
  .idx-head { margin: 0 0 var(--sp-2) 0; }
  .idx-title { font-weight: 900; font-size: 30px; color: var(--ink); margin: 0; }
  .idx-sub { font-size: 12px; color: var(--ink-2); margin: 4px 0 0; line-height: 1.6; }
  .idx-flow { column-count: 3; column-gap: var(--sp-5); column-rule: 1px solid var(--rule); flex: 1; margin-top: var(--sp-3); }
  .idx-chap {
    column-span: all;
    display: flex; align-items: baseline; gap: 8px;
    border-bottom: 2px solid var(--ink-blue);
    margin: var(--sp-3) 0 var(--sp-2); padding-bottom: 3px;
  }
  .idx-chap:first-child { margin-top: 0; }
  .idx-chap .letter { font-family: var(--font-en); font-weight: 900; font-size: 17px; color: var(--ink-blue); }
  .idx-chap .label { font-weight: 700; font-size: 13px; color: var(--ink-blue-900); }
  .idx-chap .cont { font-size: 10px; color: var(--ink-3); }
  .idx-entry {
    display: flex; gap: 6px; font-size: 11px; line-height: 1.65;
    break-inside: avoid; color: var(--ink);
  }
  .idx-entry .eid { font-family: var(--font-en); color: var(--ink-blue); min-width: 40px; }
  .idx-entry .et { color: var(--ink); }
  .idx-pagenum { position: absolute; bottom: 28px; }
  .idx-pagenum.l { left: 56px; }
  .idx-pagenum.r { right: 56px; }
</style>
</head>
<body class="vbcd">

<nav class="reader-nav">
  <a href="index.html">← 前付け一覧</a>
  <div class="nav-center">
    <a class="nav-book" href="../book/index.html">📖 本として読む</a>
  </div>
  <span>巻末・索引</span>
</nav>

<div class="draft-stamp">BACK · FULL INDEX · DRAFT</div>

"""


def render_page(page_items: list[dict], page_no: int, is_first: bool, total: int) -> str:
    head = ""
    if is_first:
        head = (
            '<div class="idx-head">'
            '<h1 class="idx-title">索引 — 全 {n} 語</h1>'
            '<p class="idx-sub">本書に載っている語を章（A〜J）ごと・ID 順にすべて並べました。'
            '気になる語をここから探し、本編の見開きへ飛んでください。</p>'
            '</div>'
        ).format(n=total)
    body = ['<div class="idx-flow">']
    for it in page_items:
        if it["kind"] == "chap":
            cont = '<span class="cont">（つづき）</span>' if it.get("cont") else ''
            body.append(
                f'<div class="idx-chap"><span class="letter">{escape(it["letter"])}</span>'
                f'<span class="label">{escape(it["label"])}</span>{cont}</div>'
            )
        else:
            body.append(
                f'<div class="idx-entry"><span class="eid">{escape(it["id"])}</span>'
                f'<span class="et">{escape(it["title"])}</span></div>'
            )
    body.append('</div>')
    side = "l" if page_no % 2 == 0 else "r"
    return (
        '<section class="page">\n'
        + head + "\n"
        + "\n".join(body)
        + f'\n  <div class="page-num idx-pagenum {side}">索引 {page_no}</div>\n'
        + '</section>\n'
    )


def main() -> int:
    labels = load_labels()
    entries = load_entries()
    total = len(entries)
    items = build_items(entries, labels)
    pages = paginate(items)

    parts = [PAGE_HEAD]
    for i, pg in enumerate(pages, 1):
        parts.append(render_page(pg, i, is_first=(i == 1), total=total))
    parts.append("\n</body>\n</html>\n")
    OUT.write_text("".join(parts), encoding="utf-8")

    print(f"==> 全件索引: {OUT.relative_to(ROOT)}")
    print(f"   収録 {total} 語 / {len(pages)} ページ（PER_PAGE={PER_PAGE}）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
