# Ponchi Semantic Cluster Registry

作成日: 2026-06-06

## Purpose

`semantic-regen-00x` は修正 wave 番号であり、章や比較単位ではない。今後の監査は `cluster_id` を主キーにして管理する。

この registry は、画像を「近い項目群の中で判別できるか」で見るための管理単位を定義する。

## Rules

- 350件全体を混ぜない。
- まず章で分ける。
- 次に、隣ページまたは同じ読者文脈で混同しやすい項目を cluster にする。
- `semantic-regen-00x` は作業 wave として残すが、必ず `cluster_id` を結果ドキュメントと ledger に書く。
- モデル世代のように画像だけで厳密識別が難しい cluster は、exact match を合格条件にしない。

## Pass Modes

| pass_mode | meaning | use case |
| --- | --- | --- |
| `exact_entry` | 画像だけで entry_id まで判別できるべき | サービス名、ロゴ付きブランド、明確なツール |
| `cluster_family` | 画像だけで同じ家系/系列だと分かればよい | GPT 系、Claude 系、Gemini 系など |
| `capability_milestone` | 追加機能・用途の段差が見えればよい | GPT-3→4、Claude 3→3.5、Gemini 2→2.5 |
| `type_distinction` | モデル種別や出力タイプが判別できればよい | reasoning / audio / image / video |
| `honest_ambiguous` | 絵だけで厳密差分を出すのが不誠実なため、本文・キャプション依存を許容 | minor version、未公開/不明確な能力差 |

## Current Clusters

Authoritative machine-readable list:

`ledgers/ponchi_semantic_cluster_registry.csv`

### High Priority

| cluster_id | entries | pass mode | status |
| --- | --- | --- | --- |
| `B-ai-assistants-core` | `B-1`, `B-2`, `B-3`, `B-10`, `B-14`, `B-15`, `B-16`, `B-17`, `B-19` | `exact_entry` for services, with logo-dependency note | active |
| `B-coding-assistants` | `B-4`, `B-5`, `B-6`, `B-7`, `B-8`, `D-35` | `exact_entry` for products; `D-35` distinguished as Composer model/workflow | active |
| `B-ms-copilot` | `B-15`, `B-16`, `B-17` | `exact_entry` | active |
| `D-openai-model-series` | `D-20`, `D-21`, `D-22`, `D-23`, `D-24`, `D-25`, `D-26` | mixed: `capability_milestone` / `type_distinction` / `honest_ambiguous` | planning |
| `D-provider-generation-series` | `D-1`, `D-2`, `D-3`, `D-4`, `D-10`, `D-11`, `D-12`, `D-13`, `D-20`, `D-21` | `cluster_family` plus visible milestone | planning |
| `D-image-video-generation` | `D-51`, `D-52`, `D-53`, `D-55`, `D-57`, `D-58` | `type_distinction` | active |
| `J-hardware-accelerators` | `J-70`, `J-72`, `J-73`, `J-74`, `J-75`, `J-76`, `J-77` | `exact_entry` for physical hardware where possible | active |

## Goal Template

Use this shape instead of a generic “semantic regen wave” goal:

```text
Goal: cluster_id=<cluster_id> の画像について、同一クラスタ内でタイトルなし判別できるかを検査する。
対象: <entry ids>
合格条件: <pass_mode> に従う。exact_entry が必要なものだけ再構図し、honest_ambiguous は本文/キャプション依存を許容して無理に差分を捏造しない。
成果物: blind sheet, candidates.csv, answer_key.csv, scored responses, findings, regen scope, staged candidates.
```

Example:

```text
Goal: cluster_id=D-openai-model-series の D-20/D-21/D-22/D-23/D-24/D-25/D-26 を、GPT系の世代差・reasoning系・open-weight系として判別可能か検査する。GPT-4とGPT-5のように画像だけで厳密差分が不明瞭なものは honest_ambiguous として、本文補助前提の visual rule を作る。
```
