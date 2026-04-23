# スキル：モバイル・コメントを取り込む（import-comments）

*スマホ（Obsidian Mobile）から `mobile_inbox/` に push された著者コメントを、対応するエントリ Markdown に反映するための手順書です。AI（Claude）が読む前提で書いています。*

## このスキルの目的

外出先で書き溜めた 3 種のコメント（`my_comment` / `stumble` / `ai_feedback`）を、PC で `content/entries/**/*.md` に安全に取り込むことです。

仕様の根拠は [docs/mobile_inbox_requirements.md](../docs/mobile_inbox_requirements.md) を参照。

## 前提条件

- `git pull` 済みで、`mobile_inbox/` 配下に未処理の `YYYY-MM-DD.md` が 1 本以上ある状態
- スマホ側は Obsidian Mobile + Obsidian Git で、見出し規約（§3）に従って書かれている前提

## 入力フォーマット

`mobile_inbox/YYYY-MM-DD.md` は、1 コメント ＝ 1 セクションの構造。H2 見出しで区切られる。

```markdown
## <entry_id> / <kind> [/ <sub>]

<本文テキスト>
```

- `entry_id`：`A-1` 〜 `J-99` または旧 3 桁 ID。`ledgers/entries.csv` で存在確認
- `kind`：`my_comment` / `stumble` / `ai_feedback` のいずれか
- `sub`：
  - `my_comment` のとき：`first_impression` / `good` / `bad` / `target`
  - `ai_feedback` のとき：指摘対象の節名（日本語可）
  - `stumble` のとき：省略

## 手順

### Step 0. 前提を読む

1. [docs/mobile_inbox_requirements.md](../docs/mobile_inbox_requirements.md) — 仕様と反映ルール
2. [docs/quality_checklist.md](../docs/quality_checklist.md) — 反映後のチェック観点
3. `mobile_inbox/` の中身をざっと眺めて、どのエントリが触られているかを把握

### Step 1. 未処理ファイルの洗い出し

- `mobile_inbox/*.md`（`processed/` 以外）を列挙
- 各ファイルを開いて、H2 セクションを順に読み取る

### Step 2. コメントごとのパースと反映

各セクションを次の流れで処理：

1. **ヘッダ解釈**：`## <entry_id> / <kind> [/ <sub>]` から 3 要素を抜く
2. **エントリ特定**：`ledgers/entries.csv` で `entry_id` の行を探し、対応する `content/entries/**/*.md` のパスを特定（ファイル名は `{id}_{slug}.md`）
3. **反映**：`kind` に応じて以下を実行

#### `my_comment` の反映

- 対象ファイルの「私のコメント」セクションを開く
- `sub` に応じて該当ラベル行の末尾に追記：
  - `first_impression` → `🙂 第一印象: ` の後ろに追記
  - `good` → `👍 良い点: ` の後ろに追記
  - `bad` → `👎 ダメな点: ` の後ろに追記
  - `target` → `🎯 誰に向くか: ` の後ろに追記
- 既存テキストがあれば、改行＋`  / ` で区切って追記（同じ項目に複数回コメントが来た想定）

例：

```markdown
- 🙂 第一印象: 初見シンプル  / 3つの入口で最初戸惑った
```

#### `stumble` の反映

- 対象ファイルの「非エンジニア視点のつまずき」セクションを開く
- 空の `-` 行を 1 つ埋める
- 空行が無くなっていれば、末尾に `- {本文}` を追加

#### `ai_feedback` の反映

- 対象ファイルの **裏台帳「備考」** セクションの末尾に、引用形式で追記：

```markdown
> [著者指摘 2026-04-24 / 対象節: 何をしてくれるか] Opus/Sonnet/Haikuの説明、4.6時代のラインナップで書き直した方が良い
```

- 本文は絶対に書き換えない。ここで積んだ指摘は、後日「まとめ本文改訂」タスクで別途処理

### Step 3. 反映後のステータス更新

- コメントが反映されたエントリの `entries.csv` を確認
- 状態遷移の目安：
  - 元が `candidate` → `drafting` に（新規にコメントが入り、著者欄が動き始めた意味）
  - 元が `drafting` または `needs_review` → `needs_review` のまま（著者欄が追記された）
  - 元が `ready` → `needs_review` に戻す（変更が入ったので再チェック対象）
- YAML frontmatter の `status` も同じ値に合わせる

### Step 4. 処理済みファイルの移動

- すべてのコメントが正常反映された `mobile_inbox/YYYY-MM-DD.md` は、そのまま `mobile_inbox/processed/` へ移動
- 部分失敗（§Step 5）があったファイルは元の場所に残す

### Step 5. エラー処理

以下のケースはスキップし、処理ログに記録。そのファイルは `processed/` へ移動しない。

| エラー | 対応 |
| :-- | :-- |
| `entry_id` が `entries.csv` に存在しない | 該当セクションは飛ばし、ログに `unknown_id: X-NN` を追加 |
| `kind` 不明 | 同上 |
| `sub` が `my_comment` で規定外の値（例：`great` など） | 同上、`sub` 値をログに残す |
| 本文が空 | 同上 |
| 対応ファイルが `content/entries/**/*.md` に存在しない | ログに `file_missing: X-NN` を追加。エントリ新規作成はこのスキルの責務外なので、`skills/write-entry.md` に回す |

処理ログはユーザーへの報告メッセージにまとめて返す（ファイルとしては残さない）。

## 守ること

- **本文節（左ページ／右ページ）は絶対に書き換えない**：`ai_feedback` は備考に積むだけ
- **著者欄を AI が先読み補完しない**：`my_comment` / `stumble` は与えられた本文をそのまま入れる。文体調整・要約・分割もしない
- **processed/ への移動は、全セクションが正常反映された場合のみ**：部分失敗ファイルは残して、人間が次回見直せるように

## 呼び出し例

```
ユーザー：「import-comments 実行して」
→ Step 0〜4 を順に実行
→ 最後に「X 件反映／Y 件スキップ。スキップ内訳：...」のサマリを返す
```

## やらないこと

- エントリの新規作成（`skills/write-entry.md` の役割）
- 本文の加筆・要約・整形（著者の声をそのまま入れる）
- `ai_feedback` を本文に反映（別タスクとして人間判断を経る）
- `mobile_inbox/processed/` の古いファイルの削除（履歴として残す）

## 関連

- 要件定義：[docs/mobile_inbox_requirements.md](../docs/mobile_inbox_requirements.md)
- 執筆スキル：[skills/write-entry.md](write-entry.md)
- チェックリスト：[docs/quality_checklist.md](../docs/quality_checklist.md)
- 台帳：[ledgers/entries.csv](../ledgers/entries.csv)

## 履歴

- v0.1（2026-04-24）: 初版。Phase 2 の入口として定義。実装は手作業ベース（スクリプト化は後続）。
