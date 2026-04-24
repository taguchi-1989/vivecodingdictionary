# VibeCodingDictionary プロジェクト向け CLAUDE.md

*次のセッションがこのプロジェクトに入ったときに、テイストと構造を外さないようにするための手引きです。毎セッション最初にこのファイルを読む前提。*

## 1. このプロジェクトは何か

非エンジニア・周辺職種の人が、AI 開発まわりの語彙を「辞書引き」できるようにする図鑑。詳細は [docs/book_philosophy.md](docs/book_philosophy.md)。

読者像は **「AI を仕事で使いたいが、プログラミングで生計を立てているわけではない人」**。著者も同じ立場（応用情報・G 検定保持、機械系の開発業務、AI を使う側）。

## 2. 今やっていること

letter A〜J 計 335 件の候補から、各エントリを `spread_v1` テンプレで書き進めている段階です。

10 letter 分のサンプル（A-2 / B-2 / C-2 / D-12 / E-1 / F-50 / G-1 / H-53 / I-1 / J-14、加えて旧 3 桁 ID の 301〜305 / 101 / 201）は書き出し済み。残り約 320 件。

## 3. 書くときに必ず守ること

### トーン

- **「です・ます」調で書く**（必須）
- 結論から書く
- 読者を馬鹿にしない、強い断定を避ける

### 構造（[templates/entry_template.md](templates/entry_template.md) の順序・節名に従う）

- **左ページ**：tagline ／ ひとことで ／ 何をしてくれるか ／ バイブコーディングでの位置づけ ／ メイン図 ／ 関連用語
- **右ページ**：この用語の見どころ（6 視点）／ 開発フローでの位置（必須）
- **著者記入欄**（非エンジニアのつまずき ／ 私のコメント）：**著者本人のみ記入。AI は空スケルトンだけ残す**
- **裏台帳メモ**：誌面ポンチ絵メモ ／ コミュニティ補完メモ ／ 出典メモ ／ 備考

### 書き方の細則

- カタカナ語は初出で日本語訳を補う（例：Context ＝ 文脈）
- 略称は初出で展開（例：CC ＝ Claude Code）
- モデル・料金・提供状況は `evaluation_date` つきの時変情報
- 事実と主観を分ける（主観は「私のコメント」欄だけ、AI は触らない）

詳細は [docs/editorial_style.md](docs/editorial_style.md)。

## 4. ID 体系（触らない）

- letter A〜J の 10 区切り固定
- 10 番刻みサブ範囲
- 欠番は詰め直さない
- v0.5 で renumber は終了。以降は **ID を動かさず、追加は空き番号のみ**

詳細は [docs/id_scheme.md](docs/id_scheme.md)。

## 5. デザインは本プロジェクトのスコープ外

**誌面レイアウト・HTML/CSS・実レンダリング・配色調整は別担当**。本プロジェクトの Claude Code では扱いません。

- `drafts/prototypes/mockups/` の過去試作は参照用として残しますが、新規のデザイン作業は**やらない**
- テンプレの「構造」（節の順序、裏台帳への記述）は守るが、見た目の検討はしない
- `誌面ポンチ絵メモ` にはデザイン担当への**指示書**として「何を描きたいか」を残す

## 6. 書く／レビューする／取り込むときの手順書

### 執筆する（自動化：`entry-writer` サブエージェント経由）

- 「B-3 ChatGPT を書いて」のように頼まれたら、[.claude/agents/entry-writer.md](.claude/agents/entry-writer.md) サブエージェントを呼び出す（Agent tool、subagent_type="entry-writer"）。親エージェントは直接書かない
- 手順の本体：[skills/write-entry.md](skills/write-entry.md) Step 0〜7
- 下準備メモ：[ledgers/stage2_briefs.md](ledgers/stage2_briefs.md)（Stage 2 の 46 件ぶん）

### レビュー／自動チェック

- **保存すると自動で走る**：[scripts/validate_entry.py](scripts/validate_entry.py) が `content/entries/**/*.md` の Edit/Write 後に発火し、字数・構造・トーンを機械チェック（[.claude/settings.json](.claude/settings.json) の PostToolUse hook で設定）
- 手でも走らせられる：`python3 scripts/validate_entry.py content/entries/service/B-1_gemini.md`
- チェック観点：[docs/quality_checklist.md](docs/quality_checklist.md)（特に §H 誌面量の目安）
- 原則：[docs/quality_guidelines.md](docs/quality_guidelines.md)

### 外出先コメントを取り込む

- [docs/mobile_inbox_requirements.md](docs/mobile_inbox_requirements.md) — Obsidian Mobile + Git 連携の仕様
- [docs/mobile_setup_guide.md](docs/mobile_setup_guide.md) — Android セットアップ手引き（PAT 作成 → clone → 初回テスト）
- [skills/import-comments.md](skills/import-comments.md) — `mobile_inbox/` から本編へ反映する手順

## 7. 迷ったとき開く順番

1. [docs/book_philosophy.md](docs/book_philosophy.md) — 根っこのフィロソフィー
2. [docs/editorial_style.md](docs/editorial_style.md) — トーン・文体
3. [templates/entry_template.md](templates/entry_template.md) — 構造の正解
4. [ledgers/entry_candidates.md](ledgers/entry_candidates.md) — 335 件の棚と要確認
5. [ledgers/writing_priority.md](ledgers/writing_priority.md) — ステージ別の執筆順
6. [docs/id_scheme.md](docs/id_scheme.md) — ID ルール（触らない）

## 8. 次のステップ

[ledgers/next_session_handoff.md](ledgers/next_session_handoff.md) にこの時点の TODO と引き継ぎ事項が入っています。次セッションはまずそれを開いてください。

## 9. リポジトリ

管理は <https://github.com/Taguchi-1989/ViveCodingDictionary>（`main` ブランチ）。
