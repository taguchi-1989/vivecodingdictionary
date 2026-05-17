---
id: G-1
title: Context
title_reading: コンテキスト
category: term_llm
subtype: basic
experience_level: hands_on
reader_level: 2
importance: B
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
status: ready
---

# Context

## tagline

日本語では「文脈」。LLM に渡す情報のすべてを指し、質と量で応答が変わります。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

LLM は Context に入っている情報だけを手がかりに応答します。System Prompt／指示／添付資料／会話履歴／ツール結果の 5 要素で構成され、入れすぎても少なすぎても応答が劣化します。

## どこで出会うか

バイブコーディングの核概念です。AI に同じ質問を投げても「何を、どの順で、どれだけ」並べたかで結果が大きく変わります。「必要なものを必要な分だけ」が原則です。

## メイン図

### 図の狙い

LLM を中心に、Context に流れ込む情報源を 5 方向から示します。「Context ≒ 文脈の袋」というイメージを持てるようにします。点線円で Context Window の上限も表します。

### C. 概念図（figure_type: structure）

- 中心に置く概念: LLM（1 回の応答を生成する推論の箱）
- 周辺の要素（5 個）: System Prompt ／ ユーザーの指示 ／ 添付資料（ファイル・画像）／ 会話履歴 ／ ツール結果
- 関係の描き方: 5 本の矢印が中央 LLM に流れ込む。LLM の外側に「Context Window」という点線の円。円の外に出た情報は「見えない」ことを示す。円が小さすぎると入りきらない／大きすぎても中身がぼやける、というバランスを添える

## 会話での使い方例

「いま LLM の焦点は Context をどう設計するかで、量より中身が効くんですよね。」

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
## 関連用語

- Context Engineering
- Context Window
- System Prompt
- Token

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- 「コンテキスト」は日常語と距離があり、「文脈」と言ってくれた方が伝わりやすいと感じます。
- 入れすぎても少なすぎても劣化すると言われますが、ちょうどよい量の感覚が掴めません。
- 会話が長くなると重要な情報が勝手に圧縮・消去されることがあります。
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象:
- 👍 良い点:
- 👎 ダメな点:
- 👥 誰向けか:
<!-- user-input:end key="my_comment" -->

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

Context Engineering（G-11）、Context Window（G-5）、Hallucination（J-51）は別エントリで深掘りします。本エントリは「Context という語そのもの」に絞り、運用テクニック（圧縮／クリア／動的追加）は G-11 へ送ります。

### 本エントリから G-11 等へ移した素材（旧「どこで出会うか」より）

- **膨らみすぎると起きること** — Context を膨らませすぎるとハルシネーション（J-51）が出やすくなり、応答が薄く・雑になる。「全部投げ込めば賢くなる」ではなく必要なものを必要なぶんだけ
- **圧縮とクリア** — 長い会話は自動的に圧縮（要約して詰め直す）されることがある。圧縮を重ねるうちに情報が歪むので、思い切って新しい会話にクリアして作り直すのが効く
- **動的な Context** — Claude Code のようなエージェントは、ファイル読み込み・ツール結果・過去の対話を動的に Context に足していく。「何が入っているか」を意識せずに使うと手戻りが起きる。Context Engineering（G-11）という語が生まれた背景

## 出典メモ

- Anthropic docs "Context windows" — checked 2026-04-23
- OpenAI API reference — checked 2026-04-23
- Google "Gemini long context" — checked 2026-04-23

## 備考

「LLM が記憶を持たず、Context がすべて」という前提を明示しています。Memory 機能は別の層として扱います。
