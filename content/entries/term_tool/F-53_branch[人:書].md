---
id: F-53
title: branch
title_reading: ブランチ
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
  - git
  - commit
  - merge
  - git push
  - git pull
status: needs_review
---

# branch

## tagline

作業の枝を切り出し、本線を壊さずに並行開発できるようにします。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

git の履歴から「枝（ブランチ）」を切り出し、本線（main）に影響を与えずに変更を試せます。作業が終わったら merge（F-55）で本線に合流させます。

## どこで出会うか

AI にコードを書かせるとき、機能ごとに branch を切っておくと、失敗しても本線を汚さずに捨てられます。チームでは「どの branch で作業するか」が共有の合言葉になります。

## メイン図

### 図の狙い

main から branch が枝分かれし、作業後に合流する流れを 1 枚で見せます。

### C. 概念図（figure_type: structure）

- 中心に置く概念: main ブランチ（1 本の幹）
- 周辺の要素: feature-A ブランチ／feature-B ブランチ／merge 先の合流点
- 関係の描き方: 幹から枝が横に伸び、矢印で合流点へ戻る


## 会話での使い方例

「この機能は branch を切って試したので、main はきれいなままです。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

main を保ったまま、作業用の独立した枝を作ります。

### 2. うれしさ

本線を壊さずに試せるので、AI の提案も気軽に検証できます。

### 3. 注意点

長期放置した branch は合流時に競合（コンフリクト）が起きます。

### 4. どこで役立つか

機能追加・バグ修正・実験的な変更のすべてで基盤になります。

### 5. はじめに

切り方（`git branch` / `git switch -c`）と main との関係。

### 6. 深掘り先

merge、rebase、pull request。

## 開発フローでの位置（必須）

1. branch を切る — `git switch -c feature-xxx` で作業用の枝を作成する
2. commit を積む — 変更を記録しながら作業を進める（F-54）
3. push して共有 — リモートに枝を送り、チームに見せる（F-51）
4. merge で合流 — レビュー後に main へ取り込む（F-55）


## 関連用語

- git
- commit
- merge
- git push
- git pull


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

- 描く内容: 横向きの時系列に main ブランチが走り、そこから feature-A と feature-B の枝が伸び、合流点に戻る構造図
- 登場人物: 開発者 1 人。feature ブランチ上で作業中の表情（集中）と、main に合流した後の表情（安堵）
- 吹き出し・心の声: 作業中「main は汚さないで済む」／合流後「きれいに取り込めた」
- 中央に置くキーワード/ラベル: branch ＝ 枝を切る ＝ 本線を守る

### 6視点アイコン（右ページ上段）

- 共通アイコン流用

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: 枝切りアイコン（ブランチ分岐の矢印）
- Step 2 のアイコン/絵柄: 保存アイコン（commit の積み重ね）
- Step 3 のアイコン/絵柄: クラウド矢印（push）
- Step 4 のアイコン/絵柄: 合流アイコン（merge の合流点）
- 矢印で示す流れの意図: 切る → 積む → 送る → 合流 のループ


## コミュニティ補完メモ

- git 全体の概念は F-50 git が担う。本エントリは branch 操作（切り出し・命名・切り替え）に絞る
- 合流の動作（コンフリクト解決・fast-forward の違い）は F-55 merge が担う
- push/pull の送受信詳細は F-51／F-52 が担う
- commit の積み方は F-54 commit が担う
- rebase・worktree・cherry-pick は別エントリ（スコープ外）

## 出典メモ

- git-scm.com/docs/git-branch — checked 2026-04-29

## 備考

branch 名の命名規則（feature/、hotfix/ 等）は組織によって異なるため、本文では扱わない。pull request（PR）との関係は GitHub（F-60）エントリが担う想定。
