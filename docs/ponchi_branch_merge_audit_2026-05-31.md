# Ponchi Branch Merge Audit 2026-05-31

## 目的

ポンチ絵の 2:1 再生成と公式ロゴ運用について、他ブランチに残っている作業を確認し、今の `main` に安全に取り込む範囲を整理する。

## 現在の状態

- 現在ブランチ: `main`
- `main` は `origin/main` より 2 commits ahead。
- 直近でコミット済み:
  - `de4e84d Document ponchi regeneration workflow`
  - `a93a6cb Document ponchi logo sizing`
- ワークツリーには `assets/ponchi/final/*.webp` の大量変更と `assets/ponchi/experiments/regeneration/` の未追跡ファイルが残っている。
- 上記の画像差分は今回の文書コミットには含めない。画像は目視監査後に別単位で扱う。

## 確認したブランチ

| ブランチ / ref | main との差分 | 判定 |
| :-- | :-- | :-- |
| `origin/codex/preview-layout-polish` | `main` との差分なし | 追加マージ不要 |
| `codex/preview-layout-polish` | `b2556af`, `2b7d1dc` が main 未反映 | 部分取り込み候補あり |
| `chore/import-mobile-drafts-and-salvage` | `006b9de` が main 未反映 | そのままマージしない |

## 確認した stash

| stash | 内容 | 判定 |
| :-- | :-- | :-- |
| `stash@{0}` | `drafts/prototypes/mockups/design_philosophy_v2/overlay.css`, `ledgers/next_session_handoff.md` | ポンチ再生成とは無関係 |
| `stash@{1}` | 同上 | ポンチ再生成とは無関係 |

## 有用だった過去作業

### `2b7d1dc Add imagegen logo reference workflow`

含まれていたもの:

- `drafts/IMAGE_GEN_POLICY_v2.md` の v2.12 方針。
- 公式ロゴ参照パイプラインの文書。
- `role_balance`, `composition_type`, `scene_brief` の運用。
- 手や指の破綻を避けるポーズ制限。
- Docker, Go, Kubernetes, Node.js, PHP, Python, Rust などの公式ロゴ候補と取得元ログ。
- 生成実験画像。

取り込み方針:

- ルール知見は `docs/ponchi_character_bible.md` と `docs/ponchi_image_generation_rules.md` に統合する。
- 公式ロゴを imagegen に保持させる旧方針は、現在の安全側ルールに合わせて採用しない。
- 現在の正は「AI はロゴを生成しない。公式素材を後工程で決定論的に合成する」。
- 旧ブランチのロゴ素材は候補として有用だが、実際に使う前に `docs/brand_usage_audit.md` に取得元、ローカルパス、利用条件を追記してから採用する。
- 生成実験画像は本番差し替えとしては採用しない。

### `b2556af Add draft assets and AWS icon set`

含まれていたもの:

- 前付け/後付け用の draft HTML と生成画像。
- AWS Architecture Icons 一式。
- `scripts/resize_to_2_1.py` などの補助スクリプト。

取り込み方針:

- AWS アイコンセットはすでに `main` 側に存在するため、追加マージ不要。
- draft HTML と前付け画像はポンチ本文再生成とは別作業として扱う。
- 補助スクリプトは必要になった時点で個別に比較する。

### `006b9de Add generated ponchi images batch`

含まれていたもの:

- `E-25`, `E-26`, `E-27`, `E-30`, `E-50`, `H-*`, `I-*`, `J-*` の PNG 生成画像。
- `ledgers/ponchi_generation_queue.csv` の更新。

取り込み方針:

- 旧生成 PNG は、現在のブランド資産ルール、キャラ一貫性ルール、2:1 意味構図監査を通していない。
- そのまま `main` にマージしない。
- 必要なら個別に目視比較し、良い構図だけを `scene_brief` の参考にする。

## 今回 main に反映した内容

- Character A/B/C の見た目は固定しつつ、男女の説明役・聞き手役を固定しないルールを追加。
- `role_balance` を文書化。
- 手・指・持ち物の破綻を避けるポーズ制限を追加。
- 生成前 `scene_brief` を必須化。
- `composition_type` を文書化。

## マージ判断

現時点では、他ブランチを丸ごと `git merge` しない。理由:

- 未監査の生成画像が大量に混ざる。
- ロゴを imagegen に保持させる旧運用が、現在の公式後合成ルールと衝突する。
- 現在のワークツリーに未コミット画像差分が大量にあり、通常マージは衝突や意図しない画像採用を招きやすい。

安全な進め方:

1. ルール文書だけを先に統合してコミットする。
2. 公式ロゴ素材は `docs/brand_usage_audit.md` に追記できるものだけ個別に取り込む。
3. 画像差し替えは `scene_brief`、プロンプト、生成物、公式素材合成、寸法監査を 1 エントリずつまとめてコミットする。
