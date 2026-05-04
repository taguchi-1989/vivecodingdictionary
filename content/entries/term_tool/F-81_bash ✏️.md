---
# ── 識別・分類 ──
id: F-81
title: bash
title_reading: バッシュ
category: term_tool
subtype: shell

# ── 読者・体験 ──
experience_level: hands_on
reader_level: 2-3
importance: D

# ── 誌面形式 ──
figure_type: structure
page_layout: spread_v1

# ── 時変情報 ──
start_date: 1989-01-01
version_status: active
pricing_note: none
evaluation_date: 2026-04-29

# ── 関係 ──
related_terms:
  - git
  - Node.js
  - WSL
  - PowerShell

# ── 制作状態 ──
status: drafting
---

# bash

## tagline

Bourne Again Shell の略。Linux・macOS で広く使われるコマンド入力環境です。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

ターミナル（端末）でコマンドを受け付け、ファイル操作・環境変数の設定・パイプ（`|`）やリダイレクト（`>`）による処理の組み合わせを実行します。複数の処理をまとめたシェルスクリプトを書けば、反復作業を自動化できます。

## どこで出会うか

Claude Code や Cursor の Bash ツールが裏で呼ぶのがこのシェルです。AI が出すコマンドやスクリプトはほぼ bash 互換で書かれるため、ターミナルを開くたびに存在します。Windows では WSL（F-82）経由で使うことがあります。

## メイン図

### 図の狙い

bash がコマンドを受け取り、OS に指示を渡す流れを中心に、スクリプトで自動化できるイメージを示す。

### C. 概念図（figure_type: structure）

- 中心に置く概念: bash（シェル）
- 周辺の要素: コマンド入力 / 環境変数 / パイプ・リダイレクト / シェルスクリプト / OS（カーネル）
- 関係の描き方: bash を中心に、入力側（人・AI）と出力側（OS）を矢印でつなぐ


## 会話での使い方例

「bash の知識があると、Claude が出すコマンドをすぐ確認して動かせます。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

OS へのコマンド仲介役で、文字で指示を出す入り口です。

### 2. うれしさ

スクリプト化で繰り返し作業を一発自動化できます。

### 3. 注意点

macOS のデフォルトは zsh であり、bash と挙動が微妙に異なります。

### 4. どこで役立つか

AI ツールが出すコマンドの読み書きに直結します。

### 5. はじめに

シバン行（`#!/usr/bin/env bash`）の意味と基本コマンドを押さえれば十分です。

### 6. 深掘り先

WSL、PowerShell、シェルスクリプト

## 開発フローでの位置（必須）

1. 環境セットアップ — ターミナルを開き、bash で各種ツールをインストールします。
2. AI との対話 — Claude Code が Bash ツール経由でコマンドを実行します。
3. スクリプト作成 — 繰り返す手順を `.sh` ファイルにまとめて自動化します。
4. デバッグ — エラーメッセージを bash 上で確認し、原因を特定します。


## 関連用語

- git
- Node.js
- WSL
- PowerShell


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

- 描く内容: 人物がターミナルにコマンドを打ち込み、bash がそれを受け取って OS に渡す構造図
- 登場人物: ターミナルを前にしたエンジニア（または非エンジニアでも可）
- 吹き出し・心の声: 「このコマンド、bash が解釈してくれてるんだ」
- 中央に置くキーワード/ラベル: bash

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: 端末アイコン（セットアップ）
- Step 2 のアイコン/絵柄: AI・ロボットアイコン（Claude Code との連携）
- Step 3 のアイコン/絵柄: スクリプトファイルアイコン（.sh）
- Step 4 のアイコン/絵柄: 虫眼鏡・バグアイコン（デバッグ）
- 矢印で示す流れの意図: 環境構築から自動化・デバッグへ進む開発サイクル

## コミュニティ補完メモ

- PowerShell（F-83）との住み分け：bash は Linux・macOS 向け、PowerShell は Windows ネイティブ向け。Windows で bash を使うなら WSL（F-82）経由になる点をそちらで補完。
- WSL（F-82）との住み分け：WSL は「Windows 上で Linux 環境を動かす仕組み」、bash は「その中で使うシェル」。入れ子の関係なので混同注意。

## 出典メモ

- GNU Bash 公式サイト <https://www.gnu.org/software/bash/> — checked 2026-04-29
- macOS Catalina リリースノート（zsh デフォルト化）<https://support.apple.com/ja-jp/111901> — checked 2026-04-29


## 備考

- macOS Catalina（2019）以降のデフォルトは zsh だが、`/bin/bash` で bash も利用可能。
- スクリプトの先頭行「シバン」`#!/usr/bin/env bash` は「このファイルを bash で実行する」という宣言。読者のつまずきとして著者欄での記載を推奨。
- バイブコーディング文脈では Claude Code の `Bash` ツールが直接 bash を呼ぶため、AI ツール利用者にとって間接的に毎日使う環境。
