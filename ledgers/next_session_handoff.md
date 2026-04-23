# 次セッションへの引き継ぎ（2026-04-24）

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

## 次セッションの TODO（優先順）

### 最優先：テイスト保持の仕組み作り（着手前）

執筆を大量に進める前に、**テイスト（トーン・構造・語彙選び）を外さないための補助**を整える。以下のいずれか、または組合せ：

1. **エントリ執筆専用のスキル／サブエージェント定義**
   - 例：`skills/write-entry.md` を作り、spread_v1 の節順・です・ます調・著者記入欄スケルトンを必ず守る手順を記述
   - エントリ 1 本書く → レビューパス → 修正、を一連の skill として固める
2. **雛形出力プロンプトのテンプレ化**
   - 「ID と短いブリーフ」だけ渡すと、spread_v1 構造で一気にドラフトが出るプロンプト雛形を用意
3. **レビュー用のチェックリスト**
   - 1 エントリ書き終わった後、機械的に通すトーン＆構造チェックリスト（「です・ます調？」「著者記入欄空？」「カタカナ初出で訳あり？」等）

**判断の種**：1 と 3 を併用するのが手堅い。2 は時間があれば足す。

### 次：執筆をスケールさせる

テイスト保持の仕組みが動き出したら、[writing_priority.md](writing_priority.md) のステージ 2 へ入る。

- ステージ 2 対象（約 40 件）：核となる基礎語彙。B-1 Gemini / B-3 ChatGPT / C-1 OpenAI / D-11 Claude 3.5 系 / F-3 Python / F-10 React など。
- **書くたびに**：`entries.csv` の `status` を `drafting` → `needs_review` → `ready` と更新する

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
3. 上記「最優先 TODO」からスタート（テイスト保持の仕組み作り）
4. 仕組みが動いたらステージ 2 の執筆へ

## 直近コミット

- 2026-04-24 initial commit: VibeCodingDictionary の土台一式（62 ファイル）
