# semantic-regen-016 results

Date: 2026-06-06

Purpose: second execution batch for the full I/J ponchi rebuild. This batch
finishes the remaining J hardware accelerator, processor, memory, and storage
interface outliers after `semantic-regen-015`.

## Scope

| entry | result |
| --- | --- |
| `J-70 VRAM` | staged as GPU-local memory banks around an accelerator die |
| `J-71 RAM` | staged as CPU-connected DIMM main memory |
| `J-74 RTX シリーズ` | staged as a fan-cooled consumer graphics-card lineup |
| `J-75 Tensor コア` | staged as matrix compute tiles inside a chip |
| `J-76 CPU` | staged as central processor package with instruction, memory, and I/O lanes |
| `J-77 GPU (概念)` | staged as massively parallel compute lanes |
| `J-80 SATA` | staged as a cable-and-port storage interface |
| `J-81 M.2` | staged as a direct motherboard stick slot |

## Gates

| gate | result |
| --- | --- |
| prompt lint | `ok: 8 file(s)` |
| image audit | `pass=8`, `review=0`, `fail=0` |
| color audit | `pass=8`, `review=0`, `fail=0` |
| quality score | `high=4`, `mid=4`, `low=0` |
| comparison audit | `candidate_ok=4`, `candidate_ok_mid_review=4` |

## Comparison Notes

- `J-70` and `J-71` are separated by GPU-local memory banks versus CPU/DIMM
  main memory.
- `J-74`, `J-75`, and `J-77` are separated by consumer card lineup, internal
  tensor compute tiles, and concept-level parallel GPU lanes.
- `J-76` is separated from GPU/Tensor/RAM/storage by central instruction,
  memory, and I/O coordination.
- `J-80` and `J-81` are separated by SATA cable/port interface versus direct
  M.2 motherboard stick slot.
- No characters are used in this batch. The entries are physical hardware and
  interface concepts, so diagram-only composition is the right character policy.
- No generated logos, official seals, product UI, readable words, or brand
  colors are accepted in the staged candidates.

## Artifacts

- Prompts: `assets/ponchi/pipeline_prompts/semantic-regen-016/`
- Generated bases: `assets/ponchi/experiments/batches/semantic-regen-016/`
- Final candidates: `assets/ponchi/final_candidates/semantic-regen-016/`
- Candidate audit: `docs/ponchi_batch_audits/semantic-regen-016-final-candidates.md`
- Image audit: `docs/ponchi_semantic_audit/semantic_regen_016/base_image_audit.md`
- Color audit: `docs/ponchi_semantic_audit/semantic_regen_016/color_audit.md`
- Quality scores: `docs/ponchi_semantic_audit/semantic_regen_016/quality_scores.md`
- Comparison audit: `docs/ponchi_semantic_audit/semantic_regen_016/comparison_audit.csv`
- Candidate update ledger: `ledgers/semantic_regen_016_candidate_update.csv`

## Judgment

`semantic-regen-016` passes as a staged candidate batch for the full I/J
rebuild. No production final image was overwritten. `J-75`, `J-77`, `J-80`,
and `J-81` remain mid-score visual-review rows due density/contrast, but all
four pass image, color, and comparison gates. `J-81` was regenerated from the
first low-quality attempt and then palette-normalized before staging.
