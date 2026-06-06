# semantic-regen-018 results

Date: 2026-06-06

Purpose: fourth execution batch for the full I/J ponchi rebuild. This batch
rebuilds I chapter MCP tool-domain entries where the old finals were generally
thin and needed stronger domain-specific visual axes.

## Scope

| entry | result |
| --- | --- |
| `I-10 Filesystem MCP` | staged as local file permission gate with allowed/blocked folders |
| `I-11 GitHub MCP` | staged as remote repository issue/PR/code-search operation board |
| `I-12 Git MCP` | staged as scoped local git branch/diff/commit workflow |
| `I-13 Slack MCP` | staged as team chat channel/thread summary and posting workflow |
| `I-23 Serena MCP` | staged as symbol/LSP code navigation and focused context tray |
| `I-24 Context7 MCP` | staged as stale-memory to current-docs lookup flow |
| `I-30 Notion MCP` | staged as workspace pages/database/comment integration |
| `I-41 SQLite MCP` | staged as local DB query transform and table-result workflow |
| `I-50 AWS MCP` | staged as cloud-resource MCP server cluster and fanout |

## Gates

| gate | result |
| --- | --- |
| prompt lint | `ok: 9 file(s)` |
| image audit | `pass=9`, `review=0`, `fail=0` |
| color audit | `pass=9`, `review=0`, `fail=0` |
| quality score | `high=9`, `mid=0`, `low=0` |
| comparison audit | `candidate_ok=9` |

## Comparison Notes

- `I-10`, `I-12`, and `I-41` are separated by folder permission gate, local
  git graph/diff/commit, and local DB cylinder/table results.
- `I-11` is remote repository operations, not local git. `I-13` is team chat,
  not issue/PR workflow.
- `I-23` is codebase symbol navigation, while `I-24` is fresh documentation
  lookup. Both avoid turning into generic search boxes.
- `I-30` is workspace pages/database/comments, while `I-41` is raw local DB
  query. `I-50` is cloud-resource fanout and does not use AWS marks or colors.
- Character A is used consistently as a small operator/developer. No temporary
  characters were introduced.
- No generated logos, official seals, product UI, readable words, or brand
  colors are accepted in the staged candidates. `I-12` was regenerated because
  the first render contained a readable `VS` mark.

## Artifacts

- Prompts: `assets/ponchi/pipeline_prompts/semantic-regen-018/`
- Generated bases: `assets/ponchi/experiments/batches/semantic-regen-018/`
- Final candidates: `assets/ponchi/final_candidates/semantic-regen-018/`
- Candidate audit: `docs/ponchi_batch_audits/semantic-regen-018-final-candidates.md`
- Image audit: `docs/ponchi_semantic_audit/semantic_regen_018/base_image_audit.md`
- Color audit: `docs/ponchi_semantic_audit/semantic_regen_018/color_audit.md`
- Quality scores: `docs/ponchi_semantic_audit/semantic_regen_018/quality_scores.md`
- Comparison audit: `docs/ponchi_semantic_audit/semantic_regen_018/comparison_audit.csv`
- Candidate update ledger: `ledgers/semantic_regen_018_candidate_update.csv`

## Judgment

`semantic-regen-018` passes as a staged candidate batch for the full I/J
rebuild. No production final image was overwritten. `I-11` and `I-50` required
palette normalization before the final color pass. `I-12` required one rerender
to remove readable text from the comparison marker.
