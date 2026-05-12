---
# ── 識別・分類 ──
id: F-13
title: Tauri
title_reading: タウリ
category: term_tool
subtype: framework

# ── 読者・体験 ──
experience_level: partial
reader_level: 3-4
importance: D

# ── 誌面形式 ──
figure_type: comparison
page_layout: spread_v1

# ── 時変情報 ──
start_date: 2022-06-19
end_date:
version_status: active
pricing_note: none
evaluation_date: 2026-04-29

# ── 関係 ──
related_terms:
  - Electron
  - Rust
  - VS Code
  - shadcn/ui

# ── 制作状態 ──
status: ready
---

## tagline

Rust ベースの軽量デスクトップ・モバイルアプリ開発フレームワークです。OS 標準の WebView を使うため軽く動きます。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

React 等のフロントを使いつつ、バックエンドを Rust（ラスト）で動かすデスクトップアプリを作れます。OS 標準の WebView を使うため、バイナリが数 MB〜十数 MB に収まります。

## どこで出会うか

「Electron は重い」という話題で名前が出ます。1Password 8 の採用事例として記事に登場するほか、バイブコーディングで軽量 AI アプリを作る選択肢として紹介されることもあります。

## メイン図

### 図の狙い

Electron と Tauri のバイナリサイズ・構成の違いを並べて、Tauri が軽い理由を直感的に示します。

### B. 登場シーン（figure_type: comparison）

- シーン1: Electron — Chromium（クロミウム）エンジンを同梱するため、アプリ単体で 100〜150 MB になることがあります
- シーン2: Tauri — OS 標準の WebView を使うため、同等のアプリが数 MB〜十数 MB に収まります
- シーン3: フロントエンドは JS/TS、バックエンドは Rust という分業構成で動きます
- 並べる基準: 構成要素とバイナリサイズの比較

## 会話での使い方例

「Tauri なら Electron より軽い AI デスクトップアプリが作れますよね。」

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

OS 標準 WebView でデスクトップ・モバイルアプリを動かすフレームワークです。

### 2. うれしさ

Electron 比で 1/10〜1/30 のバイナリサイズで配布できます。

### 3. 注意点

バックエンドが Rust のため、深い機能追加では Rust の知識が必要になることがあります。

### 4. どこで役立つか

軽量 AI デスクトップアプリやオフライン動作ツールの配布に向いています。

### 5. はじめに

フロントエンドは普通の JS/TS で書けて、`tauri create` で雛形が立ち上がります。

### 6. 深掘り先

Electron、Rust、shadcn/ui

## 開発フローでの位置（必須）

1. プロジェクト作成 — `npm create tauri-app` でフロントエンド選択から雛形を生成します
2. UI 開発 — React・Vue 等で画面を組み、通常の Web 開発と同じ感覚で進めます
3. バックエンド連携 — Rust 側でファイル操作・通信などの機能を API として宣言します
4. ビルド・配布 — `tauri build` で各 OS 向けの軽量バイナリを生成して配布します

## 関連用語

- Electron
- Rust
- VS Code
- shadcn/ui

<!-- ━━━━━━━━ 著者記入欄（右ページ下段に印刷される／AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

- AI に教えてもらって初めて知りました。当時は学習リソースが少なく AI も苦手そうで、概念理解に時間がかかりました。

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

- 🙂 第一印象: Electron の代替として紹介されました。
- 👍 良い点: 軽量に実装できる点は良いと思います。Rust ベースで実際に作ったことはありませんが、仕組みとしては筋が良いと感じます。
- 👎 ダメな点: 学習リソースが少なく AI も苦手そうな印象がありました（今は改善しているかもしれません）。
- 👥 誰向けか: ネイティブアプリを軽量に配布したい人向けだと思います。

<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: comparison）

- 描く内容: Electron と Tauri の構成を左右に並べた比較図。Electron 側は Chromium の大きなブロック、Tauri 側は OS WebView の小さなブロックを示す
- 登場人物: 開発者が「こっちにしよう」と指差しているシーン
- 吹き出し・心の声: 「100 MB → 5 MB に！」「Rust が動いてるけど、UI は普通の React でした。」
- 中央に置くキーワード/ラベル: Electron vs Tauri バイナリサイズ比較

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: ターミナル画面（雛形生成）
- Step 2 のアイコン/絵柄: ブラウザ風の UI 編集画面
- Step 3 のアイコン/絵柄: 歯車（Rust バックエンド API）
- Step 4 のアイコン/絵柄: パッケージ箱（配布バイナリ）
- 矢印で示す流れの意図: 作成 → UI 開発 → 連携 → 配布の順で進む

## コミュニティ補完メモ

- Electron（F-12）との住み分け：Electron は Node.js を同梱する重厚なフレームワーク、Tauri は OS WebView を使う軽量代替。サイズと起動速度を重視するなら Tauri、Node.js エコシステム依存が深いなら Electron という選び方になります。
- Rust（F-200）との住み分け：Tauri のバックエンドが Rust であることに触れるが、Rust 自体の説明は F-200 に委ねます。
- VS Code（F-30）は Electron 製であるため、Tauri の対比例として言及しています。

## 出典メモ

- <https://tauri.app/blog/tauri_2_0_0_released/> — checked 2026-04-29
- <https://v2.tauri.app/> — checked 2026-04-29

## 備考

- Tauri 1.0 は 2022-06-19 リリース、Tauri 2.0 は 2024-10 リリース（モバイル対応追加）
- 1Password 8 デスクトップ版が Tauri 採用の代表事例として引用されることがあります
- WebView の実装差（Windows: WebView2、macOS: WKWebView、Linux: WebKitGTK）で挙動が微妙に異なることがあります
