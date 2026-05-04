---
id: H-7
title: CI/CD
title_reading: シーアイシーディー
category: workflow
subtype: methodology
experience_level: partial
reader_level: 2-3
importance: C
figure_type: workflow
page_layout: spread_v1
start_date:
end_date:
version_status: active
pricing_note: none
evaluation_date: 2026-04-29
related_terms:
  - GitHub Actions
  - DevOps
  - git push
  - Vercel
  - テスト自動化
status: drafting
---

# CI/CD

## tagline

Continuous Integration / Continuous Delivery の略。コードを push するたびに自動でテスト・ビルド・デプロイまで動かす仕組みです。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

git push をトリガーに、テスト・ビルド・デプロイを自動で順番に実行します。手動作業のミスと待ち時間を減らし、問題を早期に検出できます。

## どこで出会うか

GitHub や GitLab のリポジトリでプルリクエストを出したとき、緑のチェックマークや赤い × 印でテスト結果が表示される場面が代表的な遭遇シーンです。Vercel や Netlify が「デプロイ中」と表示するのも CI/CD の一部です。

## メイン図

### 図の狙い

push 1 回でテスト → ビルド → デプロイまで流れる様子を人物付きで示します。

### A. Before / After（figure_type: workflow）

- Before
  - 状況: 手動でテスト実行・サーバーへアップロード
  - 視覚要素: 人物が何度も PC を操作している
  - つまずき: 手順抜け・環境差異による本番障害
- After
  - 状況: push 後は自動で全工程が走る
  - 視覚要素: パイプライン矢印（push → test → build → deploy）
  - うれしさ: 人は次の機能を書くだけで済みます

## 会話での使い方例

「push 後は CI/CD が自動でテストとデプロイを走らせるので、手作業は不要です。」

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

push をトリガーに自動で品質検証とリリースをつなぎます。

### 2. うれしさ

人手作業を自動化し、本番障害の早期検出が可能になります。

### 3. 注意点

パイプライン設定が複雑になると、維持コストがかかります。

### 4. どこで役立つか

チーム開発・頻繁なリリースを行うプロジェクトで効果的です。

### 5. はじめに

push → テスト → デプロイの流れと GitHub Actions の存在。

### 6. 深掘り先

GitHub Actions、DevOps、テスト自動化。

## 開発フローでの位置（必須）

1. コード変更 — ローカルで機能を実装する
2. git push — リモートリポジトリへ送信する
3. 自動テスト（CI）— テストが全件パスするか確認する
4. 自動ビルド — 本番向けの成果物を生成する
5. 自動デプロイ（CD）— サーバーや CDN へ反映する

## 関連用語

- GitHub Actions
- DevOps
- git push
- Vercel
- テスト自動化

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

### メイン図（左ページ中段 / figure_type: workflow）

- 描く内容: 左から右へ「push → テスト → ビルド → デプロイ」の矢印パイプライン。各ステップを四角ボックスで表示する
- 登場人物: 左端に開発者 1 人（PC でコードを書いている）。右端にユーザー 1 人（ブラウザでサイトが開いた画面）
- 吹き出し・心の声: 開発者「push するだけ！」／テストボックス「全件グリーン」／ユーザー「もう更新されてる」
- 中央に置くキーワード/ラベル: CI（テスト・ビルド）／CD（デプロイ）

### 6視点アイコン（右ページ上段）

- 共通アイコン流用

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: コード・エディタアイコン
- Step 2 のアイコン/絵柄: 上矢印（push）アイコン
- Step 3 のアイコン/絵柄: チェックマーク（テスト）アイコン
- Step 4 のアイコン/絵柄: 歯車（ビルド）アイコン
- 矢印で示す流れの意図: 手動操作が push の 1 回だけで済むことを示す

## コミュニティ補完メモ

- GitHub Actions（F-62）は CI/CD を実現するツールの一例。本エントリは概念・仕組みを扱い、具体ツールの設定は F-62 へ誘導する
- DevOps（H-8）は CI/CD を含む開発・運用連携の思想全体。本エントリはその中核実装として位置づける
- Vercel（B-20）/ Netlify（B-21）は CI/CD を内蔵したホスティングサービス。本エントリでは「デプロイ先の一形態」として言及するにとどめる
- git push（F-51）が CI/CD のトリガー。F-51 側からの誘導先として機能する

## 出典メモ

- GitHub Actions 公式ドキュメント <https://docs.github.com/en/actions> — checked 2026-04-29
- Atlassian "What is CI/CD?" <https://www.atlassian.com/continuous-delivery/principles/continuous-integration-vs-delivery-vs-deployment> — checked 2026-04-29

## 備考

CI（Continuous Integration）と CD（Continuous Delivery / Continuous Deployment）は厳密に別概念だが、本エントリでは実務で一体で使われる点を優先して CI/CD とまとめて扱います。Continuous Delivery（承認後デプロイ）と Continuous Deployment（自動デプロイ）の区別は深掘り先として備考に留めます。
