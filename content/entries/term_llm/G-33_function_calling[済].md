---
id: G-33
title: Function Calling
title_reading: ファンクションコーリング
category: term_llm
subtype: control
experience_level: partial
reader_level: 3
importance: D
figure_type: workflow
page_layout: spread_v1
start_date:
end_date:
version_status: active
pricing_note: none
evaluation_date: 2026-04-29
related_terms:
  - Tool Use
  - MCP
  - Agent
  - JSON
status: ready
---

# Function Calling

## tagline

LLM が関数名と引数を JSON で返す仕組みです。OpenAI 由来の呼称です。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

LLM（大規模言語モデル）がテキストではなく「関数名と引数」を JSON で返し、アプリ側がその JSON を使って関数を実行します。実行結果を LLM に戻すと最終回答が生成されます。

## どこで出会うか

OpenAI の API ドキュメントで「Function Calling」、Anthropic の Claude API では同じ仕組みを「Tool Use」と呼ぶため、両方の呼称が混在する記事で見かけます。

## メイン図

### 図の狙い

LLM が関数呼び出しを JSON で返し、ホストが実行して結果を戻す往復フローを一目で示す。

### A. Workflow（figure_type: workflow）

- Step 1: ユーザーが質問を送る
- Step 2: LLM が関数名と引数を JSON で返す
- Step 3: ホストが関数を実行して結果を LLM に戻す
- Step 4: LLM が結果を踏まえて最終回答を生成する

## 会話での使い方例

「Function Calling で LLM が JSON を返すので、ホスト側で関数を実行できます。」

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

LLM が関数名・引数を JSON で返す呼び出し規約です。

### 2. うれしさ

自然文ではなく構造化 JSON で返るので解析が安定します。

### 3. 注意点

関数の実行はホスト側が担い、LLM は指示するだけです。

### 4. どこで役立つか

天気取得や検索など外部 API を AI に連携する場面です。

### 5. はじめに

Tool Use と同義で、呼称が OpenAI 由来という点を把握します。

### 6. 深掘り先

Tool Use（G-30）、MCP（I-1）、Agent。

## 開発フローでの位置（必須）

1. 関数を定義する — 名前・引数・説明を JSON スキーマで LLM に渡す
2. LLM にリクエストを送る — ユーザー入力と関数定義を API に送信する
3. JSON レスポンスを受け取る — LLM が返した関数名と引数を取り出す
4. 関数を実行する — ホスト側で実際の処理を行い結果を取得する
5. 結果を LLM に戻す — 実行結果を追加して再度 API を呼び最終回答を得る

## 関連用語

- Tool Use
- MCP
- Agent
- JSON Schema

<!-- ━━━━━━━━ 著者記入欄（右ページ下段に印刷される／AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

- Tool Use に比べて聞きなじみがないです。
- JSON を知らない人には「JSON 形式で返す」説明がちんぷんかんぷんです。
- 規格としてどこまで支配的になるかも見えません。

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

- 🙂 第一印象: ちゃんと見たのは今回が初めて。
- 👍 良い点: 出力が固定されるのは良いことだと思う。
- 👎 ダメな点: 馴染みが薄い。あと自分でシステム／ツールの使い分けをするのが難しそう。
- 👥 誰向けか: 自作の応答システムを作る人向け。


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: workflow）

- 描く内容: 「ユーザー → LLM → ホスト（関数実行） → LLM → 最終回答」の左右往復フロー
- 登場人物: ノート PC を操作する人物（ユーザー）とサーバーを示すアイコン（ホスト）の 2 者を左右に配置する
- 吹き出し・心の声: LLM の箱に「{"function":"get_weather","args":{"city":"Tokyo"}} を返します」という吹き出し。ホストの箱に「実行して結果を渡します」という吹き出し
- 中央に置くキーワード/ラベル: JSON ↔ 結果（Result）

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: JSON スキーマを渡す手
- Step 2 のアイコン/絵柄: 送信矢印（API リクエスト）
- Step 3 のアイコン/絵柄: ダウンロード矢印（JSON レスポンス受け取り）
- Step 4 のアイコン/絵柄: 歯車（関数実行）
- Step 5 のアイコン/絵柄: チェックマーク付き回答用紙（最終回答）
- 矢印で示す流れの意図: 「定義 → 送信 → 受取 → 実行 → 回答」の一往復


## コミュニティ補完メモ

- Tool Use（G-30）との住み分け：Function Calling は OpenAI が 2023 年 6 月に命名した用語。Anthropic はほぼ同義の機能を「Tool Use」と呼ぶ。本エントリは用語史的経緯（OpenAI 由来）と JSON 返却という具体的なプロトコルに焦点を当てる。概念全体は G-30 Tool Use で扱う。
- MCP（I-1）との住み分け：MCP は Function Calling / Tool Use の接続方法を標準化する規格。「呼び方の仕組み vs 接続の規格」として分担する。
- Agent（G-41 並列実行中）との住み分け：Agent は Function Calling を繰り返す高次の仕組み。Function Calling は 1 往復の呼び出しに焦点を当てる。


## 出典メモ

- platform.openai.com/docs/guides/function-calling — checked 2026-04-29
- docs.anthropic.com/en/docs/build-with-claude/tool-use — checked 2026-04-29


## 備考

- Function Calling は OpenAI が 2023 年 6 月（gpt-3.5-turbo-0613 / gpt-4-0613）で初めて実装・命名した。Anthropic はほぼ同義の機能を「Tool Use」と呼ぶ。現在では「Function Calling」が両社共通の通称として広まっている側面もある。
- JSON スキーマで関数を定義する点が一般的なプロンプト指示とは異なる。構造化された出力が得られるため、後続処理の実装が安定しやすい。
