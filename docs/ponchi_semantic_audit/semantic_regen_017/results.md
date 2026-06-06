# semantic-regen-017 results

Date: 2026-06-06

Purpose: third execution batch for the full I/J ponchi rebuild. This batch
starts the I chapter with MCP core roles and setup entries, including the
previously sparse `I-80` and `I-81` final images.

## Scope

| entry | result |
| --- | --- |
| `I-1 MCP` | staged as a shared connector protocol hub |
| `I-2 MCP Server` | staged as provider-side server bridge with tool/resource drawers |
| `I-3 MCP Client` | staged as host-side caller and connection manager |
| `I-4 MCP Transport` | staged as local-vs-remote communication route comparison |
| `I-5 MCP SDK` | staged as SDK core with registration modules and lifecycle pipes |
| `I-80 自作 MCP のテンプレ` | staged as scaffold starter project with custom module insertion |
| `I-81 MCP の登録・設定` | staged as config registration flow from entries to available tools |

## Gates

| gate | result |
| --- | --- |
| prompt lint | `ok: 7 file(s)` |
| image audit | `pass=7`, `review=0`, `fail=0` |
| color audit | `pass=7`, `review=0`, `fail=0` |
| quality score | `high=7`, `mid=0`, `low=0` |
| comparison audit | `candidate_ok=7` |

## Comparison Notes

- `I-1` is the total protocol view; `I-2` is the provider-side server; `I-3`
  is the host-side caller. The three are no longer generic connector cards.
- `I-4` is separated by route choice: local subprocess route versus remote
  server route.
- `I-5` is separated from `I-80` by SDK internals and lifecycle wrapping,
  while `I-80` is a starter scaffold filled with a custom module.
- `I-81` is separated from both `I-3` and `I-80` by setup action: config
  entries become recognized tool drawers.
- Character A is used consistently as a small operator/developer where human
  workflow clarifies the concept. No temporary characters were introduced.
- No generated logos, official seals, product UI, readable words, or brand
  colors are accepted in the staged candidates.

## Artifacts

- Prompts: `assets/ponchi/pipeline_prompts/semantic-regen-017/`
- Generated bases: `assets/ponchi/experiments/batches/semantic-regen-017/`
- Final candidates: `assets/ponchi/final_candidates/semantic-regen-017/`
- Candidate audit: `docs/ponchi_batch_audits/semantic-regen-017-final-candidates.md`
- Image audit: `docs/ponchi_semantic_audit/semantic_regen_017/base_image_audit.md`
- Color audit: `docs/ponchi_semantic_audit/semantic_regen_017/color_audit.md`
- Quality scores: `docs/ponchi_semantic_audit/semantic_regen_017/quality_scores.md`
- Comparison audit: `docs/ponchi_semantic_audit/semantic_regen_017/comparison_audit.csv`
- Candidate update ledger: `ledgers/semantic_regen_017_candidate_update.csv`

## Judgment

`semantic-regen-017` passes as a staged candidate batch for the full I/J
rebuild. No production final image was overwritten. `I-5` required palette
normalization after the first color audit review, then passed the final color
gate. `I-80` and `I-81` specifically address the prior sparse/card-only final
problem.
