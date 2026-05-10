---
id: G-30
title: Tool Use
title_reading: ツールユース
category: term_llm
subtype: control
experience_level: partial
reader_level: 3
importance: B
figure_type: workflow
page_layout: spread_v1
start_date:
end_date:
version_status: active
pricing_note: none
evaluation_date: 2026-04-29
related_terms:
  - MCP
  - Function Calling
  - System Prompt
  - Agent
status: ready
---

# Tool Use

## tagline

LLM がツールを呼び出す仕組みです。外部の検索や計算をモデルに任せられます。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

Tool Use（ツールユース）とは、LLM（大規模言語モデル）が「このツールを使いたい」と意図を返し、ホスト側が実行して結果を戻す仕組みです。Web 検索やコード実行を組み込めます。

## どこで出会うか

Claude API や OpenAI API のドキュメントで「Tool Use」「Function Calling」として紹介されます。Claude Code や ChatGPT Plugins など、AI が外部ツールを動かす場面の裏で動いています。

## メイン図

### 図の狙い

LLM が直接答えを作るのではなく、「ツール呼び出し → 実行 → 結果受け取り → 最終回答」という往復フローを一目で伝える。

### A. Workflow（figure_type: workflow）

- Step 1: ユーザーが質問を送る
- Step 2: LLM が「ツールを呼びたい」という意図（ツール名・引数）を返す
- Step 3: ホストがツールを実行し、結果を LLM に戻す
- Step 4: LLM が結果を踏まえて最終回答を生成する

## 会話での使い方例

「Tool Use があると LLM が検索結果を受け取って回答できます。」

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

LLM と外部ツールをつなぐ呼び出し・結果受け渡しの仕組みです。

### 2. うれしさ

LLM 単体では難しい計算や検索を組み込めます。

### 3. 注意点

ツールの実行はホスト側が行い、LLM は指示を出すだけです。

### 4. どこで役立つか

検索・コード実行・ファイル操作を AI に連携させる場面で使います。

### 5. はじめに

「LLM が何を呼ぶかを決め、実行はホストが担う」という分担を把握します。

### 6. 深掘り先

MCP（I-1）、Function Calling（G-33）、Agent。

## 開発フローでの位置（必須）

1. ツールを定義する — 名前・引数・説明を JSON スキーマで LLM に渡す
2. LLM にリクエストを送る — System Prompt とユーザー入力を API に送信する
3. ツール呼び出しを受け取る — LLM がツール名と引数を返してきたら実行する
4. 結果を LLM に戻す — 実行結果をメッセージとして追加し再度 API を呼ぶ
5. 最終回答を受け取る — LLM が結果を踏まえた回答を生成して返す

## 関連用語

- MCP
- Function Calling
- System Prompt
- Agent

<!-- ━━━━━━━━ 著者記入欄（右ページ下段に印刷される／AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

- 人がやっている操作を AI に代わりにやらせる、と置き換えれば概念は理解できる。要は AI がパソコン操作を担うという話。
- ただ、この概念を知らない人と話すときには、まずここを共有しないと話が進まない。
-

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

- 🙂 第一印象: AI が Web 検索できるようになったときは世界が変わったと思った。
- 👍 良い点: パソコンでできることを事実上すべてできるようになり得るところがすごい。
- 👎 ダメな点: ネイティブで実行できるのか、コンピューターユースのように GUI ベースで動かすのかで粒度が変わるし、対応状況にも差がある。「ツールを使えるから何でも OK」ではない。
- 👥 誰向けか: ほぼすべての人。


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: workflow）

- 描く内容: 左から右への 4 ステップ矢印フロー。「ユーザー → LLM → ホスト（ツール実行） → LLM → 最終回答」の往復を横長に配置する
- 登場人物: ノート PC に向かう人物（ユーザー）と、サーバーアイコン（ホスト）の 2 者を左右に配置する
- 吹き出し・心の声: LLM の箱に「search("今日の天気") を呼びたい」という吹き出し。ホストの箱に「実行して結果を返します」という吹き出し
- 中央に置くキーワード/ラベル: ツール呼び出し（Tool Call） ↔ 結果（Result）

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: JSON スキーマを渡す手
- Step 2 のアイコン/絵柄: 送信矢印（API リクエスト）
- Step 3 のアイコン/絵柄: 歯車（ツール実行）
- Step 4 のアイコン/絵柄: 戻り矢印（結果を返す）
- Step 5 のアイコン/絵柄: チェックマーク付き回答用紙（最終回答）
- 矢印で示す流れの意図: 「定義 → 送信 → 実行 → 戻す → 回答」の一往復


## コミュニティ補完メモ

- MCP（I-1）との住み分け：Tool Use は「LLM がツールを呼ぶ仕組み」全般の概念。MCP はその標準プロトコル（どう接続するかの規格）。「仕組み vs 規格」として分担する。
- Function Calling（G-33）との住み分け：Function Calling は OpenAI 由来の用語で Tool Use とほぼ同義だが、歴史的経緯と呼称の違いに焦点を当てる。本エントリでは Anthropic・OpenAI 共通概念として扱う。
- 具体的なツール例（Web 検索・コード実行・ファイル操作）は MCP 個別エントリ群（I-10〜I-50）に逃がす。


## 出典メモ

- docs.anthropic.com/en/docs/build-with-claude/tool-use — checked 2026-04-29
- platform.openai.com/docs/guides/function-calling — checked 2026-04-29


## 備考

- Tool Use は Anthropic の呼称、Function Calling は OpenAI の呼称。機能はほぼ同義だが、API のパラメータ名が異なる。G-33 Function Calling エントリで歴史的経緯を扱う。
- ツールの実行責任はホスト（アプリ側）にあり、LLM はあくまで呼び出す意図を返すだけである点が初学者のつまずきになりやすい。
