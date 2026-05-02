---
id: J-74
title: RTX シリーズ
title_reading: アールティーエックス シリーズ
category: term_general
subtype: hardware
experience_level: hands_on
reader_level: 2-3
importance: D
figure_type: comparison
page_layout: spread_v1
start_date: 2018-09
end_date:
version_status: active
pricing_note: paid
evaluation_date: 2026-04-30
related_terms:
  - GPU
  - VRAM
  - Tensor コア
  - H100
  - Ollama
status: needs_review
---

# RTX シリーズ

## tagline

NVIDIA のコンシューマー向け GPU シリーズです。ローカル LLM 動作の主役でもあります。


<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

GeForce RTX は GPU（グラフィクス処理装置）の製品ラインです。画像描画だけでなく、AI 推論に必要な並列計算を担います。搭載 VRAM が大きいほど、より大きなモデルをローカルで動かせます。

## どこで出会うか

Ollama などでローカル LLM を試す際に「RTX 4090 なら 70B モデルが動く」といった文脈で登場します。PC スペック紹介記事やセットアップガイドでも、GPU の型番として目にします。

## メイン図

### 図の狙い

世代ごとの VRAM 容量と「動かせるモデル規模」の対応を示し、どの RTX を選ぶと何ができるかを伝えます。

### B. 登場シーン（figure_type: comparison）

- シーン1: RTX 4060（8GB）— 7B クラスのモデルを Ollama で動かす
- シーン2: RTX 4090（24GB）— 70B クラスのモデルをローカルで推論する
- シーン3: RTX 5090（32GB）— より大きなモデルや高精度推論に余裕を持たせる
- 並べる基準: VRAM 容量と動かせるモデル規模


## 会話での使い方例

「RTX 4090 なら VRAM が 24GB あるので、70B モデルもローカルで動きます。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

AI 推論に使える並列計算リソースを PC に提供します。

### 2. うれしさ

クラウドなしでもローカル LLM を動かせる環境が整います。

### 3. 注意点

VRAM 不足だとモデルが起動しないか、速度が極端に落ちます。

### 4. どこで役立つか

Ollama や LM Studio などでのローカル推論セットアップ時に重要です。

### 5. はじめに

世代名（40 系など）と VRAM 容量の 2 点を押さえれば判断できます。

### 6. 深掘り先

VRAM、Tensor コア、H100


## 開発フローでの位置（必須）

1. PC 選定 — RTX シリーズの世代と VRAM 容量を確認する
2. 環境構築 — GPU ドライバと CUDA をインストールする
3. モデル選択 — VRAM に収まる規模のモデルを選ぶ
4. ローカル推論 — Ollama などで LLM を起動して動作確認する
5. スケール判断 — 速度や精度が不足なら上位 GPU かクラウドを検討する


## 関連用語

- GPU
- VRAM
- Tensor コア
- H100
- Ollama


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

- 描く内容: RTX 4060 / 4090 / 5090 の 3 列を横並びにして、各 GPU の VRAM 容量と「動かせるモデル規模」をラベルで示す比較表
- 登場人物: PC の前に座る人物（非エンジニア想定）
- 吹き出し・心の声: 「VRAM 24GB なら 70B も動くんですね」
- 中央に置くキーワード/ラベル: VRAM 容量 / 動かせるモデル規模

### 6視点アイコン（右ページ上段）

- 共通アイコン流用

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: PC 選定（ショッピングカート）
- Step 2 のアイコン/絵柄: ドライバ設定（ギア）
- Step 3 のアイコン/絵柄: モデル選択（ダウンロード矢印）
- Step 4 のアイコン/絵柄: LLM 起動（ロケット）
- 矢印で示す流れの意図: ハード選定から推論完了までの一本道


## コミュニティ補完メモ

- J-72 H100 との住み分け: H100 はデータセンター用のサーバー GPU（HGX 基板実装）で個人購入の対象外。RTX はコンシューマー／クリエイター向け。「個人で買えるか」が境界線。
- J-77 GPU との住み分け: GPU は総称、RTX シリーズはその中の NVIDIA 製品ラインの一つ。GPU の説明は J-77 に任せ、ここは RTX 固有の世代進化・VRAM 選択に絞る。
- J-75 Tensor コア との関係: RTX シリーズに搭載される AI 演算専用ユニット。詳細は J-75 へ。
- J-70 VRAM との関係: RTX 選定の主指標。詳細は J-70 へ。


## 出典メモ

- NVIDIA GeForce RTX 公式 https://www.nvidia.com/ja-jp/geforce/graphics-cards/ — checked 2026-04-30
- RTX 50 シリーズ（Blackwell）発表 https://www.nvidia.com/ja-jp/geforce/graphics-cards/50-series/ — checked 2026-04-30


## 備考

- 価格は時変情報。RTX 4090 24GB は 2026-04 時点で国内市場 30 万円前後、RTX 5090 32GB は 50 万円前後（evaluation_date 参照）。
- RTX 20 シリーズ（Turing、2018-09）が Tensor コア初搭載の起点。以降 30（Ampere）→ 40（Ada Lovelace）→ 50（Blackwell）と継代。
- DLSS（ディープラーニング超解像）やレイトレーシングはゲーム向け機能で、AI 推論用途とは別の価値軸。本エントリではローカル LLM 用途にスコープを絞っている。
