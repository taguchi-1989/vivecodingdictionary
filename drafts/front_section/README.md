# 前付け 7 見開き — HTML たたき台

A 群（A-1〜A-11）を `spread_v1` ではなく独自レイアウト（`front_*`）で作る、画像生成の下絵としての HTML 群です。

## 目的

- A 群の前付け（まえがき・凡例・索引など）は、用語エントリ用の `spread_v1` テンプレでは内容が空転する
- 仕様は [docs/front_section_layout.md](../../docs/front_section_layout.md) で確定済み
- 本ディレクトリの HTML は「画像生成（最終版）のたたき台」として、構図・本文・コンポーネントを Claude が起こした下絵
- 著者が中身をレビュー → 画像生成プロンプトに反映 → 最終版を確定する想定

## 構成

| # | ファイル | 見開き | layout | ID |
|:-:|:--|:--|:--|:--|
| 0 | `0_concept_spread.html` | 扉「知らないことばで、止まらない。」 | `front_concept_spread` | front_concept |
| 1 | `1_a1_preface.html` | まえがき | `front_essay` | A-1 |
| 2 | `2_a2_anatomy.html` | 見開きの読み方（分解図） | `front_anatomy` | A-2 |
| 3 | `3_a3_a9_map_index.html` | 図鑑の歩き方＋ミニ索引 | `front_map_index` | A-3 + A-9 |
| 4 | `4_a4_a5_a6_legend_marks.html` | 注意マークの凡例 | `front_legend_marks` | A-4 + A-5 + A-6 |
| 5 | `5_a7_a8_swatch.html` | 図と色の見本帳 | `front_swatch` | A-7 + A-8 |
| 6 | `6_a10_a11_log_glossary.html` | 更新履歴と略称 | `front_log_glossary` | A-10 + A-11 |

一覧は [index.html](index.html) から開けます。

## スタイル

- `_common.css` — 共通スタイル（spread レイアウト・チロム・タグ帯・ピル等）
- 親 base.css は [drafts/prototypes/mockups/design_philosophy_v2/base.css](../prototypes/mockups/design_philosophy_v2/base.css) を参照
- Zen Maru Gothic + Inter のフォント体系、青系単色のトーンを継承

## 見開きサイズ

- 1 ページ: 750 × 1061px（本編 `spread_v1` と同じ印刷想定）
- 見開き合計: 1500 × 1061px
- ブラウザでそのまま表示するとほぼ実寸感

## 次の工程

1. **著者レビュー** — 構図・本文の方向性確認
2. **画像生成プロンプト化** — レイアウトを参考に Midjourney/SD/Imagen 等のプロンプトに展開
3. **最終版の差し替え** — HTML たたき台を画像（または最終 HTML）に置き換え
4. **A-N の markdown 整理** — `front_*` レイアウト前提に書き直し（[docs/front_section_layout.md](../../docs/front_section_layout.md) §6 残作業）

## 関連ファイル

- [docs/front_section_layout.md](../../docs/front_section_layout.md) — 仕様
- [drafts/opening_spread_brief.md](../opening_spread_brief.md) — 扉のブリーフ
- [drafts/opening/opening-spread-annotated.html](../opening/opening-spread-annotated.html) — 扉の旧モック
- [content/entries/common/A-*.md](../../content/entries/common/) — A 群既存マークダウン（本書きの原型）

## 履歴

- 2026-05-24: 初版 7 spreads ＋ 共通 CSS ＋ index 一式を作成
