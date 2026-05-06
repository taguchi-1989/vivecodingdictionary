---
id: J-16
title: Fine-tuning
title_reading: ファインチューニング
category: term_general
subtype: ml_basic
experience_level: research_only
reader_level: 4-5
importance: C
figure_type: comparison
page_layout: spread_v1
start_date:
end_date:
version_status: active
pricing_note: paid
evaluation_date: 2026-04-29
related_terms:
  - LoRA
  - Prompt Engineering
  - Transformer
  - RAG
status: ready
---

# Fine-tuning

<!--
バイブコーディング図鑑 エントリー雛形 v2（2ページ見開き想定、iter 22 準拠）
-->

## tagline

事前学習済みモデルを特定ドメインのデータで追加学習し、挙動を寄せていく技術です。

<!-- 字数確認: 40字 -->


<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

汎用モデル（pre-trained model、事前学習済みモデル）が持つ知識をベースにしつつ、自社の専門用語や特定の文体・出力フォーマットを追加データで学ばせます。モデルの「素の反応」を目的に合わせて変えられます。

<!-- 字数確認: 93字 -->

## どこで出会うか

OpenAI や Google の API ドキュメントに「Fine-tuning」の章があり、業務システムに組み込む場面で登場します。Prompt で対応できないか試した後の選択肢として検討されることが多い技術です。

<!-- 字数確認: 89字 -->

## メイン図

### 図の狙い

Prompt Engineering との使い分けを対比で示す。少量データ・短期検証は Prompt、大量データ・恒常的な挙動変更は Fine-tuning という判断軸を掴んでもらう。

### A. Before / After（figure_type: before_after）

- Before
  - 状況: 汎用モデルに社内規約のコードを出力させようとする
  - 視覚要素: プロンプトに長い指示を書いても毎回ばらつく
  - つまずき: 毎回プロンプトを書き直す手間がかかる
- After
  - 状況: 社内コーディング規約データで Fine-tuning 済みのモデルを使う
  - 視覚要素: 指示なしでも規約に沿ったコードが返る
  - うれしさ: 出力が安定し、プロンプト設計の負担が減る


## 会話での使い方例

「社内 FAQ で fine-tuning するか、RAG で済ませるかを判断中です。」

<!-- 字数確認: 38字 -->


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

モデルの挙動をドメイン固有データで上書き・再調整します。

<!-- 27字 -->

### 2. うれしさ

毎回長いプロンプトを書かずに安定した出力が得られます。

<!-- 27字 -->

### 3. 注意点

データ収集・学習コストが大きく、軽い用途には過剰になります。

<!-- 29字 -->

### 4. どこで役立つか

専門用語・文体・フォーマット統一を恒常的に保ちたい場面。

<!-- 27字 -->

### 5. はじめに

Prompt で済むか Fine-tuning が必要かの判断軸を押さえます。

<!-- 29字 -->

### 6. 深掘り先

LoRA、RAG、Prompt Engineering

<!-- 23字 -->


## 開発フローでの位置（必須）

1. 課題整理 — Prompt Engineering や RAG で解決できるか先に評価します
2. データ準備 — ドメイン固有の入出力ペアを収集・クリーニングします
3. 手法選定 — フル Fine-tuning か PEFT（LoRA 等）かをコストで判断します
4. 学習実行 — API または自前環境でモデルを追加学習させます
5. 評価・展開 — 挙動が安定しているか検証してから本番に組み込みます


## 関連用語

- LoRA
- Prompt Engineering
- Transformer
- RAG


<!-- ━━━━━━━━ 著者記入欄（右ページ下段に印刷される／AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

- 性能の弱いモデルをファインチューニングして使おうとする人がいまだに多いですが、いまの最善策がそれなのかは慎重に考える必要があり、安易に飛びつくのは危ういと感じます

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

- 🙂 第一印象: GPT-3.5 の頃に企業利用を進めたい人がよく試していた、という印象です
- 👍 良い点: 短期間で見える成果が出せる場合、即効性のある選択肢になります
- 👎 ダメな点: より賢いモデルが出るたびに、過去のチューニング資産が無駄になりやすいです
- 👥 誰向けか: 安易に手を出さないほうが良い領域で、まずはサブエージェント設計などで代替できないかを検討すべき人向けです


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: comparison）

- 描く内容: Prompt Engineering と Fine-tuning の使い分けを 2 列対比で示す
- 登場人物: エンジニア（PM 風）が 2 つの選択肢の前で手を止めて考えている
- 吹き出し・心の声: 「少量データならプロンプトで十分かな…でも毎回書き直すのはつらい」
- 中央に置くキーワード/ラベル: 「Prompt か Fine-tuning か」
- Before / After の場合の対比ポイント: 左列＝Prompt（軽い・すぐ試せる）、右列＝Fine-tuning（重い・安定する）

### 6視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: チェックリストのアイコン
- Step 2 のアイコン/絵柄: データベース・テーブルのアイコン
- Step 3 のアイコン/絵柄: スケールまたは分岐矢印のアイコン
- Step 4 のアイコン/絵柄: 歯車・サーバのアイコン
- 矢印で示す流れの意図: 「検討 → 準備 → 判断 → 実行 → 検証」の一方向フロー


## コミュニティ補完メモ

- G-10 Prompt Engineering との住み分け: G-10 は「プロンプトの書き方・工夫」を扱う。Fine-tuning はモデル自体を変える手段で、G-10 を試した後の「次の選択肢」として位置づける
- J-21 LoRA との住み分け: LoRA は Fine-tuning の実装手法の 1 つ（PEFT）。本エントリは概念・判断軸を扱い、J-21 は技術詳細を扱う
- RAG との住み分け: RAG は学習コストなしで知識を拡張できる代替手段。本エントリの「どこで出会うか」で並列して言及する


## 出典メモ

- OpenAI Fine-tuning guide — <https://platform.openai.com/docs/guides/fine-tuning> — checked 2026-04-29
- Hugging Face PEFT documentation — <https://huggingface.co/docs/peft> — checked 2026-04-29


## 備考

- PEFT（Parameter-Efficient Fine-Tuning）の代表手法は LoRA（J-21）・QLoRA・Adapter 等。本エントリでは概念レベルにとどめ、技術詳細は J-21 で扱う
- 主要モデル（GPT・Claude・Gemini 等）の Fine-tuning API は提供されているが、提供状況・価格は時変情報。evaluation_date: 2026-04-29 時点での記述
- 「最新」「最先端」は使わない方針のため、性能優劣の記述は避けた
