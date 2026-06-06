# semantic-regen-024 results

Date: 2026-06-06

Purpose: tenth execution batch for the full I/J ponchi rebuild. This batch
rebuilds the J chapter GUI and operating-system ecosystem cluster.

## Scope

| entry | result |
| --- | --- |
| `J-90 GUI` | staged as visual controls and pointer operation map |
| `J-92 Linux` | staged as kernel-centered operating-system architecture stack |
| `J-93 Ubuntu` | staged as practical Linux distribution usage/deployment map |

## Gates

| gate | result |
| --- | --- |
| prompt lint | `ok: 3 file(s)` |
| image audit | `pass=3`, `review=0`, `fail=0` |
| color audit | `pass=3`, `review=0`, `fail=0` |
| quality score | `high=3`, `mid=0`, `low=0` |
| comparison audit | `candidate_ok=3` |

## Comparison Notes

- `J-90` is visual operation through generic GUI controls, not an operating
  system diagram.
- `J-92` is Linux as kernel-centered architecture and OS layers, not a specific
  distribution setup.
- `J-93` is Ubuntu as a practical distribution across desktop, host shell, cloud,
  and package-update workflow. Official Ubuntu marks and brand colors are
  intentionally absent.
- `J-93` first render was rejected for brand-like icons. The staged candidate is
  the rerendered non-branded version.
- `J-92` was palette-normalized after initial color review. Final color audit is
  `pass=3`.
- Character policy for this batch is diagram-only. No recurring character is
  used because the cluster distinctions depend on interaction controls,
  operating-system layers, and distribution deployment structures.
- No production final image was overwritten.

## Artifacts

- Prompts: `assets/ponchi/pipeline_prompts/semantic-regen-024/`
- Generated bases: `assets/ponchi/experiments/batches/semantic-regen-024/`
- Final candidates: `assets/ponchi/final_candidates/semantic-regen-024/`
- Candidate audit: `docs/ponchi_batch_audits/semantic-regen-024-final-candidates.md`
- Image audit: `docs/ponchi_semantic_audit/semantic_regen_024/base_image_audit.md`
- Color audit: `docs/ponchi_semantic_audit/semantic_regen_024/color_audit.md`
- Quality scores: `docs/ponchi_semantic_audit/semantic_regen_024/quality_scores.md`
- Comparison audit: `docs/ponchi_semantic_audit/semantic_regen_024/comparison_audit.csv`
- Candidate update ledger: `ledgers/semantic_regen_024_candidate_update.csv`

## Judgment

`semantic-regen-024` passes as a staged candidate batch for the full I/J
rebuild. The batch is ready for visual promotion review.
