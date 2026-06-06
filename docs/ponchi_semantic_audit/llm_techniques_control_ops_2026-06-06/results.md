# LLM techniques, control, and ops review

Date: 2026-06-06

Cluster: `G-llm-techniques-control`
Pass mode: `type_distinction`

## Scope correction

The original migration unit included `G-24`, but that ID is not present in `ledgers/entries.csv` or `assets/ponchi/final/`. This review removes `G-24` and adds current control entries `G-38 Plan Mode` and `G-39 Permission`.

Reviewed IDs:

`G-16;G-17;G-18;G-19;G-20;G-21;G-22;G-23;G-30;G-31;G-32;G-33;G-34;G-35;G-36;G-38;G-39;G-40;G-41;G-42;G-43;G-44;G-45;G-46;G-47`

## Judgment

The cluster passes. Some technique/control items are abstract and same-family, but the diagrams preserve useful operational differences.

## Findings

| group | entries | visual status | action |
| --- | --- | --- | --- |
| Retrieval/vector techniques | `G-16`, `G-17`, `G-18`, `G-19` | Embedding, vector DB, Chain of Thought, and prompt caching differ by vectorization, index/search, reasoning steps, and cached prefix reuse. `G-18`/`G-19` are lower-density but readable. | keep |
| Agent/config files | `G-20`, `G-21`, `G-22`, `G-23` | CLAUDE.md, AGENTS.md, SKILL.md, and settings JSON are distinct enough by file/package/config surface; exact filenames remain caption-supported. | keep |
| Control surfaces | `G-30` - `G-36`, `G-38`, `G-39` | Tool use, hook, slash command, function calling, code interpreter, deep research, artifact, plan mode, and permission each show different control/workflow gates. | keep |
| Ops concepts | `G-40` - `G-47` | Vibe coding, subagent, worktree, orchestration, multi-agent coordination, progressive disclosure, perceived nerf, and auto-compact are visually separated at the workflow level. | keep |

## Decision

No regeneration in this unit. The key fix was scope correction, not image replacement.

## Artifacts

- Blind sheet: `docs/ponchi_semantic_audit/llm_techniques_control_ops_2026-06-06/llm_techniques_control_ops_blind_sheet.png`
- Labeled sheet: `docs/ponchi_semantic_audit/llm_techniques_control_ops_2026-06-06/llm_techniques_control_ops_labeled_sheet.png`
- Candidates: `docs/ponchi_semantic_audit/llm_techniques_control_ops_2026-06-06/candidates.csv`
- Answer key: `docs/ponchi_semantic_audit/llm_techniques_control_ops_2026-06-06/answer_key.csv`
- Response template: `docs/ponchi_semantic_audit/llm_techniques_control_ops_2026-06-06/response_template.csv`
