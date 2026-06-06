# semantic-regen-014 results

Date: 2026-06-06

Purpose: regenerate the weak items in `U024 J-law-ethics` without promoting or
overwriting production files under `assets/ponchi/final/`.

## Scope

| entry | result |
| --- | --- |
| `J-50 AI 倫理` | staged as concrete ethics governance controls |
| `J-52 Sycophancy` | staged as over-agreement checked by evaluation/safety gate |
| `J-53 著作権法 30 条の 4（日本）` | staged as legal boundary between analysis/training and protected expression |
| `J-54 ISO/IEC 42001` | staged as AI management-system audit map |

## Gates

| gate | result |
| --- | --- |
| prompt lint | `ok: 4 file(s)` |
| image audit | `pass=4`, `review=0`, `fail=0` |
| color audit | `pass=4`, `review=0`, `fail=0` |
| quality score | `high=4` |

## Artifacts

- Prompts: `assets/ponchi/pipeline_prompts/semantic-regen-014/`
- Generated bases: `assets/ponchi/experiments/batches/semantic-regen-014/`
- Final candidates: `assets/ponchi/final_candidates/semantic-regen-014/`
- Candidate audit: `docs/ponchi_batch_audits/semantic-regen-014-final-candidates.md`
- Image audit: `docs/ponchi_semantic_audit/semantic_regen_014/base_image_audit.md`
- Color audit: `docs/ponchi_semantic_audit/semantic_regen_014/color_audit.md`
- Quality scores: `docs/ponchi_semantic_audit/semantic_regen_014/quality_scores.md`
- U024 review: `docs/ponchi_semantic_audit/law_ethics_2026-06-06/results.md`

## Final Verification

- Semantic migration units: `completed=29`
- Semantic cluster registry: `reviewed=29`
- Final image coverage, entry IDs only: `final_not_in_units=0`,
  `unit_not_in_final=0`

No production final image was overwritten. The four new images remain staged as
review-pending final candidates.
