---
id: G-12
title: Agent Design
title_reading: エージェント デザイン
category: term_llm
subtype: technique
experience_level: research_only
reader_level: 3-5
figure_type: structure
page_layout: spread_v1
start_date:
end_date:
version_status: active
pricing_note: none
evaluation_date: 2026-04-30
related_terms:
  - Tool Use
  - マルチエージェント協調
  - Subagent
  - オーケストレーション
status: drafting
---

# Agent Design

## tagline

LLM が自律的に判断・行動するエージェントを組み立てる設計指針の総称です。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

System Prompt（指示書）・Tool Use（外部操作）・メモリ・プランニングを組み合わせ、LLM（大規模言語モデル）が複数ステップを自律実行できる AI システムの構造を定義します。代表パターンに ReAct や Plan-and-Execute があります。

## どこで出会うか

Claude Code・Cursor・Devin などのコーディングエージェントの裏側で使われている設計思想です。「なぜ AI が自分でコマンドを打てるのか」を理解したいときに、この言葉に行き着くことがあります。

## メイン図

### 図の狙い

「単発の質問応答」と「複数ステップの自律実行」の違いを、処理の流れで示す。

### C. 概念図（figure_type: structure）

- 中心に置く概念: Agent（エージェント）ループ
- 周辺の要素: System Prompt / Tool Use / メモリ / プランニング / 自己評価（Reflexion）
- 関係の描き方: 中央ループから各要素への矢印（入力・出力・フィードバック）


## 会話での使い方例

「Agent Design の ReAct パターンで Claude にツール選択を任せています。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

LLM を単発応答から自律実行システムへ変える設計指針です。

### 2. うれしさ

設計パターンを再利用でき、試行錯誤のコストが下がります。

### 3. 注意点

「Agent」の定義は業界により異なり、強化学習文脈とは別物です。

### 4. どこで役立つか

コーディングエージェントや業務自動化ツールの構築時に役立ちます。

### 5. はじめに

ReAct パターンとツール呼び出しの流れを掴むのが出発点です。

### 6. 深掘り先

Tool Use、オーケストレーション、マルチエージェント協調


## 開発フローでの位置（必須）

1. 目的定義 — 解かせるタスクのスコープと自律度を決めます
2. 設計パターン選択 — ReAct / Plan-and-Execute など用途に合わせて選びます
3. ツール・メモリ設計 — Tool Use と短期・長期メモリの接続を組みます
4. ループ実装 — フレームワーク（LangChain / AutoGen 等）でエージェントループを構築します
5. 評価・改善 — Reflexion 的な自己評価ステップで品質を上げます


## 関連用語

- Tool Use
- マルチエージェント協調
- Subagent
- オーケストレーション


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

- 描く内容: 中央に「エージェントループ」の円形フロー。外側に System Prompt・Tool Use・メモリ・プランニングの 4 要素を配置し、矢印で入力・出力・フィードバックを示す
- 登場人物: 開発者らしい人物が右端でループを眺めている姿
- 吹き出し・心の声: 「自分で判断して動いてる…」「何回もループしてタスクを終わらせてくれる」
- 中央に置くキーワード/ラベル: Agent Loop

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: ターゲット・スコープ定義
- Step 2 のアイコン/絵柄: パターン選択（分岐アイコン）
- Step 3 のアイコン/絵柄: ツール接続（プラグ）
- Step 4 のアイコン/絵柄: ループ実装（歯車）
- Step 5 のアイコン/絵柄: 評価・フィードバック（矢印サイクル）
- 矢印で示す流れの意図: 設計から実装・改善へと繰り返すサイクルを表す


## コミュニティ補完メモ

- G-30 Tool Use との住み分け：Tool Use は「LLM がツールを呼ぶ仕組み」の 1 要素。Agent Design はその Tool Use を含む設計全体の話。
- G-41 Subagent との住み分け：Subagent はマルチエージェント構成での下位エージェントの呼称。Agent Design はシングル・マルチ両方の設計を含む上位概念。
- G-44 マルチエージェント協調との住み分け：協調パターン（Multi-Agent Debate 等）は Agent Design の 1 サブカテゴリとして位置づける。
- 強化学習エージェントとの混同注意：本書では「LLM ベースで自律実行する AI システム」に限定して使用する。


## 出典メモ

- Anthropic: Building effective agents — <https://www.anthropic.com/engineering/building-effective-agents> — checked 2026-04-30
- ReAct: Synergizing Reasoning and Acting in Language Models (Yao et al., 2022) — <https://arxiv.org/abs/2210.03629> — checked 2026-04-30
- Reflexion (Shinn et al., 2023) — <https://arxiv.org/abs/2303.11366> — checked 2026-04-30

## 備考

- 本エントリは「Agent Design」という設計指針の総称を扱う。特定フレームワーク（LangChain 等）の詳細は別エントリへ逃がす。
- evaluation_date は 2026-04-30 時点。フレームワーク名やパターン名は今後追加されることがあります。
