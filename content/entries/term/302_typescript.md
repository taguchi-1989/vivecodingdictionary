---
id: 302
title: TypeScript
category: term
subtype: language
experience_level: partial
reader_level: 2
figure_type: before_after
page_layout: spread_v1
start_date:
end_date:
version_status: active
pricing_note: none
evaluation_date: 2026-04-21
related_terms:
  - JavaScript
  - ESLint
  - React
  - コンパイル
  - tsc
status: sample
---

# TypeScript

## tagline

JavaScript に「型」の考え方を足し、開発時のミスを見つけやすくする仕組み。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## ひとことで

TypeScript は、JavaScript に「型」を足して、書いている最中にミスへ気付きやすくするための言語。

## 何をしてくれるか

JavaScript は広く使われる言語で、そのままでも動く。TypeScript はその JavaScript を土台に、コードの中で扱うデータの「形」を明示するしくみを足す。

書いた TypeScript のコードは最終的に JavaScript へ変換されて実行される。実行環境を置き換える言語ではなく、開発中の見通しをよくする道具として見ると入口がそろう。

## バイブコーディングでの位置づけ

AI にコードを直させるとき、型は「このデータはこういう形だよ」という簡単な契約書として働く。AI が誤って別の形のデータを返しそうになっても、実行前に警告で弾きやすい。

バイブコーディングの文脈では、型があるほど「この構造を壊さないで」を自然言語でなく記号で伝えられる。指示のぶれを減らす足場として機能する。

## メイン図

### 図の狙い

同じ処理について、JavaScript だけのとき（実行してから気付く）と、TypeScript を足したとき（書きながら気付く）の対比を、1人の作業者の表情つきで見せる。

### A. Before / After（figure_type: before_after）

- Before
  - 状況: JavaScript だけで書き、実行するまで型のズレに気付かない
  - 視覚要素（コード or 概念）:

    ```js
    function add(a, b) {
      return a + b
    }
    add('1', 2)
    ```

  - つまずき: 実行して初めて `'12'` と文字列連結になっていたと気付く
- After
  - 状況: TypeScript で型注釈が入り、エディタ上で警告が出る
  - 視覚要素:

    ```ts
    function add(a: number, b: number) {
      return a + b
    }
    add('1', 2) // エラー
    ```

  - うれしさ: 実行前に型のズレを見つけやすい

## 関連用語

- JavaScript — TypeScript の土台。どちらも同じ実行環境で動く
- ESLint — 書き方のゆれを見つける別軸の道具。型とは役割が違う
- React — 現場で TypeScript と組み合わせて使われる代表例
- コンパイル — TypeScript を JavaScript に変換する工程
- tsc — TypeScript をコンパイルする公式コマンド

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

型の情報で、ミスを早めに見つけやすくする。

### 2. うれしさ

大きなコードでも読みやすさを保ちやすい。

### 3. 注意点

最初は記法が増えて難しく感じやすい。

### 4. どこで効くか

共同開発、保守、レビューで効きやすい。

### 5. 最初に理解する範囲

型注釈、エラー表示、JavaScript との違い。

### 6. 深掘り先

interface / type / generics は後からでよい。

## 開発フローでの位置（必須）

1. JavaScript を書く — 書き手が普段どおりのコードを置く
2. TypeScript が確認する — 型情報と突き合わせる
3. エディタ／ビルドで警告 — 食い違いを赤線や警告で示す
4. 修正して進む — 実行前に直して次の工程へ

<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニア視点のつまずき

- 「型」が何を意味するのか、最初は直感しづらい
- エラーが出ると、何が悪いのか読みにくい
- JavaScript と何が違うのか明確になりにくい
- 全部理解しないと使えないように見えてしまう

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

- 🙂 第一印象: 最初は少し驚いたが、意図はかなりまっとう
- 👍 良い点: 早い段階で事故を減らしやすい
- 👎 ダメな点: 初学者には記述の圧がある
- 🎯 誰に向くか: React / Next.js に触る人、共同開発に入る人

<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: before_after）

- 描く内容: 左に JavaScript だけのエディタ＋焦る作業者、右に TypeScript で赤線が出たエディタ＋冷静に指さす同一作業者
- 登場人物（いれば）: 同じキャラクター1人、Before では驚き、After では納得の表情
- 吹き出し・心の声: Before「え、実行して初めて気付いた…」／ After「あ、ここ間違ってたのか」
- 中央に置くキーワード/ラベル: 「型 ＝ データの形の、かんたんな約束」
- Before / After の場合の対比ポイント: 実行後に気付く → 書いてる最中に気付く

### 6視点アイコン（右ページ上段）

- 共通アイコン流用（① target / ② heart / ③ warning / ④ people / ⑤ magnifier / ⑥ chart-up）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: `</>` — コードを書く
- Step 2 のアイコン/絵柄: `TS` バッジ — 型チェックが走る
- Step 3 のアイコン/絵柄: `!` — エディタ/ビルドで警告
- Step 4 のアイコン/絵柄: `✓` — 修正して次へ
- 矢印で示す流れの意図: 書く → チェック → 気付く → 直す のループ

## コミュニティ補完メモ

実際の現場では `tsconfig` の厳しさ、React / Next.js との組み合わせ、型定義ファイル（`.d.ts`）などが話題になる。Level 3 以降で別ページ化してもよい。

## 出典メモ

- TypeScript official site: "TypeScript is JavaScript with syntax for types", checked 2026-04-21
- TypeScript Handbook: "TypeScript for JavaScript Programmers", checked 2026-04-21

## 備考

このページは非エンジニアが会話についていくための入口に絞る。型システムの詳細は扱わない。
