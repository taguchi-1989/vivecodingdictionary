# skill: draw-ponchi — 擬人化ポンチ絵 SVG を 1 件〜複数件まとめて作る

*擬人化ポンチ絵の SVG（draft）を、`drafts/ponchi/{entry_id}.svg` に書き出すワークフロー。個別生成は `ponchi-drawer` サブエージェントに委譲する。*

## いつ呼ばれるか

ユーザーが以下のように言った場合:

- 「B-3 のポンチ絵を作って」「D-11 のポンチ絵」 ← 単発
- 「B-3 から D-11 まで一気に」「まだ SVG 無いやつ全部」 ← 複数
- 「ポンチ絵を作り直したい」「全件差し替え」 ← 全件

## 前提（最初に必ず確認）

- [docs/ponchi_svg_spec.md](../docs/ponchi_svg_spec.md) — SVG 仕様（色・stroke・手書き化）
- [.claude/agents/ponchi-drawer.md](../.claude/agents/ponchi-drawer.md) — 実行サブエージェント
- [ledgers/entries.csv](../ledgers/entries.csv) — どのエントリが active か。`path` 列に md ファイル位置あり
- 出力ディレクトリ: `drafts/ponchi/`（なければ作る）

## 手順

### Step 0. 対象エントリの特定

- ユーザーの指示から entry_id リストを作る
- 「全件」「未生成のみ」などの曖昧表現なら:
  - `drafts/ponchi/*.svg` をリストし、`content/entries/**/*.md` のうち未生成のもののみ対象
- archived エントリは対象外（status: archived）

### Step 1. 各エントリに対して `ponchi-drawer` を呼ぶ

```
Agent({
  subagent_type: "ponchi-drawer",
  description: "Draw ponchi for {entry_id}",
  prompt: "entry_id={entry_id} の擬人化ポンチ絵 SVG を作ってください。
         markdown: {md_path}
         出力先: drafts/ponchi/{entry_id}.svg
         必ず docs/ponchi_svg_spec.md を読んで仕様に従ってください。"
})
```

- **並列呼び出し可**. 複数エントリなら `run_in_background: true` で 3〜5 件同時に投げる
- ただし同時実行しすぎると quota 逼迫するので 5 件上限推奨

### Step 2. 生成物を確認

各呼び出しが完了したら:

- `drafts/ponchi/{entry_id}.svg` が存在するか確認
- ファイルサイズが 500 字以上（簡単な検証）
- 最初の行が `<?xml` か `<svg`
- `stroke="#1A1A1A"` or `stroke="#1a1a1a"` を含む（黒線画ルール）
- 不合格なら再度 ponchi-drawer を呼び直し（1 エントリ 2 回まで。それ以上は親に返してユーザー判断）

### Step 3. preview_gen.py で反映確認

- `python scripts/preview_gen.py` を実行
- preview_gen.py は `drafts/ponchi/{entry_id}.svg` があればそれを読んで `.ponchi-icon` に差し込む（この機能は preview_gen.py v2 で実装）
- HTTP サーバを立てて 1〜2 件をブラウザ確認、崩れないか

### Step 4. ユーザーへの報告

- 生成した件数、保存先、既知の問題
- 「次のエントリはどうする？」の小さな提案

## 守ること

- **1 コマンドで複数エントリ処理**を基本にする（単発呼びでも batch 1 件扱い）
- **SVG の中身は直接書かない**. 必ず ponchi-drawer に委譲。親エージェントがコンテキスト肥大化しないため
- **既存 SVG を上書きする時はユーザー確認**. 「B-3 のポンチ絵を作って」とだけ言われて既存があるなら「上書きで良いですか？」
- **失敗したエントリのリトライは 2 回まで**。3 回目は人間判断に委ねる

## 関連 skill・agent

- [skills/write-entry.md](write-entry.md) — エントリ本体の執筆。ポンチ絵メモは書くが SVG までは作らない
- [.claude/agents/entry-writer.md](../.claude/agents/entry-writer.md) — エントリ執筆サブエージェント
- [.claude/agents/ponchi-drawer.md](../.claude/agents/ponchi-drawer.md) — SVG 生成サブエージェント（本 skill が呼ぶ）

## スコープ外

- 画像生成 API の呼び出し（Midjourney / DALL·E / Stable Diffusion 等）は本 skill の範囲外。本 draft SVG を叩きにして本番画像を作るのは後工程
- 本 SVG の本番イラスト化（イラストレーター委託）も別工程
