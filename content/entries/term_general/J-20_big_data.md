---
id: J-20
title: Big Data
title_reading: ビッグ データ
category: term_general
subtype: data_learning
experience_level: research_only
reader_level: 2-3
figure_type: structure
page_layout: spread_v1
start_date:
end_date:
version_status: active
pricing_note: none
evaluation_date: 2026-04-30
related_terms:
  - Machine Learning
  - Deep Learning
  - DX
  - SaaS
status: drafting
---

# Big Data

<!-- バイブコーディング図鑑 エントリー雛形 v2 -->

## tagline

3V（量・速度・多様性）が従来システムの限界を超えたデータの総称です。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

Volume（量）・Velocity（速度）・Variety（多様性）の 3V が自社システムで扱いきれない規模になったデータを指します。明確な閾値はなく、「これまでの環境では処理できない」という相対的な状態を表す概念です。

## どこで出会うか

2010 年代の DX（デジタルトランスフォーメーション）関連資料や、データ基盤を説明するプレゼンで頻繁に登場します。機械学習（J-10）の学習データを語る文脈でも使われ、現在は RAG（G-15）やデータレイクハウスの話題で再び目にします。

## メイン図

### 図の狙い

3V の三角形と、「従来 DB の壁」を超えるイメージで概念を掴んでもらいます。

### C. 概念図（figure_type: structure）

- 中心に置く概念: 3V（Volume・Velocity・Variety）
- 周辺の要素: 従来 DB の限界 / Hadoop / Spark / BigQuery / LLM 学習データ
- 関係の描き方: 3V を中心円に置き、外側に技術要素を矢印で結ぶ


## 会話での使い方例

「Big Data 基盤の資産を、いまは LLM の RAG で活かしています。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

従来システムで処理できない規模のデータを指す概念です。

### 2. うれしさ

膨大なデータを活かして機械学習モデルの精度を高められます。

### 3. 注意点

バイト数の閾値はなく、相対的な「扱いきれない量」を指します。

### 4. どこで役立つか

DX 推進や AI モデルの学習データ整備の文脈で役立ちます。

### 5. はじめに

3V の意味と「定義に数値基準がない」点を押さえれば十分です。

### 6. 深掘り先

Machine Learning、RAG、Hadoop

## 開発フローでの位置（必須）

1. データ収集 — Web・センサー・ログなど多様なソースからデータを集めます
2. 蓄積・格納 — HDFS や BigQuery などの分散ストレージに保存します
3. 処理・変換 — Apache Spark 等でバッチ処理や集計を行います
4. 分析・活用 — 機械学習モデルの学習データや RAG の検索源として利用します


## 関連用語

- Machine Learning
- Deep Learning
- DX
- SaaS


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

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: 3V（Volume・Velocity・Variety）を三角形の頂点に配置し、中央に「Big Data」と大きく書く。外側に「従来 DB の壁（破線）」と「Hadoop / Spark / BigQuery」を配置する
- 登場人物: データアナリストふうの人物（女性・30 代）が 3V の三角形を指差している
- 吹き出し・心の声: 「これ、普通の DB に入らないんですよね…」
- 中央に置くキーワード/ラベル: Big Data（3V）

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: クラウドからデータが流れ込むアイコン
- Step 2 のアイコン/絵柄: サーバーラックのアイコン
- Step 3 のアイコン/絵柄: 歯車（処理）アイコン
- Step 4 のアイコン/絵柄: グラフ・モデルのアイコン
- 矢印で示す流れの意図: 収集 → 蓄積 → 処理 → 活用の一方向フロー


## コミュニティ補完メモ

- J-10 Machine Learning（J-10）との住み分け：Big Data は「学習データ供給源・規模の概念」を説明し、Machine Learning は「アルゴリズムと学習の仕組み」を扱う。両者は密接だが役割が異なる
- J-41 DX との住み分け：DX はデジタル化の戦略全般を指し、Big Data はその文脈で登場する技術概念の 1 つという位置づけ
- G-15 RAG との連携：Big Data 基盤に蓄積された業務データを RAG の検索対象として活用するユースケースを「どこで出会うか」で言及した

## 出典メモ

- Doug Laney "3D Data Management" META Group (2001) — checked 2026-04-30
- Gartner IT Glossary: Big Data — checked 2026-04-30


## 備考

- 「ビッグデータ」という日本語表記と「Big Data」英語表記が混在するが、本エントリでは英語 ID を採用
- 3V 以外に Veracity（正確性）・Value（価値）を加えた 5V 定義もあるが、最初の 3V に絞って説明した
- 数値閾値がない点（読者のつまずき例）は「どこで出会うか」で軽く触れ、詳細は本備考で補足
