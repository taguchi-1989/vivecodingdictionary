# セッション日誌

*Claude Code セッションごとに何をやったかを時系列で記録する。引き継ぎ（next_session_handoff.md）が「次に何をやるか」を書くのに対し、本ファイルは「何をやってきたか」を辿るためのもの。新しい日付の記事は上に足す。*

---

## 2026-04-25（金） iter 22 レイアウト変更 + 方針 B 採択 + 執筆 3 本

### 開発再開の経緯

前セッションで v2 レイアウトの 21 世代反復と全エントリ監査が終了済み。本日は Playwright MCP でプロトタイプを表示しながら、レイアウトの**最終調整**と**運用仕様の固め**と**実装方針の決断**と**執筆**を同時進行した。

### やったこと（時系列）

1. **Playwright で typescript_spread.html をブラウザ表示**
   - `python -m http.server` でローカル配信、`file://` は Chrome でブロックされるので HTTP 経由に切替
   - ドロワーの状態制御に `browser_evaluate` で JS 実行

2. **iter 22 レイアウト変更の確定**（誌面 3 点）
   - 右ページ冒頭タイトル `{{title}} をどう読むか` を削除（markdown・誌面 双方）
   - 関連用語ピルを右ページ下段（開発フロー直下）に移動
   - 擬人化ポンチ絵スロットをメインビジュアル級に拡大（96→200px アイコン、150→340px 高さ）
   - プロトタイプ HTML と overlay.css を更新、スクリーンショットで確認

3. **iter 22 を仕様書に伝搬**（計 5 本）
   - [docs/v2_rules_summary.md](v2_rules_summary.md) §0 §1 §4 §5 を書き換え
   - [drafts/prototypes/mockups/design_philosophy_v2.md](../drafts/prototypes/mockups/design_philosophy_v2.md) §3 §4
   - [drafts/prototypes/mockups/design_philosophy_v2/writing_spec.md](../drafts/prototypes/mockups/design_philosophy_v2/writing_spec.md) §1-7 §2-1 §2-6
   - [templates/entry_template.md](../templates/entry_template.md)（関連用語ブロックを右ページ区分へ）
   - [scripts/validate_entry.py](../scripts/validate_entry.py)（`related_terms` を `page="right"`、左右合計目安を再配分）

4. **既存 active エントリ 12 件を新順に移行**
   - [scripts/migrate_iter22_related_terms.py](../scripts/migrate_iter22_related_terms.py) を作成（冪等）
   - A-1 / A-2 / B-1 / B-2 / C-2 / D-12 / E-1 / F-50 / G-1 / H-53 / I-1 / J-14 を一括で書き換え
   - archived 7 件はスキップ、v2 validator で 19 件 ☆ 違反 0

5. **文字数・項目数の決定版ルール整備**
   - `v2_rules_summary.md §2` を「単一真実点」として全面書き直し（§2-1〜§2-7）
   - 書式: 許容／推奨／判定記号（❌ エラー / ⚠️ 警告 / ℹ️ 情報）で明示
   - validator の不一致（tagline 25-40 → 25-45）と表記揺れ（つまずき 3-5 個 → 3 固定）を修正
   - writing_spec.md を「例・根拠の補足」に格下げし、数値は v2_rules_summary を参照させる構成に

6. **ハンバーガードロワー の 12 エントリをリンク化**
   - 「未生成」表記を `is-available` リンクに張替え、md ファイルへ直接遷移

7. **新規エントリ 3 本を並列執筆**（entry-writer サブエージェント）
   - B-3 ChatGPT（service / structure）
   - C-1 OpenAI（person / structure）
   - D-11 Claude 3.5 系（model / timeline）
   - 全て ☆ 違反 0、6 視点の軽微な字数超過（40→41〜50 字）警告のみ
   - ドロワーにも追加

8. **アーキテクチャ方針の決断: 方針 B（markdown → generator）**
   - 手書き HTML の量産は 20 件以上で破綻、という共通認識を確認
   - 著者判断で「markdown を正、HTML/PDF は生成器で吐く」方針に倒す
   - 実装（CSS / Astro / TSX / Paged.js）は**別担当**、本プロジェクトは markdown ＋ 仕様の維持

9. **方針 B の引き渡し資産 5 本を整備**
   - [ledgers/chapters.yaml](chapters.yaml) — 章マップ 10 章
   - `entries.csv` に `path` 列追加、15 active エントリに埋込み済
   - [scripts/sync_entries_csv.py](../scripts/sync_entries_csv.py) — md → CSV 同期スクリプト
   - [docs/entry_schema.yaml](../docs/entry_schema.yaml) — v2_rules_summary §2 の機械可読版
   - [docs/component_spec_v2.md](../docs/component_spec_v2.md) — 14 primitive に分解した実装担当向け仕様

### 決めたこと

- **アーキテクチャ**: 方針 B（markdown → 静的サイト生成器）
- **スタック採択**: **Astro + React コンポーネント（ハイブリッド C）**。ページ骨格は Astro（静的出力が PDF 化向き）、コンポーネント本体は `@astrojs/react` 経由で React（実装担当の書き味を保つ）
- **iter 22 のレイアウト確定**: 右ページタイトル削除・関連用語右ページ移動・擬人化スロット大サイズ
- **figure_type 別 primitive 5 種**: before_after / structure / comparison / workflow / timeline を overlay.css に常設化（structure のみ B-3 で実戦検証済、他 3 種はスケッチ段階）
- **開発フロー**: 推奨 4 ・許容 5 ・禁止 6+ を確定
- **数値の単一真実点**: `docs/v2_rules_summary.md §2` と `docs/entry_schema.yaml`。両者の値が衝突したら schema 側を正とする
- **本プロジェクトの責任範囲**: markdown 執筆 ＋ 仕様維持。Astro + React 実装は別担当

### 次セッションへの引き継ぎ

詳細は [next_session_handoff.md](next_session_handoff.md)。要点:

- ステージ 2 の執筆継続（次候補: G-2 Token / G-40 バイブコーディング / B-4 Cursor）
- モバイル投入フロー Phase 1 の試走
- 実装担当へのハンドオフは `component_spec_v2.md §6 チェックリスト` に沿って

### 本日のコミット予定（未コミット）

- iter 22 レイアウト変更（overlay.css / typescript_spread.html / 5 仕様書）
- 12 エントリ migration + migration スクリプト
- 3 新規エントリ（B-3 / C-1 / D-11）
- 方針 B の 5 成果物（chapters.yaml / entries.csv path 列 / sync_entries_csv.py / entry_schema.yaml / component_spec_v2.md）
- CLAUDE.md §7 と next_session_handoff.md の更新
