# デザイントークン案

## 目的
見た目の判断を後で変えやすくするため、色、余白、文字サイズ、ラベルを先に分けておく。

## カラーパレット案

### Palette A: Clean Blue
標準候補。要件書の「白背景、青系2色」に最も近い。

- background: `#FFFFFF`
- text: `#1F2937`
- muted_text: `#6B7280`
- line: `#CBD5E1`
- blue_main: `#2563EB`
- blue_soft: `#DBEAFE`
- blue_deep: `#1E3A8A`
- warning_soft: `#FEF3C7`

### Palette B: Ink And Cyan
少し技術資料寄り。画面で見る場合に締まる。

- background: `#FFFFFF`
- text: `#111827`
- muted_text: `#64748B`
- line: `#D7DEE8`
- blue_main: `#0F72B8`
- blue_soft: `#E6F6FF`
- cyan_accent: `#06B6D4`
- note_soft: `#F8FAFC`

### Palette C: Editorial Navy
冊子寄り。落ち着くが、硬くなりやすい。

- background: `#FFFFFF`
- text: `#172033`
- muted_text: `#667085`
- line: `#D0D5DD`
- blue_main: `#1D4ED8`
- blue_soft: `#EFF6FF`
- navy_band: `#0B1F3A`
- note_soft: `#F9FAFB`

## 初期推奨
最初は Palette A を採用候補にする。

理由:
- 白背景との相性がよい
- 図解と本文の両方に使いやすい
- 青系2色ルールに収まりやすい
- 印刷時も比較的破綻しにくい

## 文字サイズ案

### A4 / 印刷寄り
- title: 28-34pt
- subtitle: 11-13pt
- section_heading: 11-13pt
- body: 9-10.5pt
- meta: 7-8pt
- caption: 7-8pt

### 画面プレビュー寄り
- title: 32-40px
- subtitle: 16-18px
- section_heading: 15-17px
- body: 14-16px
- meta: 12-13px
- caption: 12-13px

## 余白案
- page_margin: 広め
- block_gap: 中
- card_padding: 中
- figure_padding: 広め
- line_width: 太め

## ラベル案

### experience_level
- `hands_on`: 触った
- `partial`: 少し触った
- `research_only`: 調査ベース

### reader_level
- `Lv.1`: 言葉だけ知りたい
- `Lv.2`: 会話についていきたい
- `Lv.3`: 手を動かしたい
- `Lv.4`: 自走したい
- `Lv.5`: 実装まで踏み込みたい
- `Lv.6`: 最先端まで追いたい

### update_risk
- `low`: 更新少
- `medium`: 要確認
- `high`: 頻繁に変わる

## アイコン方針
最初はアイコンを作り込みすぎない。

- 体験区分: 小さなラベルで十分
- 読者レベル: `Lv.2` のように短く表示
- 更新リスク: 色ではなく文字で補足
- 出典確認: `checked: YYYY-MM-DD`

## NG
- 背景全体を青くしない
- グラデーションを主役にしない
- 図の中に長い文章を入れない
- タイトル以外で大きすぎる文字を使わない
- 装飾のためだけの丸や光彩を置かない
