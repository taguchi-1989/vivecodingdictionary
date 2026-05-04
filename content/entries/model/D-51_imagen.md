---
id: D-51
title: Imagen
title_reading: イマジェン
category: model
subtype: image_video
experience_level: partial
reader_level: 2
importance: D
figure_type: timeline
page_layout: spread_v1
start_date: 2022
version_status: active
pricing_note: freemium
evaluation_date: 2026-04-29
related_terms:
  - Google DeepMind
  - Gemini
  - Vertex AI
  - DALL-E
  - Stable Diffusion
status: drafting
---

# Imagen

## tagline

Google DeepMind の画像生成モデルです。写実的な画像に強みがあり、Gemini とも統合されています。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

テキストの指示から写真や絵を生成します。Imagen 1 から始まり 4 まで進化し、写実的な人物・風景・物体の描写に定評があります。最新の Imagen 4 は高解像度と細部の精度がさらに向上しています。

## どこで出会うか

Gemini アプリで画像を生成すると Imagen が動いています。開発者は Vertex AI（Google Cloud のサービス）や Gemini API 経由で利用できます。画像つきの Gemini の回答や Google 製品のビジュアル生成の背後にあるモデルです。

## メイン図

### 図の狙い

Imagen 1 から 4 への進化の流れと、Gemini・Vertex AI との接続関係を 1 枚で示します。

### タイムライン（figure_type: timeline）

- Imagen 1（2022）: Google が発表した初代。写実性の高さで注目を集めました
- Imagen 2（2023）: 細部品質と多言語対応が向上。Google 製品に統合が進みました
- Imagen 3（2024）: Gemini との本格統合。API 公開も開始
- Imagen 4（2025）: 高解像度と物体・テキスト描写の精度がさらに向上

## 会話での使い方例

「Gemini の画像生成は Imagen が動いていて、Vertex AI からも API で呼べます。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

Google 製の画像生成モデルで、写実性に強みがあります。

### 2. うれしさ

Gemini 経由で手軽に使え、API でも呼び出せます。

### 3. 注意点

モデル版（1〜4）で品質が大きく異なるため版を確認します。

### 4. どこで役立つか

資料用画像の生成、プロトタイプのビジュアル作成に使えます。

### 5. はじめに

Gemini に統合されており、Vertex AI からも API で利用できる点。

### 6. 深掘り先

Vertex AI、Gemini API、DALL-E との比較。

## 開発フローでの位置（必須）

1. 画像の用途を決める — 写実的な写真系か、イラスト系かを判断
2. アクセス方法を選ぶ — Gemini アプリ（無料）か Vertex AI API か
3. プロンプトを書く — 被写体・構図・スタイルを日本語または英語で指定
4. 生成して確認 — 版・解像度・利用規約を評価日基準でチェック
5. 用途に合わせて調整 — プロンプトの修正またはモデル版の切り替え

## 関連用語

- Google DeepMind
- Gemini
- Vertex AI
- DALL-E
- Stable Diffusion


<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

-画像生成モデルの名前があんまり有名じゃない
-ウィスクとかで使える時にどのバージョンなのかってのが出てきにくくってわかりづらい
-

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

- 🙂 第一印象:Google の画像生成モデルが上手だ
- 👍 良い点:なウィスクでほぼ使いたい放題使えた。無料で
- 👎 ダメな点:ま、最新のモデルと比べるとナノバナナとかイメージ2。とかに GPT のを取る比べると劣る
- 👥 誰向けか:昔のレベルを知りたい人


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: timeline）

- 描く内容: 横軸に Imagen 1 → 2 → 3 → 4 を矢印で結ぶ時系列。各ノードに年号とキャッチを小さく添える。右端に Gemini と Vertex AI の接続を示す分岐矢印
- 登場人物: 画面脇に小さくユーザーキャラクター（非エンジニア風）。Imagen 3 のノードを指差して「ここから API が使えるようになった」と吹き出し
- 吹き出し・心の声: Imagen 4 ノード付近に「写実性がさらに上がった」
- 中央に置くキーワード/ラベル: Imagen の系譜 ＝ 写実性と統合の進化

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: 電球（用途を考える）
- Step 2 のアイコン/絵柄: 分岐矢印（アクセス方法を選ぶ）
- Step 3 のアイコン/絵柄: テキスト入力欄（プロンプト）
- Step 4 のアイコン/絵柄: 画像と虫眼鏡（生成・確認）
- Step 5 のアイコン/絵柄: スライダー（調整・切り替え）
- 矢印で示す流れの意図: 用途決定 → アクセス選択 → 生成 → 評価 → 改善のサイクル


## コミュニティ補完メモ

- Google DeepMind（C-3）の画像生成担当として位置づけ。C-3 はアシスタント全体の総論であり、Imagen はその下位の実装モデル
- Gemini（B-1）との住み分け：Gemini はマルチモーダルなアシスタント全体。Imagen は Gemini 内部の画像生成エンジンとして使われる
- DALL-E（D-50）との住み分け：DALL-E は OpenAI 製。Imagen は Google 製。写実性はどちらも高いが、Imagen は Vertex AI / Google Cloud との連携が強み
- Stable Diffusion（D-54）との住み分け：Stable Diffusion はオープンソースでローカル実行可能。Imagen は Google のクラウド API 経由のみ
- Whisk（D-58）：Imagen を使った Google のビジュアルリミックスツール。派生ツールとして参照


## 出典メモ

- deepmind.google/technologies/imagen-3 — checked 2026-04-29
- ai.google.dev/gemini-api/docs/imagen — checked 2026-04-29


## 備考

モデル版（Imagen 1〜4）・料金・提供状況は時変情報です。Vertex AI での提供プランや Gemini API の対応バージョンは評価日時点の情報であり、本番利用前に公式ページを再確認してください。
