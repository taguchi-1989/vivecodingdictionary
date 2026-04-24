---
id: B-2
title: Claude
category: service
subtype: ai_assistant
experience_level: hands_on
reader_level: 2
figure_type: structure
page_layout: spread_v1
start_date: 2023-03
version_status: active
pricing_note: freemium
evaluation_date: 2026-04-23
related_terms:
  - Anthropic
  - Claude Code
  - Claude.ai
  - Artifacts
  - API
  - G-46 ナーフ
status: needs_review
---

# Claude

## tagline

Anthropic が提供する AI アシスタントです。対話・文章・コードを横断して扱えます。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## ひとことで

Claude は、Anthropic 社が作る AI アシスタントです。チャット、文章作成、コード生成、資料要約、画像・PDF の読み取りなど、幅広く使えます。

## 何をしてくれるか

自然言語で話しかけると、要件整理・調査・文章化・コード生成・画像読み取り・長文の要約などを返してくれます。

同じ「Claude」でも入口がいくつかあり、そこで体験が変わります。ブラウザから使う `Claude.ai`、開発者向けの CLI／エージェントの `Claude Code`、社内ツールから呼ぶ `Claude API`、AWS 経由で使う `Amazon Bedrock` など、用途ごとに窓口が違います。

モデルのラインナップは、**最も賢いモデル（Opus）／中間のモデル（Sonnet）／アンカーモデル（Haiku）** の 3 段階で、場合によって使い分けます。普段は Sonnet、難しい仕事は Opus、軽く大量に回すときは Haiku、が基本の目安です。

## どこで出会うか

本書の制作も含め、バイブコーディングの現場で日常的に触る主役のひとつです。企画のブレインストーミングは Claude.ai、実装は Claude Code、本番アプリへの組み込みは API、と同じ Claude を使い分けるのが普通になってきています。

「Claude を使う」と言ったとき、どの窓口の話かを合わせると会話が噛み合いやすくなります。

また、モデルは提供中に「ナーフ」（G-46）と呼ばれる体感上の性能低下が起きることがあります。安全調整やモデル切替が背景になることが多く、過去にはダウングレードやロールバックが話題になった例もあります。「最近 Claude が変わった」と感じたら、まずこれを疑ってみると落ち着きます。

## メイン図

### 図の狙い

同じ Claude が、使い手によって別の景色で見えることを「3 つの登場シーン」で示します。打ち合わせで「Claude」が出たら、まずどのシーンの話かを揃える足場にします。

### B. 登場シーン（figure_type: structure）

- シーン1: 企画者が Claude.ai で打ち合わせメモを整理する — 「明日の資料、要点だけ抜き出して」
- シーン2: 開発者が Claude Code で実装を進める — 「この機能、TS に直して、テストも足して」
- シーン3: 業務担当が API で社内ツールに組み込む — 「問い合わせメールを自動分類したい」
- 並べる基準: 使う人の立場別（企画 / 開発 / 業務）

## 関連用語

- Anthropic — Claude を作っている会社
- Claude Code — Claude を CLI／エージェントとして使う道具（略称 CC）
- Claude.ai — ブラウザから Claude を使う標準窓口
- Artifacts — Claude が生成物を独立パネルに出す UI 機能
- API — Claude をアプリから呼ぶためのインターフェース
- G-46 ナーフ — モデルの体感性能が下がる現象

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

対話型の AI アシスタントです。文章・コード・画像の幅広い入出力を扱います。

### 2. うれしさ

安全性と文章の自然さに強みがあり、長文や複雑な指示に向きます。

### 3. 注意点

同じ「Claude」でも入口で体験が変わります。ナーフで性能低下が体感されることもあります。

### 4. どこで役立つか

ブレスト、文章作成、コード実装、長文の要約や読解。

### 5. はじめに

Claude.ai／Claude Code／API の 3 入口と、Opus／Sonnet／Haiku の役割分担です。

### 6. 深掘り先

Extended Thinking、Artifacts、MCP、Projects、ナーフ（G-46）。

## 開発フローでの位置（必須）

1. 企画整理 — Claude.ai で壁打ち・要件まとめ
2. 設計のドラフト — 同じく Claude.ai、または Projects に資料を集める
3. 実装 — Claude Code に降りて、ファイル編集・実行まで任せる
4. レビュー＆改善 — 差分を人が確認し、再度 Claude に直しを頼む

<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニア視点のつまずき

-
-
-

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

- 🙂 第一印象:
- 👍 良い点:
- 👎 ダメな点:
- 👥 誰に向くか:

<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: 中央に「Claude」のノード。3 本の枝が伸びて、それぞれ企画者・開発者・業務担当のキャラクターに繋がる
- 登場人物: 企画者（ラップトップ＋ふせん）／開発者（ターミナル画面）／業務担当（書類＋メール）
- 吹き出し・心の声: 各人に 1 行ずつ（「要点抜いて」「実装して」「自動分類したい」）
- 中央に置くキーワード: Claude ＝ ひとつのブランド／三つの入口
- シーン比較のポイント: 同じ AI を誰の手元でどう動かしているか

### 6視点アイコン（右ページ上段）

- 共通アイコン流用（① target / ② heart / ③ warning / ④ people / ⑤ magnifier / ⑥ chart-up）

### 開発フロー図（右ページ下段）

- Step 1: 対話吹き出し — Claude.ai
- Step 2: 設計メモ — Projects / ドキュメント
- Step 3: ターミナル `>` — Claude Code
- Step 4: 差分＋チェック — レビュー
- 矢印: 相談 → 設計 → 実装 → レビュー のループ

## コミュニティ補完メモ

Opus／Sonnet／Haiku の世代別詳細は D-12 Claude 4 系、D-13 Claude 4.5 系 で扱います。本エントリは「サービスとしての窓口」に絞ります。ナーフの一般論は G-46 を参照。

## 出典メモ

- Anthropic official site — checked 2026-04-23
- Claude.ai docs — checked 2026-04-23

## 備考

料金プランは B-50 Claude の料金プラン を参照。時変情報です。
