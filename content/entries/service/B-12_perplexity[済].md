---
id: B-12
title: Perplexity
title_reading: パープレキシティ
category: service
subtype: ai_assistant
experience_level: hands_on
reader_level: 2
importance: B
figure_type: workflow
page_layout: spread_v1
start_date: 2022-08
version_status: active
pricing_note: freemium
evaluation_date: 2026-04-29
related_terms:
  - Web 検索
  - 引用
  - ChatGPT
  - Deep Research
  - Sonar
status: ready
---

# Perplexity

## tagline

質問を入力するとWeb検索して引用付きで答えるAI検索エンジンです。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

質問文を送ると、Web上の複数ページをリアルタイムで検索し、内容をまとめて引用リンク付きで返してくれます。情報のソースがその場で確認できるため、回答の信頼性を自分で判断しやすくなります。

## どこで出会うか

「直近の情報をAIに調べさせたい」と思ったときに候補に挙がるサービスです。リリースノートや技術動向など、ChatGPTやClaudeでは学習済みデータ頼みになりがちな質問に使われます。

## メイン図

### 図の狙い

質問から引用付き回答までの4ステップを示し、「どこからの情報か」が見えることを伝えます。

### B. 登場シーン（figure_type: workflow）

- シーン1: 担当者が「〇〇の現在の価格は？」と入力する
- シーン2: Perplexityが複数のWebページを検索する — 画面に検索中の様子
- シーン3: 引用番号付きで回答が表示される — 「①によると…」
- シーン4: 担当者が引用リンクをクリックして一次ソースを確認する
- 並べる基準: 検索→生成→確認の時系列

## 会話での使い方例

「Perplexityで調べると引用元がすぐ見えて確認が楽ですね。」

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

Web検索結果を引用付きでまとめて返すAI検索エンジンです。

### 2. うれしさ

回答と一緒に出典リンクが並ぶため、情報源をすぐ辿れます。

### 3. 注意点

引用元の質に依存し、誤情報を正確に引用する場合もあります。

### 4. どこで役立つか

直近の動向調査や、一次ソースを示した上での報告書作成。

### 5. はじめに

Free で使え、内部モデルと引用の仕組みを把握すると安心です。

### 6. 深掘り先

Deep Research（G-35）、Sonar API、Prompt Engineering。

## 開発フローでの位置（必須）

1. 調査フェーズ — 技術動向・ライブラリの新しい版をPerplexityで確認
2. 要件整理 — 引用付き回答をそのまま議事メモに貼り付け
3. 実装中 — エラーコードや仕様変更をリアルタイム検索で確認
4. レポート作成 — 出典URL付きの要約を報告書の参考資料に活用

## 関連用語

- Web 検索
- 引用
- ChatGPT
- Deep Research
- Sonar

<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
-
-
-
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象:
- 👍 良い点:
- 👎 ダメな点:
- 👥 誰向けか:
<!-- user-input:end key="my_comment" -->


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: workflow）

- 描く内容: 左から「質問入力 → Web検索 → 引用付き回答 → ソース確認」の4コマ横並び
- 登場人物: ノートPCの前に座るビジネスパーソン（担当者）1名
- 吹き出し・心の声: Step1「新しい情報を調べたい」、Step4「これが元の記事か」
- 中央に置くキーワード: 引用①②③ のナンバリングが回答文に並ぶ様子

### 6視点アイコン（右ページ上段）

- 共通アイコン流用

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: 虫眼鏡＋Webグローブ
- Step 2 のアイコン/絵柄: 書類＋クリップ（議事メモ）
- Step 3 のアイコン/絵柄: ターミナル＋エラーマーク
- Step 4 のアイコン/絵柄: レポート＋リンクアイコン
- 矢印で示す流れの意図: 調査から成果物活用までの一方向フロー


## コミュニティ補完メモ

- ChatGPT（B-3）／Claude（B-2）との住み分け：汎用チャットと違い、Web検索と引用表示が主機能。リアルタイム情報の調査用途に特化した位置づけ。
- Deep Research（G-35）との住み分け：Deep Researchは長時間かけて複数ソースを深掘りする上位機能。本エントリはPerplexityの基本的な「質問→検索→引用回答」フローに絞る。
- 内部モデル（GPT-4系／Claude／自社Sonar等）の詳細はSonar APIエントリで扱う想定。

## 出典メモ

- perplexity.ai — checked 2026-04-29

## 備考

- 料金は Free / Pro / Enterprise の3段階。Pro月額料金は時変情報のため本文に記載せず。
- 内部で利用するモデルはユーザーが切り替え可能（自社Sonar、GPT-4o、Claude等）。モデル詳細は時変情報。
