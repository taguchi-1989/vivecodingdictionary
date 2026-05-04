---
id: J-75
title: Tensor コア
title_reading: テンサー コア
category: term_general
subtype: hardware
experience_level: research_only
reader_level: 4-5
importance: E
figure_type: structure
page_layout: spread_v1
start_date:
end_date:
version_status: active
pricing_note:
evaluation_date: 2026-04-30
related_terms:
  - GPU
  - H100
  - RTX シリーズ
  - 量子化
  - Neural Network
status: drafting
---

# Tensor コア

## tagline

NVIDIA GPU に搭載された行列演算専用の計算ユニットです。AI 学習・推論の速度を左右します。


<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

行列の掛け算（GEMM）を通常の汎用コアより高速に処理します。FP16・BF16・FP8 など低ビット幅の混合精度演算に対応しており、LLM の学習や推論で必要な大規模行列計算を短時間でこなせます。


## どこで出会うか

GPU スペック表や AI 学習環境の選定記事で「Tensor コア数 × 世代」として登場します。H100・RTX 40 シリーズ選びの際に「何 TFLOPS 出るか」を比較する場面が代表的です。世代が新しいほど対応精度のビット幅が広がり、推論速度の差に直結します。


## メイン図

### 図の狙い

GPU チップ内に「汎用コア（CUDA コア）」と「Tensor コア」が並存する構造を示し、行列演算だけを Tensor コアが担う流れを伝える。

### C. 概念図（figure_type: structure）

- 中心に置く概念: GPU チップ（中央ブロック）
- 周辺の要素: CUDA コア群 / Tensor コア群 / 行列入力 A・B / 出力 C / FP16 ラベル
- 関係の描き方: 行列データが Tensor コアに流れ込む矢印、CUDA コアとの役割分担を色分け


## 会話での使い方例

「H100 は Tensor コアが FP8 対応なので、訓練速度が前世代と段違いです。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

GPU 内で行列演算だけを高速処理する専用ユニットです。

### 2. うれしさ

LLM 学習・推論の所要時間が大幅に短縮できます。

### 3. 注意点

世代ごとに対応精度が異なり、FP8 は H100 以降でのみ有効です。

### 4. どこで役立つか

GPU 選定や訓練コスト試算の場面で判断基準になります。

### 5. はじめに

「行列演算を速くする専用コア」という役割を押さえれば十分です。

### 6. 深掘り先

GPU、H100、量子化


## 開発フローでの位置（必須）

1. モデル設計 — 学習に必要な行列演算の規模を見積もる
2. GPU 選定 — Tensor コアの世代・対応精度を確認して機材を決める
3. 混合精度設定 — FP16 / BF16 / FP8 を指定して Tensor コアを有効活用する
4. 学習・推論実行 — Tensor コアが GEMM を処理し、スループットが上がる
5. コスト評価 — 速度向上と GPU 費用を比較して世代差を判断する


## 関連用語

- GPU
- H100
- RTX シリーズ
- 量子化
- Neural Network


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

- 描く内容: GPU チップ内の CUDA コアブロックと Tensor コアブロックを並置し、行列データが Tensor コアに流れ込む様子を図示する
- 登場人物: AI エンジニア風の人物が行列データを Tensor コアに「投げ込む」ポーズ
- 吹き出し・心の声: 「FP16 でガンガン回そう」／「CUDA コアより速い！」
- 中央に置くキーワード/ラベル: Tensor コア（FP16 / BF16 / FP8 対応）

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: 設計図（行列サイズの概略図）
- Step 2 のアイコン/絵柄: GPU チップの選択画面
- Step 3 のアイコン/絵柄: 精度設定スライダー（FP32 → FP16）
- Step 4 のアイコン/絵柄: 高速処理中の GPU（稲妻マーク）
- 矢印で示す流れの意図: 設計 → 機材選定 → 精度指定 → 実行の順で Tensor コアが活きることを伝える


## コミュニティ補完メモ

- J-77 GPU との住み分け：GPU はチップ全体を指す総称で、Tensor コアは GPU 内の専用ユニット。「GPU を選ぶ」話は J-77 で、「その GPU に搭載された演算コア」の話が本エントリ
- J-72 H100 との住み分け：H100 は GPU 製品名（ハードウェア機材）、Tensor コアはその内部構造。H100 の性能の源泉として参照関係になる
- J-74 RTX シリーズとの住み分け：RTX はコンシューマー向け GPU ファミリー。Tensor コア搭載は RTX 20 以降という歴史的事実を補足
- AMD Matrix Cores・Intel AMX・Google TPU MXU は競合技術として備考に留め、本エントリでは NVIDIA Tensor コアに絞る


## 出典メモ

- NVIDIA Tensor Core 公式ページ https://www.nvidia.com/en-us/data-center/tensor-cores/ — checked 2026-04-30
- NVIDIA Hopper アーキテクチャホワイトペーパー（FP8 サポート記載） — checked 2026-04-30
- NVIDIA Volta アーキテクチャホワイトペーパー（初代 Tensor コア V100 記載） — checked 2026-04-30


## 備考

- Tensor コアは 2017 年 Volta（V100）で初登場、Turing（RTX 20 シリーズ）以降コンシューマー向けにも展開
- 世代別対応精度の目安：Volta FP16 → Ampere BF16 / INT8 → Hopper FP8 → Blackwell FP4
- AMD の Matrix Cores（CDNA アーキテクチャ）、Intel の AMX（Advanced Matrix Extensions）、Google TPU の MXU（Matrix Multiply Unit）が競合技術として存在するが、本エントリは NVIDIA Tensor コアに限定
- FP4 は Blackwell（GB200 / RTX 50 シリーズ）からネイティブサポート開始（2025 年時点）
