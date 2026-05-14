---
id: J-51
title: Hallucination
title_reading: ハルシネーション
category: term_general
subtype: ethics_law
experience_level: hands_on
reader_level: 2
importance: A
figure_type: before_after
page_layout: spread_v1
start_date:
end_date:
version_status:
pricing_note:
evaluation_date: 2026-04-29
related_terms:
  - LLM
  - Context
  - RAG
  - Prompt Engineering
  - Sycophancy
status: ready
---

# Hallucination

## tagline

LLM がもっともらしい嘘をつく現象です。固有名詞・数値・URL で起きやすい限界です。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

Hallucination（幻覚）は、LLM が事実と異なる情報を自信ありげに生成してしまう現象です。「次の単語を予測する」仕組みの副作用で、LLM を使う場面では意識しておきたい点です。

## どこで出会うか

「存在しない論文を引用された」「社名・日付が違う」「URL が 404」といった場面で出会います。Context が不足した質問ほど起きやすく、Web 検索や RAG を組み合わせると軽減できます。

## メイン図

### 図の狙い

Context が不足した質問に LLM が断定的な誤情報を返す Before と、Context を整えることで正確に答える After を並べ、Hallucination の起きやすさが Context 設計に左右されることを示します。

### A. Before / After（figure_type: before_after）

- Before
  - 状況: Context なし・曖昧な質問で LLM に問い合わせる
  - 視覚要素: 「この薬の副作用は？」→ 「〇〇成分が含まれており安全です」（存在しない成分名）
  - つまずき: 自信ある口調で誤情報を返され、気づきにくい
- After
  - 状況: 公式資料を Context に含めて同じ質問をする
  - 視覚要素: 「添付の添付文書によると、〇〇の副作用があります（p.3 参照）」
  - うれしさ: 出典つきで事実に近い回答が返り、検証もしやすい

## 会話での使い方例

「固有名詞や数値は Hallucination が出やすいので、Context に資料を添えると安心です」

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

LLM の限界として、事実と違う断定回答を生成する現象です。

### 2. うれしさ

名前を知ることで「鵜呑みにしない」習慣が身につきます。

### 3. 注意点

口調が自信満々なので、間違いと気づきにくい点が要注意です。

### 4. どこで役立つか

情報収集・文書作成・コード生成など全タスクで常に意識が必要です。

### 5. はじめに

「固有名詞・数値・URL は必ず一次情報で確認する」が出発点です。

### 6. 深掘り先

RAG、Context（G-1）、Prompt Engineering

## 開発フローでの位置（必須）

1. 質問を組み立てる — Context が薄いと Hallucination が増えやすい点を意識します。
2. Context を整える — 公式資料を添えて LLM に渡します（G-1 参照）。
3. 回答を受け取る — 固有名詞・数値・URL は一次情報と照合します。
4. RAG を検討する — 検索結果を Context に組み込み誤情報を減らします。
5. 運用で監視する — 本番では定期的に出力の事実確認を行います。

## 関連用語

- LLM
- Context
- RAG
- Prompt Engineering
- Sycophancy

<!-- ━━━━━━━━ 著者記入欄（右ページ下段に印刷される／AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

- ハーネス（制御の仕組み）で囲っておかないと、今の弱い AI を信頼しきるのは難しいです。ソースチェックを機械的にやらせ、最後は人が見る運用が必要です
- どんな人でも騙されうるという点は変わらず、ここが非常に厄介です
- 突き詰めると「ハーネスがうまく作れていない」ことの裏返しで、自分のリテラシー不足にも行き着くところが面白い論点です

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

- 🙂 第一印象: 嘘をつかれた！という驚き
- 👍 良い点: ない（性質上）
- 👎 ダメな点: 流暢なので騙されやすいです
- 👥 誰向けか: LLM を使う人すべて


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: before_after）

- 描く内容: 左 Before に「Context なし」の吹き出しと LLM が断定的に誤情報を返すシーン、右 After に「資料を添付した Context あり」の吹き出しと正確な回答が返るシーンを並置。
- 登場人物: 非エンジニアのビジネスパーソンが画面に向かって質問している。Before では困惑した表情、After では安心した表情。
- 吹き出し・心の声: Before 側「これ本当に正しい？」、LLM から「〇〇です（誤情報）」。After 側「添付資料に書いてある通りですね」。
- 中央に置くキーワード/ラベル: Hallucination（幻覚）
- Before / After の対比ポイント: Context の有無が Hallucination の発生率を左右する点を視覚化する。

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: 質問アイコン（？マーク）
- Step 2 のアイコン/絵柄: 資料・ファイルの束アイコン（Context 整備）
- Step 3 のアイコン/絵柄: 虫眼鏡アイコン（照合・確認）
- Step 4 のアイコン/絵柄: 検索＋データベースアイコン（RAG）
- Step 5 のアイコン/絵柄: モニタリング画面アイコン（継続監視）
- 矢印で示す流れの意図: 質問組み立て → Context 整備 → 照合 → RAG → 監視 の対策サイクル

## コミュニティ補完メモ

- Context 設計（G-1）との住み分け：G-1 は「Context をどう設計するか」の実践論。J-51 は Hallucination という現象の説明に絞り、Context 設計は G-1 へ参照させる。
- Context Engineering（G-11）との住み分け：G-11 はシステム全体の Context 最適化。J-51 は現象の認識と基本対策の紹介にとどめる。
- LLM の仕組み（J-14）との住み分け：J-14 は LLM の構造全般。J-51 は Hallucination という副作用現象に絞る。
- Sycophancy（J-52）との住み分け：J-52 はユーザーに同調する傾向。J-51 は事実と異なる情報生成。振る舞いは似るが概念は別。
- RAG については「軽減策の一つ」として言及するにとどめ、RAG エントリへ参照させる。

## 出典メモ

- docs.anthropic.com — Hallucination 解説 — checked 2026-04-29
- Ji et al., "Survey of Hallucination in Natural Language Generation", ACM Computing Surveys (2023) — checked 2026-04-29

## 備考

- 固有名詞・数値・URL での発生頻度が高い点はブリーフ記載の要点のため本文に明示した。
- 「幻覚」という日本語訳は初出で括弧補足した。
- 再現性・確率性の議論（決定論的／非決定論的）は G-8 スケルトンへ分離する。
- Sycophancy（J-52）は「もっともらしい同調」であり Hallucination と隣接するが別概念。コミュニティ補完メモに住み分けを記載。
