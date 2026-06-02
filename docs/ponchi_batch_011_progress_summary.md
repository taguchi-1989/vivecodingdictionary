# ponchi-batch-011 progress summary

Target: 20 entries from `F-123` through `G-1`.

## Numeric summary

| stage | count | target |
| --- | ---: | --- |
| prompt briefs created | 20 / 20 | F-123 - G-1 all entries |
| prompt lint pass | 20 / 20 | F-123 - G-1 all entries |
| 2:1 base images created | 20 / 20 | F-123 - G-1 all entries |
| 2:1 base audit pass | 20 / 20 | F-123 - G-1 all entries |
| logo_avoid | 11 / 20 | F-123, F-130, F-150 - F-152, F-154, F-160 - F-162, F-190, G-1 |
| official logo/icon source review required | 9 / 20 | F-140, F-141, F-153, F-170 - F-172, F-180, F-181, F-200 |
| overlay_wait | 9 / 20 | F-140, F-141, F-153, F-170 - F-172, F-180, F-181, F-200 |
| final candidate created | 0 / 20 | not generated |
| final promoted | 0 / 20 | do not copy to `assets/ponchi/final/` yet |

## Entry list

| entry | title | prompt | 2:1 base | logo policy | current status |
| --- | --- | --- | --- | --- | --- |
| F-123 | ORM | done | pass | logo_avoid | base complete |
| F-130 | OAuth | done | pass | logo_avoid | base complete |
| F-140 | Mermaid | done | pass | waiting | overlay_wait |
| F-141 | PlantUML | done | pass | waiting | overlay_wait |
| F-150 | MIT ライセンス | done | pass | logo_avoid | base complete |
| F-151 | Apache 2.0 | done | pass | logo_avoid | base complete |
| F-152 | GPL | done | pass | logo_avoid | base complete |
| F-153 | Creative Commons | done | pass | waiting | overlay_wait |
| F-154 | OSS | done | pass | logo_avoid | base complete |
| F-160 | DOM | done | pass | logo_avoid | base complete |
| F-161 | SSR | done | pass | logo_avoid | base complete |
| F-162 | SSG | done | pass | logo_avoid | base complete |
| F-170 | EC2 | done | pass | waiting | overlay_wait |
| F-171 | S3 | done | pass | waiting | overlay_wait |
| F-172 | IAM | done | pass | waiting | overlay_wait |
| F-180 | OpenGL | done | pass | waiting | overlay_wait |
| F-181 | WebGL | done | pass | waiting | overlay_wait |
| F-190 | サブルーチン | done | pass | logo_avoid | base complete |
| F-200 | Rust | done | pass | waiting | overlay_wait |
| G-1 | Context (コンテキスト) | done | pass | logo_avoid | base complete |

## Generated locations

- Prompt briefs: `assets/ponchi/pipeline_prompts/ponchi-batch-011/*.md`
- 2:1 base images: `assets/ponchi/experiments/batches/ponchi-batch-011/*_base_1254x627.png`
- Base audit: `docs/ponchi_batch_audits/ponchi-batch-011-base-image-audit.md`
- Base audit CSV: `ledgers/ponchi_batch_011_base_audit.csv`
- Contact sheet: `docs/ponchi_batch_audits/ponchi-batch-011-base-contact-sheet.png`
- Batch audit: `docs/ponchi_batch_audits/ponchi-batch-011.md`
- Batch report: `ledgers/ponchi_batches/ponchi-batch-011.md`

## Visual QA

Contact sheet review passed for all 20 generated bases. F-130 was regenerated
after the first image was too sparse for base density. F-152, F-154, F-161,
F-162, F-170, F-180, and F-200 use regenerated label-free variants to reduce
readable text and brand-like marks. The 9 official-logo entries have
deterministic blank upper-right clearspace for later official-source
compositing.

## Next action

Batch 011 base generation is complete. Wave 004 now has 40 / 60 generated
2:1 bases and 40 / 60 base audit pass. Continue with `ponchi-batch-012`, or
return to official source review and deterministic overlays. Do not promote
anything to `assets/ponchi/final/` without explicit approval.
