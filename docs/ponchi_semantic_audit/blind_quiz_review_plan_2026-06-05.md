# Ponchi Blind Quiz Review Plan 2026-06-05

## 目的

ポンチ絵を「見た目がきれいか」ではなく、「画像だけでその項目だと分かるか」で再チェックする。

今回の中心課題は、低品質画像が減った後に残る次の問題を拾うこと。

- 情報密度は高いが、項目固有の意味に効いていない。
- ロゴやタイトルがないと識別できない。
- 同じ章・同じカテゴリ内で他項目と混同する。
- 正解できても確信度が低く、絵の決め手が弱い。

## 初回対象

まず B章と D章で実施する。

| chapter | count | reason |
| --- | ---: | --- |
| `B` | 40 | ブランド/サービス系。ロゴ依存やサービス間の差分不足を検出しやすい |
| `D` | 38 | モデル/生成AI系。世代差・用途差が画像だけで見えるかを検証しやすい |

350件全体を混ぜることはしない。章内または意味カテゴリ内で候補を限定してクイズ化する。これは、読者が実際に読む時も近い用語群の中で比較するため。

## 作成済みパック

Root:

`docs/ponchi_semantic_audit/blind_quiz_2026-06-05/`

### B章

- 問題シート: `docs/ponchi_semantic_audit/blind_quiz_2026-06-05/B/blind_quiz_B_sheet.png`
- 候補リスト: `docs/ponchi_semantic_audit/blind_quiz_2026-06-05/B/candidates.csv`
- 回答テンプレート: `docs/ponchi_semantic_audit/blind_quiz_2026-06-05/B/response_template.csv`
- 答え合わせ用キー: `docs/ponchi_semantic_audit/blind_quiz_2026-06-05/B/answer_key.csv`

### D章

- 問題シート: `docs/ponchi_semantic_audit/blind_quiz_2026-06-05/D/blind_quiz_D_sheet.png`
- 候補リスト: `docs/ponchi_semantic_audit/blind_quiz_2026-06-05/D/candidates.csv`
- 回答テンプレート: `docs/ponchi_semantic_audit/blind_quiz_2026-06-05/D/response_template.csv`
- 答え合わせ用キー: `docs/ponchi_semantic_audit/blind_quiz_2026-06-05/D/answer_key.csv`

`answer_key.csv` は採点用。回答エージェントには渡さない。

## 回答者に渡すもの

回答エージェントに渡すのは以下だけ。

1. `blind_quiz_<chapter>_sheet.png`
2. `candidates.csv`
3. `response_template.csv`
4. このドキュメント内の「回答ルール」と「判定観点」

渡してはいけないもの。

- `answer_key.csv`
- `ponchi_quality_scores.csv`
- 章別のタイトル付きコンタクトシート
- ファイル名が entry_id を含む個別画像

## 回答ルール

各 `blind_image_id` について、候補リストから最も近い entry を選ぶ。

回答列:

| column | meaning |
| --- | --- |
| `blind_image_id` | 問題番号。例: `B-Q001` |
| `top1_guess` | 最有力の entry_id |
| `top1_confidence` | 0-100 の確信度 |
| `top2_guess` | 2番目に迷った entry_id |
| `top3_guess` | 3番目に迷った entry_id |
| `visual_evidence` | 画像内の何を根拠にしたか |
| `confused_with` | 迷った候補。複数可 |
| `semantic_comment` | 絵の意味が弱い、ロゴ依存、汎用UIなどのコメント |

確信度の目安:

| confidence | interpretation |
| ---: | --- |
| `90-100` | 画像だけでほぼ特定できる |
| `70-89` | かなり分かるが、近い候補はある |
| `50-69` | 候補群の中ではこれだと思うが、決め手が弱い |
| `30-49` | かなり迷う |
| `0-29` | 画像だけでは分からない |

## 判定観点

回答者は、きれいさではなく次を見る。

- 画像内の主題が、候補項目の機能・用途・文脈を表しているか。
- ロゴ、公式マーク、ブランド色だけに頼っていないか。
- 同じ候補群内の別項目と混同しないだけの差分があるか。
- 200px程度に縮めても、主な意味が残るか。
- 情報量が多い場合、その情報が項目理解に効いているか。

## 採点ルール

採点時は `answer_key.csv` と回答CSVを突合する。

### Per Image Metrics

| metric | meaning |
| --- | --- |
| `top1_correct` | `top1_guess` が正解 |
| `top3_correct` | `top1/top2/top3` のいずれかに正解が入る |
| `confidence_bucket` | high / mid / low |
| `high_confidence_wrong` | 確信度70以上で不正解 |
| `low_confidence_correct` | 正解だが確信度70未満 |
| `main_confusion` | 誤答または迷い先として多い項目 |

### Semantic Decision

| decision | condition | meaning | next action |
| --- | --- | --- | --- |
| `semantic_ok` | top1正解かつ confidence >= 70 | 画像だけで識別可能 | 維持 |
| `weak_but_identifiable` | top1正解だが confidence < 70 | 分かるが決め手が弱い | 横並び確認 |
| `ambiguous` | top1不正解だが top3正解 | 近いが混同されやすい | 候補ペア比較 |
| `generic` | top3にも正解なし、confidence < 70 | 汎用図になっている | 再構図候補 |
| `misleading` | top1不正解かつ confidence >= 70 | 別項目に見える | 優先再構図 |

重要なのは、単純な正解率ではなく `misleading` と `ambiguous` を拾うこと。高確信で間違われる画像は、読者を誤誘導する可能性がある。

## 複数回答者運用

初回は各章を最低2回、できれば3回独立に回答させる。

推奨:

- `Agent A`: 章全体を普通に回答。
- `Agent B`: ロゴ・ブランド名に頼りすぎないよう、機能や構図の根拠を重視して回答。
- `Agent C`: 低確信時は無理に当てず、迷い先を詳しく書く。

統合判定:

| pattern | decision |
| --- | --- |
| すべて top1正解、平均confidence >= 75 | 維持 |
| top1正解が多いが平均confidence < 70 | 横並び確認 |
| top3正解は多いがtop1が割れる | 混同ペア確認 |
| 2人以上が同じ誤答に高確信 | 優先再構図 |
| 回答がばらける | 汎用化・意味不足として再確認 |

## B章の重点

B章はブランド/サービス名が候補に含まれるため、ロゴが出ている画像は正解しやすい。そこで採点後に追加で見る。

### Logo Dependency Check

次のように分類する。

| result | meaning |
| --- | --- |
| `logo_independent` | ロゴ以外の構図や用途からも分かる |
| `logo_assisted` | ロゴが決め手だが、絵にも用途差がある |
| `logo_dependent` | ロゴを隠すとほぼ区別できない |

`logo_dependent` は即NGではない。ブランド項目ではロゴも読者理解の一部。ただし、同じページ群でロゴ依存が多すぎる場合は、サービスの使われ方や強みを絵に追加する。

B章で特に比較したい群:

- `B-4 Cursor`
- `B-5 GitHub Copilot`
- `B-6 Windsurf`
- `B-7 Claude Code`
- `B-8 Codex`
- `B-15 Microsoft Copilot`
- `B-16 Microsoft 365 Copilot`
- `B-17 Edge Copilot`
- `B-19 Claude Cowork`

この群は「人物 + エディタ/ダッシュボード + ロゴ」に寄りやすい。ブラインド結果で迷いが多い場合、再生成前にサービス別の視覚主題を決め直す。

## D章の重点

D章はモデル名・世代名の違いが抽象的なので、画像だけで完全識別するのは難しい。そのためB章より厳しすぎない。

見るべきこと:

- モデル世代の「新旧」「能力差」「用途差」が見えるか。
- `Gemini`, `Claude`, `OpenAI`, `DeepSeek` などの系列差がロゴ以外にもあるか。
- 画像生成/動画生成系は、出力タイプや制作フローが見えるか。

D章で特に比較したい群:

- `D-1 Gemini 2`
- `D-2 Gemini 2.5`
- `D-3 Gemini 3`
- `D-10 Claude 3 系`
- `D-11 Claude 3.5 系`
- `D-12 Claude 4 系`
- `D-20 GPT-5`
- `D-21 GPT-4`
- `D-22 o1`
- `D-23 o3`
- `D-24 GPT-3`
- `D-25 GPT-1 / GPT-2`

D章は、個別画像の失敗というより「世代差をどう描くか」のルール不足が問題になりやすい。クイズ結果で混同が多い場合は、まずモデル世代群の構図ルールを作る。

## Agent Prompt

回答エージェントには以下を渡す。

```text
You are reviewing VibeCodingDictionary ponchi images by blind identification.

You will receive:
- a titleless contact sheet with blind image IDs
- a CSV candidate list for the same chapter
- a response CSV template

Do not judge whether the art is pretty. Judge whether the image itself communicates which candidate it represents.

For each blind_image_id:
1. Pick the most likely entry_id from candidates.csv.
2. Give top1_confidence from 0 to 100.
3. Add top2_guess and top3_guess if there are plausible alternatives.
4. In visual_evidence, cite concrete visible elements: logo, UI pattern, workflow, output type, hardware shape, model generation, collaboration scene, etc.
5. In semantic_comment, call out if the image is generic, logo-dependent, over-dense without meaning, or confused with another candidate.

Use low confidence when the image only looks like a generic AI dashboard or generic coding screen.
Use high confidence only when the image has specific visual evidence for that candidate.

Return the completed CSV rows only.
```

## Execution Steps

1. B章を2-3エージェントで回答。
2. `answer_key.csv` で採点し、`semantic_ok / weak_but_identifiable / ambiguous / generic / misleading` に分類。
3. B章の混同ペアを一覧化。
4. B章の `logo_dependent` 候補を抽出。
5. D章を同じ手順で回答。
6. D章はモデル世代群の混同を別集計する。
7. P0/P1の再構図候補に、ブラインド結果を加えて最終判断する。

## First Run Success Criteria

初回は完璧な採点システムではなく、次が得られれば成功。

- B章で「ロゴを除くと弱い」候補が分かる。
- B章のコーディング支援サービス群で混同ペアが分かる。
- D章でモデル世代群の混同パターンが分かる。
- `misleading` と `generic` を優先キューに追加できる。
- 逆に、現状維持してよい画像を明確に減らせる。
