---
id: F-7
title: YAML
title_reading: ヤムル
category: term_tool
subtype: language
experience_level: partial
reader_level: "2"
importance: C
figure_type: before_after
page_layout: spread_v1
start_date:
end_date:
version_status: active
pricing_note: none
evaluation_date: 2026-04-29
related_terms:
  - JSON
  - Docker Compose
  - GitHub Actions
  - OpenAPI
  - Markdown
status: drafting
---

# YAML

## tagline

インデント（字下げ）で構造を表す、人間が読み書きしやすい設定データ形式です。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

階層構造を持つデータをインデントと記号で表現し、設定ファイルや定義ファイルとして使える形式です。JSON（ジェイソン）と同じデータを書けますが、コメントが書けて記号が少ないぶん、人が編集する用途に向いています。

## どこで出会うか

GitHub Actions（ギットハブアクションズ）のワークフロー定義、Docker Compose（ドッカーコンポーズ）の設定、本書のエントリ先頭の YAML フロントマターなどで目にします。AI ツールの設定ファイルにも使われることがあります。

## メイン図

### 図の狙い

同じデータの YAML 表記と JSON 表記を左右に並べ、「読みやすさ」の差を直感で掴んでもらいます。

### A. Before / After（figure_type: before_after）

- Before（JSON）
  - 状況: `{` `}` `"` などの記号が連続するテキスト
  - 視覚要素: `{"name": "Alice", "role": "editor"}`
  - つまずき: 記号が多く、人が書いて間違いやすい
- After（YAML）
  - 状況: インデントだけで階層を表した同等データ
  - 視覚要素: `name: Alice` / `role: editor`
  - うれしさ: シンプルで読みやすく、コメントも書ける

## 会話での使い方例

「GitHub Actions の設定は YAML で書くので、インデントがずれるとエラーになります。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

インデントで構造を表す、人が読み書きしやすい設定データ形式です。

### 2. うれしさ

コメントが書けて記号が少ないため、設定ファイルの編集ミスが減ります。

### 3. 注意点

インデントがスペース 1 個ずれるだけでエラーになることがあります。

### 4. どこで役立つか

GitHub Actions・Docker Compose など設定ファイルの事実上の標準です。

### 5. はじめに

まずキーと値を `キー: 値` と書き、ネストはスペース 2 個で覚えると十分です。

### 6. 深掘り先

JSON（F-8）、GitHub Actions（G-10）、Docker Compose（F-90）。

## 開発フローでの位置（必須）

1. 設定ファイルの確認 — GitHub Actions や Docker Compose の `.yml` ファイルを開く
2. AI に修正を依頼 — 「この YAML に設定を追加して」と AI へ渡す
3. インデント検証 — AI から返ってきた YAML のインデントを目視または Lint で確かめる
4. 動作確認 — 実際にワークフロー実行・コンテナ起動して設定が反映されているか確かめる

## 関連用語

- JSON
- Docker Compose
- GitHub Actions
- OpenAPI
- Markdown


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

- 描く内容: 左半分に JSON（記号が多い）、右半分に同じデータの YAML（インデントのみ）を並べた Before / After 対比
- 登場人物: 非エンジニアの人物 1 人がエディタ画面を見比べている
- 吹き出し・心の声: 「JSON と中身は同じなのに、YAML のほうがずっと読みやすいですね。」
- 中央に置くキーワード/ラベル: JSON → YAML（同じデータ、違う見た目）
- Before / After の対比ポイント: 記号だらけの JSON（Before）とインデントだけで読める YAML（After）

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: ファイルアイコン（.yml ファイルを開く）
- Step 2 のアイコン/絵柄: チャット吹き出し（AI へ依頼）
- Step 3 のアイコン/絵柄: 虫眼鏡（インデント検証）
- Step 4 のアイコン/絵柄: チェックマーク（動作確認）
- 矢印で示す流れの意図: ファイル確認 → AI 依頼 → 検証 → 動作確認 の 4 ステップ

## コミュニティ補完メモ

- JSON（F-8）との住み分け：JSON は機械間の通信やデータ交換に向くフォーマット。コメントが書けず記号が多いが、仕様が単純で言語対応が広い。人が編集する設定ファイルには YAML、API レスポンスや設定の受け渡しには JSON という使い分けが多い。
- GitHub Actions（G-10）との住み分け：GitHub Actions はワークフロー自動化ツール。その定義ファイルが YAML で書かれる。YAML の記法は本エントリ、Actions の使い方は G-10 へ。
- Docker Compose（F-90）との住み分け：Docker Compose はコンテナ構成定義ツール。定義ファイル docker-compose.yml が YAML 形式。YAML の記法は本エントリ、Compose の仕組みは F-90 へ。
- OpenAPI との住み分け：OpenAPI（旧 Swagger）はAPI仕様定義規格で、YAML または JSON で書く。本エントリは YAML 記法に絞り、OpenAPI の仕様詳細は別エントリへ。
- Markdown（F-6）との住み分け：Markdown は文書記法、YAML はデータ形式。本書のエントリでは YAML フロントマターと Markdown 本文が組み合わさっており、自己言及として「会話での使い方例」に活かした。

## 出典メモ

- yaml.org — checked 2026-04-29
- yaml.org/spec — checked 2026-04-29

## 備考

- YAML は "YAML Ain't Markup Language" の再帰的略称。もとは "Yet Another Markup Language" だったが、マークアップ言語ではなくデータ形式であることを強調するため改称された。
- インデントはスペースのみ許容でタブ文字は使えない（仕様上の制約）。これが非エンジニアのつまずきポイントになりやすい。
- GitHub Actions のワークフロー定義ファイルの拡張子は `.yml` または `.yaml` のいずれも使える（慣習は `.yml`）。
- YAML 1.1 と 1.2 でデフォルト値の扱いなど仕様差があるが、本エントリは設定ファイルとしての実用的な使い方に絞り、バージョン差分には踏み込まない。
