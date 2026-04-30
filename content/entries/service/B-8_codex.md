---
id: B-8
title: Codex
title_reading: コデックス
category: service
subtype: ai_assistant
experience_level: research_only
reader_level: 2-3
importance: B
figure_type: comparison
page_layout: spread_v1
start_date: 2025-05-01
version_status: active
pricing_note: paid
evaluation_date: 2026-04-30
related_terms:
  - OpenAI
  - ChatGPT
  - GitHub Copilot
  - Claude Code
status: drafting
---

# Codex

<!--
バイブコーディング図鑑 エントリー v2（spread_v1 準拠）
-->

## tagline

OpenAI 製のコーディングエージェントです。リポジトリを操作して PR まで作れます。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

ChatGPT 組み込みのクラウド版と、ローカルで動く CLI 版の 2 系統があります。クラウド版はコンテナ上でリポジトリを操作し、コード修正から PR（プルリクエスト）作成まで自動化します。

## どこで出会うか

ChatGPT Pro・Team・Enterprise の画面で「Codex」エージェントとして登場します。GitHub Copilot（B-5）が Microsoft 系、Claude Code（B-7）が Anthropic 系と並ぶ、OpenAI 系の代表格です。

## メイン図

### 図の狙い

Codex のクラウド版と CLI 版の 2 系統と、主要 3 強（Copilot / Claude Code / Codex）の位置関係を並べて示します。

### B. 登場シーン（figure_type: comparison）

- シーン1: ChatGPT 上でユーザーが「このバグを直して PR を出して」と依頼し、Codex がリポジトリを操作する
- シーン2: Codex CLI をターミナルで起動し、ローカルコードに対して修正を依頼する
- シーン3: チームが「Copilot・Claude Code・Codex どれにする？」と選択する比較場面
- 並べる基準: 使う場所（クラウド／ローカル）と比較対象の 2 軸

## 会話での使い方例

「Codex に PR を作らせると、Claude Code とはクセが違いますよね。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

ChatGPT 経由でリポジトリを操作するコーディングエージェントです。

### 2. うれしさ

PR 作成まで自動化でき、コーディング作業を外出しできます。

### 3. 注意点

旧 Codex（2021 年のエンジン）と同名のため、記事の年代に注意が必要です。

### 4. どこで役立つか

単発のバグ修正や小機能追加を ChatGPT から指示したい場面に向いています。

### 5. はじめに

ChatGPT Pro プランで使えるエージェントと、OSS の CLI 版の 2 種類があります。

### 6. 深掘り先

OpenAI（C-1）、ChatGPT（B-3）、Claude Code（B-7）

## 開発フローでの位置（必須）

1. タスク定義 — 「どのバグを直すか」「どの機能を追加するか」を自然言語で整理します
2. Codex に依頼 — ChatGPT 上または CLI でリポジトリを渡して指示を出します
3. 自律実行 — Codex がコンテナ内でコードを読み書きし、修正を進めます
4. PR 確認 — 自動作成された PR を人が確認し、問題なければマージします

## 関連用語

- OpenAI
- ChatGPT
- GitHub Copilot
- Claude Code


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

### メイン図（左ページ中段 / figure_type: comparison）

- 描く内容: 左右 2 列の比較図。左列「クラウド版」（ChatGPT 画面 → Codex コンテナ → GitHub PR）、右列「CLI 版」（ターミナル → ローカルコード）
- 登場人物: 開発者 1 名。画面に向かって指示を打っている姿
- 吹き出し・心の声: 開発者「PR 作って」/ Codex「コンテナ起動中…」/ GitHub「PR が届きました！」
- 中央に置くキーワード/ラベル: Codex ＝ クラウド版 ＋ CLI 版

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: メモ帳アイコン — タスク定義
- Step 2 のアイコン/絵柄: チャット吹き出し — 依頼
- Step 3 のアイコン/絵柄: 歯車ループ — 自律実行
- Step 4 のアイコン/絵柄: PR マージアイコン — 確認・マージ
- 矢印で示す流れの意図: 人が定義 → 機械が実行 → 人が承認という役割分担

## コミュニティ補完メモ

- OpenAI（C-1）との住み分け：OpenAI はサービス提供会社全体。本エントリはその中の Codex に絞ります
- ChatGPT（B-3）との住み分け：ChatGPT は汎用チャット。Codex はその中のコーディング特化エージェント機能を指します
- GitHub Copilot（B-5）との住み分け：Copilot は Microsoft / GitHub 系で補完中心。Codex は OpenAI 系でエージェント型（PR 作成まで）です
- Claude Code（B-7）との住み分け：Claude Code は Anthropic 製の CLI エージェント。Codex は OpenAI 製で ChatGPT 組み込み型が主体です
- 旧 Codex（2021 年）については備考に記載。本エントリは 2025 年再始動版を主に扱います

## 出典メモ

- openai.com/codex — checked 2026-04-30
- github.com/openai/codex — checked 2026-04-30

## 備考

- 旧 Codex（2021 年）は GPT-3 ベースのコード補完モデルで、GitHub Copilot の初期エンジンとして使われた。2023 年に API 提供終了。2025 年 5 月に「Codex」ブランドが再始動し、コーディングエージェントとして再登場した。本エントリは 2025 年版を主に扱う
- 料金は ChatGPT Pro/Team/Enterprise プランに依存。時変情報のため本文への詳細記載は最小限にしています
- CLI 版（codex-cli）はオープンソースで公開されており、API キーを用意すれば無料で試せますが、API 費用は別途発生します
