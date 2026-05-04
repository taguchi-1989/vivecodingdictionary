---
id: J-80
title: SATA
title_reading: シリアルエーティーエー
category: term_general
subtype: hardware
experience_level: research_only
reader_level: 2-3
importance: E
figure_type: comparison
page_layout: spread_v1
start_date:
end_date:
version_status: active
pricing_note: none
evaluation_date: 2026-04-30
related_terms:
  - HDD
  - SSD
  - M.2
  - NVMe
status: needs_review
---

# SATA

## tagline

Serial ATA の略。HDD や SSD とマザーボードをつなぐ内蔵ストレージ用の接続規格です。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

PC 内部で HDD や SSD をマザーボードに接続する規格で、データ転送と電源供給を担います。7 ピンのデータケーブルと 15 ピンの電源ケーブルを使い、L 字コネクタが目印。現行主流は SATA 3.0（6Gbps）です。


## どこで出会うか

デスクトップやノート PC の内部、または SSD を選ぶ際の「SATA SSD」「NVMe SSD」表記で目にします。ローカル LLM 用 PC を自作・増設するとき、インターフェース選択の場面でも登場します。


## メイン図

### 図の狙い

SATA と NVMe の速度差を視覚的に並べ、用途に応じた選択基準を伝える。

### B. 登場シーン（figure_type: comparison）

- シーン1: SATA SSD — 最大 6Gbps、一般作業・動画編集に十分
- シーン2: NVMe SSD（PCIe Gen4）— 最大 64Gbps 相当、LLM の頻繁ロードに有利
- シーン3: HDD + SATA — 大容量保存用途で現役
- 並べる基準: 転送速度と用途の対応


## 会話での使い方例

「LLM を頻繁にロードするなら SATA より NVMe の方が体感が変わります。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

HDD や SSD をマザーボードに接続する標準規格です。

### 2. うれしさ

互換性が広く、交換・増設が手軽にできます。

### 3. 注意点

NVMe と比べると転送速度は数倍〜10 倍以上の差があります。

### 4. どこで役立つか

ローカル LLM 用 PC 構成でストレージ選択の判断に役立ちます。

### 5. はじめに

SATA SSD と NVMe SSD の速度差を把握しておくと選択が楽になります。

### 6. 深掘り先

NVMe、M.2、PCIe


## 開発フローでの位置（必須）

1. PC 構成を決める — SATA か NVMe か、用途・予算でインターフェースを選択します
2. ストレージを取り付ける — SATA ケーブルとマザーボードのポートを接続します
3. OS・環境を構築する — SSD にシステムを入れてローカル環境を整えます
4. モデルをロードして動作確認 — SATA SSD では速度上限を意識して運用します


## 関連用語

- HDD（接続元）
- SSD（接続元）
- M.2（形状規格）
- NVMe（高速規格）


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

- 描く内容: SATA SSD と NVMe SSD の速度バーを横並びで比較する図。左に SATA（6Gbps）、右に NVMe PCIe Gen4（64Gbps 相当）をバーグラフで示す
- 登場人物: PC を前に考え込む人物（ストレージ選びに迷っている表情）
- 吹き出し・心の声: 「SATA で足りる？ NVMe にすべき？」
- 中央に置くキーワード/ラベル: SATA 3.0（6Gbps） vs NVMe Gen4（〜64Gbps）

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: 設計図・チェックリスト
- Step 2 のアイコン/絵柄: ケーブル接続
- Step 3 のアイコン/絵柄: PC 起動・OS インストール
- Step 4 のアイコン/絵柄: モデルとメーター（速度確認）


## コミュニティ補完メモ

- J-79（SSD）との住み分け：SSD はストレージそのものの説明。SATA はその接続インターフェース規格の説明。SSD エントリでは「SATA 接続か NVMe 接続かで速度が変わる」と触れ、本エントリはインターフェース側の詳細を担う
- J-81（M.2）との住み分け：M.2 はフォームファクター（形状規格）。M.2 スロットに SATA 接続の SSD を挿す場合と NVMe 接続の SSD を挿す場合があり、混同しやすい点は J-81 エントリで扱う
- J-78（HDD）との住み分け：HDD は記憶媒体そのもの。HDD が SATA で接続されるという関係性に留める

## 出典メモ

- Serial ATA International Organization (SATA-IO) — checked 2026-04-30
- Wikipedia「Serial ATA」— checked 2026-04-30


## 備考

- SATA Express（10Gbps / 16Gbps）は規格として存在するが普及しなかった。PCIe / NVMe への移行が進んだため、現行市場では SATA 3.0 が実質的な現役バージョン
- HDD 向けには SATA が今もほぼ唯一の選択肢。SSD は NVMe が主流になりつつあるが、コスト重視の構成では SATA SSD も現役
- title_reading は略称音読み「サタ」としているが、正式読みは「シリアルエーティーエー」。誌面では YAML の title_reading 値が表示される
