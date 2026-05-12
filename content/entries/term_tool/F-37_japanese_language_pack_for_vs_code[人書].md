---
id: F-37
title: Japanese Language Pack for VS Code
title_reading: ジャパニーズ ランゲージ パック フォー ブイエスコード
category: term_tool
subtype: editor_ext
experience_level: hands_on
reader_level: 1-2
importance: D
figure_type: before_after
page_layout: spread_v1
start_date:
end_date:
version_status: active
pricing_note: none
evaluation_date: 2026-04-30
related_terms:
  - VS Code
  - Cursor
  - Claude Code
  - Marketplace
status: ready
---

# Japanese Language Pack for VS Code

## tagline

VS Code（ブイエスコード）のメニューを日本語化する Microsoft 公式の拡張機能です。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

インストールして再起動すると、VS Code のメニューやコマンドパレットなどが日本語表示に切り替わります。Microsoft が公式配布しており、Marketplace から無償で入手できます。

## どこで出会うか

VS Code を初めて起動したとき、右下に「日本語に切り替えますか？」と通知が出ることがあります。Cursor や Claude Code も VS Code ベースのため、同じ手順で日本語化できます。

## メイン図

### 図の狙い

インストール前後で画面の表示言語がどう変わるかを対比で示す。

### A. Before / After（figure_type: before_after）

- Before
  - 状況: 拡張を入れていない初期状態
  - 視覚要素: メニューバーに "File / Edit / View" と英語表示
  - つまずき: 操作の意味がわからず戸惑う
- After
  - 状況: Japanese Language Pack をインストールして再起動
  - 視覚要素: メニューバーに「ファイル / 編集 / 表示」と日本語表示
  - うれしさ: 用語が母語で見えるため操作を迷わず進められる


## 会話での使い方例

「Japanese Language Pack を入れたら、メニューが日本語になって戸惑いが減りました。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

VS Code の UI を日本語表示に切り替える公式拡張です。

### 2. うれしさ

英語のメニューを読む手間がなくなり、操作に集中できます。

### 3. 注意点

各拡張機能の UI は日本語化されず、本体のみが対象です。

### 4. どこで役立つか

VS Code を初めて触る非エンジニアの導入ハードルを下げます。

### 5. はじめに

Marketplace で検索してインストールし、再起動するだけです。

### 6. 深掘り先

VS Code, Marketplace, Cursor


## 開発フローでの位置（必須）

1. VS Code インストール — エディタ本体を PC に導入する
2. Language Pack 追加 — Marketplace で検索してインストールする
3. 再起動 — VS Code を再起動して日本語 UI を有効にする
4. 拡張機能を追加 — 日本語化済みの環境でほかの拡張を導入する


## 関連用語

- VS Code
- Cursor
- Claude Code
- Marketplace


<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

- これを入れないと VS Code は英語表示のままで、最初の関門になりやすいです。少し癖がある部分もありますが、入れてしまえばその後はそれほど大変ではありません。

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

- 🙂 第一印象: これで日本語になってくれてよかった、という安堵感がありました。
- 👍 良い点: 日本語で扱えるようになる点に尽きます。
- 👎 ダメな点: これを入れないと VS Code 全体が英語のままで、非常に使いづらいです。
- 👥 誰向けか: 日本語環境で VS Code を使いたい人全般に必要です。


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: before_after）

- 描く内容: VS Code のメニューバーを左右に並べ、左が英語表示・右が日本語表示の対比図
- 登場人物（いれば）: 画面を見て困惑している人物（Before）と安心している人物（After）
- 吹き出し・心の声: Before「File って何…？」/ After「ファイル、わかる！」
- 中央に置くキーワード/ラベル: 「日本語化」
- Before / After の場合の対比ポイント: メニューの文字が英語 → 日本語に変わる瞬間

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: PC とダウンロードアイコン
- Step 2 のアイコン/絵柄: Marketplace の検索ボックス
- Step 3 のアイコン/絵柄: 再起動（矢印循環）アイコン
- Step 4 のアイコン/絵柄: 拡張機能の追加アイコン
- 矢印で示す流れの意図: 導入から日本語環境完成までの順序

## コミュニティ補完メモ

- VS Code（F-30）との住み分け: F-30 がエディタ本体の概要を扱うのに対し、F-37 は日本語化手順に特化。重複なし。
- Cursor（B-4）・Claude Code（B-7）との関係: どちらも VS Code ベースであり、同じ Language Pack が適用できる旨を本文「どこで出会うか」で言及済み。

## 出典メモ

- <https://marketplace.visualstudio.com/items?itemName=MS-CEINTL.vscode-language-pack-ja> — checked 2026-04-30
- <https://code.visualstudio.com/docs/getstarted/locales> — checked 2026-04-30


## 備考

- 拡張機能側（各サードパーティ製など）の UI は日本語化されない。VS Code 本体のみが対象。これはつまずき例として左ページに入れるか著者欄に回す候補。本文「注意点」に要約して記載済み。
- 中・韓・仏・独など他言語パックも Microsoft 公式で同様に提供されているが、本エントリのスコープは日本語パックのみ。
