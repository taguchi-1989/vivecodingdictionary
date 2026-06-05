# Hardware accelerators review

Date: 2026-06-06

Cluster: `J-hardware-accelerators`
Pass mode: `exact_entry`

## Findings

| entry | title | latest candidate | judgment |
| --- | --- | --- | --- |
| `J-70` | VRAM | `ponchi-batch-017` | keep: memory-chip lane and accelerator-adjacent memory role are visible |
| `J-72` | H100 | `semantic-regen-002` | keep: deployed product cluster/rack context is distinct from Blackwell |
| `J-73` | Blackwell | `semantic-regen-002` | keep: generation progression and system architecture cues are visible |
| `J-74` | RTX series | `ponchi-batch-017` | keep: consumer/pro card lineup axis is visible enough for this cluster |
| `J-75` | Tensor cores | `ponchi-batch-017` | keep: matrix/tile compute block axis separates it from GPU concept |
| `J-76` | CPU | `semantic-regen-004` | keep: general-purpose central chip/control-flow role is visible |
| `J-77` | GPU concept | `ponchi-batch-018` | keep: parallel processor array and accelerator output are visible |

## Artifacts

- Blind sheet: `docs/ponchi_semantic_audit/hardware_accelerators_2026-06-06/hardware_accelerators_blind_sheet.png`
- Labeled sheet: `docs/ponchi_semantic_audit/hardware_accelerators_2026-06-06/hardware_accelerators_labeled_sheet.png`
- Candidates: `docs/ponchi_semantic_audit/hardware_accelerators_2026-06-06/candidates.csv`
- Answer key: `docs/ponchi_semantic_audit/hardware_accelerators_2026-06-06/answer_key.csv`
- Response template: `docs/ponchi_semantic_audit/hardware_accelerators_2026-06-06/response_template.csv`

## Judgment

No new regeneration required in U005. The main risk remains `J-77` GPU concept versus `J-75` Tensor cores, but the current candidates separate whole-processor parallelism from matrix/tile compute blocks well enough for a title-hidden cluster test.
