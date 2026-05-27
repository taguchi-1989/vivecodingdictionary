---
id: G-31
title: Hook
title_reading: フック
category: term_llm
subtype: control
experience_level: partial
reader_level: 3
importance: C
figure_type: workflow
page_layout: spread_v1
start_date:
end_date:
version_status: active
pricing_note: none
evaluation_date: 2026-04-29
related_terms:
  - Claude Code
  - Tool Use
  - settings.json
  - Slash Command
status: ready
---

# Hook

## tagline

ツール実行の前後に自動で割り込む仕組みです。検証や通知を人手なしで動かせます。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

Claude Code がツールを呼ぶ直前・直後にシェルスクリプトを自動実行する仕組みです。validator 実行や通知など、AI と切り離した処理を差し込めます。

## どこで出会うか

`settings.json` の `hooks` 項目として登場します。発火タイミングは PreToolUse・PostToolUse の 4 種あり、ツール前後に処理を挟む場面で設定します。

## メイン図

### 図の狙い

「ツール呼び出しの前後に Hook が挟まる」往復フローを一目で伝え、AI の処理と Hook の処理が別レーンで動くことを示す。

### A. Workflow（figure_type: workflow）

- Step 1: ユーザーが Claude Code に指示を送る
- Step 2: Claude Code がツール呼び出しを発動する（PreToolUse Hook がここで発火）
- Step 3: ツールがファイル保存などを実行する
- Step 4: PostToolUse Hook が発火し、外部スクリプトが自動実行される
- Step 5: スクリプトの結果が Claude Code に戻る

## 会話での使い方例

「PostToolUse の Hook に validator を仕込むと保存ごとに自動チェックできます。」

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

ツール実行の前後に外部スクリプトを呼ぶ仕掛けです。

### 2. うれしさ

AI の返答を待たずに検証や通知を動かせます。

### 3. 注意点

スクリプトが失敗すると Hook 全体が止まることがあります。

### 4. どこで役立つか

保存時の自動テストや Slack 通知の仕込みに使えます。

### 5. はじめに

発火タイミング 4 種（Pre/PostToolUse / UserPromptSubmit / Stop）を押さえます。

### 6. 深掘り先

Tool Use（G-30）／settings.json（G-23）／Slash Command。

## 開発フローでの位置（必須）

1. 設定を書く — `settings.json` の `hooks` にタイミングとコマンドを登録します
2. ツールを呼ぶ — Claude Code がファイル保存などのツールを実行します
3. Hook が発火する — Pre/PostToolUse でスクリプトが動きます
4. 結果を受け取る — 終了コードや出力が Claude Code に返ります
5. 次の処理へ — 終了コードに応じて続行かエラー扱いかが分かれます

## 関連用語

- Claude Code
- Tool Use
- settings.json
- Slash Command

<!-- ━━━━━━━━ 著者記入欄（右ページ下段に印刷される／AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- 複数ルールを口頭で指定したとき 100% 効いているか確認しづらいです。
- モデルの問題か登録ミスかの判別がつきません。
- 自分で細かく調整するときの手順が分からずつまずきます。
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: 条件付けで動かせるので、使いこなせれば便利そう。
- 👍 良い点: コミット前のチェックなどを自動で回せるのが良い。
- 👎 ダメな点: 細かい設定はハードルが高く、Claude Code 任せになりがちです。
- 👥 誰向けか: エージェント自動化を試みて Hook が効かず不安になった人向けです。
<!-- user-input:end key="my_comment" -->


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: workflow）

- 描く内容: 横方向に「ユーザー → Claude Code → ツール実行 → Hook スクリプト → Claude Code」の 5 ステップ矢印フロー。ツール実行の前後に Hook が挟まっていることを二重矢印で示す
- 登場人物: PC に向かう人物（ユーザー）と、サーバー / スクリプトアイコン（Hook スクリプト）の 2 者を配置する
- 吹き出し・心の声: Claude Code の箱に「保存するね」という吹き出し。Hook スクリプトの箱に「validator を自動で走らせます」という吹き出し
- 中央に置くキーワード/ラベル: PostToolUse Hook 発火 → 外部スクリプト実行

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: 設定ファイル（歯車）
- Step 2 のアイコン/絵柄: 送信矢印（ツール呼び出し）
- Step 3 のアイコン/絵柄: 稲妻マーク（Hook 発火）
- Step 4 のアイコン/絵柄: スクリプト実行（ターミナル画面）
- Step 5 のアイコン/絵柄: チェックマーク（終了コード判定）
- 矢印で示す流れの意図: 「設定 → 呼び出し → 発火 → 実行 → 判定」の自動連鎖


## コミュニティ補完メモ

- Tool Use（G-30）との住み分け：Tool Use は「LLM がツールを呼ぶ仕組み」全般。Hook は「ツール呼び出しの前後に別処理を挟む仕組み」。Hook は Tool Use を前提とするが、LLM ではなく設定ファイルが起点になる点が異なる。
- Slash Command（G-32）との住み分け：Slash Command はユーザーが手動で呼ぶコマンド。Hook は自動発火。「手動 vs 自動」で分担する。
- Subagent（G-41）との住み分け：Subagent は LLM が別エージェントを呼ぶ仕組み。Hook はシェルスクリプトを呼ぶ仕組みで、AI を仲介しない点が異なる。
- 本書プロジェクト自己言及：validate_entry.py（字数チェック）と update_review_queue.py（キュー更新）が PostToolUse Hook で動いている。読者に身近な実例として本文に含めた。
- 発火タイミング詳細（4 種の使い分け）はコミュニティ補完メモへ逃がす：PreToolUse（実行前に止める用途）/ PostToolUse（実行後の検証・通知）/ UserPromptSubmit（ユーザー入力直後）/ Stop（応答完了後）。


## 出典メモ

- docs.anthropic.com/en/docs/claude-code/hooks — checked 2026-04-29


## 備考

- Hook の終了コードが 0 以外の場合、Claude Code はエラーとして扱い処理を止めることがある。スクリプトの冪等性（何度実行しても同じ結果になること）を保つことが運用上重要。
- 発火タイミング 4 種（PreToolUse / PostToolUse / UserPromptSubmit / Stop）のうち、本書では PostToolUse を中心に説明し、他 3 種はコミュニティ補完メモに補足した。
