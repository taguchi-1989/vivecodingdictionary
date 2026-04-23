# 次セッションへの引き継ぎ（2026-04-24 更新）

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

## このセッションで完了したこと（2026-04-24）

- **テイスト保持の仕組み作り（最優先 TODO）が完了**
  - [docs/quality_checklist.md](../docs/quality_checklist.md) を新設（1 エントリ 5 分で通す機械的チェック）
  - [skills/write-entry.md](../skills/write-entry.md) を新設（ID ＋ブリーフから 1 本書き上げる手順書）
- **用語修正**：「どこで効くか」→「どこで役立つか」に全置換（AI っぽい言い回しを回避）。対象 14 ファイル（テンプレ／チェックリスト／スキル／既存エントリ 11 件）
- **外出先コメント投入フローの要件定義**：[docs/mobile_inbox_requirements.md](../docs/mobile_inbox_requirements.md) を新設
  - Android ＋ Obsidian Mobile ＋ Obsidian Git で vault として本リポジトリを開く構成
  - `mobile_inbox/YYYY-MM-DD.md` に H2 見出し規約で書き込む
  - PC 側は `/import-comments`（未実装）で `content/entries/**/*.md` の著者欄・備考欄に反映

## 次セッションの TODO（優先順）

### 最優先：既存 10 件に新チェックリストを通す

- 対象：A-2 / B-2 / C-2 / D-12 / E-1 / F-50 / G-1 / H-53 / I-1 / J-14（＋ 旧 3 桁 ID の 301〜305 / 101 / 201）
- [docs/quality_checklist.md](../docs/quality_checklist.md) を上から走らせ、☆ 項目が全 YES なら `entries.csv` の `status` を `drafting` → `needs_review` に更新
- これで仕組み単体のテストも兼ねる

### 次：執筆をスケールさせる（ステージ 2）

[writing_priority.md](writing_priority.md) のステージ 2 へ入る。

- 手順は必ず [skills/write-entry.md](../skills/write-entry.md) に従う（Step 0 〜 7）
- ステージ 2 対象（約 40 件）：核となる基礎語彙。B-1 Gemini / B-3 ChatGPT / C-1 OpenAI / D-11 Claude 3.5 系 / F-3 Python / F-10 React など
- **書くたびに**：`entries.csv` の `status` を `drafting` → `needs_review` → `ready` と更新する

### 並行：モバイル・コメント投入フローを Phase 1 で回す

[docs/mobile_inbox_requirements.md](../docs/mobile_inbox_requirements.md) §9 に従い、最小セットで一度動かす。

1. Android に Obsidian Mobile と Obsidian Git を入れ、本リポジトリを vault として開く
2. `mobile_inbox/2026-04-24.md` を試しに作って 1〜2 件書く → 自動 push が効くか確認
3. PC で `git pull` してファイルが届いているかチェック
4. Phase 1 が回ったら `skills/import-comments.md` の作成（Phase 2）に進む

上記 1〜3 は著者本人のスマホ作業、4 は Claude Code で実装。

### 要確認の解消

- **Claude Mitos モデル（D-14）** — 正式名称・公式モデルか通称か
- **Amical（D-70）** — ローカル音声認識モデルの正式綴り
- **Claude Cowork（B-19）** — 公式名・機能範囲
- **Supercell（F-85）** — ターミナル系の正式綴り
- **Cursor の head F モデル** — D-35 に包含でよいか別扱いか
- **料金プラン（B-50〜52）** — 2026-05 時点の想定値、公開直前に要再確認

### 保留事項

- **論文エントリの配置**（Transformer 論文等）：現 H-58 のまま、他の論文候補が揃ってから判断
- **タイムラインの細分化**：Claude 系・Gemini 系のマイナー版まで刻む作業は後回しで OK

## スコープ外（やらない）

- **デザイン／誌面レイアウト／HTML モック／配色調整**は別担当。Claude Code では扱わない。
- 既存の `drafts/prototypes/mockups/` は参照用として残すだけ

## セッション再開時の最初の動き

1. このファイルを開く
2. [CLAUDE.md](../CLAUDE.md) でプロジェクト全体のテイストと構造を再確認
3. [docs/quality_checklist.md](../docs/quality_checklist.md) と [skills/write-entry.md](../skills/write-entry.md) に目を通す（今セッションで新設）
4. 上記「最優先 TODO」からスタート（既存 10 件にチェックリストを通す）
5. それが終わったらステージ 2 の執筆へ

## 直近コミット

- 2026-04-24 initial commit: VibeCodingDictionary の土台一式（62 ファイル）
- 2026-04-24 テイスト保持の仕組み（quality_checklist / write-entry）＋ mobile_inbox 要件定義（未コミット、必要なら次セッションで）
