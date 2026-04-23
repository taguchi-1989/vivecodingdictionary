# バイブコーディング図鑑 制作計画

## 目的
非エンジニアや周辺職種の人が、AI開発・フロントエンド開発・LLM活用の現場で飛び交う言葉を、図解と短文と体験メモで辞書引きできる形にする。

## 初期スコープ
最初は要件定義書の「試作対象」に合わせて、以下の3ページを作る。

1. Gemini: サービス紹介ページ
2. Gemini 2.5 Pro / Flash / Flash-Lite: モデル比較ページ
3. TypeScript: 技術用語ページ

## ディレクトリ方針
- `content/entries/`: 公開誌面の元になるMarkdown項目
- `content/frontmatter/`: 序文、まえがき、共通方針
- `templates/`: ページ雛形、図解プロンプト雛形
- `ledgers/`: 調査・制作・図解の裏台帳
- `assets/figures/`: 図解素材とプロンプト
- `drafts/prototypes/`: レイアウトや書きぶりの試作

## 制作ルール
- 1項目1Markdownファイルで管理する。
- YAML front matter には短い属性だけを置く。
- 本文には、定義、役割、実務での意味、つまずき、主観コメント、出典メモを書く。
- 事実と主観を混ぜない。
- 体験区分は `hands_on`, `partial`, `research_only` の3段階で管理する。
- サービスやモデルの評価は、必ず `evaluation_date` を持たせる。

## IDレンジ
- 000-099: 共通・序文・方針
- 100-199: Service
- 200-299: Model
- 300-399: Term
- 400-499: Tool
- 500-599: Workflow
- 600-699: History
- 700-799: Person
- 800-899: Benchmark
- 900-999: 保留・未整理・実験枠

## 直近の作業順
1. `templates/entry_template.md` を基準テンプレとして固定する。
2. `ledgers/entries.csv` に試作3項目を登録する。
3. Gemini、モデル比較、TypeScript の3本を下書きする。
4. 各ページの図解タイプを決める。
5. 図解プロンプトを `assets/figures/prompts/` に保存する。
6. 3本を見比べて、項目不足と文章量を調整する。

## 未決定事項
- 序文を短い前書きにするか、問題提起を含む長めの文章にするか。
- 体験区分ラベルの表示デザイン。
- 図解素材の最終生成・保存ルール。
- 印刷用レイアウトの母艦ツール。
