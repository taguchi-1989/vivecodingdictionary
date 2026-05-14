#!/usr/bin/env python3
"""字数バリエーション監査スクリプト

TypeScript 見本（typescript_spread.html）の本文セクション合計を基準値として、
全エントリの本文セクション字数を集計し、圧縮候補・スカスカ候補をリストアップする。

出力: ledgers/density_audit.md（既存なら上書き）

Usage:
    python scripts/density_audit.py
"""
from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ENTRIES = ROOT / 'content' / 'entries'
OUT = ROOT / 'ledgers' / 'density_audit.md'

SECTIONS = [
    'tagline', '何をしてくれるか', 'どこで出会うか', '会話での使い方例',
    '1. 役割', '2. うれしさ', '3. 注意点',
    '4. どこで役立つか', '5. はじめに', '6. 深掘り先',
]

# TypeScript baseline (typescript_spread.html から抽出した本文セクション合計)
TS = dict(tagline=35, nani=60, doko=72, kaiwa=30, six=131)
TS_BASELINE = sum(TS.values())  # 328


def parse(text):
    if text.startswith('---'):
        end = text.find('---', 4)
        fm = text[4:end]
        body = text[end + 3:]
    else:
        fm, body = '', text
    if '裏台帳メモ' in body:
        body = body.split('裏台帳メモ')[0]
    body = re.sub(r'<!--.*?-->', '', body, flags=re.S)
    return fm, body


def section_chars(body, name):
    # H2 (## name) or H3 (### name) — H3 stops at next H2 or H3 of same or higher level.
    pat = re.compile(rf'^#{{2,3}}\s+{re.escape(name)}\s*$(.+?)(^#{{2,3}}\s|\Z)', re.S | re.M)
    m = pat.search(body)
    if not m:
        return 0
    chunk = m.group(1)
    chunk = re.sub(r'```[^`]*```', '', chunk, flags=re.S)
    chunk = re.sub(r'^[-*]\s*', '', chunk, flags=re.M)
    chunk = re.sub(r'^#+\s*', '', chunk, flags=re.M)
    chunk = re.sub(r'\s+', '', chunk)
    return len(chunk)


def tagline_chars(fm):
    m = re.search(r'^tagline:\s*[\"\']?(.+?)[\"\']?$', fm, re.M)
    if not m:
        return 0
    return len(re.sub(r'\s', '', m.group(1)))


def layout_of(fm):
    m = re.search(r'^(?:page_)?layout:\s*(\S+)', fm, re.M)
    return m.group(1) if m else 'spread_v1'


def status_of(fm):
    m = re.search(r'^status:\s*(\S+)', fm, re.M)
    return m.group(1) if m else '?'


def main():
    rows = []
    for f in sorted(ENTRIES.rglob('*.md')):
        text = f.read_text(encoding='utf-8')
        fm, body = parse(text)
        st = status_of(fm)
        if st in ('archived', 'sample'):
            continue
        if layout_of(fm).startswith('front_'):
            continue
        em = re.match(r'([A-J]-\d+)', f.stem)
        if not em:
            continue
        eid = em.group(1)
        counts = {s: section_chars(body, s) for s in SECTIONS}
        counts['tagline'] = tagline_chars(fm)
        total = sum(counts.values())
        rows.append((eid, st, total, counts))

    rows.sort(key=lambda r: -r[2])
    totals = [r[2] for r in rows]

    lines = []
    P = lines.append
    P('# 字数バリエーション監査')
    P('')
    P(f'**TypeScript 見本基準値**: 約 **{TS_BASELINE} 字**')
    P(f'内訳 — tagline {TS["tagline"]} / 何を {TS["nani"]} / どこで {TS["doko"]} / 会話 {TS["kaiwa"]} / 6視点合計 {TS["six"]}')
    P('')
    P('本一覧の `total` は同じ 10 セクションの可視文字数合計です。裏台帳・著者欄・section heading は除外。前付け（layout: front_*）と archived/sample も集計外。')
    P('')
    P(f'**対象**: {len(rows)} 件')
    P(f'**max**: {max(totals)} 字 / **min**: {min(totals)} 字 / **中央値**: {sorted(totals)[len(totals)//2]} 字 / **平均**: {sum(totals)//len(totals)} 字')
    P('')

    over = [r for r in rows if r[2] > TS_BASELINE * 1.1]
    near = [r for r in rows if TS_BASELINE * 0.9 <= r[2] <= TS_BASELINE * 1.1]
    under_med = [r for r in rows if TS_BASELINE * 0.7 <= r[2] < TS_BASELINE * 0.9]
    sparse = [r for r in rows if r[2] < TS_BASELINE * 0.7]

    P(f'**TS基準 +10%超 ({int(TS_BASELINE*1.1)}字超)**: {len(over)} 件 ← 圧縮候補')
    P(f'**TS基準 ±10% 内 ({int(TS_BASELINE*0.9)}〜{int(TS_BASELINE*1.1)}字)**: {len(near)} 件')
    P(f'**TS基準 70〜90% ({int(TS_BASELINE*0.7)}〜{int(TS_BASELINE*0.9)-1}字)**: {len(under_med)} 件')
    P(f'**TS基準 70% 未満 ({int(TS_BASELINE*0.7)-1}字以下)**: {len(sparse)} 件 ← 補強検討')
    P('')

    # Top 30
    P('## 密度トップ 30')
    P('')
    P('| rank | ID | status | total | vs TS | 何を | どこで | 会話 | 6視点計 | preview |')
    P('|------|----|--------|------:|------:|-----:|-------:|-----:|--------:|---------|')
    for i, (eid, st, total, c) in enumerate(rows[:30], 1):
        six = sum(c[s] for s in ['1. 役割', '2. うれしさ', '3. 注意点', '4. どこで役立つか', '5. はじめに', '6. 深掘り先'])
        diff = total - TS_BASELINE
        sign = '+' if diff >= 0 else ''
        href = f'../drafts/prototypes/preview/{eid}.html'
        pdf = f'../drafts/prototypes/preview/pdf/{eid}.pdf'
        P(f'| {i} | **{eid}** | {st} | {total} | {sign}{diff} | {c["何をしてくれるか"]} | {c["どこで出会うか"]} | {c["会話での使い方例"]} | {six} | [HTML]({href}) / [PDF]({pdf}) |')
    P('')

    # Bottom 20
    P('## 密度ボトム 20')
    P('')
    P('| rank | ID | status | total | vs TS | preview |')
    P('|------|----|--------|------:|------:|---------|')
    for i, (eid, st, total, c) in enumerate(rows[-20:], 1):
        diff = total - TS_BASELINE
        sign = '+' if diff >= 0 else ''
        href = f'../drafts/prototypes/preview/{eid}.html'
        pdf = f'../drafts/prototypes/preview/pdf/{eid}.pdf'
        P(f'| {i} | {eid} | {st} | {total} | {sign}{diff} | [HTML]({href}) / [PDF]({pdf}) |')
    P('')

    # Per-chapter
    P('## 章ごとの平均密度')
    P('')
    by_letter = defaultdict(list)
    for eid, st, total, c in rows:
        by_letter[eid[0]].append(total)
    P('| 章 | 件数 | 平均 | 中央値 | max | min | TS比 |')
    P('|----|-----:|-----:|------:|----:|----:|-----:|')
    for letter in sorted(by_letter):
        vs = by_letter[letter]
        avg = sum(vs) // len(vs)
        P(f'| {letter} | {len(vs)} | {avg} | {sorted(vs)[len(vs)//2]} | {max(vs)} | {min(vs)} | {avg*100//TS_BASELINE}% |')
    P('')

    # Bloated sections
    P('## 個別セクションが TS 比 1.3 倍超のエントリ')
    P('')
    P('「何を」 (TS=60) > 78 字、または「どこで」 (TS=72) > 94 字に該当する上位 25 件:')
    P('')
    P('| ID | status | 何を | どこで | preview |')
    P('|----|--------|-----:|-------:|---------|')
    bloated = [r for r in rows if r[3]['何をしてくれるか'] > 78 or r[3]['どこで出会うか'] > 94]
    bloated.sort(key=lambda r: -(r[3]['何をしてくれるか'] + r[3]['どこで出会うか']))
    for eid, st, total, c in bloated[:25]:
        href = f'../drafts/prototypes/preview/{eid}.html'
        pdf = f'../drafts/prototypes/preview/pdf/{eid}.pdf'
        nani = c['何をしてくれるか']
        doko = c['どこで出会うか']
        nani_mark = '**' if nani > 78 else ''
        doko_mark = '**' if doko > 94 else ''
        P(f'| {eid} | {st} | {nani_mark}{nani}{nani_mark} | {doko_mark}{doko}{doko_mark} | [HTML]({href}) / [PDF]({pdf}) |')

    OUT.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(f'wrote {OUT} ({len(lines)} lines, {len(rows)} entries)', file=sys.stderr)


if __name__ == '__main__':
    main()
