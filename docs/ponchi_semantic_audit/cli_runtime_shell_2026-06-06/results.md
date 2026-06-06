# CLI, runtime, and shell review

Date: 2026-06-06

Cluster: `F-cli-runtime-shell`
Pass mode: `type_distinction`

## Scope correction

The original U016 entry list included stale IDs (`F-22` - `F-26`, `F-70`, `F-72` - `F-74`) and omitted several current runtime/shell entries. This unit now covers the current CLI/build/runtime/shell/container/environment group:

`F-40;F-41;F-42;F-44;F-71;F-80;F-81;F-82;F-83;F-84;F-85;F-86;F-87;F-90;F-91`

DB, cloud, quality, file-format, license, web-foundation, graphics, and remaining general F entries are split into follow-up units `U016B` and `U016C`.

## Judgment

The group passes after replacing `F-84 Ghostty` with a new staged candidate. Build tools, shells, runtimes, container, and env/config concepts are visually separable.

## Findings

| group | entries | visual status | action |
| --- | --- | --- | --- |
| Package/build/search | `F-40`, `F-41`, `F-42`, `F-44`, `F-71` | npm, Vite, build, pnpm, and ripgrep are distinguishable by package graph, dev/build pipeline, artifact pipeline, store/workspace, and search/filter motifs. | keep |
| Runtime/shell/terminal | `F-80`, `F-81`, `F-82`, `F-83`, `F-84`, `F-86`, `F-87` | Node, bash, WSL, PowerShell, Ghostty, ollama, and sudo have distinct runtime/shell/terminal/security surfaces. | keep; `F-84` staged from `semantic-regen-013` |
| Container/env/framework | `F-85`, `F-90`, `F-91` | SuperClaude remains a logo-avoid community framework; Docker and `.env` are visually clear. | keep |

## F-84 Regeneration

The previous `F-84` final image had a low score and excessive dark/off-palette content. `semantic-regen-013` creates a lighter terminal-emulator composition with a small official Ghostty favicon overlay.

Audit result:

- Image audit: pass for base and overlay.
- Color audit: pass for base and overlay after palette normalization.
- Staged candidate: `assets/ponchi/final_candidates/semantic-regen-013/F-84_candidate.png`

## Decision

No final overwrite. Stage `F-84` as a reviewed candidate and keep the rest as-is.

## Artifacts

- Blind sheet: `docs/ponchi_semantic_audit/cli_runtime_shell_2026-06-06/cli_runtime_shell_blind_sheet.png`
- Labeled sheet: `docs/ponchi_semantic_audit/cli_runtime_shell_2026-06-06/cli_runtime_shell_labeled_sheet.png`
- Candidates: `docs/ponchi_semantic_audit/cli_runtime_shell_2026-06-06/candidates.csv`
- Answer key: `docs/ponchi_semantic_audit/cli_runtime_shell_2026-06-06/answer_key.csv`
- Response template: `docs/ponchi_semantic_audit/cli_runtime_shell_2026-06-06/response_template.csv`
- Regen audit: `docs/ponchi_semantic_audit/semantic_regen_013/`
