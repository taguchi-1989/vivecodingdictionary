#!/usr/bin/env python3
"""
A-5 読者レベル凡例（drafts/front_section/4_legend_all.html）の「読者レベル」段に、
preview_gen.medal_svg が生成する難易度勲章を差し込む（再現可能・冪等）。

Usage:
    python scripts/inject_legend_medals.py
"""
from __future__ import annotations

import io
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from preview_gen import medal_svg, exp_bars_svg  # noqa: E402  （import 時に stdout を UTF-8 化済み）

ROOT = Path(__file__).resolve().parent.parent
TARGET = ROOT / "drafts" / "front_section" / "4_legend_all.html"

LEVELS = [
    (1, "入門", "ChatGPT / Hallucination"),
    (2, "一般", "Context / MCP / Cursor"),
    (3, "中級", "Tool Use / Hook / Slash Command"),
    (4, "応用", "TypeScript / Lint"),
    (5, "上級", "量子化 / LoRA / Tensor コア"),
    (6, "専門", "gpt-oss / ノイマン型 / Anthropic 創業史"),
]

CSS_BLOCK = """
  /* 読者レベル凡例＝勲章／体験区分＝関与バー（inject_legend_medals.py が差し込み） */
  .level-row { grid-template-columns: 46px 78px 1fr !important; }
  .lvl-badge { display: flex; justify-content: center; align-items: center; }
  .lvl-badge .level-medal { display: block; }
  .exp-row .mark svg { display: block; margin: 0 auto; }
"""

EXP_KEYS = ["hands_on", "partial", "research_only"]


def build_ladder() -> str:
    rows = []
    for lv, name, ex in LEVELS:
        medal = medal_svg(lv, w=36, h=39, cls="level-medal")
        rows.append(
            f'      <div class="level-row"><div class="lvl-badge">{medal}</div>'
            f'<div class="name">{name}</div><div class="ex">{ex}</div></div>'
        )
    return '<div class="level-ladder">\n' + "\n".join(rows) + "\n    </div>"


def main() -> int:
    html = TARGET.read_text(encoding="utf-8")

    # CSS（未挿入なら追加）
    if ".lvl-badge" not in html:
        html = html.replace("</style>", CSS_BLOCK + "</style>", 1)

    # level-ladder ブロックを丸ごと差し替え（評価日 lg-h の直前まで）
    pattern = re.compile(r'<div class="level-ladder">.*?</div>\s*(<div class="lg-h">評価日)', re.DOTALL)
    new = build_ladder() + "\n\n    " + r"\1"
    html, n = pattern.subn(new, html)
    if n == 0:
        print("level-ladder ブロックが見つかりません（既に差し替え済み？構造変更？）", file=sys.stderr)
        return 1

    # 体験区分の mark（●◐○）を関与バーに差し替え（enum で対応付け、冪等）
    m_total = 0
    for key in EXP_KEYS:
        bars = exp_bars_svg(key, w=30, h=27)
        # mark セル内は </div> を含まない（svg は </svg> のみ）ので、tempered で行内に限定
        ep = re.compile(r'(<div class="mark">)(?:(?!</div>).)*(</div>\s*<div class="enum">' + re.escape(key) + r'</div>)', re.DOTALL)
        html, m = ep.subn(lambda mo, b=bars: mo.group(1) + b + mo.group(2), html)
        m_total += m

    TARGET.write_text(html, encoding="utf-8")
    print(f"==> 凡例を更新: 勲章 {n} ブロック / 体験バー {m_total} 件: {TARGET.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
