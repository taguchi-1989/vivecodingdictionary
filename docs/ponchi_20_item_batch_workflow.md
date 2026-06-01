# Ponchi 20 Item Batch Workflow

ポンチ絵を全件生成・再生成していくための、20件単位の運用手順。

## Principle

既存の `assets/ponchi/final/*.webp` は legacy final として扱う。新しいパイプラインでの完了条件は、次をすべて通ったものだけにする。

1. `subject_stack` 付き scene brief がある。
2. prompt lint を通る。
3. 2:1 ベース画像がある。
4. `1254x627` に正規化されている。
5. 密度・clearspace・キャラ・文字混入・ブランド混入の監査を通る。
6. 20件単位の contact sheet で確認済み。
7. ロゴが必要なものは公式素材を後合成し、出典が `docs/brand_usage_audit.md` に記録されている。
8. final へ昇格する判断が記録されている。

## Commands

全件を20件単位に分ける:

```powershell
python scripts\ponchi_batch_plan.py --batch-size 20
```

1バッチの確認表を作る:

```powershell
python scripts\ponchi_batch_report.py ponchi-batch-001
```

1バッチの現在状態を監査する:

```powershell
python scripts\ponchi_batch_audit.py ponchi-batch-001
```

観察ダッシュボードを更新する:

```powershell
python scripts\ponchi_pipeline_dashboard.py
```

生成後に imagegen の出力を batch フォルダへ取り込む:

```powershell
C:\Users\tgch1\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe `
  scripts\ponchi_collect_generated_batch.py ponchi-batch-001
```

途中の項目だけを取り込む場合:

```powershell
C:\Users\tgch1\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe `
  scripts\ponchi_collect_generated_batch.py ponchi-batch-001 `
  --entries B-3,B-8 `
  --out-dir assets\ponchi\experiments\batches\ponchi-batch-001-b-focus\generated-bases-v4
```

プロンプトを検査する:

```powershell
python scripts\ponchi_prompt_lint.py assets\ponchi\pipeline_prompts\ponchi-batch-001\*.md
```

公式ロゴ合成前に密度も監査する:

```powershell
python scripts\composite_official_logo.py `
  --input <base_1254x627.png> `
  --logo <official_logo.png> `
  --out <overlay_1254x627.png> `
  --audit-density `
  --min-bbox-coverage 0.50
```

ロゴ用 clearspace も含めて観察監査する:

```powershell
C:\Users\tgch1\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe `
  scripts\ponchi_image_audit.py `
  assets\ponchi\experiments\batches\ponchi-batch-001-b-focus\selected\*base_selected_1254x627.png `
  --out-csv ledgers\ponchi_b_focus_selected_base_audit.csv `
  --out-md docs\ponchi_batch_audits\ponchi-batch-001-b-focus-selected-base.md `
  --contact-sheet assets\ponchi\experiments\batches\ponchi-batch-001-b-focus\selected_base_contact_sheet.png
```

## Batch Artifacts

各バッチでは次を作る。

| artifact | path pattern | purpose |
| --- | --- | --- |
| batch report | `ledgers/ponchi_batches/ponchi-batch-001.md` | 20件の状態と確認表 |
| prompt files | `assets/ponchi/pipeline_prompts/ponchi-batch-001/{entry_id}.md` | scene brief + generation prompt |
| generated bases | `assets/ponchi/experiments/batches/ponchi-batch-001/{entry_id}_base_1254x627.png` | ロゴなし2:1ベース |
| overlay candidates | `assets/ponchi/experiments/batches/ponchi-batch-001/{entry_id}_overlay_1254x627.png` | 公式ロゴ後合成候補 |
| final candidates | `assets/ponchi/final_candidates/ponchi-batch-001/{entry_id}_candidate.webp` | final へ上げる前の確認待ち候補 |
| contact sheet | `assets/ponchi/experiments/batches/ponchi-batch-001/contact_sheet.png` | ユーザー確認用 |
| audit markdown | `docs/ponchi_batch_audits/ponchi-batch-001.md` | 採用/再生成/ロゴ待ち/却下の判断 |
| dashboard | `docs/ponchi_pipeline_dashboard.html` | 全バッチの観察ページ |

## Stage Meaning

| stage | meaning | next action |
| --- | --- | --- |
| `brief_needed` | 新パイプラインの scene brief がない | `subject_stack` 付き prompt を作る |
| `prompt_review` | 既存 prompt がある | lint して不足項目を補う |
| `overlay_wait` | ロゴが必要だが公式素材が未確定 | ベース生成は可、final 昇格は禁止 |
| `overlay_ready` | 公式素材がローカルにある | 後合成と overlay 監査へ進む |
| `overlay_audit` | 公式ロゴ合成済み | 目視・寸法・密度確認 |
| `blocked_brand_asset` | 公式素材や条件が不明 | 代用品を作らず停止 |

## Confirmation Gate

20件ごとに確認し、各 item を次のどれかにする。

| confirmation | meaning |
| --- | --- |
| `accept_base` | ロゴ不要または後合成前のベースとして採用 |
| `accept_overlay` | 公式ロゴ後合成版として採用 |
| `rerun_prompt` | prompt を直して再生成 |
| `rerun_density` | 主題が小さい、細かすぎる、空きすぎ |
| `rerun_clearspace` | ロゴ予定地が汚れている、または広すぎる |
| `overlay_wait` | ベースはよいが公式素材待ち |
| `reject` | 概念誤り、ロゴ混入、キャラ崩れなどで不採用 |

final 候補を作る:

```powershell
C:\Users\tgch1\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe `
  scripts\ponchi_stage_final_candidates.py ponchi-batch-001 `
  --include-overlay-audit
```

`--include-overlay-audit` はユーザー確認前の候補を `review_pending` として棚に置くだけ。`rerun_*` や `reject` の confirmation が付いた項目は候補化しない。

## Current Batch Split

Current generated ledger:

- CSV: `ledgers/ponchi_generation_batches.csv`
- first report: `ledgers/ponchi_batches/ponchi-batch-001.md`
- first audit: `docs/ponchi_batch_audits/ponchi-batch-001.md`
- dashboard: `docs/ponchi_pipeline_dashboard.html`
- batch size: 20
- total target entries: 350
- total batches: 18

Current stage counts after adding `v0` to logo review:

| stage | count |
| --- | ---: |
| `brief_needed` | 334 |
| `prompt_review` | 4 |
| `overlay_wait` | 4 |
| `overlay_ready` | 1 |
| `overlay_audit` | 6 |
| `blocked_brand_asset` | 1 |

## Next Work

Start with `ponchi-batch-001`.

1. A-1 through A-11 are parked; do not spend review time there until B is stable.
2. B-1 through B-9 now have selected 2:1 base images.
3. B-2, B-4, B-5, B-7, and B-9 are staged as review-pending final candidates in `assets/ponchi/final_candidates/ponchi-batch-001/`.
4. Keep B-1, B-3, and B-8 in `overlay_wait` until exact official asset choices are confirmed. Keep B-6 blocked.
5. Stop for user confirmation on `assets/ponchi/final_candidates/ponchi-batch-001/final_candidates_contact_sheet.png` before final promotion or moving to batch 002.

Current prompt status for `ponchi-batch-001`:

- `assets/ponchi/pipeline_prompts/ponchi-batch-001/`: 19 prompt files
- `python scripts\ponchi_prompt_lint.py assets\ponchi\pipeline_prompts\ponchi-batch-001\*.md`: pass
- B-5 is not regenerated in this prompt batch because it is `overlay_audit`.
