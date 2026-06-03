# ponchi-batch-001 progress summary

Target: 20 entries from `A-1` through `B-9`.

## Numeric summary

| stage | count | target |
| --- | ---: | --- |
| prompt briefs created | 20 / 20 | A-1 - B-9 all entries |
| prompt lint pass | 20 / 20 | A-1 - B-9 all entries |
| 2:1 base images created | 20 / 20 | A-1 - B-9 all entries |
| 2:1 base audit pass | 20 / 20 | A-1 - B-9 all entries |
| logo_avoid | 11 / 20 | A-1 - A-11 |
| official logo/icon source review required or already tracked | 9 / 20 | B-1 - B-9 |
| color_audit | 11 / 20 | A-1 - A-11 |
| overlay_audit | 9 / 20 | B-1, B-2, B-3, B-4, B-5, B-6, B-7, B-8, B-9 |
| overlay_wait | 0 / 20 | none |
| blocked_brand_asset | 0 / 20 | none |
| final candidate created | 20 / 20 | A-1 - A-11 plus all overlay_audit entries |
| color audit pass | 20 / 20 staged candidates | A-1 - B-9 all entries |
| final promoted | 0 / 20 | do not copy to `assets/ponchi/final/` yet |

## Entry list

| entry | title | prompt | 2:1 base | logo policy | current status |
| --- | --- | --- | --- | --- | --- |
| A-1 | まえがき | done | pass | logo_avoid | color_audit |
| A-2 | この本の読み方 | done | pass | logo_avoid | color_audit |
| A-3 | 図鑑の歩き方 | done | pass | logo_avoid | color_audit |
| A-4 | 体験区分の凡例 | done | pass | logo_avoid | color_audit |
| A-5 | 読者レベルの凡例 | done | pass | logo_avoid | color_audit |
| A-6 | 評価日・時変情報の見方 | done | pass | logo_avoid | color_audit |
| A-7 | 図のタイプ | done | pass | logo_avoid | color_audit |
| A-8 | 色・記号の凡例 | done | pass | logo_avoid | color_audit |
| A-9 | 索引 | done | pass | logo_avoid | color_audit |
| A-10 | 更新履歴と更新方針 | done | pass | logo_avoid | color_audit |
| A-11 | 略称表記 | done | pass | logo_avoid | color_audit |
| B-1 | Gemini | done | pass | official overlay/source tracked | overlay_audit |
| B-2 | Claude | done | pass | official overlay/source tracked | base complete; overlay review remains |
| B-3 | ChatGPT | done | pass | official OpenAI wordmark applied | overlay_audit |
| B-4 | Cursor | done | pass | official overlay/source tracked | base complete; overlay review remains |
| B-5 | GitHub Copilot | done | pass | official overlay/source tracked | base complete; overlay review remains |
| B-6 | Windsurf | done | pass | official Windsurf wordmark applied | overlay_audit |
| B-7 | Claude Code | done | pass | official overlay/source tracked | base complete; overlay review remains |
| B-8 | Codex | done | pass | official OpenAI wordmark applied | overlay_audit |
| B-9 | v0 | done | pass | official overlay/source tracked | base complete; overlay review remains |

## Generated locations

- Prompt briefs: `assets/ponchi/pipeline_prompts/ponchi-batch-001/*.md`
- Raw generated images: `assets/ponchi/experiments/batches/ponchi-batch-001/*_base_raw.png`
- 2:1 base images: `assets/ponchi/experiments/batches/ponchi-batch-001/*_base_1254x627.png`
- Base audit: `docs/ponchi_batch_audits/ponchi-batch-001-base-image-audit.md`
- Base audit CSV: `ledgers/ponchi_batch_001_base_audit.csv`
- Contact sheet: `docs/ponchi_batch_audits/ponchi-batch-001-base-contact-sheet.png`
- Batch audit: `docs/ponchi_batch_audits/ponchi-batch-001.md`
- Batch report: `ledgers/ponchi_batches/ponchi-batch-001.md`
- Color recheck: `docs/ponchi_batch_audits/ponchi-batch-001-color-recheck.md`
- Color recheck CSV: `ledgers/ponchi_batch_001_color_recheck.csv`
- Local generator: `scripts/ponchi_generate_batch_001_local.py`

## Visual QA

Contact sheet review passed for all 20 generated bases. A-series entries are
neutral guide/legend/index diagrams. B-series service entries contain no
generated logos, no invented logos, no product UI, no mascot marks, and no
readable text. B-1, B-2, B-3, B-4, B-5, B-6, B-7, B-8, and B-9 were rebuilt or
normalized with the strict white/black/gray/approved-blue body palette and now
pass the mechanical color gate. B-1's official icon was reduced and
repositioned after review to avoid covering the main diagram. B-6 uses the
official Windsurf black wordmark from `https://windsurf.com/brand`; its overlay
remains visual-review required because the spacious logo composition triggered
a density warning. All 20 staged candidates still require normal human visual
confirmation before final promotion.

## Next action

Batch 001 base generation is complete, and all 20 entries are staged as
review-pending candidates. B-6 is no longer blocked; the official Windsurf
wordmark is applied and recorded, but final promotion still requires visual
approval.
