---
id: H-58
title: Transformer 論文
title_reading: トランスフォーマーろんぶん
category: history
subtype: paper
experience_level: research_only
reader_level: 3
importance: E
figure_type: timeline
page_layout: spread_v1
start_date: 2017-06-12
version_status:
pricing_note:
evaluation_date: 2026-04-29
related_terms:
  - Transformer
  - Attention
  - LLM
  - BERT
  - GPT-1
status: needs_review
---

# Transformer 論文

## tagline

2017 年公開の "Attention Is All You Need"。現代 LLM（大規模言語モデル）の起点となった論文です。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

Google Brain の 8 名による論文で、Attention（注意機構）だけで文章を処理する Transformer アーキテクチャ（設計の骨格）を提案。翌年に BERT・GPT-1 が登場し、LLM ブームの土台になっています。

## どこで出会うか

「現代 AI の起点」として技術記事や書籍で参照されます。ChatGPT や Claude の説明で「Transformer ベース」と出てきたら、この論文がもとです。

## メイン図

### 図の狙い

2017 年の論文公開を起点に、BERT・GPT-1（2018 年）、GPT-3（2020 年）、ChatGPT（2022 年）、LLM 全盛（2023 年〜）へと続く時系列を 1 枚で見せます。

### A. Before / After＋時系列（figure_type: timeline）

- Before（〜2017-06）
  - 翻訳・文章生成には RNN（再帰型ニューラルネット）を使うのが主流
  - 長い文になるほど前の文脈を忘れやすいという課題があった
- 2017-06-12：arXiv:1706.03762 公開
  - Attention だけで処理する Transformer を提案
- After（2018 年〜）
  - BERT（Google）・GPT-1（OpenAI）登場
  - GPT-3（2020 年）→ ChatGPT（2022 年）→ LLM 全盛へ

## 会話での使い方例

「Transformer 論文が 2017 年の起点で、BERT や GPT もここから派生したんですよね。」

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

現代 LLM のアーキテクチャを定義した学術論文の起点です。

### 2. うれしさ

この 1 本で RNN から Transformer へのシフトが一気に起きました。

### 3. 注意点

論文自体は翻訳タスク向けで、LLM への応用は後から広がりました。

### 4. どこで役立つか

AI の歴史的文脈を理解したいときの最初の参照点になります。

### 5. はじめに

タイトル「Attention Is All You Need」と 2017 年公開という事実で十分です。

### 6. 深掘り先

Transformer（J-13）、Attention（J-17）、LLM（J-14）

## 開発フローでの位置（必須）

1. 論文公開（2017-06）— Attention だけの新アーキテクチャを提案。
2. BERT / GPT-1（2018 年）— 事前学習モデルに応用され精度向上。
3. GPT-3（2020 年）— 大規模化で生成の質が商用レベルに。
4. ChatGPT（2022 年）— 一般公開で LLM が社会に浸透。
5. LLM 全盛（2023 年〜）— Claude・Gemini も Transformer を基盤に。

## 関連用語

- Transformer
- Attention
- LLM
- BERT
- GPT-1

<!-- ━━━━━━━━ 著者記入欄（右ページ下段に印刷される／AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

-
-
-

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

- 🙂 第一印象:
- 👍 良い点:
- 👎 ダメな点:
- 👥 誰向けか:


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: timeline）

- 描く内容: 横軸に時系列（2016 年〜2024 年）。2017-06 に星印「論文公開」を置き、右へ BERT/GPT-1（2018）、GPT-3（2020）、ChatGPT（2022）、LLM 全盛（2023〜）とドットを並べる。左側（Before）には RNN の時代として研究者が首をかしげているシーン。
- 登場人物: 左に研究者（論文を持ち「RNN は長文が苦手で…」と悩んでいる）、右に一般ユーザー（ChatGPT 画面を開いて驚く）
- 吹き出し・心の声: 論文公開点「Attention だけでいける！」、右端「ここまで来た」
- 中央に置くキーワード/ラベル: Attention Is All You Need（2017）

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: 論文アイコン（公開）
- Step 2 のアイコン/絵柄: 積み木が増えるアイコン（BERT/GPT-1）
- Step 3 のアイコン/絵柄: 大きなデータの山アイコン（GPT-3 大規模化）
- Step 4 のアイコン/絵柄: 発射アイコン（ChatGPT 一般公開）
- Step 5 のアイコン/絵柄: 群像アイコン（LLM 全盛・各社競争）
- 矢印で示す流れの意図: 論文 → モデル応用 → 大規模化 → 一般公開 → 普及という歴史の流れ

## コミュニティ補完メモ

- Transformer 概念（J-13）との住み分け：J-13 は「Transformer とは何か・どう動くか」の構造視点。本エントリ H-58 は「2017 年の論文がどう LLM ブームを起こしたか」の歴史視点に絞る。
- Attention 単体（J-17）との住み分け：Attention の仕組みの詳細は J-17 へ。本エントリでは「Attention だけで処理する」という論文のポイントを一言で触れるにとどめる。
- LLM（J-14）との住み分け：J-14 は現在の LLM サービス・利用視点。H-58 は歴史的な論文という「起点」に絞る。
- ChatGPT 登場（H-53）との住み分け：H-53 は 2022 年の一般公開という社会現象の起点。H-58 はその 5 年前の学術論文という技術的起点。

## 出典メモ

- Vaswani et al., "Attention Is All You Need", arXiv:1706.03762 (2017) — checked 2026-04-29
- Google AI Blog, "Transformer: A Novel Neural Network Architecture for Language Understanding" (2017) — checked 2026-04-29

## 備考

- RNN（再帰型ニューラルネット）は初出で日本語補足を入れた。
- 論文共著者 8 名（Ashish Vaswani ほか Google Brain・Google Research）の個別紹介はスコープ外。
- BERT・GPT-1 は 2018 年登場の後続モデルとして歴史的位置づけのみ言及。詳細は各エントリへ。
