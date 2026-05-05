# 要直しキュー（revision queue）

*自動生成: 2026-05-06 06:20 / `scripts/update_review_queue.py`*

1 画面で「次やるべき・見直すべき・適合済み」が見えるダッシュボード。`scripts/validate_entry.py` のチェックを全件で走らせた結果を集計して再生成しています。手で編集しないでください。

## status 内訳

- **drafting**: 10 件
- **needs_review**: 256 件
- **ready**: 85 件
- **archived**: 39 件
- **合計**: 390 件

## ☆ 違反あり（最優先で直す）（0 件）

_なし_

## ⚠️ 警告あり（軽微超過 / 著者か entry-writer で手当て）（96 件）

| ID | title | status | 概要 |
| :-- | :-- | :-- | :-- |
| B-1 | Gemini | needs_review | ⚠ 「非エンジニアのつまずき」に記入あり（- プレビュー期間が長くモデルが安定しないので、業務で使うとき |
| B-13 | ElevenLabs | ready | ⚠ 「非エンジニアのつまずき」に記入あり（- そもそも聞いたことがなく、何のサービスかわからない人が多い; ⚠ 「私のコメント」の 第一印象 に記入あり（AI ニュースで紹介された音声があまりに自然でびっくりしま; ⚠ 「私のコメント」の 良い点 に記入あり（感情のこもった言い回しを軽く出せます） — 著者の記入なら  |
| B-17 | Edge Copilot | ready | ⚠ 「非エンジニアのつまずき」に記入あり（- 入力内容が学習に使われるか分かりづらく、業務情報を入れてよ; ⚠ 「私のコメント」の 第一印象 に記入あり（Bing Image Creator 時代に触り、ブラウザ; ⚠ 「私のコメント」の 良い点 に記入あり（無料で誰でもすぐに触れる手軽さです） — 著者の記入なら O |
| B-2 | Claude | ready | ⚠ 「非エンジニアのつまずき」に記入あり（- システムエンジニアからの評価が高い理由が最初わからなかった; ⚠ 「私のコメント」の 第一印象 に記入あり（環境構築が思ったより大変でした（VS Code や Nod; ⚠ 「私のコメント」の 良い点 に記入あり（Claude Code がファイル編集まで自動実行してくれた |
| B-20 | Vercel | ready | ⚠ 「非エンジニアのつまずき」に記入あり（- 無料枠から Pro にアップグレードしたら無料分が消えた感; ⚠ 「私のコメント」の 第一印象 に記入あり（Web アプリを作らせると Next.js のデプロイ先と; ⚠ 「私のコメント」の 良い点 に記入あり（環境変数を入れれば Supabase や Discord な |
| B-23 | AWS | ready | ⚠ 「非エンジニアのつまずき」に記入あり（- カード情報の登録時にエラーで弾かれることが多く、会員登録の; ⚠ 「私のコメント」の 第一印象 に記入あり（「クラウドといえばここ」のデファクトスタンダードという印象; ⚠ 「私のコメント」の 良い点 に記入あり（幅が広く、LLM に頼めば設定もそのまま実行してくれます。閉 |
| B-28 | Render | ready | ⚠ 「非エンジニアのつまずき」に記入あり（- 環境変数（API キーなど）をどこに入れるかが分かりづらく; ⚠ 「私のコメント」の 第一印象 に記入あり（LLM が「このタイプなら Render」と勧めてくる候補; ⚠ 「私のコメント」の 良い点 に記入あり（Python アプリ（FastAPI / Flask）を無料 |
| B-3 | ChatGPT | ready | ⚠ 「非エンジニアのつまずき」に記入あり（- ChatGPT と Codex（同じ OpenAI 製）の; ⚠ 「私のコメント」の 第一印象 に記入あり（タイピングミスや音声認識のずれがあっても意図をくみ取ってく; ⚠ 「私のコメント」の 良い点 に記入あり（更新が早く、フロンティアモデルとしての優等生感があります。バ |
| B-30 | Amazon Bedrock | ready | ⚠ 「非エンジニアのつまずき」に記入あり（- 導線が分かりにくく、AWS 自体の知識（IAM・コンソール; ⚠ 「私のコメント」の 第一印象 に記入あり（LLM に「API をセキュアに業務利用したい」と相談する; ⚠ 「私のコメント」の 良い点 に記入あり（エンタープライズレベルのセキュリティ・データ保護要件を満たし |
| B-31 | Excalidraw | ready | ⚠ 「非エンジニアのつまずき」に記入あり（- 手書き風の見た目が個人的にはあまり好みではなく、最初の見た; ⚠ 「私のコメント」の 第一印象 に記入あり（AI 系の YouTuber が解説動画でよく画面に出して; ⚠ 「私のコメント」の 良い点 に記入あり（無料でラフ図がブラウザ起動だけで描けるそうです） — 著者の |
| B-4 | Cursor | ready | ⚠ 「非エンジニアのつまずき」に記入あり（- Cursor を入れても VS Code との違いがよくわ; ⚠ 「私のコメント」の 第一印象 に記入あり（AI ニュース界隈で「良い」と騒がれていた印象でした） —; ⚠ 「私のコメント」の 良い点 に記入あり（コードをちゃんと書く人には良いです） — 著者の記入なら O |
| B-5 | GitHub Copilot | ready | ⚠ 「非エンジニアのつまずき」に記入あり（- 「GitHub」という言葉自体にアレルギーがあり入りにくか; ⚠ 「私のコメント」の 第一印象 に記入あり（Claude Code と比べると使いづらく感じました） ; ⚠ 「私のコメント」の 良い点 に記入あり（アップデートが頻繁で、いまではエージェント的な操作もできるよ |
| B-50 | Claude の料金プラン | ready | ⚠ 「非エンジニアのつまずき」に記入あり（- Claude Code は無料では使えず、Pro でも上限; ⚠ 「私のコメント」の 第一印象 に記入あり（月 100・200 ドルは高いと感じつつ、周囲の Max ; ⚠ 「私のコメント」の 良い点 に記入あり（Opus はコーディングで折り紙付き、上限が大きいので使い切 |
| B-51 | ChatGPT の料金プラン | ready | ⚠ 「非エンジニアのつまずき」に記入あり（- ChatGPT は無料のままで満足している人に課金してもら; ⚠ 「私のコメント」の 第一印象 に記入あり（月 200 ドルの Pro は最初高すぎと感じたものの、時; ⚠ 「私のコメント」の 良い点 に記入あり（Plus（月 20 ドル）の課金は得られるリターンが圧倒的に |
| C-1 | OpenAI | ready | ⚠ 「非エンジニアのつまずき」に記入あり（- サービスが多くて、ChatGPT 以外（API・DALL·; ⚠ 「私のコメント」の 第一印象 に記入あり（ChatGPT で AI ブームを作ったフロンティア企業と; ⚠ 「私のコメント」の 良い点 に記入あり（流行の先端で切磋琢磨している姿勢が見え、LLM 関連では常に |
| C-10 | Moonshot AI | needs_review | ⚠ 「非エンジニアのつまずき」に記入あり（-これ GL ん違うか？ glm かあ君か君のところで書いた内 |
| C-11 | Z.ai | needs_review | ⚠ 「非エンジニアのつまずき」に記入あり（-お遍。 glm で書いといて欲しいなってところとあと米国企業 |
| C-12 | TSMC | ready | ⚠ 「非エンジニアのつまずき」に記入あり（- 急に出てきた感のある企業名で、熊本に工場ができたと聞きます; ⚠ 「私のコメント」の 第一印象 に記入あり（微細化での高性能化が Intel より強い印象です） — ; ⚠ 「私のコメント」の 良い点 に記入あり（世界最強の技術力で大きな影響を与える企業です） — 著者の記 |
| C-13 | Groq | ready | ⚠ 「非エンジニアのつまずき」に記入あり（- xAI の Grok（グロック）と Groq（グロック）の; ⚠ 「私のコメント」の 第一印象 に記入あり（名前が Grok と混同しやすいです。） — 著者の記入な; ⚠ 「私のコメント」の 良い点 に記入あり（OSS 系モデルを高速に回せます。） — 著者の記入なら O |
| C-14 | AMD | ready | ⚠ 「非エンジニアのつまずき」に記入あり（- 読み方がわかりません…） — 著者の記入なら OK; ⚠ 「私のコメント」の 第一印象 に記入あり（Intel と NVIDIA の対抗馬という印象です） —; ⚠ 「私のコメント」の 良い点 に記入あり（製造を TSMC に委ね微細化で先行しています） — 著者の |
| C-2 | Anthropic | ready | ⚠ 「非エンジニアのつまずき」に記入あり（- 「Anthropic」という社名が読みづらく、「アンソロピ; ⚠ 「私のコメント」の 第一印象 に記入あり（OpenAI からスピンアウトした企業として認識していまし; ⚠ 「私のコメント」の 良い点 に記入あり（倫理観のある AI（Constitutional AI）を掲 |
| C-3 | Google DeepMind | ready | ⚠ 「非エンジニアのつまずき」に記入あり（- 「Google」と「Google DeepMind」の違い; ⚠ 「私のコメント」の 第一印象 に記入あり（Transformer 論文も Google 発で、研究組; ⚠ 「私のコメント」の 良い点 に記入あり（トップランナーの一角として実験的なサービスを次々出し、無料枠 |
| C-4 | Meta AI | ready | ⚠ 「非エンジニアのつまずき」に記入あり（- Llama は OSS で配布されていますが、大きいモデル; ⚠ 「私のコメント」の 第一印象 に記入あり（GAFA の一角という大きな存在として認識していました） ; ⚠ 「私のコメント」の 良い点 に記入あり（Llama などオープンウェイトのモデルを配り続けている姿勢 |
| C-5 | xAI | ready | ⚠ 「非エンジニアのつまずき」に記入あり（- 私だけかもしれませんが、X を使っていないと存在感がわかり; ⚠ 「私のコメント」の 第一印象 に記入あり（Grok 4.1 Fast はコスパが良いと噂で聞きました; ⚠ 「私のコメント」の 良い点 に記入あり（三大 AI に対し第 4 の軸として立ちつつある点です） — |
| C-51 | Dario Amodei | ready | ⚠ 「非エンジニアのつまずき」に記入あり（- ニュースではあまり見かけず、どんな人物か把握しにくいです。; ⚠ 「私のコメント」の 第一印象 に記入あり（Anthropic の創業者ということで、やはりすごい方だ; ⚠ 「私のコメント」の 良い点 に記入あり（エッセイで自身の考えを発信しているのが良さそうです。） —  |
| C-52 | Demis Hassabis | ready | ⚠ 「非エンジニアのつまずき」に記入あり（- Google がすごいのは分かりますが、具体的に誰がすごい; ⚠ 「私のコメント」の 第一印象 に記入あり（AlphaGo や AlphaFold もやっていてすごい; ⚠ 「私のコメント」の 良い点 に記入あり（技術的にはトップの一人なのだと思います） — 著者の記入なら |
| C-53 | Andrej Karpathy | ready | ⚠ 「非エンジニアのつまずき」に記入あり（- 一般ニュースには名前がほとんど出ないため追いにくいです。…; ⚠ 「私のコメント」の 第一印象 に記入あり（バイブコーディングという言葉の生みの親です。） — 著者の; ⚠ 「私のコメント」の 良い点 に記入あり（ブログや動画での発信内容が充実していて参考になります。） — |
| C-54 | Ilya Sutskever | ready | ⚠ 「非エンジニアのつまずき」に記入あり（- OpenAI 以外にも、こうして辞めた人がいるとは知りませ; ⚠ 「私のコメント」の 第一印象 に記入あり（今回初めて知りました） — 著者の記入なら OK; ⚠ 「私のコメント」の 良い点 に記入あり（安全性に関心があるのは良いことだと思います） — 著者の記入 |
| C-55 | Mira Murati | ready | ⚠ 「非エンジニアのつまずき」に記入あり（- OpenAI 退社騒動の際、何が原因で辞めたのかがまだよく; ⚠ 「私のコメント」の 第一印象 に記入あり（AI 分野のトップ研究者の一人という印象です。） — 著者; ⚠ 「私のコメント」の 良い点 に記入あり（まだよく把握できていません。） — 著者の記入なら OK |
| C-56 | Yann LeCun | ready | ⚠ 「非エンジニアのつまずき」に記入あり（- CNN を作った研究者が AI の新潮流になっている点が気; ⚠ 「私のコメント」の 第一印象 に記入あり（CNN を開発した人はすごいです。） — 著者の記入なら ; ⚠ 「私のコメント」の 良い点 に記入あり（よく分かりません。） — 著者の記入なら OK |
| C-57 | Geoffrey Hinton | ready | ⚠ 「非エンジニアのつまずき」に記入あり（- 一般のニュースでは名前を耳にせず馴染みがありません。…） ; ⚠ 「私のコメント」の 第一印象 に記入あり（深層学習を作った人はすごいですね。） — 著者の記入なら ; ⚠ 「私のコメント」の 良い点 に記入あり（よく分かりません。） — 著者の記入なら OK |
| C-58 | Elon Musk | ready | ⚠ 「非エンジニアのつまずき」に記入あり（- 「X やテスラの人」の印象が強いですが、AI 関連でも影響; ⚠ 「私のコメント」の 第一印象 に記入あり（ハイパーループやテスラの創業者で、色々やっている人です） ; ⚠ 「私のコメント」の 良い点 に記入あり（バイタリティと知名度は人類レベルでトップクラスだと思います） |
| C-59 | Jensen Huang | ready | ⚠ 「非エンジニアのつまずき」に記入あり（- NVIDIA の名前は聞きますが、Jensen Huang; ⚠ 「私のコメント」の 第一印象 に記入あり（NVIDIA の舵取りで世界一の企業に育てたのはすごいです; ⚠ 「私のコメント」の 良い点 に記入あり（CUDA を核に、オープン／クローズ戦略が巧みです） — 著 |
| C-6 | Mistral AI | needs_review | ⚠ 「非エンジニアのつまずき」に記入あり（-この辺さ結構ミストラルートとかだとさ重複してるモデルのところ |
| C-60 | Ray Kurzweil | ready | ⚠ 「非エンジニアのつまずき」に記入あり（- シンギュラリティ 2045 年予測でよく名前が出ますが、本; ⚠ 「私のコメント」の 第一印象 に記入あり（予測がうまいとされている人です） — 著者の記入なら OK; ⚠ 「私のコメント」の 良い点 に記入あり（定量的な目標・指標をセットした人です） — 著者の記入なら  |
| C-7 | Hugging Face | ready | ⚠ 「非エンジニアのつまずき」に記入あり（- 使っているものが商用利用可能なのか、単なるテスト用なのかの; ⚠ 「私のコメント」の 第一印象 に記入あり（AI ニュースで実装されたと耳にしました。） — 著者の記; ⚠ 「私のコメント」の 良い点 に記入あり（AI モデルのデファクトスタンダードな置き場です。） — 著 |
| C-8 | Microsoft AI | ready | ⚠ 「非エンジニアのつまずき」に記入あり（- 何かあるとすぐ課金、という Microsoft の企業体質; ⚠ 「私のコメント」の 第一印象 に記入あり（モデルの性能が低いナーフしてる） — 著者の記入なら OK; ⚠ 「私のコメント」の 良い点 に記入あり（エンタープライズ環境でセキュアに使えること） — 著者の記入 |
| C-80 | AI大学 | ready | ⚠ 「非エンジニアのつまずき」に記入あり（- サムネイルがアテンションエコノミー的な印象で少し気になりま; ⚠ 「私のコメント」の 第一印象 に記入あり（AI 関連のかなり幅広い情報を横断的に把握できます。） —; ⚠ 「私のコメント」の 良い点 に記入あり（偏りなくいろんな情報を取れる印象があります。） — 著者の記 |
| C-81 | にゃんた | ready | ⚠ 「非エンジニアのつまずき」に記入あり（- 昔の動画を見ると、すでに陳腐化している内容も多くあります。; ⚠ 「私のコメント」の 第一印象 に記入あり（how to が非常に分かりやすい YouTube チャン; ⚠ 「私のコメント」の 良い点 に記入あり（オフィスワーカーのボリュームゾーンに刺さる構成です。） —  |
| C-82 | まさお | ready | ⚠ 「非エンジニアのつまずき」に記入あり（- ハーネスや段階的配置など専門用語が多く、慣れていないと何を; ⚠ 「私のコメント」の 第一印象 に記入あり（サムネイルの雰囲気がうさん臭く感じました。） — 著者の記; ⚠ 「私のコメント」の 良い点 に記入あり（独自ベンチマークでのモデル評価が素晴らしく、情報も速くて深い |
| C-9 | NVIDIA | ready | ⚠ 「非エンジニアのつまずき」に記入あり（- ソフトウェア会社なのに時価総額世界一という点がイメージしづ; ⚠ 「私のコメント」の 第一印象 に記入あり（プラットフォーマーになると感じたのが 2016〜2018 ; ⚠ 「私のコメント」の 良い点 に記入あり（機械学習のデファクトスタンダードです。） — 著者の記入なら |
| D-11 | Claude 3.5 系 | needs_review | ⚠ 「非エンジニアのつまずき」に記入あり（- Claude 3.5 Sonnet には初代と v2 があ |
| D-12 | Claude 4 系 | needs_review | ⚠ 「非エンジニアのつまずき」に記入あり（- Claude Code が裏でどの版・ティアを使うか意識し; ⚠ 強い断定語「必ず」が入っている可能性（要確認） |
| D-25 | GPT-1 / GPT-2 系 | ready | ⚠ 「非エンジニアのつまずき」に記入あり（- GPT-3 から認知し始めたので、2 という数字が何を意味; ⚠ 「私のコメント」の 第一印象 に記入あり（GPT-3 以降に触れた身として、振り返っておきたい世代で; ⚠ 「私のコメント」の 良い点 に記入あり（従来主流だったディープラーニング系と別系統から出てきた点がす |
| D-26 | gpt-oss | ready | ⚠ 「非エンジニアのつまずき」に記入あり（- 無料で使えると思いましたが、モデルが大きすぎて動きませんで; ⚠ 「私のコメント」の 第一印象 に記入あり（GPT が oss になって使えることに感動しました） —; ⚠ 「私のコメント」の 良い点 に記入あり（オープンモデルなので自由にいじれます） — 著者の記入なら  |
| D-30 | Grok 系 | ready | ⚠ 「非エンジニアのつまずき」に記入あり（- エコシステムとして X を使っていないとそもそも触れません; ⚠ 「私のコメント」の 第一印象 に記入あり（三大 AI メーカーに割って入った印象です） — 著者の記; ⚠ 「私のコメント」の 良い点 に記入あり（緩くて安くて使いやすいという評判をよく聞きます） — 著者の |
| D-35 | Cursor Composer | ready | ⚠ 「非エンジニアのつまずき」に記入あり（- Cursor を有料課金していないと、そもそも出会いません; ⚠ 「私のコメント」の 第一印象 に記入あり（コーディング系 YouTuber の評判は良いようです） ; ⚠ 「私のコメント」の 良い点 に記入あり（出来は良いらしいです。触っていないので未確認です） — 著者 |
| D-40 | Llama 系 | ready | ⚠ 「非エンジニアのつまずき」に記入あり（- 大きいモデルはデータセンター級 GPU が要り、個人 PC; ⚠ 「私のコメント」の 第一印象 に記入あり（LLM の論文でよく名前を聞く印象です） — 著者の記入な; ⚠ 「私のコメント」の 良い点 に記入あり（オープンソース戦略で比較的自由に使えます） — 著者の記入な |
| D-41 | Mistral 系 | ready | ⚠ 「非エンジニアのつまずき」に記入あり（- 名前自体がそもそもそんなに有名ではありません…） — 著者; ⚠ 「私のコメント」の 第一印象 に記入あり（オープンモデル系で最初に名前が挙がるベンダーです） — 著; ⚠ 「私のコメント」の 良い点 に記入あり（オープンでフロンティアに次ぐ性能がある点です） — 著者の記 |
| D-42 | Gemma 系 | ready | ⚠ 「非エンジニアのつまずき」に記入あり（- どこの会社がやっているのか分かりづらいです…） — 著者の; ⚠ 「私のコメント」の 第一印象 に記入あり（Ollama 経由でダウンロードして使えるのが嬉しいです）; ⚠ 「私のコメント」の 良い点 に記入あり（Google のオープンウェイトでセキュリティ説明がしやすく |
| D-43 | Qwen 系 | ready | ⚠ 「非エンジニアのつまずき」に記入あり（- 中華系のモデルということで警戒感が高いです…） — 著者の; ⚠ 「私のコメント」の 第一印象 に記入あり（arXiv 論文でかなり引用され、性能比較に使われている印; ⚠ 「私のコメント」の 良い点 に記入あり（ローカル運用で 2.5 系は第一候補です） — 著者の記入な |
| D-44 | Kimi | ready | ⚠ 「非エンジニアのつまずき」に記入あり（- 馴染みのないベンダーという印象があります…） — 著者の記; ⚠ 「私のコメント」の 第一印象 に記入あり（Opus 4.5 級と評判が良いオープンモデル） — 著者; ⚠ 「私のコメント」の 良い点 に記入あり（Claude Code でエージェント自作に推奨される印象） |
| D-45 | GLM | ready | ⚠ 「非エンジニアのつまずき」に記入あり（- 一般認知度がかなり低く、知らない人には「何それ？」となりま; ⚠ 「私のコメント」の 第一印象 に記入あり（YouTuber が推していて名前を知った印象です。） —; ⚠ 「私のコメント」の 良い点 に記入あり（以前は API 料金が安くてコスパが良いと評判でした。） — |
| D-46 | DeepSeek V3 | ready | ⚠ 「非エンジニアのつまずき」に記入あり（- ニュースで名前をよく聞きますが、中国系という点で警戒感があ; ⚠ 「私のコメント」の 第一印象 に記入あり（ディープシークショックと言われるほどの強いモデルという印象; ⚠ 「私のコメント」の 良い点 に記入あり（アリーナでも評判が良く、安さもあり広く使われた印象です。）  |
| D-47 | DeepSeek R1 | ready | ⚠ 「非エンジニアのつまずき」に記入あり（- 世間で話題になりましたが、実際に触っていないと何がすごいの; ⚠ 「私のコメント」の 第一印象 に記入あり（ChatGPT 未課金だったので o1 との比較はできず、; ⚠ 「私のコメント」の 良い点 に記入あり（賢いモデルをホスト型サービスで実質無料に使えた点です。） — |
| D-50 | DALL-E | ready | ⚠ 「非エンジニアのつまずき」に記入あり（- 良いものができても、少し修正しようとするとすぐに絵が崩れま; ⚠ 「私のコメント」の 第一印象 に記入あり（自分の絵より上手くて結構感動しました。） — 著者の記入な; ⚠ 「私のコメント」の 良い点 に記入あり（一定品質のものをたくさん作れる点が良いです。） — 著者の記 |
| D-51 | Imagen | ready | ⚠ 「非エンジニアのつまずき」に記入あり（- 画像生成モデルの名前があまり有名ではありません…） — 著; ⚠ 「私のコメント」の 第一印象 に記入あり（Google の画像生成モデルは上手です） — 著者の記入; ⚠ 「私のコメント」の 良い点 に記入あり（Whisk でほぼ使い放題、しかも無料で使えました） — 著 |
| D-52 | Sora | ready | ⚠ 「非エンジニアのつまずき」に記入あり（- ChatGPT 有料プランでないと使えず、もどかしい思いを; ⚠ 「私のコメント」の 第一印象 に記入あり（これで映画が撮れる、映画はいらないと思ったほどの衝撃でした; ⚠ 「私のコメント」の 良い点 に記入あり（動画生成の常識を打ち破った歴史的なモデルです。） — 著者の |
| D-53 | Veo | ready | ⚠ 「非エンジニアのつまずき」に記入あり（- Whisk から動画を生成できましたが、思ったようなシーン; ⚠ 「私のコメント」の 第一印象 に記入あり（ベンチマークでほぼ 1 位だったので、すごいと思いました）; ⚠ 「私のコメント」の 良い点 に記入あり（Google のサブスク範囲内で無料で使えたところです） — |
| D-54 | Stable Diffusion | ready | ⚠ 「非エンジニアのつまずき」に記入あり（- 自宅 PC で試せる配布元や、調整済み LoRA を探して; ⚠ 「私のコメント」の 第一印象 に記入あり（綺麗な画像が作れて、初めて触ったときはとても感動しました。; ⚠ 「私のコメント」の 良い点 に記入あり（深層学習から ChatGPT までの AI ブームを支えたモ |
| D-55 | Nano Banana | ready | ⚠ 「非エンジニアのつまずき」に記入あり（- 正式名「Gemini 2.5 Flash Image」が長; ⚠ 「私のコメント」の 第一印象 に記入あり（既存モデルの蓄積進化なのに過大評価されている印象でした） ; ⚠ 「私のコメント」の 良い点 に記入あり（0 からキャラクターを作る用途には十分な性能がありました）  |
| D-56 | Seedance | ready | ⚠ 「非エンジニアのつまずき」に記入あり（- 中国国内でしか使えないというアナウンスがあり、ニュースベー; ⚠ 「私のコメント」の 第一印象 に記入あり（Sora 2 との優劣は不明ですが、良い動画が作れる印象で; ⚠ 「私のコメント」の 良い点 に記入あり（ベンチマークが高いですね） — 著者の記入なら OK |
| D-57 | Flow | ready | ⚠ 「非エンジニアのつまずき」に記入あり（- 回数上限があり気軽には使いづらいです…） — 著者の記入な; ⚠ 「私のコメント」の 第一印象 に記入あり（Google プロプランで Gemini と一緒に使える点; ⚠ 「私のコメント」の 良い点 に記入あり（Google のエコシステムの 1 つとして組み込まれている |
| D-58 | Whisk | ready | ⚠ 「非エンジニアのつまずき」に記入あり（- Gemini や NotebookLM に比べて知名度が低; ⚠ 「私のコメント」の 第一印象 に記入あり（無料で使えて嬉しいです。プロプラン前提ですが） — 著者の; ⚠ 「私のコメント」の 良い点 に記入あり（画像が 2 枚同時に出てきて選びやすいです） — 著者の記入 |
| D-60 | AlphaGo | ready | ⚠ 「非エンジニアのつまずき」に記入あり（- 名前は知っていても、どんな仕組みで動いているのかは難しいで; ⚠ 「私のコメント」の 第一印象 に記入あり（AI 史の象徴的な転換点の一つだと思います。） — 著者の; ⚠ 「私のコメント」の 良い点 に記入あり（人類をある側面で超えたことが明確に語りやすいです。） — 著 |
| D-71 | Whisper | ready | ⚠ 「非エンジニアのつまずき」に記入あり（- OpenAI が ChatGPT 以外もやっているのに、あ; ⚠ 「私のコメント」の 第一印象 に記入あり（OSS で使えるという点に好感があります。） — 著者の記; ⚠ 「私のコメント」の 良い点 に記入あり（組み込みシステムとして成立させられます。） — 著者の記入な |
| E-1 | SWE-Bench | needs_review | ⚠ 「非エンジニアのつまずき」に記入あり（- 各社「XX 点」と数字を見せがちで、評価条件（Verifi |
| E-2 | SWE-Bench Verified | ready | ⚠ 「非エンジニアのつまずき」に記入あり（- SWE-bench がよく分からない状態で「Verifie; ⚠ 「私のコメント」の 第一印象 に記入あり（SWE-bench の精度向上版という印象です。） — 著; ⚠ 「私のコメント」の 良い点 に記入あり（人手検証で信頼性を高めている点が良いと思います。） — 著者 |
| E-20 | MMLU | ready | ⚠ 「非エンジニアのつまずき」に記入あり（- 文字列はたまに見るのですが、何を測っているのか全然知りませ; ⚠ 「私のコメント」の 第一印象 に記入あり（何か書いてある、数字というイメージです） — 著者の記入な; ⚠ 「私のコメント」の 良い点 に記入あり（人の能力に近い水準で測れる点が良さそうです） — 著者の記入 |
| E-21 | MMLU-Pro | ready | ⚠ 「非エンジニアのつまずき」に記入あり（- そもそも MMLU が分からない状態で「Pro」と言われて; ⚠ 「私のコメント」の 第一印象 に記入あり（今回初めてちゃんと認識しました。） — 著者の記入なら O; ⚠ 「私のコメント」の 良い点 に記入あり（ベンチマーク側を強化して差別化を図っている点が良いと思います |
| E-22 | GPQA | ready | ⚠ 「非エンジニアのつまずき」に記入あり（- かなり馴染みの薄いものだと思います…） — 著者の記入なら; ⚠ 「私のコメント」の 第一印象 に記入あり（今回初めて見ました） — 著者の記入なら OK; ⚠ 「私のコメント」の 良い点 に記入あり（人間の凄い人を基準にし、事前学習できない設計が面白いです）  |
| E-23 | GSM8K | ready | ⚠ 「非エンジニアのつまずき」に記入あり（- 今回調べていて初めて聞きました。…） — 著者の記入なら ; ⚠ 「私のコメント」の 第一印象 に記入あり（今回初めて知りました。） — 著者の記入なら OK; ⚠ 「私のコメント」の 良い点 に記入あり（定型的な性能を測るのによさそうです。） — 著者の記入なら  |
| E-24 | MATH | ready | ⚠ 「非エンジニアのつまずき」に記入あり（- レベル差があるとされても、Level 5 が他のベンチマー; ⚠ 「私のコメント」の 第一印象 に記入あり（今回初めて知りました） — 著者の記入なら OK; ⚠ 「私のコメント」の 良い点 に記入あり（段階別なので 1 つで能力を幅広く測れるのが良いです） —  |
| E-3 | Terminal-Bench | ready | ⚠ 「非エンジニアのつまずき」に記入あり（- ターミナル自体がとっつきにくいです。…） — 著者の記入な; ⚠ 「私のコメント」の 第一印象 に記入あり（エージェントユースに適したベンチマークの一つという印象です; ⚠ 「私のコメント」の 良い点 に記入あり（エージェントのターミナル操作能力を測れる点が良いです。） — |
| E-4 | HumanEval | ready | ⚠ 「非エンジニアのつまずき」に記入あり（- Python 評価なのに名前に Python が入らず分か; ⚠ 「私のコメント」の 第一印象 に記入あり（今回調べていて初めて見ました） — 著者の記入なら OK; ⚠ 「私のコメント」の 良い点 に記入あり（Python コードを点数で評価できる点が良いです） — 著 |
| F-50 | git | needs_review | ⚠ 「非エンジニアのつまずき」に記入あり（- 読み方が「ギット」か「ジット」か分からず、口に出すときに迷 |
| G-1 | Context | needs_review | ⚠ 「非エンジニアのつまずき」に記入あり（- 「コンテキスト」と言われても日常語の感覚と距離があり、普通 |
| H-53 | ChatGPT 登場 | needs_review | ⚠ 「非エンジニアのつまずき」に記入あり（- 公開当初に触っていなかった人は後追いで知ることになり、20 |
| I-1 | MCP | ready | ⚠ 「非エンジニアのつまずき」に記入あり（- 何の略で、結局何の役に立つのかがピンと来ず、「AI の U; ⚠ 「私のコメント」の 第一印象 に記入あり（名前のキャッチーさが先行している印象です。） — 著者の記; ⚠ 「私のコメント」の 良い点 に記入あり（LLM からのソフトウェア操作が容易になります。） — 著者 |
| I-10 | Filesystem MCP | ready | ⚠ 「非エンジニアのつまずき」に記入あり（- 普段目にも耳にもしません…） — 著者の記入なら OK; ⚠ 「私のコメント」の 第一印象 に記入あり（今回はじめて試してみました） — 著者の記入なら OK; ⚠ 「私のコメント」の 良い点 に記入あり（Claude Code に任せれば意識せず色々できます） — |
| I-11 | GitHub MCP | ready | ⚠ 「非エンジニアのつまずき」に記入あり（- アクセストークン取得の手順でつまずきやすく、意味も分かりに; ⚠ 「私のコメント」の 第一印象 に記入あり（Claude Code から GitHub 操作を自動でや; ⚠ 「私のコメント」の 良い点 に記入あり（GitHub へのデータ転送を Claude Code から |
| I-12 | Git MCP | ready | ⚠ 「非エンジニアのつまずき」に記入あり（- 全権委任して致命的な破壊行為をされました（Sonnet 4; ⚠ 「私のコメント」の 第一印象 に記入あり（ローカル承認の回数が減って楽になりそうです） — 著者の記; ⚠ 「私のコメント」の 良い点 に記入あり（エージェントのトークン数が下がりそうです） — 著者の記入な |
| I-13 | Slack MCP | ready | ⚠ 「非エンジニアのつまずき」に記入あり（- Teams をメインに使っているので、Slack は触った; ⚠ 「私のコメント」の 第一印象 に記入あり（Slack の方が便利そうですが、Teams 標準で評価は; ⚠ 「私のコメント」の 良い点 に記入あり（Slack の全域を横断検索できそうです（要確認）。） —  |
| I-2 | MCP Server | ready | ⚠ 「非エンジニアのつまずき」に記入あり（- 具体例がどちらか分かりにくいです。ユーザー側ではなくサービ; ⚠ 「私のコメント」の 第一印象 に記入あり（キャッチーな感じです。） — 著者の記入なら OK; ⚠ 「私のコメント」の 良い点 に記入あり（LLM のエージェントユースが捗り、精度が上がります。） — |
| I-20 | Playwright MCP | ready | ⚠ 「非エンジニアのつまずき」に記入あり（- 普通に仕事をしていたら名前を聞かないです…） — 著者の記; ⚠ 「私のコメント」の 第一印象 に記入あり（確認が非常に楽になって最高です） — 著者の記入なら OK; ⚠ 「私のコメント」の 良い点 に記入あり（実際の操作を代行してくれて使い方が現代的です） — 著者の記 |
| I-21 | Puppeteer MCP | ready | ⚠ 「非エンジニアのつまずき」に記入あり（- PDF を作りたいだけなのに、できることが多すぎて何を任せ; ⚠ 「私のコメント」の 第一印象 に記入あり（何でもできすぎて、PDF 周りでもよく分かりません） — ; ⚠ 「私のコメント」の 良い点 に記入あり（PDF 生成もできるので、出版関係では使わない手はないです） |
| I-22 | Chrome DevTools MCP | ready | ⚠ 「非エンジニアのつまずき」に記入あり（- Playwright との差分が分かりづらいです。どちらを; ⚠ 「私のコメント」の 第一印象 に記入あり（Playwright と並ぶブラウザ操作役で便利そうです）; ⚠ 「私のコメント」の 良い点 に記入あり（Chrome のパフォーマンス計測も任せられるようです） — |
| I-23 | Serena MCP | ready | ⚠ 「非エンジニアのつまずき」に記入あり（- 「すごくいい、トークン効率が上がる」と言われますが、原理が; ⚠ 「私のコメント」の 第一印象 に記入あり（バイブコーダーの人がかなりおすすめしたいやつなのでしょう）; ⚠ 「私のコメント」の 良い点 に記入あり（確かにトークンの使用効率は下がった気がします） — 著者の記 |
| I-24 | Context7 MCP | ready | ⚠ 「非エンジニアのつまずき」に記入あり（- 公式情報を取ってくれる価値は感じますが、足す利点が掴めませ; ⚠ 「私のコメント」の 第一印象 に記入あり（名前をよく聞く MCP のひとつです） — 著者の記入なら; ⚠ 「私のコメント」の 良い点 に記入あり（依存関係で困ったとき公式の情報を取ってくれるそうです） —  |
| I-3 | MCP Client | ready | ⚠ 「非エンジニアのつまずき」に記入あり（- クライアントとサーバーの方向が混乱します…） — 著者の記; ⚠ 「私のコメント」の 第一印象 に記入あり（MCP の概念を AI ニュースで聞きました） — 著者の; ⚠ 「私のコメント」の 良い点 に記入あり（正確に表していて、わかっています） — 著者の記入なら OK |
| I-30 | Notion MCP | ready | ⚠ 「非エンジニアのつまずき」に記入あり（- ネイティブな Notion ユーザーではないので、正直なと; ⚠ 「私のコメント」の 第一印象 に記入あり（Notion に MCP があるのは便利そうです） — 著; ⚠ 「私のコメント」の 良い点 に記入あり（MCP 経由なので効率が高いのではないでしょうか） — 著者 |
| I-4 | MCP Transport | ready | ⚠ 「非エンジニアのつまずき」に記入あり（- エージェントがやってくれると特に意識することはありません…; ⚠ 「私のコメント」の 第一印象 に記入あり（今回初めてです） — 著者の記入なら OK; ⚠ 「私のコメント」の 良い点 に記入あり（MCP の解像度が上がります） — 著者の記入なら OK |
| I-41 | SQLite MCP | ready | ⚠ 「非エンジニアのつまずき」に記入あり（- SQL と SQLite（SQL ライト）の関係が分かりづ; ⚠ 「私のコメント」の 第一印象 に記入あり（SQL を操作できる MCP なのかな） — 著者の記入な; ⚠ 「私のコメント」の 良い点 に記入あり（ローカル完結で DB を叩いてくれて便利そうです） — 著者 |
| I-5 | MCP SDK | ready | ⚠ 「非エンジニアのつまずき」に記入あり（- SDK というものに馴染みがありません…） — 著者の記入; ⚠ 「私のコメント」の 第一印象 に記入あり（社内システムに応答させるのに使えそうです） — 著者の記入; ⚠ 「私のコメント」の 良い点 に記入あり（自作のロジックを公開できます） — 著者の記入なら OK |
| I-50 | AWS MCP | ready | ⚠ 「非エンジニアのつまずき」に記入あり（- AWS 自体の初期設定で、MCP に到達する前につまずきそ; ⚠ 「私のコメント」の 第一印象 に記入あり（AI エージェントと対話で要件を詰めれば使えそうです） —; ⚠ 「私のコメント」の 良い点 に記入あり（画面のポチポチ操作をせずに済みそうです） — 著者の記入なら |
| J-14 | LLM | needs_review | ⚠ 「非エンジニアのつまずき」に記入あり（- 「生成 AI」ではなく「LLM」と言うと、ちょっと気取って |

## ✍️ 書きかけ（drafting・全パス済み・自動昇格漏れ）（0 件）

_なし（drafting で全パスしたものは自動で needs_review に上がります）_

## 📝 著者レビュー待ち（needs_review・全パス）（244 件）

| ID | title | status | 概要 |
| :-- | :-- | :-- | :-- |
| B-10 | Devin | needs_review | — |
| B-11 | Bolt.new | needs_review | — |
| B-12 | Perplexity | needs_review | — |
| B-14 | Genspark | needs_review | — |
| B-15 | Microsoft Copilot | needs_review | — |
| B-16 | Microsoft 365 Copilot | needs_review | — |
| B-18 | Aqua Voice | needs_review | — |
| B-19 | Claude Cowork | needs_review | — |
| B-21 | Netlify | needs_review | — |
| B-22 | Cloudflare | needs_review | — |
| B-24 | Google Cloud | needs_review | — |
| B-25 | Azure | needs_review | — |
| B-26 | Azure OpenAI | needs_review | — |
| B-27 | Vertex AI | needs_review | — |
| B-29 | Supabase | needs_review | — |
| B-32 | Figma | needs_review | — |
| B-33 | Canva | needs_review | — |
| B-40 | Reddit | needs_review | — |
| B-41 | arXiv | needs_review | — |
| B-52 | Gemini の料金プラン | needs_review | — |
| B-6 | Windsurf | needs_review | — |
| B-60 | Suno | needs_review | — |
| B-61 | ACE-Step 1.5 | needs_review | — |
| B-7 | Claude Code | needs_review | — |
| B-8 | Codex | needs_review | — |
| B-9 | v0 | needs_review | — |
| C-50 | Sam Altman | needs_review | — |
| C-83 | AI の羅針盤 | needs_review | — |
| D-1 | Gemini 2 系 | needs_review | — |
| D-10 | Claude 3 系 | needs_review | — |
| D-13 | Claude 4.5 系 | needs_review | — |
| D-14 | Claude Mythos Preview | needs_review | — |
| D-2 | Gemini 2.5 系 | needs_review | — |
| D-20 | GPT-5 系 | needs_review | — |
| D-21 | GPT-4 系 | needs_review | — |
| D-22 | o1 系 | needs_review | — |
| D-23 | o3 系 | needs_review | — |
| D-24 | GPT-3 系 | needs_review | — |
| D-3 | Gemini 3 系 | needs_review | — |
| D-4 | Gemini 3.1 系 | needs_review | — |
| D-70 | Amical | needs_review | — |
| E-25 | AIME | needs_review | — |
| E-26 | Humanity's Last Exam | needs_review | — |
| E-27 | IQ Bench | needs_review | — |
| E-30 | TAU-Bench | needs_review | — |
| E-31 | WebArena | needs_review | — |
| E-32 | GAIA | needs_review | — |
| E-33 | AgentBench | needs_review | — |
| E-34 | OSWorld | needs_review | — |
| E-50 | Chatbot Arena | needs_review | — |
| E-51 | LMSYS Arena | needs_review | — |
| F-1 | JavaScript | needs_review | — |
| F-10 | React | needs_review | — |
| F-100 | 拡張子早見表 | needs_review | — |
| F-101 | .ico | needs_review | — |
| F-102 | .mp4 | needs_review | — |
| F-103 | .mp3 | needs_review | — |
| F-104 | .webp | needs_review | — |
| F-11 | Next.js | needs_review | — |
| F-110 | Lighthouse | needs_review | — |
| F-111 | a11y | needs_review | — |
| F-12 | Electron | needs_review | — |
| F-120 | PostgreSQL | needs_review | — |
| F-121 | SQLite | needs_review | — |
| F-122 | Prisma | needs_review | — |
| F-123 | ORM | needs_review | — |
| F-13 | Tauri | needs_review | — |
| F-130 | OAuth | needs_review | — |
| F-14 | three.js | needs_review | — |
| F-140 | Mermaid | needs_review | — |
| F-141 | PlantUML | needs_review | — |
| F-15 | shadcn/ui | needs_review | — |
| F-150 | MIT ライセンス | needs_review | — |
| F-151 | Apache 2.0 | needs_review | — |
| F-152 | GPL | needs_review | — |
| F-153 | Creative Commons | needs_review | — |
| F-154 | OSS | needs_review | — |
| F-16 | Tailwind CSS | needs_review | — |
| F-160 | DOM | needs_review | — |
| F-161 | SSR | needs_review | — |
| F-162 | SSG | needs_review | — |
| F-17 | Astro | needs_review | — |
| F-170 | EC2 | needs_review | — |
| F-171 | S3 | needs_review | — |
| F-172 | IAM | needs_review | — |
| F-180 | OpenGL | needs_review | — |
| F-181 | WebGL | needs_review | — |
| F-190 | サブルーチン | needs_review | — |
| F-2 | TypeScript | needs_review | — |
| F-20 | ESLint | needs_review | — |
| F-200 | Rust | needs_review | — |
| F-21 | Prettier | needs_review | — |
| F-3 | Python | needs_review | — |
| F-30 | VS Code | needs_review | — |
| F-34 | VS Code 拡張機能 | needs_review | — |
| F-35 | Markdown Preview Enhanced | needs_review | — |
| F-36 | Git Graph | needs_review | — |
| F-37 | Japanese Language Pack for VS Code | needs_review | — |
| F-38 | Markdown All in One | needs_review | — |
| F-4 | HTML | needs_review | — |
| F-40 | npm | needs_review | — |
| F-41 | Vite | needs_review | — |
| F-42 | ビルド | needs_review | — |
| F-43 | テスト | needs_review | — |
| F-44 | pnpm | needs_review | — |
| F-5 | CSS | needs_review | — |
| F-51 | git push | needs_review | — |
| F-52 | git pull | needs_review | — |
| F-53 | branch | needs_review | — |
| F-54 | commit | needs_review | — |
| F-55 | merge | needs_review | — |
| F-56 | .gitignore | needs_review | — |
| F-57 | リポジトリ | needs_review | — |
| F-58 | git stash | needs_review | — |
| F-59 | README.md | needs_review | — |
| F-6 | Markdown | needs_review | — |
| F-60 | GitHub | needs_review | — |
| F-61 | Pull Request | needs_review | — |
| F-62 | GitHub Actions | needs_review | — |
| F-7 | YAML | needs_review | — |
| F-71 | ripgrep | needs_review | — |
| F-8 | JSON | needs_review | — |
| F-80 | Node.js | needs_review | — |
| F-81 | bash | needs_review | — |
| F-82 | WSL | needs_review | — |
| F-83 | PowerShell | needs_review | — |
| F-84 | Ghostty | needs_review | — |
| F-85 | SuperClaude Framework | needs_review | — |
| F-86 | ollama | needs_review | — |
| F-87 | sudo | needs_review | — |
| F-9 | SVG | needs_review | — |
| F-90 | Docker | needs_review | — |
| F-91 | .env | needs_review | — |
| G-10 | Prompt Engineering | needs_review | — |
| G-11 | Context Engineering | needs_review | — |
| G-12 | Agent Design | needs_review | — |
| G-13 | Few-shot Learning | needs_review | — |
| G-14 | Thinking モデル | needs_review | — |
| G-15 | RAG | needs_review | — |
| G-16 | Embedding | needs_review | — |
| G-17 | ベクトル DB | needs_review | — |
| G-18 | Chain of Thought | needs_review | — |
| G-19 | Prompt Caching | needs_review | — |
| G-2 | Token | needs_review | — |
| G-20 | CLAUDE.md | needs_review | — |
| G-21 | AGENTS.md | needs_review | — |
| G-22 | SKILL.md | needs_review | — |
| G-23 | .claude/settings.json | needs_review | — |
| G-3 | Dictation | needs_review | — |
| G-30 | Tool Use | needs_review | — |
| G-31 | Hook | needs_review | — |
| G-32 | Slash Command | needs_review | — |
| G-33 | Function Calling | needs_review | — |
| G-34 | Code Interpreter | needs_review | — |
| G-35 | Deep Research | needs_review | — |
| G-36 | Artifact | needs_review | — |
| G-38 | Plan Mode | needs_review | — |
| G-39 | Permission | needs_review | — |
| G-4 | System Prompt | needs_review | — |
| G-40 | バイブコーディング | needs_review | — |
| G-41 | Subagent | needs_review | — |
| G-42 | Worktree | needs_review | — |
| G-43 | オーケストレーション | needs_review | — |
| G-44 | マルチエージェント協調 | needs_review | — |
| G-45 | 段階的開示 | needs_review | — |
| G-46 | ナーフ | needs_review | — |
| G-47 | Auto-compact | needs_review | — |
| G-5 | Context Window | needs_review | — |
| G-6 | One-shot | needs_review | — |
| G-7 | 指示追従性 | needs_review | — |
| G-8 | 決定論的／非決定論的 | needs_review | — |
| G-9 | effort レベル | needs_review | — |
| H-1 | TDD | needs_review | — |
| H-2 | ペアプログラミング | needs_review | — |
| H-3 | バイブコーディングの流儀 | needs_review | — |
| H-4 | コードレビュー | needs_review | — |
| H-5 | Scrum / Agile | needs_review | — |
| H-50 | Bard → Gemini | needs_review | — |
| H-51 | Preview から正式版への流れ | needs_review | — |
| H-52 | Copilot から Claude Code までの流れ | needs_review | — |
| H-54 | GPT-4 リリース | needs_review | — |
| H-55 | LLaMA のオープン化 | needs_review | — |
| H-56 | Claude のバージョン史 | needs_review | — |
| H-57 | Gemini の命名史 | needs_review | — |
| H-58 | Transformer 論文 | needs_review | — |
| H-59 | AI エージェント元年 | needs_review | — |
| H-6 | Git Flow | needs_review | — |
| H-60 | Codex → GitHub Copilot の系譜 | needs_review | — |
| H-61 | Preview 版という文化 | needs_review | — |
| H-62 | Anthropic 創業の流れ | needs_review | — |
| H-63 | Vibe Coding 命名 | needs_review | — |
| H-7 | CI/CD | needs_review | — |
| H-8 | DevOps | needs_review | — |
| I-80 | 自作 MCP のテンプレ | needs_review | — |
| I-81 | MCP の登録・設定 | needs_review | — |
| J-1 | AGI | needs_review | — |
| J-10 | Machine Learning | needs_review | — |
| J-100 | 識字 | needs_review | — |
| J-11 | Deep Learning | needs_review | — |
| J-12 | Neural Network | needs_review | — |
| J-13 | Transformer | needs_review | — |
| J-15 | VLM | needs_review | — |
| J-16 | Fine-tuning | needs_review | — |
| J-17 | Attention | needs_review | — |
| J-18 | MoE | needs_review | — |
| J-19 | 量子化 | needs_review | — |
| J-2 | 強い AI／弱い AI | needs_review | — |
| J-20 | Big Data | needs_review | — |
| J-21 | LoRA | needs_review | — |
| J-22 | パラメータ数の単位 | needs_review | — |
| J-23 | 拡散モデル | needs_review | — |
| J-3 | Singularity | needs_review | — |
| J-31 | 第 5 世代コンピュータ | needs_review | — |
| J-32 | ノイマン型 | needs_review | — |
| J-33 | 量子コンピュータ | needs_review | — |
| J-4 | ASI | needs_review | — |
| J-40 | IoT | needs_review | — |
| J-41 | DX | needs_review | — |
| J-42 | Web3 | needs_review | — |
| J-43 | SaaS | needs_review | — |
| J-50 | AI 倫理 | needs_review | — |
| J-51 | Hallucination | needs_review | — |
| J-52 | Sycophancy | needs_review | — |
| J-53 | 著作権法 30 条の 4 | needs_review | — |
| J-54 | ISO/IEC 42001 | needs_review | — |
| J-55 | 個人情報保護法 | needs_review | — |
| J-56 | GDPR | needs_review | — |
| J-62 | チューリングテスト | needs_review | — |
| J-70 | VRAM | needs_review | — |
| J-71 | RAM | needs_review | — |
| J-72 | H100 | needs_review | — |
| J-73 | Blackwell | needs_review | — |
| J-74 | RTX シリーズ | needs_review | — |
| J-75 | Tensor コア | needs_review | — |
| J-76 | CPU | needs_review | — |
| J-77 | GPU | needs_review | — |
| J-78 | HDD | needs_review | — |
| J-79 | SSD | needs_review | — |
| J-80 | SATA | needs_review | — |
| J-81 | M.2 | needs_review | — |
| J-90 | GUI | needs_review | — |
| J-91 | CLI | needs_review | — |
| J-92 | Linux | needs_review | — |
| J-93 | Ubuntu | needs_review | — |

## ✅ 完成（ready・全パス）（0 件）

_なし_

## 動線

- **☆ 違反**（タグ `[AI直]`）: その場で entry-writer を呼んで直す（status は drafting のまま）
- **⚠️ 警告**（タグ `[AI整]`）: 軽微なら手で削る／溜まったらまとめて対応
- **needs_review**（タグ `[人書]`）: 著者本人が「非エンジニアのつまずき」「私のコメント」4 項目を埋める。全項目埋まると保存時に `ready`（`[済]`）へ自動昇格
- このキューは `Edit/Write` のたびに自動更新されます。手動更新は `python3 scripts/update_review_queue.py`
- ファイル名のタグを更新するには `python3 scripts/apply_status_markers.py`
