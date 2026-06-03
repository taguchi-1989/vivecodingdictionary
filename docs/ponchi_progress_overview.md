# Ponchi regeneration progress overview

Goal: regenerate all 350 ponchi images as meaningful 2:1 illustrations, and
apply official logos or official icons only after source review and deterministic
post-compositing.

## Current totals

Authoritative sources:

- Entries: `ledgers/entries.csv`
- Pipeline ledger: `ledgers/ponchi_generation_batches.csv`
- Brand source audit: `docs/brand_usage_audit.md`
- Batch dashboard: `docs/ponchi_pipeline_dashboard.html`

| metric | count |
| --- | ---: |
| total active entries | 350 |
| current 20-item batches | 18 |
| wave size target | 60 |
| wave count target | 6 waves, final wave may be shorter |

## Chapter counts

| chapter | count |
| --- | ---: |
| A | 11 |
| B | 40 |
| C | 29 |
| D | 38 |
| E | 19 |
| F | 82 |
| G | 40 |
| H | 22 |
| I | 19 |
| J | 50 |

## Current pipeline stage counts

| stage | count |
| --- | ---: |
| `color_audit` | 214 |
| `overlay_wait` | 3 |
| `overlay_audit` | 133 |

## Latest 2:1 Base Progress

| scope | generated bases | base audit pass | note |
| --- | ---: | ---: | --- |
| `ponchi-batch-001` | 20 / 20 | 20 / 20 | base complete; 11 entries are `logo_avoid`, 9 overlays in `overlay_audit`, 0 remain `overlay_wait` |
| `ponchi-batch-002` | 20 / 20 | 20 / 20 | base complete; 18 overlays in `overlay_audit`, 1 entry remains `overlay_wait`, B-19 is confirmed logo-less in `color_audit` |
| `ponchi-batch-003` | 20 / 20 | 20 / 20 | base complete; 19 overlays in `overlay_audit`, 1 entry remains `overlay_wait` |
| `ponchi-batch-004` | 20 / 20 | 20 / 20 | base complete; 8 overlays in `overlay_audit`, 1 entry remains `overlay_wait`, 11 are `logo_avoid` |
| `ponchi-batch-005` | 20 / 20 | 20 / 20 | base complete; 20 overlays in `overlay_audit`, 0 remain `overlay_wait` |
| `ponchi-batch-006` | 20 / 20 | 20 / 20 | base complete; 17 overlays in `overlay_audit`, 0 remain `overlay_wait`, 3 are `logo_avoid`; D-56 is confirmed logo-less after Seedance source review |
| Wave 002 | 60 / 60 | 60 / 60 | Batches 004-006 base complete; official review/overlay remains |
| `ponchi-batch-007` | 20 / 20 | 20 / 20 | base complete; 20 entries are `logo_avoid` |
| `ponchi-batch-008` | 20 / 20 | 20 / 20 | base complete; 14 overlays in `overlay_audit`, 6 are `logo_avoid`, 0 remain `overlay_wait` |
| `ponchi-batch-009` | 20 / 20 | 20 / 20 | base complete; 9 overlays in `overlay_audit`, 11 are `logo_avoid`, 0 remain `overlay_wait` |
| Wave 003 | 60 / 60 | 60 / 60 | Batches 007-009 base complete; official review/overlay remains |
| `ponchi-batch-010` | 20 / 20 | 20 / 20 | base complete; 10 overlays in `overlay_audit`, 10 are `logo_avoid` / confirmed logo-less |
| `ponchi-batch-011` | 20 / 20 | 20 / 20 | base complete; 9 overlays in `overlay_audit`, 11 are `logo_avoid` |
| `ponchi-batch-012` | 20 / 20 | 20 / 20 | base complete; 20 entries are `logo_avoid` |
| Wave 004 | 60 / 60 | 60 / 60 | Batches 010-012 base complete; official review/overlay remains |
| `ponchi-batch-013` | 20 / 20 | 20 / 20 | base complete; 20 entries are `logo_avoid` |
| `ponchi-batch-014` | 20 / 20 | 20 / 20 | base complete; 20 entries are `logo_avoid` |
| `ponchi-batch-015` | 20 / 20 | 20 / 20 | base complete; 20 entries are `logo_avoid` |
| Wave 005 | 60 / 60 | 60 / 60 | Batches 013-015 base complete; no official overlays required |
| `ponchi-batch-016` | 20 / 20 | 20 / 20 | base complete; 20 entries are `logo_avoid` |
| `ponchi-batch-017` | 20 / 20 | 20 / 20 | base complete; 20 entries are `logo_avoid` |
| `ponchi-batch-018` | 10 / 10 | 10 / 10 | base complete; 10 entries are `logo_avoid` |
| Wave 006 | 50 / 50 | 50 / 50 | Batches 016-018 base complete; no official overlays required |
| Numerically tracked base total | 350 / 350 | 350 / 350 | Batches 001-018 all have generated 2:1 bases and base audit pass |

## Wave map

| wave | batches | entries | primary focus | status |
| --- | --- | ---: | --- | --- |
| Wave 001 | `ponchi-batch-001` - `ponchi-batch-003` | 60 | finish B logo pipeline, classify Batch 003, generate first all-chapter base set | base_complete_overlay_active |
| Wave 002 | `ponchi-batch-004` - `ponchi-batch-006` | 60 | all non-B chapters in ledger order, 2:1 base and brand decisions | base_complete |
| Wave 003 | `ponchi-batch-007` - `ponchi-batch-009` | 60 | all non-B chapters in ledger order, 2:1 base and brand decisions | base_complete |
| Wave 004 | `ponchi-batch-010` - `ponchi-batch-012` | 60 | F-heavy batch generation and audit | base_complete |
| Wave 005 | `ponchi-batch-013` - `ponchi-batch-015` | 60 | F/G/I coverage and logo decisions | base_complete |
| Wave 006 | `ponchi-batch-016` - `ponchi-batch-018` | 50 | remaining chapters completion and final cleanup | base_complete |
| Overlay cleanup | B-service batches and earlier overlay_wait rows | varies | official logo source review, deterministic overlay, final-candidate review | active |

## Overlay Cleanup Progress

| metric | count |
| --- | ---: |
| official logo overlays in `overlay_audit` | 133 |
| non-brand base candidates in `color_audit` | 214 |
| review-pending final candidates staged | 347 |
| remaining `overlay_wait` rows | 3 |
| remaining `official_logo_source_available_needs_import` rows | 0 |
| remaining `blocked_brand_asset` rows | 0 |

## Color Policy Gate

Color-policy status is tracked separately from `overlay_audit`. `overlay_audit`
means the structural overlay candidate exists; it does not prove the generated
body illustration follows the strict white/black/gray/approved-blue palette.

Latest audit command:

```powershell
& 'C:\Users\tgch1\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' scripts/ponchi_color_audit.py --manifest-root assets/ponchi/final_candidates --out-csv ledgers/ponchi_color_audit.csv --out-md docs/ponchi_color_audit_summary.md --contact-sheet docs/ponchi_batch_audits/ponchi-color-audit-contact-sheet.png
```

| color gate status | count |
| --- | ---: |
| `color_audit_pass` | 347 |
| `color_audit_review` | 0 |
| `color_audit_fail` | 0 |

Current color-gate artifacts:

- `docs/ponchi_color_acceptance_gate.md`
- `ledgers/ponchi_color_audit.csv`
- `docs/ponchi_color_audit_summary.md`
- `docs/ponchi_batch_audits/ponchi-color-audit-contact-sheet.png`

All 347 staged final candidates now pass the mechanical color gate. This
includes 133 official-overlay candidates and 214 non-brand base candidates.
The non-brand candidates were normalized to the strict body palette after an
intermediate audit found 137 failures and 47 review rows. Batch 001 service
candidates were rebuilt with the strict body palette. D-51 Imagen and D-60
AlphaGo were rebuilt as strict-palette local diagrams instead of
photo/natural-color compositions. Remaining work is official-source overlay
cleanup for `overlay_wait` rows and human visual review before any final
promotion. B-6 Windsurf was unblocked after confirming the official Windsurf
brand page and applying the official black wordmark as a deterministic overlay.
F-85 SuperClaude Framework was moved to the non-brand `color_audit` lane after
official repository review found no SuperClaude-specific logo, icon, or lockup.
B-19 Claude Cowork and D-56 Seedance were also moved to the non-brand
`color_audit` lane after official source review found no distinct product
logo suitable for deterministic overlay; D-56's base was palette-normalized
before restaging.

Latest overlay pass:

- `ponchi-batch-001`: B-1 Gemini, B-3 ChatGPT, B-6 Windsurf, and B-8 Codex deterministic official overlays staged as review-pending candidates. B-6 uses the official Windsurf black wordmark from `https://windsurf.com/brand`; the base was palette-normalized, and the overlay remains visual-review required because density was accepted with a warning for the spacious logo composition.
- `ponchi-batch-002`: B-10 Devin, B-14 Genspark, B-15 Microsoft Copilot, B-16 Microsoft 365 Copilot, B-17 Edge Copilot, B-18 Aqua Voice, B-24 Google Cloud, B-25 Azure, B-26 Azure OpenAI, and B-27 Vertex AI deterministic official overlays staged as review-pending candidates. B-15 uses the official Copilot icon extracted from `copilot.microsoft.com`; B-16 and B-17 use the same official Copilot-family icon because dedicated Microsoft 365 Copilot / Edge Copilot lockups were not confirmed locally. These three remain product-logo review-pending before final promotion. B-18 uses the official Aqua Voice favicon from the official homepage; a standalone Aqua Voice lockup was not confirmed. B-19 Claude Cowork is staged as a logo-less base candidate because official sources use Claude Team / Team plan language and no distinct `Claude Cowork` product logo was confirmed; do not apply a generic Claude or Anthropic logo.
- `ponchi-batch-003`: B-30, B-31, B-32, B-33, B-40, B-41, B-50, B-51, B-52, B-60, B-61, C-1, C-2, C-3, C-4, C-5, C-6, C-7, and C-9 deterministic official overlays staged as review-pending candidates. B-33 Canva uses the official Canva type logo from Canva's developer brand package. B-61 uses the official ACE-Step logo from the official GitHub repo and preserves the black-square artwork unchanged. C-4 Meta AI uses a Chrome-rendered PNG from the official Meta AI SVG because ImageMagick rendered that SVG blank/white.
- `ponchi-batch-004`: C-10 Moonshot AI, C-11 Z.ai, C-13 Groq, C-14 AMD, C-80 AI大学, C-81 にゃんた, C-82 まさお, and C-83 AI の羅針盤 deterministic official overlays staged as review-pending candidates. C-80 - C-83 use official YouTube channel avatars as official icon overlays. C-83's source page displays `AI時代の羅針盤`, while the ledger title remains `AI の羅針盤`; keep that naming mismatch as a final-review note. C-10 still shows `review` in the Batch 004 overlay image audit because its clearspace ink is high; do not promote it without visual review.
- `ponchi-batch-006`: D-42 Gemma, D-43 Qwen, D-44 Kimi, D-45 GLM, D-46 DeepSeek V3, D-47 DeepSeek R1, D-51 Imagen, D-53 Veo, D-54 Stable Diffusion, D-55 Nano Banana, D-57 Flow, D-58 Whisk, and D-70 Amical deterministic official overlays staged as review-pending candidates. D-45 uses the official Z.ai icon as a developer/organization overlay; a dedicated GLM product logo was not confirmed. D-54 uses the official Stability AI organization logo on an approved-blue plate; a dedicated Stable Diffusion product logo was not confirmed. D-55 uses the official Gemini sparkle as a Gemini-family overlay; a dedicated Nano Banana product logo was not confirmed. D-56 Seedance is staged as a logo-less, palette-normalized base candidate because the official Seedance page did not confirm a distinct Seedance product logo or lockup. D-57 uses the official Google Flow favicon on an approved-blue plate; a standalone Flow lockup was not confirmed. D-58 uses the official Google Labs Whisk favicon; a standalone Whisk lockup was not confirmed. D-70 uses the official Amical GitHub/website app icon; its entry prose still conflicts with the official local-first dictation app source and needs final-review reconciliation.
- `ponchi-batch-005`: D-1 - D-4, D-10 - D-14, D-20 - D-26, D-30, D-35, and D-41 deterministic official overlays staged as review-pending candidates.
- `ponchi-batch-005`: D-40 Llama 系 deterministic official Meta organization icon overlay staged as a review-pending candidate from the official Llama site source.
- `ponchi-batch-006`: D-50, D-52, D-60, and D-71 deterministic official overlays staged as review-pending candidates.
- `ponchi-batch-008`: F-10 React, F-11 Next.js, F-12 Electron, F-13 Tauri, F-14 three.js, F-15 shadcn/ui, F-16 Tailwind CSS, F-17 Astro, F-20 ESLint, F-21 Prettier, F-30 VS Code, F-34 VS Code extensions, F-35 Markdown Preview Enhanced, and F-36 Git Graph deterministic official overlays staged as review-pending candidates.
- `ponchi-batch-009`: F-37 Japanese Language Pack for VS Code, F-38 Markdown All in One, F-40 npm, F-41 Vite, F-44 pnpm, F-50 git, F-60 GitHub, F-61 Pull Request, and F-62 GitHub Actions deterministic official overlays staged as review-pending candidates.
- `ponchi-batch-010`: F-80 Node.js, F-82 WSL, F-83 PowerShell, F-84 Ghostty, F-86 Ollama, F-90 Docker, F-110 Lighthouse, F-120 PostgreSQL, F-121 SQLite, and F-122 Prisma deterministic official overlays staged as review-pending candidates.
- `ponchi-batch-011`: F-140 Mermaid, F-141 PlantUML, F-153 Creative Commons, F-170 EC2, F-171 S3, F-172 IAM, F-180 OpenGL, F-181 WebGL, and F-200 Rust deterministic official overlays staged as review-pending candidates.

## Operating gates

- Do not promote anything into `assets/ponchi/final/` without explicit user
  confirmation.
- Treat existing `assets/ponchi/final/*.webp` files as legacy evidence until a
  regenerated candidate is approved.
- Never ask image generation to draw a logo, official icon, official mark,
  mascot, app UI, or brand-like substitute.
- Brand assets must come from official source pages, official repos, official
  press kits, or official icon libraries.
- If source or usage is unclear, leave the item in `overlay_wait` or
  `blocked_brand_asset` and record the reason in `docs/brand_usage_audit.md`.
- Every generated 2:1 base must be `1254x627` and pass base audit before
  overlay or candidate staging.
- Every candidate must pass the color gate before final promotion. Use
  `scripts/ponchi_color_audit.py`; do not treat `overlay_audit` or
  `review_pending` as color-policy approval.
- Every 60-entry wave must produce a wave audit and handoff before starting a
  new heavy continuation thread.
