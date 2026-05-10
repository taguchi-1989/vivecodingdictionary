---
id: J-17
title: Attention
title_reading: アテンション
category: term_general
subtype: ml_basic
experience_level: research_only
reader_level: 3
importance: C
figure_type: structure
page_layout: spread_v1
start_date:
end_date:
version_status:
pricing_note:
evaluation_date: 2026-04-29
related_terms:
  - Transformer
  - LLM
  - Self-Attention
  - Deep Learning
  - エンコーダー
status: ready
---

# Attention

## tagline

Transformer の核。入力のどの単語に注目するかを重みで計算する仕組みです。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

文中の各単語が、他のどの単語と関係が深いかを数値の重みで表します。Query（問い合わせ）・Key（索引）・Value（値）の 3 要素を掛け合わせて計算し、重要な単語ほど強く参照します。

## どこで出会うか

AI モデルの解説記事で「Self-Attention」「Multi-Head Attention」の形で目にします。ChatGPT や Claude が長い文脈を掴めるのも、この機構が並列計算で文全体を一度に処理するためです。

## メイン図

### 図の狙い

「ある単語が文中の他の単語にどれだけ注目するか」を矢印の太さで視覚化し、Attention の直感を掴んでもらいます。

### C. 概念図（figure_type: structure）

- 中心に置く概念: Attention（注意機構）
- 周辺の要素: Query・Key・Value の 3 ベクトル、重みの矢印、入力トークン列
- 関係の描き方: 各トークンから Query/Key の掛け合わせで重みが生まれ、Value を加重合計する流れ

## 会話での使い方例

「Attention が文脈の鍵で、Query と Key の組み合わせで重みが変わるんですよね。」

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

文中の単語どうしの関係強度を数値の重みで計算します。

### 2. うれしさ

全単語を並列処理できるため、長い文脈も落とさず扱えます。

### 3. 注意点

仕組みの詳細より「何に注目するか」の概念把握が先決です。

### 4. どこで役立つか

LLM の動作原理を理解したいときの最初の足がかりになります。

### 5. はじめに

Query・Key・Value の 3 語と「重みで参照する」イメージで十分です。

### 6. 深掘り先

Transformer（J-13）、LLM（J-14）、Deep Learning（J-11）

## 開発フローでの位置（必須）

1. 入力のトークン化 — 文章を単語単位のトークンに分割します。
2. Attention の計算 — Query・Key・Value で各トークンの関係強度を計算します。
3. 重みづけ集約 — 重要度に応じて Value を加重合計し、文脈を反映した表現を得ます。
4. 多層スタック — Attention 層を重ねて深い文脈理解を積み上げます。
5. 出力生成 — 文脈ベクトルをもとに次トークンを予測します。

## 関連用語

- Transformer
- LLM
- Self-Attention
- Deep Learning
- エンコーダー

<!-- ━━━━━━━━ 著者記入欄（右ページ下段に印刷される／AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

- 馴染みは薄いものの、詳しい人と話していると不意に出てきて躓きやすい言葉です。「アテンションエコノミー」のような別文脈の Attention とも混同しやすいです

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

- 🙂 第一印象: Transformer の文脈で初めて目にした言葉です
- 👍 良い点: ここを押さえると、現代 LLM の原理原則を一段深く理解できる感覚があります
- 👎 ダメな点: Attention だけを理解しても、現行モデルのすごさをすべて説明できるわけではありません
- 👥 誰向けか: 原理原則を腰を据えて理解したい人にとって、必ず通る用語です

<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: 「今日の天気は？」という文の各単語が横一列に並び、「天気」という単語から他の単語へ矢印が伸び、「今日」と「は」には細い矢印、「天気」自身と「？」には太い矢印が向かう構図。矢印の太さが Attention の重みを表す。
- 登場人物: 非エンジニアの人物が図を見ながら「どの単語に注目しているの？」と疑問を持つシーン
- 吹き出し・心の声: 人物「矢印が太いほど注目してるんだ」、太い矢印のそばに「重み大」ラベル
- 中央に置くキーワード/ラベル: Attention（注意機構）

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: テキスト分割アイコン（トークン化）
- Step 2 のアイコン/絵柄: Q・K・V の 3 つのブロックアイコン（Attention 計算）
- Step 3 のアイコン/絵柄: 加重合計の天秤アイコン（重みづけ集約）
- Step 4 のアイコン/絵柄: 積み上げ層アイコン（多層スタック）
- Step 5 のアイコン/絵柄: 出力テキストアイコン（出力生成）
- 矢印で示す流れの意図: 入力 → 計算 → 集約 → 深化 → 出力という Attention の処理順

## コミュニティ補完メモ

- Transformer（J-13）との住み分け：J-13 は Transformer アーキテクチャ全体（Encoder/Decoder の構造・歴史的意義）を扱う。J-17 は Attention 機構そのもの（Q/K/V の計算方法・重みの概念）に絞る。
- Self-Attention / Multi-Head Attention などの変種：本エントリでは概念紹介に留め、詳細は「深掘り先」でJ-13へ誘導する。
- 元祖は Bahdanau Attention（2015年、機械翻訳向け）で、2017年「Attention Is All You Need」で現在の形に確立された経緯は備考に記す。

## 出典メモ

- Vaswani et al., "Attention Is All You Need", arXiv:1706.03762 (2017) — checked 2026-04-29
- Jay Alammar, "The Illustrated Transformer", jalammar.github.io — checked 2026-04-29
- Bahdanau et al., "Neural Machine Translation by Jointly Learning to Align and Translate", arXiv:1409.0473 (2015) — checked 2026-04-29

## 備考

- Attention は固有語のため略称展開なし。Query・Key・Value は初出で日本語訳（問い合わせ・索引・値）を括弧で補った。
- Self-Attention（自己注意機構）・Multi-Head Attention（多頭注意機構）は変種として言及するに留め、詳細は別エントリへ回す。
- 数式（softmax(QK^T/√d_k)V 等）は非エンジニア向けのため省略。「重みで参照する」という概念のみ記述。
- 元祖の Bahdanau Attention（2015）から 2017 年論文で「Self-Attention のみ」の構造へ進化した点は、深掘り関心層向けに出典メモに記す。
