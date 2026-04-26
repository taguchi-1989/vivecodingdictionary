# モバイル（Obsidian Mobile）編集ワークフロー手引き

*Phase 1 のセットアップ（[mobile_setup_guide.md](mobile_setup_guide.md)）が通った後に、実際にスマホで「何を」「どこに」書くかをまとめた手引きです。v0.1（2026-04-26）。*

*仕様の根拠は [mobile_inbox_requirements.md](mobile_inbox_requirements.md) と [editorial_style.md](editorial_style.md)、[v2_rules_summary.md](v2_rules_summary.md)。本文書はそれらを携帯で実行するための運用ガイドに絞ります。*

## このドキュメントのゴール

スマホ（Android ＋ Obsidian Mobile）から、次の 4 種類の編集が**安全に**できるようになることです。

| モード | 書く場所 | 安全度 | いつ使うか |
| :-- | :-- | :-- | :-- |
| A. 受信箱に書き溜め | `mobile_inbox/YYYY-MM-DD.md` | ◎ | 移動中・思いつき・短文。基本これ |
| B. 著者欄を直接書く | `content/entries/**/*.md` の右ページ著者欄 | ○ | 落ち着いて 1 件まとめて書ける時 |
| C. 裏台帳メモを足す | `content/entries/**/*.md` の末尾 | ○ | ポンチ絵案・出典・備考を思い出した時 |
| D. 本文節の手直し | `content/entries/**/*.md` の左/右ページ本文 | △ | 誤字・事実誤りなど、軽微な修正のみ |

「迷ったら A」が原則です。A は仕組みで衝突を防いでいて、PC 側に着いてから AI と一緒に整理できます。B/C は「自分の文章を自分で書く」モードです。D は要注意（後述）。

## 前提

- [mobile_setup_guide.md](mobile_setup_guide.md) の Step 1〜6 が通っている
- Obsidian Git の Auto pull / Auto commit & push が 10 分間隔で動いている
- PC 側で開発中のときは、PC で必ず先に `git pull` してから作業する自己ルール

## 共通の安全策（先に読む）

### 1. 開いたら必ず Pull、閉じる前に Push

Obsidian の自動同期は 10 分間隔ですが、**手動 Pull / Push が一番確実**です。

- スマホで作業を始める前：右サイドバーの Obsidian Git アイコン → **Pull**
- スマホで作業を終える前：右サイドバー → **Commit and push**

PC 側で `git pull` 忘れによるコンフリクトを起こさないために、**PC とスマホの作業時間を重ねない**のが鉄則です。

### 2. 書く対象は 1 セッション 1 ファイルまで

スマホは画面が狭く、複数ファイル横断は事故のもとです。

- 「今日は B-2 のつまずきを書く」と決める
- 別件を思いついたら、A モード（受信箱）に放り込んで戻る

### 3. 構造（見出し）は壊さない

`spread_v1` テンプレの節名（`## tagline` `## 何をしてくれるか` `## 私のコメント` 等）は機械チェックの依存先です。

- **見出し行（## で始まる行）は触らない**
- 中身の本文だけを足す／直す
- 万一見出しを壊したら、PC で `python3 scripts/validate_entry.py {対象ファイル}` が落ちて気づける

### 4. 怪しい時は受信箱（A）に逃がす

「ここを直したいが触っていいか分からない」と感じたら、A モードで `ai_feedback` として書き残し、PC で AI と相談します。詳細は [mobile_inbox_requirements.md](mobile_inbox_requirements.md) §3。

---

## モード A：受信箱に書き溜め（推奨）

最も安全で、運用も既に立ち上がっているモードです。

### 書く場所

- `mobile_inbox/YYYY-MM-DD.md`（日付ごと 1 ファイル、無ければ新規作成）

### 書き方

1 コメント＝ H2 セクション 1 個。フォーマット固定：

```markdown
## <entry_id> / <kind> [/ <sub>]

<本文テキスト>
```

実例：

```markdown
## B-2 / my_comment / first_impression
初見シンプル。3つの入口があると知って最初は戸惑った。

## B-2 / stumble
Opus/Sonnet/Haikuの3段階が、値段と賢さのどちらで分かれているのか最初わからなかった。

## B-2 / ai_feedback / 何をしてくれるか
4.6時代にラインナップ更新されたので書き直し候補。
```

### kind と sub の対応

| kind | sub | 反映先 |
| :-- | :-- | :-- |
| `my_comment` | `first_impression` / `good` / `bad` / `target` | 右ページ「私のコメント」の対応行 |
| `stumble` | （なし） | 右ページ「非エンジニアのつまずき」の箇条書き |
| `ai_feedback` | 指摘対象の節名（日本語可） | 裏台帳「備考」に引用形式で積む |

### PC へ戻ったら

```
ユーザー：「import-comments 実行して」
```

詳細は [skills/import-comments.md](../skills/import-comments.md)。

---

## モード B：著者欄を直接書く

「私のコメント」「非エンジニアのつまずき」は **著者本人のみ記入**で、AI が触らない欄です。スマホで直接書いても安全です。

### 書く場所

- `content/entries/{category}/{ID}_{slug}.md` の右ページ著者欄
  - `## 非エンジニアのつまずき`
  - `## 私のコメント`

### 書き方（つまずき）

箇条書き 3〜4 項目、各 15〜30 字目安。空の `-` 行を埋める形で足します。

```markdown
## 非エンジニアのつまずき

- Opus/Sonnet/Haikuの値段と賢さの対応がすぐ出てこなかった
- 「Projects」と「Artifacts」の違いが最初わからなかった
- 
```

### 書き方（私のコメント）

4 行固定。絵文字ラベル行はそのまま、コロンの後ろに本文を足します。各 20〜35 字目安。

```markdown
## 私のコメント

- 🙂 第一印象: 初見シンプル。3つの入口で最初戸惑った
- 👍 良い点: 長い文脈でも返答の筋が通っている
- 👎 ダメな点: 料金体系の言葉がまだ慣れない
- 👥 誰向けか: 文章を仕事で書く人
```

### 制約

- **絵文字ラベル行（🙂 / 👍 / 👎 / 👥）は触らない**：機械チェックがこれを見て判定します
- ラベル名（`第一印象:` `良い点:` 等）も触らない
- 字数オーバーは validator で警告が出ますが、PC 側で詰める想定で OK

### モード A と何が違うか

- A は **後で AI が反映先を機械的に振り分け**ます。失敗してもファイルは戻る
- B は **直接書く**ので、見出し構造を壊すと validator が落ちます

A で慣れてから B に進む順番が無難です。

---

## モード C：裏台帳メモを足す

ファイル末尾の **裏台帳メモ**（誌面ポンチ絵メモ／コミュニティ補完メモ／出典メモ／備考）は誌面に出ない作業欄で、ここに書くのも安全です。

### 書く場所と用途

| 節 | 用途 | スマホ向きの例 |
| :-- | :-- | :-- |
| `## 誌面ポンチ絵メモ` | デザイン担当への指示 | 「ロゴ近くに吹き出しで『シンプル』」のような図メモ |
| `## コミュニティ補完メモ` | SNS で見かけた表現・他の人の言い回し | 「Twitter で『沼』と呼ばれていた」 |
| `## 出典メモ` | URL ＋ checked 日付 | `- https://example.com/foo — checked 2026-04-26` |
| `## 備考` | 上記に入らない雑記 | 著者の判断保留メモ、`ai_feedback` 反映済みログ等 |

### 書き方

既存の節を残したまま、末尾に追記します。

```markdown
## 出典メモ

- https://docs.anthropic.com/en/docs/claude-code/overview — checked 2026-04-26
- https://www.anthropic.com/news/claude-3-5-sonnet — checked 2026-04-25
```

### 注意

- `## 備考` には、`ai_feedback` を import した結果の引用行（`> [著者指摘 ...]`）が積まれます。**手で書くときはその下に追記**し、引用行の中身は触らない
- `## コミュニティ補完メモ` は人物・サービスの実名を書くことがあります。誤情報を書かないよう、出典が思い出せない時は受信箱（A）に逃がす

---

## モード D：本文節の手直し（要注意）

左ページ（`## tagline` `## 何をしてくれるか` `## どこで出会うか` `## メイン図`）と右ページ前半（`## この用語の見どころ` `## 開発フローでの位置`）は、AI が書いた成果物です。

### やっていいこと

- 明らかな誤字脱字の修正
- 評価日（`evaluation_date`）以降に変わったモデル名・料金の単純訂正
- 句読点や改行の整えで読みやすくする

### やってはいけないこと

- 節の構造（見出し）を増減すること
- 字数目安（[v2_rules_summary.md](v2_rules_summary.md)）から大きく外す書き換え
- 主観や著者意見を本文に混ぜること（それは「私のコメント」へ）
- 引用形式の「`> [著者指摘 ...]`」行（備考欄に積まれた `ai_feedback` 履歴）の改変

### 迷ったらどうするか

**迷ったら本文は触らず、A モードで `ai_feedback` として書き残してください**。

```markdown
## B-2 / ai_feedback / 何をしてくれるか
2行目の「3 段階の」は4.6時代に4段階になっているので書き直し候補。
```

PC で AI と並んでから本文をどう書き換えるかを決める、の 2 段構えです。

---

## モード E（将来）：新規エントリの起票草案

外出先で「これエントリ化したい」と思った語の起票は、まだ正式運用に入っていません。当面は **`mobile_inbox/new_candidates.md`** に書き溜めるだけにしてください。

```markdown
## new_candidate / Voice Mode

- 何か：ChatGPT のリアルタイム音声会話モード
- 想定 ID：B-? もしくは E-?
- 一言：通話感覚で AI に相談できる
```

PC で `ledgers/entry_candidates.md` と突き合わせ、空き ID を振って `skills/write-entry.md` で着手します。

---

## ありがちなトラブルと対処

### 編集中に Obsidian が固まる

- vault 全体が大きいと起きやすい
- 対策：開きたいファイルを「ピン留め」して、Files ペインを閉じる
- それでも重い時：`mobile_inbox/` だけを書く運用に絞り、本文編集は PC 側で行う

### 自動 push の直後に PC 側で push したらコンフリクト

- 原則は §共通の安全策 を守る
- それでも起きたら：PC 側で `git pull --rebase` → 手動マージ → `git push`、その後スマホで Obsidian Git の **Pull**
- スマホ側で先に編集していた未 push 分が消えそうな時は、**まず Obsidian Git の Backup を取ってから**触る

### `## 私のコメント` の絵文字行を間違って消した

- すぐ書き戻す。フォーマットは [templates/entry_template.md](../templates/entry_template.md) の §私のコメント を見る
- スマホで戻せなければ、A モードに「絵文字行を消したかも、要確認」と書いて PC で復元

### validator が落ちた（PC で）

- `python3 scripts/validate_entry.py {ファイル}` が指摘した節名を、テンプレと突き合わせて手で戻す
- スマホでの編集中ならまず A モードに逃がして、PC 側で確認する

---

## 1 日の運用フローの例

朝の通勤：

1. Obsidian Mobile を開く → Obsidian Git で Pull
2. `mobile_inbox/2026-04-26.md` を新規作成
3. 昨日触った B-2（Claude）について「## B-2 / my_comment / first_impression」を 1 件書く
4. Commit and push（または 10 分待つ）

昼休み：

1. Pull
2. `content/entries/service/B-2_claude.md` を開く
3. 「非エンジニアのつまずき」に 1 行追加（モード B）
4. Commit and push

夜、PC で：

1. `git pull`
2. Claude Code に「import-comments 実行して」
3. 朝の `mobile_inbox/` 分が反映され、processed/ に移動
4. 昼の B モード分はそのまま反映済み（追加作業不要）
5. validator で異常がないか確認 → コミットがクリーンなら明日へ

---

## やらないこと（このガイドの守備範囲外）

- 新規エントリの本文執筆 → `skills/write-entry.md`（PC のみ）
- 誌面デザイン・CSS の調整 → スコープ外（[CLAUDE.md](../CLAUDE.md) §5）
- `ledgers/entries.csv` の編集 → PC 側のみ（CSV は機械処理の入口）
- ID の付け直し → やらない（[id_scheme.md](id_scheme.md)）

---

## 関連

- 同期セットアップ（前提）：[mobile_setup_guide.md](mobile_setup_guide.md)
- 受信箱の仕様：[mobile_inbox_requirements.md](mobile_inbox_requirements.md)
- 取り込みスキル：[../skills/import-comments.md](../skills/import-comments.md)
- 受信箱 README：[../mobile_inbox/README.md](../mobile_inbox/README.md)
- テンプレ構造：[../templates/entry_template.md](../templates/entry_template.md)
- v2 確定ルール：[v2_rules_summary.md](v2_rules_summary.md)
- 文体原則：[editorial_style.md](editorial_style.md)
- 品質チェック：[quality_checklist.md](quality_checklist.md)

## 履歴

- v0.1（2026-04-26）: 初版。Phase 1 完了後の実編集ワークフロー（A〜D モード）を整理。
