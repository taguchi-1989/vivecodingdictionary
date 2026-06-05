# AI assistants core review

Date: 2026-06-06

Cluster: `B-ai-assistants-core`
Pass mode: `exact_entry`

## Findings

| entry | title | judgment | action |
| --- | --- | --- | --- |
| `B-1` | Gemini | keep | semantic-regen-003 already passed; multimodal assistant map remains distinct |
| `B-2` | Claude | keep | semantic-regen-003 already passed; long-document/artifact Claude context remains distinct |
| `B-3` | ChatGPT | keep | semantic-regen-003 already passed; chat/GPT/API ecosystem remains distinct |
| `B-10` | Devin | keep | semantic-regen-003 already passed; autonomous issue-to-PR/review loop remains distinct |
| `B-14` | Genspark | keep | semantic-regen-003 already passed; multi-agent report/slides/task flow remains distinct |
| `B-15` | Microsoft Copilot | keep new | semantic-regen-007 general Microsoft assistant candidate reduces M365 confusion |
| `B-16` | Microsoft 365 Copilot | keep new | semantic-regen-007 M365 work graph candidate reduces general Copilot confusion |
| `B-17` | Edge Copilot | keep | browser page plus sidebar remains visually distinct |
| `B-19` | Claude Cowork | recompose | semantic-regen-009 staged as shared workspace/project/connectors/artifacts feature |

## Artifacts

- Blind sheet: `docs/ponchi_semantic_audit/ai_assistants_core_2026-06-06/ai_assistants_core_blind_sheet.png`
- Labeled sheet: `docs/ponchi_semantic_audit/ai_assistants_core_2026-06-06/ai_assistants_core_labeled_sheet.png`
- Candidates: `docs/ponchi_semantic_audit/ai_assistants_core_2026-06-06/candidates.csv`
- Answer key: `docs/ponchi_semantic_audit/ai_assistants_core_2026-06-06/answer_key.csv`
- Response template: `docs/ponchi_semantic_audit/ai_assistants_core_2026-06-06/response_template.csv`

## Next

Use the refreshed blind sheet for any external responder scoring. The current in-thread judgment is that all entries have a distinct visual axis after `semantic-regen-009`, with `B-19` still review-pending because the product name itself is less visually anchored than logo-backed entries.
