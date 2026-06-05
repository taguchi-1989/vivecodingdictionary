# Semantic Regen 004 Plan

作成日: 2026-06-06

対象: semantic-regen-001 から 003 で触っていない P1 残件。P0 は既に候補化済みなので、wave 4 は「意味はあるが弱い/色で落ちている」画像を扱う。

## Scope

| priority | entry | title | issue | action |
| --- | --- | --- | --- | --- |
| P1 | `D-35` | Cursor Composer | Composer 固有の複数ファイル編集・差分作成が弱く、ロゴ依存が強い | 再構図 |
| P1 | `J-42` | Web3 | 分散・所有・台帳の意味が弱く、汎用ノード図に見える | 再構図 |
| P1 | `A-6` | 評価日・時変情報の見方 | 意味は通るが色ゲート fail | 色補正優先 |
| P1 | `I-10` | Filesystem MCP | ファイルツリーの意味は明確だが色ゲート fail | 色補正優先 |
| P1 | `J-55` | 個人情報保護法 | 法/保護の文脈は出ているが色ゲート fail | 色補正優先 |
| P1 | `J-76` | CPU | CPU の意味は出ているが色ゲート fail | 色補正優先 |

## Output

- Batch id: `semantic-regen-004`
- Generated/edited images: `assets/ponchi/experiments/batches/semantic-regen-004/`
- Final review candidates: `assets/ponchi/final_candidates/semantic-regen-004/`
- Audit docs: `docs/ponchi_semantic_audit/semantic_regen_004/`
- Prompt docs: `assets/ponchi/pipeline_prompts/semantic-regen-004/`

`assets/ponchi/final/` は触らない。合格候補は review candidate として置く。

## Judgment

### D-35 Cursor Composer

Pass if the image communicates Composer as multi-file edit planning and diff application, not just a Cursor logo or a generic editor.

Must show:

- multiple affected files
- diff/change blocks
- plan-to-apply flow
- small before/after editor state

Must avoid:

- single IDE screen only
- logo-only identification
- generic code assistant chat

### J-42 Web3

Pass if the image communicates distributed ownership plus ledger verification, not just connected dots.

Must show:

- user-owned wallet/identity boundary
- distributed ledger blocks
- token/permission transfer
- several independent nodes verifying the same record

Must avoid:

- generic network mesh
- blockchain coin speculation
- plain cloud architecture

### Color-Fix Entries

Pass if the existing semantic structure remains recognizable and generated-body color audit passes. If color normalization makes the image visually flat or harms meaning, prefer regeneration over mechanical recolor.

## Retest

For D-35 and J-42, create a small titleless focus sheet with nearby confusers:

- `D-35`: `B-4`, `B-6`, `B-7`, `B-8`, `D-21`, `D-20`
- `J-42`: `J-40`, `J-41`, `J-43`, `J-53`, `J-56`

Color-fix entries do not need semantic blind retest unless the edited image changes structure.

## Success Criteria

- 6 candidates staged in `final_candidates/semantic-regen-004/`.
- Image audit passes or has documented review reason.
- Color audit passes for color-fix entries.
- D-35/J-42 pass titleless focus review or are explicitly held for another iteration.
