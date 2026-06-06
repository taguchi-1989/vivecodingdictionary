# Benchmarks review

Date: 2026-06-06

Cluster: `E-benchmarks`
Pass mode: `type_distinction`

## Scope correction

The migration unit originally listed `E-5` and `E-10` - `E-15`, but those entry IDs are not present in `ledgers/entries.csv` or `assets/ponchi/final/`. This review corrects the unit to the actual E chapter benchmark set:

`E-1;E-2;E-3;E-4;E-20;E-21;E-22;E-23;E-24;E-25;E-26;E-27;E-30;E-31;E-32;E-33;E-34;E-50;E-51`

## Judgment

The images work as benchmark-category diagrams. They reliably distinguish coding, knowledge/reasoning, agent/web/OS, and arena-style evaluation. Exact benchmark names inside a close family remain caption-supported rather than visually provable.

## Findings

| group | entries | visual status | action |
| --- | --- | --- | --- |
| Coding benchmarks | `E-1`, `E-2`, `E-3`, `E-4` | Repository patch/test, verified checklist, terminal, and function-test motifs are separated. `E-1` vs `E-2` remains same-family. | keep; same-family exact names are caption-supported |
| Knowledge/reasoning | `E-20`, `E-21`, `E-22`, `E-23`, `E-24`, `E-25`, `E-26`, `E-27` | Broad exam, harder exam, science QA, math word problems, contest math, final exam, and puzzle reasoning are visible. `MMLU` vs `MMLU-Pro` is inherently subtle. | keep; `E-20`/`E-21` exact distinction is caption-supported |
| Agent benchmarks | `E-30`, `E-31`, `E-32`, `E-33`, `E-34` | Transactional tool use, browser task, general assistant, multi-environment agent, and desktop OS control are distinguishable. | keep |
| Arena benchmarks | `E-50`, `E-51` | Pairwise/human-vote leaderboard motif is visible. `Chatbot Arena` and `LMSYS Arena` are related enough that exact identity depends on the caption. | keep; exact name is caption-supported |

## Decision

No regeneration in this unit. The weak cases are honest same-family ambiguities, not low-quality or meaningless density. The important visual burden for this unit is type/category distinction, and that passes.

## Artifacts

- Blind sheet: `docs/ponchi_semantic_audit/benchmarks_2026-06-06/benchmarks_blind_sheet.png`
- Labeled sheet: `docs/ponchi_semantic_audit/benchmarks_2026-06-06/benchmarks_labeled_sheet.png`
- Candidates: `docs/ponchi_semantic_audit/benchmarks_2026-06-06/candidates.csv`
- Answer key: `docs/ponchi_semantic_audit/benchmarks_2026-06-06/answer_key.csv`
- Response template: `docs/ponchi_semantic_audit/benchmarks_2026-06-06/response_template.csv`
