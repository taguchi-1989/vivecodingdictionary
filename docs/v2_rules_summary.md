# v2 ルール総覧 — バイブコーディング図鑑 執筆・誌面の確定仕様

*2026-04-25 作成。iter 1-21 の反復で確定した**全ルールのサマリ**。執筆時の第一参照点・デザイン担当への引き渡し・新セッション開始時の前提確認に使う。*

**原典**:
[design_philosophy_v2.md](../drafts/prototypes/mockups/design_philosophy_v2.md) / [writing_spec.md](../drafts/prototypes/mockups/design_philosophy_v2/writing_spec.md) / [book_readiness_review.md](../drafts/prototypes/mockups/design_philosophy_v2/book_readiness_review.md) / [check_entry.py](../drafts/prototypes/mockups/design_philosophy_v2/check_entry.py)

---

## 0. 書くときの 1 分チェック

新しいエントリに取り掛かる前に、以下を順に確認:

- [ ] 文体は **ですます調**（必須）
- [ ] `templates/entry_template.md` をコピーして開いている
- [ ] タイトルと tagline は**重複していない**（`{{title}} は、…` で始めない）
- [ ] `## ひとことで` は**書かない**（tagline で代替される）
- [ ] `## どこで出会うか` は名前どおり（旧「バイブコーディングでの位置づけ」は NG）
- [ ] 6 視点 ④ は「どこで役立つか」、⑤ は「はじめに」（旧「どこで効くか」「最初に理解する範囲」は NG）
- [ ] 「誰向けか」（「誰に向くか」ではない）
- [ ] 著者記入欄「非エンジニアのつまずき」「私のコメント」は AI は触らない
- [ ] 書き終わったら `python drafts/prototypes/mockups/design_philosophy_v2/check_entry.py path/to/entry.md` で検証

---

## 1. 紙面の構造（見開き 2 ページ）

### 左ページ

1. 上チロム: book icon + 章ラベル（例「技術用語」）＋ページ番号
2. **タイトル** — 96px ネイビー
3. **タグライン青帯** — 25〜45 字、淡青塗り、タイトルの言い換えではなく**一歩先の定義**
4. **タグ行**: 体験区分 ／ 推奨読者レベル（青枠ピル ×2）
5. **本文セクション 2 つ**（「ひとことで」は削除済み）
   - 何をしてくれるか（60〜200 字）
   - どこで出会うか（60〜200 字）
6. **Before/After 図** または概念図
7. **擬人化ポンチ絵スロット**（30〜80 字の caption、青 dashed 枠）
8. **関連用語**（3〜5 個のピル）
9. 下チロム: 左 `YYYY.MM · Draft` ／ 右 `（会話での使い方例）`

### 右ページ

1. 上チロム: book icon + `{{title}} の見方` ラベル＋ページ番号
2. **タイトル** — `{{title}} をどう読むか` 50px ネイビー
3. **この用語の見どころ**（6 視点グリッド）
   - 役割 ／ うれしさ ／ 注意点 ／ どこで役立つか ／ **はじめに** ／ 深掘り先
4. **2 カラム下段**（比率 **4 : 6**、右のコメントが広い）
   - 左: 非エンジニアのつまずき（3 項目、青ドット）
   - 右: 私のコメント（4 項目固定、first/good/bad/who）
5. **開発フローでの位置**（4 ステップ横並び）
6. **参考 URL**（1 本 + checked YYYY-MM-DD）
7. 下チロム: 左 `F-01 · language` ／ 右 `📖 バイブコーディング図鑑`

---

## 2. 文字数と書くものの原則

### 左ページ本文

| 箇所 | 文字数 | 注意 |
|---|---|---|
| tagline | **25〜45** | 推奨 30〜38、名詞止め可 |
| 何をしてくれるか | **60〜200** | 2〜4 文、ですます必須 |
| どこで出会うか | **60〜200** | 2〜4 文、ですます必須、具体シーン |
| 関連用語 | **3〜5 個** | 1〜10 字の用語名 |
| ポンチ絵 caption | **30〜80** | 1 シーンに絞る |

### 6 視点（右ページ）

| # | 節名 | 文字数 | アイコン |
|---|---|---|---|
| 1 | 役割 | 15〜40 | 的 ＋ 十字（bullseye with crosshair） |
| 2 | うれしさ | 15〜40 | ハート |
| 3 | 注意点 | 15〜40 | 警告三角 |
| 4 | どこで役立つか | 15〜40 | 電球 |
| 5 | はじめに | 15〜40 | 双葉の芽（Lucide sprout） |
| 6 | 深掘り先 | 15〜50 | 文書 + 虫眼鏡（file-search） |

### 著者記入欄

| 節 | 項目数 | 項目あたり | 記法 |
|---|---|---|---|
| 非エンジニアのつまずき | **3 項目** | 15〜30 字 | 青ドット、事実寄り |
| 私のコメント | **4 項目固定** | 10〜40 字 | first/good/bad/who、バッジ ★/✓/!/☺ に変換 |

---

## 3. 文体ルール

- **です・ます調 必須**（CLAUDE.md 準拠）
- 結論から書く
- 読者を馬鹿にしない、強い断定を避ける、煽らない
- 絵文字は **私のコメント** の 4 種（★/✓/!/☺）以外 使わない
- tagline は title の言い換えでなく**一歩先の定義**
- 箇条書き連発・言い換え連続を避ける

## 4. ビジュアル・トークン（CSS 側の確定値）

ページ寸法: 750 × **1061 px**（ISO A/B 系 √2 準拠）

### カラー

| 用途 | 変数 | 値 |
|---|---|---|
| メイン青 | `--ink-blue` | #2F7BE6 |
| ネイビー（タイトル） | `--ink-blue-900` | #123E82 |
| 濃青（見出し文字） | `--ink-blue-700` | #1E5FBC |
| 淡青（タグライン塗り） | `--ink-blue-100` | #D6E4F8 |
| ごく淡青（背景） | `--ink-blue-50` | #EAF1FB |
| 墨（本文） | `--ink` | #1A1A1A |
| 墨-中 | `--ink-2` | #4A5568 |
| 紙 | `--paper` | #FFFFFF |
| 紙-2（淡グレー） | `--paper-2` | #F3F6FB |

**ルール**: 3 色以上は使わない。青単色＋墨＋白＋淡青のみ。

### 書体

- 和文: **Zen Maru Gothic**（Light/Regular/Medium/Bold/Black）
- 英数: **Inter**
- 和文 `font-feature-settings: "palt"` 適用

### 主要サイズ（iter 20 確定）

| 箇所 | サイズ |
|---|---|
| 左ページタイトル | 96px 900 ネイビー |
| 右ページタイトル | 50px 900 ネイビー |
| 本文 | 16px, line-height 1.8 |
| 本文見出し（ひとことで等） | 17px 700 濃青 |
| セクションラベル（青バー付） | 20px 900 墨 |
| タグライン帯 | 18px 700 |
| 体験区分タグ | 16px 700 |
| 6 視点タイトル | 20px 900 |
| 6 視点本文 | 14.5px, line-height 1.7 |
| つまずき／コメント | 14.5px |
| フローラベル | 14px 700 |
| 関連用語ピル | 15px |
| 参考 URL | 12.5px Inter |

### レイアウト

- ページ body padding: **40px / 44px / 100px**（top / horizontal / bottom）
- **ノド非対称**: 左ページの右 padding ＋14px、右ページの左 padding ＋14px（綴じ側を広く）
- 左青バー: 5×22px、ラベルとの gap 12px
- 6 視点セル: 縦スタック配置（番号バッジ枠内左上・アイコン 52px 中央・タイトル中央・本文中央）
- Before/After: 親カード（角丸 12px・青枠 1.5px）＋ 子カード（角丸 8px・淡青塗り）の 2 層
- フッター: 左右非対称（左ページ・右ページでラベル構成を変える）
- 2 カラム下段: **4 : 6**（つまずき : コメント）

---

## 5. 削除・リネーム履歴（既存エントリの旧名を検出した場合）

| 旧 | 新 | 世代 |
|---|---|---|
| `## ひとことで` | **削除**（tagline で代替） | iter 7 |
| `## バイブコーディングでの位置づけ` | `## どこで出会うか` | iter 5 |
| `### 4. どこで効くか` | `### 4. どこで役立つか`（iter 5 で変更したが iter 10 で戻した） | iter 10 |
| `### 5. 最初に理解する範囲` | `### 5. はじめに` | iter 6 |
| `## 非エンジニア視点のつまずき` | `## 非エンジニアのつまずき` | 2026-04-25 |
| 誰に向くか | **誰向けか** | 2026-04-25 |

右ページサブタイトル「定義だけでなく、役割・つまずき・実務上の意味をセットで見ると…」は**各エントリから削除**（iter 8）。`A-2 この本の読み方` に集約。

---

## 6. 自動チェッカーの使い方

執筆後:

```bash
python drafts/prototypes/mockups/design_philosophy_v2/check_entry.py path/to/entry.md
```

全件監査:

```bash
python drafts/prototypes/mockups/design_philosophy_v2/check_entry.py --dir content/entries/
```

チェック項目:
- YAML 必須キー（id / title / category / figure_type / page_layout / evaluation_date）
- 必須節の存在
- 各節の文字数レンジ
- ですます語尾（本文節）
- tagline が title の言い換えでない
- 関連用語 3〜5 個
- 旧節名の互換警告

`status: archived` のエントリは検証対象外（参照素材として凍結）。

---

## 7. 書籍化に向けて残っている課題

詳細は [book_readiness_review.md](../drafts/prototypes/mockups/design_philosophy_v2/book_readiness_review.md)。要点のみ:

- ✅ 縦横比 1:1.4142（ISO A 系）準拠
- ✅ ノド非対称 margin
- ☐ bleed 3〜5mm（印刷用 PDF 生成時）
- ☐ CMYK 色校正（実刷り前必須）
- ☐ 実イラスト／写真の差し込み（ポンチ絵スロット・擬人化）
- ☐ 章ごとの視覚的変化点（335 entry 同型の単調さ緩和）
- ☐ フォント埋め込み確認（SIL OFL の Zen Maru Gothic）

---

## 8. ファイル位置

| 用途 | パス |
|---|---|
| テンプレ（新規執筆時にコピー） | `templates/entry_template.md` |
| エントリ本体 | `content/entries/**/{letter}-{num}_name.md` |
| プロトタイプ HTML | `drafts/prototypes/mockups/design_philosophy_v2/typescript_spread.html` |
| 追加 CSS primitive | `drafts/prototypes/mockups/design_philosophy_v2/overlay.css` |
| 完全仕様（設計思想） | `drafts/prototypes/mockups/design_philosophy_v2.md` |
| 文字数・原則の細則 | `drafts/prototypes/mockups/design_philosophy_v2/writing_spec.md` |
| 自動チェッカー | `drafts/prototypes/mockups/design_philosophy_v2/check_entry.py` |
| 書籍化レビュー | `drafts/prototypes/mockups/design_philosophy_v2/book_readiness_review.md` |
| 反復スクショ（iter 1-21） | `drafts/prototypes/mockups/design_philosophy_v2/screenshots/` |
| 旧トーン・品質原則 | `docs/editorial_style.md` / `docs/quality_checklist.md` / `docs/quality_guidelines.md` |
| 本書コンセプト | `docs/book_philosophy.md` |
| 本ドキュメント | `docs/v2_rules_summary.md` |

---

## 9. このドキュメントと既存 docs の関係

- `docs/editorial_style.md` — 文体の**原則**（変更なし、本ドキュメントから参照）
- `docs/quality_checklist.md` — 1 エントリ 5 分の**目視**チェック（変更なし）
- `docs/quality_guidelines.md` — 品質の**観点**（変更なし）
- **本ドキュメント** — iter 16-21 で確定した**節単位の具体値・紙面構成・リネーム履歴**を 1 箇所に集約

新規セッション開始時は、本ドキュメントを最初に読む → 必要なら個別仕様に降りる、で前提が揃う。
