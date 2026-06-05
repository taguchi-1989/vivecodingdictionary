# Semantic Regeneration and Retest Plan

作成日: 2026-06-05

対象: `docs/ponchi_semantic_audit/blind_quiz_2026-06-05/blind_quiz_run_001_results.md` の Run 001 で `misleading` または高リスクに分類された B 章 / D 章画像。

## 目的

今回の目的は「画像の情報量を増やす」ことではなく、タイトルを隠した状態でも、その画像が候補群の中で何を指しているかを誤解しにくくすること。

許容する混同:

- 同じブランド系列内の世代差: `Claude 4 系` と `Claude 4.5 系`、`Gemini 2 系` と `Gemini 3 系` など。
- 同じ用途カテゴリ内の弱い迷い: coding assistant 同士、動画生成モデル同士など。ただし高確信の誤答は改善対象にする。

優先して直す混同:

- 別サービスを高確信で指している画像。
- モデルの種類を取り違える画像。例: reasoning model が音声認識に見える、動画生成が静止画生成に見える。
- 料金・運用・管理形態など、本文の主題があるのに、単なるブランド一般画像に見えているもの。

## Run 001 の判断

P0 は全て再生成候補にする。理由は top1 が誤答で、かつ信頼度が高く、今の画像が別エントリの視覚語彙を強く出しているため。

| priority | entry | title | wrong top1 | confidence | 初期判断 |
| --- | --- | --- | --- | ---: | --- |
| P0 | `B-26` | Azure OpenAI | `B-27` Vertex AI | 72 | 企業 Azure 管理・リージョン・SLA を絵で出す |
| P0 | `B-31` | Excalidraw | `B-6` Windsurf | 88 | 手描きラフ図 / ホワイトボードへ寄せる |
| P0 | `B-5` | GitHub Copilot | `B-4` Cursor | 70 | IDE 製品ではなく補完・PR・GitHub 文脈へ寄せる |
| P0 | `B-52` | Gemini の料金プラン | `B-1` Gemini | 95 | Gemini 本体ではなく料金段差・選択表を主役にする |
| P0 | `B-6` | Windsurf | `B-4` Cursor | 74 | 単一エディタ画面ではなく agentic cascade / project-wide flow に寄せる |
| P0 | `D-22` | o1 系 | `D-71` Whisper | 84 | 音声・波形を消し、推論・熟考・比較を主役にする |
| P0 | `D-53` | Veo | `D-51` Imagen | 82 | 静止画生成ではなく動画・時間軸・カメラワークを主役にする |
| P0 | `D-58` | Whisk | `D-57` Flow | 76 | 動画制作ではなく複数画像のリミックスを主役にする |
| P0 | `D-70` | Amical | `D-58` Whisk | 83 | 題材が本文とブランド監査で不一致。先にスコープ確定 |

## スコープ

Wave 1 では P0 の 9 件だけを対象にする。P1/P2 は、Wave 1 の結果を見て「クラスタ全体の構図ルール」として別 wave に回す。

Wave 1 の狙い:

- 高確信誤答を消す。
- 既存の高密度品質を維持する。
- final 画像は上書きせず、候補画像として出す。
- 画像単体の正解率だけでなく、混同相手を入れた小さな再テストで確認する。

Wave 1 から除外するもの:

- D 章の世代差全体の一括修正。
- B 章の coding assistant 全体再設計。
- `P1 generic` の全件再生成。

ただし `B-5` と `B-6` は P0 なので、coding assistant クラスタ内でも先に触る。

## 再生成方針

共通ルール:

- 画像内のタイトル文字で正解させない。
- ロゴを大きくするだけで解決しない。
- 密度を増やすだけで解決しない。
- 「そのエントリ固有の利用場面 / 判断軸 / 入出力」を主役にする。
- 混同相手の視覚語彙を明示的に避ける。
- 公式ロゴが必要なものは、既存の deterministic overlay 前提を維持する。

### B-26 Azure OpenAI

問題: 現行プロンプトが「左右にブロック」まで抽象化されており、Google Cloud / Vertex AI 的な汎用クラウド AI 図に見える。

改善案:

- 左に OpenAI 直 API の軽量プロトタイプ、右に Azure 管理の企業導入を対比する。
- 右側は企業ネットワーク、リージョン境界、監査ログ、SLA、Azure Monitor 的な運用メーターを無文字アイコンで出す。
- モデルそのものより「同じモデルを Azure の管理境界内に置く」ことを絵にする。
- Google 風の sparkle、マルチモデル hub、汎用クラウド AI パレットを避ける。

再テスト時の混同相手: `B-24` Google Cloud、`B-25` Azure、`B-27` Vertex AI、`B-1` Gemini。

### B-31 Excalidraw

問題: 手描き作図ツールではなく、アプリ構築 / agentic IDE に見えている。

改善案:

- 中央の主役を「手描き風ホワイトボード」にする。
- Before は箇条書きメモだけで困っている状態、After はラフな箱・矢印・付箋で整理された状態。
- 線は意図的にラフ、角丸・矢印・付箋・ペンを大きく出す。
- コードエディタ、タスクカード、ビルド画面、複数ファイルの変更フローを避ける。

再テスト時の混同相手: `B-6` Windsurf、`B-32` Figma、`B-33` Canva、`F-140` Mermaid が候補に入る場合はそれも入れる。

### B-5 GitHub Copilot

問題: 大きな IDE 画面に見え、Cursor と区別しづらい。

改善案:

- 「GitHub 上の開発フローに寄り添う補完」として描く。
- IDE 画面は補助に留め、ghost completion、PR review、repo branch、issue から code suggestion への流れを主役にする。
- 一つの巨大エディタ画面ではなく、コード補完と GitHub 側のレビュー補助を並べる。
- standalone editor / AI IDE / project-wide agent flow を避ける。

再テスト時の混同相手: `B-4` Cursor、`B-6` Windsurf、`B-7` Claude Code、`B-8` Codex。

### B-52 Gemini の料金プラン

問題: Gemini ブランド一般として強く読まれ、料金プランの画像になっていない。

改善案:

- 3 段の料金・利用量・機能範囲の比較を主役にする。
- Free / Pro / Ultra の文字を直接読ませる必要はないが、段差、価格タグ、利用量メーター、機能チェック数の増加を明確にする。
- Gemini 本体の対話画面やモデル hub を主役にしない。
- Vertex AI への法人 API 課金と混ざらないよう、個人向けプラン比較の文脈に寄せる。

再テスト時の混同相手: `B-1` Gemini、`B-27` Vertex AI、`B-50` Claude 料金、`B-51` ChatGPT 料金。

### B-6 Windsurf

問題: Cursor 的な AI IDE に見えている。エディター同士の混同なので重症度は相対的に低いが、P0 の高確信誤答なので直す。

改善案:

- 単一ファイル編集画面ではなく、複数ファイル、テスト、ブラウザ確認、タスク分解をまたぐ agentic cascade を主役にする。
- 「依頼 → 計画 → 複数箇所変更 → テスト → 結果確認」の流れを大きく出す。
- Cursor 風のチャット付きエディタ、単一中央 editor、補完 UI を避ける。
- ブランド素材が blocked のため、ロゴ依存ではなく概念差で識別させる。

再テスト時の混同相手: `B-4` Cursor、`B-5` GitHub Copilot、`B-7` Claude Code、`B-8` Codex。

### D-22 o1 系

問題: 音声・波形に見える具体物があり、Whisper と誤認されている。

改善案:

- 音声波形、マイク、録音、字幕、スピーカーを禁止。
- 「速い汎用モデル」と「遅い reasoning model」の比較に戻す。
- o1 側は深い思考、長い推論ラダー、数学・ロジック・コード最適化の難問カードを主役にする。
- o1-preview / o1 / o1-mini / o1-pro の系列感は、読めない小ラベルではなく縦のバリアント段差で表す。

再テスト時の混同相手: `D-20` GPT-5 系、`D-21` GPT-4 系、`D-23` o3 系、`D-71` Whisper。

### D-53 Veo

問題: Imagen 的な静止画生成に見えている。

改善案:

- 動画の時間軸を最重要要素にする。
- frame strip、playhead、camera path、motion arrows、scene consistency を大きく出す。
- 1 枚絵のギャラリー、画像生成の before/after、静止画バリエーションだけの構図を避ける。
- Flow とは「Veo はエンジン、Flow は制作ツール」という関係が見えるよう、中央にモデルエンジン、右に複数の利用口を置く。

再テスト時の混同相手: `D-51` Imagen、`D-52` Sora、`D-56` Seedance、`D-57` Flow。

### D-58 Whisk

問題: Flow / Veo 的な動画制作ワークフローに見えている。

改善案:

- 複数の参照画像カードを混ぜて、1 つの合成画像またはスタイル違いバリエーションにする絵を主役にする。
- 入力側は subject / scene / style のような画像材料、出力側は合成結果カード。
- タイムライン、playhead、動画フレーム列、カメラワークを避ける。
- Imagen との関係は「画像生成エンジンを使う remix tool」として控えめに示す。

再テスト時の混同相手: `D-51` Imagen、`D-53` Veo、`D-55` Nano Banana、`D-57` Flow。

### D-70 Amical

問題: Run 001 では Whisk と誤認された。さらに `docs/brand_usage_audit.md` では Amical が local-first AI dictation / note-taking app と確認されている一方、現在の本文は韓国系医療 AI ソリューションとして書かれており、題材が一致していない。

改善案:

- 画像再生成の前に、D-70 の本文スコープを確定する。
- local-first dictation / note-taking app として扱うなら、音声入力、ローカル処理、ノート化、プライバシー境界を主役にする。
- 現在本文の医療 AI ソリューションとして扱うなら、公式ロゴ・ブランド監査との不一致を解決してから描く。
- Whisk / Imagen 系の画像カード、リミックス、生成バリエーションは避ける。

再テスト時の混同相手: `D-58` Whisk、`D-71` Whisper、`B-18` Aqua Voice、`B-13` ElevenLabs。

## 生成と検証の流れ

1. 対象確定
   - Wave 1 は P0 9 件。
   - D-70 は本文スコープ確定待ち。確定しない場合は `blocked_scope` として再生成対象から外す。

2. semantic brief 作成
   - 各 entry に `must_show`, `must_avoid`, `confuser_entries`, `pass_condition` を書く。
   - 既存プロンプトの抽象化語句を、本文固有の判断軸へ置き換える。

3. 候補生成
   - 出力先は `assets/ponchi/experiments/batches/semantic-regen-001/`。
   - 1 entry につき原則 2 案作る。D-70 はスコープ確定後のみ。
   - official overlay 対象は既存の clearspace / deterministic overlay ルールに従う。

4. 機械監査
   - `scripts/ponchi_image_audit.py` でサイズ、密度、clearspace を確認する。
   - `scripts/ponchi_color_audit.py` または `scripts/ponchi_quality_score.py` 系で色・線密度の逸脱を確認する。
   - 機械監査で `review` になったものは、意味が良くてもそのまま昇格しない。

5. 目視ショートレビュー
   - 旧画像、新候補 A、新候補 B、混同相手画像を並べた contact sheet を作る。
   - ここではタイトルありで「改善方向が合っているか」を見る。

6. ブラインド再テスト
   - タイトルを消した affected cluster quiz を作る。
   - 対象画像、旧 top1 誤答、top2/top3 混同相手、近傍カテゴリを同じ候補リストに入れる。
   - 少なくとも 1 agent、可能なら 2 agent に回答させる。
   - 回答は top1/top3/confidence/reason を記録する。

7. 合否判定
   - P0 合格: top1 正解、confidence >= 70、かつ旧誤答への高確信誘導が消えている。
   - 条件付き合格: top1 正解だが confidence 50-69。旧画像より改善していれば P2 として保留可能。
   - 不合格: top1 誤答、または wrong confidence >= 60。
   - D-70 は本文スコープが未確定なら、画像の出来に関わらず final 昇格不可。

8. staging
   - 合格候補は `assets/ponchi/final_candidates/semantic-regen-001/` に置く。
   - `assets/ponchi/final/` はまだ触らない。
   - final 昇格は別途、ユーザー確認後に実施する。

## 実行時の成果物

- `docs/ponchi_semantic_audit/semantic_regen_retest_plan_2026-06-05.md`
- `ledgers/ponchi_semantic_regen_scope_2026-06-05.csv`
- `assets/ponchi/experiments/batches/semantic-regen-001/`
- `docs/ponchi_semantic_audit/semantic_regen_001/`
- `docs/ponchi_semantic_audit/semantic_regen_001/blind_retest_results.md`
- `docs/ponchi_semantic_audit/semantic_regen_001/blind_retest_problem_queue.csv`

## OK 後に開始する作業

ユーザー OK 後、次の goal として開始する。

Goal 案:

`P0 semantic-regen wave 1: B/D の高確信誤認 9 件について、改善 brief 作成、候補画像生成、機械監査、ブラインド再テスト、合否レポート作成まで実施する`

開始直後の判断:

- D-70 を `blocked_scope` にするか、local-first dictation / note-taking app として本文・画像側を揃えるかを決める。
- それ以外の 8 件は再生成対象として進める。
