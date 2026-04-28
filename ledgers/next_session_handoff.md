# 次セッションへの引き継ぎ（2026-04-28 v7 更新 / スケルトン先行）

*2026-04-28 セッションで「スケルトン先行運用」へ切り替えました。letter A〜J 計 339 件のうち約 318 件にスケルトン（status: skeleton、本文未着手の枠だけ）を生成済み。次セッションはこのファイルと [docs/v2_rules_summary.md](../docs/v2_rules_summary.md) を読んだあと、書きたいエントリの YAML を `status: skeleton → drafting` に上げて `entry-writer` で本文を埋めてください。*

## 2026-04-28: スケルトン先行運用へ切り替え

**変更内容**:

- 新ステータス `status: skeleton` を追加（[docs/entry_schema.yaml](../docs/entry_schema.yaml) v2.27.0）。validator は archived/sample と同様にスキップ
- スケルトン専用テンプレ：[templates/skeleton_template.md](../templates/skeleton_template.md)
- ジェネレータ：[scripts/generate_skeleton.py](../scripts/generate_skeleton.py)
- B letter 37 件で先にテストし、YAML パーサのインラインコメント問題と既存ファイル上書き事故を発見・修正してから残り 281 件を一括生成

**現状ステータス内訳**（[ledgers/entries.csv](entries.csv)）:

- `needs_review`: 11（A-2, B-1, B-2, C-2, D-12, E-1, F-50, G-1, H-53, I-1, J-14）
- `drafting`: 1（B-3 ChatGPT）
- `candidate`: 3（A-1, C-1, D-11 — 既に書かれているが needs_review に上げる前。手で確認・昇格を）
- `sample`: 6（旧 3 桁 ID、archived 相当）
- `skeleton`: 318（本文未着手）

**次セッションの最短ルート**:

1. [stage2_briefs.md](stage2_briefs.md) の 46 件から 1 件選ぶ（連関の強い B-4 Cursor、C-1 OpenAI などが入口）
2. md ファイルを開いて `status: skeleton` → `status: drafting` に変更
3. `entry-writer` サブエージェント呼び出し（"B-4 Cursor を書いて"）
4. validator で機械チェック → 著者レビュー → `status: needs_review`

---

## （旧）2026-04-26 v6 更新内容（参考）

*v2 レイアウトの 21 世代反復と全エントリ監査・修正が終わり、iter 22 で左右ページの役割再バランスを実施。続く 2026-04-26 セッションで「会話での使い方例」セクションを左ページ末尾に正式追加しました。*

## 2026-04-26: 「会話での使い方例」セクション追加

**誌面追加 1 点**:

「わかってる人風」が自然にこの語を会話で使う 1 例を、左ページ末尾の独立スロット（下チロム右側「（会話での使い方例）」枠）に印字するセクションを正式追加。**25〜50 字（推奨 30〜40）、1 文**。markdown 上は `## メイン図` の後、`<!-- 右ページ -->` の前に置く。

**伝搬済みファイル**:

- [templates/entry_template.md](../templates/entry_template.md) — `## 会話での使い方例` セクション追加
- [docs/v2_rules_summary.md](../docs/v2_rules_summary.md) §1 / §2-3 / §2-6 / §5 リネーム履歴
- [docs/entry_schema.yaml](../docs/entry_schema.yaml) — left_page slot ＋ required_sections に追加（schema_version v2.26.0）
- [docs/quality_checklist.md](../docs/quality_checklist.md) — B 左ページにチェック項目追加
- [skills/write-entry.md](../skills/write-entry.md) — Step 3 左ページの順序リストに追加
- [.claude/agents/entry-writer.md](../.claude/agents/entry-writer.md) — Step 3 字数目安テーブルに行追加
- [scripts/validate_entry.py](../scripts/validate_entry.py) — REQUIRED_SECTIONS / SECTION_TARGETS に追加
- [drafts/prototypes/mockups/design_philosophy_v2/check_entry.py](../drafts/prototypes/mockups/design_philosophy_v2/check_entry.py) — REQUIRED_SECTIONS / SECTION_RULES に追加
- [drafts/prototypes/mockups/design_philosophy_v2/writing_spec.md](../drafts/prototypes/mockups/design_philosophy_v2/writing_spec.md) — §1-8 として追加
- [drafts/prototypes/mockups/design_philosophy_v2.md](../drafts/prototypes/mockups/design_philosophy_v2.md) — §3 紙面構成に項目追加

**既存エントリ**: 既存 20 エントリ（A-1 / A-2 を除く active 13 件 ＋ archived 7 件）に会話での使い方例を 1 文ずつ追加済み。A-1 preface / A-2 reading_guide は本書の序文・読み方ガイドのため対象外。

**字数の決定**: 当初「許容 30-40 / 推奨 30-38」で仮置きしたが、既存エントリ実測（B-2 Claude=29 字、I-1 MCP=42-47 字など）を踏まえて**許容 25-50 / 推奨 30-40** に最終調整。validator は許容外でのみ ⚠️ 警告。

## iter 22（2026-04-25）: 左右ページの役割再バランス

**誌面変更 3 点**:

1. **右ページ冒頭タイトル `{{title}} をどう読むか` を削除**（誌面・markdown 双方）。右ページは「この用語の見どころ」から直接始まる
2. **関連用語ピルを右ページ下段（開発フローの直下）に移動**。markdown 上も右ページ区分に移した
3. **擬人化ポンチ絵スロットをメインビジュアルに拡大**（200px アイコン・340px 高さ）。左ページ最下段、Before/After の下に置く主役ビジュアル

**伝搬済みファイル**:

- [docs/v2_rules_summary.md](../docs/v2_rules_summary.md) §0 チェックリスト／§1 紙面構造／§4 レイアウト／§5 リネーム履歴
- [drafts/prototypes/mockups/design_philosophy_v2/overlay.css](../drafts/prototypes/mockups/design_philosophy_v2/overlay.css) `.ponchi-slot` をデフォルトで大サイズに
- [drafts/prototypes/mockups/design_philosophy_v2/typescript_spread.html](../drafts/prototypes/mockups/design_philosophy_v2/typescript_spread.html) 左ページから関連用語削除・右ページ下段に再配置・右タイトル削除
- [drafts/prototypes/mockups/design_philosophy_v2.md](../drafts/prototypes/mockups/design_philosophy_v2.md) §3 紙面構成
- [drafts/prototypes/mockups/design_philosophy_v2/writing_spec.md](../drafts/prototypes/mockups/design_philosophy_v2/writing_spec.md) §1-7 擬人化スロット／§2-1 右ページ冒頭タイトル削除／§2-6 関連用語（右ページへ）
- [templates/entry_template.md](../templates/entry_template.md) 関連用語ブロックを右ページ区分へ
- [scripts/validate_entry.py](../scripts/validate_entry.py) `related_terms` を `page="right"` に、左右合計目安を左 155-250／右 220-430 に更新

**既存エントリの移行**: [scripts/migrate_iter22_related_terms.py](../scripts/migrate_iter22_related_terms.py) で **active 12 エントリ**（A-1, A-2, B-1, B-2, C-2, D-12, E-1, F-50, G-1, H-53, I-1, J-14）の `## 関連用語` ブロックを `## 開発フローでの位置（必須）` の直後に移動済み（2026-04-25）。archived 7 エントリはスキップ。再実行しても冪等（`already migrated` を返す）。

**既知の注意**: 移行後も v2 validator（check_entry.py）は全 19 エントリ ☆ 警告 0。ただし strict 側の `scripts/validate_entry.py` は既存エントリで文字数超過（tagline / 何をしてくれるか等）を警告する。これは移行前からの編集課題で、移行による新規回帰ではない。

## 2026-04-25 追加: 静的サイト生成器への移行準備（方針 B 採択）

著者判断で **「markdown を正、HTML/PDF はそこから生成する」方針** に倒した。本プロジェクトは markdown ＋ 仕様の維持が主務。実装（CSS / Astro / TSX / Paged.js）は別担当へ引き渡す想定。

**整備済みの引き渡し資産 4 本**:

- [ledgers/chapters.yaml](chapters.yaml) — letter（A〜J）→ 章ラベル／カテゴリ／ディレクトリのマップ。ハンバーガーナビの自動生成元。
- [ledgers/entries.csv](entries.csv) — `path` 列を追加（`scripts/sync_entries_csv.py` で md 実体と自動同期）。15 active エントリに path 埋込み済。
- [docs/entry_schema.yaml](../docs/entry_schema.yaml) — v2_rules_summary §2 の機械可読版。frontmatter 制約・文字数・必須節・リネーム履歴を YAML で集約。**generator / validator / 仕様書の三者が同一入力を参照する単一真実点**。
- [docs/component_spec_v2.md](../docs/component_spec_v2.md) — `typescript_spread.html` を 14 primitive / 6 セクション / 2 ページ / 1 スプレッドに分解した引き渡し仕様。**スタック採択: Astro + React ハイブリッド（C）**（§0 に確定、2026-04-25）。Paged.js で PDF 化想定。

**新規エントリ追加時の運用**:

1. エントリを書く（entry-writer で）
2. `python scripts/sync_entries_csv.py` で path 列を更新
3. `python scripts/validate_entry.py` で字数・トーン検証
4. `python drafts/prototypes/mockups/design_philosophy_v2/check_entry.py` で構造検証
5. （任意）`typescript_spread.html` のドロワーに手動追加（generator 稼働後はこの 5 が不要になる）

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
