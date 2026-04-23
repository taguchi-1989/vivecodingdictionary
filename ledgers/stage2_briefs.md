# Stage 2 執筆ブリーフ（46 件）

*Stage 2 対象の各エントリに、執筆開始前の下準備メモを並べます。3 項目：figure_type 推奨／主要出典／スコープ境界。*

*運用：[skills/write-entry.md](../skills/write-entry.md) Step 2（YAML 埋め）の直前に、該当エントリをここで拾う。entry_candidates.md の 1 行記述と併読。*

*書き終わったら各行に ✅ を付けて進捗可視化。書き直しが必要になった行は ⚠️。*

---

## A — 序文・メタ（3 件）

### A-1 まえがき
- figure_type: なし（または表紙風の扉絵）
- 主要出典: 著者の動機・立場（book_philosophy.md）
- スコープ境界: 読み方は A-2、歩き方は A-3、ID 体系は A-11 へ

### A-4 体験区分の凡例
- figure_type: comparison（hands_on／partial／research_only の対比表）
- 主要出典: book_philosophy.md §著者属性
- スコープ境界: 個別判定は各エントリ内。本エントリは意味と表記ルールだけ

### A-5 読者レベルの凡例
- figure_type: structure（Level 1〜6 の階段図）
- 主要出典: 著者が本書で設定する目安
- スコープ境界: カリキュラム的な順路指導は A-3 へ

## B — サービス（9 件）

### B-1 Gemini
- figure_type: structure（サービス／モデル／API／Vertex の 4 入口）
- 主要出典: gemini.google.com、deepmind.google、cloud.google.com/vertex-ai
- スコープ境界: モデル詳細は D-2 Gemini 2.5 系へ。Bard 改名の歴史は H-50 へ

### B-3 ChatGPT
- figure_type: structure（ChatGPT アプリ／API／GPT-5 系モデルの関係）
- 主要出典: openai.com、chatgpt.com
- スコープ境界: モデル世代詳細は D-20 GPT-5 系へ。登場の歴史は H-53 へ（済）

### B-4 Cursor
- figure_type: before_after（VS Code 単体との対比、AI が常駐）
- 主要出典: cursor.com、cursor.com/features
- スコープ境界: 独自モデル（Composer、cursor-tab-3）は D-35 へ

### B-5 GitHub Copilot
- figure_type: before_after（手打ち／補完なし → Copilot 補完あり）
- 主要出典: github.com/features/copilot
- スコープ境界: GitHub 本体は F-60、Copilot Chat は別派生

### B-20 Vercel
- figure_type: structure（コード push → Preview URL → Production）
- 主要出典: vercel.com
- スコープ境界: Next.js は F-11（済）、v0 は B-9 へ

### B-23 AWS
- figure_type: structure（EC2／S3／Bedrock／Lambda ほかの主要サービス傘）
- 主要出典: aws.amazon.com
- スコープ境界: Bedrock は B-30 で個別、他クラウドとの対比は B-24/B-25 と自然に

### B-50 Claude の料金プラン
- figure_type: comparison（Free／Pro／Max 5x／Max 20x／Team／Enterprise の縦比較）
- 主要出典: claude.com/pricing、claude.com/pricing/max（checked 2026-04-24）
- スコープ境界: API 料金（per-token）は別枠で言及。ChatGPT／Gemini 比較は B-51／B-52 へ

### B-51 ChatGPT の料金プラン
- figure_type: comparison
- 主要出典: openai.com/chatgpt/pricing
- スコープ境界: モデルごとの能力差は D-20 へ。API 料金は別

### B-52 Gemini の料金プラン
- figure_type: comparison
- 主要出典: gemini.google.com、one.google.com（AI Pro / AI Ultra）
- スコープ境界: Vertex AI の法人向けは B-27 で独立扱い

## C — 人・会社（5 件）

### C-1 OpenAI
- figure_type: structure（ChatGPT／API／Codex／DALL・E／Sora の事業傘）
- 主要出典: openai.com
- スコープ境界: Sam Altman は C-50、各モデル詳細は D 系へ

### C-3 Google DeepMind
- figure_type: structure（Gemini／AlphaFold／研究部門の位置づけ）
- 主要出典: deepmind.google
- スコープ境界: Gemini サービスは B-1、モデルは D-2 へ

### C-9 NVIDIA
- figure_type: structure（GPU／CUDA／DGX の関係、AI インフラの位置づけ）
- 主要出典: nvidia.com
- スコープ境界: GPU の概念は J-77 へ、CUDA は別エントリ候補

### C-50 Sam Altman
- figure_type: なし or 登場シーン（会社を率いる発言者としての位置）
- 主要出典: 公式プロフィール、主要発表文の一次情報
- スコープ境界: OpenAI 組織論は C-1 へ、個人史は最小限

### C-51 Dario Amodei
- figure_type: なし or 登場シーン
- 主要出典: anthropic.com 創業メンバーページ、公開論文・インタビュー
- スコープ境界: Anthropic 組織論は C-2（済）へ

## D — モデル（5 件）

### D-11 Claude 3.5 系
- figure_type: timeline（3.5 Sonnet → 3.5 Haiku → Sonnet 3.7 の流れ）
- 主要出典: anthropic.com/news、docs.anthropic.com
- スコープ境界: 4 系は D-12（済）、4.5 系は D-13 へ

### D-13 Claude 4.5 系
- figure_type: timeline（4.5 Sonnet → 4.5 Haiku、他 4 系との違い）
- 主要出典: anthropic.com/news、docs.anthropic.com
- スコープ境界: 4 系全体論は D-12（済）、ナーフの一般論は G-46 へ

### D-20 GPT-5 系
- figure_type: timeline or comparison（GPT-4 → GPT-5 → reasoning 系）
- 主要出典: openai.com/index/gpt-5、platform.openai.com/docs
- スコープ境界: ChatGPT サービスは B-3、o1/o3 等の reasoning 系は別サブ

### D-30 Grok 系
- figure_type: timeline（Grok-1 → Grok-2 → Grok-3/4）
- 主要出典: x.ai、grok.com
- スコープ境界: xAI 組織論は別枠、X（Twitter）連携は触れる程度

### D-40 Llama 系
- figure_type: timeline（Llama 1〜4 の系譜、オープンモデルの代表）
- 主要出典: llama.com、ai.meta.com
- スコープ境界: DeepSeek／Qwen は別エントリ、オープンモデル総論は別

## E — ベンチマーク（3 件）

### E-2 SWE-Bench Verified
- figure_type: structure（SWE-Bench 全体 → Verified サブセット）
- 主要出典: openai.com "SWE-Bench Verified" ブログ、swebench.com
- スコープ境界: 親の SWE-Bench は E-1（済）、派生は別エントリ

### E-20 MMLU
- figure_type: structure（57 タスクの傘と主要カテゴリ）
- 主要出典: paperswithcode.com/sota/multi-task-language-understanding-on-mmlu
- スコープ境界: MMLU-Pro 等の派生は別エントリ、人間水準との比較は軽く

### E-50 Chatbot Arena
- figure_type: workflow（ユーザー投票 → ELO レーティングの流れ）
- 主要出典: lmarena.ai、arxiv 元論文
- スコープ境界: 個別モデルの順位推移は時変情報で最小限に

## F — 従来コード語彙（9 件）

### F-3 Python
- figure_type: structure（言語／エコシステム／AI/ML での地位）
- 主要出典: python.org
- スコープ境界: ライブラリ群（NumPy／pandas／PyTorch）は別エントリ

### F-4 HTML
- figure_type: before_after（テキスト → ブラウザ表示）or structure
- 主要出典: developer.mozilla.org
- スコープ境界: CSS は F-5、JS は F-1 へ

### F-5 CSS
- figure_type: before_after（スタイル前／後）
- 主要出典: developer.mozilla.org
- スコープ境界: Tailwind などのフレームワークは別、プリプロセッサは別

### F-30 VS Code
- figure_type: structure（エディタ＋拡張のプラットフォーム）
- 主要出典: code.visualstudio.com
- スコープ境界: Cursor との関係は B-4、Copilot は B-5

### F-51 git add
- figure_type: workflow（working → staging → commit）
- 主要出典: git-scm.com/docs
- スコープ境界: git 全体は F-50（済）へ、個別コマンドは互いに参照

### F-52 git commit
- figure_type: workflow or before_after
- 主要出典: git-scm.com/docs
- スコープ境界: F-50 と連携、commit message 規約は触れる程度

### F-53 git push
- figure_type: structure（ローカル → リモート）
- 主要出典: git-scm.com/docs
- スコープ境界: リモート側は GitHub（F-60）、pull は F-54

### F-54 git pull
- figure_type: structure（pull ＝ fetch ＋ merge）
- 主要出典: git-scm.com/docs
- スコープ境界: rebase 派は別エントリ、conflict 解消の詳細は別

### F-55 git branch
- figure_type: structure（枝分かれ／合流）
- 主要出典: git-scm.com/docs
- スコープ境界: merge 戦略、worktree は別エントリ

## G — バイブ特有語彙（4 件）

### G-2 Token
- figure_type: before_after（文字列 → token 分割）
- 主要出典: platform.openai.com/tokenizer、anthropic docs
- スコープ境界: Context は G-1（済）、料金との関係は料金エントリへ

### G-10 Prompt Engineering
- figure_type: comparison（雑な指示 → 整えた指示）
- 主要出典: Anthropic docs、OpenAI cookbook、研究論文
- スコープ境界: Context Engineering（G-11）との違いを明示、System Prompt は別

### G-30 Tool Use
- figure_type: workflow（LLM → ツール呼び出し → 結果回収）
- 主要出典: docs.anthropic.com、platform.openai.com
- スコープ境界: MCP は I-1（済）で標準化、Function Calling は別扱い可

### G-40 バイブコーディング
- figure_type: structure or timeline（本書の中心語彙、AI 時代の開発スタイル）
- 主要出典: 著者の体験と公開記事（Karpathy 発言など）
- スコープ境界: 歴史は H-3、個別ツールは各エントリへ誘導

## H — 進め方・歴史（2 件）

### H-3 バイブコーディングの流儀
- figure_type: workflow（AI に任せる ↔ 人が確認する）
- 主要出典: 著者のまとめ＋関連記事
- スコープ境界: 用語定義は G-40、個別ツールは B 系へ

### H-50 Bard → Gemini
- figure_type: timeline（2023-02 Bard → 2024-02 Gemini 改名 → 以降の世代）
- 主要出典: blog.google、deepmind.google
- スコープ境界: 現行 Gemini は B-1、モデル世代は D-2 へ

## I — MCP（2 件）

### I-2 MCP Server
- figure_type: structure（MCP Client ⇔ Server ⇔ External Service の位置）
- 主要出典: modelcontextprotocol.io、anthropic.com
- スコープ境界: プロトコル全体は I-1（済）、個別 MCP は I-10 以降へ

### I-11 GitHub MCP
- figure_type: workflow（Claude Code → GitHub MCP → issue 操作など）
- 主要出典: github.com/github/github-mcp-server
- スコープ境界: GitHub 本体は F-60、他の MCP は I-10/I-20 等へ

## J — 一般語彙（4 件）

### J-11 Deep Learning
- figure_type: structure（ニューラルネット → 深層化の位置）
- 主要出典: 教科書系（Goodfellow "Deep Learning" 等）、MIT/Stanford 公開資料
- スコープ境界: Transformer は J-13、LLM は J-14（済）

### J-13 Transformer
- figure_type: structure（Attention ＋ 多層、2017 論文の骨格）
- 主要出典: "Attention Is All You Need"（arXiv:1706.03762）、Illustrated Transformer
- スコープ境界: Attention 単独は別エントリ候補、MoE は J-18 等

### J-51 Hallucination
- figure_type: before_after（Context 不足 → 事実と違う回答）
- 主要出典: Anthropic docs、研究論文
- スコープ境界: Context 設計は G-1（済）、再現性の議論は別

### J-77 GPU（概念）
- figure_type: structure（CPU との対比、並列計算の役割）
- 主要出典: nvidia.com、教科書系
- スコープ境界: NVIDIA 企業は C-9、CUDA は別エントリ候補

---

## 運用メモ

- 図解方針（人の視点主役）はプロジェクトメモリ「誌面図解は『人の視点』が主役」を参照
- 時変情報（料金、モデル名、リリース日）は必ず `evaluation_date: 2026-04-24` 付きで書く
- 迷ったら書かずに要確認リストに戻す（推測で埋めない）

## 履歴

- v0.1（2026-04-24）: 初版。writing_priority.md §ステージ 2 の 46 件に対応。
