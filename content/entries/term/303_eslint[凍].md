---
id: 303
title: ESLint
category: term
subtype: linter
experience_level: partial
reader_level: 2
figure_type: before_after
start_date:
end_date:
version_status: active
pricing_note: none
evaluation_date: 2026-04-21
related_terms:
  - JavaScript
  - TypeScript
  - lint
  - CI
status: archived
# 旧 3 桁 ID。v0.5 renumber 以降は letter-ID 体系のため本エントリは参照素材として凍結。
---

# ESLint

## ひとことで
ESLint は、JavaScript や JSX のコードを静的に調べて、問題や書き方のゆれを見つけるための道具。

## 何をしてくれるか
コードを実行する前に、よくあるミス、チームで決めた書き方からのズレ、危ない書き方を検出する。

設定によっては、自動で直せる問題もある。エディタ上で赤線や警告として見えることもあれば、CIでチェックされることもある。

## 実務での意味
ESLint は、チームのコード品質をそろえるための門番のような役割を持つ。

AIにコードを書かせたあとでも、ESLint を通すことで「見た目は動きそうだが、プロジェクトのルールに合っていない」問題に気づきやすくなる。

## 非エンジニアのつまずき
<!-- user-input:start key="stumble" -->
ESLint のエラーは、アプリが壊れているエラーとは限らない。書き方のルール違反や、将来バグになりそうな注意も含まれる。

そのため「赤い表示が出たから全部重大な障害」とは限らない。ただし、放置するとレビューや本番反映で止まることがある。
<!-- user-input:end key="stumble" -->

## 会話での使い方例

「AI 生成コードも ESLint を通せばチームの書き方ルールに自動で揃いますよ。」

## 最初にどこまで理解すればよいか
- コードの問題を早めに見つける道具
- 書き方の統一にも使う
- 自動修正できる問題もある
- AI生成コードの品質確認にも役立つ

## 私のコメント
<!-- user-input:start key="my_comment" -->
ESLint は、非エンジニアから見ると「また怒られている」ように見えるかもしれない。でも実際には、チームの合意を機械的に守るための仕組み。AI活用が増えるほど、こういう自動チェックの価値は上がる。
<!-- user-input:end key="my_comment" -->

## 誌面デザイン案
Before / After 型。Before は書き方がばらばらなコード群、After はESLintがゆれや問題に印を付ける図。

## 出典メモ
- ESLint official site, checked 2026-04-21
- ESLint command line interface docs, checked 2026-04-21

## 備考
Prettier、型チェック、テストとの違いは別項目化するとよい。
