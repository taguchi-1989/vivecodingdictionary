# Ponchi Character Bible

作成日: 2026-05-31

## 目的

ポンチ絵を再生成するときに、毎回違う人物・ロボットに見えないようにするための固定キャラ基準。画像ごとの主題は変えてよいが、人物の造形、服、線の密度、ロボットの形はこの文書に合わせる。

## 共通スタイル

- 白い紙に黒・グレー・指定青だけのクリーンな線画。
- 人物は実在人物に似せない。
- 顔は最小限の記号表現。目は小さい点、鼻は省略可、口は短い線。
- 髪型や服装はシンプルにし、流行や職業コスプレに寄せない。
- かわいいマスコット絵、漫画的な誇張、リアルな肖像、3D、写真風は禁止。
- 手足は読みやすい比率。極端な頭身、極端な幼児化、過剰な表情は禁止。

## 固定キャラ

この 3 名構成は `drafts/IMAGE_GEN_POLICY_v2.md` の「著者の決定（2026-05-24 確定）」に合わせる。

### Character A: Reader Woman

用途: 読者視点、要件確認、操作、説明、判断。女性キャラを「聞き手専用」に固定しない。

- 成人女性に見えるが、個人を特定できない中性的な顔。
- 肩くらいの黒髪。単純な外形で、細かい髪束は描かない。
- 白または極薄グレーのトップスに、黒または濃グレーのカーディガン風の線。
- 体型は標準。片手を軽く上げて質問・確認している姿勢が基本。
- アクセサリー、柄物、ブランド風の服は禁止。

### Character B: Teacher Man

用途: 開発者視点、設計、レビュー、操作、説明、質問。男性キャラを「先生専用」に固定しない。

- 成人男性に見えるが、個人を特定できない中性的な顔。
- 短い黒髪。前髪は少しだけ横に流す。
- 丸首の薄グレーの長袖トップス。
- 黒または濃グレーのシンプルなパンツ。
- 体型は標準。姿勢は落ち着いていて、片手で図を指すかノート PC に向かう。
- 眼鏡、髭、ロゴ入り服、帽子は基本禁止。

### Character C: Pet Robot

用途: AI、AI補完、AIエージェント、モデル、見えない処理の擬人化。

- 小型の卓上ロボットまたは半身ロボット。
- 頭は角丸長方形、体は小さな台形または箱形。
- 顔は黒い点の目 2 つだけ。口、眉、感情過多な表情は使わない。
- 腕は細い線、手は丸いミトン形。
- 体色は白または極薄グレー。青は発光点やアクティブ状態にだけ使う。
- アンテナは 1 本まで。翼、耳、尻尾、動物的特徴は禁止。
- 企業ロゴ、胸のマーク、文字、画面表示は禁止。

## 使い分け

- 読者の理解、疑問、要件確認: Character A を主役にしやすいが、説明役にもしてよい。
- 開発ツールや言語、説明、設計: Character B を主役にしやすいが、確認役や質問役にもしてよい。
- AI の支援や自律処理: Character C を小さく添える。
- 1 枚に全員を入れる必要はない。主題が弱くなる場合は 1 人だけでよい。
- 人物が不要な純粋な概念図では、キャラを入れず図形だけでもよい。

## 役割ローテーション

技術力や判断力を性別に紐づけない。キャラクターの見た目は固定するが、絵の中の役割は回ごとに変える。

使える `role_balance`:

| 値 | 構図 |
| :-- | :-- |
| `male_explains` | Character B がボードを示し、Character A が確認する |
| `female_explains` | Character A がボードを示し、Character B が確認する |
| `both_review` | 2 人とも同じ図を見て共同レビューする |
| `female_operates_male_checks` | Character A が PC 操作、Character B が結果確認 |
| `male_operates_female_checks` | Character B が PC 操作、Character A が結果確認 |
| `solo_female_works` | Character A だけで操作・確認する |
| `solo_male_works` | Character B だけで操作・確認する |
| `robot_supports` | Character C が小さな記号カードで補助し、人間が確認する |
| `diagram_only` | 人物もロボットも出さず、図解だけで見せる |

同じ `role_balance` を連続させすぎない。特に「男性が説明、女性が聞く」構図だけに偏らないようにする。

## 手とポーズ

手や指は破綻しやすいため、ポーズは単純にする。

避ける構図:

- 両手を大きく見せる説明ポーズ。
- 指差しとペン持ちを同時にさせる。
- 片手に複数の物を持たせる。
- 人物 2 人が同時に細かい物を操作する。
- 手前に大きな手を置く。
- Character C を含めて全員に棒やペンを持たせる。

推奨:

- 片手だけを軽く上げる。
- もう片方の手は机、ノート、PC の陰に隠す。
- 説明は手のポーズではなく、ボード上の矢印、ノード、チェックで表現する。
- 持ち物は 1 人 1 つまでにする。

## プロンプト共通ブロック

```text
Character continuity: use the same recurring simple characters across the
series. If a reader/listener is needed, use Character A: an anonymous adult
woman with shoulder-length black hair, minimal dot eyes, a white or very light
gray top with a dark simple cardigan outline, no accessories, no patterned
clothing. If a teacher/developer/explainer is needed, use Character B: an
anonymous adult man with short black hair, minimal dot eyes, a light gray plain
long-sleeve shirt, dark simple pants, no glasses, no beard, no logo clothing.
If AI assistance is needed, use Character C: a small pet robot with a
rounded-rectangle head, two dot eyes, a small box body, thin line arms, white or
very light gray body, and blue only as a tiny active-status accent. Keep faces
symbolic and non-identifiable. Do not create new mascot designs, animal
features, realistic portraits, brand marks, text, or clothing logos.
Keep the character identities stable but rotate their roles. Do not always make
the man the explainer and the woman the listener. Use simple poses with at most
one clear hand gesture per person, and express explanations with arrows, nodes,
and checks rather than complex fingers or hand-held objects.
```

## 目視確認

再生成後に確認すること:

- Character A/B/C のどれかとして識別できるか。
- 前回画像と服・髪型・ロボット形状が大きく変わっていないか。
- 顔が具体的すぎないか。
- ロボットが企業マスコットや動物風になっていないか。
- キャラが主題を邪魔していないか。
- 性別による説明役・聞き手役の固定化が起きていないか。
- 手、指、持ち物が破綻していないか。
