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

用途: 読者、聞き手、非エンジニア視点、要件を確認する人。

- 成人女性に見えるが、個人を特定できない中性的な顔。
- 肩くらいの黒髪。単純な外形で、細かい髪束は描かない。
- 白または極薄グレーのトップスに、黒または濃グレーのカーディガン風の線。
- 体型は標準。片手を軽く上げて質問・確認している姿勢が基本。
- アクセサリー、柄物、ブランド風の服は禁止。

### Character B: Teacher Man

用途: 教える人、説明者、開発者視点、設計・レビュー・ターミナル操作。

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

- 読者の理解、疑問、要件確認: Character A を主役にする。
- 開発ツールや言語、説明、設計: Character B を主役にする。
- AI の支援や自律処理: Character C を小さく添える。
- 1 枚に全員を入れる必要はない。主題が弱くなる場合は 1 人だけでよい。
- 人物が不要な純粋な概念図では、キャラを入れず図形だけでもよい。

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
```

## 目視確認

再生成後に確認すること:

- Character A/B/C のどれかとして識別できるか。
- 前回画像と服・髪型・ロボット形状が大きく変わっていないか。
- 顔が具体的すぎないか。
- ロボットが企業マスコットや動物風になっていないか。
- キャラが主題を邪魔していないか。
