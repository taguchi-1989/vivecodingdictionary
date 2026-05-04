---
id: I-80
title: 自作 MCP のテンプレ
category: mcp
subtype: diy
experience_level: hands_on
reader_level: 4-5
importance: E
figure_type: structure
page_layout: spread_v1
start_date:
end_date:
version_status: active
pricing_note: none
evaluation_date: 2026-04-30
related_terms:
  - MCP
  - MCP Server
  - MCP Client
  - TypeScript SDK
  - MCP の登録・設定
status: needs_review
---

# 自作 MCP のテンプレ

## tagline

MCP Server を自作するときのひな形です。SDK コマンドで最小構成をすぐ動かせます。


<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

`create-mcp-server`（TypeScript SDK）や `mcp`（Python SDK）がツール定義・リソース定義・プロンプト定義の 3 点セットを生成します。あとは中身を埋めるだけです。

## どこで出会うか

公式の `modelcontextprotocol/servers` に Filesystem・GitHub・Slack のリファレンス実装があります。構造の学習やコピー元に使えます。

## メイン図

### 図の狙い

テンプレから自作 Server が生まれ、MCP Client に接続されるまでの流れを示す。

### C. 概念図（figure_type: structure）

- 中心に置く概念: テンプレ → 自作 Server → MCP Client
- 周辺の要素: ツール定義、リソース定義、プロンプト定義、TypeScript SDK、Python SDK
- 関係の描き方: 矢印で「生成 → 接続」の流れ

## 会話での使い方例

「ひな形を出してツール定義を書き換えるだけで動きますよ。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

SDK 付属のひな形で Server 自作の初動を短縮します。

### 2. うれしさ

ゼロから構造を考えず、定義部分の記述に集中できます。

### 3. 注意点

SDK バージョンによって API の形式が変わることがあります。

### 4. どこで役立つか

社内ツールや独自データを LLM に接続したい場面で使います。

### 5. はじめに

TypeScript か Python かを選び、SDK をインストールして確認します。

### 6. 深掘り先

MCP Server、TypeScript SDK、MCP の登録・設定

## 開発フローでの位置（必須）

1. SDK 選択 — TypeScript か Python か用途に合わせて選びます
2. ひな形生成 — `create-mcp-server` または `uvx` でスキャフォールドを展開します
3. 定義記述 — ツール・リソース・プロンプトの 3 項目を埋めます
4. 接続確認 — MCP Client（Claude Code 等）から Server を呼び出して動作を確かめます

## 関連用語

- MCP
- MCP Server
- MCP Client
- TypeScript SDK
- MCP の登録・設定


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

- 描く内容: テンプレリポジトリから自作 Server が生まれ、MCP Client に矢印でつながる構造図
- 登場人物: 開発者（男性または女性）がターミナルの前に座り、ひな形ファイルを指差している
- 吹き出し・心の声: 「ツール定義を埋めるだけでいい！」
- 中央に置くキーワード/ラベル: テンプレ → Server → Client

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: 分岐アイコン（TypeScript / Python の選択）
- Step 2 のアイコン/絵柄: ターミナルとフォルダアイコン
- Step 3 のアイコン/絵柄: 鉛筆とコードブロック
- Step 4 のアイコン/絵柄: 接続プラグと緑チェック


## コミュニティ補完メモ

- I-2 MCP Server との住み分け：I-2 は MCP Server の概念と役割を説明。本エントリは「自作するときの具体的な出発点（ひな形）」に絞る
- I-81 MCP の登録・設定 との住み分け：I-81 は作った Server を設定ファイルに登録する操作。本エントリはその前段（Server を作る工程）を扱う
- TypeScript SDK 自体の詳細は別エントリ（TypeScript SDK）へ逃がす

## 出典メモ

- <https://github.com/modelcontextprotocol/servers> — checked 2026-04-30
- <https://modelcontextprotocol.io/quickstart/server> — checked 2026-04-30

## 備考

- TypeScript SDK は `@modelcontextprotocol/sdk` パッケージ、Python SDK は `mcp` パッケージ（`uvx mcp` で即実行可）
- `modelcontextprotocol/servers` リポジトリのリファレンス実装（Filesystem / GitHub / Slack 等）はコピー元として活用できる
- SDK のバージョン更新頻度が高いため、evaluation_date に注意
