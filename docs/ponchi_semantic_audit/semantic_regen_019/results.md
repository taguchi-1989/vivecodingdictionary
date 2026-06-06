# semantic-regen-019 results

Date: 2026-06-06

Purpose: fifth execution batch for the full I/J ponchi rebuild. This batch
rebuilds the browser automation MCP trio with exact distinctions between
cross-browser automation, single-browser scripting, and DevTools diagnostics.

## Scope

| entry | result |
| --- | --- |
| `I-20 Playwright MCP` | staged as cross-browser semantic automation with trace and screenshot artifacts |
| `I-21 Puppeteer MCP` | staged as single-browser click/type/screenshot/scrape/export script flow |
| `I-22 Chrome DevTools MCP` | staged as DevTools diagnostics with elements, console, network, performance, and audit panels |

## Gates

| gate | result |
| --- | --- |
| prompt lint | `ok: 3 file(s)` |
| image audit | `pass=3`, `review=0`, `fail=0` |
| color audit | `pass=3`, `review=0`, `fail=0` |
| quality score | `high=3`, `mid=0`, `low=0` |
| comparison audit | `candidate_ok=3` |

## Comparison Notes

- `I-20` is a multi-browser test runner with trace/screenshot/result artifacts.
- `I-21` is one browser with a vertical script step rail. It is deliberately not
  a cross-browser matrix and not a DevTools panel.
- `I-22` is diagnostic inspection: elements, console rows, network waterfall,
  performance trace, and audit cards.
- Character A is used consistently as the small operator/reviewer. No temporary
  characters were introduced.
- No generated logos, official seals, product UI, readable words, or brand
  colors are accepted in the staged candidates. `I-20` was regenerated because
  the first render contained browser-logo-like marks; `I-21` was regenerated
  because the first render contained a readable `T` icon.

## Artifacts

- Prompts: `assets/ponchi/pipeline_prompts/semantic-regen-019/`
- Generated bases: `assets/ponchi/experiments/batches/semantic-regen-019/`
- Final candidates: `assets/ponchi/final_candidates/semantic-regen-019/`
- Candidate audit: `docs/ponchi_batch_audits/semantic-regen-019-final-candidates.md`
- Image audit: `docs/ponchi_semantic_audit/semantic_regen_019/base_image_audit.md`
- Color audit: `docs/ponchi_semantic_audit/semantic_regen_019/color_audit.md`
- Quality scores: `docs/ponchi_semantic_audit/semantic_regen_019/quality_scores.md`
- Comparison audit: `docs/ponchi_semantic_audit/semantic_regen_019/comparison_audit.csv`
- Candidate update ledger: `ledgers/semantic_regen_019_candidate_update.csv`

## Judgment

`semantic-regen-019` passes as a staged candidate batch for the full I/J
rebuild. No production final image was overwritten. `I-20` required logo-risk
rerender plus palette normalization; `I-21` required text-risk rerender.
