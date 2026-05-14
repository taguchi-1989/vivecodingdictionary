# バイブコーディング図鑑 (VibeCodingDictionary)

非エンジニア・周辺職種の人が AI 開発まわりの語彙を「辞書引き」できるようにする図鑑。

詳細な趣旨は [docs/book_philosophy.md](docs/book_philosophy.md)、執筆ガイドは [CLAUDE.md](CLAUDE.md) を参照。

## 開発状況（at a glance）

| 指標 | 値 |
|------|----|
| エントリ総数 | 327 件（A〜J 章） |
| [済] 完成 | 245 件 |
| [人書] 著者欄記入待ち | 64 件 |
| [AI整] / [AI直] | 10 件 |
| [凍] archived | 8 件 |
| 本文密度中央値 | 約 397 字（TS 見本基準 328 字、比 121%）|
| ポンチ絵 SVG あり | 15 件（残 304 件は画像生成待ち）|

## 開発時プレビュー

ローカルで `python3 scripts/preview_gen.py` を走らせると、`drafts/prototypes/preview/` 配下に開発用プレビューが生成されます（本番は別担当が Astro + React で実装）。生成物は git 管理外。

### 主要ダッシュボード（要ローカル生成）

- **[全エントリ一覧 overview.html](drafts/prototypes/preview/overview.html)** — 各エントリの全 10 セクション字数・著者欄字数・ポンチ絵有無・PDF/HTML プレビューリンクを 1 画面で。章・状態・ポンチ絵で絞り込み可。
- 個別エントリ HTML: `drafts/prototypes/preview/<ID>.html`
- 個別エントリ PDF (199×281mm 本サイズ): `drafts/prototypes/preview/pdf/<ID>.pdf`

### 監査レポート（コミット対象）

- **[字数監査サマリ](ledgers/density_audit.md)** — TS 見本基準と各セクションの max/推奨ターゲット、章別平均、肥大セクション一覧
- **[字数監査 詳細表](ledgers/density_audit_detail.md)** — 全 308 エントリ × 全セクションの字数表（⚠ max 超、▲ 推奨超）
- **[執筆優先度](ledgers/writing_priority.md)** — ステージ別の執筆順
- **[要直しキュー](ledgers/revision_queue.md)** — validator 自動生成、☆違反／警告／書きかけ／著者レビュー待ちの一覧
- **[次セッション引き継ぎ](ledgers/next_session_handoff.md)**

## 主なスクリプト

| スクリプト | 用途 |
|-----------|------|
| `scripts/generate_skeleton.py` | スケルトン（YAML + 必須節見出し）一括生成 |
| `scripts/validate_entry.py` | エントリ検証（字数・構造・トーン）。保存フックで自動実行 |
| `scripts/preview_gen.py` | 開発用 HTML プレビュー生成 |
| `scripts/preview_to_pdf.py` | preview HTML → 199×281mm PDF 化、overflow 検出 |
| `scripts/density_audit.py` | 字数バリエーション監査（サマリ + 詳細表） |
| `scripts/overview_gen.py` | 全エントリ一覧 overview.html 生成 |
| `scripts/sync_entries_csv.py` | `ledgers/entries.csv` をディスクの最新 path に同期 |
| `scripts/update_review_queue.py` | revision_queue.md 自動更新 |

## ドキュメント

- [docs/v2_rules_summary.md](docs/v2_rules_summary.md) — v2 確定ルール総覧（最初に読む）
- [docs/entry_schema.yaml](docs/entry_schema.yaml) — 字数・必須節の機械可読版
- [docs/component_spec_v2.md](docs/component_spec_v2.md) — 実装担当（Astro + React）への引き渡し仕様
- [docs/editorial_style.md](docs/editorial_style.md) — トーン・文体の原則
- [docs/claude_layout_handoff.md](docs/claude_layout_handoff.md) — 実寸 PDF レイアウト調整の引き渡し
- [templates/entry_template.md](templates/entry_template.md) — エントリの構造テンプレ

## ID 体系

A〜J の 10 区切り。10 番刻みのサブ範囲。欠番は詰め直さず、追加は空き番号のみ。詳細 [docs/id_scheme.md](docs/id_scheme.md)。

## リポジトリ

<https://github.com/Taguchi-1989/ViveCodingDictionary> （`main` ブランチ）
