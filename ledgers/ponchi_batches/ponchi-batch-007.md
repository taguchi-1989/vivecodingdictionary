# ponchi-batch-007 review

## Gate

- Do not promote any item to final until this batch is reviewed.
- Generate or update scene briefs first, then lint prompts, then generate base images.
- Stop brand entries at `overlay_wait` until official assets are imported and recorded.

## Items

| # | entry | title | stage | logo status | next action | confirmation |
| ---: | --- | --- | --- | --- | --- | --- |
| 1 | `E-3` | Terminal-Bench | `brief_needed` | `logo_avoid` | create benchmark scene brief without logos | `not_reviewed` |
| 2 | `E-4` | HumanEval | `brief_needed` | `logo_avoid` | create benchmark scene brief without logos | `not_reviewed` |
| 3 | `E-20` | MMLU | `brief_needed` | `logo_avoid` | create benchmark scene brief without logos | `not_reviewed` |
| 4 | `E-21` | MMLU-Pro | `brief_needed` | `logo_avoid` | create benchmark scene brief without logos | `not_reviewed` |
| 5 | `E-22` | GPQA | `brief_needed` | `logo_avoid` | create benchmark scene brief without logos | `not_reviewed` |
| 6 | `E-23` | GSM8K | `brief_needed` | `logo_avoid` | create benchmark scene brief without logos | `not_reviewed` |
| 7 | `E-24` | MATH | `brief_needed` | `logo_avoid` | create benchmark scene brief without logos | `not_reviewed` |
| 8 | `E-25` | AIME | `brief_needed` | `logo_avoid` | create benchmark scene brief without logos | `not_reviewed` |
| 9 | `E-26` | Humanity's Last Exam | `brief_needed` | `logo_avoid` | create benchmark scene brief without logos | `not_reviewed` |
| 10 | `E-27` | IQ Bench | `brief_needed` | `logo_avoid` | create benchmark scene brief without logos | `not_reviewed` |
| 11 | `E-30` | TAU-Bench | `brief_needed` | `logo_avoid` | create benchmark scene brief without logos | `not_reviewed` |
| 12 | `E-31` | WebArena | `brief_needed` | `logo_avoid` | create benchmark scene brief without logos | `not_reviewed` |
| 13 | `E-32` | GAIA | `brief_needed` | `logo_avoid` | create benchmark scene brief without logos | `not_reviewed` |
| 14 | `E-33` | AgentBench | `brief_needed` | `logo_avoid` | create benchmark scene brief without logos | `not_reviewed` |
| 15 | `E-34` | OSWorld | `brief_needed` | `logo_avoid` | create benchmark scene brief without logos | `not_reviewed` |
| 16 | `E-50` | Chatbot Arena | `brief_needed` | `logo_avoid` | create benchmark scene brief without logos | `not_reviewed` |
| 17 | `E-51` | LMSYS Arena | `brief_needed` | `logo_avoid` | create benchmark scene brief without logos | `not_reviewed` |
| 18 | `F-1` | JavaScript | `prompt_review` | `logo_avoid` | lint prompt, generate 2:1 base, audit density | `not_reviewed` |
| 19 | `F-2` | TypeScript | `prompt_review` | `logo_avoid` | lint prompt, generate 2:1 base, audit density | `not_reviewed` |
| 20 | `F-3` | Python | `brief_needed` | `logo_avoid` | create language concept scene brief without logos | `not_reviewed` |

## Batch Commands

```powershell
python scripts\ponchi_batch_plan.py --batch-size 20
python scripts\ponchi_batch_report.py ponchi-batch-007
python scripts\ponchi_prompt_lint.py <prompt-files>
```
