---
id: G-5
title: Context Window
title_reading: コンテキストウィンドウ
category: term_llm
subtype: basic
experience_level: research_only
reader_level: 2
importance: C
figure_type: comparison
page_layout: spread_v1
start_date:
end_date:
version_status: active
pricing_note:
evaluation_date: 2026-04-29
related_terms:
  - Context
  - Token
  - Context Engineering
  - LLM
  - RAG
status: ready
---

# Context Window

## tagline

LLM が 1 回の応答で読める情報量の上限です。トークン数で測り、モデルごとに異なります。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

LLM（大規模言語モデル）が 1 回の推論で参照できるトークン数の上限です。指示・会話履歴・添付ファイルはこの枠に収まる範囲でしか見えません。

## どこで出会うか

API ドキュメントやモデル比較表に「128K」「200K」「1M」と表記されます。「入力が長すぎる」とエラーが出るのは、Context Window の上限を超えた場合です。

## メイン図

### 図の狙い

主要モデルの Context Window サイズを横幅の帯グラフで並べ、「1M トークンでも実効的に使える長さには限界がある」という感覚を掴んでもらいます。

### B. 登場シーン（figure_type: comparison）

- シーン1: GPT-4（32K）→ GPT-4 Turbo（128K）→ Claude 3 系（200K）→ Gemini 1.5 Pro（1M）の帯グラフ
- シーン2: 帯の中に「会話履歴」「添付資料」「System Prompt」がブロックとして積み上がる様子
- シーン3: 帯の右端近くに「lost in the middle」の注釈（中間に挟んだ情報は参照されにくい）
- 並べる基準: トークン数の大小（左が小、右が大）

## 会話での使い方例

「Context Window が広いと長文を渡せますが、中間情報の見落としには注意ですよね。」

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

LLM が一度に見られる情報量の上限を示す枠です。

### 2. うれしさ

上限が広いほど長文書類や複数ファイルを分割せず渡せます。

### 3. 注意点

広くても中間部の情報は参照されにくくなることがあります。

### 4. どこで役立つか

長い仕様書・会話履歴・コードベースを一括で処理する場面です。

### 5. はじめに

「〇〇K トークン」が枠の広さで、超えると情報が見えない点を押さえることです。

### 6. 深掘り先

Context Engineering、RAG、Prompt Caching。

## 開発フローでの位置（必須）

1. 素材を用意する — 指示・資料・会話履歴をそろえる
2. トークン数を見積もる — Tokenizer ツールで合計量を確認する
3. 枠に収める — 上限を超える分は要約・分割・RAG で補う
4. LLM に送る — 優先度の高い情報を先頭か末尾に置く
5. 出力を確認する — 中間情報が欠落していないかを検証する

## 関連用語

- Context
- Token
- Context Engineering
- LLM
- RAG


<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- 昔のモデルは Context Window が小さく、分割などの工夫が必要でした。
- コンテキストを圧縮すると文脈がおかしくなることがよくありました。
-
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: 覚えられる範囲がちっちゃいのが課題なんだな。
- 👍 良い点: 最近のモデルは改善が進み、ボトルネックは解消されつつあります。
- 👎 ダメな点: 全部入れようとするプロセス自体が間違いで、依然として課題はゼロではありません。
- 👥 誰向けか: LLM を使って何かをやる人には知識として必要。
<!-- user-input:end key="my_comment" -->


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: comparison）

- 描く内容: 横帯グラフ（左が小、右が大）でモデルごとの Context Window サイズを比較。GPT-4（32K）→ GPT-4 Turbo（128K）→ Claude 3 系（200K）→ Gemini 1.5 Pro（1M）を 4 段で積む。各帯の中に「System Prompt」「会話履歴」「資料」のブロックを積み上げて表示
- 登場人物: 帯の右端を覗き込む読者キャラクター。「これ全部入るの？」という吹き出し
- 吹き出し・心の声: 「1M でも中間の情報は迷子になりがち」という注釈を帯の中間付近に添える
- 中央に置くキーワード/ラベル: Context Window ＝ 情報の枠

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: 書類スタック（素材をそろえる）
- Step 2 のアイコン/絵柄: 電卓・メーター（トークン数を確認）
- Step 3 のアイコン/絵柄: ハサミ＋箱（分割・要約・RAG で補う）
- Step 4 のアイコン/絵柄: 送信矢印（優先情報を先頭・末尾に置く）
- Step 5 のアイコン/絵柄: 虫眼鏡＋チェック（中間情報の欠落確認）
- 矢印で示す流れの意図: 「そろえる → 測る → 調整する → 送る → 確認する」の 1 往復


## コミュニティ補完メモ

- G-1 Context は「LLM に渡す情報の総体（何を入れるか）」の設計視点。本エントリ G-5 はその「容量上限」に絞る。
- G-2 Token は「情報量の単位」の説明。G-5 はその単位で測った上限値の説明。
- G-11 Context Engineering は「Context Window をどう使い切るか・何を捨てるか」の技術論。本エントリからは「詳しくは G-11 へ」と送る。
- 「lost in the middle」問題（Liu et al. 2023）は本エントリの注意点に 1 句入れ、詳細は G-11 または備考へ送る。
- RAG（検索拡張生成）は Context Window を補う手段として言及するにとどめ、RAG エントリへ送る。


## 出典メモ

- Anthropic docs "Models overview" <https://docs.anthropic.com/en/docs/about-claude/models> — checked 2026-04-29
- OpenAI docs "Models" <https://platform.openai.com/docs/models> — checked 2026-04-29
- Google AI "Gemini API models" <https://ai.google.dev/gemini-api/docs/models> — checked 2026-04-29
- Liu et al. "Lost in the Middle: How Language Models Use Long Contexts" (2023) — checked 2026-04-29


## 備考

モデルごとの Context Window サイズは頻繁に更新されます（例：GPT-4 は 8K → 32K → 128K と拡大）。evaluation_date を定期的に更新してください。1M トークンのような大きな枠でも、入力の中間部分に置いた情報が参照されにくい「lost in the middle」現象は別問題で、容量と実効的な使える長さは異なります。
