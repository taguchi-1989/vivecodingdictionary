---
id: J-14
title: LLM（大規模言語モデル）
category: term_general
subtype: ml_basic
experience_level: hands_on
reader_level: 1
figure_type: structure
page_layout: spread_v1
version_status: active
evaluation_date: 2026-04-23
related_terms:
  - Transformer
  - Token
  - Neural Network
  - Context
  - Fine-tuning
  - VLM
status: drafting
---

# LLM（大規模言語モデル）

## tagline

日本語では「大規模言語モデル」と訳されます。膨大な文章で訓練された、言葉を扱う AI の現在の主流です。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## ひとことで

LLM は **Large Language Model**（大規模言語モデル）の略です。インターネット規模の文章データで訓練され、テキストを理解したり生成したりする AI の総称です。ChatGPT、Claude、Gemini の中身は、すべてこの LLM です。

## 何をしてくれるか

LLM ができることは、乱暴にまとめると「テキストを入れると、続きのテキストを返す」です。この単純な動きから、驚くほど幅広い応用が生まれます。

- 文章の続きを書く、要約する、翻訳する
- 質問に答える、会話する
- コードを書く、コードを説明する
- 資料を読み込んで整理する
- 画像や PDF を読んで説明する（マルチモーダル対応モデル）

### 仕組みを乱暴に言うと

LLM は「次に来る単語を予測する」モデルです。巨大な **パラメータ数**（数 B〜数百 B。J-22 参照）で訓練されると、予測の精度が高まり、まるで文脈を理解しているかのような応答ができるようになります。

### 代表的な LLM

- **GPT 系**（OpenAI）— GPT-3.5、GPT-4、GPT-5
- **Claude 系**（Anthropic）— Opus、Sonnet、Haiku
- **Gemini 系**（Google）— Pro、Flash、Flash-Lite
- **Llama 系**（Meta、オープン）
- **DeepSeek、Qwen、Kimi**（オープン／中国系）

## バイブコーディングでの位置づけ

バイブコーディングの根幹です。「何を LLM に渡して、何を返してもらうか」の設計がすべての出発点になります。

LLM は **Context（文脈）** に書いてあるものだけを手がかりに応答します。Context の設計が上手くなれば、同じ LLM でも応答が伸びます。逆に、LLM を変えるよりも Context を整えるほうが効く場面が多くあります。

モデルの「賢さ」はパラメータ数だけでは決まりません。訓練データ、アーキテクチャ（Transformer などの構造）、ファインチューニング、推論時の工夫（Thinking モデル、effort レベルなど）で実力は大きく変わります。

## メイン図

### 図の狙い

LLM を中心に、入力・内部・出力の 3 層を 1 枚で見せます。「テキスト→予測→テキスト」という骨格と、Context／Token／パラメータ数／Transformer という周辺語彙の位置関係が分かるようにします。

### C. 概念図（figure_type: structure）

- 中心に置く概念: LLM（1 回の応答を生成する推論の箱）
- 周辺の要素（5〜6 個）: 入力側に「Context（文脈）」「Token（数え方）」／内部に「Transformer（アーキテクチャ）」「パラメータ数（B／T）」／出力側に「続きのテキスト」／下部に「訓練データ（インターネット規模）」
- 関係の描き方: 左から右へのフロー（Context → LLM → 出力）。下から LLM へ「訓練データ」の矢印。内部構造を点線の箱で示す

## 関連用語

- Transformer — 現代 LLM の基盤アーキテクチャ（2017 論文）
- Token — Context のサイズを数える単位
- Neural Network — LLM の土台となる計算構造
- Context — LLM に渡す情報全体
- Fine-tuning — 既存モデルに追加学習して特化させる
- VLM — 画像も扱える Vision Language Model

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

文章を扱う AI の現代的な主流です。ChatGPT／Claude／Gemini の中身。

### 2. うれしさ

対話で使えて、幅広いタスク（文章・コード・要約・翻訳）に応用できます。

### 3. 注意点

Hallucination（事実と違うことを言う）や、限界があります。万能ではありません。

### 4. どこで役立つか

文章作成、コード生成、要約、対話のほぼ全タスク。

### 5. 最初に理解する範囲

「次の単語を予測するモデル」という骨格と、GPT／Claude／Gemini／Llama の代表系譜。

### 6. 深掘り先

Transformer、Attention、MoE、量子化、Fine-tuning、VLM。

## 開発フローでの位置（必須）

1. 目的を決める — 何を LLM にしてほしいか
2. 適切な LLM を選ぶ — 最も賢い／中間／アンカー、またはオープンモデル
3. Context を構成して渡す — 指示・資料・履歴
4. 出力を評価して反映 — 不足なら Context を足して再実行

<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニア視点のつまずき

-
-
-

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

- 🙂 第一印象:
- 👍 良い点:
- 👎 ダメな点:
- 🎯 誰に向くか:

<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: 中央に LLM の箱（グラデーションで内部に Transformer の格子を透かす）。左に入力矢印（Context、Token）、右に出力矢印（続きのテキスト）、下から訓練データの矢印（インターネット規模のアイコン群）
- 登場人物: 入力側に読者キャラクター（質問を投げる）、出力側で同じキャラクターが回答を読む
- 吹き出し・心の声: 「次の単語を予測し続けている」
- 中央に置くキーワード: LLM ＝ 大規模言語モデル ＝ 言葉を扱う AI の主流
- 追加: LLM の箱内に「数 B〜数百 B パラメータ」の注記を小さく

### 6視点アイコン（右ページ上段）

- 共通アイコン流用

### 開発フロー図（右ページ下段）

- Step 1: 目的アイコン（標的）
- Step 2: モデル選択アイコン（3 段のバッジ）
- Step 3: Context スタックアイコン
- Step 4: 評価アイコン（目＋チェック）
- 矢印: 目的 → 選ぶ → Context → 評価 のループ

## コミュニティ補完メモ

個別モデル（GPT 系、Claude 系、Gemini 系など）は D セクションで個別に扱います。本エントリは LLM という概念の総論に絞ります。Transformer・Attention・MoE・量子化の内部詳細は J-13／J-17／J-18／J-19 を参照。

## 出典メモ

- Anthropic docs "What are LLMs" — checked 2026-04-23
- OpenAI docs — checked 2026-04-23
- Stanford CS224N (Lecture Notes) — checked 2026-04-23

## 備考

本エントリは非エンジニア読者の入口として、「仕組みの骨格」と「代表モデル」「使い方の型」の 3 点に絞ります。内部の数式や訓練手法は別エントリで扱います。
