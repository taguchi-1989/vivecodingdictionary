# 前付け（A 章）の例外レイアウト仕様

*2026-05-13 起票。A 章（A-1〜A-11）は本書の前付けで、用語エントリ用の `spread_v1` テンプレでは内容が空転します。前付け部分だけ独自のレイアウトを許容する例外仕様をここに集約します。本書本体（B〜J 章）の `spread_v1` には影響しません。*

**原典への接続**: [docs/v2_rules_summary.md](v2_rules_summary.md) §1〜2 の `spread_v1` を「本編の標準」として温存し、本書冒頭の 7 見開きだけが本仕様で動きます。

## 1. なぜ例外にするのか

A 章は辞書本体ではなく、**読者が本編に入る前に渡す「使い方」と「凡例」**です。`spread_v1` の以下の節は前付けでは意味が立ちません。

- `tagline` 青帯（用語の言い換えではなく一歩先の定義）
- 「どこで出会うか」（前付けに「出会う」場面はない）
- 6 視点（役割／うれしさ／注意点／…）
- 「開発フローでの位置」（メタ情報に開発フローはない）

スケルトンを `spread_v1` で埋めてきたため、現状の A-1〜A-11 は無理やり書かれた節が並んでいます。前付けを「ビジュアル先行・節構造自由」にすることで、本来の役割（読み方・凡例・索引）に戻します。

## 2. 構成（重め 7 見開き）

A-1〜A-11 の 11 エントリを、扉 1 ＋ 本付け 6 の **7 見開き** に再編成します。ID は維持し、複数 ID を 1 見開きに同居させるときは `spread_group` フィールドで束ねます。

| # | 構成 ID | 見開き名 | layout 名 |
| :-: | :-- | :-- | :-- |
| 0 | （新規・無番） | 扉「知らないことばで、止まらない。」 | `front_concept_spread` |
| 1 | A-1 | まえがき | `front_essay` |
| 2 | A-2 | 見開きの読み方（分解図） | `front_anatomy` |
| 3 | A-3 + A-9 | 図鑑の歩き方と索引 | `front_map_index` |
| 4 | A-4 + A-5 + A-6 | この本の注意マーク（凡例） | `front_legend_marks` |
| 5 | A-7 + A-8 | 図と色の見本帳 | `front_swatch` |
| 6 | A-10 + A-11 | 更新履歴と略称 | `front_log_glossary` |

## 3. 各見開きの設計

各見開きは「左右ページの主役」を 1 つに絞り、残りは余白と装飾で支えます。文字量は `spread_v1` より一段軽い前提（左右合計 200〜350 字程度）です。

### 0. 扉  `front_concept_spread`

**主役**: 1 枚絵で「知らないことばで止まる → 引く → 戻る」を見せる。

- 左ページ: 「知らないことばで、止まらないために。」のコピー＋抽象人物のイラスト 3 コマ（困る／引く／戻る）
- 右ページ: 「1 項目は見開き 2 ページ。左でつかみ、右で使う。」のコピー＋見開きミニチュア（実際の `spread_v1` の縮小サムネを置き、6 つの場所を矢印で指す）
- 既存資産: [assets/opening/opening-spread-concept.png](../assets/opening/opening-spread-concept.png) を出発点に使えます
- 文字量目安: 左 80〜120 字／右 80〜120 字。タイトル無し、ページ番号無し、章ラベル無し

### 1. A-1 まえがき  `front_essay`

**主役**: 著者の声で書く巻頭言。

- 左ページ全面: 大判の「ことばの橋」イラスト 1 枚＋短いリード文（30〜50 字）
- 右ページ: 縦組み風の本文 2 段（合計 350〜500 字）。「同じ日本語を話していても、同じ言語空間にいるとは限りません。」を冒頭に据える
- 既存テンプレの 6 視点・開発フロー・関連用語・つまずき・私のコメントは**置かない**
- 著者欄（私のコメント）も置かない。前付けは著者ボイスそのものなので、別欄にする必要が無いため

### 2. A-2 見開きの読み方（分解図）  `front_anatomy`

**主役**: 本編 1 エントリの実物見開きの注釈図。

- 見開き全面に **実物大の `spread_v1` 1 枚を半透明で敷き**、コールアウト矢印で各部位を指す
- 指す対象: タイトル ／ 読み ／ tagline 青帯 ／ 何をしてくれるか ／ どこで出会うか ／ メイン図 ／ ポンチ絵 ／ 会話での使い方例 ／ 6 視点 ／ 開発フロー ／ 関連用語 ／ 著者欄（つまずき・私のコメント）／ 参考 URL
- コールアウトは 1 件 20〜40 字以内
- 注釈の「下地」サンプルには TypeScript（F-2 など実書済みの定番エントリ）を使うと、本書のトーンが伝わります

### 3. A-3 + A-9 図鑑の歩き方と索引  `front_map_index`

**主役**: A〜J の地図と索引の入口。

- 左ページ: A〜J を円環または横並びの地図にして、章ごとのテーマラベルを置く。読者レベル別の推奨ルート 3 本（Lv1 はここから／Lv3 はここから／Lv5 はここから）を色違いの線で重ねる
- 右ページ: 索引の見出しと使い方。letter 順 ／ 五十音順 の 2 系統があることを示し、どちらをいつ使うかを 1 文ずつ。索引本体は巻末別ページ
- A-3 と A-9 の本文は短く要約（合計 300〜450 字）。`spread_group: front_03_map_index` で束ねる

### 4. A-4 + A-5 + A-6 注意マーク（凡例）  `front_legend_marks`

**主役**: 各エントリに付くマーク／タグ／日付の見方をまとめて 1 見開きに。

- 左ページ: 「体験区分」（A-4）と「読者レベル」（A-5）のタグ凡例。アイコン＋短い説明を 2 行ずつ
  - 体験区分: `hands_on` / `partial` / `research_only`
  - 読者レベル: 1〜6 を縦の階段で表現し、各段に「読める語の例」を 2〜3 個
- 右ページ: 「評価日・時変情報」（A-6）の凡例。`evaluation_date` ／ `version_status` ／ `pricing_note` がなぜ要るかを 1 ブロック（80〜120 字）＋例示
- 3 つの A エントリの本文は各 80〜120 字に圧縮。`spread_group: front_04_legend_marks`

### 5. A-7 + A-8 図と色の見本帳  `front_swatch`

**主役**: 本書で使う図のタイプとカラー／記号の物理サンプル。

- 左ページ: 「図のタイプ」（A-7）のカタログ。`structure` / `timeline` / `comparison` / `before_after` / `workflow` のミニサムネ 5 枚を 2 段グリッドで並べ、各 1 行で「いつ使う図か」
- 右ページ: 「色・記号」（A-8）のスウォッチ。
  - 青のトーン（タグライン帯・dashed 枠・参考 URL リンク）
  - ☆ 違反 ／ ⚠ 警告のバッジ
  - 私のコメントの 4 種（★/✓/!/☺）と意味
  - 関連用語ピル、6 視点アイコン
- 装飾より「実物が並んでいる」ことが大事。文字は最小限（合計 250〜350 字）。`spread_group: front_05_swatch`

### 6. A-10 + A-11 更新履歴と略称  `front_log_glossary`

**主役**: 機能的な前付け（リファレンス）。

- 左ページ: 「更新履歴」（A-10）。横向きタイムライン。`evaluation_date` の運用と「次に何が変わる予定か」枠
- 右ページ: 「略称表記」（A-11）。略称 ／ 正式名称 ／ 読み ／ 初出ページ の 4 列表。CC＝Claude Code、MCP＝Model Context Protocol、a11y＝accessibility 等
- 文字装飾は最小、表とタイムラインのレイアウトが主役。`spread_group: front_06_log_glossary`

## 4. YAML への影響

### 4-1. 既存キー

- `page_layout` の取りうる値を `spread_v1` の他に **`front_concept_spread` / `front_essay` / `front_anatomy` / `front_map_index` / `front_legend_marks` / `front_swatch` / `front_log_glossary`** の 7 種を追加で許容します
- 該当する A-1〜A-11 の YAML をそれぞれ書き換えます

### 4-2. 新設キー `spread_group`

複数エントリを 1 見開きに同居させるため、以下の任意フィールドを導入します。

```yaml
spread_group: front_03_map_index  # 同じ値を持つエントリは同居して 1 見開きを構成する
spread_position: left              # left / right / full （見開きでの担当面）
```

- 単独で 1 見開きを占めるエントリ（A-1 まえがき）には付けません
- `entries.csv` には影響しません。ledger の 339 件カウントも維持されます

### 4-3. 扉エントリの扱い

扉見開きは **ID を持たない前付け** として、`content/entries/common/` ではなく **`content/frontmatter/`** に置きます（既に空ディレクトリがある）。

- ファイル: `content/frontmatter/00_concept_spread.md`
- YAML: `id` は持たず、`page_layout: front_concept_spread`、`status: drafting` から開始
- validator はこのディレクトリを別ルールで読みます（次節）

## 5. validator・generator への影響メモ

このセクションは別タスク。仕様確定後にスクリプト側を改修します。

- [scripts/validate_entry.py](../scripts/validate_entry.py) L252: `page_layout != "spread_v1"` で警告している箇所を、`front_*` 系を許容するように拡張
- 前付け 7 見開きは `spread_v1` の節構造チェック（tagline 帯／何を／どこで／6 視点／開発フロー／関連用語／著者欄）を**スキップ**する。`page_layout` の値で分岐
- `content/frontmatter/**/*.md` も Edit/Write hook の対象にする
- 自動昇格（drafting → needs_review）は `front_*` でも有効にする
- [scripts/update_review_queue.py](../scripts/update_review_queue.py) は 7 見開きを「前付け」セクションとして集計

## 6. 残作業（このスレッドの外でやること）

優先順:

1. **本仕様の合意** — 構成・layout 名・spread_group のキー名を確定（このドキュメント）
2. **扉エントリの新規執筆** — `content/frontmatter/00_concept_spread.md` を書く
3. **A-1〜A-11 の各 YAML 更新** — `page_layout` 差し替え＋必要箇所に `spread_group` / `spread_position` 追加
4. **A-1〜A-11 の本文整理** — 各見開きの設計（§3）に合わせて節を入れ替え。`spread_v1` 用に書かれた tagline・6 視点・開発フローは前付け版では削るか転用
5. **validator 改修** — §5 の通り
6. **デザイン担当への引き渡し** — 7 見開きぶんのレイアウト指示書（本ドキュメント §3 がベース）。本編 `spread_v1` とは別系の HTML/CSS が要る

## 7. 開いておくべき関連ファイル

- [drafts/opening_spread_brief.md](../drafts/opening_spread_brief.md) — 扉見開きの最初のブリーフ。本仕様の §3-0 はここを継承
- [drafts/opening/opening-spread-annotated.html](../drafts/opening/opening-spread-annotated.html) — 扉見開きの注釈版モック
- [assets/opening/opening-spread-concept.png](../assets/opening/opening-spread-concept.png) — 扉のコンセプト画像
- [content/entries/common/A-*.md](../content/entries/common/) — 既存 11 エントリ。本仕様で再編成対象
- [docs/v2_rules_summary.md](v2_rules_summary.md) — 本編 `spread_v1` の確定仕様（こちらは触らない）
