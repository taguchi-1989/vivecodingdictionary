---
id: G-39
title: Permission
title_reading: パーミッション
category: term_llm
subtype: control
experience_level: hands_on
reader_level: 3-4
importance: D
figure_type: structure
page_layout: spread_v1
start_date:
end_date:
version_status: active
pricing_note: none
evaluation_date: 2026-04-30
related_terms:
  - Claude Code
  - settings.json
  - Plan Mode
  - Hook
status: needs_review
---

# Permission

## tagline

AI エージェントのツール実行を allow / deny / ask の 3 値で制御する許可ルールです。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

Claude Code（CC）がツールを呼ぶたびに設定ルールを参照し、実行を許可・拒否・確認のいずれかに振り分けます。`allow` リストを整えると毎回の確認が省けます。

## どこで出会うか

`settings.json` の `permissions` キーとして現れます。CC を使い始め「この操作は毎回確認が入る」と感じたとき、ルールを整えるきっかけになります。

## メイン図

### 図の狙い

ツール呼び出しが来たとき、設定ルールに従って 3 通りに分岐する流れを示す。

### C. 概念図（figure_type: structure）

- 中心に置く概念: Permission ルール判定
- 周辺の要素: Bash / Edit / Write / MCP の各ツール、allow / deny / ask の 3 出力先
- 関係の描き方: ツール呼び出し → 判定ボックス → 3 方向の矢印


## 会話での使い方例

「Permission で `git status` を allow にしておくと、毎回確認されずに済みます。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

ツール実行を allow / deny / ask の 3 値で制御します。

### 2. うれしさ

確認不要の操作を事前宣言でき、作業が中断しません。

### 3. 注意点

allow リストが増えすぎると管理コストが上がります。

### 4. どこで役立つか

チーム開発で settings.json を共有する場面で機能します。

### 5. はじめに

allow / deny / ask の 3 値と設定ファイルの場所を把握することです。

### 6. 深掘り先

Plan Mode, Hook, YOLO モード

## 開発フローでの位置（必須）

1. 設定ファイル作成 — `.claude/settings.json` に `permissions` を追加します
2. ルール記述 — `allow` と `deny` に該当操作を列挙します
3. CC 起動 — ツール呼び出し時にルールが参照されます
4. 運用調整 — `ask` が多い操作を `allow` に昇格します
5. チーム共有 — settings.json を Git に commit して統一します


## 関連用語

- Claude Code
- settings.json
- Plan Mode
- Hook


<!-- ━━━━━━━━ 著者記入欄（右ページ下段に印刷される／AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

-
-どこまで委任するかが鍵やね。これ黒どこである？あるが、昔使った人はもう本当イエスをひたすら押すみたいなところが仕事じゃないけど、それの管理で手いっぱいなったりとかってのは昔良かったけど、あと一方でデンタル3。スキップパーミッションみたいなこともある人も私も含めているだろうし、ここのパーミッション設定ってのは結構鍵ではあったんだけど、ミッションよりもえっと何だろうな。しっかり7時を守りながらやってくれるようなところもあるので、えっと重要だけど、技術的にだいぶ解決されてきたって印象かな？
-

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

- 🙂 第一印象:とりあえず全部委任したいて思ったなバイブコーナーなので
- 👍 良い点:しっかり設定するとやっちゃいけないようなあの。栗東で昔のやつ吹っ飛ばすみたいな。そんな機能とかはやっちゃいけないところは許可
- 👎 ダメな点:何も考えずにスキプっていう風にやって吹っ飛ばされるのが昔はあった。多分今はもうほとんどないと思うけど
- 👥 誰向けか:エージェントで偉人をしてやる人はどんなんじゃないかな


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: ツール呼び出しが来たとき、Permission ルールに照らして 3 方向に分岐するフロー図
- 登場人物（いれば）: 開発者（人物シルエット）が CC に指示を出す場面
- 吹き出し・心の声: 開発者「git status は毎回聞かないで！」→ Permission ルール「allow に入ってるから自動実行します」
- 中央に置くキーワード/ラベル: `allow / deny / ask` の 3 分岐ボックス
- Before / After の場合の対比ポイント: （今回は structure なので不要）

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: ファイルアイコン（設定ファイル）
- Step 2 のアイコン/絵柄: リストアイコン（ルール記述）
- Step 3 のアイコン/絵柄: 稲妻アイコン（CC 起動・自動判定）
- Step 4 のアイコン/絵柄: スライダーアイコン（調整）
- Step 5 のアイコン/絵柄: グループアイコン（チーム共有）
- 矢印で示す流れの意図: 設定 → 記述 → 実行 → 改善 → 共有の一方向フロー


## コミュニティ補完メモ

- G-38 Plan Mode との住み分け：Plan Mode は「計画段階で人間が確認する」仕組み、Permission は「実行段階で自動判定するルール」。二層防御として組み合わせて使う。
- G-31 Hook との住み分け：Hook はツール実行の前後に処理を挟む仕組み。Permission は実行可否の判定、Hook は実行前後の副次処理という役割の違いがある。
- G-23 settings.json との関係：Permission の設定は settings.json の `permissions` キーに書く。settings.json エントリで設定ファイル全体を解説し、本エントリは Permission ルールの意味と運用に絞る。
- 「YOLO モード」はすべての権限チェックをスキップする設定。Permission のアンチパターンとして言及する価値があるが、単体エントリがあれば深掘り先として誘導する。


## 出典メモ

- Anthropic ドキュメント「Claude Code / Settings」— checked 2026-04-30


## 備考

- `permissions.allow` の値は `Bash(コマンド名)` のようにツール名＋引数パターンで指定する形式（2026-04-30 時点）。形式は変更される可能性があるため evaluation_date を付与。
- YOLO モード（`--dangerously-skip-permissions` フラグ）は全許可チェックをスキップするため、自動化スクリプト用途に限定することが推奨されている。
