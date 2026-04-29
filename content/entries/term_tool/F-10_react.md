---
id: F-10
title: React
title_reading: リアクト
category: term_tool
subtype: framework
experience_level: partial
reader_level: 2
figure_type: structure
page_layout: spread_v1
start_date:
end_date:
version_status: active
pricing_note: none
evaluation_date: 2026-04-29
related_terms:
  - JavaScript
  - JSX
  - コンポーネント
  - Next.js
  - TypeScript
status: drafting
---

# React

## tagline

画面を部品（コンポーネント）に分けて組み立てる JavaScript ライブラリです。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

ボタン・カード・フォームなど画面の各パーツをコンポーネント（部品）として独立して作り、組み合わせてアプリ全体を構成します。状態（State）が変わると関係する部品だけ自動で画面を更新します。

## どこで出会うか

AI への修正依頼でよく出てきます。「このコンポーネントの表示を変えて」「Props（親から子への値の受け渡し）が足りない」など、粒度を部品単位で指定する会話になります。

## メイン図

### 図の狙い

ページ全体をコンポーネントの入れ子に分解した構造図で「部品で考える」発想を 1 枚で見せます。

### C. 概念図（figure_type: structure）

- 中心に置く概念: App コンポーネント（ページ全体）
- 周辺の要素: Header、SearchBar、ProductCard（×3）、Footer の 5 部品
- 関係の描き方: 包含（親 → 子のツリー構造）、矢印で Props の流れを示す

## 会話での使い方例

「React のコンポーネント単位で指定すると、AI への修正依頼が伝わりやすいですよ。」

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

UI を部品（コンポーネント）に分けて再利用しながらアプリを組み立てます。

### 2. うれしさ

部品単位で AI に修正を依頼できるので、指示の粒度が揃えやすくなります。

### 3. 注意点

ページ遷移やサーバー処理は React 単体では扱えず、Next.js などと組み合わせることがあります。

### 4. どこで役立つか

Web アプリの画面開発全般と、AI への UI 修正指示の粒度を合わせる場面で役立ちます。

### 5. はじめに

コンポーネント・Props・State の 3 概念と、JSX という HTML に似た記法が出発点です。

### 6. 深掘り先

Next.js、JSX、State、Props、TypeScript。

## 開発フローでの位置（必須）

1. 画面設計 — 「何の部品が要るか」をコンポーネント単位で整理します。
2. コンポーネント実装 — JSX で部品の見た目と State を書き、AI に生成させます。
3. Props でつなぐ — 親から子に値を渡して部品を組み合わせます。
4. ブラウザ確認 — State が変わった部分だけ自動更新されることを確認します。

## 関連用語

- JavaScript
- JSX
- コンポーネント
- Next.js
- TypeScript


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

- 描く内容: ページ全体（App）を囲む外枠の中に、Header・SearchBar・ProductCard×3・Footer が入れ子で並ぶツリー構造図
- 登場人物: 非エンジニアの担当者 1 人がページを指差している
- 吹き出し・心の声: 「この検索フォームだけ直せばいいんだ」と気づいた表情
- 中央に置くキーワード/ラベル: コンポーネント（部品）

### 6視点アイコン（右ページ上段）

- 共通アイコン流用

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: 付箋に部品名を書いて並べるアイコン（設計）
- Step 2 のアイコン/絵柄: コードブロック＋AI 吹き出し（実装）
- Step 3 のアイコン/絵柄: 矢印でつながれた部品 2 つ（Props）
- Step 4 のアイコン/絵柄: ブラウザウィンドウ＋チェックマーク（確認）
- 矢印で示す流れの意図: 設計 → 実装 → 組み合わせ → 確認 の一方向ループ


## コミュニティ補完メモ

- JavaScript 全体（F-1）との住み分け：F-1 は言語全般。F-10 は React ライブラリとコンポーネント概念に絞る。
- TypeScript（F-2）との住み分け：F-2 は型システム。F-10 では「TypeScript と組み合わせることが多い」程度に触れるだけ。
- Next.js（F-11）との住み分け：F-11 はページ遷移・SSR など周辺機能まで扱うフレームワーク。F-10 は UI 組み立てのコア概念に限定。
- 状態管理ライブラリ（Redux 等）・React Native はスコープ外。

## 出典メモ

- react.dev（公式ドキュメント） — checked 2026-04-29
- react.dev/learn/describing-the-ui — checked 2026-04-29

## 備考

- React 自体は Meta（旧 Facebook）が開発・オープンソース公開しているライブラリ（2013 年〜）。
- バージョンは頻繁に更新されるため、Hooks（useState 等）の挙動が古い情報と異なることがあります。
- version_status: active（2026-04-29 時点）、pricing_note: none（MIT ライセンス、無償）。
