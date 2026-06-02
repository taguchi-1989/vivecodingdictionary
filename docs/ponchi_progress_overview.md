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
| `brief_needed` | 207 |
| `overlay_wait` | 112 |
| `overlay_audit` | 14 |
| `overlay_ready` | 12 |
| `prompt_review` | 4 |
| `blocked_brand_asset` | 1 |

## Latest 2:1 Base Progress

| scope | generated bases | base audit pass | note |
| --- | ---: | ---: | --- |
| `ponchi-batch-003` | 20 / 20 | 20 / 20 | base complete |
| `ponchi-batch-004` | 20 / 20 | 20 / 20 | base complete; 9 entries remain `overlay_wait` |
| `ponchi-batch-005` | 20 / 20 | 20 / 20 | base complete; 13 entries remain `overlay_wait` |
| `ponchi-batch-006` | 20 / 20 | 20 / 20 | base complete; 15 entries remain `overlay_wait`, 3 are `overlay_ready` |
| Wave 002 | 60 / 60 | 60 / 60 | Batches 004-006 base complete; official review/overlay remains |
| `ponchi-batch-007` | 20 / 20 | 20 / 20 | base complete; 20 entries are `logo_avoid` |
| `ponchi-batch-008` | 20 / 20 | 20 / 20 | base complete; 14 entries remain `overlay_wait`, 6 are `logo_avoid` |
| `ponchi-batch-009` | 20 / 20 | 20 / 20 | base complete; 8 entries remain `overlay_wait`, 1 is `overlay_audit` |
| Wave 003 | 60 / 60 | 60 / 60 | Batches 007-009 base complete; official review/overlay remains |
| `ponchi-batch-010` | 20 / 20 | 20 / 20 | base complete; 11 entries remain `overlay_wait` |
| `ponchi-batch-011` | 20 / 20 | 20 / 20 | base complete; 9 entries remain `overlay_wait` |
| `ponchi-batch-012` | 20 / 20 | 20 / 20 | base complete; 20 entries are `logo_avoid` |
| Wave 004 | 60 / 60 | 60 / 60 | Batches 010-012 base complete; official review/overlay remains |
| Numerically tracked base total | 200 / 350 | 200 / 350 | Batch 003 plus Batches 004-012 |

## Wave map

| wave | batches | entries | primary focus | status |
| --- | --- | ---: | --- | --- |
| Wave 001 | `ponchi-batch-001` - `ponchi-batch-003` | 60 | finish B logo pipeline, classify Batch 003, generate first all-chapter base set | active |
| Wave 002 | `ponchi-batch-004` - `ponchi-batch-006` | 60 | all non-B chapters in ledger order, 2:1 base and brand decisions | base_complete |
| Wave 003 | `ponchi-batch-007` - `ponchi-batch-009` | 60 | all non-B chapters in ledger order, 2:1 base and brand decisions | base_complete |
| Wave 004 | `ponchi-batch-010` - `ponchi-batch-012` | 60 | F-heavy batch generation and audit | base_complete |
| Wave 005 | `ponchi-batch-013` - `ponchi-batch-015` | 60 | F/G/I coverage and logo decisions | next |
| Wave 006 | `ponchi-batch-016` - `ponchi-batch-018` | 50 | remaining chapters completion and final cleanup | not_started |

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
- Every 60-entry wave must produce a wave audit and handoff before starting a
  new heavy continuation thread.
