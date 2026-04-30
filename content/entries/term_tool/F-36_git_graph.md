---
id: F-36
title: Git Graph
title_reading: ギット グラフ
category: term_tool
subtype: editor_ext
experience_level: hands_on
reader_level: 2-3
figure_type: before_after
page_layout: spread_v1
start_date:
end_date:
version_status: active
pricing_note: none
evaluation_date: 2026-04-30
related_terms:
  - VS Code
  - git
  - branch
  - Pull Request
status: drafting
---

# Git Graph

## tagline

VS Code 拡張機能の一つ。リポジトリのコミット履歴をグラフで視覚的に表示します。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

ブランチ・タグ・マージの分岐を縦軸のグラフとして画面に描き、各コミットの差分やファイル変更を即座に確認できます。チェックアウト・マージ・チェリーピックなどの操作も GUI から実行できます。


## どこで出会うか

VS Code の拡張機能マーケットプレイスで入手できます。AI エージェントが複数のブランチや Pull Request（プルリクエスト）を大量に作る開発で、「履歴がどう枝分かれしているか」を一目で把握したい場面で使われます。


## メイン図

### 図の狙い

コマンド操作だけでは把握しにくいブランチの分岐状態が、グラフ表示でどう見えるかを対比する。

### A. Before / After（figure_type: before_after）

- Before
  - 状況: ターミナルで `git log --oneline` を実行しているが、どのブランチがどこから分岐したか把握しにくい
  - 視覚要素: テキストのコミットハッシュとメッセージが縦に並ぶ
  - つまずき: 5 本の AI 生成ブランチがどう絡んでいるか読み解けない
- After
  - 状況: Git Graph パネルを開くとブランチが色分けされた縦軸グラフで表示される
  - 視覚要素: 各コミットが丸いノードで示され、ブランチが色付き線で分岐・合流している
  - うれしさ: 合流点とコンフリクトの可能性を視覚で確認できる


## 会話での使い方例

「Git Graph で Claude が作った 5 本の branch の枝分かれを確認しました。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

VS Code 上でコミット履歴をグラフ表示する拡張機能です。

### 2. うれしさ

ブランチの分岐・合流をターミナルなしで視覚確認できます。

### 3. 注意点

GitLens（同じく VS Code 拡張）とは別物で、こちらはリポジトリ全体のグラフ表示が中心です。

### 4. どこで役立つか

AI エージェントが多数の PR を作る環境で履歴の全体像を把握するのに役立ちます。

### 5. はじめに

「グラフ表示」と「GUI 操作」の 2 機能があると把握すれば十分です。

### 6. 深掘り先

GitLens、SourceTree、GitHub Desktop


## 開発フローでの位置（必須）

1. 拡張インストール — VS Code Marketplace から「Git Graph」を検索してインストールします
2. グラフ確認 — ステータスバーの「Git Graph」ボタンからブランチ全体の分岐を確認します
3. コミット詳細確認 — ノードをクリックして差分・変更ファイルをその場で確認します
4. GUI 操作 — 右クリックメニューからチェックアウト・マージ・チェリーピックを実行します


## 関連用語

- VS Code
- git
- branch
- Pull Request


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

### メイン図（左ページ中段 / figure_type: before_after）

- 描く内容: 左側にターミナルのテキストログ、右側に Git Graph のカラフルなグラフ画面を対比
- 登場人物: 開発者（非エンジニア想定）がモニターを見ながら首をかしげている
- 吹き出し・心の声: 左「どのブランチがどこから来たの…」→ 右「あ、ここで Claude が 5 本作ったんだ！」
- 中央に置くキーワード/ラベル: 「Git Graph」
- Before / After の場合の対比ポイント: テキストのみ vs カラーグラフ

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: 拡張機能アイコン（パズルピース）
- Step 2 のアイコン/絵柄: ブランチグラフのミニアイコン
- Step 3 のアイコン/絵柄: ファイル差分アイコン
- Step 4 のアイコン/絵柄: マウス右クリックメニュー

## コミュニティ補完メモ

- GitLens（VS Code 拡張）との住み分け：GitLens はコード行に対するブレーム表示（誰がいつ書いたか）が中心。Git Graph はリポジトリ全体のブランチグラフ表示が中心。両者は共存可能で、役割が異なる
- SourceTree、GitHub Desktop との住み分け：後者 2 つは独立アプリ。VS Code を離れずに同じ情報を得たい場合は Git Graph が優位
- F-50 git との関係：git は版管理システム本体、Git Graph はその履歴を可視化するフロントエンド拡張

## 出典メモ

- VS Code Marketplace: Git Graph by mhutchie — checked 2026-04-30
- [marketplace.visualstudio.com/items?itemName=mhutchie.git-graph](https://marketplace.visualstudio.com/items?itemName=mhutchie.git-graph) — checked 2026-04-30


## 備考

- インストール数は 1,400 万超（2026-04-30 時点）。時変情報のため evaluation_date を参照のこと
- 無料拡張機能。ライセンスは MIT
