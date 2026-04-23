---
id: 101
title: Gemini
category: service
subtype: ai_assistant
experience_level: research_only
reader_level: 2
figure_type: structure
start_date:
end_date:
version_status: active
pricing_note: "利用面やAPI面で料金体系が分かれるため、正式な価格は公式ページ確認"
evaluation_date: 2026-04-21
related_terms:
  - Gemini 2.5 Pro
  - Gemini 2.5 Flash
  - Gemini 2.5 Flash-Lite
  - Vertex AI
status: sample
---

# Gemini

## ひとことで
Gemini は、Google が提供する生成AIサービスとモデル群の名前。文章、画像、音声、動画、コードなどを扱えるAIとして、チャット利用にも開発利用にも登場する。

## 何をしてくれるか
Gemini という名前は、ひとつのアプリだけではなく、複数の入口を持つブランドとして見ると理解しやすい。

- 普通の利用者にとっては、AIチャットや作業支援のサービス
- 開発者にとっては、APIから呼び出せるモデル群
- 企業やクラウド利用者にとっては、Vertex AI 上で使う生成AI機能

つまり「Geminiを使う」と言っても、チャット画面で相談する話なのか、APIでアプリに組み込む話なのか、Vertex AIで業務システムに接続する話なのかで意味が変わる。

## 実務での意味
打ち合わせで Gemini が出てきたら、最初に確認したいのは「サービス名として話しているのか、モデル名として話しているのか」。

たとえば、Gemini 2.5 Pro や Gemini 2.5 Flash はモデル名。Gemini という大きな箱の中に、用途別のモデルが入っていると考えると混乱しにくい。

## 非エンジニア視点のつまずき
Gemini は名前の粒度が少しややこしい。サービス、モデル、API、Google Cloud の機能が同じ会話に混ざりやすい。

つまずきやすい言い方:

- 「Geminiでやる」だけでは、チャットなのかAPIなのかわからない
- 「Geminiの性能」と言っても、どのモデルの性能かで話が変わる
- 「無料で使えるか」と「API料金がいくらか」は別の話になる

## 最初にどこまで理解すればよいか
Level 2 では、まず次の区別ができれば十分。

- Gemini: 大きなサービス・モデル群の名前
- Gemini 2.5 Pro: 複雑な推論やコードに強いモデル
- Gemini 2.5 Flash: 速度と性能のバランスを狙うモデル
- Gemini 2.5 Flash-Lite: 低遅延・高スループット向けの軽量寄りモデル
- Vertex AI: Google Cloud 側でAIモデルを業務利用する入口

## 私のコメント
Gemini は「AIチャットの名前」としてだけ覚えると、開発や業務利用の話に入ったときに急にわからなくなる。最初から「Geminiという棚の中に、用途別のモデルや使い方がある」と見たほうが、後で整理しやすい。

## 誌面デザイン案
このページは「構造図型」が合う。

- 左上に大きく `Gemini`
- 下に `チャット利用`、`API利用`、`Vertex AI利用` の3つの入口
- さらに下に `Pro`、`Flash`、`Flash-Lite` などのモデル群
- 本文は右側に短い説明ブロックを置く

読者に見せたいのは細かいスペックではなく、「Geminiという言葉が複数の階層をまたぐ」という構造。

## コミュニティ補完メモ
実際の使い分けは、個人利用、業務利用、開発利用でかなり違う。利用者の具体的なワークフロー例を後で足すとよい。

## 出典メモ
- Google Cloud: Google models, Generative AI on Vertex AI, checked 2026-04-21
- Google Cloud: Gemini 2.5 Pro / Flash / Flash-Lite model pages, checked 2026-04-21

## 備考
このサンプルでは、要件書の試作対象に合わせて Gemini 2.5 系を中心に扱っている。Google のモデル一覧には Gemini 3 系も掲載されているため、正式公開時は掲載対象を再確認する。
