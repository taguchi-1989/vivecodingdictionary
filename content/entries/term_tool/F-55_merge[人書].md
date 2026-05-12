---
id: F-55
title: merge
title_reading: マージ
category: term_tool
subtype: git
experience_level: hands_on
reader_level: 2
importance: C
figure_type: before_after
page_layout: spread_v1
version_status: active
evaluation_date: 2026-04-29
related_terms:
  - branch
  - commit
  - git pull
  - conflict
  - rebase
status: ready
---

# merge

## tagline

別の branch（枝）の変更を、今いる枝に取り込む操作です。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

`git merge` は、分岐して別々に進んでいる 2 本の branch を 1 本に合流させます。取り込んだ変更は新しい commit として履歴に残り、どこで合流したかが後から追えます。

## どこで出会うか

feature branch（機能開発用の枝）での作業が終わり、main（本線）に取り込む場面で登場します。`git pull` も内部で merge を呼ぶため、他の人の変更を取り込むたびに使われます。

## メイン図

### 図の狙い

「merge 前に 2 本の枝が分かれている状態」と「merge 後に 1 本に合流した状態」を左右に並べ、変更が合流するイメージを掴んでもらいます。

### A. Before / After（figure_type: before_after）

- Before
  - 状況: main と feature が分岐して、それぞれ commit が進んでいる
  - 視覚要素（コード or 概念）: main から枝が 2 本伸び、それぞれに commit が積まれている図
  - つまずき: 2 つの枝がどこで何が違うか分からず、取り込み方が見えない
- After
  - 状況: `git merge feature` を実行し、feature の変更が main に取り込まれた
  - 視覚要素: 2 本の枝が 1 点に合流し、merge commit が生まれた図
  - うれしさ: 変更が 1 本になり、どの枝の何が合流したか履歴で追える

## 会話での使い方例

「feature branch で作った機能、確認できたので main に merge しておきますね。」

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

2 本の branch を合流させ、変更を 1 本の履歴にまとめます。

### 2. うれしさ

並行開発した変更を安全に統合でき、経緯が履歴に残ります。

### 3. 注意点

同じ箇所を両方で変えると conflict（競合）が起きて手動解消が必要です。

### 4. どこで役立つか

機能ブランチの統合、pull request のマージ、共同開発に役立ちます。

### 5. はじめに

branch が何かと、merge commit が履歴に残る仕組みを押さえます。

### 6. 深掘り先

rebase、conflict 解消、fast-forward merge、pull request。

## 開発フローでの位置（必須）

1. branch を作る — feature branch で作業を開始する（F-53）
2. commit を積む — 変更を記録しながら開発を進める（F-54）
3. main に切り替える — `git checkout main` で本線へ戻る
4. merge を実行する — `git merge feature` で変更を取り込む
5. conflict を解消する — 競合があれば手動で解決して commit する


## 関連用語

- branch
- commit
- git pull
- conflict
- rebase


<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

- 単純な流れならうまくいくのですが、コンフリクトが起きて解決できなくなったときはブランチごと捨てたこともありました。エラーが意味不明で VS Code の作業も無駄になったときはつらかったです。
- 最近はコストが低くなったためか、merge をあまり意識しなくなっています。

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

- 🙂 第一印象: 「くっつけるんだろうな」という素朴な感覚でした。
- 👍 良い点: 並列開発の成果を取り込む仕組みとして適切に機能しています。
- 👎 ダメな点: 素直にマージできないときがありますが、それは開発側の問題であることが多いです。
- 👥 誰向けか: 継続的に運用していく人には必要な操作です。

<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: before_after）

- 描く内容: 左に 2 本の枝が分岐したまま伸びている状態、右に 2 本が 1 点に合流して merge commit が生まれた状態
- 登場人物: キャラクター 1 人。Before で困り顔（「どっちが正しい？」）、After で安心顔（「1 本にまとまった」）
- 吹き出し・心の声: Before「branch が 2 本ある、どうやって合わせるんだろう」／After「merge commit で合流した、履歴にも残ってる」
- 中央に置くキーワード/ラベル: `git merge` ＝ 枝を合流させる

### 6視点アイコン（右ページ上段）

- 共通アイコン流用

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: 枝分かれアイコン（branch 作成）
- Step 2 のアイコン/絵柄: スタンプアイコン（commit）
- Step 3 のアイコン/絵柄: 矢印で main へ切り替え
- Step 4 のアイコン/絵柄: 合流アイコン（2 本の線が 1 点に集まる）
- Step 5 のアイコン/絵柄: レンチ・解消アイコン（conflict 解消）
- 矢印で示す流れの意図: 枝で作って → 記録して → 本線に戻って → 合流させる、の一連の流れ

## コミュニティ補完メモ

- merge の上位概念は F-50 git。git 全体（差分・履歴・責任の所在）は F-50 で扱い、merge は「2 本の枝を合流させる操作」に絞る。
- branch（F-53）は「枝を作る」、merge（F-55）は「枝を合流させる」のペア関係。相互に関連用語で参照する。
- git pull（F-52）は内部で merge を呼ぶが、pull の「リモートから取ってくる」操作は F-52 に任せ、本エントリは merge 単体の「2 本を合流させる」に集中する。
- conflict（競合）の詳細な解消手順は別エントリへ逃がす。本エントリでは「起きる可能性がある」程度に留める。
- rebase は「歴史を直線にする派」で別エントリ。merge は「合流の証跡を残す派」として対比の一言だけ触れる程度にする。


## 出典メモ

- git-scm.com/docs/git-merge — checked 2026-04-29
- Pro Git book（git-scm.com/book）— checked 2026-04-29


## 備考

- title は "merge" のまま使用（F-50 git のスタイルに合わせ、コマンド名をそのまま title にする方針）。
- git pull（F-52）との相互参照が重要。pull を説明するとき「内部で merge を使います」と参照できる。
