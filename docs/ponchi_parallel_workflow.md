# ポンチ絵 連続生成ワークフロー

`image_gen` はリポジトリ内スクリプトから直接並列実行できないため、実運用では「バッチを切る」「複数レーンで順番に投げる」「生成済み PNG を固定名で取り込む」という形で並列化します。

## 1. 台帳を同期する

```powershell
python scripts\ponchi_batch.py sync
```

`ledgers/ponchi_generation_queue.csv` を、現在の `drafts/ponchi/*.svg` と `assets/ponchi/final/*.png` から更新します。

## 2. 次バッチを作る

```powershell
python scripts\ponchi_batch.py next --name batch_20260516_01 --count 12 --lanes 4 --sync
```

出力:

- `assets/ponchi/batches/batch_20260516_01.csv`
- `assets/ponchi/batch_prompts/batch_20260516_01.md`

`lane` は手動実行時の論理レーンです。Codex の `image_gen` 自体は 1 枚ずつですが、プロンプト束を 4 レーン分に分けておくことで、複数セッションや複数実行者に配りやすくなります。

## 3. 画像を生成する

`assets/ponchi/batch_prompts/{batch}.md` の順番どおりに `image_gen` へ投げます。

重要:

- 公式ロゴ、実画面、実在人物の肖像は避けます。
- 画像内の日本語長文は入れません。
- 生成順を崩さないようにします。後工程で時刻順に固定名へコピーします。

## 4. 生成済み PNG を取り込む

```powershell
python scripts\ponchi_batch.py import `
  --name batch_20260516_01 `
  --source C:\Users\tgch1\.codex\generated_images\019e2873-8014-7bd1-b213-24a4978d8f38 `
  --skip 61
```

`--skip` は、その生成フォルダ内で既に取り込み済みの古い PNG 枚数です。取り込み後、`assets/ponchi/final/{entry_id}.png` が作られ、台帳も更新されます。

## 5. コミット単位

安定する単位は 10〜40 枚です。

```powershell
git add assets\ponchi\final ledgers\ponchi_generation_queue.csv assets\ponchi\batches assets\ponchi\batch_prompts
git commit -m "Add ponchi image batch"
```
