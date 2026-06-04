# Ponchi Quality Rule Evaluation 2026-06-03

## 目的

350件の `assets/ponchi/final/*.webp` に対して、2:1 画像の品質差を拾うための機械得点を作り、既知の問題候補を使って判定ルールの妥当性を確認する。

この得点は採用可否ではなく、目視レビューと再生成計画の優先順位を作るための補助指標として扱う。

## 作成物

- 得点スクリプト: `scripts/ponchi_quality_score.py`
- 全件得点台帳: `ledgers/ponchi_quality_scores.csv`
- 次に見る56件の計画CSV: `ledgers/ponchi_regen_review_plan.csv`
- 集計サマリ: `docs/ponchi_quality_score_summary.md`
- 低スコア確認シート: `docs/ponchi_batch_audits/ponchi-quality-low-contact-sheet.png`
- 中位問題候補シート: `docs/ponchi_batch_audits/ponchi-quality-mid-review-contact-sheet.png`
- 既知2:1機械変換候補シート: `docs/ponchi_batch_audits/ponchi-quality-known-padding-contact-sheet.png`

実行コマンド:

```powershell
& 'C:\Users\tgch1\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' scripts\ponchi_quality_score.py
```

## 初回結果

| 区分 | 件数 |
| --- | ---: |
| high | 325 |
| mid | 24 |
| low | 1 |

| レビュー行き先 | 件数 | 意味 |
| --- | ---: | --- |
| `full_regen_review` | 1 | 機械得点で明確な外れ値。最優先で再生成判断 |
| `official_overlay_color_review` | 10 | 色NGだが公式素材文脈あり。即再生成ではなくロゴ/公式素材監査 |
| `composition_regen_review` | 23 | 既知の2:1機械変換候補。横長構図として退屈かを目視確認 |
| `sparse_diagram_review` | 4 | 高得点だが、軽い・薄い・ロゴ依存の図解。しょぼさ確認 |
| `visual_review` | 22 | 中位帯。濃淡・線密度・余白の目視確認 |
| `light_review` | 290 | 軽い章別サンプリング確認 |

## 妥当だった点

1. `F-84 Ghostty` は score 56 で唯一の low になった。低スコア検出は明確な外れ値拾いとして機能している。
2. `B-41 arXiv`, `C-82 まさお` など、得点は中位でも色ポリシーが強く反応するものを別レーンに分けられた。
3. 公式ロゴや公式アイコン由来の色は `official_overlay_color_review` に逃がせたため、色NGを単純な再生成扱いにしない運用にできた。
4. 既知の2:1機械変換23件は、得点が高くても `composition_regen_review` に残せた。
5. `B-7 Claude Code` のような「ロゴ + 単純な箱線 + 余白」の高得点画像は、`sparse_diagram_review` として拾えるようにした。

## 危ない点

1. 既知の2:1機械変換23件は多くが high に入った。つまり、現在の得点だけでは「横長構図として退屈」「中央に置いただけ」「意味の展開が弱い」を検出できない。
2. `central_padding_shape` の自動検出は今回ほぼ役に立たなかった。白余白や薄青背景、横長UI風の枠があると、単純なbboxでは中央配置を見抜けない。
3. 公式素材の色は正当な例外の可能性がある。色NGは、生成本文の色ズレなのか、後合成された公式素材なのかを分離しないと誤判定になる。
4. high帯でも、意味のズレ、ロゴ風のAI生成、読める文字、構図ファミリーの使い回しは検出できない。
5. `sparse_diagram_review` は意図的に粗い。J章の抽象図や凡例まで自動NGにすると誤判定が増えるため、ブランド/サービス文脈を中心に「レビュー送り」に留める。

## 判定ルールの修正方針

機械得点は次の5レーンに固定する。

| レーン | 条件 | 次アクション |
| --- | --- | --- |
| P0 `full_regen_review` | score < 70 | 即目視。原則、再生成候補 |
| P1 `official_overlay_color_review` | color fail + 公式素材文脈あり | 公式素材の出典・合成範囲・base画像を確認 |
| P1 `composition_regen_review` | 既知2:1機械変換、または人間が退屈と判断 | 200px表示と横長構図の意味を確認 |
| P1 `sparse_diagram_review` | 高得点だが、軽量・低インク・低濃淡・公式ロゴ依存 | しょぼい横長図解か、意図した抽象図かを確認 |
| P2 `visual_review` | 70-84、または濃淡/線密度/余白フラグ | OK/微修正/再生成に人間が分類 |
| P3 `light_review` | 85以上かつ強い警告なし | 章ごとに10%程度を抜き取り確認 |

「退屈な中位・高位」を拾うため、次の人間レビュー列を `ledgers/ponchi_regen_review_plan.csv` の運用で追加する。

- `meaning_at_200px`: `ok` / `weak` / `unreadable`
- `boring_2to1`: `no` / `maybe` / `yes`
- `composition_family`: `process_flow` / `concept_map` / `before_after` / `timeline_scale` / `collaboration_hub` / `diagram_only`
- `regen_decision`: `OK` / `微修正` / `再生成` / `公式素材確認待ち`
- `human_note`: 一言メモ

## 次のレビュー順

1. `P0`: `F-84 Ghostty` を見て、再生成プロンプト作成へ進める。
2. `P1 sparse_diagram_review`: `B-7 Claude Code` 型の薄いブランド図解を確認し、再生成対象にするか決める。
3. `P1 official_overlay_color_review`: 10件を公式素材例外として妥当か確認する。base画像が残っていない場合は、色NGを暫定保留にする。
4. `P1 composition_regen_review`: 23件を contact sheet で見て、退屈な横長化だけを再生成へ送る。全件自動再生成にはしない。
5. `P2 visual_review`: 22件を低スコア順に確認し、濃淡・線密度が実害か、単に構図が豊かなだけかを分ける。
6. `P3 light_review`: 各章から抜き取り、スコアが高いのに意味が弱い画像がないかを確認する。

## 完了条件

- `ledgers/ponchi_regen_review_plan.csv` の60件に `regen_decision` が入る。
- `再生成` と `公式素材確認待ち` の件数が分かる。
- 「scoreが高いが退屈」な例を最低5件、「scoreが中位だが採用可能」な例を最低5件メモする。
- その結果をもとに、次の再生成バッチを20件以内で切る。
