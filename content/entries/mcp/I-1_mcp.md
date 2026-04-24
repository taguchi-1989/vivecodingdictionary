---
id: I-1
title: MCP（Model Context Protocol）
category: mcp
subtype: protocol
experience_level: hands_on
reader_level: 2
figure_type: structure
page_layout: spread_v1
start_date: 2024-11
version_status: active
evaluation_date: 2026-04-23
related_terms:
  - MCP Server
  - MCP Client
  - MCP Transport
  - Tool Use
  - Claude Code
status: needs_review
---

# MCP（Model Context Protocol）

## tagline

LLM とツール・データをつなぐ標準規格。「AI の USB-C」と呼ばれる共通コネクタです。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

LLM とツール（GitHub、Slack など）を共通の方式で接続する規格です。2024 年に Anthropic が提案しました。

- MCP サーバーを一度作れば MCP 対応のどの LLM からも使えます
- LLM クライアント（Claude Code、Cursor 等）は任意の MCP サーバーを差し替えられます
- Server／Client／Transport の 3 役で構成されます

## どこで出会うか

Claude Code や Cursor で使う「拡張カタログ」の規格です。公式・コミュニティ・自作の 3 層でエコシステムが広がっています。

対応 MCP を 1 つ入れるだけで GitHub 操作・Figma 読み込み・社内 DB 連携が実現できます。急拡大中の領域で、MCP 前提のエージェント設計が標準になっていきます。

## メイン図

### 図の狙い

LLM ⇔ MCP Client ⇔ MCP Server ⇔ External Service の 4 段構造を、1 枚の概念図で見せます。「個別連携」から「共通プロトコル」への構造変化が視覚で伝わるようにします。

### C. 概念図（figure_type: structure）

- 中心に置く概念: MCP Protocol（LLM とツールの間に立つ共通規格）
- 周辺の要素（4〜5 個）: LLM（Claude など）／MCP Client（Claude Code など）／MCP Server（GitHub MCP など）／External Service（GitHub 本体）／Transport（通信方式 stdio/SSE/HTTP）
- 関係の描き方: 左に LLM、右に外部サービス、中央に MCP Protocol を太く描く。両側の矢印は MCP Protocol を介して流れる
- Before/After 対比のヒント: 左下に「Before: 個別連携でバラバラ」の小さい概念図、右下に「After: MCP で統一」の概念図を添える

## この用語の見どころ

### 1. 役割

LLM とツールをつなぐ共通コネクタです。

### 2. うれしさ

一度書けば、MCP 対応のどの LLM からも同じように使えます。

### 3. 注意点

仕様とエコシステムが急成長中で、数ヶ月で状況が変わります。

### 4. どこで役立つか

エージェントのツール拡張、データ連携、社内システムとの橋渡し。

### 5. はじめに

Server／Client／Transport の 3 役と共通コネクタの発想。

### 6. 深掘り先

MCP SDK、各種 MCP（GitHub／Playwright／Notion）、自作 MCP のテンプレ。

## 開発フローでの位置（必須）

1. 欲しい外部連携を見つける — 何のツール・データと繋ぎたいか
2. 既存の MCP があるか探す — 公式／コミュニティ／商用
3. 無ければ自作、あれば設定 — SDK または設定ファイル
4. MCP Client から呼び出して実行 — Claude Code や Cursor の中で使う

<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 関連用語

- MCP Server — MCP を提供する側（ツール・データを出す）
- MCP Client — MCP を呼ぶ側（Claude Code、Cursor 等）
- MCP Transport — 通信方式（stdio / SSE / HTTP）
- Tool Use — LLM がツールを呼び出す機能全般（MCP はその標準規格版）
- Claude Code — MCP の代表的なクライアント

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

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

- 描く内容: 中央に「MCP Protocol」の太い帯。左側に LLM（Claude のロゴ風）＋ MCP Client（Claude Code ターミナル）、右側に MCP Server 群（GitHub／Playwright／Notion）＋ External Service。矢印が MCP Protocol 帯を通って両側を繋ぐ
- 登場人物: LLM 側に開発者キャラクター 1 人、外部サービス側に「つなぎ先」アイコン群
- 吹き出し・心の声: 「MCP があれば、同じやり方でどこにも繋がる」
- 中央に置くキーワード: MCP ＝ LLM とツールの共通コネクタ
- 追加: 左下に小さく「Before: バラバラ連携」／右下に「After: MCP で統一」の対比を添える

### 6視点アイコン（右ページ上段）

- 共通アイコン流用

### 開発フロー図（右ページ下段）

- Step 1: 探索アイコン（欲しい連携を見つける）
- Step 2: カタログアイコン（既存 MCP を探す）
- Step 3: 組み立て or ダウンロードアイコン（自作 or 設定）
- Step 4: 実行アイコン（Client から呼び出し）
- 矢印: 見つける → 探す → 用意する → 呼ぶ

## コミュニティ補完メモ

個別 MCP（I-10 Filesystem、I-11 GitHub、I-20 Playwright、I-30 Notion など）は別エントリで深掘り。本エントリは「プロトコル自体の総論」に絞ります。

## 出典メモ

- Anthropic "Introducing the Model Context Protocol"（2024-11）— checked 2026-04-23
- modelcontextprotocol.io — checked 2026-04-23

## 備考

MCP の仕様・エコシステムは急成長中です。evaluation_date を必ず持たせて時変情報として扱います。
