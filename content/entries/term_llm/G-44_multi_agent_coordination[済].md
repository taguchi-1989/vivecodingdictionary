---
id: G-44
title: マルチエージェント協調
category: term_llm
subtype: ops
experience_level: research_only
reader_level: 4-5
importance: E
figure_type: structure
page_layout: spread_v1
start_date:
end_date:
version_status:
pricing_note:
evaluation_date: 2026-04-30
related_terms:
  - Subagent
  - オーケストレーション
  - Tool Use
  - MCP
  - AutoGen
status: ready
---

# マルチエージェント協調


<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## tagline

複数 AI エージェントが役割を分担し、出力を受け渡しながらタスクを進める構成です。


## 何をしてくれるか

planner（計画役）・executor（実行役）・reviewer（レビュー役）のように役割を分けた複数エージェントが協調して動きます。1 体では context が不足する大きなタスクや、専門的な工程に向きます。


## どこで出会うか

AutoGen や CrewAI などのフレームワーク、Claude Code の Subagent 機能を使った設計記事で目にします。「エージェントが別のエージェントを呼ぶ」構成として紹介されます。


## メイン図

### 図の狙い

planner → executor → reviewer の 3 役が出力をバケツリレーで渡す様子を示し、1 体完結との違いを掴んでもらう。

### C. 概念図（figure_type: structure）

- 中心に置く概念: エージェント間の出力受け渡し（矢印フロー）
- 周辺の要素: planner / executor / reviewer / タスク入力 / 最終出力
- 関係の描き方: 左から右へ順に矢印でつなぐ。各エージェントの吹き出しに役割ラベルを付ける


## 会話での使い方例

「マルチエージェント協調にすると Subagent がレビュー役を担えるので品質が上がります。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

複数エージェントで分業し、大規模タスクを完遂します。

### 2. うれしさ

context 制限を分散し、専門性の高い工程を並列化できます。

### 3. 注意点

通信コストとレイテンシが増え、無限ループに陥ることがあります。

### 4. どこで役立つか

コード生成・レビュー・テストを自動で回したい場面に向きます。

### 5. はじめに

Subagent とオーケストレーションの概念を先に理解しておくと入りやすいです。

### 6. 深掘り先

Subagent、オーケストレーション、AutoGen


## 開発フローでの位置（必須）

1. タスク分解 — オーケストレーターがタスクを役割別に割り当てます
2. planner 起動 — 計画エージェントが手順を生成して渡します
3. executor 起動 — 実行エージェントが各ステップを処理します
4. reviewer 起動 — レビューエージェントが出力を検証して差し戻します
5. 結果統合 — オーケストレーターが最終成果物をまとめます


## 関連用語

- Subagent
- オーケストレーション
- Tool Use
- MCP
- AutoGen


<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- 役割を分けるのは人間の組織と同じ発想で、AI でもうまく機能するのが面白いです。
- Anthropic 等のブログを追いかけないと自分では発想できないのが大変です。
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: 言葉自体は今回初めて聞いた。
- 👍 良い点: 実装の精度を上げられる。役割を定義しておけば、毎回バグ修正の指示を出さずに済む。
- 👎 ダメな点: 「こういう使い方をするといい」と知ること自体が一番のハードルになりそう。
- 👥 誰向けか: 品質の高いコードを一発で生成したい人向け。
<!-- user-input:end key="my_comment" -->


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: 3 人の人物（planner・executor・reviewer）が左から右に並び、矢印で出力を手渡しする様子
- 登場人物: 帽子付き計画担当（planner）／パソコン前の実行担当（executor）／虫眼鏡持ちのレビュー担当（reviewer）
- 吹き出し・心の声: planner「次はこの順でやります」→ executor「実行しました」→ reviewer「ここ直してください」
- 中央に置くキーワード/ラベル: 「役割分担フロー」

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: タスクを切り分ける手のひら
- Step 2 のアイコン/絵柄: ノートを持つ人（計画）
- Step 3 のアイコン/絵柄: 歯車を回す人（実行）
- Step 4 のアイコン/絵柄: チェックリストを持つ人（レビュー）
- Step 5 のアイコン/絵柄: 完成ボックスにまとめる人


## コミュニティ補完メモ

- G-41 Subagent との住み分け：Subagent は「1 エージェントが別エージェントを呼ぶ仕組み」の単体説明。G-44 はその仕組みを使った「複数エージェントによる協調パターン全体」を扱う
- G-43 オーケストレーションとの住み分け：G-43 は「エージェントを束ねる調停役の仕組み」。G-44 はその仕組みを含む協調構成全体のパターン名
- G-30 Tool Use との住み分け：G-30 は「エージェントが外部ツールを呼ぶ」単体機能。G-44 はエージェント間の連携パターン


## 出典メモ

- Anthropic Multi-Agent Research (2025) — https://www.anthropic.com/research/building-effective-agents — checked 2026-04-30
- Microsoft AutoGen — https://microsoft.github.io/autogen/ — checked 2026-04-30
- CrewAI — https://www.crewai.com/ — checked 2026-04-30


## 備考

- 通信コストとレイテンシの増加は設計段階で織り込む必要があります。各エージェント間の呼び出し回数が増えると API コストも比例して上がる点に注意してください
- 「互いに無限ループ」のリスクは、ループ上限やタイムアウトをオーケストレーター側で設定することで対処するのが一般的です
