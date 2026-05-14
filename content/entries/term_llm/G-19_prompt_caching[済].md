---
id: G-19
title: Prompt Caching
title_reading: プロンプト キャッシング
category: term_llm
subtype: technique
experience_level: partial
reader_level: 3-4
importance: C
figure_type: before_after
page_layout: spread_v1
start_date: 2024-08-01
end_date:
version_status: active
pricing_note: paid
evaluation_date: 2026-04-30
related_terms:
  - System Prompt
  - Context Engineering
  - CLAUDE.md
  - Claude Code
  - Token
status: ready
---

# Prompt Caching

## tagline

同じプロンプト断片をサーバ側で再利用し、料金とレイテンシを下げる LLM API の仕組みです。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

同じ前提文書を毎回 API に送ると都度フルコストが発生します。Prompt Caching はサーバ側に内部状態を保持し、再利用時のトークン課金を抑えます。

## どこで出会うか

Claude Code など長文指示書を持つエージェントを使っていると月の請求で気づきます。Anthropic API の `cache_control` で保持位置を指定します。

## メイン図

### 図の狙い

キャッシュあり・なしでの API 呼び出しコストの違いを、1 人のエンジニアが同じ指示書を何度も送るシーンで見せる。

### A. Before / After（figure_type: before_after）

- Before
  - 状況: CLAUDE.md（長文）を毎リクエストに含めて送信
  - 視覚要素（コード or 概念）: 同じ指示書が 10 回分の請求行に並ぶ
  - つまずき: 「なぜこんなにトークンが消えるの？」
- After
  - 状況: `cache_control` でブレークポイントを設定、5 分間キャッシュヒット
  - 視覚要素: 2 回目以降の請求行が 1/10 のコスト表示
  - うれしさ: 月額が 30〜40% 削減できることがあります

## 会話での使い方例

「CLAUDE.md にキャッシュブレークポイントを置いたら、月額が 30% 下がりました。」

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

LLM API の繰り返し入力をサーバ側で再利用してコストを削減します。

### 2. うれしさ

キャッシュヒット時の入力トークン課金が約 1/10 になります。

### 3. 注意点

Anthropic は `cache_control` の明示が要り、設計次第で効果が変わります。

### 4. どこで役立つか

長文 System Prompt を持つエージェント運用で効果が出ます。

### 5. はじめに

書き込みと読み出しで課金率が異なる点を先に確認します。

### 6. 深掘り先

Context Engineering、System Prompt、Token

## 開発フローでの位置（必須）

1. 指示書の設計 — CLAUDE.md や System Prompt の長さを確認する
2. ブレークポイント設定 — `cache_control` で再利用範囲の末尾を指定する
3. 動作確認 — ヒット／ミスをログで見て 5 分以内の再利用を検証する
4. コスト計測 — 書き込み（＋25%）と読み出し（約 1/10）の収支を見る
5. 運用最適化 — 変更頻度を調整しヒット率を保つ

## 関連用語

- System Prompt
- Context Engineering
- CLAUDE.md
- Token

<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

- この言葉も最近聞いたばかりでよく分かっていないが、Serena MCP あたりがこれに当たるかもしれない（要確認）。
- Claude Code の初期に「トークン効率を上げる」と話題になっていたのは、おそらくこのキャッシュの話。
- 業務で使うときは情報のキャッシュをあまり意識していなかったが、個人で遊んでいると気になり始める部分。

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

- 🙂 第一印象: 「Serena MCP を使えばキャッシングされてコストが下がる」みたいな話が流行っていた。
- 👍 良い点: トークン効率が上がる。
- 👎 ダメな点: 今は Claude Code のハーネスに組み込まれているので、わざわざ MCP で使う必要はないと思う。
- 👥 誰向けか: 歴史的な文脈で見るくらいの位置づけ。

<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: before_after）

- 描く内容: 左側に「毎回フルコストの請求書が積み重なる棚」、右側に「キャッシュヒットで薄い請求書 1 枚」の対比
- 登場人物（いれば）: エンジニア（1 名）が API コンソールを眺めている
- 吹き出し・心の声: Before「また全部送ってる…月末が怖い」/ After「2 回目からほぼ無料で読み込める！」
- 中央に置くキーワード/ラベル: cache_control / ヒット率
- Before / After の対比ポイント: 請求トークン数の差（10x）

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: 文書アイコン（指示書）
- Step 2 のアイコン/絵柄: コードブロック（cache_control 設定）
- Step 3 のアイコン/絵柄: チェックマーク（ログ確認）
- Step 4 のアイコン/絵柄: グラフ（コスト計測）
- 矢印で示す流れの意図: 設計→設定→検証→最適化の PDCA

## コミュニティ補完メモ

- G-11 Context Engineering との住み分け：Context Engineering はプロンプト全体の設計戦略、Prompt Caching はその運用コスト削減の実装技術。「何を入れるか」と「どう再利用するか」で分担。
- G-4 System Prompt との住み分け：System Prompt はキャッシュ対象となる長文の代表例。G-4 で概念を説明し、G-19 でコスト削減の手段として言及する形で補完。
- OpenAI の自動キャッシュと Anthropic の明示的キャッシュの違いは備考に記載。

## 出典メモ

- <https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching> — checked 2026-04-30
- <https://platform.openai.com/docs/guides/prompt-caching> — checked 2026-04-30

## 備考

- Anthropic は 2024-08 に Claude API でキャッシュ機能を先行公開。キャッシュ書き込みコスト＋25%、読み出しは通常の約 1/10、有効期間 5 分（TTL は変更可能性あり）。
- OpenAI（GPT-4o 以降）は自動的にキャッシュを検出するため `cache_control` 相当の設定不要。Anthropic との設計思想の違いに注意。
- Google（Gemini API）も Context Caching として類似機能を提供。
- キャッシュの有効期間（TTL）は API バージョンや設定により変わるため evaluation_date 以降は要再確認。
