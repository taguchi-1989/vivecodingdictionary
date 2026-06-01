# ponchi-batch-001 B-focus audit summary

## Scope

A-1 through A-11 are parked for later review. This pass focuses on B-1 through B-9, especially density, 2:1 framing, and logo clearspace drift.

## Selected Base Contact Sheet

`assets/ponchi/experiments/batches/ponchi-batch-001-b-focus/selected_base_contact_sheet.png`

## Overlay Candidate Contact Sheet

`assets/ponchi/experiments/batches/ponchi-batch-001-b-focus/overlay_candidates_contact_sheet.png`

## Automated Base Audit

Command output is recorded in:

- `ledgers/ponchi_b_focus_selected_base_audit.csv`
- `docs/ponchi_batch_audits/ponchi-batch-001-b-focus-selected-base.md`

All selected base images passed:

- size: `1254x627`
- `bbox_coverage >= 0.50`
- `clearspace_ink_ratio <= 0.015`

## Item Decisions

| entry | selected file | base audit | logo status | decision |
| --- | --- | --- | --- | --- |
| `B-1` Gemini | `B-1_base_selected_1254x627.png` | pass | official Gemini asset not confirmed | `overlay_wait` |
| `B-2` Claude | `B-2_base_selected_1254x627.png` / `B-2_claude_overlay_candidate_1254x627.png` | pass | official Claude logo imported and overlaid | `overlay_audit` |
| `B-3` ChatGPT | `B-3_base_selected_1254x627.png` | pass | exact ChatGPT/OpenAI asset choice pending | `overlay_wait` |
| `B-4` Cursor | `B-4_base_selected_1254x627.png` / `B-4_cursor_overlay_candidate_1254x627.png` | pass | official Cursor lockup imported and overlaid | `overlay_audit` |
| `B-5` GitHub Copilot | `B-5_base_selected_1254x627.png` / `B-5_overlay_selected_1254x627.png` | base pass | official GitHub Copilot lockup already applied | `overlay_audit` |
| `B-6` Windsurf | `B-6_base_selected_1254x627.png` | pass | official Windsurf asset not confirmed | `blocked_brand_asset` |
| `B-7` Claude Code | `B-7_base_selected_1254x627.png` / `B-7_claude_code_overlay_candidate_1254x627.png` | pass | official Claude Code logo imported and overlaid | `overlay_audit` |
| `B-8` Codex | `B-8_base_selected_1254x627.png` | pass | exact Codex/OpenAI asset choice pending | `overlay_wait` |
| `B-9` v0 | `B-9_base_selected_1254x627.png` / `B-9_v0_overlay_candidate_1254x627.png` | pass | official v0 logo imported and overlaid with adjusted 180px placement | `overlay_audit` |

## Imported Official Assets

| brand | source | local asset |
| --- | --- | --- |
| Claude | `https://anthropic.com/press-kit` | `assets/logos/anthropic/anthropic-media-resources/Anthropic media resources/Anthropic logos/Claude logos/1 Claude logo/PNG/Claude logo - Slate.png` |
| Claude Code | `https://anthropic.com/press-kit` | `assets/logos/anthropic/anthropic-media-resources/Anthropic media resources/Anthropic logos/Claude logos/2 Claude Code logo/PNG/Claude Code logo - Slate.png` |
| Cursor | `https://cursor.com/brand` | `assets/logos/cursor/cursor-brand-assets/General Logos/Lockup Horizontal/PNG/LOCKUP_HORIZONTAL_2D_LIGHT.png` |
| v0 | `https://vercel.com/design/brands` | `assets/logos/vercel/v0-assets/v0/Light/v0-logo-light.png` |

## Rejected / Superseded Attempts

- B-1/B-2/B-3/B-8 first brand-base trials had clean logo spaces but too much empty canvas by the new bbox gate.
- B-6 first generated base had enough density but polluted the upper-right logo clearspace.
- B-2/B-3/B-8 v2/v3 attempts improved density but were regenerated again when clearspace ink exceeded the `0.015` threshold.

## Next Gate

Do not promote these images to `assets/ponchi/final/` yet. B-2, B-4, B-5, B-7, and B-9 are staged as review-pending final candidates. B-1, B-3, B-6, and B-8 remain blocked or waiting on exact official asset decisions.
