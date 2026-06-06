# Ponchi Image Quality Goal Plan

Date: 2026-06-06

## Goal

Raise production ponchi image quality by auditing beyond mechanical pass/fail.
The current pipeline catches size, density, clearspace, and color drift, but it
can still let through images that are too abstract, too SVG-like, semantically
generic, or visually repetitive.

## Current State

- Final image set: 350 entries.
- Mechanical quality bands from `ledgers/ponchi_quality_scores.csv`:
  - high: 327
  - mid: 20
  - low: 3
- Color gate:
  - pass: 242
  - review: 93
  - fail: 15
- Semantic migration units:
  - completed: 26 / 28
  - remaining: `U024 J-law-ethics`, `U025 J-ui-os-storage`
- Current U024 finding:
  - readable enough: `J-51`, `J-55`, `J-56`, `J-62`
  - weak / too abstract: `J-50`, `J-52`, `J-53`, `J-54`
- Known U025 correction:
  - `J-30` is stale and has no current final image or entry row.
  - `J-23` exists and should replace `J-30` in the U025 review scope.

## Audit Gates

### Gate 1: Mechanical Baseline

Run the existing checks before any semantic decision:

- `scripts/ponchi_image_audit.py`
- `scripts/ponchi_color_audit.py`
- `scripts/ponchi_quality_score.py`

Reject or hold candidates that fail size, 2:1 framing, color policy, logo
clearspace, or extreme density/luma checks.

### Gate 2: Production Look

Reject candidates even when mechanical scores pass if they show any of these:

- simple box-line-node diagram as the main image
- icon-only abstraction with no concrete scene or metaphor
- SVG-like geometry that lacks raster ponchi illustration feel
- dense but meaningless screens or panels
- tiny subject with excessive padding
- repeated desk/PC/board composition without a reason

### Gate 3: Semantic Distinction

For each cluster, review images as a set, not one by one. A candidate passes
only if a reviewer can distinguish it from likely confusers by visible signals.

Use this rule for law/ethics:

- `J-50 AI 倫理`: fairness, safety, transparency, and accountability checks
  around one AI system.
- `J-52 Sycophancy`: an assistant visibly over-agrees with a dubious user
  premise while truth/safety evidence is ignored.
- `J-53 著作権法 30 条の 4`: a Japanese legal boundary between permitted
  analysis/training use and protected expression.
- `J-54 ISO/IEC 42001`: an AI management system under audit, with policy,
  risk register, controls, and workflow governance.

### Gate 4: Brand And Logo Integrity

Keep the existing rule:

- never generate company logos, official icons, product UI, or brand color
  schemes with the image model;
- use official assets only through deterministic overlay;
- audit base images separately when overlays are present.

### Gate 5: Final Promotion Safety

Do not overwrite `assets/ponchi/final/` until the candidate has:

- image audit pass;
- color audit pass or explicit reviewed exception;
- semantic cluster review pass;
- candidate manifest entry;
- ledger updates;
- contact sheet artifact.

## Execution Plan

1. Complete `U024 J-law-ethics`.
   - Regenerate only `J-50`, `J-52`, `J-53`, and `J-54` as raster ponchi
     candidates with `imagegen`.
   - Save under `semantic-regen-014`.
   - Run image and color audits.
   - Produce contact sheets and update ledgers.
   - Mark U024 completed and commit after review.

2. Complete `U025 J-ui-os-storage`.
   - Replace stale `J-30` with `J-23` in the review scope.
   - Audit UI, OS, hardware, and storage entries as one confuser set.
   - Prioritize known weak items from the quality score output:
     `J-42`, `J-71`, `J-72`, `J-73`, `J-74`, `J-75`, `J-76`, `J-78`,
     `J-79`, `J-80`, `J-81`, `J-90`, `J-91`, `J-92`, `J-93`, `J-100`.
   - Regenerate only items that fail semantic or production-look gates.
   - Mark U025 completed and commit after review.

3. Reconcile remaining registry state.
   - Confirm whether `B-pricing` and `D-reasoning-models` should remain active
     or be marked reviewed based on previous regeneration notes.
   - Confirm all migration units are completed.
   - Confirm no migration unit references missing final images.
   - Confirm no final image is outside the semantic migration coverage.

4. Final verification.
   - Rerun mechanical score and color summaries.
   - Confirm `git status --short` has only expected untracked attachment
     noise, if any.
   - Mark the active goal complete only after U024, U025, and registry
     reconciliation are done.

## Immediate Next Step

Start `semantic-regen-014` for the four weak U024 entries. The first generation
target should be `J-50 AI 倫理`, because it sets the visual quality bar for the
rest of the law/ethics cluster.
