---
id: G-6
title: One-shot
title_reading: ワンショット
category: term_llm
subtype: prompt_technique
experience_level: hands_on
reader_level: 2-3
importance: C
figure_type: comparison
page_layout: spread_v1
start_date:
end_date:
version_status:
pricing_note:
evaluation_date: 2026-04-30
related_terms:
  - Prompt Engineering
  - Few-shot Learning
  - Zero-shot
  - System Prompt
status: ready
---

# One-shot

## tagline

例を 1 つだけ見せて、AI に同じ形式で答えさせるプロンプト技法です。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

出力例を 1 件だけ添えることで AI の返答フォーマットを揃えます。「例: Hello → こんにちは」と示すだけで同じ書き方で応答します。

## どこで出会うか

Prompt Engineering の解説で登場します。「Zero-shot・One-shot・Few-shot」の 3 段階整理の中の 1 つとして紹介されます。

## メイン図

### 図の狙い

例の有無で AI の返答がどう変わるかを、Zero-shot・One-shot の対比で掴んでもらう。

### A. Before / After（figure_type: comparison）

- Before
  - 状況: Zero-shot（例なし）でプロンプトを送る
  - 視覚要素: 「次の英文を日本語にしてください。Good morning →」
  - つまずき: AI が「おはようございます。」「Good morning は朝のあいさつです。」など形式がばらつく
- After
  - 状況: One-shot（例 1 つ）を添えてプロンプトを送る
  - 視覚要素: 「次の英文を訳してください。例: Hello → こんにちは。Good morning →」
  - うれしさ: AI が「おはようございます。」と一語で返すなど、形式が揃う


## 会話での使い方例

「One-shot で出力形式を見せたら、Claude が一発で揃えてくれました。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

例を 1 件だけ示して AI の出力形式を制御する技法です。

### 2. うれしさ

フォーマット指定の手間なしに、一貫した出力が得られます。

### 3. 注意点

例が 1 つだと曖昧さが残り、期待通りにならない場合があります。

### 4. どこで役立つか

翻訳・要約・分類など、出力形式を統一したい作業で効果が出ます。

### 5. はじめに

Zero-shot との違いを確認すると理解が早まります。

### 6. 深掘り先

Few-shot Learning、Prompt Engineering、Zero-shot

## 開発フローでの位置（必須）

1. タスク把握 — AI に任せたい作業と望む出力形式を決めます
2. 例を 1 件作成 — 入力と出力のペアを 1 つ用意してプロンプトに添えます
3. プロンプト送信 — One-shot を含む指示を Claude や GPT に投げます
4. 出力確認 — 形式が揃っているか確認し、揃わなければ Few-shot に切り替えます


## 関連用語

- Prompt Engineering
- Few-shot Learning
- Zero-shot


<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

- 「ワンショットの賢さ」と言われても意味が分からないと文脈を追えない。
- 「エージェント向きでない」とセットで出てきてチャット利用者には掴みにくい。

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

- 🙂 第一印象: Gemini はこれが賢い、という文脈で聞いた覚えがある。
- 👍 良い点: HTML 生成など非常に賢い出力が出てくることはある。
- 👎 ダメな点: 長期タスク性能と別物と認識しないと誤解しやすい。
- 👥 誰向けか: エージェント委任者はワンショットと長期性能を別物と押さえて。

<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: comparison）

- 描く内容: 左に「Zero-shot プロンプト」右に「One-shot プロンプト」を並べ、AI の返答がどう変わるかを示す対比図
- 登場人物（いれば）: AI エージェントを擬人化したキャラクター（ロボット風）と、プロンプトを送る人物
- 吹き出し・心の声: Zero-shot 側「形式が分からない…」、One-shot 側「この形式でいいですか！」
- 中央に置くキーワード/ラベル: 「例を 1 つ添える」
- Before / After の場合の対比ポイント: 返答のフォーマットがばらつく → 揃う

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: チェックリスト（タスク確認）
- Step 2 のアイコン/絵柄: 鉛筆（例を書く）
- Step 3 のアイコン/絵柄: 送信アイコン（プロンプト送信）
- Step 4 のアイコン/絵柄: 虫眼鏡（出力確認）
- 矢印で示す流れの意図: 準備→例作成→実行→評価の 1 サイクル

## コミュニティ補完メモ

- Few-shot Learning（G-13）との住み分け：G-6 は「例が 1 件だけ」の概念を説明。例が複数必要なケースや比較表が必要なら G-13 へ誘導。
- Zero-shot は G-6 の対概念として本文中に登場させる。Zero-shot 単独エントリがある場合はスコープを確認すること。
- Prompt Engineering（G-10）との住み分け：G-10 が全体技法、G-6 はその中の 1 テクニック。

## 出典メモ

- Brown et al. "Language Models are Few-Shot Learners" (GPT-3 paper), NeurIPS 2020 — checked 2026-04-30
- OpenAI Cookbook: Prompt Engineering guide — checked 2026-04-30


## 備考

- 「One-shot Learning」は機械学習文脈では「少数データで分類器を学習する手法」を指すこともある。本書は LLM プロンプト技法の意味のみを扱う。読者の混乱を防ぐため「どこで出会うか」節での文脈明示が重要。
- 「One-shot」は Zero-shot / Few-shot と 3 点セットで語られることが多い。3 語を関連用語に揃えておくと読者の横断参照がしやすい。
