# Ponchi Semantic Migration Plan

作成日: 2026-06-06

## Objective

全ポンチ絵を `semantic-regen-00x` の修正 wave ではなく、`cluster_id` 単位で監査・修正・候補化する運用へ移行する。

## Unit Rule

各単元は必ず次の順で閉じる。

1. `cluster_id` と対象 entry を確定する。
2. タイトルなし比較シート、候補CSV、answer_key、response_template を作る。
3. `pass_mode` に従って監査する。
4. `keep`, `caption_required`, `focus_retest`, `recompose`, `color_fix` に分類する。
5. 修正が必要なものだけ生成/補正し、機械監査を通す。
6. `assets/ponchi/final_candidates/<semantic-regen-xxx>/` に候補を置く。
7. 結果ドキュメントと ledger を更新する。
8. 単元ごとに commit する。

`assets/ponchi/final/` はユーザー確認なしに上書きしない。

## Pass Modes

詳細は `docs/ponchi_semantic_audit/semantic_cluster_registry.md` と `docs/ponchi_semantic_audit/model_distinction_rules.md` を参照。

- `exact_entry`: 同じクラスタ内で entry 単位まで判別できるべき。
- `cluster_family`: 系列・家系が分かればよい。
- `capability_milestone`: 追加機能や世代段差が見えればよい。
- `type_distinction`: reasoning / image / video / tool などの型が判別できればよい。
- `honest_ambiguous`: 絵だけで厳密差分を出すのが不誠実。本文・キャプション補助を許容。

## Work Queue

Machine-readable queue:

`ledgers/ponchi_semantic_migration_units.csv`

### Phase 0: Migration Foundation

Completed:

- cluster registry
- model distinction rules
- D OpenAI model series pilot
- D-25 recompose

### Phase 1: Active High-Risk Clusters

1. `B-ms-copilot`
2. `B-coding-assistants`
3. `B-ai-assistants-core`
4. `J-hardware-accelerators`
5. `D-provider-generation-series`
6. `D-image-video-generation`
7. `I-browser-automation-mcp`

### Phase 2: Chapter Coverage Clusters

- `A-common-frontmatter`
- `C-organizations`
- `C-people`
- `C-youtubers`
- `E-benchmarks`
- `F-languages-frameworks`
- `F-devtools-git-editor`
- `F-cloud-db-runtime`
- `G-llm-basic-concepts`
- `G-llm-techniques-control`
- `G-llm-ops`
- `H-history-timelines`
- `H-workflows`
- `I-mcp-core`
- `I-mcp-tools`
- `J-ai-ml-basics`
- `J-law-ethics`
- `J-ui-os-storage`

## Commit Cadence

Commit after each unit with a message shaped like:

`Audit <cluster_id> ponchi semantics`

If a unit only creates a plan/review pack and no images:

`Add <cluster_id> semantic review pack`

If a unit includes regenerated candidates:

`Add <cluster_id> semantic regen candidates`

## Current Next Unit

Next execution unit:

`B-ms-copilot`

Reason:

- Already scoped in `ledgers/ponchi_semantic_regen_005_scope.csv`.
- High risk of near-page confusion: `B-15 Microsoft Copilot`, `B-16 Microsoft 365 Copilot`, `B-17 Edge Copilot`.
- Clear visual distinction axes exist: general assistant / M365 work graph / browser sidebar.
