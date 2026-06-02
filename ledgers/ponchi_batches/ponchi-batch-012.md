# ponchi-batch-012 review

## Gate

- Do not promote any item to final until this batch is reviewed.
- Generate or update scene briefs first, then lint prompts, then generate base images.
- Stop brand entries at `overlay_wait` until official assets are imported and recorded.

## Items

| # | entry | title | stage | logo status | next action | confirmation |
| ---: | --- | --- | --- | --- | --- | --- |
| 1 | `G-2` | Token | `brief_needed` | `logo_avoid` | generate generic tokenization scene; no AI-company logos | `not_reviewed` |
| 2 | `G-3` | Dictation | `brief_needed` | `logo_avoid` | generate generic speech-to-text workflow; no app logos | `not_reviewed` |
| 3 | `G-4` | System Prompt | `brief_needed` | `logo_avoid` | generate generic instruction hierarchy scene; no model/provider logos | `not_reviewed` |
| 4 | `G-5` | Context Window | `brief_needed` | `logo_avoid` | generate generic context capacity scene; no model/provider logos | `not_reviewed` |
| 5 | `G-6` | One-shot | `brief_needed` | `logo_avoid` | generate one-example learning scene; no model/provider logos | `not_reviewed` |
| 6 | `G-7` | 指示追従性 | `brief_needed` | `logo_avoid` | generate instruction-following evaluation scene; no model/provider logos | `not_reviewed` |
| 7 | `G-8` | 決定論的／非決定論的 | `brief_needed` | `logo_avoid` | generate deterministic versus nondeterministic output comparison; no model/provider logos | `not_reviewed` |
| 8 | `G-9` | effort レベル | `brief_needed` | `logo_avoid` | generate reasoning effort control scene; no model/provider logos | `not_reviewed` |
| 9 | `G-10` | Prompt Engineering | `brief_needed` | `logo_avoid` | generate prompt refinement workflow; no model/provider logos | `not_reviewed` |
| 10 | `G-11` | Context Engineering | `brief_needed` | `logo_avoid` | generate context assembly workflow; no model/provider logos | `not_reviewed` |
| 11 | `G-12` | Agent Design | `brief_needed` | `logo_avoid` | generate agent planning architecture scene; no model/provider logos | `not_reviewed` |
| 12 | `G-13` | Few-shot Learning | `brief_needed` | `logo_avoid` | generate multiple-example learning scene; no model/provider logos | `not_reviewed` |
| 13 | `G-14` | Thinking モデル | `brief_needed` | `logo_avoid` | generate hidden reasoning/workspace scene; no model/provider logos | `not_reviewed` |
| 14 | `G-15` | RAG | `brief_needed` | `logo_avoid` | generate retrieval-augmented generation scene; no model/provider logos | `not_reviewed` |
| 15 | `G-16` | Embedding | `brief_needed` | `logo_avoid` | generate vector embedding scene; no model/provider logos | `not_reviewed` |
| 16 | `G-17` | ベクトル DB | `brief_needed` | `logo_avoid` | generate vector database search scene; no database/product logos | `not_reviewed` |
| 17 | `G-18` | Chain of Thought | `brief_needed` | `logo_avoid` | generate step-by-step reasoning chain scene; no model/provider logos | `not_reviewed` |
| 18 | `G-19` | Prompt Caching | `brief_needed` | `logo_avoid` | generate reusable prompt-cache scene; no model/provider logos | `not_reviewed` |
| 19 | `G-20` | CLAUDE.md | `brief_needed` | `logo_avoid` | generate generic agent instruction file scene; no Claude or Anthropic logos | `not_reviewed` |
| 20 | `G-21` | AGENTS.md | `brief_needed` | `logo_avoid` | generate generic multi-agent instruction file scene; no product logos | `not_reviewed` |

## Batch Commands

```powershell
python scripts\ponchi_batch_plan.py --batch-size 20
python scripts\ponchi_batch_report.py ponchi-batch-012
python scripts\ponchi_prompt_lint.py <prompt-files>
```
