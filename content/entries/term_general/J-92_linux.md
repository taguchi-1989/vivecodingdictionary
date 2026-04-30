---
id: J-92
title: Linux
title_reading: リナックス
category: term_general
subtype: ui_os
experience_level: partial
reader_level: 2-3
figure_type: structure
page_layout: spread_v1
start_date: 1991-10-01
version_status: active
pricing_note: none
evaluation_date: 2026-04-30
related_terms:
  - Ubuntu
  - bash
  - WSL
  - GPL
status: drafting
---

# Linux

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## tagline

1991 年に公開されたオープンソースの Unix 系 OS カーネルです。サーバ・AI 基盤・組込み機器の土台として広く使われています。

## 何をしてくれるか

CPU やメモリなどのハードウェアを管理し、アプリが動く土台を提供します。カーネル単体ではなく、GNU ツールやデスクトップ環境と組み合わせた「ディストリビューション（distro）」として配布されることがほとんどです。

## どこで出会うか

AI モデルの学習・推論サーバはほぼ Linux 上で動いています。Docker（F-90）や Kubernetes もこの OS を前提としており、クラウドやバイブコーディングのインフラを調べると必ず名前が出ます。Windows 上では WSL（F-82）を使って触れることができます。

## メイン図

### 図の狙い

Linux カーネルがハードウェアとアプリケーション層の間に位置し、様々なディストリビューションがその上に乗る構造を示す。

### C. 概念図（figure_type: structure）

- 中心に置く概念: Linux カーネル
- 周辺の要素: Ubuntu / Fedora / RHEL / Android / Docker / WSL
- 関係の描き方: カーネルを中央に置き、各ディストリや用途が外側に包含される同心円

## 会話での使い方例

「サーバは Linux 一択ですが、開発機は WSL でも十分です。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

ハードウェアとアプリの間を仲介する OS カーネルです。

### 2. うれしさ

無償で使え、サーバから組込みまで幅広く動かせます。

### 3. 注意点

「Linux」はカーネルだけで、使うにはディストリビューションを選ぶ必要があります。

### 4. どこで役立つか

AI サーバ・クラウド・Docker など、開発インフラのほぼ全域で必要です。

### 5. はじめに

ディストリビューションの概念と Ubuntu・WSL の存在を押さえると入りやすいです。

### 6. 深掘り先

Ubuntu（J-93）、bash（F-81）、WSL（F-82）

## 開発フローでの位置（必須）

1. インフラ選定 — クラウドやサーバの OS として Linux ディストリを選ぶ
2. 環境構築 — Ubuntu や WSL 上に開発ツール・Docker を導入する
3. 開発・実行 — bash コマンドでビルド・テスト・デプロイを操作する
4. 本番運用 — AI 推論サーバや Web サーバが Linux 上で常時稼働する

## 関連用語

- Ubuntu
- bash
- WSL
- GPL


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

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: Linux カーネルを中央の円に、外側リングに Ubuntu / Fedora / Android / Docker / WSL を配置した同心円図
- 登場人物: エンジニア風の人物がサーバラックを前に立っている
- 吹き出し・心の声: 「クラウドもスマホも、土台は全部 Linux でした」
- 中央に置くキーワード/ラベル: Linux Kernel

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: サーバ選定（クラウドアイコン）
- Step 2 のアイコン/絵柄: 環境構築（端末アイコン）
- Step 3 のアイコン/絵柄: bash 操作（コマンドラインアイコン）
- Step 4 のアイコン/絵柄: 本番稼働（サーバ常時稼働アイコン）
- 矢印で示す流れの意図: 選定から本番まで Linux が一貫して使われる流れ


## コミュニティ補完メモ

- Ubuntu（J-93）との住み分け：J-92 Linux はカーネルと「ディストリ全体」の概念を扱う。J-93 Ubuntu は Ubuntu ディストリ固有の特徴（apt / LTS / 入門向け）を扱う
- bash（F-81）との住み分け：Linux は OS 基盤、bash はその上で動くシェル。セットで参照される
- WSL（F-82）との住み分け：WSL は Windows から Linux を使う手段。Linux の概念説明は本エントリで行い、WSL はアクセス手段として F-82 に委ねる
- GPL（F-152）との住み分け：Linux が GPL v2 でライセンスされる事実は tagline で触れる程度にとどめ、ライセンス詳細は F-152 に委ねる

## 出典メモ

- <https://www.kernel.org/> — checked 2026-04-30
- <https://top500.org/statistics/details/osfam/1/> — TOP500 Linux 100% — checked 2026-04-30
- <https://source.android.com/docs/core/architecture> — Android カーネルが Linux — checked 2026-04-30

## 備考

- Linux カーネルは 1991-10-01 に Linus Torvalds が Usenet に投稿して公開。GPL v2 ライセンス
- Linus Torvalds は BDFL（終身慈悲深い独裁者）として核心部を統括、Linux Foundation が運営支援
- TOP500 スーパーコンピュータは 2017 年以降 100% Linux（時点によって変わる可能性があるため evaluation_date を参照）
- デスクトップ用途では Ubuntu、Pop!_OS など GUI 中心のディストリも多い。「黒い画面」のみではない点を読者に伝える
