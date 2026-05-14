---
id: J-73
title: Blackwell
title_reading: ブラックウェル
category: term_general
subtype: hardware
experience_level: research_only
reader_level: 3-4
importance: E
figure_type: timeline
page_layout: spread_v1
start_date: 2024-03-01
end_date:
version_status: active
pricing_note: paid
evaluation_date: 2026-04-30
related_terms:
  - NVIDIA
  - H100
  - GPU
  - VRAM
status: ready
---

# Blackwell

<!--
バイブコーディング図鑑 エントリー雛形 v2（2ページ見開き想定、iter 22 準拠）
-->

## tagline

NVIDIA が 2024 年 3 月に発表した GPU アーキテクチャ世代で、Hopper（H100）の後継です。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

B200 は HBM3e メモリと FP4 演算で AI の学習・推論性能を引き上げます。GB200 SuperChip は CPU と 2 GPU を統合し省電力と高密度実装を両立します。

## どこで出会うか

主要クラウド各社が 2024 年末から B200 / GB200 を順次提供しています。LLM の学習コストや推論速度を扱う業界記事で「Blackwell 世代」という表現を目にします。

## メイン図

### 図の狙い

NVIDIA GPU アーキテクチャの世代順（Volta → Turing → Ampere → Hopper → Blackwell）を示し、Blackwell の立ち位置を伝える。

## 会話での使い方例

「Blackwell の B200 が来てから、推論コストが目に見えて下がりました。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

LLM の学習・推論を担う NVIDIA GPU の 2024 年世代名です。

### 2. うれしさ

H100 比でAI 推論性能が向上し、クラウドの利用料が下がることがあります。

### 3. 注意点

製品が多く、B100・B200・GB200・B300・RTX 50 系で用途が異なります。

### 4. どこで役立つか

大規模 LLM の推論基盤選びやクラウド比較の文脈で登場します。

### 5. はじめに

科学者の名前に由来し、Hopper の次世代が Blackwell と押さえると整理しやすいです。

### 6. 深掘り先

H100、GPU、NVLink

## 開発フローでの位置（必須）

1. モデル選定 — 利用する LLM の推論要件（VRAM・速度）を確認する
2. インフラ選定 — B200 / GB200 対応クラウドの提供状況を調べる
3. 実行環境構築 — クラウド API または GPU インスタンスを確保する
4. 推論・学習実行 — Blackwell 世代の FP4 演算で処理を走らせる


## 関連用語

- NVIDIA
- H100
- GPU
- VRAM
- NVLink


<!-- ━━━━━━━━ 著者記入欄（右ページ下段に印刷される／AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

- マニアックな人でないと追いきれない話です。世界中で取り合いになっており、Intel の「●●レイク」のような世代名と同じく、覚えてもその時しか使えない、陳腐化しやすい固有名詞です
- 
- 

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

- 🙂 第一印象: 現状の最新世代の GPU で、名前がかっこいいなと思いました
- 👍 良い点: モデル側だけでなく、アーキテクチャの物理的進歩で推論コストが下がっていく流れは非常に好ましいです
- 👎 ダメな点: 実質、ロックインされているのでは、と感じる点
- 👥 誰向けか: 最先端の話題で会話する人向け


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: timeline）

- 描く内容: NVIDIA GPU 世代の横並びタイムライン（Volta → Turing → Ampere → Hopper → Blackwell）
- 登場人物（いれば）: エンジニア風の人物がタイムラインを指差して「ここが今！」と示す
- 吹き出し・心の声: 「Hopper の次が Blackwell ですね」「B200 でようやく推論コストが下がりました」
- 中央に置くキーワード/ラベル: Blackwell（強調）/ 2024〜2026

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: 虫眼鏡（要件確認）
- Step 2 のアイコン/絵柄: クラウドのアイコン（インフラ選定）
- Step 3 のアイコン/絵柄: サーバーラック（環境構築）
- Step 4 のアイコン/絵柄: 稲妻マーク（高速推論実行）
- 矢印で示す流れの意図: 「要件 → 選定 → 構築 → 実行」の線形フロー


## コミュニティ補完メモ

- J-72 H100 との住み分け：H100 は「Hopper 世代の代表製品」、Blackwell は「その次の世代アーキテクチャ名」。製品 vs 世代名の違いがある。本エントリは世代名の解説に絞り、製品スペック詳細は J-72 に委ねる
- J-77 GPU との住み分け：GPU は概念・総称、Blackwell は NVIDIA の特定世代名。どちらも知りたい読者は両方参照する前提で重複説明は省く

## 出典メモ

- NVIDIA GTC 2024 発表 — checked 2026-04-30
- NVIDIA 公式 Blackwell アーキテクチャページ <https://www.nvidia.com/en-us/data-center/technologies/blackwell-architecture/> — checked 2026-04-30


## 備考

- 命名由来：米国の数学者 David Blackwell（統計学・ゲーム理論）に因む。NVIDIA の GPU 世代名は科学者の名前（Volta / Turing / Ampere / Hopper / Blackwell）を慣例とする
- 製品ラインアップ（時変）：B100 / B200（データセンター）/ GB200（CPU + 2GPU 統合 SuperChip）/ B300 / RTX 50 系（コンシューマ）。詳細は evaluation_date 以降に変動の可能性がある
- 第 5 世代 NVLink で 1.8TB/s の帯域幅。スペック詳細は NVIDIA 公式を参照のこと
