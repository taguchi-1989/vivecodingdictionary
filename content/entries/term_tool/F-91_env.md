---
id: F-91
title: .env
title_reading: ドット イーエヌブイ
category: term_tool
subtype: config_file
experience_level: hands_on
reader_level: 2-3
importance: D
figure_type: before_after
page_layout: spread_v1
start_date:
end_date:
version_status: active
pricing_note: none
evaluation_date: 2026-04-29
related_terms:
  - .gitignore
  - git
  - Node.js
  - Python
  - MCP
status: drafting
---

# .env

## tagline

API キーなどを `KEY=VALUE` 形式で書き並べた設定ファイル。プロジェクトルートに置くのが慣習です。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

`dotenv` 系ライブラリで起動時に読み込まれ、コード中から `process.env.KEY` や `os.environ['KEY']` で値を参照できます。ソースコードに秘密情報を直書きせずに済みます。

## どこで出会うか

AI ツールに API キーを渡す場面で登場します。Claude Code の MCP 設定や OpenAI 利用でも前提になり、`.gitignore`（F-56）で除外しテンプレ用に `.env.example` を残す運用が定番です。

## メイン図

### 図の狙い

`.env` に書いた値がコードに渡る流れと、コミットを防ぐ `.gitignore` の役割を対比で示す。

### A. Before / After（figure_type: before_after）

- Before
  - 状況: API キーをソースコードに直書き
  - 視覚要素: `const key = "sk-abcd1234"` がコードに露出
  - つまずき: git にコミットすると全世界に漏れる
- After
  - 状況: `.env` に `OPENAI_API_KEY=sk-abcd1234` を移し `.gitignore` で除外
  - 視覚要素: コードは `process.env.OPENAI_API_KEY` を参照するだけ
  - うれしさ: リポジトリは安全、手元だけで値を差し替えられる


## 会話での使い方例

「API キーは `.env` に逃がしてから Claude に渡すと安全です。」

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

API キーなどの秘密情報を外出しして管理する設定ファイルです。

### 2. うれしさ

コードを変えずに環境ごとの値を切り替えられます。

### 3. 注意点

`.gitignore` に書き忘れると秘密情報がコミットに混入します。

### 4. どこで役立つか

AI ツールや外部サービスの API キーを扱う場面で必須です。

### 5. はじめに

`KEY=VALUE` の書き方と `.gitignore` への登録の 2 点を押さえます。

### 6. 深掘り先

.gitignore、git、MCP


## 開発フローでの位置（必須）

1. ライブラリ導入 — Node.js なら `npm install dotenv`、Python なら `pip install python-dotenv` を実行します
2. `.env` 作成 — プロジェクトルートに `KEY=VALUE` 形式で API キーや接続情報を書き並べます
3. `.gitignore` 登録 — `.env` を追記して git の追跡から除外し、誤コミットを防ぎます
4. `.env.example` 追加 — キー名だけ書いた例示ファイルをリポジトリに含め、チームに構造を伝えます
5. コードから参照 — `process.env.KEY` や `os.environ['KEY']` で値を読み込んで使います


## 関連用語

- .gitignore
- git
- Node.js
- Python
- MCP


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

- 描く内容: 左に「コードに直書きされた API キー」、右に「`.env` ファイルに移してコードはキー名だけ参照」の対比
- 登場人物: 開発者が画面を見て青ざめている（Before）、安心している（After）の 2 コマ
- 吹き出し・心の声: Before「あ、これ git に上げちゃった…」/ After「キーは `.env` に分離できました。」
- 中央に置くキーワード/ラベル: `.env` ／ `.gitignore`
- Before / After の対比ポイント: ソースコードへの直書き vs. 外部ファイル経由の参照

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: パッケージボックス（ライブラリ導入）
- Step 2 のアイコン/絵柄: ファイルと鍵マーク（`.env` 作成）
- Step 3 のアイコン/絵柄: 南京錠と git ロゴ（`.gitignore` 登録）
- Step 4 のアイコン/絵柄: コピーアイコン（`.env.example` 追加）
- 矢印で示す流れの意図: ライブラリ導入から実際の参照まで、安全に使い始める一方向の手順

## コミュニティ補完メモ

- F-56 .gitignore との住み分け：`.gitignore` は「git で追跡しないファイルを指定するルール」、`.env` は「実際に除外される設定ファイル本体」。セットで使うが役割は別物。
- F-50 git との住み分け：git の基本操作（コミット・プッシュ）を扱う F-50 に対して、F-91 は「git に含めてはいけないファイルの管理」にフォーカスする。
- 環境別ファイル（`.env.local` / `.env.production` / `.env.test`）の読み込み順序はフレームワーク依存（Next.js, Vite 等）。詳細は各フレームワークのエントリへ誘導。

## 出典メモ

- dotenv npm 公式 — checked 2026-04-29
- python-dotenv PyPI — checked 2026-04-29

## 備考

- 環境別ファイル（`.env.local` / `.env.production` / `.env.test`）の読み込み優先順位はフレームワーク次第で異なります。Next.js では `.env.local` が最優先になるなど、フレームワークごとに差があります。
- GitHub Push Protection や `git secrets` による自動検知を併用すると、誤プッシュ時のキー漏洩リスクをさらに下げられます。
