# LLM basic concepts review

Date: 2026-06-06

Cluster: `G-llm-basic-concepts`
Pass mode: `type_distinction`

## Judgment

The cluster passes. These are abstract LLM concepts, so exact terms are partially caption-supported, but the diagrams convey distinct structures: context/token/window, instruction layers, determinism/effort, prompt/context/agent techniques, thinking, and RAG.

## Findings

| group | entries | visual status | action |
| --- | --- | --- | --- |
| Core inputs | `G-1`, `G-2`, `G-3`, `G-4`, `G-5` | Context, tokenization, dictation, system prompt, and context window are visually separable by supplied state, token pieces, voice input, instruction layer, and bounded window. | keep |
| Basic behavior controls | `G-6`, `G-7`, `G-8`, `G-9` | One-shot, instruction following, deterministic/non-deterministic output, and effort ladder are differentiated. `G-7` is lower-density but semantically readable. | keep |
| Techniques | `G-10` - `G-15` | Prompt engineering, context engineering, agent design, few-shot learning, thinking model, and RAG each show distinct control/input/retrieval structures. | keep |

## Decision

No regeneration in this unit. Same-family terms remain caption-supported, but the diagrams provide meaningful semantic scaffolding.

## Artifacts

- Blind sheet: `docs/ponchi_semantic_audit/llm_basic_concepts_2026-06-06/llm_basic_concepts_blind_sheet.png`
- Labeled sheet: `docs/ponchi_semantic_audit/llm_basic_concepts_2026-06-06/llm_basic_concepts_labeled_sheet.png`
- Candidates: `docs/ponchi_semantic_audit/llm_basic_concepts_2026-06-06/candidates.csv`
- Answer key: `docs/ponchi_semantic_audit/llm_basic_concepts_2026-06-06/answer_key.csv`
- Response template: `docs/ponchi_semantic_audit/llm_basic_concepts_2026-06-06/response_template.csv`
