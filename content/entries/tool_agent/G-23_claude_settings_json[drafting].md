---
id: G-23
title: .claude/settings.json
title_reading: ドット クロード スラッシュ セッティングス ドット ジェイソン
category: tool_agent
subtype: config_file
experience_level: hands_on
reader_level: 3-4
importance: C
figure_type: structure
page_layout: spread_v1
start_date:
end_date:
version_status: active
pricing_note: none
evaluation_date: 2026-04-30
related_terms:
  - Claude Code
  - CLAUDE.md
  - Hook
  - Permission
status: drafting
---

<!--
バイブコーディング図鑑 エントリー雛形 v2（2ページ見開き想定、iter 22 準拠）
-->

## tagline

Claude Code のプロジェクト用設定ファイルで、Hook や Permission をリポジトリ単位で揃えられます。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

`.claude/` に置くだけで、Bash 許可リストや保存時 Hook を Claude Code に読み込ませられます。同僚も同じ設定でリポジトリを開けるので動作が揃います。

## どこで出会うか

Claude Code を使い始めると、リポジトリ直下に `.claude/` が現れるか自分で作るよう案内されます。Hook を入れたい、または Bash 許可範囲をプロジェクトごとに変えたいときに編集します。

## メイン図

### 図の狙い

グローバル設定（`~/.claude/settings.json`）とプロジェクト設定（`.claude/settings.json`）の優先順位と、主要キーの対応を示します。

### C. 概念図（figure_type: structure）

- 中心に置く概念: `.claude/settings.json`（プロジェクト設定）
- 周辺の要素: `~/.claude/settings.json`（グローバル設定）／`permissions`（許可・拒否ルール）／`hooks`（PreToolUse・PostToolUse）／`env`（環境変数）／`.claude/settings.local.json`（個人上書き）
- 関係の描き方: プロジェクト設定がグローバル設定を上書きする矢印。`settings.local.json` はさらに上位で個人のみ有効（git 管理外）


## 会話での使い方例

「`.claude/settings.json` の Hook で保存時 validator を走らせます。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

プロジェクト単位で Claude Code の動作ルールを定義するファイルです。

### 2. うれしさ

Hook や Permission をリポジトリに含めることでチーム全員の設定が揃います。

### 3. 注意点

グローバル・プロジェクト・ローカルの 3 層があり、優先順位の把握が必要です。

### 4. どこで役立つか

複数人開発で validator や lint を保存時に必ず実行させたい場面で役立ちます。

### 5. はじめに

プロジェクト設定がグローバル設定を上書きする優先順位だけ押さえれば始められます。

### 6. 深掘り先

Hook、Permission、CLAUDE.md

## 開発フローでの位置（必須）

1. 準備 — プロジェクト直下に `.claude/` を作ります。
2. 設定記述 — `settings.json` に `permissions` / `hooks` を書きます。
3. Hook 登録 — `PostToolUse` に validator を指定します。
4. 個人上書き — 個人設定は `settings.local.json` に分けます。
5. 共有 — `settings.json` をコミットして共有します。


## 関連用語

- Claude Code
- CLAUDE.md
- Hook
- Permission

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

- 描く内容: グローバル設定とプロジェクト設定が重なる層構造。プロジェクト設定が上に乗っているイメージ
- 登場人物: チームメンバーのアイコン（2〜3 人）がリポジトリを共有している場面
- 吹き出し・心の声: 「あれ、私だけ設定が違う…」→「`.claude/settings.json` にまとめたら揃いました！」
- 中央に置くキーワード/ラベル: `.claude/settings.json`
- Before / After の場合の対比ポイント: —

### 6視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: フォルダ作成アイコン
- Step 2 のアイコン/絵柄: JSON ファイル編集アイコン
- Step 3 のアイコン/絵柄: Hook（矢印 + スクリプト）アイコン
- Step 4 のアイコン/絵柄: 個人用設定ファイル（鍵マーク付き）
- Step 5 のアイコン/絵柄: git コミット → チームへの共有矢印
- 矢印で示す流れの意図: 設定が個人からチーム全体へ広がる流れ

## コミュニティ補完メモ

- CLAUDE.md（G-20）との住み分け：CLAUDE.md はプロジェクトの指示書（AI へのルール文章）、`.claude/settings.json` は Claude Code の動作設定（JSON 形式の機械設定）。両者はセットで使うが役割は別。
- Hook（G-31）との住み分け：Hook の概念説明は G-31 で行い、本エントリは `settings.json` の中で Hook をどう書くかという実装視点を担う。
- Permission（G-39）との住み分け：Permission の概念は G-39 で説明し、本エントリは `settings.json` 内の `permissions` キーの設定方法を扱う。
- `.cursor/settings.json` など他ツールへの言及：競合ツールにも類似の仕組みがある点は備考に留める。


## 出典メモ

- Anthropic Claude Code 公式ドキュメント — checked 2026-04-30


## 備考

- `settings.local.json` はプロジェクト設定をさらに個人だけで上書きするファイル。git の `.gitignore` に追加して管理外にするのが一般的な運用です。
- グローバル（`~/.claude/settings.json`）→ プロジェクト（`.claude/settings.json`）→ ローカル（`.claude/settings.local.json`）の順で後者が優先されます。
- Cursor の `.cursor/settings.json`、Windsurf の類似ファイルなど、AI エディタ系ツールはそれぞれ独自の設定ファイルを持ちます。スコープは Claude Code に限定。
