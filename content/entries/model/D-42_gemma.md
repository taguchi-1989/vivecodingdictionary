---
id: D-42
title: Gemma 系
title_reading: ジェンマ系
category: model
subtype: open
experience_level: research_only
reader_level: 3
importance: C
figure_type: timeline
page_layout: spread_v1
start_date: 2024
version_status: active
pricing_note: none
evaluation_date: 2026-04-29
related_terms:
  - Google
  - Gemini
  - オープンモデル
  - Ollama
  - ファインチューニング
status: drafting
---

# Gemma 系

## tagline

Google が公開するオープンウェイトモデル群。手元のマシンで動かせる小型版です。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

Google DeepMind が開発・公開するテキスト生成モデル群です。ウェイトを自分のサーバーや PC にダウンロードして推論でき、クラウド API なしで動かせます。1B〜27B の小型帯を中心に揃えており、商用利用も原則可能です。

## どこで出会うか

ローカル LLM を試す場面や、コストを抑えながら Google 品質を使いたい場面で名前が出ます。Ollama や Hugging Face がデフォルトで対応しており、Gemini の商用 API を使わず手元で動かしたいときに選ばれます。

## メイン図

### 図の狙い

Gemma 1 から Gemma 3 までの系譜を時系列で示し、「世代ごとに何が進んだか」を 1 枚で捉えてもらいます。

### A. 時系列タイムライン（figure_type: timeline）

- Gemma 1（2024-02）: 2B・7B の小型構成で初公開。研究・商用利用を解禁
- Gemma 2（2024-06）: 2B・9B・27B に拡張。日本語性能が向上
- Gemma 3（2025）: マルチモーダル対応。1B〜27B と幅広い構成

## 会話での使い方例

「Gemma 3 は小型でも Google 品質なので、ローカル推論の最初の選択肢になります。」

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

Google 製のオープンウェイトモデル群。手元で動く小型帯の代表です。

### 2. うれしさ

クラウド不要でデータを外に出さず、商用利用も原則可能です。

### 3. 注意点

Google 独自利用規約があり、再配布や派生モデルの条件を要確認です。

### 4. どこで役立つか

社内データを外に出せない場面や、コスト重視のローカル推論。

### 5. はじめに

Gemini（商用 API）と Gemma（オープンウェイト）の役割分担が要点です。

### 6. 深掘り先

Ollama、ファインチューニング、Gemini

## 開発フローでの位置（必須）

1. モデルを選ぶ — Gemma 3（1B/4B/27B）など用途と GPU に合わせて版を選ぶ
2. ウェイトを取得 — Hugging Face または Kaggle からダウンロード
3. ローカルで実行 — Ollama や LM Studio で起動して動作確認
4. 必要に応じて調整 — ファインチューニングや量子化で用途に合わせる
5. アプリに組み込む — API サーバー化して他ツールから呼び出す

## 関連用語

- Google
- Gemini
- オープンモデル
- Ollama
- ファインチューニング


<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

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

### メイン図（左ページ中段 / figure_type: timeline）

- 描く内容: 横軸に時系列で「Gemma 1 → Gemma 2 → Gemma 3」を矢印で結ぶ。各世代の下に「商用解禁」「日本語向上」「マルチモーダル」などのラベルを添える
- 登場人物: 画面脇に小さくエンジニアキャラクター。Gemma 3 あたりを指差して「これで十分使えます」と吹き出し
- 吹き出し・心の声: 「API 料金ゼロ、Google 品質でローカル推論」
- 中央に置くキーワード: Gemma 系 ＝ Google 製オープンウェイトの系統

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: モデルカードのアイコン（版選択）
- Step 2 のアイコン/絵柄: ダウンロード矢印
- Step 3 のアイコン/絵柄: PC + 歯車（ローカル起動）
- Step 4 のアイコン/絵柄: スライダー（調整・量子化）
- Step 5 のアイコン/絵柄: プラグアイコン（アプリ組み込み）
- 矢印で示す流れの意図: 選択 → 取得 → 起動 → 調整 → 活用 の一方通行


## コミュニティ補完メモ

- Gemini（D-1/D-2/D-3/D-4）との住み分け：Gemini は Google の商用クローズド API 系、Gemma は同じ研究成果から派生したオープンウェイト系。両者を「閉じた Gemini・開いた Gemma」として対比する
- Llama（D-40）との住み分け：Llama は Meta 製で最も広く参照される系統。Gemma は「Google エコシステム寄りのオープンモデル」として並記する
- Mistral（D-41）との住み分け：Mistral は欧州発。Gemma は Google DeepMind の研究を直接反映する点が独自色
- DeepMind（C-3）との関係：Gemma は DeepMind の研究成果を取り込んでいる。技術的背景の詳細は C-3 へ誘導する

## 出典メモ

- ai.google.dev/gemma — checked 2026-04-29
- blog.google（Gemma 3 発表記事）— checked 2026-04-29
- Hugging Face: google/gemma モデルページ — checked 2026-04-29

## 備考

モデル名・パラメータ数・ライセンス条件は時変情報です。Gemma 3 の版構成は evaluation_date 2026-04-29 時点の情報であり、本番利用前に公式を再確認します。「オープンウェイト」という表現は厳密には OSS と異なり、Google が公開しているのはウェイトファイルとコードであって、学習データは非公開です。Gemma の利用規約（Gemma Terms of Use）は Apache 2.0 ではなく独自規約のため、商用・再配布の条件を公式で確認します。
