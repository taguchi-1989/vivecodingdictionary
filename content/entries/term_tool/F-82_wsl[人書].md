---
id: F-82
title: WSL
title_reading: ダブリュー エス エル
category: term_tool
subtype: shell
experience_level: hands_on
reader_level: 2-3
importance: D
figure_type: structure
page_layout: spread_v1
start_date:
end_date:
version_status: active
pricing_note: none
evaluation_date: 2026-04-29
related_terms:
  - bash
  - PowerShell
  - git
  - Docker
status: needs_review
---

# WSL

## tagline

Windows Subsystem for Linux の略。Windows の中で本物の Linux 環境を動かす仕組みです。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

WSL2 は軽量な仮想マシンで Linux カーネルを起動し、Ubuntu などのディストリビューション（Linux の配布形態）を Windows 上で利用できるようにします。Windows のファイルとも相互にアクセスできます。

## どこで出会うか

Claude Code や bash 関連の記事は手順が Linux 前提のことが多く、Windows ユーザーが「まず WSL を入れてから」という案内に出会うのが典型的な接点です。

## メイン図

### 図の狙い

Windows の中に Linux の層が入れ子になっている構造を示し、「仮想マシンより軽く、ネイティブとは別の層」という位置づけを伝えます。

### C. 概念図（figure_type: structure）

- 中心に置く概念: WSL2 レイヤー（Windows の中の Linux 領域）
- 周辺の要素: Windows OS / Linux カーネル / Ubuntu ターミナル / VS Code Remote / ファイル共有パス
- 関係の描き方: Windows を外側の枠、その内側に WSL2 の領域を入れ子で配置し、ファイル共有の矢印を双方向で示す


## 会話での使い方例

「WSL を入れてから Claude Code を使うと、bash 前提の記事がそのまま動きます。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

Windows 上で Linux コマンドやツールを動かす互換レイヤーです。

### 2. うれしさ

Linux 専用ツールを再起動なしで試せます。

### 3. 注意点

ファイルパスの形式が Windows と Linux で異なるため注意が必要です。

### 4. どこで役立つか

bash スクリプトや Docker を Windows 機で扱う場面で役立ちます。

### 5. はじめに

WSL2 は軽量仮想マシンで動き、WSL1 より Linux 互換性が高い点を押さえます。

### 6. 深掘り先

bash、Docker、VS Code Remote


## 開発フローでの位置（必須）

1. 導入 — PowerShell で `wsl --install` を実行します。
2. ディストリ選択 — Ubuntu など使いたい配布形態を追加します。
3. ツール導入 — bash や git、uv などを WSL 内に入れます。
4. エディタ連携 — VS Code の Remote 拡張で WSL 内を編集します。
5. 日常利用 — Claude Code など bash 前提のツールを動かします。


## 関連用語

- bash
- PowerShell
- git
- Docker


<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

-昔黒人コデックスか昔コデックスとかがもう黒のコードもかな。Windows 環境で使おうとすると基本的に wsl 環境にまず入れてくださいって言うんだったりするんだけど、 wsl 環境を構築するところていうところがま非常に Windows ユーザーの特にシステム自体のこう理解しづらいよね。どんな？ OS Windows なのにどこに立ち上げるって言ってるけど、なん か
-
-

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

- 🙂 第一印象:なんか入れないとコテックス動かなかったけど、めっちゃ苦労した
- 👍 良い点:Linux 環境の言語を Windows で使えるところはいいよね
- 👎 ダメな点:Li昔はセットアップが結構大変だった
- 👥 誰向けか:あの割と先端開発者向けかな


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: Windows の外枠の中に WSL2 領域を入れ子で描く。Ubuntu ターミナルウィンドウが WSL 内で開いている図
- 登場人物: Windows ユーザー（人物）が画面の前に座り、ターミナルを覗き込んでいる
- 吹き出し・心の声: 「Linux なのに Windows から動かせる？」→ 「WSL2 が橋渡しします」
- 中央に置くキーワード/ラベル: WSL2

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: PowerShell ウィンドウとコマンド入力
- Step 2 のアイコン/絵柄: Microsoft Store の Ubuntu ロゴ
- Step 3 のアイコン/絵柄: ターミナルとパッケージアイコン群
- Step 4 のアイコン/絵柄: VS Code と WSL バッジ
- Step 5 のアイコン/絵柄: Claude Code ロゴとターミナル


## コミュニティ補完メモ

- F-81 bash との住み分け：bash はシェル言語・コマンドの仕組みそのもの、WSL は bash を Windows で動かすための土台。「bash を使うには WSL が要る（Windows の場合）」という関係。
- F-83 PowerShell との住み分け：PowerShell は Windows ネイティブのシェル。WSL は Linux 系ツールを使いたいときの追加レイヤー。どちらを使うかは目的次第。
- F-90 Docker との住み分け：Docker Desktop on Windows は WSL2 バックエンドを推奨しており、WSL を入れると Docker の動作が安定しやすい。

## 出典メモ

- Microsoft Learn「WSL のインストール」 — checked 2026-04-29
- [Microsoft Learn WSL install](https://learn.microsoft.com/ja-jp/windows/wsl/install) — checked 2026-04-29


## 備考

- WSL1 と WSL2 は並存できる。WSL2 のほうが Linux カーネル互換性が高く、現在の主流。
- Windows 11 / Windows 10 バージョン 2004 以降で利用可能。
