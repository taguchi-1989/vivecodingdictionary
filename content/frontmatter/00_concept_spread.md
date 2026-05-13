---
id: front_concept
title: 扉
category: common
subtype: opening
experience_level: hands_on
reader_level: 1
importance: A
page_layout: front_concept_spread
evaluation_date: 2026-05-13
status: drafting
---

# 扉

このページは、表紙コピー「知らないことばで、止まらない。」の答えを最初に渡す見開きです。誌面ではタイトル・ページ番号・章ラベルを表示しません。本ファイルはデザイン担当向けのレイアウト指示書として扱います。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 左ページのコピー

知らないことばで、止まらないために。

## 左ページの本文

AI や開発の現場では、ふだん使わないことばが当たり前に飛び交います。意味がわからないとき、会話はそこで止まります。本書は、その止まり方をなくすための辞書です。

## 左ページの図（3 コマ・抽象人物）

会議で「コンテキスト」と聞いて固まる→本を開いて引く→同じ会議に戻って自分のことばで話す、の 3 コマで「困る／引く／戻る」を見せます。

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## 右ページのコピー

1 項目は、見開き 2 ページ。左でつかみ、右で使う。

## 右ページの本文

各エントリは、左ページで意味とつかみどころを、右ページで役割・うれしさ・注意点・関連語をまとめます。気になる語だけ引いて、会話に戻ってください。通読は不要です。

## 右ページの図（見開きミニチュア）

本編 1 エントリの実物見開きを縮小して中央に置き、左ページ側を「意味／出会う場面／メイン図」、右ページ側を「役割／うれしさ／注意点／関連語」のラベルで指します。下端に「読み終えたら現場へ戻る」の戻り矢印を入れます。

<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### 左ページ図（3 コマ・抽象人物）

- 描く内容: 困る／引く／戻る の 3 コマ。それぞれ 1 人の人物
- 登場人物: 性別や職種が出ない抽象人物 1 人。線画・濃紺主体・余白多め
- 吹き出しは入れない。状況だけで伝える
- 既存資産: [assets/opening/opening-spread-concept.png](../../assets/opening/opening-spread-concept.png) 左ページの方向を継承

### 右ページ図（見開きミニチュア）

- 描く内容: 本編 1 エントリの実物見開きを 60% 程度に縮小して中央配置
- 下地サンプル: F-2 TypeScript など定番エントリのスクリーンを使うと本書のトーンが伝わる
- ラベルは指示線（dashed）と 14px 文字で配置
- 下端に「現場へ戻る」の戻り矢印（1 本、ループ閉じ）
- 既存資産: [drafts/opening/opening-spread-annotated.html](../../drafts/opening/opening-spread-annotated.html) の発想を流用

## 出典メモ

- [drafts/opening_spread_brief.md](../../drafts/opening_spread_brief.md) — checked 2026-05-13（最初の扉ブリーフ）
- [assets/opening/opening-spread-concept.png](../../assets/opening/opening-spread-concept.png) — checked 2026-05-13（コンセプト画）
- 表紙コピー「知らないことばで、止まらない。」— 2026-04 採択

## 備考

- 本書前付け（A 章）全体の例外仕様は [docs/front_section_layout.md](../../docs/front_section_layout.md) で扱う
- 扉は ID `front_concept`。letter ID 体系外で、`ledgers/entries.csv` には載せない
- 誌面ではタイトル「扉」・ページ番号・章ラベルを表示しない。コピー 2 文と図 2 つだけが見える
- HTML/CSS 実装は別担当。本ファイルはマークダウンによるレイアウト指示書として扱う
