---
id: J-18
title: MoE
title_reading: ミクスチャーオブエキスパーツ
category: term_general
subtype: ml_basic
experience_level: research_only
reader_level: 4
figure_type: structure
page_layout: spread_v1
start_date:
end_date:
version_status:
pricing_note:
evaluation_date: 2026-04-29
related_terms:
  - Transformer
  - LLM
  - Mixtral
  - DeepSeek
  - ファインチューニング
status: drafting
---

# MoE

## tagline

Mixture of Experts の略。モデル内の複数の「専門家」から少数だけを選んで推論する設計です。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

入力ごとに Router（ルーター、振り分け係）が少数の Expert（エキスパート、専門サブネットワーク）だけを起動し、残りを休ませます。総パラメータ数は大きくても、実際に使う部分は少なくて済むため、性能とコストを両立できます。

## どこで出会うか

「MoE アーキテクチャ採用」という表現で、Mixtral や DeepSeek V3 の技術紹介に登場します。LLM（大規模言語モデル）の比較記事で「スパース MoE」と書かれているとき、この仕組みを指しています。

## メイン図

### 図の狙い

入力がルーターで振り分けられ、少数の専門家ネットワークだけが動く構造を、人物の驚きとともに見せます。

### C. 概念図（figure_type: structure）

- 中心に置く概念: Router（ルーター）
- 周辺の要素: Expert 1〜N（専門サブネット）、アクティブ Expert（2〜4 個）、休止 Expert（大多数）
- 関係の描き方: 入力 → Router → 選ばれた Expert → 出力の矢印フロー。休止 Expert はグレーアウト

## 会話での使い方例

「MoE はルーターが Expert を選ぶ分、密なモデルより推論コストが抑えられます。」

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

入力ごとに少数の専門家を選び、全体の効率を高めます。

### 2. うれしさ

総パラメータが大きくても推論コストを抑えられます。

### 3. 注意点

ルーティングが不安定になると特定 Expert に偏りが生じます。

### 4. どこで役立つか

大規模モデルの性能を維持しながらコストを下げたいときに有効です。

### 5. はじめに

「Router が Expert を選ぶ」という大枠だけまず押さえれば十分です。

### 6. 深掘り先

Transformer（J-13）、LLM（J-14）、Mixtral（D-41）

## 開発フローでの位置（必須）

1. アーキテクチャ選択 — 密なモデルか MoE かをパラメータ規模と予算を踏まえて決めます。
2. Expert 設計 — Expert の数とルーティング方式（Top-k など）を決定します。
3. 事前学習 — 大量データで Router と各 Expert の重みを同時に調整します。
4. 推論・評価 — アクティブ Expert 数を確認しながら速度とコストを検証します。
5. 利用 — API やサービスを通じて LLM として呼び出します。

## 関連用語

- Transformer
- LLM
- Mixtral
- DeepSeek
- ファインチューニング

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

- 描く内容: 中央に Router ボックスを置き、左から入力矢印が入る。右へ Expert 1〜8 が並び、そのうち 2〜3 個だけが青くハイライトされ、残りはグレーアウト。選ばれた Expert から右へ出力矢印。
- 登場人物: 非エンジニアの人物が図を見て「え、これだけ動くの？」と驚くシーン
- 吹き出し・心の声: 人物の吹き出し「全部じゃなくて一部だけ動くんだ」。Router ボックスに「誰を呼ぶか決める」ラベル。アクティブ Expert に「今回の担当」ラベル。
- 中央に置くキーワード/ラベル: Router

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: 設計図・天秤アイコン（密 vs MoE の選択）
- Step 2 のアイコン/絵柄: 歯車グループアイコン（Expert 設計）
- Step 3 のアイコン/絵柄: 本・データの山アイコン（事前学習）
- Step 4 のアイコン/絵柄: スピードメーターアイコン（推論・評価）
- Step 5 のアイコン/絵柄: API コール矢印アイコン（利用）
- 矢印で示す流れの意図: 設計 → 構成 → 学習 → 検証 → 運用というモデル開発の大枠

## コミュニティ補完メモ

- Transformer（J-13）との住み分け：J-13 はアーキテクチャの骨格（Attention の仕組み）。J-18 は「その骨格に複数の専門家を組み込む設計パターン」に絞る。
- LLM（J-14）との住み分け：J-14 はサービス・利用視点。J-18 は実装レベルの効率化手法に絞る。
- Mixtral（D-41）との住み分け：D-41 は Mistral 社の具体的サービス。J-18 は MoE という設計概念の説明に留め、採用例として Mixtral・DeepSeek V3 を参照するにとどめる。
- DeepSeek V3（D-46）との住み分け：D-46 は DeepSeek 社のモデル詳細。J-18 では「MoE 採用の代表例」として名前を出すのみ。

## 出典メモ

- Shazeer et al., "Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer", arXiv:1701.06538 — checked 2026-04-29
- Mistral AI, "Mixtral of Experts", mistral.ai/news — checked 2026-04-29
- DeepSeek-V3 Technical Report, deepseek.com — checked 2026-04-29

## 備考

- MoE は略称のため tagline 冒頭に「Mixture of Experts の略。」を入れた。
- 「スパース MoE」「Dense MoE」の詳細な区別はコミュニティ補完メモへ逃がした。
- GPT-4 が MoE を採用しているとの噂は未確認情報のため本文には含めていない。
