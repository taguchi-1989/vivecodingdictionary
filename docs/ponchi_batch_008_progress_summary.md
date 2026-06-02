# ponchi-batch-008 progress summary

対象: `F-4` から `F-36` までの 20 件。

## 数字サマリー

| 段階 | 件数 | 対象 |
| --- | ---: | --- |
| prompt 作成済み | 20 / 20 | F-4 - F-36 全件 |
| prompt lint pass | 20 / 20 | F-4 - F-36 全件 |
| 2:1 base 作成済み | 20 / 20 | F-4 - F-36 全件 |
| 2:1 base audit pass | 20 / 20 | F-4 - F-36 全件 |
| logo_avoid | 6 / 20 | F-4 - F-9 |
| 公式ロゴ/公式アイコン要確認 | 14 / 20 | F-10 - F-17, F-20, F-21, F-30, F-34 - F-36 |
| overlay_wait | 14 / 20 | F-10 - F-17, F-20, F-21, F-30, F-34 - F-36 |
| final candidate 化済み | 0 / 20 | 未生成 |
| final 昇格済み | 0 / 20 | まだ `assets/ponchi/final/` へはコピーしない |

## Entry 一覧

| entry | title | prompt | 2:1 base | logo policy | current status |
| --- | --- | --- | --- | --- | --- |
| F-4 | HTML | done | pass | logo_avoid | base complete |
| F-5 | CSS | done | pass | logo_avoid | base complete |
| F-6 | Markdown | done | pass | logo_avoid | base complete |
| F-7 | YAML | done | pass | logo_avoid | base complete |
| F-8 | JSON | done | pass | logo_avoid | base complete |
| F-9 | SVG | done | pass | logo_avoid | base complete |
| F-10 | React | done | pass | waiting | overlay_wait |
| F-11 | Next.js | done | pass | waiting | overlay_wait |
| F-12 | Electron | done | pass | waiting | overlay_wait |
| F-13 | Tauri | done | pass | waiting | overlay_wait |
| F-14 | three.js | done | pass | waiting | overlay_wait |
| F-15 | shadcn/ui | done | pass | waiting | overlay_wait |
| F-16 | Tailwind CSS | done | pass | waiting | overlay_wait |
| F-17 | Astro | done | pass | waiting | overlay_wait |
| F-20 | ESLint | done | pass | waiting | overlay_wait |
| F-21 | Prettier | done | pass | waiting | overlay_wait |
| F-30 | VS Code | done | pass | waiting | overlay_wait |
| F-34 | VS Code 拡張機能 | done | pass | waiting | overlay_wait |
| F-35 | Markdown Preview Enhanced | done | pass | waiting | overlay_wait |
| F-36 | Git Graph | done | pass | waiting | overlay_wait |

## Generated locations

- Prompt briefs: `assets/ponchi/pipeline_prompts/ponchi-batch-008/*.md`
- 2:1 base images: `assets/ponchi/experiments/batches/ponchi-batch-008/*_base_1254x627.png`
- Base audit: `docs/ponchi_batch_audits/ponchi-batch-008-base-image-audit.md`
- Contact sheet: `docs/ponchi_batch_audits/ponchi-batch-008-base-contact-sheet.png`
- Batch audit: `docs/ponchi_batch_audits/ponchi-batch-008.md`
- Batch report: `ledgers/ponchi_batches/ponchi-batch-008.md`

## Visual QA

Contact sheet review passed for the generated bases. F-12, F-30, and F-34 were
regenerated to reduce OS-logo, real-editor-UI, and known-service-icon risk.
The 14 overlay-wait entries have deterministic blank upper-right logo
clearspace for later official-source compositing.

## Next action

Batch 008 base generation is complete. Wave 003 is now 40 / 60 generated
2:1 bases and 40 / 60 base audit pass. Continue with Batch 009 next.
Do not promote anything to `assets/ponchi/final/` without explicit approval.
