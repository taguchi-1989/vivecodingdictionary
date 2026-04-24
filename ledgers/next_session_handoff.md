# 次セッションへの引き継ぎ（2026-04-25 v4 更新）

*前セッションで v2 レイアウトの 21 世代反復と全エントリ監査・修正が終わりました。次セッションはこのファイルを最初に開き、続いて [docs/v2_rules_summary.md](../docs/v2_rules_summary.md) を読んでから執筆に入ってください。*

---

## 最初の 3 分で把握すべき現状

- **v2 レイアウト凍結済み**: iter 1-21 で確定。全ルールは [docs/v2_rules_summary.md](../docs/v2_rules_summary.md) に集約
- **既存 19 エントリ全て v2 準拠**: `python drafts/prototypes/mockups/design_philosophy_v2/check_entry.py --dir content/entries/` で全 OK
- **テンプレ（templates/entry_template.md）は v2 対応済**: 新規執筆はそのままコピーで OK
- **自動チェッカー稼働中**: 保存時に PostToolUse hook で走る（scripts/validate_entry.py）＋ 手動では check_entry.py

---

## この 2 セッションで完了したこと（2026-04-24 〜 2026-04-25）

### Design System v2 の採択と凍結

- Claude.ai/design が出した見開きサンプル（TypeScript p.04-05）をゴールとし、Playwright で 21 世代の HTML 反復
- 最終 HTML: [drafts/prototypes/mockups/design_philosophy_v2/typescript_spread.html](../drafts/prototypes/mockups/design_philosophy_v2/typescript_spread.html)
- CSS primitive: [drafts/prototypes/mockups/design_philosophy_v2/overlay.css](../drafts/prototypes/mockups/design_philosophy_v2/overlay.css)
- 反復スクショ iter 1-21: [drafts/prototypes/mockups/design_philosophy_v2/screenshots/](../drafts/prototypes/mockups/design_philosophy_v2/screenshots/)
- 右上ハンバーガーナビで A〜J の 2 階層エントリリストを実装

### 仕様ドキュメント 4 本

- [docs/v2_rules_summary.md](../docs/v2_rules_summary.md) — **正式入口**（執筆前に必ず）
- [drafts/prototypes/mockups/design_philosophy_v2.md](../drafts/prototypes/mockups/design_philosophy_v2.md) — 設計思想・CSS トークン・決定履歴
- [drafts/prototypes/mockups/design_philosophy_v2/writing_spec.md](../drafts/prototypes/mockups/design_philosophy_v2/writing_spec.md) — 節ごと文字数・書き方原則
- [drafts/prototypes/mockups/design_philosophy_v2/book_readiness_review.md](../drafts/prototypes/mockups/design_philosophy_v2/book_readiness_review.md) — 書籍化の残課題

### 自動チェッカー

- [drafts/prototypes/mockups/design_philosophy_v2/check_entry.py](../drafts/prototypes/mockups/design_philosophy_v2/check_entry.py)
- 使い方: `python drafts/prototypes/mockups/design_philosophy_v2/check_entry.py --dir content/entries/`
- archived エントリはスキップ、エラー・警告付きで出力

### 既存エントリの v2 対応

**11 新 letter エントリ**を v2 仕様に合わせて修正（[6b58358], [7db1d65]）:

- A-2 / B-1 / B-2 / C-2 / D-12 / E-1 / F-50 / G-1 / H-53 / I-1 / J-14
- 「ひとことで」削除、本文を 200 字以内に圧縮、6 視点セルを 40 字以内、related_terms を 5 個に

**6 旧 3 桁エントリ**を `status: archived` に凍結:

- 201 / 301 / 302 / 303 / 304 / 305 （101 は既に archived）

**新規 A-1 まえがき** を作成（[content/entries/common/A-1_preface.md](../content/entries/common/A-1_preface.md)）

### 節名リネーム（全ファイル伝搬）

| 旧 | 新 | 影響ファイル |
|---|---|---|
| 非エンジニア視点のつまずき | **非エンジニアのつまずき** | 38 |
| 誰に向くか | **誰向けか** | 22 |

### 紙面の確定ビジュアル（iter 1-21 の累積）

- 左タイトル 96px ネイビー、右タイトル 50px ネイビー（純黒はしんどい・純青は目立ちすぎ）
- タグライン帯は淡青塗り（--ink-blue-100）、25〜45 字
- 6 視点セル: 縦スタック、番号バッジ左上、アイコン 52px 中央（4 個差し替え: 的に crosshair / 電球 / 若葉→sprout / file-search）
- つまずき:コメント = **4:6** 比率
- フッター左右分割: 左ページ「YYYY.MM · Draft / （会話での使い方例）」、右ページ「F-01 · language / 📖 バイブコーディング図鑑」
- ノド非対称 margin、縦横比 750×1061（√2 準拠）
- 本文 16px、6 視点本文 14.5px（A4 換算 約 11pt）
- 右上プロトタイプナビ（ハンバーガー → A〜J 2 階層）

---

## 次セッションの TODO

### 最優先: ステージ 2 の執筆着手

[writing_priority.md](writing_priority.md) §ステージ 2 の 46 件を [stage2_briefs.md](stage2_briefs.md) と併読。

新規エントリ執筆手順:

1. [docs/v2_rules_summary.md](../docs/v2_rules_summary.md) の §0 1 分チェックリストに目を通す
2. [templates/entry_template.md](../templates/entry_template.md) を該当ディレクトリへコピー（`content/entries/service/B-3_chatgpt.md` のように）
3. YAML → tagline → 本文 2 節 → Before/After → 関連用語 → 6 視点 → 開発フロー → 裏台帳の順に埋める
4. 著者記入欄（非エンジニアのつまずき／私のコメント）は空スケルトンのまま残す
5. `python drafts/prototypes/mockups/design_philosophy_v2/check_entry.py content/entries/path/to/entry.md` で検証、エラーゼロに
6. `entries.csv` の status を更新

次に書く候補（stage2_briefs の並び）:

1. **B-3 ChatGPT**（H-53 と接続）
2. **C-1 OpenAI**（B-3 との流れ）
3. **D-11 Claude 3.5 系**（D-12 と接続）
4. **G-2 Token**（G-1 Context とセット）
5. **G-40 バイブコーディング**（本書の中心語彙）

### 著者確認の残件

- **Cursor の "head F" モデル**: `cursor-tab-3` のことか、`Composer` か、別物か。回答次第で D-35 の扱いを決定

### 旧 3 桁 ID の letter-ID 書き直し（素材として取り込み）

- 301 JavaScript → F-1（予定）
- 302 TypeScript → F-2（予定）
- 303 ESLint → F-10（予定）
- 304 React → F-11（予定）
- 305 Next.js → F-20（予定）
- 201 Gemini 2.5 系 → D-2（予定）
- 101 Gemini は B-1 に取り込み済（archived）

ステージ 2 執筆と一体で、対応する letter-ID を書くときに旧 3 桁の内容を素材として引用する形。

### 並行: モバイル投入フロー Phase 1

[docs/mobile_inbox_requirements.md](../docs/mobile_inbox_requirements.md) §9 Phase 1。Android Obsidian Mobile 経由のコメント取り込みを一度回して、import-comments スキルの挙動を確認。

### 保留事項

- **論文エントリの配置**（Transformer 論文等）: 現 H-58 のまま、他の論文候補が揃ってから
- **タイムラインの細分化**: Claude 系 / Gemini 系のマイナー版刻みは後回し
- **302_typescript の著者欄 AI 記入**: 新テンプレで F-2 を書き直すときにクリア（archived なので急がない）
- **書籍化の印刷工程**: bleed / CMYK 色校正 / フォント埋め込み確認は別担当に渡す段階で（[book_readiness_review.md](../drafts/prototypes/mockups/design_philosophy_v2/book_readiness_review.md) §5-6）

---

## スコープ外（やらない）

- **CSS・React 実装（v2 仕様の実装）**: 別担当。本プロジェクトは markdown ベースの仕様更新・執筆・検証まで
- ただし v2 仕様自体の**微調整・議論・追加ルールの集約**は引き続き本プロジェクトで OK

---

## セッション再開時の最初の動き

1. このファイルを開く
2. [docs/v2_rules_summary.md](../docs/v2_rules_summary.md) を通読（執筆前の前提を揃える）
3. 著者に Cursor "head F" の再確認（5 分で済む）
4. [stage2_briefs.md](stage2_briefs.md) から 1 件選び、上記の執筆手順で着手

---

## 直近コミット（新しい順）

- `8c44654` add docs/v2_rules_summary.md: consolidated v2 rules for authors
- `6b58358` refine typography, 4:6 bottom split, icons; rename 視点/向くか
- `2f71c65` bump body text sizes one step across the spread
- `9560b01` add prototype hamburger nav with A-J two-level drawer
- `7db1d65` bring entries to v2 spec: trim 11 letter drafts, archive 6 legacy 3-digit
- `4ab0a84` add Design System v2 spec, prototype, and entry validator
- `6d1eb6c` migrate to v2 template from finalized design mockup
