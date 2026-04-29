---
id: G-11
title: Context Engineering
title_reading: コンテキストエンジニアリング
category: term_llm
subtype: technique
experience_level: partial
reader_level: 3
figure_type: comparison
page_layout: spread_v1
start_date:
end_date:
version_status: active
pricing_note: none
evaluation_date: 2026-04-29
related_terms:
  - Context
  - Prompt Engineering
  - System Prompt
  - RAG
  - Context Window
status: drafting
---

# Context Engineering

## tagline

LLM に渡す情報・状態・履歴の全体を設計する技術です。Prompt Engineering より広い層を扱います。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

LLM（大規模言語モデル）が参照する Context（文脈）の「何を・どの順で・どれだけ渡すか」を設計します。指示文を磨く Prompt Engineering より上位の概念で、System Prompt・履歴・ファイルなど全体の構造を整えます。

## どこで出会うか

「指示を変えても改善しない」場面で、Context の設計が根本原因であることがあります。Anthropic や AI 研究者の間で 2024〜2025 年に認知が広まり、CLAUDE.md もその実践例の 1 つです。

## メイン図

### 図の狙い

Prompt Engineering（指示文の磨き込み）と Context Engineering（情報全体の設計）を左右に並べ、スコープの広さの違いを視覚で伝える。

### B. 登場シーン（figure_type: comparison）

- シーン1（Prompt Engineering）: 人物が指示テキストを手直しする。吹き出し「言い方を変えよう」
- シーン2（Context Engineering）: 人物が System Prompt・資料・履歴をまとめて配置し直す。吹き出し「渡す情報を設計しよう」
- 並べる基準: 同一タスク・同一モデルで、改善の対象レイヤーが異なる

## 会話での使い方例

「Context Engineering は渡す情報の設計なので、指示文の書き方より先に考えたいですね。」

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

LLM が参照する Context 全体の構造と内容を設計します。

### 2. うれしさ

指示を変えずに渡す情報を整えるだけで応答が安定します。

### 3. 注意点

Prompt Engineering と混同されやすく、上位概念であることが見落とされます。

### 4. どこで役立つか

長期プロジェクトや複数ファイルを扱う開発で効果が出ます。

### 5. はじめに

System Prompt・履歴・ファイルの 3 つが Context の主要構成要素です。

### 6. 深掘り先

Context（G-1）, System Prompt（G-4）, RAG

## 開発フローでの位置（必須）

1. 目的と材料を整理 — タスクに必要な情報源（資料・履歴・ツール）を洗い出す
2. Context を設計 — System Prompt・資料・履歴の順と量を決める
3. 実行・出力確認 — 不要な情報を削り、不足なら追加して再実行する
4. 繰り返し改善 — Prompt Engineering と組み合わせて応答品質を高める

## 関連用語

- Context
- Prompt Engineering
- System Prompt
- RAG
- Context Window

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

### メイン図（左ページ中段 / figure_type: comparison）

- 描く内容: 左右 2 コマの対比。左は人物が指示テキストを書き直す姿、右は人物が情報のブロック（System Prompt・資料・履歴）を並べ替える姿
- 登場人物: 非エンジニアのビジネスパーソン（男女どちらでも可）が PC に向かう姿
- 吹き出し・心の声: 左「言い方を変えよう」、右「渡す情報を設計しよう」
- 中央に置くキーワード/ラベル: 「指示文の磨き込み vs 情報全体の設計」

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: 付箋に材料リストを書く人
- Step 2 のアイコン/絵柄: ブロックを並べる人（積み木のイメージ）
- Step 3 のアイコン/絵柄: 出力を確認してブロックを取捨選択する人
- Step 4 のアイコン/絵柄: Prompt Engineering と組み合わせる二刀流のイメージ
- 矢印で示す流れの意図: 「整理 → 設計 → 確認 → 改善」のサイクル


## コミュニティ補完メモ

- G-10 Prompt Engineering との住み分け：本エントリは「Context 全体の設計」が対象。指示テキスト単体の磨き込みは G-10 へ誘導する。「Prompt Engineering は Context Engineering の一部」という整理が有効。
- G-1 Context（needs_review 済）：本エントリの上位概念。Context そのものの定義は G-1 に任せ、G-11 では「設計行為」に絞る。
- G-4 System Prompt、G-20 CLAUDE.md：Context Engineering の具体的な実装手段として言及。詳細は各エントリへ誘導。
- G-5 Context Window：容量制限の話。「何を入れるか」の設計制約として本エントリに関係するが、容量の説明は G-5 へ。
- RAG（Retrieval-Augmented Generation）：外部情報を動的に Context に追加する手法で Context Engineering の実践例。詳細は RAG エントリへ。
- 2024〜2025 年の流れ（Karpathy 等の議論）：「プロンプトの言い方より、何を渡すかのほうが重要」という認識が広まっている。時変の可能性があるため出典メモに記録。

## 出典メモ

- docs.anthropic.com（Anthropic context engineering 解説） — checked 2026-04-29
- Andrej Karpathy 等の議論記事（context engineering の重要性） — checked 2026-04-29

## 備考

- 「Context Engineering」という語は 2024〜2025 年にかけて急速に広まっており、定義が固まりきっていない側面がある。evaluation_date の定期見直しを推奨。
- Prompt Engineering との境界はグラデーションであるため、本エントリでは「指示テキストより広い層を扱う」という切り口で差別化する。
