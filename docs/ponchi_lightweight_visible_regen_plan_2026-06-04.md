# Ponchi Lightweight Visible Regen Plan 2026-06-04

## 判断

`docs/ponchi_lightweight_gallery.html` の軽い順デフォルト表示 top100 を対象にする。

ユーザー目視で残してよいとされたもの:

| rank | entry | title | size |
| ---: | --- | --- | ---: |
| 87 | `G-32` | Slash Command | 34.5KB |
| 91 | `G-47` | Auto-compact | 36.1KB |
| 92 | `B-30` | Amazon Bedrock | 38.0KB |
| 94 | `H-4` | コードレビュー | 39.6KB |
| 96 | `H-52` | Copilot から Claude Code までの流れ | 40.9KB |
| 97 | `G-31` | Hook | 41.1KB |
| 98 | `G-40` | バイブコーディング | 42.1KB |
| 99 | `G-38` | Plan Mode | 42.5KB |

`G-28` は `ledgers/entries.csv` と `assets/ponchi/final/` に存在しないため、今回のkeep対象には入れない。入力ミスの可能性として保留。

上記8件以外の top100 表示画像は、現時点では `regen_user_ng_visible` として作り直し対象にする。

## 作成物

- 判定CSV: `ledgers/ponchi_lightweight_visible_regen_plan.csv`
- 20件単位の再生成バッチCSV: `ledgers/ponchi_lightweight_regen_batches.csv`

件数:

| decision | count |
| --- | ---: |
| `keep_user_ok` | 8 |
| `regen_user_ng_visible` | 92 |

再生成タイプ:

| regen_type | count | 意味 |
| --- | ---: | --- |
| `composition_regen` | 13 | 既知の機械的2:1化、中央配置、横長構図として弱いもの |
| `richer_scene_regen` | 3 | `B-7 Claude Code` 型。ロゴと単純な箱線に依存し、誌面の絵として薄いもの |
| `lightweight_quality_regen` | 76 | ファイルが軽く、描き込み・濃淡・意味の密度が弱いもの |

## 優先順位

### P0

既に別ルールで問題候補になっているものを最優先にする。

- `composition_regen_review`
- `sparse_diagram_review`
- `full_regen_review`

### P1

25KB未満の軽量画像。機械スコアが高くても、見た目が薄くなりやすい。

### P2

25KB以上35KB未満。軽量寄りで、画面上ではしょぼさが出やすい。

### P3

35KB以上だが、top100内でユーザーがNGと判断したもの。

## バッチ

92件を20件単位で切る。

| batch | count | 方針 |
| --- | ---: | --- |
| `lightweight-regen-001` | 20 | P0全部 + P1先頭4件。まずここを作り直す |
| `lightweight-regen-002` | 20 | P1継続。軽量抽象図を強化 |
| `lightweight-regen-003` | 20 | P1継続 |
| `lightweight-regen-004` | 20 | P1/P2 |
| `lightweight-regen-005` | 12 | P2/P3残り |

## First Batch

`lightweight-regen-001`:

| # | priority | entry | title | size | regen_type |
| ---: | --- | --- | --- | ---: | --- |
| 1 | P0 | `J-93` | Ubuntu | 13.2KB | `composition_regen` |
| 2 | P0 | `J-91` | CLI | 16.1KB | `composition_regen` |
| 3 | P0 | `J-81` | M.2 | 16.4KB | `composition_regen` |
| 4 | P0 | `J-92` | Linux | 17.4KB | `composition_regen` |
| 5 | P0 | `J-90` | GUI | 18.5KB | `composition_regen` |
| 6 | P0 | `I-4` | MCP Transport | 21.0KB | `composition_regen` |
| 7 | P0 | `I-3` | MCP Client | 21.9KB | `composition_regen` |
| 8 | P0 | `B-6` | Windsurf | 24.1KB | `richer_scene_regen` |
| 9 | P0 | `I-2` | MCP Server | 24.5KB | `composition_regen` |
| 10 | P0 | `J-100` | 識字（リテラシー） | 26.6KB | `composition_regen` |
| 11 | P0 | `B-4` | Cursor | 30.5KB | `composition_regen` |
| 12 | P0 | `B-7` | Claude Code | 31.6KB | `richer_scene_regen` |
| 13 | P0 | `I-5` | MCP SDK | 32.0KB | `composition_regen` |
| 14 | P0 | `B-5` | GitHub Copilot | 32.5KB | `richer_scene_regen` |
| 15 | P0 | `B-2` | Claude | 34.5KB | `composition_regen` |
| 16 | P0 | `B-3` | ChatGPT | 39.4KB | `composition_regen` |
| 17 | P1 | `I-21` | Puppeteer MCP | 13.4KB | `lightweight_quality_regen` |
| 18 | P1 | `J-4` | ASI | 15.1KB | `lightweight_quality_regen` |
| 19 | P1 | `J-80` | SATA | 15.8KB | `lightweight_quality_regen` |
| 20 | P1 | `J-19` | 量子化 | 16.0KB | `lightweight_quality_regen` |

## 再生成方針

### composition_regen

- 既存の単純横長化を捨てる。
- 2:1の横幅に意味の流れを作る。
- 中央に1つの箱を置くだけにしない。
- 200px幅でも「何の話か」が残る構図にする。

### richer_scene_regen

- ロゴを主役にしない。
- 公式素材は後合成。AI生成でロゴ風マークを描かせない。
- 人物・ロボット・作業場面・比較対象を入れて、サービスが使われる状況を見せる。
- `B-7 Claude Code` 型の、文書箱から吹き出しが出るだけの構図は禁止。

### lightweight_quality_regen

- 抽象図でもよいが、線・面・関係の密度を増やす。
- 白地に細線だけで終わらせない。
- 2-4個の大きな視覚ブロックを置く。
- 小さな点やカードを増やすだけではなく、Before/After、流れ、対比、中心概念を明確にする。

## 採用基準

再生成後は、次を満たすものだけ `assets/ponchi/final/` 昇格候補にする。

- 1254x627の2:1。
- 白黒グレー指定青中心。
- 公式ロゴが必要なものは後合成。
- 軽い順ギャラリーで少なくとも今回のkeep対象8件と同程度以上に見える。
- `file_size_kb` は絶対基準にしないが、20KB未満なら必ず目視確認。
- `sparse_diagram_review` に再び入るものは不採用。
