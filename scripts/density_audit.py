#!/usr/bin/env python3
"""字数バリエーション監査（v2: 各領域別ブロック詳細）

各セクションの目安文字数と現状を比較し、超過/不足を可視化する。

出力:
  - ledgers/density_audit.md       — サマリ（章別平均、外れ値）
  - ledgers/density_audit_detail.md — 全エントリ × 全セクションの詳細表

Usage:
    python scripts/density_audit.py
"""
from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
ENTRIES = REPO / 'content' / 'entries'
OUT_SUMMARY = REPO / 'ledgers' / 'density_audit.md'
OUT_DETAIL = REPO / 'ledgers' / 'density_audit_detail.md'

# ─── 各セクションのターゲット（min, max, 推奨 max） ──────────
# max 超えは ⚠ 表示。推奨 max 超えは note。
TARGETS = {
    # 左ページ
    'tagline':              {'min': 25, 'max': 45, 'rec_max': 38, 'kind': 'body'},
    '何をしてくれるか':       {'min': 60, 'max': 85, 'rec_max': 75, 'kind': 'body'},
    'どこで出会うか':         {'min': 60, 'max': 90, 'rec_max': 80, 'kind': 'body'},
    '会話での使い方例':       {'min': 25, 'max': 50, 'rec_max': 40, 'kind': 'body'},
    # 右ページ 6 視点
    '1. 役割':               {'min': 15, 'max': 30, 'rec_max': 25, 'kind': 'six'},
    '2. うれしさ':           {'min': 15, 'max': 30, 'rec_max': 25, 'kind': 'six'},
    '3. 注意点':             {'min': 15, 'max': 30, 'rec_max': 25, 'kind': 'six'},
    '4. どこで役立つか':     {'min': 15, 'max': 30, 'rec_max': 25, 'kind': 'six'},
    '5. はじめに':           {'min': 15, 'max': 30, 'rec_max': 25, 'kind': 'six'},
    '6. 深掘り先':           {'min': 15, 'max': 35, 'rec_max': 30, 'kind': 'six'},
}
# 著者欄ターゲット
AUTHOR_BULLET_TARGET = {'max': 40, 'rec_max': 35}
COMMENT_LABELS = ['第一印象', '良い点', 'ダメな点', '誰向けか']

# TS 見本基準（参考値）
TS = {'tagline': 35, '何をしてくれるか': 60, 'どこで出会うか': 72, '会話での使い方例': 30,
      '1. 役割': 21, '2. うれしさ': 20, '3. 注意点': 18,
      '4. どこで役立つか': 20, '5. はじめに': 25, '6. 深掘り先': 27}
TS_BASELINE = sum(TS.values())  # 328


# ─── パーサ ───────────────────────────────────────────────


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
    """## または ### のセクション本文文字数"""
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


def tagline_chars(fm, body):
    """tagline は ## tagline 本文セクション。なければ YAML の tagline: フィールド。"""
    n = section_chars(body, 'tagline')
    if n > 0:
        return n
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


def extract_section_raw(body, heading):
    pat = re.compile(rf'^##\s+{re.escape(heading)}\s*$(.+?)(^##\s|\Z)', re.S | re.M)
    m = pat.search(body)
    return m.group(1) if m else ''


def tsumazuki_bullets(body):
    sect = extract_section_raw(body, '非エンジニアのつまずき')
    bullets = []
    for line in sect.splitlines():
        m = re.match(r'^\s*-\s+(.+)$', line)
        if not m:
            continue
        t = m.group(1).strip()
        if re.fullmatch(r'[（(]\s*著者記入欄[・·]?空?\s*[）)]', t):
            continue
        bullets.append(t)
    return bullets


def comment_items(body):
    sect = extract_section_raw(body, '私のコメント')
    out = {label: '' for label in COMMENT_LABELS}
    for line in sect.splitlines():
        m = re.match(r'^\s*-\s+(.+)$', line)
        if not m:
            continue
        content = m.group(1).strip()
        for label in COMMENT_LABELS:
            mm = re.search(rf'{re.escape(label)}\s*[:：]\s*(.*)$', content)
            if mm:
                v = mm.group(1).strip()
                if re.fullmatch(r'[（(]\s*著者記入欄[・·]?空?\s*[）)]', v):
                    v = ''
                out[label] = v
                break
    return out


# ─── 監査 ─────────────────────────────────────────────────


def audit_entry(f: Path):
    text = f.read_text(encoding='utf-8')
    fm, body = parse(text)
    st = status_of(fm)
    if st in ('archived',):
        return None
    if layout_of(fm).startswith('front_'):
        return None
    em = re.match(r'([A-J]-\d+)', f.stem)
    if not em:
        return None
    eid = em.group(1)

    sections = {}
    for name in TARGETS:
        if name == 'tagline':
            sections[name] = tagline_chars(fm, body)
        else:
            sections[name] = section_chars(body, name)

    body_total = sum(sections.values())

    tsu = tsumazuki_bullets(body)
    com = comment_items(body)

    return {
        'id': eid,
        'letter': eid[0],
        'num': int(eid.split('-')[1]),
        'status': st,
        'sections': sections,
        'body_total': body_total,
        'tsumazuki': tsu,
        'comment': com,
    }


def fmt_chars(n: int, target: dict, badge_only: bool = False) -> str:
    """文字数を表示。max 超えは ⚠、rec_max 超えは ▲、その他はそのまま。"""
    max_ = target['max']
    rec = target['rec_max']
    if n > max_:
        return f'⚠ {n}' if not badge_only else '⚠'
    if n > rec:
        return f'▲ {n}' if not badge_only else '▲'
    return str(n)


def section_badge(n: int, target: dict) -> str:
    if n > target['max']:
        return 'over'
    if n > target['rec_max']:
        return 'near'
    if n < target['min']:
        return 'under'
    return 'ok'


def author_badge(text: str) -> str:
    if not text:
        return 'empty'
    if len(text) > AUTHOR_BULLET_TARGET['max']:
        return 'over'
    if len(text) > AUTHOR_BULLET_TARGET['rec_max']:
        return 'near'
    return 'ok'


# ─── 出力 ─────────────────────────────────────────────────


def write_summary(rows):
    lines = []
    P = lines.append
    P('# 字数監査サマリ\n')
    P(f'**TS 見本基準値** 本文合計 {TS_BASELINE} 字 (内訳 — '
      + ' / '.join(f'{k} {v}' for k, v in TS.items()) + ')\n')
    P('各セクションの **max / 推奨 max** 設定値:\n')
    P('| section | min | rec max | max |')
    P('|---------|----:|--------:|----:|')
    for name, t in TARGETS.items():
        P(f'| {name} | {t["min"]} | {t["rec_max"]} | {t["max"]} |')
    P(f'| 非エンジニアのつまずき (各 bullet) | — | {AUTHOR_BULLET_TARGET["rec_max"]} | {AUTHOR_BULLET_TARGET["max"]} |')
    P(f'| 私のコメント (各ラベル) | — | {AUTHOR_BULLET_TARGET["rec_max"]} | {AUTHOR_BULLET_TARGET["max"]} |')
    P('')

    totals = [r['body_total'] for r in rows]
    P(f'**対象**: {len(rows)} 件（前付け／archived 除外）')
    P(f'**本文合計**: max {max(totals)} / min {min(totals)} / 中央値 {sorted(totals)[len(totals)//2]} / 平均 {sum(totals)//len(totals)}\n')

    # Over-the-max counts per section
    P('## セクションごとの「max 超」件数\n')
    P('| section | max | over | near | over IDs (上位) |')
    P('|---------|----:|-----:|-----:|----------------|')
    for name, t in TARGETS.items():
        over = [r for r in rows if r['sections'][name] > t['max']]
        near = [r for r in rows if t['rec_max'] < r['sections'][name] <= t['max']]
        over.sort(key=lambda r: -r['sections'][name])
        ids = ', '.join(f'{r["id"]}({r["sections"][name]})' for r in over[:8])
        P(f'| {name} | {t["max"]} | {len(over)} | {len(near)} | {ids} |')
    P('')

    # Author overflow
    tsu_over = 0
    tsu_near = 0
    com_over = 0
    com_near = 0
    tsu_long_ids = []
    com_long_ids = []
    for r in rows:
        for b in r['tsumazuki']:
            if len(b) > 40:
                tsu_over += 1
                if not any(eid == r['id'] for eid, _ in tsu_long_ids):
                    tsu_long_ids.append((r['id'], max(len(x) for x in r['tsumazuki'])))
            elif len(b) > 35:
                tsu_near += 1
        for label, v in r['comment'].items():
            if v and len(v) > 40:
                com_over += 1
                if not any(eid == r['id'] for eid, _ in com_long_ids):
                    com_long_ids.append((r['id'], max((len(x) for x in r['comment'].values() if x), default=0)))
            elif v and len(v) > 35:
                com_near += 1
    tsu_long_ids.sort(key=lambda x: -x[1])
    com_long_ids.sort(key=lambda x: -x[1])

    P('## 著者欄の「max=40 超」bullet 数\n')
    P(f'- 非エンジニアのつまずき bullet 超過 **{tsu_over}** 件 / 推奨超過 {tsu_near} 件')
    P(f'- 私のコメント ラベル超過 **{com_over}** 件 / 推奨超過 {com_near} 件')
    P('')
    P('### つまずき 超過 ID 上位 15')
    P('')
    for eid, n in tsu_long_ids[:15]:
        P(f'- {eid} (最大 {n} 字)')
    P('')
    P('### 私のコメント 超過 ID 上位 15')
    P('')
    for eid, n in com_long_ids[:15]:
        P(f'- {eid} (最大 {n} 字)')
    P('')

    # Per-chapter average
    P('## 章ごとの本文合計平均\n')
    by_letter = defaultdict(list)
    for r in rows:
        by_letter[r['letter']].append(r['body_total'])
    P('| 章 | 件数 | 平均 | 中央値 | max | min |')
    P('|----|-----:|-----:|------:|----:|----:|')
    for letter in sorted(by_letter):
        vs = by_letter[letter]
        P(f'| {letter} | {len(vs)} | {sum(vs)//len(vs)} | {sorted(vs)[len(vs)//2]} | {max(vs)} | {min(vs)} |')
    P('')

    OUT_SUMMARY.write_text('\n'.join(lines) + '\n', encoding='utf-8')


def write_detail(rows):
    """全エントリ × 全セクションの詳細表"""
    lines = []
    P = lines.append
    P('# 字数監査 詳細表\n')
    P('凡例: `⚠` max 超 / `▲` 推奨 max 超 / 通常表示 = OK / `—` 空')
    P('')

    # Header
    cols = ['ID', 'status']
    for name in TARGETS:
        cols.append(name)
    cols.extend(['本文計', 'つま1', 'つま2', 'つま3', 'コ印象', 'コ良い', 'コダメ', 'コ誰', 'preview'])
    P('| ' + ' | '.join(cols) + ' |')
    P('|' + '|'.join(['---'] * len(cols)) + '|')

    for r in rows:
        cells = [r['id'], r['status']]
        for name, t in TARGETS.items():
            cells.append(fmt_chars(r['sections'][name], t))
        cells.append(str(r['body_total']))

        # tsumazuki: up to 3
        for i in range(3):
            if i < len(r['tsumazuki']):
                n = len(r['tsumazuki'][i])
                if n > 40:
                    cells.append(f'⚠ {n}')
                elif n > 35:
                    cells.append(f'▲ {n}')
                else:
                    cells.append(str(n))
            else:
                cells.append('—')

        # comment: 4 labels
        for label in COMMENT_LABELS:
            v = r['comment'][label]
            if not v:
                cells.append('—')
            else:
                n = len(v)
                if n > 40:
                    cells.append(f'⚠ {n}')
                elif n > 35:
                    cells.append(f'▲ {n}')
                else:
                    cells.append(str(n))

        cells.append(f'[H](../drafts/prototypes/preview/{r["id"]}.html) [P](../drafts/prototypes/preview/pdf/{r["id"]}.pdf)')
        P('| ' + ' | '.join(cells) + ' |')

    OUT_DETAIL.write_text('\n'.join(lines) + '\n', encoding='utf-8')


def main():
    rows = []
    for f in sorted(ENTRIES.rglob('*.md')):
        r = audit_entry(f)
        if r:
            rows.append(r)
    rows.sort(key=lambda r: (r['letter'], r['num']))
    write_summary(rows)
    write_detail(rows)
    print(f'wrote {OUT_SUMMARY} (summary)')
    print(f'wrote {OUT_DETAIL} ({len(rows)} entries)')


if __name__ == '__main__':
    main()
