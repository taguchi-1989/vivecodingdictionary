---
id: F-9
title: SVG
title_reading: エスブイジー
category: term_tool
subtype: language
experience_level: partial
reader_level: 2-3
importance: C
figure_type: comparison
page_layout: spread_v1
start_date:
end_date:
version_status: active
pricing_note: none
evaluation_date: 2026-04-29
related_terms:
  - HTML
  - CSS
  - JavaScript
  - Mermaid
status: ready
---

# SVG

## tagline

Scalable Vector Graphics の略。XML タグで図形を文字として記述するベクター画像形式です。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

`<circle cx="50" cy="50" r="40" fill="blue"/>` のように、XML タグで図形の座標・色・形を記述します。テキストなので拡大しても劣化せず、アイコンやロゴ、グラフに向きます。

## どこで出会うか

AI に「丸い青いアイコンを作って」と頼むと SVG コードを返すことがあります。Web のロゴや図表、データ可視化にも使われ、HTML（F-4）に直接埋め込む場面で目にします。

## メイン図

### 図の狙い

ラスター（PNG・JPEG）との対比で、SVG がテキストで書かれた図形であることを示します。

### B. 登場シーン（figure_type: comparison）

- シーン1: PNG — ピクセルの集合、拡大すると粗くなる
- シーン2: SVG — XML タグの集合、拡大しても線が滑らか
- 並べる基準: 拡大耐性と編集可能性の違い


## 会話での使い方例

「SVG なら Claude に直接生成してもらえるから、図のたたき台に向きます。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

XML タグで図形を記述するベクター画像形式です。

### 2. うれしさ

テキストなので diff・検索・AI 生成が可能です。

### 3. 注意点

写真など複雑な画像は PNG や JPEG のほうが適しています。

### 4. どこで役立つか

アイコン・ロゴ・グラフ・データ可視化に向きます。

### 5. はじめに

HTML へのインライン埋め込みと、CSS での色変更の 2 点が基礎です。

### 6. 深掘り先

HTML（F-4）、CSS（F-5）、JavaScript（F-1）


## 開発フローでの位置（必須）

1. 要件整理 — アイコンや図表が必要なシーンを特定する
2. AI 生成 — Claude や ChatGPT に SVG コードを出力させる
3. HTML 埋め込み — `<svg>` タグをページに貼り付ける
4. CSS 調整 — fill・stroke を CSS で変更してスタイルを整える
5. 確認 — 拡大・縮小して劣化がないことをブラウザで確認する


## 関連用語

- HTML
- CSS
- JavaScript
- Mermaid


<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- 画像のつもりで開くとテキストの羅列が出てきて驚きました
- できることの多さに期待が膨らむ一方、実際には難しい場面もあります
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: 軽くしっかりした画像が出せ、LLM に書かせられると知って驚きました
- 👍 良い点: LLM が得意で再現性があり、後から編集もできる点が優れています
- 👎 ダメな点: LLM の精度がまだ足りず、CAD 相当のレベルには至っていません
- 👥 誰向けか: 編集可能な画像を作りたい人向けで、今後の可能性に注目です
<!-- user-input:end key="my_comment" -->

<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: comparison）

- 描く内容: 左に PNG の拡大粗れ（ピクセルがブロック状に見える）、右に SVG の拡大（線が滑らか）の対比
- 登場人物: デザイナー風の人物がロゴを拡大ルーペで確認している
- 吹き出し・心の声: 「拡大しても崩れない！」
- 中央に置くキーワード/ラベル: PNG vs SVG
- Before / After の場合の対比ポイント: ラスター（劣化）× ベクター（綺麗）

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: メモ帳（要件）
- Step 2 のアイコン/絵柄: AI チャット画面（生成）
- Step 3 のアイコン/絵柄: HTML ファイル（埋め込み）
- Step 4 のアイコン/絵柄: CSS ブラシ（スタイル調整）
- 矢印で示す流れの意図: AI 生成 → 組み込み → 仕上げ の一方通行


## コミュニティ補完メモ

- Mermaid（F-140）との住み分け：Mermaid はフローチャート・シーケンス図など「関係図」専門で AI が Markdown 記法で生成。SVG は汎用の図形描画で、Mermaid が最終的に SVG を出力する下位形式でもある。
- PNG・JPEG との住み分け：写真や複雑な画像はラスター形式が適切。SVG はアイコン・ロゴ・図表など「幾何学的な図形」向け。


## 出典メモ

- MDN Web Docs: SVG — <https://developer.mozilla.org/ja/docs/Web/SVG> — checked 2026-04-29
- W3C SVG 仕様 — <https://www.w3.org/TR/SVG2/> — checked 2026-04-29

## 備考

- SVG は W3C 標準規格で、ほぼすべての主要ブラウザがネイティブ対応済み。
- AI（Claude / ChatGPT など）は `<svg>` タグ付きのコードを直接出力できるため、バイブコーディング文脈では「たたき台をすぐ作れる画像形式」として注目されています。
