# ポンチ絵・画像生成 量産計画

*2026-05-15 作成。`drafts/ponchi/*.svg` の下書きと、後工程の画像生成をつなぐための実行計画。*

## 0. 現状

- `ledgers/entries.csv` 基準では全 351 件。
- `status: archived` を除く対象は 350 件。
- 既存のポンチ絵 SVG は 15 件。
- 未生成は non-archived 全体で 335 件、`ready` のみでも 228 件。
- 既存仕様は [docs/ponchi_svg_spec.md](ponchi_svg_spec.md) にあり、黒一色の手書き風 SVG を `drafts/ponchi/{entry_id}.svg` に置く運用。

## 1. ゴール

各エントリに「使う人の 1 コマ」が入っている状態にする。

読者が専門用語を見たときに、抽象説明だけでなく「誰が、どんな場面で、どう困る／助かるのか」を直感でつかめるようにする。図の主役はロゴや製品画面ではなく、人・道具・吹き出し・状況に置く。

## 2. 絵柄の方向性

### 下書き SVG

- 黒一色の手書き風線画。
- 192 x 192 の正方形。
- 1 エントリ 1 コマ。
- ロゴや実在人物の肖像は描かず、一般化した小物で示す。
- 目的は「構図の叩き台」と「誌面での仮差し込み」。

### 本番画像生成

- SVG 下書きを構図参照として使う。
- 出力は印刷対応を考え、最初から高解像度で作る。
- 絵柄は、やわらかい手描き風・薄い紙色背景・黒またはごく少ないアクセントに寄せる。
- 生成画像内の文字は極力使わない。吹き出し文言は誌面側の caption に逃がす。
- 商標ロゴ、実在人物の顔、具体的な UI 画面の再現は避ける。

## 3. 進め方

### Phase 1: 棚卸し

対象を 3 グループに分ける。

1. `ready` かつ SVG なし: 先に進める。
2. `人書` / `needs_review` で SVG なし: 文章レビュー後に進める。
3. common / 凡例 / 索引系: ポンチ絵が必要か個別判断する。

この時点で `ledgers/ponchi_generation_queue.csv` を作り、`entry_id`, `title`, `status`, `md_path`, `has_svg`, `has_final_image`, `priority`, `notes` を持たせる。

### Phase 2: パイロット 10 件

まず 10 件だけで品質基準を固める。

候補:

- B-1 Gemini
- B-2 Claude
- B-3 ChatGPT
- B-4 Cursor
- B-8 Codex
- D-12 Claude 4
- F-1 JavaScript
- F-2 TypeScript
- G-1 Context
- J-14 LLM

この 10 件で、サービス・モデル・技術用語・LLM 用語・一般概念の代表パターンを確認する。

### Phase 3: SVG 下書き量産

1 バッチ 20 件を目安に、`drafts/ponchi/{entry_id}.svg` を作る。

各エントリでは markdown 末尾の `## 誌面ポンチ絵メモ` から以下を抽出する。

- 描く内容
- 登場人物
- 吹き出し・心の声
- 中央に置くキーワード
- シーン比較のポイント

SVG は「画像生成前の絵コンテ」として扱い、この段階では細部の画力より、構図と意味の明確さを優先する。

### Phase 4: 画像生成プロンプト化

SVG とポンチ絵メモから、1 件ずつ画像生成用プロンプトを作る。

保存先:

- `assets/ponchi/prompts/{entry_id}.md`

現在の正は [docs/ponchi_prompt_pipeline.md](ponchi_prompt_pipeline.md) に従う。古い「タイトルからそのまま絵を作る」方式は使わない。

プロンプトに含める要素:

- エントリ名
- `subject_type`
- `subject_stack`
  - `entry_subject`: 用語・サービス名そのもの
  - `visual_subject`: 絵で一番大きく見せる構造や流れ
  - `supporting_subjects`: 補助的に出す人物、小物、カード
  - `logo_subject`: 後合成する公式ロゴ。不要なら `none`
  - `excluded_subjects`: 似せてはいけないロゴ、UI、色、文字
- ロゴ状態
- 登場人物と視覚参照
- 構図ファミリー、構図タイプ、密度
- clearspace と main subject scale
- 禁止事項

標準プロンプトの型:

```text
Use case: infographic-diagram
Asset type: VibeCodingDictionary ponchi image
Primary request: Create a 2:1 horizontal technical-book ponchi illustration for {entry_id} {title}.
Subject: The entry subject is {entry_subject}, but the visual subject is {visual_subject}.
Composition: Use {composition_family} / {composition_type} with {composition_density} density.
Logo and brand rule: {logo block}
Color palette: strict white/black/gray plus approved blue accents only.
Style: clean simple editorial line illustration.
Avoid: {avoid list}. No readable text, no watermark.
```

### Phase 5: 本番画像生成

1 バッチ 10 件を目安に生成する。

保存先:

- `assets/ponchi/final/{entry_id}.png`
- 必要なら作業版を `assets/ponchi/work/{entry_id}_v01.png` に残す。

生成後に見る項目:

- 一目で「人が使っている場面」に見えるか。
- 用語の意味を誤解させる小物がないか。
- ロゴ・商標・実在人物に寄りすぎていないか。
- 画像内文字が崩れていないか。
- 200px 前後に縮小しても読めるか。
- 白黒印刷にしても意味が残るか。

### Phase 6: プレビュー差し込み

preview generator 側で、優先順位を以下にする。

1. `assets/ponchi/final/{entry_id}.png`
2. `drafts/ponchi/{entry_id}.svg`
3. placeholder

本番画像を入れたら、`scripts/preview_gen.py` と PDF 出力で確認する。

### Phase 7: 全体レビュー

50 件ごとに並べて見て、単調さと絵柄のズレを確認する。

確認観点:

- 似た構図が連続しすぎていないか。
- サービス章だけ製品紹介っぽくなりすぎていないか。
- 人物の属性表現が偏っていないか。
- 初学者が見て怖くないか。
- 技術者が見ても雑すぎないか。

## 4. 優先順位

最初は `ready` のうち、読者が最初に読む可能性が高いものから進める。

1. B 章: 主要サービス
2. D 章: 主要モデル
3. G 章: LLM 用語
4. F 章: 開発ツール・技術用語
5. J 章: 一般概念
6. C / E / H / I 章: 人物・ベンチマーク・歴史・MCP
7. A 章 common: 必要なものだけ個別対応

## 5. 1 件あたりの完成条件

- `drafts/ponchi/{entry_id}.svg` がある。
- `assets/ponchi/prompts/{entry_id}.md` がある。
- `assets/ponchi/final/{entry_id}.png` がある。
- preview HTML で崩れていない。
- PDF 出力で枠からはみ出していない。
- `ledgers/ponchi_generation_queue.csv` の `has_final_image` が true。

## 6. 次にやること

1. `ledgers/ponchi_generation_queue.csv` を生成する。
2. 既存 15 SVG を点検し、画像生成に回せる品質か見る。
3. パイロット 10 件の不足 SVG を作る。
4. パイロット 10 件の画像生成プロンプトを作る。
5. 10 件だけ実画像を生成し、誌面プレビューで方向性を決める。

この 10 件で絵柄と作業単価が見えたら、以後は 20 件単位の SVG 下書き、10 件単位の画像生成で回す。
