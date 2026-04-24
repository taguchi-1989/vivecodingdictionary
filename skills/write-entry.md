# スキル：エントリを 1 本書く（write-entry）

*ID と短いブリーフから、`spread_v1` テンプレに沿ったエントリを 1 本書き上げるための手順書です。AI（Claude）が読む前提で書いています。*

## このスキルの目的

バイブコーディング図鑑のエントリを、**テイスト（トーン・構造・語彙選び）を外さずに** 量産できる状態にすることです。335 件を書き切るまで、このスキルが手順の中心になります。

## 入力

以下のいずれかで呼び出されます。

- **フル指定**：ID ＋ title ＋ 短いブリーフ（書きたいことの骨子）
- **最小指定**：ID のみ（ブリーフは `ledgers/entry_candidates.md` から拾う）

## 出力

- `content/entries/{category}/{id}_{slug}.md` に新規ファイル 1 本
- 本文はテンプレ `templates/entry_template.md` の節順そのまま、著者記入欄は空スケルトン
- ドラフト完了時のステータスは `status: drafting`

## 手順

### Step 0. 前提ドキュメントを読む（毎回）

1. [CLAUDE.md](../CLAUDE.md) — プロジェクト全体の約束
2. [docs/book_philosophy.md](../docs/book_philosophy.md) — 根っこの思想と読者像
3. [docs/editorial_style.md](../docs/editorial_style.md) — トーン・文体の細則
4. [docs/quality_checklist.md](../docs/quality_checklist.md) — 書き終わり時に通すチェック
5. [templates/entry_template.md](../templates/entry_template.md) — 節の順番と各節の意味

既に同一セッションで読み込み済みなら Step 0 は省略可。ただし「前回から 10 本以上書いた」「セッション開始直後」なら必ず読み直す。

### Step 1. ID と配置先を決める

1. `ledgers/entry_candidates.md` で該当 ID の行を探し、候補メタ情報を確認
2. `ledgers/entries.csv` で重複・採番衝突がないか確認
3. 出力パスを決定：`content/entries/{category}/{id}_{slug}.md`
   - `category` は YAML の `category` と一致（`service` / `model` / `term` など）
   - `slug` は半角英小文字 + アンダースコア（例：`claude` / `chatgpt_launch` / `reading_guide`）

既存ファイルが置かれるフォルダ：

```
content/entries/
  common/       A セクション（序文・索引）
  service/      B（サービス）
  person/       C（人・会社）
  model/        D（モデル）
  benchmark/    E（ベンチマーク）
  term/         F（従来コード語彙）
  term_general/ J（AI 一般語彙）
  term_llm/     G（バイブ特有語彙）— 既存例は term に混在、新設はここ
  history/      H（進め方・歴史）
  mcp/          I（MCP）
  tool/         補助ツール
  workflow/     開発の流れ
```

### Step 2. ブリーフと分類を埋める（YAML）

テンプレの YAML を埋める。**埋めづらい項目があれば、まず `entry_candidates.md` とウェブ一次情報で事実確認** してから書く。推測で埋めてはならない。

埋めるときの判断基準：

- `experience_level`：著者が実際に使っているか（`hands_on`）、少し触った程度か（`partial`）、完全に調査ベースか（`research_only`）
- `reader_level`：Level 1〜2 は基礎語／用語紹介、Level 3〜4 は中核概念、Level 5〜6 は専門に寄る
- `figure_type`：書きたい図のタイプを先に決める（本文を書きながら図タイプを変えると齟齬が出る）
- `evaluation_date`：今日の日付。時変情報を含む場合は必須
- `related_terms`：3〜6 個。仮置きで書き、本文を書き終えた後で必ず見直す

### Step 3. 左ページを書く（v2 誌面）

順番厳守。**左ページ本文の合計は 175〜300 字が目安**（メイン図と Before/After が左ページの大半を占める）。超えたら Step 7 のチェックで削る。

1. **tagline**（**25〜40 字**、1〜2 文）：用語を言い切る。結論ファースト、です・ます調、カタカナは読み仮名。**旧「ひとことで」は本セクションに合流**
2. **何をしてくれるか**（**60〜100 字**、2 文）：役割と仕組みを具体的に。長いコードは貼らない
3. **どこで出会うか**（**70〜110 字**、2 文）：読者が実際にこの用語と出会う面（ツール・エディタ・会議・エラー表示）。旧「バイブコーディングでの位置づけ」の後継。**著者の個人的エピソードは「私のコメント」に回す**
4. **メイン図**：`figure_type` に応じた A / B / C のどれか 1 つだけ残す。「図の狙い」を 1〜2 文で添える
5. **関連用語**（3〜5 個、合計 20〜50 字）：誌面ではタグチップ表示。短い単語中心

### Step 4. 右ページを書く（v2 誌面）

**右ページ本文の合計は 200〜380 字が目安**（著者欄を除く）。

1. **この用語の見どころ（6 視点）**：1.役割 / 2.うれしさ / 3.注意点 / 4.どこで役立つか / 5.**はじめに** / 6.深掘り先。**各 1 文・20〜30 字目安**（合計 120〜200 字）
2. **開発フローでの位置（必須）**：4〜5 ステップ。**各 30〜40 字**「短ラベル — 1 行補足」形式。サービス／モデル／歴史でも省略不可

### Step 5. 著者記入欄は空スケルトンのまま残す

**絶対に AI は埋めない。** テンプレのコメント `<!-- AUTHOR: user_only / AI-ASSIST: no -->` が目印。

著者欄は v2 誌面で**右ページ下段に印刷**されるが、記入するのは著者本人のみ。AI は空スケルトンを用意するだけ。

- `非エンジニア視点のつまずき`：`-\n-\n-` のまま（3〜4 項目分の箇条書き空欄）
- `私のコメント`：`🙂 第一印象:` `👍 良い点:` `👎 ダメな点:` `👥 誰に向くか:` の 4 ラベルのみ（絵文字は `🎯` ではなく **`👥`**）

気を利かせて推測の「つまずき」を書くのも NG。これは著者の一次体験だけを入れる欄。

### Step 6. 裏台帳メモを埋める

1. **誌面ポンチ絵メモ**
   - メイン図の「描く内容」「登場人物」「吹き出し・心の声」「中央キーワード」を具体的に
   - **必ず人物と吹き出しを入れる**（プロジェクトメモリ「誌面図解は『人の視点』が主役」参照）
   - 6 視点アイコンは `共通アイコン流用` でよい（個別演出が要るときだけ具体化）
   - 開発フロー図の各ステップのアイコン・絵柄を書く
2. **コミュニティ補完メモ**：近接エントリとのスコープ分担を書く
3. **出典メモ**：`- ソース名 — checked YYYY-MM-DD` 形式。時変情報を含むなら必須
4. **備考**：時期差分・別会社サービス・例外ケースのメモ

### Step 7. チェックリストを通す

[docs/quality_checklist.md](../docs/quality_checklist.md) を上から下まで機械的に走らせる。

- `☆` がついた項目はすべて YES になるまで修正
- 全 YES になったら `ledgers/entries.csv` の `status` を `drafting` → `needs_review` に更新
- ファイルを保存し、次の ID へ

## 守ること（テイストの核）

書いている間、常に頭に置く原則。

- **です・ます調**：例外なし
- **結論から書く**：定義 → 補足の順
- **初出で日本語訳／略称展開**：`Context（コンテキスト）` `Claude Code（略称 CC）`
- **強い断定を避ける**：「最新」「最強」「完全」「絶対」を使わない。「ことがあります」で弱化
- **事実と主観を混ぜない**：主観は著者欄に逃がす（AI は触らない）
- **比喩は便利、仕様説明の代わりにしない**：太字は概念キーワードに限定
- **「人の視点」主役**：図の設計は必ず人物＋吹き出しを指示する
- **スコープを被らせない**：近接エントリとの住み分けを常に意識し、備考／コミュニティ補完メモに書き残す
- **字数目安を超えない**（v2 誌面）：左ページ本文 175〜300 字、右ページ本文 200〜380 字。超えたら重複・著者エピソード・他エントリ領域を優先して削る（checklist §H 参照）

## やらないこと

- **デザイン・誌面レイアウト・HTML・配色**：別担当。触らない（[CLAUDE.md](../CLAUDE.md) §5）
- **著者記入欄の先回り記入**：著者本人のみ
- **ID の付け替え・欠番詰め**：v0.5 で確定、動かさない（[docs/id_scheme.md](../docs/id_scheme.md)）
- **推測で埋める時変情報**：出典がないなら `status: needs_source` で止める

## 呼び出し例

```
# フル指定
write-entry B-1 Gemini
- 短いブリーフ：Google の汎用 AI アシスタント。Bard から改名。Gemini Pro / Flash / Nano のモデル階層。Google Workspace 統合、Android 標準化。
- reader_level: 2
- figure_type: structure
- experience_level: hands_on

# 最小指定
write-entry C-1
→ entry_candidates.md を見て OpenAI のブリーフを自分で拾ってから Step 0 へ
```

## 関連

- チェックリスト：[docs/quality_checklist.md](../docs/quality_checklist.md)
- 原則：[docs/quality_guidelines.md](../docs/quality_guidelines.md)
- トーン：[docs/editorial_style.md](../docs/editorial_style.md)
- テンプレ：[templates/entry_template.md](../templates/entry_template.md)
- 候補台帳：[ledgers/entry_candidates.md](../ledgers/entry_candidates.md)
- 優先度：[ledgers/writing_priority.md](../ledgers/writing_priority.md)

## 履歴

- v0.1（2026-04-24）: 初版。handoff「テイスト保持の仕組み作り」TODO に対応。サンプル 10 件からテイストを抽出して手順化。
- v0.2（2026-04-24）: 各セクションに字数目安を明記（左ページ本文 700〜800 字、右ページ本文 250〜400 字）。B-1 Gemini 実稼働で 40% 超過した反省を反映。
- v0.3（2026-04-24）: 誌面 v2 に追随。セクション改名（ひとことで → tagline 合流、バイブ位置づけ → どこで出会うか、最初に理解する範囲 → はじめに、🎯 → 👥）。字数目安を v2 実測値に大幅縮小（左 175-300、右 200-380）。
