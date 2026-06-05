# Ponchi Blind Quiz Run 001 Results

## Inputs

- B respondent: `agent_parfit_responses.csv`
- D respondent: `agent_rawls_responses.csv`
- Scoring script: `scripts/score_ponchi_blind_quiz.py`

## Summary

| chapter | total | top1 | top3 | semantic_ok | weak | ambiguous | generic | misleading |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| B | 40 | 25 | 29 | 21 | 4 | 4 | 6 | 5 |
| D | 38 | 20 | 26 | 14 | 6 | 6 | 8 | 4 |

## High-Risk Misleading Items

| chapter | entry | title | guessed as | confidence | note |
| --- | --- | --- | --- | ---: | --- |
| B | `B-26` | Azure OpenAI | `B-27` | 72 | Google Cloud; Gemini |
| B | `B-31` | Excalidraw | `B-6` | 88 | Cursor; Bolt.new |
| B | `B-5` | GitHub Copilot | `B-4` | 70 | Claude Code; Codex |
| B | `B-52` | Gemini の料金プラン | `B-1` | 95 | Vertex AI; Genspark |
| B | `B-6` | Windsurf | `B-4` | 74 | Claude Code; Codex |
| D | `D-22` | o1 系 | `D-71` | 84 | D-21|D-24 |
| D | `D-53` | Veo | `D-51` | 82 | D-55|D-54 |
| D | `D-58` | Whisk | `D-57` | 76 | D-53|D-56 |
| D | `D-70` | Amical | `D-58` | 83 | D-55|D-51 |

## Generic Items

| chapter | entry | title | guessed as | confidence | note |
| --- | --- | --- | --- | ---: | --- |
| B | `B-1` | Gemini | `B-31` | 38 | Figma; Canva |
| B | `B-10` | Devin | `B-19` | 66 | Claude; Microsoft 365 Copilot |
| B | `B-14` | Genspark | `B-10` | 58 | Codex; Claude Code |
| B | `B-2` | Claude | `B-5` | 50 | Codex; Claude Code |
| B | `B-28` | Render | `B-9` | 38 | Canva; Figma |
| B | `B-3` | ChatGPT | `B-5` | 44 | Codex; Claude Code |
| D | `D-1` | Gemini 2 系 | `D-4` | 36 | D-3|D-2|D-1 |
| D | `D-10` | Claude 3 系 | `D-14` | 32 | D-13|D-12|D-11 |
| D | `D-11` | Claude 3.5 系 | `D-13` | 41 | D-12|D-14|D-11 |
| D | `D-13` | Claude 4.5 系 | `D-11` | 45 | D-10|D-12 |
| D | `D-14` | Claude Mythos Preview | `D-12` | 42 | D-13|D-11 |
| D | `D-25` | GPT-1 / GPT-2 系 | `D-20` | 38 | D-23|D-21 |
| D | `D-51` | Imagen | `D-70` | 34 | D-50|D-58 |
| D | `D-71` | Whisper | `D-25` | 35 | D-24|D-21 |

## Immediate Interpretation

- B章はロゴが見えている項目は強い一方、コーディング支援サービスとクラウドAIサービスで混同が出た。
- D章はブランド系列は当たりやすいが、モデル世代差はかなり弱い。Gemini/Claude/OpenAIの世代群は個別画像より構図ルールの問題として扱うべき。
- `misleading` は高確信誤答なので、単なる保留ではなく優先レビュー対象にする。
- `generic` は画像が汎用ダッシュボード化しているため、視覚主題の再定義が必要。

Problem queue: `docs/ponchi_semantic_audit/blind_quiz_2026-06-05/blind_quiz_run_001_problem_queue.csv`
