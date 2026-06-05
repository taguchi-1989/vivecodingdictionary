# Ponchi Semantic Audit Findings 2026-06-05

## Scope

Current `assets/ponchi/final/*.webp` 350件を対象に、画像品質ではなく「情報密度が項目理解に効いているか」を目視確認した。

参照シート:

- `docs/ponchi_semantic_audit/ponchi-semantic-audit-A.png`
- `docs/ponchi_semantic_audit/ponchi-semantic-audit-B.png`
- `docs/ponchi_semantic_audit/ponchi-semantic-audit-C.png`
- `docs/ponchi_semantic_audit/ponchi-semantic-audit-D.png`
- `docs/ponchi_semantic_audit/ponchi-semantic-audit-E.png`
- `docs/ponchi_semantic_audit/ponchi-semantic-audit-F.png`
- `docs/ponchi_semantic_audit/ponchi-semantic-audit-G.png`
- `docs/ponchi_semantic_audit/ponchi-semantic-audit-H.png`
- `docs/ponchi_semantic_audit/ponchi-semantic-audit-I.png`
- `docs/ponchi_semantic_audit/ponchi-semantic-audit-J.png`
- `docs/ponchi_batch_audits/lightweight-regen-current-final-92-contact-sheet.png`

## Overall Judgment

旧版の「白地に薄い線だけ」「2:1に広げただけ」「サムネイルで弱い」問題は大きく減った。特に軽量再生成92件は、`final.webp` では全件 2026-06-04 22:31 に更新済みで、情報量そのものは増えている。

一方で、新しい問題として次が見える。

- 密度は高いが、汎用UIパネル・ダッシュボード・カード列に寄りすぎて、項目固有の特徴が弱い。
- ブランド/サービス系で、ロゴが識別を担い、絵の中身は「AIっぽい操作画面」に留まるものがある。
- 同一カテゴリ内で差分が弱い。特にコーディング支援サービス、モデル世代、MCPツール、GPU/CPU周辺。
- 一部は色ゲートfailや低スコアよりも、意味上の差別化不足が本質的な問題。

## Priority Queue

| priority | entry | issue | recommended action |
| --- | --- | --- | --- |
| P0 | `J-72 H100` | 情報密度はあるが、H100固有の特徴より汎用データセンター/チップ図に寄る。色failとlowも重なる。 | H100の用途、GPUクラスタ、推論/学習負荷の流れを主役に再調整 |
| P0 | `J-73 Blackwell` | H100との差が弱い。Blackwell世代の特徴が見えにくい。色failとlowも重なる。 | 世代更新、複数GPU、性能/規模の伸びをH100と対になる構図で再調整 |
| P0 | `F-84 Ghostty` | 低スコア継続。黒画面と端末風要素はあるが、シリーズ内で外れ値。 | 端末アプリとしての軽快さ、設定、シェル実行を白黒青の範囲で再設計 |
| P1 | `D-35 Cursor Composer` | 余白とロゴ依存が強く、Composer固有の「複数ファイル編集/差分作成」が弱い。 | sparse diagramから再構図 |
| P1 | `J-42 Web3` | ネットワーク図としては直接的だが、分散・所有・台帳の意味が弱く、汎用ノード図に見える。 | 分散台帳、ユーザー、トークン/権限の関係を明示 |
| P1 | `A-6 評価日・時変情報の見方` | 構図の意味はあるが色fail。 | 色補正優先。意味再生成は不要寄り |
| P1 | `I-10 Filesystem MCP` | 意味は明確だが色fail。 | 色補正優先 |
| P1 | `J-55 個人情報保護法` | 法/保護の文脈は出ているが色fail。 | 色補正優先 |
| P1 | `J-76 CPU` | CPU図としては意味があるが色fail。 | 色補正優先 |

## Category-Level Review

### B: ブランド/サービス

情報量は増えたが、`B-4 Cursor`, `B-5 GitHub Copilot`, `B-6 Windsurf`, `B-7 Claude Code`, `B-8 Codex`, `B-15 Microsoft Copilot`, `B-16 Microsoft 365 Copilot`, `B-17 Edge Copilot`, `B-19 Claude Cowork` は、並べると「人物 + エディタ/ダッシュボード + ロゴ」に寄りやすい。ロゴを隠すと項目差が弱いものがある。

次回はこの群をまとめて、各サービスの「使われ方の差」を1行で定義してから、差が出ていないものだけ作り直す。

### C: 企業/人物

人物・企業系は全体として採用可能。ただし人物項目は、本人の役割や代表的文脈より「人物 + AI/組織パネル」の汎用絵になりやすい。`C-51`, `C-56`, `C-59` など低〜中位のものは、画像品質よりも人物固有性の確認が必要。

### D: モデル/生成AI

`D-1` から `D-26` のモデル世代系は、ロゴと性能パネルで統一されているが、世代間差が読み取りにくい。個別再生成ではなく、モデル世代の構図ルールを一度決め直すべき。

画像生成/動画生成系の `D-50` 以降は、写真サムネイル風の要素が多いが、用途の意味は比較的出ている。色・公式素材の扱いを確認する。

### E: ベンチマーク

E章は比較的良い。評価問題、回答、採点、ランキングの流れが見えやすく、情報密度が意味に乗っている。`E-25`, `E-26`, `E-27`, `E-30`, `E-50` は composition review に残っているが、意味監査上は大きな優先ではない。

### F: ツール/言語

ロゴやアプリ画面に助けられているものが多い。言語系・拡張機能系は、ロゴを除くと「開発環境パネル」に見えやすい。`F-84 Ghostty` はP0。その他は全件再生成ではなく、章内で似すぎているものを比較レビューする。

### G: Codex/LLM概念

概念図としてはかなり良い。`G-1 Context`, `G-5 Context Window`, `G-13 Few-shot Learning`, `G-15 RAG`, `G-19 Prompt Caching`, `G-31 Hook`, `G-47 Auto-compact` などは、密度が意味に乗っている。大きな再生成対象は少ない。

### H: ワークフロー

H章も比較的良い。TDD, Scrum, Git Flow, CI/CD, DevOps は流れが読み取れる。`H-50` 以降はやや抽象化しているが、シリーズとしては許容範囲。

### I: MCP

I章は全体としてMCPらしい接続・ツール呼び出しの表現が揃っている。ただしツール別の差分は小さい。`I-10 Filesystem MCP`, `I-20 Playwright MCP`, `I-22 Chrome DevTools MCP`, `I-41 SQLite MCP`, `I-50 AWS MCP` は比較的意味が出ている。`I-21 Puppeteer MCP` はPlaywrightとの差分確認対象。

### J: 一般AI/技術

軽量再生成でかなり改善したが、ハードウェア群は差分レビューが必要。`J-72 H100`, `J-73 Blackwell` はP0。`J-78 HDD`, `J-79 SSD`, `J-80 SATA`, `J-81 M.2` は意味は明確なので、色/密度の確認は必要だが全再生成ではない。

`J-12 Neural Network` や `J-42 Web3` はシンプルで直接的だが、今のシリーズ内では情報密度が低く見える。意味としては通るが、誌面の見栄えでは再構図候補。

## Next Steps

1. P0の3件を先に直す。
2. 色failだが意味が通っている4件は、再生成ではなく色補正で済むか確認する。
3. B章のコーディング支援サービス群を横並び比較し、ロゴなしでも違いが残るか確認する。
4. D章のモデル世代群は、世代差を見せる共通ルールを決めてから必要分だけ再生成する。
5. 残りは全件再生成ではなく、章内で似すぎている群だけをレビューキューに入れる。
