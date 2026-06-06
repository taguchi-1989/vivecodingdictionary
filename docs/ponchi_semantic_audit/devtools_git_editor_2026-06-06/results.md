# Devtools, Git, and editor review

Date: 2026-06-06

Cluster: `F-devtools-git-editor`
Pass mode: `type_distinction`

## Scope correction

The original migration unit listed `F-63` - `F-65`, but those IDs are not present in the current entries/final images. This review removes those stale IDs and includes `F-59 README.md`, which belongs with the Git/repository documentation cluster.

Reviewed IDs:

`F-20;F-21;F-30;F-34;F-35;F-36;F-50;F-51;F-52;F-53;F-54;F-55;F-56;F-57;F-58;F-59;F-60;F-61;F-62`

## Judgment

The cluster passes. Tool identities and operation semantics are meaningfully separated: lint vs format, editor vs extension, Git object/workflow concepts, and GitHub platform workflows.

## Findings

| group | entries | visual status | action |
| --- | --- | --- | --- |
| Code quality tools | `F-20`, `F-21` | ESLint reads as rule diagnostics; Prettier reads as formatting/normalization. | keep |
| Editor and extensions | `F-30`, `F-34`, `F-35`, `F-36` | VS Code base, extension marketplace, Markdown preview, and Git graph are distinguishable. VS Code-logo color review remains a prior color note, not semantic failure. | keep |
| Git concepts | `F-50` - `F-59` | Push/pull direction, branch divergence, commit node, merge join, ignore filter, repository container, stash shelf, and README documentation are visually separated. | keep |
| GitHub workflows | `F-60`, `F-61`, `F-62` | Platform, pull-request review, and CI automation differ in workflow structure. | keep |

## Decision

No regeneration in this unit. The images are semantically useful; exact Git subcommands are mostly supported by arrow/graph motifs, with captions handling the final specificity.

## Artifacts

- Blind sheet: `docs/ponchi_semantic_audit/devtools_git_editor_2026-06-06/devtools_git_editor_blind_sheet.png`
- Labeled sheet: `docs/ponchi_semantic_audit/devtools_git_editor_2026-06-06/devtools_git_editor_labeled_sheet.png`
- Candidates: `docs/ponchi_semantic_audit/devtools_git_editor_2026-06-06/candidates.csv`
- Answer key: `docs/ponchi_semantic_audit/devtools_git_editor_2026-06-06/answer_key.csv`
- Response template: `docs/ponchi_semantic_audit/devtools_git_editor_2026-06-06/response_template.csv`
