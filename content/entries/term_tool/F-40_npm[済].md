---
id: F-40
title: npm
title_reading: エヌピーエム
category: term_tool
subtype: cli_build
experience_level: hands_on
reader_level: 2
importance: C
figure_type: workflow
page_layout: spread_v1
version_status: active
pricing_note: none
evaluation_date: 2026-04-29
related_terms:
  - Node.js
  - package.json
  - JavaScript
  - pnpm
  - Vite
status: ready
---

# npm

## tagline

Node Package Manager の略。JavaScript のライブラリを一括で管理するツールです。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

JavaScript で使うライブラリをコマンド 1 つでインストール・更新・削除できます。`package.json` に依存関係が記録され、環境を再現しやすくなります。

## どこで出会うか

Vite や TypeScript など多くの JS ツールが npm 経由で配布されます。AI にプロジェクト作成を頼むと `npm install` を案内されることがあります。

## メイン図

### 図の狙い

`npm install` を起点に、ライブラリが `node_modules` へ展開され、スクリプトが実行されるまでの流れを 1 枚で見せます。

### C. 概念図（figure_type: workflow）

- 中心に置く概念: npm コマンド（install / run / publish）
- 周辺の要素: package.json、node_modules、npmjs.com レジストリ、スクリプト実行
- 関係の描き方: npmjs.com からライブラリを取得 → node_modules に展開 → スクリプトで利用する矢印フロー

## 会話での使い方例

「npm install してから npm run dev を叩けば、すぐ起動できますよ。」

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

JavaScript ライブラリの取得・管理・実行をコマンドで担います。

### 2. うれしさ

依存関係が package.json に記録され、環境を再現しやすくなります。

### 3. 注意点

node_modules は容量が大きく、Git 管理対象から外す設定が要ります。

### 4. どこで役立つか

JavaScript 系プロジェクトのセットアップや CI 環境で使います。

### 5. はじめに

install / run / init と package.json の役割を押さえます。

### 6. 深掘り先

pnpm、yarn、package-lock.json、npmjs.com。

## 開発フローでの位置（必須）

1. `npm init` — package.json を生成して初期化する
2. `npm install {ライブラリ}` — ライブラリを取得して node_modules に展開する
3. `npm run dev` — スクリプトを実行して開発サーバーを起動する
4. `npm run build` — 本番向けにビルドして成果物を生成する

## 関連用語

- Node.js
- package.json
- JavaScript
- pnpm
- Vite

<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

- pip の経験があるので npm 自体はすんなり入りましたが、綴りが npm か mpn か混乱しました。
- ターミナルはタイポが命取りで、音声で日本語指示できる環境のほうが非エンジニアには楽です。

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

- 🙂 第一印象: コマンドをよく間違える、という体験からのスタートでした。
- 👍 良い点: 慣れればパッケージを楽に引っ張ってこられて便利です。
- 👎 ダメな点: 1 文字ミスが命取りになるターミナルは非エンジニアにハードルが高いです。
- 👥 誰向けか: JavaScript 系のパッケージを管理・インストールする人全般に必要です。


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: workflow）

- 描く内容: 左に npmjs.com のロゴ風アイコン、中央に「npm install」コマンドを打つ人物、右に node_modules フォルダと package.json が並ぶ。矢印でライブラリが流れてくる様子を示す
- 登場人物: ターミナルの前に座る人物 1 名（初心者感のある表情）
- 吹き出し・心の声: 「npm install って打つだけで全部入るんですか？」「はい、package.json に書いたものが全部入ります」
- 中央に置くキーワード/ラベル: npm install → node_modules 展開 → 開発スタート

### 6視点アイコン（右ページ上段）

- 共通アイコン流用

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: ファイルアイコン（package.json 初期化）
- Step 2 のアイコン/絵柄: ダウンロード矢印（ライブラリ取得）
- Step 3 のアイコン/絵柄: 再生ボタン（開発サーバー起動）
- Step 4 のアイコン/絵柄: 箱アイコン（ビルド成果物）
- 矢印で示す流れの意図: 初期化 → 取得 → 開発 → 本番化 のライフサイクル


## コミュニティ補完メモ

- Node.js（F-80）との住み分け：Node.js は npm の実行環境（ランタイム）。npm はそのエコシステムのパッケージ管理層。Node.js がインストール済みであることが前提
- pnpm（F-44）との住み分け：pnpm は npm の代替ツールで高速・省容量。操作感は似ているが内部の依存解決方式が異なる。本エントリは npm の基本概念に集中し、比較は pnpm エントリへ逃がす
- Vite（F-41）との住み分け：Vite は npm 経由でインストールして使うビルドツール。「npm で入れる」対象の代表例として言及できる関係
- JavaScript（F-1）との住み分け：npm は JavaScript エコシステムの管理層。言語自体の説明は F-1 に委ねる

## 出典メモ

- npmjs.com — checked 2026-04-29
- docs.npmjs.com — checked 2026-04-29

## 備考

- npm は Node.js に同梱されており、Node.js をインストールすると自動的に使えるようになります
- `node_modules` ディレクトリは `.gitignore` に記載して Git 管理から除外するのが慣例です
- npm v7 以降、`package-lock.json` が自動生成され、依存関係の固定がより厳密になっています
