---
id: F-122
title: Prisma
title_reading: プリズマ
category: term_tool
subtype: orm
experience_level: hands_on
reader_level: 3-4
importance: D
figure_type: before_after
page_layout: spread_v1
start_date:
end_date:
version_status: active
pricing_note: freemium
evaluation_date: 2026-04-29
related_terms:
  - TypeScript
  - PostgreSQL
  - SQLite
  - ORM
status: needs_review
---

# Prisma

## tagline

TypeScript（F-2）向けの型安全な ORM（Object-Relational Mapping）です。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

`schema.prisma` にテーブル定義を書くと、TypeScript 用の DB クライアントを自動生成します。SQL を直接書かずに、型補完付きでデータを取得・更新できます。

## どこで出会うか

Next.js（F-11）や Express の TypeScript プロジェクトで登場します。`schema.prisma` の構文は Claude や Cursor が読み取りやすく、クエリコードまで補完してもらえます。

## メイン図

### 図の狙い

`schema.prisma` を起点に、マイグレーションとクライアント生成が連動する流れを示します。

### A. Before / After（figure_type: before_after）

- Before
  - 状況: 素の SQL 文字列でデータ取得
  - 視覚要素: `SELECT * FROM users WHERE id = ?` — 型なし・ミスが実行時に発覚
  - つまずき: カラム名のタイポが実行まで気づけない
- After
  - 状況: Prisma クライアントで型付きクエリ
  - 視覚要素: `prisma.user.findUnique({ where: { id } })` — 補完が効いて安全
  - うれしさ: カラム名・型の誤りをエディタが即座に検出できます


## 会話での使い方例

「`schema.prisma` を Claude に書かせたら、API のクエリまで型付きで揃いました。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

TypeScript から DB を型安全に操作する ORM です。

### 2. うれしさ

スキーマ変更がコード側の型に即反映されます。

### 3. 注意点

`migrate dev` は開発用で、本番は `migrate deploy` を使います。

### 4. どこで役立つか

Next.js や Express の API 実装で DB 操作を安全にできます。

### 5. はじめに

`schema.prisma` の書き方と `prisma generate` の役割を把握します。

### 6. 深掘り先

ORM、TypeScript、PostgreSQL


## 開発フローでの位置（必須）

1. スキーマ定義 — `schema.prisma` にモデルを書く
2. マイグレーション — `prisma migrate dev` で DB に反映
3. クライアント生成 — `prisma generate` で型付きクライアントを生成
4. クエリ実装 — `prisma.user.findMany()` などを記述
5. データ確認 — Prisma Studio（GUI）で目視確認


## 関連用語

- TypeScript
- PostgreSQL
- SQLite
- ORM


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

### メイン図（左ページ中段 / figure_type: before_after）

- 描く内容: 左に SQL 文字列で書いたコード、右に Prisma クライアントの型付きクエリを並べる
- 登場人物（いれば）: 開発者（エンジニア風の人物）
- 吹き出し・心の声: Before「カラム名が合ってるか不安…」→ After「補完が出た、これで大丈夫です！」
- 中央に置くキーワード/ラベル: schema.prisma
- Before / After の対比ポイント: 型なし SQL vs 型補完付き Prisma クエリ

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: ファイルアイコン（schema.prisma）
- Step 2 のアイコン/絵柄: データベース＋矢印（migrate）
- Step 3 のアイコン/絵柄: 歯車（generate）
- Step 4 のアイコン/絵柄: コードエディタ（クエリ実装）
- Step 5 のアイコン/絵柄: 虫眼鏡（Prisma Studio）
- 矢印で示す流れの意図: スキーマ → DB → クライアント → コード → 確認の一方向フロー

## コミュニティ補完メモ

- ORM（F-123）との住み分け：F-123 は ORM という概念（設計思想・一般原則）を扱い、F-122 はその具体実装として Prisma に焦点を当てます
- SQLite（F-121）・PostgreSQL（F-120）との関係：Prisma はこれらを対応 DB として利用する上位ツールです
- TypeScript（F-2）との関係：Prisma の型生成は TypeScript の型安全を最大化するためのものです


## 出典メモ

- [Prisma Documentation](https://www.prisma.io/docs) — checked 2026-04-29


## 備考

- `prisma migrate dev` は開発環境でのみ使用。本番環境では `prisma migrate deploy` を使い分ける必要があります
- pricing_note: freemium — OSS 本体は無料、Prisma Accelerate（接続プール）などのクラウドサービスは有料プランあり（2026-04-29 時点）
