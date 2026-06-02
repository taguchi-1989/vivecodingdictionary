# ponchi-batch-012 progress summary

Target: 20 entries from `G-2` through `G-21`.

## Numeric summary

| stage | count | target |
| --- | ---: | --- |
| prompt briefs created | 20 / 20 | G-2 - G-21 all entries |
| prompt lint pass | 20 / 20 | G-2 - G-21 all entries |
| 2:1 base images created | 20 / 20 | G-2 - G-21 all entries |
| 2:1 base audit pass | 20 / 20 | G-2 - G-21 all entries |
| logo_avoid | 20 / 20 | G-2 - G-21 all entries |
| official logo/icon source review required | 0 / 20 | none |
| overlay_wait | 0 / 20 | none |
| final candidate created | 0 / 20 | not generated |
| final promoted | 0 / 20 | do not copy to `assets/ponchi/final/` yet |

## Entry list

| entry | title | prompt | 2:1 base | logo policy | current status |
| --- | --- | --- | --- | --- | --- |
| G-2 | Token | done | pass | logo_avoid | base complete |
| G-3 | Dictation | done | pass | logo_avoid | base complete |
| G-4 | System Prompt | done | pass | logo_avoid | base complete |
| G-5 | Context Window | done | pass | logo_avoid | base complete |
| G-6 | One-shot | done | pass | logo_avoid | base complete |
| G-7 | 指示追従性 | done | pass | logo_avoid | base complete |
| G-8 | 決定論的／非決定論的 | done | pass | logo_avoid | base complete |
| G-9 | effort レベル | done | pass | logo_avoid | base complete |
| G-10 | Prompt Engineering | done | pass | logo_avoid | base complete |
| G-11 | Context Engineering | done | pass | logo_avoid | base complete |
| G-12 | Agent Design | done | pass | logo_avoid | base complete |
| G-13 | Few-shot Learning | done | pass | logo_avoid | base complete |
| G-14 | Thinking モデル | done | pass | logo_avoid | base complete |
| G-15 | RAG | done | pass | logo_avoid | base complete |
| G-16 | Embedding | done | pass | logo_avoid | base complete |
| G-17 | ベクトル DB | done | pass | logo_avoid | base complete |
| G-18 | Chain of Thought | done | pass | logo_avoid | base complete |
| G-19 | Prompt Caching | done | pass | logo_avoid | base complete |
| G-20 | CLAUDE.md | done | pass | logo_avoid | base complete |
| G-21 | AGENTS.md | done | pass | logo_avoid | base complete |

## Generated locations

- Prompt briefs: `assets/ponchi/pipeline_prompts/ponchi-batch-012/*.md`
- 2:1 base images: `assets/ponchi/experiments/batches/ponchi-batch-012/*_base_1254x627.png`
- Base audit: `docs/ponchi_batch_audits/ponchi-batch-012-base-image-audit.md`
- Base audit CSV: `ledgers/ponchi_batch_012_base_audit.csv`
- Contact sheet: `docs/ponchi_batch_audits/ponchi-batch-012-base-contact-sheet.png`
- Batch audit: `docs/ponchi_batch_audits/ponchi-batch-012.md`
- Batch report: `ledgers/ponchi_batches/ponchi-batch-012.md`

## Visual QA

Contact sheet review passed for all 20 generated bases. G-12, G-16, and G-20
were regenerated to remove robot-face, animal, and concrete-product-like
imagery. G-7, G-13, and G-21 were also regenerated to reduce face-like assistant
icons and keep the batch closer to abstract LLM concept diagrams.

## Next action

Batch 012 base generation is complete. Wave 004 now has 60 / 60 generated
2:1 bases and 60 / 60 base audit pass. Continue with Wave 005 /
`ponchi-batch-013`, or return to official source review and deterministic
overlays. Do not promote anything to `assets/ponchi/final/` without explicit
approval.
