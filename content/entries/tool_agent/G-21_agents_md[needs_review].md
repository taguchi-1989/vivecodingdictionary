---
id: G-21
title: AGENTS.md
title_reading: エージェンツエムディー
category: tool_agent
subtype: config_file
experience_level: partial
reader_level: 3
importance: C
figure_type: structure
page_layout: spread_v1
start_date:
end_date:
version_status: active
pricing_note: none
evaluation_date: 2026-04-29
related_terms:
  - CLAUDE.md
  - Cursor
  - Codex
  - System Prompt
  - SKILL.md
status: needs_review
---

# AGENTS.md

## tagline

複数の AI コーディングツールが共通で読める、ツール非依存のプロジェクト指示書です。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

プロジェクトのルートに置くと、Cursor や Codex、OpenHands など対応する AI エージェントが読み込み、コーディング規約や注意事項を把握した状態で動き始めます。特定のツールに縛られない点が特徴です。

## どこで出会うか

複数の AI コーディングツールをチームで使い分ける場面や、ツールを乗り換えるときに紹介されやすいです。Claude Code は CLAUDE.md（G-20）を優先しますが、AGENTS.md も読めます。

## メイン図

### 図の狙い

AGENTS.md を中心に、Cursor・Codex・OpenHands など複数ツールが同じファイルを読む関係を示し、「1 つ書けば複数に届く」を掴んでもらう。

### C. 概念図（figure_type: structure）

- 中心に置く概念: AGENTS.md（プロジェクトルートに置かれたファイル）
- 周辺の要素: Cursor / Codex / OpenHands / Claude Code（AGENTS.md も読める）
- 関係の描き方: 中心から各ツールへ矢印。Claude Code は CLAUDE.md との両矢印で補足

## 会話での使い方例

「AGENTS.md を置いておくと、ツールが変わっても規約を読み直させる手間が省けます。」

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

ツールを問わず AI エージェントが読む共通の指示書です。

### 2. うれしさ

1 つ書けば複数ツールに同じ規約を伝えられます。

### 3. 注意点

対応ツールはまだ広がりつつある段階で、全ツールが読むわけではありません。

### 4. どこで役立つか

複数ツールを使い分けるチームでの規約統一に効果的です。

### 5. はじめに

CLAUDE.md との違いは「ツール依存か汎用か」の 1 点です。

### 6. 深掘り先

CLAUDE.md、SKILL.md、System Prompt

## 開発フローでの位置（必須）

1. 規約を整理 — コーディング規約・禁止事項を箇条書きにまとめる
2. AGENTS.md を作成 — プロジェクトルートにファイルを置き、規約を記述する
3. エージェントが読み込む — 対応ツールがセッション開始時に自動で把握する
4. ツール追加時も流用 — 新しいツールを導入してもファイルを書き直す必要がない
5. 定期的に更新 — チームの合意を得て Git でレビューしながら規約を育てる

## 関連用語

- CLAUDE.md
- Cursor
- Codex
- System Prompt
- SKILL.md

<!-- ━━━━━━━━ 著者記入欄（右ページ下段に印刷される／AI は触らない） ━━━━━━━━ -->

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

- 描く内容: 中央に AGENTS.md のファイルアイコン。周囲に Cursor・Codex・OpenHands・Claude Code の各ツールアイコンを配置し、中央から各ツールへ矢印を引く。Claude Code だけ CLAUDE.md との両矢印も添える
- 登場人物: ファイルそばに人物（開発者）が AGENTS.md を書いている姿
- 吹き出し・心の声: 「1 つ書けば全部に届く」「ツール変えても大丈夫」
- 中央に置くキーワード/ラベル: AGENTS.md ＝ 汎用の指示書

### 6視点アイコン（右ページ上段）

- 共通アイコン流用

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: 付箋に規約を書く人
- Step 2 のアイコン/絵柄: フォルダにファイルを置く人
- Step 3 のアイコン/絵柄: 複数ツールが本を開いて読むアイコン
- Step 4 のアイコン/絵柄: 新しいツールを追加してもファイルがそのまま使える図
- Step 5 のアイコン/絵柄: チームで Git でレビューする人たち
- 矢印で示す流れの意図: 「整理 → 記述 → 自動読込 → 流用 → 更新」の循環

## コミュニティ補完メモ

- CLAUDE.md（G-20）との住み分け：CLAUDE.md は Claude Code 専用の指示書。AGENTS.md は Cursor・Codex・OpenHands など複数ツールが読む汎用版。Claude Code のみを使うなら CLAUDE.md で十分。
- SKILL.md（G-22）との住み分け：AGENTS.md はプロジェクト全体の規約を伝える。SKILL.md はエージェントが参照するスキル・手順書の単位ファイル。AGENTS.md から SKILL.md を参照させる使い方もある。
- settings.json（G-23）との住み分け：設定ファイルで権限やツールを制御し、AGENTS.md は自然言語で文脈・規約を伝える。補完関係にある。
- 「対応ツールが広がりつつある」の状況は 2026-04-29 時点の評価。今後追加ツールが増える可能性がある。

## 出典メモ

- docs.github.com/en/copilot/customizing-copilot/adding-personal-custom-instructions-for-github-copilot — checked 2026-04-29
- openai.com/index/introducing-codex — checked 2026-04-29
- docs.all-hands.ai/usage/how-to/github-action — checked 2026-04-29

## 備考

- AGENTS.md は OpenAI が Codex CLI の文脈で広めた仕様が起点。その後 Cursor・OpenHands 等が追随し、事実上の共通フォーマットになりつつある。
- Claude Code は CLAUDE.md を優先するが、AGENTS.md も読むことができる（両ファイル共存可）。
- 「採用は広がりつつある」段階のため、対応ツールの最新状況は各ツールの公式ドキュメントで確認が必要。
