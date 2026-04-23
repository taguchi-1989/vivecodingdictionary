# 執筆優先度（ステージ別）

*2026-04-23 起草。全 332 件の候補から、どれを先に書くかの段取り。ステージ 1 でテンプレと構造を検証し、段階的に拡張する。*

## ステージ 0：すでに下書き済み（7 件）

旧 3 桁 ID で書かれたサンプル。新テンプレ（spread_v1）への書き直しを進める。

- F-1 JavaScript（旧 301）
- F-2 TypeScript（旧 302）— **既に v2 テンプレで書き直し済み**
- F-10 React（旧 304）
- F-11 Next.js（旧 305）
- F-20 ESLint（旧 303）
- B-1 Gemini（旧 101）
- D-2 Gemini 2.5 系（旧 201）

## ステージ 1：テンプレ検証（約 15 件）

掲載順の各 letter から「最も入口」にあたる語を 1〜2 件ずつ選んで書く。テンプレの過不足を早く潰す。

| # | ID | 候補 | 理由 |
| --- | --- | --- | --- |
| 1 | A-2 | この本の読み方 | 読者の玄関。序文級 |
| 2 | J-14 | LLM | 「聞いたことがある」入口。J の代表 |
| 3 | J-41 | DX | 非 AI 文脈の入口。バズワードの代表例として |
| 4 | B-2 | Claude | サービスの主役の 1 つ |
| 5 | B-7 | Claude Code | 本書の制作ツール自体。視点が具体的になる |
| 6 | C-2 | Anthropic | 会社の代表例。B-2 との接続確認 |
| 7 | D-12 | Claude 4 系 | モデル世代の書き方検証 |
| 8 | E-1 | SWE-Bench | ベンチマーク側の書き方検証 |
| 9 | F-1 | JavaScript | 既に下書きあり。v2 移行で確定 |
| 10 | F-2 | TypeScript | v2 完了済。参照用 |
| 11 | F-50 | git | 従来道具の入口 |
| 12 | G-1 | Context | バイブ特有語彙の核 |
| 13 | G-20 | CLAUDE.md | 設定ファイル系の代表 |
| 14 | I-1 | MCP | MCP 棚全体の入口 |
| 15 | H-53 | ChatGPT 登場 | 歴史の時系列エントリ 1 件 |

**目的**：10 letter × 複数サブ範囲を横断し、テンプレで書きにくい箇所を洗い出す。ステージ 1 完了後に図のポンチ絵・本文量・6 視点の字数をまとめて見直す。

## ステージ 2：核となる基礎語彙（約 40 件）

ステージ 1 で問題がなければ展開する。各 letter の「絶対に載せるべき」基礎を埋める。

- A: A-1 まえがき / A-4 体験区分 / A-5 読者レベル
- B: B-1 Gemini / B-3 ChatGPT / B-4 Cursor / B-5 GitHub Copilot / B-20 Vercel / B-23 AWS / B-50〜52 料金プラン
- C: C-1 OpenAI / C-3 Google DeepMind / C-9 NVIDIA / C-50 Sam Altman / C-51 Dario Amodei
- D: D-2 Gemini 2.5 系（済）/ D-11 Claude 3.5 系 / D-13 Claude 4.5 系 / D-20 GPT-5 系 / D-30 Grok 系 / D-40 Llama 系
- E: E-2 SWE-Bench Verified / E-20 MMLU / E-50 Chatbot Arena
- F: F-3 Python / F-4 HTML / F-5 CSS / F-10 React（済）/ F-11 Next.js（済）/ F-20 ESLint（済）/ F-30 VS Code / F-51〜55 git 系
- G: G-2 Token / G-10 Prompt Engineering / G-30 Tool Use / G-40 バイブコーディング
- H: H-3 バイブコーディングの流儀 / H-50 Bard → Gemini
- I: I-2 MCP Server / I-11 GitHub MCP
- J: J-11 Deep Learning / J-13 Transformer / J-51 Hallucination / J-77 GPU（概念）

## ステージ 3：拡張・深掘り（残り約 270 件）

ステージ 1・2 で確定した型で、残りを並行執筆。優先順は以下の基準で判定：

1. **読者が会話で遭遇する頻度**（使用頻度順）
2. **時変情報の鮮度**（モデル名・料金など、古くなりやすいものを先に）
3. **連関の強い近接語彙**（1 つ書くと隣が書きやすくなる群）

## 運用メモ

- ステージ 1 は 15 件に限定。これが終わるまでステージ 2 には手を付けない
- 各ステージ完了ごとに、`docs/editorial_style.md` と `templates/entry_template.md` の見直しを入れる
- 「要確認」が残っているエントリ（Claude Cowork、Amical、Supercell 等）は正式名確定後に着手
- 執筆の着手ログは `ledgers/entries.csv` の `status` 列を `drafting` → `needs_review` → `ready` と更新して追跡
