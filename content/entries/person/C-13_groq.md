---
id: C-13
title: Groq
title_reading: グロック
category: person_org
subtype: company
experience_level: research_only
reader_level: 3-4
importance: C
figure_type: structure
page_layout: spread_v1
start_date: 2016-01-01
version_status: active
pricing_note: freemium
evaluation_date: 2026-04-30
related_terms:
  - NVIDIA
  - Llama 系
  - Grok 系
  - GroqCloud
status: drafting
---

# Groq

## tagline

LPU（Language Processing Unit）を開発する AI 推論専用チップ企業です。GPU とは異なる設計で LLM の推論速度を大幅に引き上げます。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

LPU と呼ぶ独自設計の推論専用チップで、LLM（大規模言語モデル）の出力を超低レイテンシで実行します。GroqCloud API 経由で Llama・Mixtral・DeepSeek などのオープンウェイトモデルを利用でき、OpenAI 互換 API として接続できます。


## どこで出会うか

「GPU 以外で LLM を動かす選択肢」として技術記事や API 比較記事で名前を見かけます。リアルタイム翻訳・チャットボット・コーディング補助など、応答速度が重視される用途で GroqCloud の導入事例が紹介される場面で出会います。


## メイン図

### 図の狙い

GPU ベースの推論と LPU ベースの推論を速度・構造の観点で対比し、Groq の立ち位置を示す。

### B. 登場シーン（figure_type: structure）

- シーン1: エンジニアが API の速度比較をして GroqCloud を選ぶ
- シーン2: スタートアップが低レイテンシのチャット API 基盤を探している
- シーン3: AI チップ業界の比較記事で NVIDIA と並べて紹介される
- 並べる基準: 用途（速度重視 API／チップ設計の違い）


## 会話での使い方例

「Groq の LPU を使うと Llama の推論が速いので、リアルタイム翻訳のバックエンドに乗せました。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

LLM 推論専用チップ LPU を設計・提供する AI スタートアップです。

### 2. うれしさ

GPU 推論より高速なレスポンスが得られる場面があります。

### 3. 注意点

xAI の Grok（D-30）と社名・読みが似ており混同されやすいです。

### 4. どこで役立つか

低レイテンシが必要なリアルタイム API 連携の検討場面で役立ちます。

### 5. はじめに

「LPU = 推論専用チップ、GroqCloud = その API サービス」と押さえます。

### 6. 深掘り先

NVIDIA, LPU, GroqCloud


## 開発フローでの位置（必須）

1. 要件確認 — 応答速度要件を整理し、GPU 推論との比較が必要か判断します
2. API 選定 — GroqCloud の無料枠で速度・料金を OpenAI 互換 API と比較します
3. 実装 — OpenAI 互換 API として既存コードのエンドポイントを差し替えます
4. 検証 — レイテンシ計測と出力品質を確認し、本番移行を判断します


## 関連用語

- NVIDIA
- Llama 系
- Grok 系
- GroqCloud


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

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: GPU と LPU の推論フローを横並びで比較する構造図
- 登場人物: エンジニア（開発者）が左側に立ち、どちらの箱を選ぶか迷っている
- 吹き出し・心の声: 「速度が要るならこっちかな…」と GPU・LPU の箱を見比べる
- 中央に置くキーワード/ラベル: LPU vs GPU

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: チェックリスト（要件確認）
- Step 2 のアイコン/絵柄: 天秤（API 選定）
- Step 3 のアイコン/絵柄: コード画面（実装）
- Step 4 のアイコン/絵柄: グラフ（検証）
- 矢印で示す流れの意図: 速度要件の確認から選定・実装・検証までの一連の流れ

## コミュニティ補完メモ

- C-9 NVIDIA との住み分け：NVIDIA は GPU 全般を扱う大手半導体企業。Groq は LLM 推論専用チップに特化したスタートアップで、NVIDIAの GPU 市場に対するオルタナティブとして位置づける
- D-30 Grok 系との住み分け：Grok は xAI（Elon Musk）が開発した LLM モデル。Groq（Jonathan Ross 設立）はチップ・インフラ企業で別物。名前の類似性は混乱の原因になるため、注意点に明記する
- C-14 AMD との住み分け：AMD は汎用 GPU・CPU を手がける大手。Groq は推論専用チップに絞った設計思想が異なる

## 出典メモ

- [groq.com](https://groq.com/) — checked 2026-04-30
- [GroqCloud OpenAI 互換 API ドキュメント](https://console.groq.com/docs/openai) — checked 2026-04-30


## 備考

- 設立: 2016 年、創業者 Jonathan Ross（元 Google TPU 開発リーダー）
- Grok（xAI / D-30）との混同注意: Musk の xAI が後発で類似名称を使用した経緯あり
- 速度実績: Llama 3.1 70B で 750 tok/sec 前後（GPU 比較として 2024 年時点の公開データ。時変情報のため要確認）
- Cerebras・SambaNova と並ぶ AI チップ専業スタートアップ層の一社
