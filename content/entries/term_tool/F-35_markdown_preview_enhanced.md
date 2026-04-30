---
id: F-35
title: Markdown Preview Enhanced
title_reading: マークダウン プレビュー エンハンスト
category: term_tool
subtype: editor_ext
experience_level: hands_on
reader_level: 2-3
importance: D
figure_type: before_after
page_layout: spread_v1
start_date:
end_date:
version_status: active
pricing_note: none
evaluation_date: 2026-04-30
related_terms:
  - VS Code
  - Markdown
  - Markdown All in One
  - Mermaid
status: drafting
---

# Markdown Preview Enhanced

## tagline

標準プレビューを超える Markdown 強化拡張です。図・数式・PDF 出力まで一気に使えます。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

VS Code（F-30）向けの Markdown プレビュー拡張機能（エクステンション）です。Mermaid（F-140）図や KaTeX 数式のレンダリング、コードチャンク実行、HTML / PDF / PNG へのエクスポートなど、標準プレビューにはない機能をまとめて提供します。

## どこで出会うか

AI アシスタントが出力した Mermaid 入り仕様書を VS Code で確認するときに活躍します。拡張機能マーケットプレイスで「Markdown Preview Enhanced」を検索すると見つかります。Markdown All in One（F-38）と組み合わせて使う人も多いです。

## メイン図

### 図の狙い

標準プレビューとの機能差を対比することで、MPE でできることをひと目で伝えます。

### A. Before / After（figure_type: before_after）

- Before
  - 状況: 標準プレビューのみの環境
  - 視覚要素: Mermaid コードがそのままテキストで表示される
  - つまずき: 図が描画されず、仕様書の意図が伝わらない
- After
  - 状況: MPE を導入した環境
  - 視覚要素: Mermaid がフローチャートとして描画され、PDF ボタンも表示
  - うれしさ: AI が出した図付き仕様書をそのまま確認・出力できる

## 会話での使い方例

「MPE を入れたら、Claude が出した Mermaid 図がそのまま PDF まで出せました。」

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

VS Code の Markdown プレビューを多機能に拡張します。

### 2. うれしさ

Mermaid 図や数式を即座に確認し PDF 出力まで完結できます。

### 3. 注意点

コードチャンク実行は Python など環境依存の設定が必要です。

### 4. どこで役立つか

AI 生成の図付き仕様書を素早く確認・共有する場面で効果的です。

### 5. はじめに

VS Code へのインストールと標準プレビューとの違いを把握する段階です。

### 6. 深掘り先

Mermaid、PlantUML、KaTeX

## 開発フローでの位置（必須）

1. 仕様書作成 — AI に Markdown 形式で図入り仕様書を生成させます
2. プレビュー確認 — MPE でリアルタイムに Mermaid 図・数式を描画確認します
3. 修正サイクル — AI と対話しながら図の構造や記述を整えます
4. エクスポート — 完成した仕様書を PDF や HTML として書き出します

## 関連用語

- VS Code
- Markdown
- Markdown All in One
- Mermaid

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

### メイン図（左ページ中段 / figure_type: before_after）

- 描く内容: 左に標準プレビュー（Mermaid コードがテキストのまま）、右に MPE（フローチャートが描画され PDF ボタンが表示）の対比
- 登場人物: 画面を見て首をかしげる開発者（Before）、画面を見てうなずく開発者（After）
- 吹き出し・心の声: Before「図が文字のまま…」/ After「Mermaid がそのまま見える！」
- 中央に置くキーワード/ラベル: Markdown Preview Enhanced
- Before / After の対比ポイント: Mermaid テキスト表示 vs 図描画 + PDF エクスポートボタン

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: AI チャット画面（仕様書生成）
- Step 2 のアイコン/絵柄: VS Code プレビューパネル（図描画）
- Step 3 のアイコン/絵柄: 矢印往復（AI との修正サイクル）
- Step 4 のアイコン/絵柄: PDF ファイルアイコン（エクスポート）
- 矢印で示す流れの意図: AI 生成 → 確認 → 修正 → 出力という 1 往復の流れ

## コミュニティ補完メモ

- F-38 Markdown All in One との住み分け：All in One は編集補助（ショートカット・リスト整形・目次生成）がメイン。MPE はプレビュー強化・出力機能がメイン。両者は競合しないため併用が一般的。
- F-140 Mermaid との住み分け：Mermaid は図の記法（言語）そのもの。MPE はその Mermaid をレンダリングするツールの 1 つ。
- F-30 VS Code が前提環境。Atom 版も存在するが本エントリは VS Code 文脈で記述。

## 出典メモ

- <https://marketplace.visualstudio.com/items?itemName=shd101wyy.markdown-preview-enhanced> — checked 2026-04-30
- <https://shd101wyy.github.io/markdown-preview-enhanced/> — checked 2026-04-30

## 備考

- 開発者：Yiyi Wang（GitHub: shd101wyy）。長年にわたり個人でメンテされている人気拡張。
- コードチャンク実行（Python / Node.js 等）は実行環境の別途用意が必要。初心者には上級機能。
- プレゼン化（reveal.js 連携）は本エントリでは深掘りせず、将来の関連エントリへ回す。
