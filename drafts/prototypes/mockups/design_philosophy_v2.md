# Design Philosophy v2 — 正式版（iter 16）

*2026-04-24 iter 16 確定。Claude.ai/design が吐いた TypeScript 見開きサンプル p.04-05 をゴール画像として、HTML で 16 世代回したうえでユーザー判断を反映した**正式仕様**。*

**関連成果物:**
- 実物プロトタイプ: [typescript_spread.html](design_philosophy_v2/typescript_spread.html)
- スタイル overlay: [overlay.css](design_philosophy_v2/overlay.css)
- 最終スクショ: [screenshots/iter16.png](design_philosophy_v2/screenshots/iter16.png)
- 書籍化レビュー: [design_philosophy_v2/book_readiness_review.md](design_philosophy_v2/book_readiness_review.md)
- 執筆仕様（文字数・原則）: [design_philosophy_v2/writing_spec.md](design_philosophy_v2/writing_spec.md)
- 自動チェッカー: [design_philosophy_v2/check_entry.py](design_philosophy_v2/check_entry.py)

> **スコープ注記**: CLAUDE.md では誌面レイアウト・HTML/CSS は「別担当」としている。本ドキュメントは**計画と引き渡し仕様**。iter 16 時点のプロトタイプ（static HTML）は存在するが、本採用時は別担当が React/Vue コンポーネントへ移植する想定。
>
> **観察の制限**: Claude は画像は目視できるが、現行 Design System 側の HTML を直接レンダリングせずコードから推定した差分ぶんは、iter 1-16 のスクショで実測に置き換え済み。

---

## 1. 設計思想（ゴール画像から抽出＋9 世代で調整）

1. **静寂の青白紙**。色は青（ネイビー `#123E82` ／メイン `#2F7BE6` ／淡青 `#D6E4F8` / `#EAF1FB`）、墨、白以外は出さない。
2. **タイトルは墨色ではなくネイビー（`--ink-blue-900 = #123E82`）**。純黒（`#1A1A1A`）は「しんどい」というユーザー判断（iter 7）。純ブルー（`#2F7BE6`）は目立ちすぎる。両者の間のネイビーに落ち着いた。
3. **左青バーが情報階層の背骨**。セクションラベル全てに 5×22px の青縦バー＋ラベル（18px / weight 900）。ページ全体の律動を作る最重要プリミティブ。
4. **丸みと鋭さの二声**。和文は Zen Maru Gothic、数字・英字は Inter。
5. **アイコンは第二の言語**。本文セクション冒頭の丸枠アイコン（44px 径）、6 視点タイル右上のアウトラインアイコン（**40px**、iter 9 で 34→40px に引き上げ）、フロー図の箱内アイコン（28px）。**全セクションに視覚的な取っ手**。
6. **見出しは一呼吸置く、続きはすぐ置く**。セクション間 44px、見出しから本文 14px。
7. **本文は 1.75 行**。
8. **ピルとバッジの使い分け**。ピル＝アウトライン丸角矩形（カテゴリ・タグ・関連用語）、バッジ＝塗り円＋白抜き数字／アイコン（6 視点の 1-6、本文冒頭アイコン円）。
9. **図は囲みの中に囲み**。Before/After は親カード（角丸 12px・青枠 1.5px）＋子カード（角丸 8px・淡青塗り）の二層。
10. **重複は刈る**。タグライン帯と「ひとことで」本文が同義反復→「ひとことで」本文セクションは削除（iter 7）。右ページの「定義だけでなく…」サブタイトルは毎ページ繰り返しになる→前付け「この図鑑の読み方」に集約、個別エントリからは削除（iter 8）。

---

## 2. 確定トークン（overlay.css で追加する primitive）

現行 `colors_and_type.css` の `--ink-blue-*` / `--paper-*` / `--ink-*` / `--sp-*` / `--radius-*` / `--font-jp` / `--font-en` はそのまま流用。

### 2-1. タイトル

```css
/* specificity: base.css の .vbcd h1 (0,1,1) に勝つため h1.title-hero */
.vbcd h1.title-hero {
  font-size: 96px;  font-weight: 900;
  color: var(--ink-blue-900);  /* #123E82 ネイビー */
  letter-spacing: -0.02em;  line-height: 1.02;  margin: 0 0 22px;
}
.vbcd h1.title-hero--right {
  font-size: 50px;  letter-spacing: -0.01em;  line-height: 1.1;
}
```

**重要**: base.css の `.vbcd h1` が `font-size: 40px; color: var(--fg)` を指定しており、シングルクラス `.title-hero` では specificity 負け。**必ず `h1.title-hero` の複合セレクタ**で書くこと。iter 2-4 でこの罠にはまって 3 世代無駄にした。

### 2-1.5. タイトル読みスロット（2026-04-28 追加）

```css
/* タイトル直下に小さく置く読み・日本語展開スロット。YAML title_reading から流す */
.vbcd .title-reading {
  font-family: var(--font-jp);
  font-weight: 500;
  font-size: 14px;
  color: var(--ink-2);
  letter-spacing: 0.04em;
  line-height: 1.4;
  margin: -16px 0 18px;  /* 96px タイトルの直下に詰める */
}
.vbcd .title-reading:empty { display: none; }
```

**役割**: タイトルが英字略称・固有名で、読みが一意でない／日本語展開を併記したい語に対して、タイトル直下に小さく置く独立スロット。誌面例:

```html
<h1 class="title-hero">git</h1>
<div class="title-reading">ギット</div>
<div class="tagline-bar">…</div>
```

**運用**: YAML `title_reading` フィールドが空または欠落のときは空文字 → `:empty` セレクタで非表示にする。タイトル文字列の中に `Context（コンテキスト）` のような括弧書き読みを置くのは廃止（誌面で 96px のヒーロー枠に括弧が大きく出すぎ、視覚階層を崩すため）。

### 2-2. タグライン帯

```css
.tagline-bar {
  display: inline-block;
  padding: 14px 22px;
  background: var(--ink-blue-100);  /* #D6E4F8 */
  color: var(--ink);
  border-radius: var(--radius-lg);  /* 12px */
  font-weight: 700;  font-size: 16px;  line-height: 1.5;
  margin-bottom: 24px;
}
```

### 2-3. 体験区分・推奨読者レベル タグ（iter 8 で太化）

```css
.tag-row { display: flex; gap: 14px; margin-bottom: 32px; }
.tag-chip {
  display: inline-flex; align-items: center; gap: 10px;
  padding: 12px 20px;
  border: 1.5px solid var(--ink-blue);
  border-radius: var(--radius);
  font-size: 15px; font-weight: 700; color: var(--ink);
}
.tag-chip svg { width: 20px; height: 20px; color: var(--ink-blue); }
```

### 2-4. 本文セクション（ひとことで削除後、2 セクション構成）

```css
.body-section {
  display: flex; gap: 18px; padding: 20px 0;
  border-bottom: 1px dotted var(--rule-strong);
  align-items: flex-start;
}
.icon-circle {
  width: 44px; height: 44px;
  border: 1.5px solid var(--ink-blue);
  border-radius: 50%;
  color: var(--ink-blue);
}
.icon-circle svg { width: 22px; height: 22px; }
.body-heading { font-weight: 700; font-size: 16px; color: var(--ink-blue-700); }
.body-text { font-size: 13.5px; line-height: 1.75; color: var(--ink); }
```

### 2-5. セクション見出し（青バー＋ラベル）

```css
.section-heading {
  display: flex; align-items: center; gap: 12px;
  margin: 44px 0 14px;
}
.section-heading::before {
  content: "";
  width: 5px; height: 22px;
  background: var(--ink-blue);
  border-radius: 1px;
}
.section-heading .label {
  font-weight: 900; font-size: 18px;
  color: var(--ink); letter-spacing: 0.02em;
}
```

### 2-6. 6 視点グリッド（iter 9 でアイコン 40px に拡張）

```css
.seepoint-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; }
.seepoint-cell {
  position: relative;
  border: 1.5px solid var(--ink-blue);
  border-radius: var(--radius);
  padding: 20px 16px 16px;
  min-height: 176px;
}
.seepoint-cell .badge-num {
  position: absolute; top: -8px; left: 12px;
  width: 26px; height: 26px; border-radius: 50%;
  background: var(--ink-blue); color: var(--paper);
  font-family: var(--font-en); font-weight: 900; font-size: 13px;
}
.seepoint-cell .seepoint-icon {
  position: absolute; top: 12px; right: 14px;
  width: 40px; height: 40px;  /* iter 9 で 34→40 に拡張 */
  color: var(--ink-blue);
}
.seepoint-cell .seepoint-title {
  font-weight: 900; font-size: 19px;
  color: var(--ink); margin: 24px 0 8px;
}
.seepoint-cell .seepoint-body {
  font-size: 12.5px; line-height: 1.65; color: var(--ink-2);
}
```

### 2-7. Before/After 図（ネスト二層）

```css
.figure-ba {
  border: 1.5px solid var(--ink-blue);
  border-radius: var(--radius-lg);
  padding: 16px;
}
.figure-ba .ba-box {
  border: 1px solid var(--rule);
  border-radius: var(--radius);
  padding: 14px 16px;
  background: var(--paper-3);  /* 淡青 */
}
```

### 2-8. フローステップ

```css
.flow-step {
  padding: 16px 12px;
  border: 1.5px solid var(--ink-blue);
  border-radius: var(--radius);
  min-height: 110px;
}
.flow-step svg { width: 28px; height: 28px; color: var(--ink-blue); }
.flow-step .flow-label { font-size: 12px; font-weight: 700; line-height: 1.35; }
```

### 2-9. ページ上／下チロム（フッター横並び、iter 7）

```css
.page-body { padding: 40px 44px 100px; }

.page-chrome-top {
  display: flex; justify-content: space-between;
  padding: 20px 40px 12px;
  border-bottom: 1px solid var(--rule);
}

/* 下チロム: book icon + 本タイトル 横並び（縦積みより省スペース） */
.page-chrome-bottom {
  position: absolute; bottom: 20px; left: 0; right: 0;
  display: flex; flex-direction: column; align-items: center;
}
.page-chrome-bottom::before {
  content: ""; width: 44%; height: 1px;
  background: var(--rule); margin-bottom: 8px;
}
.page-chrome-bottom .chrome-inline {
  display: flex; flex-direction: row; align-items: center; gap: 6px;
}
.page-chrome-bottom .chrome-inline svg { width: 13px; height: 13px; }
.page-chrome-bottom .book-title {
  font-size: 10px; color: var(--ink-blue);
  letter-spacing: 0.1em; font-weight: 500;
}
```

---

## 3. 紙面構成の確定（iter 7-8 で確定、iter 22 で左右ページの役割を再バランス）

### 左ページ（p.04 相当）

1. チロム（book icon + 技術用語ラベル / ページ番号）
2. **タイトル** `{{title}}` — `title-hero` 96px ネイビー。**純粋名のみ**、括弧書き読みは含めない
3. **タイトル読み**（任意）`{{title_reading}}` — `title-reading` 14px グレー。タイトル直下に小さく。YAML が空なら非表示（2026-04-28 追加）
4. **タグライン帯** — 25〜40 字、淡青塗り、title の言い換えではなく一歩先の定義
5. **タグ行** — 体験区分 ／ 推奨読者レベル の 2 ピル
6. **本文セクション 2 つ**（ひとことで は削除）
   - 何をしてくれるか — 役割と仕組み、2〜4 文
   - どこで出会うか — 現場のどこで名前を聞くか、2〜4 文
7. **Before/After** — 親＋子の二層カード（または図の代替）
8. **擬人化ポンチ絵スロット（メインビジュアル）** — 200px 円アイコン＋ 340px 高さの青 dashed 枠、caption 30〜80 字（iter 22 で拡大、左ページの主役ビジュアルに昇格）
9. **会話での使い方例**（25〜50 字、推奨 30〜40、1 文） — 「わかってる人風」が自然にこの語を会話で使う 1 例。下チロム右側スロットに印字（2026-04-26 追加）
10. **下チロム** — 左 `YYYY.MM · Draft` ／ 右 `（会話での使い方例）`

※ 旧 iter 21 までの「関連用語ピル」（左ページ下段）は iter 22 で右ページ下段に移動。

### 右ページ（p.05 相当）

1. チロム（book icon + `{{title}} の見方` / ページ番号）
2. **セクション見出し**「この用語の見どころ」— 上端に配置（iter 22 で冒頭タイトルを削除し、直接始まる）
3. **6 視点グリッド** — 役割 ／ うれしさ ／ 注意点 ／ どこで役立つか ／ **はじめに** ／ 深掘り先
4. **2 カラム下段**（4:6 比率）
   - 非エンジニアのつまずき — 青ドット箇条書き
   - 私のコメント — ★/✓/!/☺ バッジ＋ラベル＋本文
5. **開発フローでの位置** — 4 ステップ横並び、アイコン＋ラベル＋矢印
6. **関連用語** — 3〜5 ピル（iter 22 で左ページから移動）
7. **参考 URL** — 1 本 + checked YYYY-MM-DD
8. **下チロム** — 左 `F-01 · language` ／ 右 📖 バイブコーディング図鑑

※ 旧 iter 21 までは冒頭に `{{title}} をどう読むか`（50px ネイビー、`title-hero--right`）が入っていたが、iter 22 で**削除**。誌面の縦が詰まり、「見どころ」「コメント」「フロー」が 1 ステップずつ上がった。

---

## 4. テンプレ側（markdown）で変えるべき箇所

[templates/entry_template.md](../../../templates/entry_template.md) を本仕様に合わせる場合の変更リスト:

| 変更箇所 | 現行 | 新 |
|---|---|---|
| `## ひとことで` | 1〜2 文の本文セクション | **削除**（tagline で代替） |
| `## バイブコーディングでの位置づけ` | 節名 | `## どこで出会うか` にリネーム |
| `### 4. どこで役立つか` | 6 視点 ④ | **変更なし**（iter 10 で「どこで効くか」から戻した） |
| `### 5. 最初に理解する範囲` | 6 視点 ⑤ | `### 5. はじめに` にリネーム |
| 右ページ冒頭サブタイトル | （無し） | （引き続き無し、前付けに集約） |
| 体験区分／推奨読者レベル | YAML のみ | タグ行として誌面表示前提、YAML はそのまま |
| （新規） ポンチ絵スロット | なし | **iter 22**: 左ページ最下段、Before/After の下。メインビジュアル（200px アイコン・340px 高さ）に拡大 |
| 右ページ冒頭タイトル `{{title}} をどう読むか` | `title-hero--right` | **iter 22 で誌面から削除**。markdown にも当該見出しを書かない |
| 関連用語セクション | 左ページ下段 | **iter 22**: 右ページ下段（開発フロー直下）へ移動 |

---

## 5. デザイン担当への引き渡し物

- [typescript_spread.html](design_philosophy_v2/typescript_spread.html) — iter 16 確定プロトタイプ
- [overlay.css](design_philosophy_v2/overlay.css) — 追加 CSS（base.css に被らない新 primitive のみ）
- [screenshots/iter16.png](design_philosophy_v2/screenshots/iter16.png) — 最終ビジュアル
- [writing_spec.md](design_philosophy_v2/writing_spec.md) — 節ごと文字数と書くもの原則（執筆者向け）
- [check_entry.py](design_philosophy_v2/check_entry.py) — 自動チェッカー（CI 組み込み可）
- [book_readiness_review.md](design_philosophy_v2/book_readiness_review.md) — 書籍化の残課題レビュー

デザイン担当は本プロトタイプを **React/Vue コンポーネント化**（zip の `ui_kits/book/TermCardPage.jsx` / `TermCardPageRight.jsx` を書き換え）する。その際に:
- 本ドキュメントの §2 の CSS 値を JSX スタイル／Tailwind クラスに翻訳
- §3 の紙面構成に従い 各 slot を props 化
- 本文「ひとことで」は削除（props から落とす）
- サブタイトルは個別エントリ側から落として前付けのみに残す

---

## 6. 16 世代イテレーションで残った決定事項

| 項目 | 最終値 | 世代 |
|---|---|---|
| 左タイトル | 96px ネイビー (#123E82) | iter 5 (サイズ), iter 7 (色黒→), iter 7 (色ネイビー→) |
| 右タイトル | 50px ネイビー (#123E82) | iter 5, iter 7 |
| タグライン背景 | `--ink-blue-100` | iter 2 |
| 本文セクション区切り | 1px dotted `--rule-strong` | iter 2 |
| セクション見出しバー | 5×22px 青、ラベル 18px 900 | iter 4 |
| 体験区分／推奨読者レベルタグ | padding 12/20, 15px 700, icon 20px | iter 8 |
| 6 視点セル | 縦レイアウト（番号左上・アイコン中央・タイトル中央・本文中央）、min-height 210 | iter 12 |
| 6 視点番号バッジ | 30px、枠内、14px 900 Inter | iter 12 |
| 6 視点アイコン | 52px、中央配置 | iter 9, 12 |
| 6 視点タイトル | 18px 900 | iter 3, 12 |
| Before/After 箱内 padding | 14/16 | iter 2 |
| フローステップ | padding 16/12, min-height 110 | iter 2 |
| ページ body padding | 40/44/100（ノド非対称あり） | iter 2, 16 |
| 縦横比 | 750×1061（√2、ISO A/B 系）。2026-04-28 に一時 1424px に膨らむ問題が表面化したが、ポンチ絵 rollback ＋ preview 専用 `overlay-tight.css`（W 案）で本来寸法に再収束 | iter 16, 2026-04-28 |
| ノド margin | 左ページは右 +14、右ページは左 +14 | iter 16 |
| 擬人化ポンチ絵スロット | 左ページ、青 dashed 枠 placeholder | iter 16 |
| 「最初に理解する範囲」→ | 「はじめに」 | iter 6 |
| 「どこで役立つか」 | 維持（iter 5 で「どこで効くか」にしたが iter 10 で戻した） | iter 10 |
| 「ひとことで」セクション | 削除（tagline で代替） | iter 7 |
| 右ページサブタイトル | 削除（前付け「この図鑑の読み方」に集約） | iter 8 |
| **タイトル末尾の括弧書き読み** | **廃止し `title-reading` 独立スロット（14px グレー）へ移動** | 2026-04-28 |
| フッター | 左右非対称: 左ページ=「2026.04·Draft／（会話での使い方例）」、右ページ=「F-01·language／📖 バイブコーディング図鑑」 | iter 7, 14, 15 |
| **specificity 罠** | base.css の `.vbcd h1` (0,1,1) に勝つため `.vbcd h1.title-hero` と書く | iter 5（iter 2-4 でハマった） |

---

## 7. 既存ルールへの影響

- **CLAUDE.md**「デザインはスコープ外」は本ドキュメントで一部超えた（markdown 構造だけでなく視覚仕様まで踏み込んだ）。実装は引き続き別担当、本ドキュメントまでが Claude Code のスコープ
- **文体ルール「ですます調必須」は維持**（CLAUDE.md 準拠）。サンプル本文が である調だった件は spec としては ですます で書き直す前提
- **`templates/entry_template.md` への反映タイミング**: iter 16 まで触っていない。ユーザー承認後に §4 のリストを適用する
- **既執筆 10 letter 分**: 「ひとことで」本文を持っているので、削除する場合は一括置換か次回レビュー送り。ユーザー判断待ち
- **`docs/quality_checklist.md` / `docs/quality_guidelines.md` / `docs/editorial_style.md`**: 相補関係。writing_spec.md は iter 16 レイアウト下での節単位閾値に特化、既存 docs は全体のトーン・品質原則を担う

## 8. 使い方（執筆者・レビュアー向け）

### 執筆するとき

1. [templates/entry_template.md](../../../templates/entry_template.md) を開く（※ v2 反映後の想定）
2. [writing_spec.md](design_philosophy_v2/writing_spec.md) §1-2 の節ごと文字数目安を参照
3. 書き終えたら `python drafts/prototypes/mockups/design_philosophy_v2/check_entry.py path/to/entry.md` で自動検証
4. エラー（E）はゼロにする、警告（W）は意図的な場合のみ残す

### レビューするとき

1. [book_readiness_review.md](design_philosophy_v2/book_readiness_review.md) §5 の総評表と照合
2. [typescript_spread.html](design_philosophy_v2/typescript_spread.html) をブラウザで開き、見開きレイアウトとして崩れないか確認
3. 自動チェッカーで CI 的に複数 entry を一括検証: `python check_entry.py --dir content/entries/`

### CI に組み込むとき

`check_entry.py` は終了コード 0=OK / 1=エラーあり を返す。GitHub Actions / pre-commit フックで:

```yaml
- run: python drafts/prototypes/mockups/design_philosophy_v2/check_entry.py --dir content/entries/
```
