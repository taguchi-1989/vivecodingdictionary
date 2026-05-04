---
id: G-47
title: Auto-compact
title_reading: オートコンパクト
category: term_llm
subtype: ops
experience_level: hands_on
reader_level: 3-4
importance: E
figure_type: before_after
page_layout: spread_v1
start_date:
end_date:
version_status: active
pricing_note: none
evaluation_date: 2026-04-30
related_terms:
  - Claude Code
  - Context Window
  - CLAUDE.md
  - Context Engineering
status: needs_review
---

# Auto-compact

## tagline

会話履歴がコンテキスト枠（Context Window）を超えそうなとき、自動で要約・圧縮して続けられる仕組みです。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

Claude Code（略称 CC）の使用トークン（文字量の単位）が約 80% に達すると、過去履歴を短いダイジェストに置き換えます。圧縮後も会話を続けられ、長いセッションが途切れにくくなります。

## どこで出会うか

CC で長時間の開発セッションを続けると、画面に「会話が圧縮されました」と通知が出ます。`/compact` で手動実行も可能です。デフォルト ON なので、意識せず自動で動きます。

## メイン図

### 図の狙い

圧縮前後で「何が変わり、何が残るか」を一目で示します。

### A. Before / After（figure_type: before_after）

- Before
  - 状況: トークン使用量が 80% に到達しそう
  - 視覚要素（コード or 概念）: 長い会話ログが画面外にはみ出すイメージ
  - つまずき: 「もう指示が入らない、止まってしまう」
- After
  - 状況: Auto-compact が走り、過去履歴が要約ダイジェストに圧縮される
  - 視覚要素: 短い要約テキスト + 続きの会話が続く
  - うれしさ: セッションを切らずに作業を続けられる


## 会話での使い方例

「長いセッションは Auto-compact を意識し、要点を CLAUDE.md にメモしましょう。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

長い会話履歴を自動で要約し、コンテキスト枠の枯渇を防ぎます。

### 2. うれしさ

セッションを途中で切らずに長期の作業を継続できます。

### 3. 注意点

圧縮で細部が落ちるため、重要事項は別ファイルに残しておくと安全です。

### 4. どこで役立つか

数時間にわたる CC の長期セッションで特に効果を発揮します。

### 5. はじめに

デフォルト ON なので、存在を知っておくだけで戸惑いが減ります。

### 6. 深掘り先

Context Window、CLAUDE.md、Context Engineering


## 開発フローでの位置（必須）

1. 長期セッション開始 — CC で複数ファイルをまたぐ作業を始める
2. トークン蓄積 — 会話が増え、履歴がコンテキスト枠を圧迫し始める
3. Auto-compact 発動 — 使用量が閾値に達すると過去履歴が自動で要約される
4. 作業継続 — 要約後の枠でセッションを続け、中断なく開発を進める
5. 重要事項の保全 — 圧縮で落ちやすい詳細は CLAUDE.md やメモに事前に記録しておく


## 関連用語

- Claude Code
- Context Window
- CLAUDE.md
- Context Engineering


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

- 描く内容: 左側に長い会話ログが積み上がって枠からはみ出しそうな状態、右側に Auto-compact 後の短い要約ブロック＋続く会話の状態を並べる
- 登場人物（いれば）: 画面の前で作業するエンジニア風の人物
- 吹き出し・心の声: Before「あれ、もう枠が埋まりそう…」/ After「圧縮が走った。よし、続けられる」
- 中央に置くキーワード/ラベル: Auto-compact
- Before / After の場合の対比ポイント: 履歴の量（長い vs 短い要約）と会話の継続可否

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: ノート PC と作業開始アイコン
- Step 2 のアイコン/絵柄: バーが伸びるゲージ（トークン蓄積）
- Step 3 のアイコン/絵柄: 圧縮・折りたたみアイコン
- Step 4 のアイコン/絵柄: 会話継続の矢印
- Step 5 のアイコン/絵柄: ファイル保存・メモアイコン
- 矢印で示す流れの意図: 自動圧縮が挟まっても作業が途切れないサイクルを示す


## コミュニティ補完メモ

- G-5 Context Window との住み分け：Context Window は「枠の概念」の解説、Auto-compact は「枠が満杯に近づいたときに CC が自動で行う対処」。補完関係にある。
- G-32 /compact コマンドとの住み分け：/compact は手動実行のスラッシュコマンド。Auto-compact はそれを自動で行う CC の挙動。同じ圧縮処理の手動 vs 自動の違い。
- G-20 CLAUDE.md との住み分け：圧縮で落ちた文脈を補う手段として CLAUDE.md を参照。Auto-compact の注意点を説明する際にセットで紹介するとよい。

## 出典メモ

- Claude Code 公式ドキュメント（Anthropic）— checked 2026-04-29
- [Claude Code ドキュメント](https://docs.anthropic.com/ja/docs/claude-code/overview) — checked 2026-04-29


## 備考

- Auto-compact は Claude Code 固有の機能名。OpenAI Codex CLI や Cursor にも類似の自動圧縮機能が存在するが、挙動や名称は異なるため、比較は「コミュニティ補完メモ」で触れるにとどめ、本文には記載しない。
- version_status: active（2026-04-29 時点）。将来の CC バージョンで動作・閾値が変わる可能性あり。
