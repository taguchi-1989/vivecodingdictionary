---
id: F-44
title: pnpm
title_reading: ピーエヌピーエム
category: term_tool
subtype: cli_build
experience_level: hands_on
reader_level: 3-4
importance: C
figure_type: comparison
page_layout: spread_v1
start_date:
end_date:
version_status: active
pricing_note: none
evaluation_date: 2026-04-29
related_terms:
  - npm
  - Vite
  - Node.js
  - monorepo
status: drafting
---

# pnpm

## tagline

npm より高速・省容量な JavaScript パッケージマネージャです。グローバルストアとリンクで重複を排除します。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

JavaScript プロジェクトの依存パッケージをインストール・管理するツールです。パッケージをグローバルストアに 1 回保存し、各プロジェクトはシンボリックリンクで参照します。npm（F-40）や Yarn よりディスク消費が少なく、install も速くなります。


## どこで出会うか

Vite（F-41）や Vue の公式ドキュメントで推奨ツールとして名前が出ます。AI エディタがプロジェクトの `package.json` を読んで pnpm コマンドを自動選択する場面や、CI のキャッシュ設定でも目にします。


## メイン図

### 図の狙い

npm と pnpm のディスク使用構造を並べて、グローバルストアとリンクの仕組みを掴んでもらいます。

### B. 登場シーン（figure_type: comparison）

- シーン1: npm — プロジェクトごとに node_modules を丸ごとコピー
- シーン2: pnpm — グローバルストアに 1 つ保存、各プロジェクトはリンクで参照
- 並べる基準: ディスク使用量と install 速度の差


## 会話での使い方例

「pnpm に切り替えたら CI のキャッシュ込みで install が 30 秒以上短くなりました。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

npm の代替として依存パッケージを管理するツールです。

### 2. うれしさ

ストア共有でディスク節約と高速 install が同時に得られます。

### 3. 注意点

node_modules 構造が独自なため、稀にパス解決で問題が出ます。

### 4. どこで役立つか

モノレポや CI 環境など、install 回数が多い構成で差が出ます。

### 5. はじめに

npm との違いはストア共有の仕組みとコマンド互換性を押さえます。

### 6. 深掘り先

npm, Vite, monorepo


## 開発フローでの位置（必須）

1. 環境構築 — `npm install -g pnpm` または corepack で有効化します
2. パッケージ追加 — `pnpm add パッケージ名` で依存を追加します
3. workspace 設定 — `pnpm-workspace.yaml` でモノレポ構成を定義します
4. CI 組み込み — キャッシュキーに pnpm ストアパスを指定して高速化します


## 関連用語

- npm
- Vite
- Node.js
- monorepo


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

### メイン図（左ページ中段 / figure_type: comparison）

- 描く内容: 左側に npm の構造（プロジェクト A と B がそれぞれ node_modules をコピー保持）、右側に pnpm の構造（グローバルストアから矢印でリンク）を並べた比較図
- 登場人物: エンジニア風の人物が左右の構造を指さして比較している
- 吹き出し・心の声: 左「同じパッケージが 3 つも…」右「1 つで全部つながります」
- 中央に置くキーワード/ラベル: pnpm グローバルストア

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: インストールアイコン
- Step 2 のアイコン/絵柄: プラス記号
- Step 3 のアイコン/絵柄: フォルダ構造
- Step 4 のアイコン/絵柄: CI サーバ
- 矢印で示す流れの意図: セットアップから運用までの一方向フロー


## コミュニティ補完メモ

- npm（F-40）との住み分け: npm は Node.js 標準添付のデファクト。pnpm は npm 互換コマンドを持つが、ストア構造が異なるため既存プロジェクトの移行時に確認が必要。
- Yarn との差: Yarn も高速化を売りにするが、pnpm のストア共有モデルはディスク削減効果がより大きい。
- monorepo 文脈: pnpm workspace は Turborepo や Nx と組み合わせることが多い。Turborepo エントリがあれば住み分けを記載する。


## 出典メモ

- <https://pnpm.io/motivation> — checked 2026-04-29
- <https://vitejs.dev/guide/> (pnpm 推奨記述) — checked 2026-04-29


## 備考

- pnpm は「Performant npm」の略とされているが、公式サイトでは略称であることより機能の説明が中心。tagline では略称展開より機能説明を優先した。
- node_modules のホイスティング（hoist）挙動が npm と異なり、暗黙的な依存が解決できずにエラーになるケースがあるため注意点に記載。
