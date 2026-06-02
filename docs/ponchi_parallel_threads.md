# Ponchi parallel thread registry

This registry tracks background Codex threads used for the long-running 350
entry ponchi regeneration goal.

## Controller thread

- Thread id: `019e84fa-2201-7753-9e6c-22f7e9612a81`
- Role: integration, audit, progress overview, wave handoff, user-facing
  coordination.

## Worker threads

| role | thread id | scope | first target |
| --- | --- | --- | --- |
| B continuation | `019e8510-b717-7d81-95e8-eff08d341dfb` | B chapter official logo/source/overlay pipeline | Batch 002 remaining `overlay_wait` items |
| All-chapters forward | `019e8511-032d-7ba1-aa6e-a8cbcedac19a` | all remaining batches in ledger order, not only C/D | Batch 003 prompt/base generation |

## Coordination rules

- No thread may write to `assets/ponchi/final/` without explicit user approval.
- Workers should stage candidates under `assets/ponchi/final_candidates/`.
- Workers must not revert unrelated dirty worktree changes.
- Workers should update `docs/brand_usage_audit.md`,
  `ledgers/ponchi_generation_batches.csv`, and relevant batch/wave audit files
  as they make progress.
- Controller should periodically inspect worker outputs with `read_thread` and
  reconcile the ledgers.

## Worker handoff files

- B continuation: `docs/ponchi_agent_b_continuation_handoff.md`
- All-chapters forward: `docs/ponchi_agent_all_chapters_handoff.md`
