---
id: F-12
title: Electron
title_reading: エレクトロン
category: term_tool
subtype: framework
experience_level: partial
reader_level: 2-4
figure_type: structure
page_layout: spread_v1
start_date:
end_date:
version_status: active
pricing_note: none
evaluation_date: 2026-04-29
related_terms:
  - JavaScript
  - Node.js
  - VS Code
  - Tauri
status: drafting
---

# Electron

## tagline

Web 技術でデスクトップアプリを作れるフレームワークです。VS Code や Slack もこれで動いています。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

HTML・CSS・JavaScript（ジャバスクリプト）で書いた Web アプリを、Windows・Mac・Linux のデスクトップアプリとして配布できる形にしてくれます。Chromium（Web レンダリング）と Node.js（OS API アクセス）を 1 パッケージに同梱するため、1 つのコードベースで 3 OS に対応できます。

## どこで出会うか

VS Code（F-30）・Slack・Discord・Notion・Claude Desktop など、日常で使うデスクトップアプリの多くが Electron 製です。「Web で作った AI チャット画面をローカルアプリにしたい」という場面で名前が挙がることがあります。

## メイン図

### 図の狙い

Web コードが Electron を通じて 3 OS のデスクトップアプリになる流れを示します。

### C. 概念図（figure_type: structure）

- 中心に置く概念: Electron（Chromium + Node.js を同梱）
- 周辺の要素: HTML/CSS/JS コード、Windows、Mac、Linux
- 関係の描き方: 中心から 3 OS へ矢印で展開

## 会話での使い方例

「Electron なら Web のスキルだけでデスクトップアプリ化できますね。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

Web 技術を 3 OS のデスクトップアプリに変換するフレームワークです。

### 2. うれしさ

JavaScript の知識だけで Windows・Mac・Linux に同時対応できます。

### 3. 注意点

Chromium を同梱するためインストール容量が 100〜300 MB になることがあります。

### 4. どこで役立つか

Web スキルだけでローカルで動く AI ツールやエディタを作る場面で役立ちます。

### 5. はじめに

「VS Code も Electron 製」を起点に、仕組みを把握するのが近道です。

### 6. 深掘り先

Node.js、Tauri、JavaScript

## 開発フローでの位置（必須）

1. Web アプリ実装 — HTML/CSS/JS でブラウザ動作を確認します
2. Electron 導入 — npm で electron パッケージを追加してプロジェクトに組み込みます
3. ビルド設定 — electron-builder 等でプラットフォームごとのパッケージを生成します
4. 配布 — 各 OS 向けインストーラーを書き出してユーザーに配布します

## 関連用語

- JavaScript
- Node.js
- VS Code
- Tauri


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

- 描く内容: 中央に「Electron」ボックス（中に Chromium と Node.js のロゴ）、左から HTML/CSS/JS コードが流入し、右へ Windows・Mac・Linux の 3 OS アイコンへ矢印展開
- 登場人物: 開発者（手元に JS コードを持つ）
- 吹き出し・心の声: 「Web コードのまま 3 OS に出せる！」
- 中央に置くキーワード/ラベル: Electron

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: ブラウザ画面
- Step 2 のアイコン/絵柄: npm パッケージ箱
- Step 3 のアイコン/絵柄: ビルド歯車
- Step 4 のアイコン/絵柄: 3 OS ロゴ並び
- 矢印で示す流れの意図: Web → Electron → 各 OS 配布の一方向フロー


## コミュニティ補完メモ

- Tauri（F-13）との住み分け：Electron は Web スキルそのまま使えて採用実績が多い。Tauri は Rust ベースで軽量だが学習コストが上がる。容量・メモリを重視するなら Tauri、実績と手軽さを重視するなら Electron。
- VS Code（F-30）はその採用例として触れることで Electron の存在感を示せる。

## 出典メモ

- <https://www.electronjs.org/> — checked 2026-04-29
- <https://code.visualstudio.com/docs/editor/whyvscode> — checked 2026-04-29

## 備考

- Chromium + Node.js を毎アプリ同梱する構造上、インストール容量は 100〜300 MB が目安。メモリ消費も多めになることがある。
- 代替として Tauri（F-13）が登場しており、軽量化を求める場合の選択肢になっている（2026-04-29 時点で active）。
