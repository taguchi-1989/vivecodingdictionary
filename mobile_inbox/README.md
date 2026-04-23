# mobile_inbox — 外出先コメントの受信箱

*スマホ（Android ＋ Obsidian Mobile）で書き溜めた著者コメントの、取り込み前の置き場です。PC 側で `/import-comments` スキルが読み、対応エントリに反映します。*

## 使い方

### スマホ側（入れる）

- `YYYY-MM-DD.md` を日付ごとに 1 本作る
- 1 コメントを 1 セクション（H2 見出し）で書く：

```markdown
## <entry_id> / <kind> [/ <sub>]

<本文テキスト>
```

- `kind` は `my_comment` / `stumble` / `ai_feedback` のいずれか
- 詳しい仕様は [../docs/mobile_inbox_requirements.md](../docs/mobile_inbox_requirements.md)

### 記入例

```markdown
## B-2 / my_comment / first_impression
初見シンプル。でも3つの入口があると知って最初は戸惑った。

## B-2 / stumble
Opus/Sonnet/Haikuの3段階が、値段と賢さのどちらで分かれているのか最初わからなかった。

## B-2 / ai_feedback / 何をしてくれるか
4.6時代にラインナップ更新されたので書き直し候補。

## F-50 / my_comment / good
差分が取れる、の説明がしっくりきた。
```

### PC 側（取り込む）

1. `git pull` で最新の受信箱を取得
2. Claude Code に「import-comments 実行して」と指示
3. スキルが各エントリに反映し、処理済みファイルを `processed/` へ移動

## フォルダ構成

```
mobile_inbox/
├── README.md           # この手引き
├── 2026-04-24.md       # 未処理の受信箱
├── 2026-04-25.md
└── processed/          # 処理済みアーカイブ
    ├── 2026-04-22.md
    └── ...
```

## 関連ドキュメント

- 要件定義：[../docs/mobile_inbox_requirements.md](../docs/mobile_inbox_requirements.md)
- 取り込みスキル：[../skills/import-comments.md](../skills/import-comments.md)
- 執筆スキル：[../skills/write-entry.md](../skills/write-entry.md)
