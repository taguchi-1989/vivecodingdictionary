---
id: E-2
title: SWE-Bench Verified
title_reading: スウィーベンチベリファイド
category: benchmark
subtype: coding
experience_level: research_only
reader_level: 2
importance: C
figure_type: structure
page_layout: spread_v1
start_date: 2024
version_status: active
evaluation_date: 2026-04-29
related_terms:
  - SWE-Bench
  - HumanEval
  - Chatbot Arena
  - Claude Code
status: ready
---

# SWE-Bench Verified

## tagline

SWE-Bench の中から人手で検証した 500 問のサブセットです。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

OpenAI が SWE-Bench 全体の問題を人手で精査し、解答可能と確認した 500 問だけを抜き出したものです。不正解の原因が「AI の実力不足」なのか「問題設定の曖昧さ」なのかを切り分けられます。

## どこで出会うか

新モデルの発表資料で「SWE-Bench Verified で XX%」という形で出てきます。元の全件セットより信頼性が高いため、各社が比較に使う場面が増えています。

## メイン図

### 図の狙い

SWE-Bench 全体から Verified サブセットへの絞り込みの構造と、絞り込むことで何が嬉しいかを 1 枚で見せます。

### C. 概念図（figure_type: structure）

- 中心に置く概念: SWE-Bench（全件）→ 人手検証 → Verified（500 問）
- 周辺の要素（3〜6 個）: 全件数（2294 問）／人手レビュアー／確認済み問題／除外された曖昧問題／スコア
- 関係の描き方: 大きな円（全件）の中に小さな円（Verified）を包含で描く。人手レビュアーの人物アイコンが橋渡しする


## 会話での使い方例

「比較するなら SWE-Bench Verified の数字が信頼性は高いです。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

SWE-Bench から問題品質を人手で担保した 500 問のサブセットです。

### 2. うれしさ

問題の曖昧さに左右されず、AI の実力を比べやすくなります。

### 3. 注意点

500 問は全件の約 22% であり、分野の偏りが残ることがあります。

### 4. どこで役立つか

モデル選定時に複数サービスのスコアを横並びで比べる場面で使えます。

### 5. はじめに

元の SWE-Bench との関係と「人手検証」の意味を押さえると読めます。

### 6. 深掘り先

SWE-Bench、Multi-SWE-Bench、HumanEval

## 開発フローでの位置（必須）

1. 新モデル発表を確認 — Verified スコアが提示されているか見る
2. スコアの前提を把握 — Verified か全件かで信頼性が変わります
3. 他モデルと横比較 — 同じ Verified 条件なら数字を並べやすいです
4. 採用判断の補助資料にする — 体感や別指標と合わせて判断します


## 関連用語

- SWE-Bench
- HumanEval
- Chatbot Arena
- Claude Code


<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

-★sweベンチも？？なのにVerifyって何となる？
-何が測れるかよくわからない
-

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

- 🙂 第一印象:sweベンチの親戚的な感じ。
- 👍 良い点:正しい評価ができる？？
- 👎 ダメな点:既に飽和しかけている??
- 👥 誰向けか:モデルの賢さををざっと判断したい人向け


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: 大きな円（SWE-Bench 全 2294 問）の内側に小さな円（Verified 500 問）を包含で配置。人手レビュアーの人物アイコンが大円から小円へふるいをかける動作を示す
- 登場人物: 人手レビュアー 1 名（ふるいを持ったシンプルなアイコン）
- 吹き出し・心の声: 「これは解けるはず、これは曖昧だから除外」
- 中央に置くキーワード/ラベル: 「人手検証」「500 問」「信頼性 UP」

### 6視点アイコン（右ページ上段）

- 共通アイコン流用

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: 発表スライドのアイコン（新モデル発表）
- Step 2 のアイコン/絵柄: 虫眼鏡（スコアの前提確認）
- Step 3 のアイコン/絵柄: 比較表（横並び比較）
- Step 4 のアイコン/絵柄: チェックと天秤（採用判断）
- 矢印で示す流れの意図: 発表 → 確認 → 比較 → 判断


## コミュニティ補完メモ

- SWE-Bench（E-1）との住み分け：親エントリ E-1 が「SWE-Bench とは何か・80 点帯での頭打ち」を担う。本エントリ E-2 は「Verified という絞り込みの意味と信頼性向上」に集中する
- SWE-Bench Lite 等の派生は別エントリ扱い。本エントリでは触れない
- Chatbot Arena（E-50）との住み分け：Arena は主観評価（人間投票）、Verified は客観タスク（コード修正）という対比で参照し合う関係


## 出典メモ

- openai.com "SWE-Bench Verified" ブログ — checked 2026-04-29
- swebench.com — checked 2026-04-29


## 備考

SWE-Bench Verified は 2024 年に OpenAI が提案・公開したサブセット。問題数は 500 問（全 2294 問の約 22%）。採点基準や設定は E-1 SWE-Bench の内容を参照のこと。
