# 次セッションへの引き継ぎ（2026-04-24 v3 更新）

*コンテキストが増えてきたので区切ります。次セッションはこのファイルを最初に開いて続きから再開してください。*

## 直近までの状態（サマリ）

### 決まっていること

- **本のフィロソフィー・著者属性・執筆ポリシー**：[docs/book_philosophy.md](../docs/book_philosophy.md) に確定
- **ID 体系**：letter A〜J の 10 区切り、10 番刻みサブ範囲。v0.5 確定版（[docs/id_scheme.md](../docs/id_scheme.md)）
- **エントリ候補**：335 件（[ledgers/entry_candidates.md](entry_candidates.md)）
- **テンプレ**：spread_v1（見開き 2 ページ）。[templates/entry_template.md](../templates/entry_template.md)
- **トーン**：です・ます調、カタカナ語は日本語訳を初出で補う、略称は展開
- **執筆優先度**：ステージ別（[ledgers/writing_priority.md](writing_priority.md)）
- **タイムライン方針**：4 案（a/b/c/d）全採用。細部は [drafts/prototypes/timeline_drafts.md](../drafts/prototypes/timeline_drafts.md)
- **リポジトリ**：<https://github.com/Taguchi-1989/ViveCodingDictionary>

### 書き出し済みエントリ（spread_v1）

- A-2 この本の読み方
- B-2 Claude
- C-2 Anthropic
- D-12 Claude 4 系（timeline 型）
- E-1 SWE-Bench（workflow 型）
- F-50 git（before_after 型）
- G-1 Context
- H-53 ChatGPT 登場（timeline 型）
- I-1 MCP
- J-14 LLM
- 旧 3 桁 ID のサンプル 301〜305（F-1/F-2/F-20/F-10/F-11）、101（B-1）、201（D-2）も並走

## このセッションで完了したこと（2026-04-24、2 回分）

### テイスト保持の仕組み（最優先 TODO）完了

- [docs/quality_checklist.md](../docs/quality_checklist.md) — 1 エントリ 5 分で通す機械的チェック（☆ マーク必須）
- [skills/write-entry.md](../skills/write-entry.md) — ID ＋ブリーフから 1 本書き上げる Step 0〜7 手順書
- [ledgers/stage2_briefs.md](stage2_briefs.md) — Stage 2 の 46 件ぶんの figure_type／主要出典／スコープ境界

### 用語統一

- 「どこで効くか」→「どこで役立つか」に全置換（AI 臭回避）。対象 14 ファイル

### 既存 10 件の品質チェック通過

- A-2 / B-2 / C-2 / D-12 / E-1 / F-50 / G-1 / H-53 / I-1 / J-14 すべて ☆ 項目合格
- YAML と `entries.csv` の `status` を `drafting` → `needs_review` に更新済み
- 旧 3 桁 ID サンプル 7 件（101/201/301–305）は旧テンプレ由来のため `sample` のまま据え置き（302 は著者欄に AI 記入が残っているので、新テンプレでの書き直し時に要クリア）

### 外出先コメント投入フロー（要件定義＋スキル＋受信箱）

- 要件定義：[docs/mobile_inbox_requirements.md](../docs/mobile_inbox_requirements.md)（Android ＋ Obsidian Mobile ＋ Obsidian Git）
- 取り込みスキル：[skills/import-comments.md](../skills/import-comments.md)
- 受信箱：`mobile_inbox/` と `mobile_inbox/processed/` のディレクトリと [README](../mobile_inbox/README.md) 作成

### 要確認事項の調査完了

- ✅ **D-14 Claude Mythos Preview**（限定公開、Project Glasswing 経由、一般提供なし）
- ✅ **B-19 Claude Cowork**（正式名確定、Enterprise プランに含まれる）
- ✅ **F-85 SuperClaude Framework**（"Supercell" は聞き違い。コミュニティ OSS、Anthropic 非公式）
- ✅ **料金プラン B-50〜52**（2026-04-24 時点の数値を取得済、B-50 に反映）
- ⚠️ **D-70 Amical**：実在確認できず。**Amica（semperai/amica）か Whisper の聞き違いの可能性高**。**著者に再確認要**
- ⚠️ **Cursor の "head F"**：公式確認できず。Cursor 独自モデルは `cursor-tab-3` と `Composer` のみ。D-35 のまま Composer 主軸でいく想定

### CLAUDE.md 更新

- §6 に「執筆／レビュー／取り込み」の手順書セクションを追加（quality_checklist / write-entry / import-comments / mobile_inbox_requirements への導線）

## 次セッションの TODO（優先順）

### 最優先：著者再確認 2 件

- **D-70 Amical**：Amica か Whisper かの聞き違い可能性を著者に問う。不明なら `D-70` はエントリ候補から一旦外す
- **Cursor の "head F" モデル**：`cursor-tab-3` のことか、`Composer` のことか、別物か。**回答次第で D-35 の扱いを決定**

### 最優先：ステージ 2 の執筆着手

[writing_priority.md](writing_priority.md) §ステージ 2 の 46 件を [stage2_briefs.md](stage2_briefs.md) と併読して進める。

- 手順は必ず [skills/write-entry.md](../skills/write-entry.md) に従う（Step 0 〜 7）
- 書くごとに：`entries.csv` の `status` を `candidate` → `drafting` → `needs_review` → `ready` と更新
- チェックリスト通過まで `needs_review`、著者の欄記入が済んで初めて `ready`

書き始める候補（stage2_briefs の並び順）：

1. **B-1 Gemini**（既存 101 の素材を参考にしつつ新テンプレで）
2. **B-3 ChatGPT**（H-53 と接続）
3. **C-1 OpenAI**（B-3 との流れで）
4. **D-11 Claude 3.5 系**（D-12 との接続）
5. **G-2 Token**（G-1 Context とセット）
6. **G-40 バイブコーディング**（本書の中心語彙、書ければ大きい）

### 並行：モバイル投入フローを Phase 1 で回す（著者本人のスマホ作業）

[docs/mobile_inbox_requirements.md](../docs/mobile_inbox_requirements.md) §9 Phase 1 に従う。

1. Android の Obsidian Mobile ＋ Obsidian Git に本リポジトリを vault として開く
2. `mobile_inbox/2026-04-24.md` を作って見出し規約どおりに 1〜2 件書く
3. 自動 push が効いているか確認。PC 側で `git pull` して届いているか確認
4. 回り始めたら `/import-comments` を一度走らせて、反映が正しいかを検証

Phase 1 が回ったら、必要に応じて import-comments の挙動調整（Phase 3）に進む。

### 保留事項

- **論文エントリの配置**（Transformer 論文等）：現 H-58 のまま、他の論文候補が揃ってから判断
- **タイムラインの細分化**：Claude 系・Gemini 系のマイナー版まで刻む作業は後回しで OK
- **旧 3 桁 ID の新テンプレ書き直し**：B-1 / D-2 / F-1 / F-2 / F-10 / F-11 / F-20 の 7 件。ステージ 2 の対応 ID（例：B-1 を書くときに 101 の素材を取り込む）と一体で進める
- **302_typescript の著者欄 AI 記入**：新テンプレで F-2 を書き直すときにクリアする

## スコープ外（やらない）

- **デザイン／誌面レイアウト／HTML モック／配色調整**は別担当。Claude Code では扱わない。
- 既存の `drafts/prototypes/mockups/` は参照用として残すだけ

## セッション再開時の最初の動き

1. このファイルを開く
2. [CLAUDE.md](../CLAUDE.md) §6 の手順書セクションに目を通す
3. 著者に D-70 Amical と Cursor "head F" の再確認を聞く（5 分で済む）
4. [stage2_briefs.md](stage2_briefs.md) から 1 件選び、[skills/write-entry.md](../skills/write-entry.md) Step 0 から執筆開始

## 直近コミット

- 2026-04-24 initial commit: VibeCodingDictionary の土台一式（62 ファイル）
- 2026-04-24 add CLAUDE.md and next_session_handoff for context handover
- 2026-04-24 add taste toolkit and mobile_inbox requirements, rename どこで効くか
- 2026-04-24 run checklist, research unresolved items, prepare stage2 briefs（このコミット）
