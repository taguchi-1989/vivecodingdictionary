---
id: E-31
title: WebArena
title_reading: ウェブアリーナ
category: benchmark
subtype: agent
experience_level: research_only
reader_level: 2-3
importance: D
figure_type: structure
page_layout: spread_v1
start_date: 2023
version_status: active
pricing_note: none
evaluation_date: 2026-04-30
related_terms:
  - GAIA
  - AgentBench
  - OSWorld
  - Playwright MCP
status: drafting
---

# WebArena

## tagline

Web ブラウザ上で動く AI エージェントの実用度を測るベンチマークです。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

カーネギーメロン大学が 2023 年に発表したベンチマークです。Docker で再現した 5 種の擬似 Web サイトに自然言語タスク 812 個を与え、AI エージェントの完了率を計測します。

## どこで出会うか

ブラウザ操作系エージェント（Operator・Computer Use 等）の性能比較記事で頻出します。「WebArena スコア XX%」という共通指標で各サービスの実用度を横並びに比べる際に使われます。

## メイン図

### 図の狙い

Docker で再現した 5 つの擬似サイトに AI エージェントが挑む構造を示す。

### C. 概念図（figure_type: structure）

- 中心に置く概念: AI エージェント
- 周辺の要素: EC サイト / GitLab 風 / Reddit 風 / 地図 / ホテル予約
- 関係の描き方: エージェントから 5 サイトへ矢印、完了率（%）ラベル付き


## 会話での使い方例

「WebArena のスコアで Operator が頭一つ抜けたらしいですね。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

ブラウザ操作エージェントの完了率を共通スケールで測ります。

### 2. うれしさ

実サイトに近い環境でテストするため、スコアが実用度に直結しやすいです。

### 3. 注意点

Docker のローカル再現環境のため、実本番サービスへの影響はありません。

### 4. どこで役立つか

エージェント選定時に各サービスの実力を横並びで比較できます。

### 5. はじめに

Docker 擬似環境・812 タスク・完了率の 3 点を押さえれば読み解けます。

### 6. 深掘り先

GAIA、AgentBench、OSWorld


## 開発フローでの位置（必須）

1. エージェント選定 — WebArena スコアを他ベンチと並べて候補を絞ります
2. 環境構築 — Docker で 5 種擬似サイトをローカルに立ち上げます
3. タスク実行 — 812 個の自然言語タスクをエージェントに与えます
4. 完了率集計 — 正解判定し、スコアとして記録します
5. 比較・報告 — GAIA や AgentBench と並べて実用度を評価します


## 関連用語

- GAIA
- AgentBench
- OSWorld
- Playwright MCP


<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

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

- 描く内容: AI エージェントのアイコンを中央に置き、5 種の擬似サイトアイコン（カート／コード／吹き出し／地図ピン／ベッド）を周囲に配置。完了率バーを各アイコン下に添える
- 登場人物: 研究者風の人物がエージェントを操作している様子
- 吹き出し・心の声: 「実サイトと同じことをやらせてみます」「Docker だから本番に影響ゼロですよ」
- 中央に置くキーワード/ラベル: WebArena 812 Tasks

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: 比較表・虫眼鏡
- Step 2 のアイコン/絵柄: Docker クジラアイコン
- Step 3 のアイコン/絵柄: ロボットアーム・ブラウザ画面
- Step 4 のアイコン/絵柄: チェックリスト・グラフ棒
- Step 5 のアイコン/絵柄: 横並びスコア表
- 矢印で示す流れの意図: 選定 → 環境構築 → 実行 → 集計 → 比較の 5 段階サイクル


## コミュニティ補完メモ

- GAIA（E-32）との住み分け：GAIA はブラウザ操作に限らない汎用エージェント推論。WebArena はブラウザ GUI 操作に特化した点で異なります
- AgentBench（E-33）との住み分け：AgentBench は DB・OS 操作など複数環境を対象にします。WebArena は Web ブラウザ UI 操作に絞った点が特徴です
- OSWorld（E-34）との住み分け：OSWorld はデスクトップ OS 全体の操作を対象にします。WebArena は Web ブラウザ内のタスクに限定しています
- Operator / Computer Use の比較指標として頻出するため、サービス比較文脈で引用されることが多い

## 出典メモ

- WebArena: A Realistic Web Environment for Building Autonomous Agents（arXiv:2307.13854） — checked 2026-04-30
- webarena.dev — checked 2026-04-30


## 備考

- 公開時（2023 年）の GPT-4 スコアは約 14%。2025 年時点では Claude 3.5 Sonnet・GPT-4o が 20〜30% 台、Operator 系で 40% 台と段階的に向上（evaluation_date:2026-04-30 時点）
- スコアは使用するエージェントの設定・プロンプト戦略・評価バージョンによって変動することがあります
- Docker 擬似環境を使うため「実サイトに繋ぐの？」という読者の疑問に対し、本番影響ゼロである点を強調すると理解が進みます
