---
id: H-55
title: LLaMA のオープン化
category: history
subtype: event
experience_level: research_only
reader_level: 2-3
importance: D
figure_type: timeline
page_layout: spread_v1
start_date: 2023-02-01
end_date:
version_status: active
pricing_note: none
evaluation_date: 2026-04-30
related_terms:
  - Ollama
  - Hugging Face
  - llama.cpp
  - Mistral 系
  - ローカル LLM
status: drafting
---

# LLaMA のオープン化

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## tagline

Meta が公開した LLaMA シリーズが、オープンモデル文化を一気に広げた転換点です。

## 何をしてくれるか

LLaMA（Large Language Model Meta AI）は、Meta が公開した大規模言語モデル群です。重みをダウンロードして手元で動かせるため、自前サーバーや個人 PC での推論が現実的になりました。

## どこで出会うか

「ローカル LLM を動かす」文脈でよく出てくる名前です。Ollama や LM Studio のセットアップ記事でモデル選択肢として登場し、Hugging Face や Llama 3 系の記事でも見かけます。

## メイン図

### 図の狙い

2023 年のリークから商用解禁、そしてエコシステム拡大までの時系列を一枚で示す。

### C. 概念図（figure_type: timeline）

- 中心に置く概念: LLaMA → LLaMA 2 → Llama 3 の時系列
- 周辺の要素: リーク・ローカル推論・商用解禁・派生モデル群
- 関係の描き方: 横軸時系列の矢印、各点にアイコン

## 会話での使い方例

「Ollama で Llama 3 を動かすと、クラウドなしでローカル推論が試せます。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

オープンモデル文化の火種となった歴史的リリース群です。

### 2. うれしさ

クラウド契約なしに LLM を手元で動かせる道が開きました。

### 3. 注意点

商用利用条件はバージョンごとに異なるため確認が必要です。

### 4. どこで役立つか

ローカル推論やファインチューニングの起点として使われます。

### 5. はじめに

LLaMA 2（2023-07）が商用利用 OK になった点を押さえると理解が早いです。

### 6. 深掘り先

llama.cpp、Ollama、Hugging Face

## 開発フローでの位置（必須）

1. 2023-02 LLaMA 公開 — 研究者限定配布。直後にリークし話題化。
2. 2023-07 LLaMA 2 公開 — Microsoft 共催で商用利用 OK に。
3. ローカル推論が普及 — llama.cpp・Ollama・LM Studio が登場。
4. 2024〜2025 後続モデル — Llama 3 系や Mistral などが追随。
5. エコシステム拡大 — Hugging Face のモデル共有文化が加速。

## 関連用語

- Ollama
- Hugging Face
- llama.cpp
- Mistral 系
- ローカル LLM


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

- 描く内容: 2023-02 〜 2025 の横軸時系列。各マイルストーンを旗アイコンで表示
- 登場人物: 個人開発者（男性）が PC の前に座り「手元で動いた！」と驚く
- 吹き出し・心の声: 「クラウドなしで LLM が動いた」「商用 OK になった」
- 中央に置くキーワード/ラベル: LLaMA → LLaMA 2 → Llama 3

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: 封筒（研究者限定配布）
- Step 2 のアイコン/絵柄: 鍵が開く（商用解禁）
- Step 3 のアイコン/絵柄: ノート PC（ローカル推論）
- Step 4 のアイコン/絵柄: 派生モデルのアイコン群
- Step 5 のアイコン/絵柄: Hugging Face のロゴ的アイコン（笑顔の顔文字）
- 矢印で示す流れの意図: 限定公開 → 解禁 → 普及 → 多様化 の因果

## コミュニティ補完メモ

- D-40 Llama 系との住み分け: 本エントリは「歴史的経緯・転換点」、D-40 は「現行モデルスペック比較」に集中する
- D-41 Mistral 系・D-42 Gemma 系・D-43 Qwen 系: LLaMA のオープン化が引き起こした後続モデル群として言及するにとどめる
- F-86 Ollama: ローカル推論ツールの代表として関連用語で紐づけ

## 出典メモ

- Meta AI blog — LLaMA 2 公式発表 — checked 2026-04-30
- https://ai.meta.com/blog/meta-llama-3/ — checked 2026-04-30
- https://ollama.com/ — checked 2026-04-30

## 備考

- LLaMA 1 は研究者限定のはずが 4chan などへリークし、結果として個人勢のローカル LLM 実験の火種になった経緯がある（事実として記載、善悪評価は著者コメント欄に回す）
- Llama 2 のライセンスは「月間アクティブユーザー 7 億人以上のサービスには別途 Meta との契約が必要」という条件付き。一般的な個人・中小利用は OK
- Llama 3 系（3.0 / 3.1 / 3.2 / 3.3）は 2024 年以降に展開、2025 年に Llama 4 が登場
- 時変情報（最新バージョン・ライセンス詳細）は evaluation_date: 2026-04-30 時点
