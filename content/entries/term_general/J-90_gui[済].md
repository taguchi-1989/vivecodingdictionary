---
id: J-90
title: GUI
title_reading: グーイ
category: term_general
subtype: ui_os
experience_level: partial
reader_level: 1-2
importance: C
figure_type: comparison
page_layout: spread_v1
start_date:
end_date:
version_status: active
pricing_note:
evaluation_date: 2026-04-30
related_terms:
  - CLI
  - VLM
  - Playwright MCP
  - OSWorld
status: ready
---

# GUI

## tagline

Graphical User Interface の略。マウスやタッチで「絵」を操作する画面インターフェースです。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

ウィンドウ・アイコン・メニュー・ボタンなどの視覚要素を通じて、コマンドを覚えなくてもソフトウェアを操作できます。1984 年の Apple Macintosh 以降、PC 操作の標準形として広まりました。

## どこで出会うか

OS のデスクトップや Web ブラウザ、アプリの設定画面はすべて GUI です。AI の文脈では「Computer Use が GUI を自動操作する」など、AI が人間用の画面を読み取って操作する話題で出てきます。

## メイン図

### 図の狙い

GUI と CLI の操作方法の違いを「絵で触る」対「文字で打つ」で対比し、GUI の直感性を掴んでもらう。

### B. 登場シーン（figure_type: comparison）

- シーン1: 社員がアプリのボタンをクリックして設定を変更する
- シーン2: AI エージェントがブラウザの GUI を画像認識で読み取り、フォームを自動入力する
- シーン3: CLI に慣れていない担当者がメニューから操作を選ぶ
- 並べる基準: 人間 vs. AI それぞれの GUI 活用シーンで対比

## 会話での使い方例

「Computer Use が GUI を直接操作するので、業務アプリの自動化が一気に進みます。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

コマンドを使わず、視覚要素で操作できる仕組みです。

### 2. うれしさ

直感的に操作できるため、非エンジニアでも扱いやすくなります。

### 3. 注意点

UI（User Interface）の一種で、音声・CLI なども UI に含まれます。

### 4. どこで役立つか

AI が GUI を自動操作する Computer Use・RPA の文脈で重要です。

### 5. はじめに

GUI は「絵で操作」、CLI は「文字で操作」という対比が整理の出発点です。

### 6. 深掘り先

CLI、Computer Use、VLM

## 開発フローでの位置（必須）

1. 要件確認 — 操作対象が GUI か CLI かをまず確認します
2. 画面設計 — ボタン・メニューなど GUI 要素を設計・配置します
3. 自動化検討 — GUI 操作を AI や RPA に任せるか判断します
4. テスト・確認 — 実際の GUI 画面で操作・表示を検証します


## 関連用語

- CLI
- VLM
- Playwright MCP
- OSWorld


<!-- ━━━━━━━━ 著者記入欄（右ページ下段に印刷される／AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- 当たり前すぎる操作を GUI と名づけられると、逆に理解しづらいです。
- CLI と対比しないと、何が GUI なのかが掴みにくい。
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: まあ、こんなもんか。
- 👍 良い点: 誰でもパソコンを分かりやすく使えるようにしたところ。
- 👎 ダメな点: AI エージェントから触りづらいのが、場面によっては致命的。
- 👥 誰向けか: 自動化を進めようとしている人、その文脈で会話する人。
<!-- user-input:end key="my_comment" -->


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: comparison）

- 描く内容: 左に「人間がマウスでボタンをクリックする画面」、右に「AI エージェントが同じ画面を画像として読み取りフォームに入力する」場面を並置
- 登場人物: 左＝オフィスワーカー（マウスを持つ手）、右＝AI エージェント（ロボットアイコン）
- 吹き出し・心の声: 左「ここをクリックすればいい」、右「この座標に入力します」
- 中央に置くキーワード/ラベル: GUI

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: 要件チェックリスト
- Step 2 のアイコン/絵柄: 画面ワイヤーフレーム
- Step 3 のアイコン/絵柄: ロボット＋画面
- Step 4 のアイコン/絵柄: チェックマーク付き画面
- 矢印で示す流れの意図: 設計から自動化・確認へと段階的に進む流れ


## コミュニティ補完メモ

- CLI（J-91）との住み分け：GUI は「絵で操作」、CLI は「文字で操作」の対義語として対で説明。GUI エントリではその対比を軸に据える。CLI エントリ側で「文字入力の強み」を掘り下げる
- UI との混同：UI はインターフェース全般（音声・触覚・CLI・GUI を包含）、GUI はその中のグラフィカル系。本エントリでは注意点 3 の視点で触れるにとどめ、UI 単独エントリには立ち入らない
- Computer Use / VLM との接続：AI が GUI を操作する話題は本エントリの「どこで出会うか」と開発フロー 3 で触れ、詳細は VLM（J-15）・OSWorld（E-34）に委ねる


## 出典メモ

- Wikipedia "Graphical user interface" — checked 2026-04-30
- Xerox Alto / Apple Macintosh 史料（Computer History Museum） — checked 2026-04-30


## 備考

- GUI の起源として 1973 年 Xerox Alto が先行、1984 年 Apple Macintosh が一般化、1985 年 Windows 1.0 で大衆化という流れがある。本文では「1984 年 Apple Macintosh」のみ代表例として記載し、詳細は備考に残す
- WIMP（Windows・Icons・Menus・Pointer）モデルは GUI の構成要素の呼称。誌面字数の都合で本文には入れず、補足扱い
