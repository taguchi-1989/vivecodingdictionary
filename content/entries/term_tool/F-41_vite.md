---
id: F-41
title: Vite
title_reading: ヴィート
category: term_tool
subtype: cli_build
experience_level: partial
reader_level: 3
figure_type: before_after
page_layout: spread_v1
version_status: active
pricing_note: none
evaluation_date: 2026-04-29
related_terms:
  - npm
  - ESM
  - HMR
  - Webpack
  - TypeScript
status: drafting
---

# Vite

## tagline

ESM（ES Modules）を活用した高速フロントエンドビルドツールです。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

フロントエンドの開発サーバ起動とコードのビルド（まとめ）を担うツールです。開発中はファイルを変更するたびに該当モジュールだけを差し替える HMR（Hot Module Replacement）が動き、ブラウザのリロードがほぼ瞬時です。

## どこで出会うか

React・Vue・Svelte などのプロジェクトで npm（Node Package Manager）経由でインストールします。`npm run dev` で開発サーバが立ち上がる場面や、Bolt.new が内部でプロジェクトを生成するときに使われています。

## メイン図

### 図の狙い

Webpack 時代の「全部バンドルしてから起動」と、Vite の「ESM をそのまま使って即起動」の差を 1 枚で見せます。

### A. Before / After（figure_type: before_after）

- Before
  - 状況: Webpack でビルド。全ファイルをまとめてからでないとサーバが立ち上がらない
  - 視覚要素（コード or 概念）: 数百ファイルを 1 つに束ねる処理が終わるまで待つ砂時計
  - つまずき: コードを 1 行直すだけでビルドが数十秒かかり、待ち時間がストレスになる
- After
  - 状況: Vite で開発。ESM をブラウザがそのまま読み、変更したファイルだけ差し替わる
  - 視覚要素: サーバ起動が一瞬、ファイル変更後の反映もほぼ瞬時のアニメーション
  - うれしさ: 待ち時間がなくなり、コードを変えた結果がすぐ画面に出て確認が速い

## 会話での使い方例

「Vite を使うと dev サーバが数秒で立ち上がり、HMR で即反映されますよ。」

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

開発サーバの高速起動と、本番向けバンドルの両方を担います。

### 2. うれしさ

ファイル変更が画面に即反映され、待ち時間が大幅に減ります。

### 3. 注意点

本番ビルドは esbuild ではなく Rollup を使い、動作差が出ることがあります。

### 4. どこで役立つか

React・Vue・Svelte など主要フレームワークの開発に使えます。

### 5. はじめに

`npm create vite@latest` でプロジェクトを作り、`npm run dev` を試します。

### 6. 深掘り先

Rollup、esbuild、HMR、ESM。

## 開発フローでの位置（必須）

1. プロジェクト作成 — `npm create vite@latest` でテンプレートを選ぶ
2. 開発サーバ起動 — `npm run dev` で即起動、HMR が自動で動く
3. コード編集 — 変更したファイルだけ差し替わりブラウザに即反映される
4. 本番ビルド — `npm run build` で Rollup が最適化した成果物を生成する

## 関連用語

- npm
- ESM
- HMR
- Webpack
- TypeScript

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

- 描く内容: 左に「全ファイルをバンドルしてから起動する Webpack 時代（砂時計と積み上がったファイル）」、右に「ESM でブラウザが直接読み込み、変更ファイルだけ差し替わる Vite（稲妻アイコンと即時反映）」
- 登場人物: 開発者キャラクター 1 人。Before で砂時計を見ながら待っている表情、After でコードを変えてすぐ画面を確認している表情
- 吹き出し・心の声: Before「ビルド終わるまで待てない…」／After「変えたらすぐ反映される！」
- 中央に置くキーワード/ラベル: ESM ＝ 変更ファイルだけ差し替え ＝ 待ち時間ゼロ
- Before/After 対比ポイント: 全バンドル（遅） vs 差分差し替え（速）

### 6視点アイコン（右ページ上段）

- 共通アイコン流用

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: パッケージアイコン（npm create）
- Step 2 のアイコン/絵柄: 稲妻アイコン（dev サーバ即起動）
- Step 3 のアイコン/絵柄: 鉛筆＋更新矢印（編集→即反映）
- Step 4 のアイコン/絵柄: 箱に詰めるアイコン（本番ビルド）
- 矢印で示す流れの意図: 作る → 動かす → 直す → 届ける のサイクル

## コミュニティ補完メモ

- Webpack（F 系候補）との住み分け：Webpack は設定の柔軟性と老舗エコシステムが強み。Vite は速さと手軽さが強みで、新規プロジェクトの主流になりつつある。本エントリは「Vite の速さの理由（ESM・HMR）」に絞る。
- npm（F-40）との関係：Vite は npm でインストールして使うツール。npm の説明とは重複しないよう、本エントリはビルドとサーバ起動の仕組みに注力する。
- Bolt.new（B-11）との関係：Bolt.new が内部で Vite を使っていることには本文で一言触れるが、詳細は B-11 エントリに任せる。

## 出典メモ

- vite.dev — checked 2026-04-29
- vitejs.dev — checked 2026-04-29

## 備考

- Vite は Vue.js 作者の Evan You が開発。Vue 専用ではなく、React・Svelte・Solid・Lit など主要フレームワークすべてに対応している。
- 開発サーバは esbuild でトランスパイル（TypeScript → JS）、本番ビルドは Rollup でバンドルするという二段構えになっている。この差が「設定が違う」と感じる原因になることがある。
- バージョンによって設定ファイルの書き方が変化することがある（vite.config.ts）。時変情報として扱う。
