---
id: G-41
title: Subagent
title_reading: サブエージェント
category: term_llm
subtype: ops
experience_level: hands_on
reader_level: 4
importance: D
figure_type: structure
page_layout: spread_v1
start_date:
end_date:
version_status: active
pricing_note: none
evaluation_date: 2026-04-29
related_terms:
  - Claude Code
  - Hook
  - Slash Command
  - Worktree
  - マルチエージェント
status: needs_review
---

# Subagent

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## tagline

親が呼び出す役割特化の子エージェントです。独立した Context（コンテキスト）で動き親を汚しません。

## 何をしてくれるか

`.claude/agents/<名前>.md` にシステムプロンプトを書くと、親エージェントが Agent ツールでそのサブエージェントを呼び出せます。結果だけを親に返す仕組みなので、親の Context を汚さずにタスクを分担できます。

## どこで出会うか

Claude Code（略称 CC）を使った開発で「レビュー担当」「執筆担当」のように役割を分けたいときに登場します。並列・直列どちらの呼び出しにも対応しています。

## メイン図

### 図の狙い

親エージェントがサブエージェントを呼び出し、独立した Context で動いた後に結果を返す流れを示す。

### C. 概念図（figure_type: structure）

- 中心に置く概念: 親エージェント → サブエージェント呼び出し（Agent ツール）→ 独立 Context で作業 → 結果を返す
- 周辺の要素: `.claude/agents/<name>.md`（定義ファイル）／独立 Context（親を汚さない）／並列・直列呼び出し
- 関係の描き方: 左から右へ矢印。親エージェントの箱の下にサブエージェントの箱を並べ、矢印で「呼び出し」と「返却」を示す

## 会話での使い方例

「CC のレビューと執筆は Subagent で分けると Context が干渉しにくいです。」

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

親エージェントから呼ばれ、役割特化のタスクを独立 Context で担います。

### 2. うれしさ

親の Context を汚さずに並列・直列でタスクを捌けます。

### 3. 注意点

定義ファイルが増えると管理が煩雑になることがあります。

### 4. どこで役立つか

レビュー・執筆・テストのように役割を分けた自動化で効果的です。

### 5. はじめに

定義ファイルの置き場所と Agent ツールでの呼び出し方が基本です。

### 6. 深掘り先

Hook、Slash Command、マルチエージェント

## 開発フローでの位置（必須）

1. 役割を決める — 「reviewer」「writer」など担当機能を絞る
2. 定義ファイルを作る — `.claude/agents/<name>.md` にプロンプトと使用ツールを書く
3. 親から呼び出す — Agent ツールで名前と指示を渡す
4. 独立 Context で実行 — 作業し、結果を親に返す
5. 必要に応じ並列化 — 複数を同時起動して分担する

## 関連用語

- Claude Code
- Hook
- Slash Command
- Worktree
- マルチエージェント

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

- 描く内容: 左に「親エージェント」の人物が Agent ツールのボタンを押す図。右側に「Subagent（entry-writer）」の人物が独立した吹き出し枠の中で作業している。枠の外と中で Context が分離していることを点線の境界で示す。結果が矢印で親に戻る
- 登場人物: 親エージェント役の人物（画面を操作中）／サブエージェント役の人物（独立した空間で執筆中）
- 吹き出し・心の声: 親「entry-writer、G-41 を書いて」／子「了解、独立 Context で書きます」
- 中央に置くキーワード/ラベル: 独立 Context で動く

### 6視点アイコン（右ページ上段）

- 共通アイコン流用

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: 付箋に「役割」を書く人
- Step 2 のアイコン/絵柄: ファイルにシステムプロンプトを書く人
- Step 3 のアイコン/絵柄: 親エージェントが呼び出しボタンを押す人
- Step 4 のアイコン/絵柄: サブエージェントが独立した箱の中で作業する人
- Step 5 のアイコン/絵柄: 複数のサブエージェントが並んで同時に作業する人たち
- 矢印で示す流れの意図: 「設計 → 定義 → 呼び出し → 実行 → 並列化」の流れ

## コミュニティ補完メモ

- Hook（G-31）との住み分け：Hook はツール実行のタイミングで自動発火するスクリプト。Subagent は明示的に Agent ツールで呼ぶ独立エージェント。どちらも CC の自動化機能だが制御のタイミングが異なる
- Slash Command（G-32）との住み分け：Slash Command はチャット欄でユーザーが手動で起動するショートカット。Subagent はエージェントが自律的に別エージェントを呼ぶ仕組み
- Worktree（G-42）との住み分け：Worktree は Git の複数ブランチを同時展開する機能。Subagent と組み合わせると並列作業の効果がさらに高まる
- マルチエージェント協調（J-44）との住み分け：Subagent は Claude Code における具体的な実装手段の 1 つ。J-44 はより広い概念としてのマルチエージェント協調を扱う
- 本書プロジェクト自身が `.claude/agents/entry-writer.md` を持ち、本エントリの執筆にも Subagent を使っている（自己言及）

## 出典メモ

- docs.anthropic.com/en/docs/claude-code/sub-agents — checked 2026-04-29

## 備考

- Subagent は Claude Code 固有の機能名称。他のエージェントフレームワークでは「ツール呼び出し」「エージェント委譲」などと呼ばれることがある
- 並列実行時は各サブエージェントが独立した Context を持つため、Context Window を節約しながら複数タスクをこなせる
- 定義ファイル（`.claude/agents/<name>.md`）には `description` フィールドを書くことで、親エージェントがどのサブエージェントを呼ぶべきかを判断しやすくなる
