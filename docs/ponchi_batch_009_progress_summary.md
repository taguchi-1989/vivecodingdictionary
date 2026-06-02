# ponchi-batch-009 progress summary

対象: `F-37` から `F-71` までの 20 件。

## 数字サマリー

| 段階 | 件数 | 対象 |
| --- | ---: | --- |
| prompt 作成済み | 20 / 20 | F-37 - F-71 全件 |
| prompt lint pass | 20 / 20 | F-37 - F-71 全件 |
| 2:1 base 作成済み | 20 / 20 | F-37 - F-71 全件 |
| 2:1 base audit pass | 20 / 20 | F-37 - F-71 全件 |
| logo_avoid | 11 / 20 | F-42, F-51 - F-59, F-71 |
| 公式ロゴ/公式アイコン要確認 | 9 / 20 | F-37, F-38, F-40, F-41, F-44, F-50, F-60 - F-62 |
| overlay_wait / overlay_audit | 9 / 20 | F-37, F-38, F-40, F-41, F-44, F-50, F-60 - F-62 |
| final candidate 化済み | 0 / 20 | 未生成 |
| final 昇格済み | 0 / 20 | まだ `assets/ponchi/final/` へはコピーしない |

## Entry 一覧

| entry | title | prompt | 2:1 base | logo policy | current status |
| --- | --- | --- | --- | --- | --- |
| F-37 | Japanese Language Pack for VS Code | done | pass | waiting | overlay_wait |
| F-38 | Markdown All in One | done | pass | waiting | overlay_wait |
| F-40 | npm | done | pass | waiting | overlay_wait |
| F-41 | Vite | done | pass | waiting | overlay_wait |
| F-42 | ビルド | done | pass | logo_avoid | base complete |
| F-44 | pnpm | done | pass | waiting | overlay_wait |
| F-50 | git | done | pass | waiting | overlay_wait |
| F-51 | git push | done | pass | logo_avoid | base complete |
| F-52 | git pull | done | pass | logo_avoid | base complete |
| F-53 | branch | done | pass | logo_avoid | base complete |
| F-54 | commit | done | pass | logo_avoid | base complete |
| F-55 | merge | done | pass | logo_avoid | base complete |
| F-56 | .gitignore | done | pass | logo_avoid | base complete |
| F-57 | リポジトリ | done | pass | logo_avoid | base complete |
| F-58 | git stash | done | pass | logo_avoid | base complete |
| F-59 | README.md | done | pass | logo_avoid | base complete |
| F-60 | GitHub | done | pass | local official asset exists | overlay_audit |
| F-61 | Pull Request | done | pass | waiting | overlay_wait |
| F-62 | GitHub Actions | done | pass | waiting | overlay_wait |
| F-71 | ripgrep (rg) | done | pass | logo_avoid | base complete |

## Generated locations

- Prompt briefs: `assets/ponchi/pipeline_prompts/ponchi-batch-009/*.md`
- 2:1 base images: `assets/ponchi/experiments/batches/ponchi-batch-009/*_base_1254x627.png`
- Base audit: `docs/ponchi_batch_audits/ponchi-batch-009-base-image-audit.md`
- Base audit CSV: `ledgers/ponchi_batch_009_base_audit.csv`
- Contact sheet: `docs/ponchi_batch_audits/ponchi-batch-009-base-contact-sheet.png`
- Batch audit: `docs/ponchi_batch_audits/ponchi-batch-009.md`
- Batch report: `ledgers/ponchi_batches/ponchi-batch-009.md`

## Visual QA

Contact sheet review passed for the generated bases. F-37, F-38, and F-60 were
regenerated to reduce text-like marks and real-product-UI risk. The 9
official-logo entries have deterministic blank upper-right logo clearspace for
later official-source compositing.

## Next action

Batch 009 base generation is complete. Wave 003 now has 60 / 60 generated
2:1 bases and 60 / 60 base audit pass. Continue with Wave 004 / Batch 010 next,
or return to official source review and deterministic overlays. Do not promote
anything to `assets/ponchi/final/` without explicit approval.
