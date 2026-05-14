#!/usr/bin/env python3
"""全エントリ「ざっと見る」用一覧 HTML 生成

出力: drafts/prototypes/preview/overview.html

各エントリを 1 行で表示し、章・ステータス・密度で絞り込み／ソートできるシングルページ。
本文セクション合計、TS 基準比、HTML preview と PDF preview へのリンクを並べる。

Usage:
    python scripts/overview_gen.py
"""
from __future__ import annotations

import json
import re
import sys
from collections import defaultdict
from html import escape
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / 'scripts'))
from density_audit import (
    SECTIONS, TS_BASELINE,
    layout_of, parse, section_chars, status_of, tagline_chars,
)

ENTRIES = REPO / 'content' / 'entries'
OUT = REPO / 'drafts' / 'prototypes' / 'preview' / 'overview.html'

CHAPTERS = {
    'A': 'はじめに・読み方',
    'B': 'サービス',
    'C': '人・会社',
    'D': 'モデル',
    'E': 'ベンチマーク',
    'F': 'ツール',
    'G': 'AI 用語（言語モデル系）',
    'H': '歴史・開発手法',
    'I': 'MCP',
    'J': '一般用語',
}


def collect():
    rows = []
    for f in sorted(ENTRIES.rglob('*.md')):
        text = f.read_text(encoding='utf-8')
        fm, body = parse(text)
        st = status_of(fm)
        layout = layout_of(fm)
        if st == 'archived':
            continue
        em = re.match(r'([A-J]-\d+)', f.stem)
        if not em:
            continue
        eid = em.group(1)

        # extract title from YAML
        tm = re.search(r'^title:\s*[\"\']?(.+?)[\"\']?\s*$', fm, re.M)
        title = tm.group(1).strip() if tm else eid

        # category
        cm = re.search(r'^category:\s*(\S+)', fm, re.M)
        category = cm.group(1).strip() if cm else ''

        # tag from filename
        tag_m = re.search(r'\[(.+?)\]', f.stem)
        tag = tag_m.group(1) if tag_m else ''

        # density
        if layout.startswith('front_'):
            total = -1
        else:
            counts = {s: section_chars(body, s) for s in SECTIONS}
            counts['tagline'] = tagline_chars(fm)
            total = sum(counts.values())

        rows.append({
            'id': eid,
            'letter': eid[0],
            'num': int(eid.split('-')[1]),
            'title': title,
            'status': st,
            'layout': layout,
            'category': category,
            'tag': tag,
            'total': total,
        })
    rows.sort(key=lambda r: (r['letter'], r['num']))
    return rows


def gen_html(rows):
    by_letter = defaultdict(list)
    for r in rows:
        by_letter[r['letter']].append(r)

    # Stats per chapter
    chapter_stats = {}
    for letter, items in by_letter.items():
        valid = [it for it in items if it['total'] >= 0]
        chapter_stats[letter] = {
            'count': len(items),
            'ready': sum(1 for it in items if it['status'] == 'ready'),
            'needs_review': sum(1 for it in items if it['status'] == 'needs_review'),
            'avg_density': sum(it['total'] for it in valid) // len(valid) if valid else 0,
        }

    # JSON for client filter
    data_json = json.dumps(rows, ensure_ascii=False)

    parts = []
    P = parts.append
    P('<!DOCTYPE html>')
    P('<html lang="ja"><head><meta charset="UTF-8">')
    P('<meta name="viewport" content="width=device-width, initial-scale=1">')
    P('<title>バイブコーディング図鑑 — 全エントリ一覧</title>')
    P('<style>')
    P('* { box-sizing: border-box; }')
    P('body { margin:0; font-family: "Hiragino Kaku Gothic ProN","Yu Gothic UI","Meiryo",sans-serif; color:#1a2333; background:#f3f6fb; }')
    P('header { background:#fff; border-bottom:1px solid #d8e0eb; padding:18px 24px; position:sticky; top:0; z-index:10; box-shadow:0 1px 0 rgba(0,0,0,0.03); }')
    P('h1 { font-size:20px; margin:0 0 4px; color:#0c2552; font-weight:900; }')
    P('.subtitle { font-size:12px; color:#6c7a91; }')
    P('.toolbar { display:flex; gap:8px; flex-wrap:wrap; margin-top:12px; align-items:center; }')
    P('.btn { background:#eef3fb; color:#27406b; border:1px solid #d4dded; padding:5px 11px; border-radius:6px; cursor:pointer; font-size:12px; font-weight:600; }')
    P('.btn:hover { background:#dde6f5; }')
    P('.btn.on { background:#27406b; color:#fff; border-color:#27406b; }')
    P('select { padding:5px 9px; border-radius:6px; border:1px solid #d4dded; font-size:12px; background:#fff; }')
    P('main { padding:18px 24px 60px; max-width:1400px; margin:0 auto; }')
    P('.chapter { margin:24px 0 12px; padding:6px 12px; background:#0c2552; color:#fff; border-radius:6px; font-weight:700; font-size:14px; display:flex; gap:16px; align-items:baseline; }')
    P('.chapter .stat { font-size:11px; opacity:0.7; font-weight:400; }')
    P('table { width:100%; border-collapse:collapse; background:#fff; border:1px solid #d8e0eb; border-radius:6px; overflow:hidden; }')
    P('th,td { padding:7px 10px; border-bottom:1px solid #eef0f4; font-size:13px; vertical-align:middle; }')
    P('th { background:#fafbfd; text-align:left; font-weight:700; color:#27406b; font-size:11px; letter-spacing:0.05em; }')
    P('tr:last-child td { border-bottom:none; }')
    P('tr:hover td { background:#fcfdff; }')
    P('.id { font-family:"SFMono-Regular","Consolas",monospace; font-size:12px; font-weight:700; color:#0c2552; width:50px; }')
    P('.title { font-weight:600; color:#1a2333; min-width:180px; }')
    P('.tag { font-size:10px; padding:2px 6px; border-radius:3px; font-weight:600; display:inline-block; }')
    P('.tag.sumi { background:#dbeefd; color:#0c2552; }')        # 済
    P('.tag.hito { background:#fff0d4; color:#7a4f00; }')         # 人書
    P('.tag.ai_sei { background:#e3e6ec; color:#3a4254; }')       # AI整
    P('.tag.ai_choku { background:#e9e9e9; color:#444; }')         # AI直
    P('.tag.tou { background:#f0d0d0; color:#7a1818; }')           # 凍')
    P('.status { font-size:10px; color:#6c7a91; }')
    P('.density { text-align:right; font-variant-numeric:tabular-nums; font-size:12px; }')
    P('.density.high { color:#9a2727; font-weight:700; }')
    P('.density.mid { color:#3a4254; }')
    P('.density.low { color:#1a6b1a; }')
    P('.density.na { color:#aab2c0; }')
    P('.links { white-space:nowrap; }')
    P('.links a { color:#27406b; text-decoration:none; font-size:11px; padding:2px 6px; border-radius:3px; background:#eef3fb; margin-right:3px; border:1px solid #d4dded; font-weight:600; }')
    P('.links a:hover { background:#27406b; color:#fff; }')
    P('.hidden { display:none !important; }')
    P('.legend { font-size:11px; color:#6c7a91; margin-top:6px; }')
    P('.legend code { background:#eef3fb; padding:1px 4px; border-radius:3px; font-size:10px; }')
    P('</style></head><body>')

    P('<header>')
    P('<h1>バイブコーディング図鑑 — 全エントリざっと見</h1>')
    total_count = len(rows)
    total_ready = sum(1 for r in rows if r['status'] == 'ready')
    total_nr = sum(1 for r in rows if r['status'] == 'needs_review')
    valid_dens = [r['total'] for r in rows if r['total'] >= 0]
    median_d = sorted(valid_dens)[len(valid_dens) // 2] if valid_dens else 0
    P(f'<div class="subtitle">全 {total_count} 件 / ready {total_ready} / needs_review {total_nr} / 本文密度中央値 {median_d} 字（TS 基準 {TS_BASELINE} 字 比 {median_d*100//TS_BASELINE}%）</div>')
    P('<div class="toolbar">')
    P('<span style="font-size:12px;font-weight:600;">章フィルタ:</span>')
    P('<button class="btn on" data-filter="all" onclick="filterChapter(this)">すべて</button>')
    for letter in sorted(by_letter):
        P(f'<button class="btn" data-filter="{letter}" onclick="filterChapter(this)">{letter} {CHAPTERS.get(letter,"")} ({len(by_letter[letter])})</button>')
    P('<span style="margin-left:24px;font-size:12px;font-weight:600;">状態:</span>')
    P('<button class="btn on" data-status="all" onclick="filterStatus(this)">すべて</button>')
    P('<button class="btn" data-status="ready" onclick="filterStatus(this)">ready</button>')
    P('<button class="btn" data-status="needs_review" onclick="filterStatus(this)">needs_review</button>')
    P('<button class="btn" data-status="hito" onclick="filterStatus(this)">[人書] 残</button>')
    P('</div>')
    P('<div class="legend">密度色 — <span class="density high">赤</span> TS基準 +30% 超 / <span class="density mid">通常</span> +10〜30% / <span class="density low">緑</span> TS±10% 内</div>')
    P('</header>')

    P('<main>')
    for letter in sorted(by_letter):
        items = by_letter[letter]
        stat = chapter_stats[letter]
        P(f'<div class="chapter" data-chapter="{letter}">'
          f'<span>{letter}章 — {CHAPTERS.get(letter, "")}</span>'
          f'<span class="stat">{stat["count"]} 件 / ready {stat["ready"]} / needs_review {stat["needs_review"]} / 平均密度 {stat["avg_density"]} 字</span>'
          f'</div>')
        P(f'<table data-chapter="{letter}">')
        P('<thead><tr><th>ID</th><th>タイトル</th><th>タグ</th><th>status</th><th style="text-align:right;">本文字数</th><th style="text-align:right;">TS比</th><th>preview</th></tr></thead>')
        P('<tbody>')
        for r in items:
            tag_cls_map = {'済': 'sumi', '人書': 'hito', 'AI整': 'ai_sei', 'AI直': 'ai_choku', '凍': 'tou'}
            tag_cls = tag_cls_map.get(r['tag'], 'ai_choku')
            tag_label = r['tag'] if r['tag'] else '—'

            if r['total'] < 0:
                density_class = 'na'
                density_html = '<span class="density na">— front</span>'
                ts_html = '—'
            else:
                ratio = r['total'] * 100 // TS_BASELINE
                if ratio > 130:
                    density_class = 'high'
                elif ratio <= 110:
                    density_class = 'low'
                else:
                    density_class = 'mid'
                density_html = f'<span class="density {density_class}">{r["total"]}</span>'
                ts_html = f'<span class="density {density_class}">{ratio}%</span>'

            hto = f'{r["id"]}.html'
            pdf = f'pdf/{r["id"]}.pdf'
            P(f'<tr data-status="{r["status"]}" data-tag="{r["tag"]}">'
              f'<td class="id">{r["id"]}</td>'
              f'<td class="title">{escape(r["title"])}</td>'
              f'<td><span class="tag {tag_cls}">{tag_label}</span></td>'
              f'<td class="status">{r["status"]}</td>'
              f'<td class="density">{density_html}</td>'
              f'<td class="density">{ts_html}</td>'
              f'<td class="links"><a href="{hto}" target="_blank">HTML</a><a href="{pdf}" target="_blank">PDF</a></td>'
              f'</tr>')
        P('</tbody></table>')
    P('</main>')

    P('<script>')
    P('let curChapter = "all"; let curStatus = "all";')
    P('function apply() {')
    P('  document.querySelectorAll(".chapter, table").forEach(el => {')
    P('    const ch = el.dataset.chapter;')
    P('    el.classList.toggle("hidden", curChapter !== "all" && ch !== curChapter);')
    P('  });')
    P('  document.querySelectorAll("tbody tr").forEach(tr => {')
    P('    const st = tr.dataset.status; const tag = tr.dataset.tag;')
    P('    let show = true;')
    P('    if (curStatus === "ready") show = (st === "ready");')
    P('    else if (curStatus === "needs_review") show = (st === "needs_review");')
    P('    else if (curStatus === "hito") show = (tag === "人書");')
    P('    tr.classList.toggle("hidden", !show);')
    P('  });')
    P('}')
    P('function filterChapter(btn) {')
    P('  document.querySelectorAll("[data-filter]").forEach(b => b.classList.remove("on"));')
    P('  btn.classList.add("on"); curChapter = btn.dataset.filter; apply();')
    P('}')
    P('function filterStatus(btn) {')
    P('  document.querySelectorAll("[data-status]").forEach(b => b.classList.remove("on"));')
    P('  btn.classList.add("on"); curStatus = btn.dataset.status; apply();')
    P('}')
    P('</script></body></html>')

    return '\n'.join(parts)


def main():
    rows = collect()
    html = gen_html(rows)
    OUT.write_text(html, encoding='utf-8')
    print(f'wrote {OUT} ({len(rows)} entries)', file=sys.stderr)


if __name__ == '__main__':
    main()
