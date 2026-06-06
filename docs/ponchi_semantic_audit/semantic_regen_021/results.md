# semantic-regen-021 results

Date: 2026-06-06

Purpose: seventh execution batch for the full I/J ponchi rebuild. This batch
rebuilds the J chapter training, adaptation, data, model-scale, and generation
mechanics cluster.

## Scope

| entry | result |
| --- | --- |
| `J-16 Fine-tuning` | staged as whole-model behavior adaptation using domain data |
| `J-17 Attention` | staged as token relationship weights and weighted context gathering |
| `J-18 MoE` | staged as sparse router-to-expert selection |
| `J-19 量子化` | staged as model weight compression and memory reduction |
| `J-20 Big Data` | staged as data scale/velocity/variety exceeding a conventional database wall |
| `J-21 LoRA` | staged as frozen base model plus small adapter/difference layers |
| `J-22 パラメータ数の単位` | staged as model-size scale ladder with resource growth |
| `J-23 拡散モデル` | staged as noise-to-image reverse-diffusion workflow |

## Gates

| gate | result |
| --- | --- |
| prompt lint | `ok: 8 file(s)` |
| image audit | `pass=8`, `review=0`, `fail=0` |
| color audit | `pass=8`, `review=0`, `fail=0` |
| quality score | `high=7`, `mid=1`, `low=0` |
| comparison audit | `candidate_ok=8` |

## Comparison Notes

- `J-16` and `J-21` are separated as whole-model update versus frozen model
  plus adapter layers.
- `J-19` and `J-22` are separated as compression versus size scale.
- `J-17` and `J-18` are separated as token attention weights versus router to
  expert selection.
- `J-20` is a data-platform scale motif, not a model learning loop.
- `J-23` is a generation workflow from noise to image, not text-only LLM or VLM
  image understanding.
- `J-18` is the only `mid` quality score. The quieter inactive expert pool is
  accepted as part of the sparse-routing concept.
- `J-17`, `J-19`, and `J-22` were palette-normalized after initial color review.
  Final color audit is `pass=8`.
- No production final image was overwritten.

## Artifacts

- Prompts: `assets/ponchi/pipeline_prompts/semantic-regen-021/`
- Generated bases: `assets/ponchi/experiments/batches/semantic-regen-021/`
- Final candidates: `assets/ponchi/final_candidates/semantic-regen-021/`
- Candidate audit: `docs/ponchi_batch_audits/semantic-regen-021-final-candidates.md`
- Image audit: `docs/ponchi_semantic_audit/semantic_regen_021/base_image_audit.md`
- Color audit: `docs/ponchi_semantic_audit/semantic_regen_021/color_audit.md`
- Quality scores: `docs/ponchi_semantic_audit/semantic_regen_021/quality_scores.md`
- Comparison audit: `docs/ponchi_semantic_audit/semantic_regen_021/comparison_audit.csv`
- Candidate update ledger: `ledgers/semantic_regen_021_candidate_update.csv`

## Judgment

`semantic-regen-021` passes as a staged candidate batch for the full I/J
rebuild. The batch is ready for visual promotion review.
