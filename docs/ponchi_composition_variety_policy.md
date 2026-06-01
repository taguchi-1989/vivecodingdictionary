# Ponchi Composition Variety Policy

作成日: 2026-05-31

## 目的

2:1 再生成では、同じ絵柄や同じ人数構成を増やすのではなく、エントリの説明目的に合わせて構図の型を使い分ける。シリーズとしての統一感は、色、線、キャラ、余白、ロゴ後合成ルールで保ち、画面の組み方は意図的に変える。

## 基本方針

- 1 バッチに同じ構図を並べすぎない。
- `2人 + ロボット + 机 + PC` を標準形にしない。
- 「説明したい概念」が主役で、人物は必要な時だけ添える。
- ブランド系は公式ロゴ後合成の余白を確保するが、絵を小さくしすぎない。ロゴ予定地以外は主図解や人物で意味のある密度にする。
- どの型でも、読める文字、偽ロゴ、実在 UI、ブランドカラーは入れない。

## 構図ファミリー

| family | 用途 | 主な `composition_type` | 使いどころ |
| :-- | :-- | :-- | :-- |
| `concept_map` | 要素の関係を見せる | `diagram_first`, `cards_on_wall` | 言語、ランタイム、エコシステム |
| `process_flow` | 入力から出力への流れ | `diagram_first`, `robot_console` | LLM、エージェント、生成処理 |
| `before_after` | 問題と改善を対比する | `board_review`, `single_laptop` | 型、安全性、レビュー、補完 |
| `layer_stack` | 階層・責務分担を見せる | `standing_board`, `diagram_only` | モデル階層、環境、抽象化 |
| `collaboration_hub` | 人や機能が集まる場所 | `cards_on_wall`, `logo_clearspace` | GitHub、チーム開発、PR、Issue |
| `timeline_scale` | 時系列・規模変化を見せる | `diagram_only`, `standing_board` | モデル世代、文脈長、性能変化 |
| `tool_loop` | 操作、検証、差分、戻りを見せる | `single_laptop`, `robot_console` | CLI、ローカル作業、テスト、修正 |
| `brand_clearspace` | 公式ロゴを後合成する | `logo_clearspace` | サービス名が読者理解に必要な項目 |

## バッチ運用ルール

5 枚程度をまとめて試す場合は、次を満たす。

- 最低 3 種類以上の `family` を含める。
- 同じ `family` は連続 2 枚まで。
- 人物あり、ロボットあり、図解のみを混ぜる。
- `role_balance` は最低 3 種類を混ぜる。
- ブランドロゴが必要な画像は、生成時点では白い余白だけを作る。
- ブランドロゴが必要な画像でも、右半分や上半分を空き地にしない。

## scene_brief 追加項目

`scene_brief` には `composition_family` を追加する。

```yaml
composition_family:
composition_type:
composition_density: compact | balanced | spacious
```

`composition_family` は上表から選び、`composition_type` は具体的な画面の組み方を選ぶ。

## 次の応用バッチ

| entry_id | family | composition_type | ねらい |
| :-- | :-- | :-- | :-- |
| `F-1 JavaScript` | `concept_map` | `diagram_first` | 中央コアからブラウザ、サーバ、型、UI へ広がる |
| `F-2 TypeScript` | `before_after` | `single_laptop` | 気づけない不具合と、型で先に気づく差を見せる |
| `G-1 Context` | `timeline_scale` | `diagram_first` | 入る情報、外れる情報、文脈窓の広がりを見せる |
| `J-14 LLM` | `process_flow` | `diagram_first` | 入力、モデル層、出力の流れを主役にする |
| `F-60 GitHub` | `collaboration_hub` | `logo_clearspace` | 共同作業ハブと公式ロゴ後合成の余白を両立する |

この 5 枚は、同一スタイルの量産ではなく、ルール検証用の応用パターンとして扱う。本番差し替え前に、各画像を `OK`, `微修正`, `再生成`, `公式ロゴ合成待ち` に分類する。
