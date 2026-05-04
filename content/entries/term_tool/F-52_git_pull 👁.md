---
id: F-52
title: git pull
title_reading: ギットプル
category: term_tool
subtype: git
experience_level: hands_on
reader_level: 2
importance: C
figure_type: structure
page_layout: spread_v1
version_status: active
evaluation_date: 2026-04-29
related_terms:
  - git push
  - git fetch
  - merge
  - branch
  - リポジトリ
status: needs_review
---

# git pull

## tagline

リモートの最新変更を取得してローカルに反映するコマンドです。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

`git pull` は、リモートリポジトリ（GitHub 等）の最新状態を取得し、ローカルの作業コピーに取り込む 2 段構えのコマンドです。内部では `git fetch`（取得）と `git merge`（統合）を順に実行します。

## どこで出会うか

チームで開発するとき、朝一番に「pull してから作業開始」という習慣として登場します。AI に書かせたコードを共有リポジトリへ送る前にも、他のメンバーの変更を取り込むために使います。

## メイン図

### 図の狙い

`git pull` が「fetch → merge の 2 ステップ」である構造を 1 枚で見せ、リモートとローカルの同期イメージを掴んでもらいます。

### C. 概念図（figure_type: structure）

- 中心に置く概念: git pull = fetch + merge
- 周辺の要素: リモートリポジトリ（GitHub）／ローカルリポジトリ／作業コピー／fetch 矢印／merge 矢印
- 関係の描き方: リモート → fetch → ローカルリポジトリ → merge → 作業コピー の流れを 2 本の矢印で示す

## 会話での使い方例

「朝イチに git pull しておくと、他の人の変更が手元に入りますよ。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

リモートの最新変更を取得してローカルへ反映します。

### 2. うれしさ

1 コマンドで fetch と merge が済み、手元が最新になります。

### 3. 注意点

ローカルに未 commit の変更があると conflict が起きます。

### 4. どこで役立つか

チーム開発での朝イチ同期や、AI 提案の共有前確認に役立ちます。

### 5. はじめに

fetch と merge の 2 段構えと conflict の概念を押さえます。

### 6. 深掘り先

git fetch、git merge、rebase、conflict 解消。

## 開発フローでの位置（必須）

1. 朝イチに `git pull` — リモートの最新を手元に取り込む
2. 作業・AI にコード生成させる — ローカルで編集を進める
3. `git add` → `git commit` — 変更を記録する
4. `git push` — 完成した変更をリモートへ送る


## 関連用語

- git push
- git fetch
- merge
- branch
- リポジトリ


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

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: 左に雲マーク（リモートリポジトリ）、右にパソコン（ローカル）、2 本の矢印で fetch → merge の 2 ステップを示す構造図
- 登場人物: 朝出社したキャラクター 1 人がパソコンに向かう場面
- 吹き出し・心の声: 「まず pull して今日の差分を確認します。」
- 中央に置くキーワード/ラベル: git pull = fetch + merge

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: クラウド下矢印（pull）
- Step 2 のアイコン/絵柄: 鉛筆アイコン（作業・AI 生成）
- Step 3 のアイコン/絵柄: 保存アイコン＋スタンプ（add → commit）
- Step 4 のアイコン/絵柄: クラウド上矢印（push）
- 矢印で示す流れの意図: 取り込む → 編集 → 記録 → 送る のサイクルを示す


## コミュニティ補完メモ

- F-50 git: git 全体の概念・差分・責任の所在を扱う親エントリ。本エントリは pull コマンドに絞る
- F-51 git push: push は「送る」方向。pull の逆の操作。同義語的に語られやすいが方向が逆なので住み分けは明確
- F-53 branch: branch 操作との関係（どのブランチを pull するか）は F-53 に委ねる
- F-55 merge: pull の内部で呼ばれることは 1 文で言及するにとどめ、merge の詳細は F-55 に委ねる
- git fetch（単独エントリ未設定の場合）: fetch と merge を分けて実行したい場合の補足はコミュニティ補完として残す


## 出典メモ

- git-scm.com/docs/git-pull — checked 2026-04-29


## 備考

- `git pull --rebase` オプションで merge の代わりに rebase を使う流派があるが、詳細は別エントリへ
- conflict 解消の手順は本エントリのスコープ外。「注意点」で存在を示すにとどめる
