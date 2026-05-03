---
id: D-41
title: Mistral 系
title_reading: ミストラル系
category: model
subtype: open
experience_level: research_only
reader_level: 3
importance: C
figure_type: timeline
page_layout: spread_v1
start_date: 2023
version_status: active
pricing_note: freemium
evaluation_date: 2026-04-29
related_terms:
  - オープンモデル
  - Llama
  - MoE
  - La Plateforme
  - ファインチューニング
status: drafting
---

# Mistral 系

## tagline

欧州発のオープンモデル代表。Apache 2.0 で自由に使えます。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

仏 Mistral AI が開発するテキスト生成モデル群です。Mixtral（Mixture of Experts、MoE）構造を採用した軽量から高性能まで複数の版があり、多くが Apache 2.0 ライセンスで公開されています。

## どこで出会うか

ローカル推論や社内 LLM の構築で Llama（D-40）と並んで候補に挙がります。GDPR（欧州の個人データ保護規則）対応が必要な場面で選ばれやすく、商用 API は La Plateforme（ラ・プラットフォーム）から利用できます。

## メイン図

### 図の狙い

Mistral 7B から Mistral Large までの系譜を時系列で示し、MoE 採用がどこで起きたかを 1 枚で捉えてもらいます。

## 会話での使い方例

「Mistral は Apache 2.0 なので、商用プロジェクトにも比較的組み込みやすいですよ。」

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

仏 Mistral AI 製のオープンモデル群。欧州発の代表格です。

### 2. うれしさ

Apache 2.0 で商用利用しやすく、欧州規制にも対応しやすいです。

### 3. 注意点

版ごとにライセンスが異なる場合があり、商用前に確認が必要です。

### 4. どこで役立つか

GDPR 対応が必要な社内システムやローカル推論の構築。

### 5. はじめに

Mixtral での MoE 採用と Apache 2.0 の自由度が差別化の要点です。

### 6. 深掘り先

MoE、Ollama、La Plateforme

## 開発フローでの位置（必須）

1. モデルを選ぶ — 軽量（Mistral 7B）か高性能（Mistral Large）か用途で選ぶ
2. 取得方法を決める — Hugging Face からダウンロードか La Plateforme の API か
3. ローカルで実行 — Ollama などで起動して動作を確認する
4. 必要に応じて調整 — ファインチューニングや量子化で用途に合わせる
5. アプリに組み込む — API サーバー化して他ツールから呼び出す

## 関連用語

- オープンモデル
- Llama
- MoE
- La Plateforme
- ファインチューニング

<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

- 名前がそもそもそんなに有名じゃない
- どこからどう使っていいのかの？手順がわかんない
- 

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

- 🙂 第一印象: オープンモデルとして報酬系だと一番先に名前が上がってくるベンダー
- 👍 良い点: オープンモデルで使ってまフロンティアに継ぐような性能がある点
- 👎 ダメな点: エコシステムないので使いづらいしデータセンター室だし
- 👥 誰向けか: LL のモデルを試し比較対象試したいとかベンチマーク取りたい人の


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: timeline）

- 描く内容: 横軸に時系列で「Mistral 7B → Mixtral 8x7B → Mixtral 8x22B → Mistral Small/Medium/Large」を矢印で結ぶ。Mixtral の位置に「MoE 採用」ラベルを添える
- 登場人物: 画面脇にエンジニアキャラクター。Mixtral を指差して「ここから構造が変わった」と吹き出し
- 吹き出し・心の声: 「Apache 2.0 だから商用でも使いやすい」（ライセンスの利点を短く）
- 中央に置くキーワード: Mistral 系 ＝ 欧州発・Apache 2.0 で自由なオープンモデル

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: モデルカードのアイコン（版選択）
- Step 2 のアイコン/絵柄: 分岐矢印（ダウンロード or API）
- Step 3 のアイコン/絵柄: PC + 歯車（ローカル起動）
- Step 4 のアイコン/絵柄: スライダー（調整・量子化）
- Step 5 のアイコン/絵柄: プラグアイコン（アプリ組み込み）


## コミュニティ補完メモ

- Llama（D-40）との住み分け：Llama は Meta 製で最も広く参照される系統、Mistral は欧州発で Apache 2.0 と GDPR 対応が独自色。どちらもオープンモデルだが出自と商用条件が異なる
- Mistral の版展開詳細（7B → Mixtral 8x7B → Mixtral 8x22B → Small/Medium/Large）は左ページから省いてここに記録。各版のライセンスが異なる場合があるため（例：一部モデルは BSL）商用前に要確認
- MoE の詳細（Mixture of Experts の仕組み）は J-18 スケルトンで扱う予定。本エントリでは「Mixtral で本格採用」という事実の注記にとどめる
- Gemma（D-42）・Qwen（D-43）は別系統のオープンモデル。本エントリは欧州発・Apache 2.0 の観点で差別化して書く

## 出典メモ

- mistral.ai — checked 2026-04-29
- Hugging Face: mistralai モデルページ — checked 2026-04-29

## 備考

モデル名・ライセンス・提供状況は時変情報です。Mistral AI は版ごとにライセンスが異なる場合があり（例：一部モデルは BSL ライセンス）、evaluation_date 2026-04-29 時点の情報として記録しています。本番利用前に公式ページを再確認します。La Plateforme の料金も時変情報のため pricing_note を freemium としています。
