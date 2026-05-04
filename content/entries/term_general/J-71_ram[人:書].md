---
id: J-71
title: RAM
title_reading: ラム
category: term_general
subtype: hardware
experience_level: research_only
reader_level: 2-3
importance: D
figure_type: comparison
page_layout: spread_v1
start_date:
end_date:
version_status:
pricing_note:
evaluation_date: 2026-04-30
related_terms:
  - VRAM
  - CPU
  - HDD
  - SSD
status: needs_review
---

# RAM

## tagline

Random Access Memory の略。CPU が作業中データを一時保管する高速メモリです。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

CPU が実行中のプログラムやデータを置く場所です。起動中のアプリや開いているファイルは RAM 上に展開されます。電源を切ると消える揮発性メモリで、永続保存は SSD などが担います。

## どこで出会うか

PC のスペック表で「16GB RAM」と表記されます。ローカル LLM（大規模言語モデル）をノート PC で動かす際、「CPU 推論なら RAM 容量が要る」という文脈で目にします。Apple Silicon の Unified Memory も同種です。

## メイン図

### 図の狙い

RAM・VRAM・ストレージの 3 階層を横並びで示し、「どのチップが使う一時領域か」を一目でわかるようにする。

### B. 登場シーン（figure_type: comparison）

- シーン1: CPU がアプリを実行中 — RAM 上にデータが広がっている様子
- シーン2: GPU が LLM を推論中 — VRAM 上にモデルが乗っている様子
- シーン3: 電源を切ったとき — RAM も VRAM も空になり、SSD だけデータが残る
- 並べる基準: どのチップが使う一時領域か（CPU 用 vs GPU 用 vs 永続）

## 会話での使い方例

「Llama を CPU だけで動かすなら、RAM が 64GB あると 7B モデルが快適です。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

CPU が実行中データを一時的に置く高速メモリです。

### 2. うれしさ

容量が多いほど大きなモデルや多タスクを捌けます。

### 3. 注意点

電源断でデータは消える揮発性。永続保存は SSD 等が担います。

### 4. どこで役立つか

ローカル LLM の CPU 推論で RAM 容量がボトルネックになります。

### 5. はじめに

RAM は CPU 用、VRAM は GPU 用と分けて覚えると混乱が減ります。

### 6. 深掘り先

VRAM、CPU、SSD

## 開発フローでの位置（必須）

1. 環境選定 — ローカル LLM 実行に必要な RAM 容量を確認する
2. モデル読み込み — LLM のウェイトを RAM 上に展開する（CPU 推論時）
3. 推論実行 — CPU が RAM 上のデータを参照しながらトークンを生成する
4. セッション終了 — RAM 上の展開データは解放され、次回起動時に再ロードする

## 関連用語

- VRAM（GPU 用一時メモリ）
- CPU（RAM の主な利用者）
- HDD / SSD（永続ストレージ）


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

- 描く内容: 横 3 列の比較表。左列「RAM（CPU 用）」中列「VRAM（GPU 用）」右列「SSD（永続）」をそれぞれ棚の絵で表現する
- 登場人物（いれば）: 作業机に座るエンジニア風の人物 1 名。机の上が RAM、引き出しが SSD のイメージ
- 吹き出し・心の声: 「机の上（RAM）は広いと作業しやすい！」「引き出し（SSD）は電源切っても消えない」
- 中央に置くキーワード/ラベル: RAM vs VRAM vs SSD の 3 階層ラベル

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: チェックリスト（環境選定）
- Step 2 のアイコン/絵柄: 下矢印＋RAM チップ（モデル読み込み）
- Step 3 のアイコン/絵柄: CPU と RAM の往復矢印（推論実行）
- Step 4 のアイコン/絵柄: 電源ボタン（セッション終了）
- 矢印で示す流れの意図: RAM がローカル LLM 推論のライフサイクルの中心にあることを示す


## コミュニティ補完メモ

- J-70 VRAM との住み分け: J-70 は GPU 用一時メモリで LLM 推論のボトルネックになる文脈。J-71（本エントリ）は CPU 用一時メモリで CPU 推論・一般 PC 用途を扱う。Apple Silicon の Unified Memory は両者を共有する例外として備考に記載
- J-78 HDD・J-79 SSD との住み分け: J-78/79 は永続ストレージ。RAM は一時メモリで役割が異なる。本エントリでは「揮発性 vs 永続性」の対比に留め、詳細は J-78/79 に委ねる

## 出典メモ

- PC スペック表記の慣例（一般知識） — checked 2026-04-30
- Apple Silicon Unified Memory: <https://developer.apple.com/documentation/apple-silicon> — checked 2026-04-30

## 備考

- 容量例（2026-04 時点）: 一般的なノート PC で 16〜32GB、ハイエンドで 64〜128GB、サーバ用は 1TB 超も一般的。時変情報のため evaluation_date で管理
- Apple Silicon の Unified Memory は CPU と GPU（Neural Engine 含む）がメモリを共有する設計。RAM と VRAM の区別が曖昧になるため、本文では「RAM の一種」と簡略化し、詳細は備考に記載
- title は略称 RAM のみとし、旧スケルトンの「RAM (メモリ)」から変更
