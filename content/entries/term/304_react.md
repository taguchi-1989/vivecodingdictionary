---
id: 304
title: React
category: term
subtype: framework
experience_level: partial
reader_level: 2
figure_type: structure
start_date:
end_date:
version_status: active
pricing_note: none
evaluation_date: 2026-04-21
related_terms:
  - JavaScript
  - TypeScript
  - JSX
  - Next.js
status: archived
# 旧 3 桁 ID。v0.5 renumber 以降は letter-ID 体系のため本エントリは参照素材として凍結。
---

# React

## ひとことで
React は、画面を小さな部品で組み立てるための JavaScript ライブラリ。ボタン、カード、一覧、ページなどをコンポーネントとして考える。

## 何をしてくれるか
React では、UIを部品単位で作る。小さな部品を組み合わせて、大きな画面やアプリを構成する。

たとえば、プロフィールカード、検索フォーム、商品一覧、ナビゲーションなどを、それぞれ再利用できる部品として扱う。

## 実務での意味
React の会話では、「この画面をどう作るか」よりも「どの部品に分けるか」が重要になる。

AIにUI修正を頼むときも、「このコンポーネントの表示を変える」「このpropsを渡す」「この状態で出し分ける」のような会話になりやすい。

## 非エンジニア視点のつまずき
React はWebサイトを作る全部入りの道具ではない。画面を作る中心ではあるが、ページ遷移、サーバー処理、データ取得、ビルドなどは別の仕組みと組み合わせることが多い。

Next.js が出てくるのは、この周辺機能をまとめて扱いやすくするため。

## 最初にどこまで理解すればよいか
- React はUIを部品で作るための道具
- 部品をコンポーネントと呼ぶ
- JSXという、HTMLに似た書き方が出てくる
- Next.js は React を使ったフレームワーク

## 私のコメント
React は「画面を部品で考える」感覚がわかると、一気に会話しやすくなる。非エンジニアでも、Figmaのコンポーネントや資料の部品化に近いものとして捉えられる。

## 誌面デザイン案
構造図型。ページ全体を、ヘッダー、検索欄、カード、ボタンなどのコンポーネントに分解して見せる。

## 出典メモ
- React official site, checked 2026-04-21
- React docs: Describing the UI, checked 2026-04-21

## 備考
State、props、hooks は別項目化候補。
