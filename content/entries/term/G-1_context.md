---
id: G-1
title: Context（コンテキスト）
category: term_llm
subtype: basic
experience_level: hands_on
reader_level: 2
figure_type: structure
page_layout: spread_v1
version_status: active
evaluation_date: 2026-04-23
related_terms:
  - Context Engineering
  - Context Window
  - System Prompt
  - Token
  - Prompt Engineering
status: needs_review
---

# Context（コンテキスト）

## tagline

日本語では「文脈」。LLM に渡す情報のすべてを指し、質と量で応答が変わります。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

LLM は Context に入っている情報だけを手がかりに応答します。記憶を持たないため、同じ LLM でも Context の中身が違えば応答が変わります。

構成は System Prompt／指示／添付資料／会話履歴／ツール結果の 5 要素です。Context Window は 128K から 100 万トークン超に拡大しましたが、入れすぎると応答が劣化します。

## どこで出会うか

バイブコーディングの核概念です。AI に同じ質問を投げても、「何を、どの順で、どれだけ」Context に並べたかで結果が大きく変わります。

### 膨らみすぎると起きること

Context を膨らませすぎると、ハルシネーション（J-51）が出やすくなったり、応答が薄く・雑になったりします。「全部投げ込めば賢くなる」ではなく、**必要なものを必要な分だけ**が原則です。

### 圧縮とクリア

長いやり取りが続くと、過去の会話を **圧縮**（要約して詰め直す）する仕組みが働くことがあります。ただし圧縮を重ねるうちに情報が歪んでいき、だんだん変な方向に引っ張られることがあります。そういうときは思い切って **新しく会話をクリアして作り直す** のが効くことが多いです。

Claude Code のようなエージェントは、ファイル読み込み・ツール結果・過去の対話を動的に Context に足していきます。「何が入っているか」を意識せずに使うと、手戻りや誤解が起きやすくなります。Context Engineering（G-11）という語が生まれた背景でもあります。

## メイン図

### 図の狙い

LLM を中心に、Context に流れ込む情報源を 5 方向から示します。「Context ≒ 文脈の袋」というイメージを持てるようにします。点線円で Context Window の上限も表します。

### C. 概念図（figure_type: structure）

- 中心に置く概念: LLM（1 回の応答を生成する推論の箱）
- 周辺の要素（5 個）: System Prompt ／ ユーザーの指示 ／ 添付資料（ファイル・画像）／ 会話履歴 ／ ツール結果
- 関係の描き方: 5 本の矢印が中央 LLM に流れ込む。LLM の外側に「Context Window」という点線の円。円の外に出た情報は「見えない」ことを示す。円が小さすぎると入りきらない／大きすぎても中身がぼやける、というバランスを添える

## 関連用語

- Context Engineering — Context 全体の設計技法
- Context Window — Context に入れられる上限（トークン数）
- System Prompt — Context の先頭に置く役割定義
- Token — Context のサイズを数える単位
- Prompt Engineering — 指示テキスト単体の設計術（Context より狭い）

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

LLM に見せる「文脈」の全体です。

### 2. うれしさ

質を上げれば、同じモデルでも応答が変わります（伸びます）。

### 3. 注意点

膨らませすぎると応答が劣化し、圧縮しすぎると情報が歪みます。

### 4. どこで役立つか

指示の精度、長文読解、複数資料を扱う複雑タスク。

### 5. はじめに

System Prompt＋指示＋資料＋履歴の 4 要素と Window 上限の存在。

### 6. 深掘り先

Context Engineering、Prompt Caching、RAG、Memory。

## 開発フローでの位置（必須）

1. 目的を整理 — 何を AI にしてほしいか
2. 必要情報を選ぶ — どの資料・履歴・ツール結果が要るか
3. Context に並べる — System Prompt → 指示 → 資料 → 履歴
4. LLM 実行 → 出力確認 — 不足なら情報を足し、歪んだら会話をクリアして作り直す

<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニア視点のつまずき

-
-
-

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

- 🙂 第一印象:
- 👍 良い点:
- 👎 ダメな点:
- 👥 誰に向くか:

<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: 中央に LLM の箱、周囲に 5 つの材料アイコン（System Prompt、指示、資料、履歴、ツール結果）が矢印で流入。外側に「Context Window」の点線円。円の外に「入り切らなかった情報」を灰色で 1 つ描く。円のそばに「128K → 1M」の矢印（歴史的な拡大）
- 登場人物: 箱の脇に小さく読者キャラクター — 材料を選んで箱に放り込む姿
- 吹き出し・心の声: 「何を、どれだけ入れるか」「多すぎると逆にバカになる」
- 中央に置くキーワード: Context ＝ 文脈の袋
- 追加メモ: 右下に小さく「圧縮しすぎたらクリアして作り直す」の注記

### 6視点アイコン（右ページ上段）

- 共通アイコン流用

### 開発フロー図（右ページ下段）

- Step 1: 目的アイコン（標的）
- Step 2: 選別アイコン（フィルター）
- Step 3: スタックアイコン（並べる）
- Step 4: 実行＋確認アイコン＋クリアボタン（歯車 → チェック → ゴミ箱）
- 矢印: 整理 → 選ぶ → 並べる → 実行・確認・必要ならクリア のループ

## コミュニティ補完メモ

Context Engineering（G-11）、Context Window（G-5）、Hallucination（J-51）は別エントリで深掘りします。本エントリは Context という語の全体像と歴史、膨らませすぎ問題、クリアの判断までをカバーします。

## 出典メモ

- Anthropic docs "Context windows" — checked 2026-04-23
- OpenAI API reference — checked 2026-04-23
- Google "Gemini long context" — checked 2026-04-23

## 備考

「LLM が記憶を持たず、Context がすべて」という前提を明示しています。Memory 機能は別の層として扱います。
