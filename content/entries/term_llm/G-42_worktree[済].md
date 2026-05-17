---
id: G-42
title: Worktree
title_reading: ワークツリー
category: term_llm
subtype: ops
experience_level: partial
reader_level: 3
importance: D
figure_type: structure
page_layout: spread_v1
start_date:
end_date:
version_status: active
pricing_note: none
evaluation_date: 2026-04-29
related_terms:
  - git
  - branch
  - Subagent
  - 並列実行
  - Claude Code
status: ready
---

# Worktree

## tagline

同じリポジトリのブランチを別ディレクトリで並列展開できる git の仕組みです。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

1 つのリポジトリに複数の作業ディレクトリを作り、ブランチを切り替えずに並列で作業できます。AI エージェントが複数タスクを同時進行するときもファイル衝突を防ぎます。

## どこで出会うか

Claude Code で「複数の機能を同時に開発したい」「Subagent（サブエージェント）を並行して動かしたい」という場面で登場します。並列実行を支える土台の一つです。

## メイン図

### 図の狙い

1 つのリポジトリから複数の Worktree が枝分かれし、AI エージェントがそれぞれ別の作業を同時進行している構造を示します。

### C. 概念図（figure_type: structure）

- 中心に置く概念: リポジトリ（1 つの .git）
- 周辺の要素: worktree-A（feature/login）、worktree-B（feature/payment）、worktree-C（hotfix/bug）、Subagent A・B・C
- 関係の描き方: 中心から矢印で各 worktree へ放射、各 worktree に AI キャラクターが座っている

## 会話での使い方例

「Worktree を使えば、Subagent 同士がブランチを取り合わずに並列で動けますよ。」

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

同一リポジトリで複数ブランチを並列展開する仕組みです。

### 2. うれしさ

AI が複数タスクを同時進行でき、衝突しません。

### 3. 注意点

Worktree の数が増えるとディスクと管理コストが増えます。

### 4. どこで役立つか

並列 AI 開発や大規模マルチエージェント構成で役立ちます。

### 5. はじめに

`git worktree add` コマンドと branch の関係を掴みます。

### 6. 深掘り先

branch、Subagent、並列実行、Claude Code。

## 開発フローでの位置（必須）

1. リポジトリ準備 — git リポジトリとブランチを用意します
2. Worktree 作成 — `git worktree add` でブランチを別ディレクトリに展開します
3. 並列作業 — 各 Worktree で AI エージェントが独立して作業します
4. マージ — 各ブランチの成果を main へ取り込みます
5. Worktree 削除 — 不要になったら `git worktree remove` で片付けます

## 関連用語

- git
- branch
- Subagent
- 並列実行
- Claude Code

<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- 1 人作業だと必要性を感じにくく、並列実行が必要になって初めて意味が見えます。
- 複数並行中にどこで作業していたか忘れてマージし損ねることがあります。
-
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: 衝突しないのが良い。以前衝突した経験があるので助かります。
- 👍 良い点: タスクベースで切れるところ。
- 👎 ダメな点: どの粒度で切るか、課題管理をどうするかが難しいです。
- 👥 誰向けか: コーディングの効率を上げたい人、チームで開発する人向け。
<!-- user-input:end key="my_comment" -->


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: 中心に 1 つの「リポジトリ（.git）」ボックスを置き、放射状に worktree-A / B / C の 3 ディレクトリへ矢印を引く。各ディレクトリには小さな AI キャラクターが座り、それぞれ別作業中
- 登場人物: AI エージェントを擬人化した小キャラクター 3 体（色違い）
- 吹き出し・心の声: worktree-A「feature/login を開発中」/ worktree-B「feature/payment を開発中」/ worktree-C「hotfix を修正中」
- 中央キーワード: Worktree ＝ 並列実行の土台

### 6視点アイコン（右ページ上段）

- 共通アイコン流用

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: リポジトリアイコン
- Step 2 のアイコン/絵柄: フォルダ＋プラスアイコン
- Step 3 のアイコン/絵柄: AI キャラクター 3 体が横並びで作業中
- Step 4 のアイコン/絵柄: マージ矢印（合流）
- Step 5 のアイコン/絵柄: ゴミ箱アイコン（クリーンアップ）
- 矢印で示す流れの意図: 準備 → 展開 → 並列作業 → 統合 → 後片付け のループ

## コミュニティ補完メモ

- F-50 git との住み分け: F-50 は git 全体（コミット・差分・履歴）を扱い、G-42 は「Worktree で並列展開する AI 開発の土台」に絞る
- G-41 Subagent との住み分け: G-41 は「複数の AI エージェントを起動する仕組み」を扱い、G-42 はそのエージェントが衝突しないためのディレクトリ基盤側を扱う
- branch（F-53）との住み分け: branch は分岐の概念、worktree はその branch を物理的に別ディレクトリで実体化する手段

## 出典メモ

- git-scm.com/docs/git-worktree — checked 2026-04-29
- Claude Code ドキュメント（worktree 統合）— checked 2026-04-29

## 備考

Worktree は git 2.5（2015 年）から使えますが、AI エージェントの並列実行（Subagent / background task）の普及で 2024〜2025 年ごろから注目が高まった機能です。複数 AI が同じファイルを同時に編集する衝突を防ぐ手段として、Claude Code など AI ネイティブ環境が推奨するパターンになっています。
