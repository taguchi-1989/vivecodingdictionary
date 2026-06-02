# Ponchi Logo Requirement Matrix 2026-06-01

## 目的

ポンチ絵再生成で、ロゴを入れるべき項目と入れない項目を先に分ける。ロゴが必要でも、公式素材と利用条件が確認できていないものは後合成しない。AI 生成でロゴ風の図形やブランドカラーを作らせることも禁止する。

対象は、現在 `assets/ponchi/prompts/` にある再生成プロンプト 12 件。

## ステータス定義

| status | 意味 |
| :-- | :-- |
| `logo_avoid` | ロゴ不要。汎用アイコンだけで説明する |
| `base_2to1_ready_logo_blocked` | 元絵の 2:1 ベースは再生成済み。ロゴは公式素材・利用条件・ローカルパスが未確定のため未反映 |
| `official_logo_source_available_needs_import` | 公式ソースは確認済み。まだローカル素材化・利用条件記録・合成監査が未完了 |
| `official_logo_source_review_required` | 公式ガイドは確認済みだが、この項目に使うべき具体ロゴ、取得経路、または許諾条件の追加確認が必要 |
| `official_logo_available` | 公式素材がローカルにあり、後合成に進められる |
| `official_logo_applied` | 公式素材を後合成済み。本番画像または確認画像まで作成済み |

## 判定方針

ブランド名・製品名・モデル系列名そのものが見出しになっている項目は、本文だけで足りるとしてロゴを避けない。公式ロゴ、公式 lockup、公式アイコンのソースが確認できる場合は、2:1 ベース再生成後に公式素材を取得し、未改変で後合成する。

ただし、AI 生成でロゴ風の図形を描かせることは引き続き禁止する。公式ソースが未確認、利用条件が不明、または具体的なロゴ選定が未確定なら、合成は止めて `official_logo_source_review_required` または `base_2to1_ready_logo_blocked` に置く。

## マーキング

| entry_id | title | logo_need | status | local official asset | action |
| :-- | :-- | :-- | :-- | :-- | :-- |
| `B-1` | Gemini | required | `official_logo_source_review_required` | none | 2:1 ベース生成済み。Google Brand Resource Center の利用条件を前提に、Gemini に使う公式プロダクトアイコン/lockup と許諾要否を確認してから合成 |
| `B-2` | Claude | required | `official_logo_applied` | `assets/logos/anthropic/anthropic-media-resources/Anthropic media resources/Anthropic logos/Claude logos/1 Claude logo/PNG/Claude logo - Slate.png` | B-focus ベースに公式 Claude ロゴを後合成済み。`overlay_candidates_contact_sheet.png` で目視確認 |
| `B-3` | ChatGPT | required | `official_logo_source_review_required` | none | 2:1 ベース生成済み。OpenAI 公式ブランドガイドを前提に、OpenAI wordmark と ChatGPT 固有表現のどちらを使うか決めてから合成 |
| `B-4` | Cursor | required | `official_logo_applied` | `assets/logos/cursor/cursor-brand-assets/General Logos/Lockup Horizontal/PNG/LOCKUP_HORIZONTAL_2D_LIGHT.png` | B-focus ベースに公式 Cursor horizontal lockup を後合成済み。`overlay_candidates_contact_sheet.png` で目視確認 |
| `B-5` | GitHub Copilot | required | `official_logo_applied` | `assets/logos/github/GitHub_Logos/GitHub Logos/PNG/GitHub_Copilot_Lockup_Black_Clearspace.png` | 本番 `assets/ponchi/final/B-5.webp` に公式 lockup 合成済み |
| `B-7` | Claude Code | required | `official_logo_applied` | `assets/logos/anthropic/anthropic-media-resources/Anthropic media resources/Anthropic logos/Claude logos/2 Claude Code logo/PNG/Claude Code logo - Slate.png` | B-focus ベースに公式 Claude Code ロゴを後合成済み。`overlay_candidates_contact_sheet.png` で目視確認 |
| `B-8` | Codex | required | `official_logo_source_review_required` | none | 2:1 ベース生成済み。OpenAI 公式ブランドガイドを前提に、Codex 固有 lockup があるか、OpenAI wordmark で扱うかを確認してから合成 |
| `B-9` | v0 | required | `official_logo_applied` | `assets/logos/vercel/v0-assets/v0/Light/v0-logo-light.png` | B-focus ベースに公式 v0 ロゴを後合成済み。180px配置で final 候補へ昇格 |
| `B-10` | Devin | required | `official_logo_source_review_required` | none | batch-002 対象。公式ロゴ素材・利用条件・ローカルパスを確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `B-11` | Bolt.new | required | `official_logo_applied` | `assets/logos/bolt/bolt-logo-text-official-512.png` | batch-002 ベースに公式 StackBlitz `bolt.new` repo の Bolt wordmark を後合成済み。`.new` suffix は合成・生成しない |
| `B-12` | Perplexity | required | `official_logo_applied` | `assets/logos/perplexity/Perplexity-Primary-Lockup-Offblack.svg` | batch-002 ベースに公式 Perplexity Brand Guidelines の offblack primary lockup を後合成済み |
| `B-13` | ElevenLabs | required | `official_logo_applied` | `assets/logos/elevenlabs/elevenlabs-logo-black.svg` | batch-002 ベースに公式 ElevenLabs black SVG を後合成済み。final 候補で目視確認 |
| `B-14` | Genspark | required | `official_logo_source_available_needs_import` | none | 公式 brand page で logo system と downloads を確認済み。Cloudflare challenge のためローカル取得は未完。AI 生成ロゴは禁止してベースだけ維持 |
| `B-15` | Microsoft Copilot | required | `official_logo_source_review_required` | none | batch-002 対象。Microsoft 公式ブランド/製品素材を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `B-16` | Microsoft 365 Copilot | required | `official_logo_source_review_required` | none | batch-002 対象。Microsoft 365 Copilot の公式素材と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `B-17` | Edge Copilot | required | `official_logo_source_review_required` | none | batch-002 対象。Edge/Copilot のどちらの公式表現にするか決めるまで、AI 生成ロゴは禁止してベースだけ作る |
| `B-18` | Aqua Voice | required | `official_logo_source_review_required` | none | batch-002 対象。公式ロゴ素材・利用条件・ローカルパスを確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `B-19` | Claude Cowork | required | `official_logo_source_review_required` | none | batch-002 対象。正式名称と Claude ロゴ適用可否を Anthropic 公式ソースで確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `B-20` | Vercel | required | `official_logo_applied` | `assets/logos/vercel/vercel-assets/Vercel/logotype/light/vercel-logotype-light.png` | batch-002 ベースに公式 Vercel ロゴを後合成済み。final 候補で目視確認 |
| `B-21` | Netlify | required | `official_logo_applied` | `assets/logos/netlify/netlify-logo-full/netlify-logo-full/large/lightmode/logo-netlify-large-monochrome-lightmode.png` | batch-002 ベースに公式 Netlify ロゴを後合成済み。`ponchi-batch-002-base-contact-sheet.png` と final 候補で目視確認 |
| `B-22` | Cloudflare | required | `official_logo_applied` | `assets/logos/cloudflare/Cloudflare_logo_kit/Cloudflare_logo_kit/Cloudflare_logo_kit/Cloudflare logo/png/CF_logo_horizontal_singlecolor_blk.png` | batch-002 ベースに公式 Cloudflare ロゴを後合成済み。`ponchi-batch-002-base-contact-sheet.png` と final 候補で目視確認 |
| `B-23` | AWS | required | `official_logo_source_review_required` | none | batch-002 対象。ローカルの AWS Architecture Icons はブランド lockup と別扱い。公式ロゴ/利用条件を確認してから合成 |
| `B-24` | Google Cloud | required | `official_logo_source_review_required` | none | batch-002 対象。Google Cloud の公式ロゴ素材・利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `B-25` | Azure | required | `official_logo_source_review_required` | none | batch-002 対象。Microsoft Azure の公式ロゴ素材・利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `B-26` | Azure OpenAI | required | `official_logo_source_review_required` | none | batch-002 対象。Azure と OpenAI のどちらの公式表現にするか決めるまで、AI 生成ロゴは禁止してベースだけ作る |
| `B-27` | Vertex AI | required | `official_logo_source_review_required` | none | batch-002 対象。Google Cloud/Vertex AI の公式素材と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `B-28` | Render | required | `official_logo_applied` | `assets/logos/render/render-wordmark-from-press.png` | batch-002 ベースに公式 Render wordmark を後合成済み。final 候補で目視確認 |
| `B-29` | Supabase | required | `official_logo_applied` | `assets/logos/supabase/brand-assets/supabase-logo-wordmark--light.png` | batch-002 ベースに公式 Supabase ロゴを後合成済み。final 候補で目視確認 |
| `B-30` | Amazon Bedrock | required | `official_logo_source_review_required` | none | batch-003 対象。AWS サービスとして公式サービスアイコン/ブランド lockup のどちらを使うべきか確認してから合成 |
| `B-31` | Excalidraw | required | `official_logo_source_review_required` | none | batch-003 対象。公式ロゴ素材・利用条件・ローカルパスを確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `B-32` | Figma | required | `official_logo_source_review_required` | none | batch-003 対象。公式 brand assets と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `B-33` | Canva | required | `official_logo_source_review_required` | none | batch-003 対象。公式ロゴ素材・利用条件・ローカルパスを確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `B-40` | Reddit | required | `official_logo_source_review_required` | none | batch-003 対象。公式 brand assets と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `B-41` | arXiv | required | `official_logo_source_review_required` | none | batch-003 対象。公式ロゴ/識別マークの有無と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `B-50` | Claude の料金プラン | required | `official_logo_source_available_needs_import` | `assets/logos/anthropic/anthropic-media-resources/Anthropic media resources/Anthropic logos/Claude logos/1 Claude logo/PNG/Claude logo - Slate.png` | Claude 関連の料金プラン項目。公式 Claude ロゴはローカルにあるが、料金プラン図での使用可否と配置を確認してから合成 |
| `B-51` | ChatGPT の料金プラン | required | `official_logo_source_review_required` | none | OpenAI/ChatGPT 関連の料金プラン項目。OpenAI wordmark か ChatGPT 固有表現かを決めてから合成 |
| `B-52` | Gemini の料金プラン | required | `official_logo_source_review_required` | none | Gemini 関連の料金プラン項目。Gemini 公式プロダクトアイコン/lockup と許諾要否を確認してから合成 |
| `B-60` | Suno | required | `official_logo_source_review_required` | none | batch-003 対象。公式ロゴ素材・利用条件・ローカルパスを確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `B-61` | ACE-Step 1.5 | required | `official_logo_source_review_required` | none | batch-003 対象。モデル/プロジェクト公式素材の有無を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `C-1` | OpenAI | required | `official_logo_available` | `assets/logos/openai/openai_wordmark_black_official_template_layer.png` | OpenAI 公式 wordmark はローカルにある。C-1 用ベース生成後に後合成可 |
| `C-2` | Anthropic | required | `official_logo_available` | `assets/logos/anthropic/anthropic-media-resources/Anthropic media resources/Anthropic logos/Anthropic logos/1 Anthropic logo/PNG/Anthropic logo - Slate.png` | Anthropic 公式ロゴはローカルにある。C-2 用ベース生成後に後合成可 |
| `C-3` | Google DeepMind | required | `official_logo_source_review_required` | none | Google DeepMind の公式ロゴ/利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `C-4` | Meta AI | required | `official_logo_source_review_required` | none | Meta AI の公式ロゴ/利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `C-5` | xAI | required | `official_logo_source_review_required` | none | xAI の公式ロゴ/利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `C-6` | Mistral AI | required | `official_logo_source_review_required` | none | Mistral AI の公式ロゴ/利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `C-7` | Hugging Face | required | `official_logo_source_review_required` | none | Hugging Face の公式ロゴ/利用条件と mascot 使用可否を確認するまで、AI 生成ロゴ・mascotは禁止してベースだけ作る |
| `C-8` | Microsoft AI | required | `official_logo_source_review_required` | none | Microsoft AI の公式表現と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `C-9` | NVIDIA | required | `official_logo_source_review_required` | none | NVIDIA の公式ロゴ/利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `C-10` | Moonshot AI | required | `official_logo_source_review_required` | none | Batch004 対象。公式ロゴ/利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `C-11` | Z.ai | required | `official_logo_source_review_required` | none | Batch004 対象。公式ロゴ/利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `C-12` | TSMC | required | `official_logo_source_review_required` | none | Batch004 対象。公式ロゴ/利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `C-13` | Groq | required | `official_logo_source_review_required` | none | Batch004 対象。公式ロゴ/利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `C-14` | AMD | required | `official_logo_source_review_required` | none | Batch004 対象。公式ロゴ/利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `C-50` | Sam Altman | not_needed | `logo_avoid` | none | 人物項目。公式ロゴではなく、実在人物の写実的 likeness も避け、抽象タイムライン/関係図としてベースを作る |
| `C-51` | Dario Amodei | not_needed | `logo_avoid` | none | 人物項目。公式ロゴではなく、実在人物の写実的 likeness も避け、抽象タイムライン/関係図としてベースを作る |
| `C-52` | Demis Hassabis | not_needed | `logo_avoid` | none | 人物項目。公式ロゴではなく、実在人物の写実的 likeness も避け、抽象タイムライン/関係図としてベースを作る |
| `C-53` | Andrej Karpathy | not_needed | `logo_avoid` | none | 人物項目。公式ロゴではなく、実在人物の写実的 likeness も避け、抽象タイムライン/関係図としてベースを作る |
| `C-54` | Ilya Sutskever | not_needed | `logo_avoid` | none | 人物項目。公式ロゴではなく、実在人物の写実的 likeness も避け、抽象タイムライン/関係図としてベースを作る |
| `C-55` | Mira Murati | not_needed | `logo_avoid` | none | 人物項目。公式ロゴではなく、実在人物の写実的 likeness も避け、抽象タイムライン/関係図としてベースを作る |
| `C-56` | Yann LeCun | not_needed | `logo_avoid` | none | 人物項目。公式ロゴではなく、実在人物の写実的 likeness も避け、抽象タイムライン/関係図としてベースを作る |
| `C-57` | Geoffrey Hinton | not_needed | `logo_avoid` | none | 人物項目。公式ロゴではなく、実在人物の写実的 likeness も避け、抽象タイムライン/関係図としてベースを作る |
| `C-58` | Elon Musk | not_needed | `logo_avoid` | none | 人物項目。公式ロゴではなく、実在人物の写実的 likeness も避け、抽象タイムライン/関係図としてベースを作る |
| `C-59` | Jensen Huang | not_needed | `logo_avoid` | none | 人物項目。公式ロゴではなく、実在人物の写実的 likeness も避け、抽象タイムライン/関係図としてベースを作る |
| `C-60` | Ray Kurzweil | not_needed | `logo_avoid` | none | 人物項目。公式ロゴではなく、実在人物の写実的 likeness も避け、抽象タイムライン/関係図としてベースを作る |
| `C-80` | AI大学 | required | `official_logo_source_review_required` | none | YouTube チャンネル/媒体項目。公式チャンネルアイコン等の扱いを確認するまで、AI 生成ロゴ・チャンネルアイコンは禁止してベースだけ作る |
| `C-81` | にゃんた | required | `official_logo_source_review_required` | none | YouTube チャンネル/媒体項目。公式チャンネルアイコン等の扱いを確認するまで、AI 生成ロゴ・チャンネルアイコンは禁止してベースだけ作る |
| `C-82` | まさお | required | `official_logo_source_review_required` | none | YouTube チャンネル/媒体項目。公式チャンネルアイコン等の扱いを確認するまで、AI 生成ロゴ・チャンネルアイコンは禁止してベースだけ作る |
| `C-83` | AI の羅針盤 | required | `official_logo_source_review_required` | none | YouTube チャンネル/媒体項目。公式チャンネルアイコン等の扱いを確認するまで、AI 生成ロゴ・チャンネルアイコンは禁止してベースだけ作る |
| `D-1` | Gemini 2 系 | required | `official_logo_source_review_required` | none | Batch005 対象。Gemini/Google の公式プロダクト表現と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `D-2` | Gemini 2.5 系 | required | `official_logo_source_review_required` | none | Batch005 対象。Gemini/Google の公式プロダクト表現と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `D-3` | Gemini 3 系 | required | `official_logo_source_review_required` | none | Batch005 対象。Gemini/Google の公式プロダクト表現と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `D-4` | Gemini 3.1 系 | required | `official_logo_source_review_required` | none | Batch005 対象。Gemini/Google の公式プロダクト表現と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `D-10` | Claude 3 系 | required | `official_logo_source_available_needs_import` | `assets/logos/anthropic/anthropic-media-resources/Anthropic media resources/Anthropic logos/Claude logos/1 Claude logo/PNG/Claude logo - Slate.png` | Batch005 対象。Claude 公式ロゴはローカルにあるが、モデル系列図での使用可否と配置を確認してから合成 |
| `D-11` | Claude 3.5 系 | required | `official_logo_source_available_needs_import` | `assets/logos/anthropic/anthropic-media-resources/Anthropic media resources/Anthropic logos/Claude logos/1 Claude logo/PNG/Claude logo - Slate.png` | Batch005 対象。Claude 公式ロゴはローカルにあるが、モデル系列図での使用可否と配置を確認してから合成 |
| `D-12` | Claude 4 系 | required | `official_logo_source_available_needs_import` | `assets/logos/anthropic/anthropic-media-resources/Anthropic media resources/Anthropic logos/Claude logos/1 Claude logo/PNG/Claude logo - Slate.png` | モデル系列名に Claude が入るためロゴ対象。公式素材はローカルにあるが、モデル系列図での使用可否と配置を確認してから合成 |
| `D-13` | Claude 4.5 系 | required | `official_logo_source_available_needs_import` | `assets/logos/anthropic/anthropic-media-resources/Anthropic media resources/Anthropic logos/Claude logos/1 Claude logo/PNG/Claude logo - Slate.png` | Batch005 対象。Claude 公式ロゴはローカルにあるが、モデル系列図での使用可否と配置を確認してから合成 |
| `D-14` | Claude Mythos Preview | required | `official_logo_source_available_needs_import` | `assets/logos/anthropic/anthropic-media-resources/Anthropic media resources/Anthropic logos/Claude logos/1 Claude logo/PNG/Claude logo - Slate.png` | Batch005 対象。Claude 関連モデル名として扱い、公式素材の使用可否と配置を確認してから合成 |
| `D-20` | GPT-5 系 | required | `official_logo_available` | `assets/logos/openai/openai_wordmark_black_official_template_layer.png` | Batch005 対象。OpenAI 公式 wordmark はローカルにある。モデル系列図での使用可否と配置を確認してから合成 |
| `D-21` | GPT-4 系 | required | `official_logo_available` | `assets/logos/openai/openai_wordmark_black_official_template_layer.png` | Batch005 対象。OpenAI 公式 wordmark はローカルにある。モデル系列図での使用可否と配置を確認してから合成 |
| `D-22` | o1 系 | required | `official_logo_available` | `assets/logos/openai/openai_wordmark_black_official_template_layer.png` | Batch005 対象。OpenAI 公式 wordmark はローカルにある。モデル系列図での使用可否と配置を確認してから合成 |
| `D-23` | o3 系 | required | `official_logo_available` | `assets/logos/openai/openai_wordmark_black_official_template_layer.png` | Batch005 対象。OpenAI 公式 wordmark はローカルにある。モデル系列図での使用可否と配置を確認してから合成 |
| `D-24` | GPT-3 系 | required | `official_logo_available` | `assets/logos/openai/openai_wordmark_black_official_template_layer.png` | Batch005 対象。OpenAI 公式 wordmark はローカルにある。モデル系列図での使用可否と配置を確認してから合成 |
| `D-25` | GPT-1 / GPT-2 系 | required | `official_logo_available` | `assets/logos/openai/openai_wordmark_black_official_template_layer.png` | Batch005 対象。OpenAI 公式 wordmark はローカルにある。モデル系列図での使用可否と配置を確認してから合成 |
| `D-26` | gpt-oss | required | `official_logo_available` | `assets/logos/openai/openai_wordmark_black_official_template_layer.png` | Batch005 対象。OpenAI 関連モデル名として扱い、公式 wordmark の使用可否と配置を確認してから合成 |
| `D-30` | Grok 系 | required | `official_logo_source_review_required` | none | Batch005 対象。xAI/Grok の公式素材と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `D-35` | Cursor Composer | required | `official_logo_source_available_needs_import` | `assets/logos/cursor/cursor-brand-assets/General Logos/Lockup Horizontal/PNG/LOCKUP_HORIZONTAL_2D_LIGHT.png` | Batch005 対象。Cursor 公式 lockup はローカルにあるが、Composer 項目での使用可否と配置を確認してから合成 |
| `D-40` | Llama 系 | required | `official_logo_source_review_required` | none | Batch005 対象。Meta/Llama の公式素材と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `D-41` | Mistral 系 | required | `official_logo_source_review_required` | none | Batch005 対象。Mistral の公式素材と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `D-42` | Gemma 系 | required | `official_logo_source_review_required` | none | Batch006 対象。Google/Gemma の公式素材と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `D-43` | Qwen 系 | required | `official_logo_source_review_required` | none | Batch006 対象。Qwen/Alibaba Cloud の公式素材と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `D-44` | Kimi | required | `official_logo_source_review_required` | none | Batch006 対象。Moonshot/Kimi の公式素材と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `D-45` | GLM | required | `official_logo_source_review_required` | none | Batch006 対象。Zhipu/GLM の公式素材と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `D-46` | DeepSeek V3 | required | `official_logo_source_review_required` | none | Batch006 対象。DeepSeek の公式素材と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `D-47` | DeepSeek R1 | required | `official_logo_source_review_required` | none | Batch006 対象。DeepSeek の公式素材と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `D-50` | DALL-E | required | `official_logo_available` | `assets/logos/openai/openai_wordmark_black_official_template_layer.png` | Batch006 対象。OpenAI 公式 wordmark はローカルにある。画像生成モデル項目での使用可否と配置を確認してから合成 |
| `D-51` | Imagen | required | `official_logo_source_review_required` | none | Batch006 対象。Google/Imagen の公式素材と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `D-52` | Sora | required | `official_logo_available` | `assets/logos/openai/openai_wordmark_black_official_template_layer.png` | Batch006 対象。OpenAI 公式 wordmark はローカルにある。動画生成モデル項目での使用可否と配置を確認してから合成 |
| `D-53` | Veo | required | `official_logo_source_review_required` | none | Batch006 対象。Google/Veo の公式素材と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `D-54` | Stable Diffusion | required | `official_logo_source_review_required` | none | Batch006 対象。Stability AI / Stable Diffusion の公式素材と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `D-55` | Nano Banana | required | `official_logo_source_review_required` | none | Batch006 対象。公式素材と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `D-56` | Seedance | required | `official_logo_source_review_required` | none | Batch006 対象。Seedance/提供元の公式素材と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `D-57` | Flow | required | `official_logo_source_review_required` | none | Batch006 対象。Flow/提供元の公式素材と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `D-58` | Whisk | required | `official_logo_source_review_required` | none | Batch006 対象。Whisk/提供元の公式素材と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `D-60` | AlphaGo | required | `official_logo_source_review_required` | none | Batch006 対象。Google DeepMind/AlphaGo の公式素材と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `D-70` | Amical | required | `official_logo_source_review_required` | none | Batch006 対象。公式素材と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `D-71` | Whisper | required | `official_logo_available` | `assets/logos/openai/openai_wordmark_black_official_template_layer.png` | Batch006 対象。OpenAI 公式 wordmark はローカルにある。音声モデル項目での使用可否と配置を確認してから合成 |
| `E-1` | SWE-Bench | not_needed | `logo_avoid` | none | Batch006 対象。ベンチマーク項目として汎用評価図で説明し、ロゴや公式アイコンは使わない |
| `E-2` | SWE-Bench Verified | not_needed | `logo_avoid` | none | Batch006 対象。ベンチマーク項目として汎用評価図で説明し、ロゴや公式アイコンは使わない |
| `E-3` | Terminal-Bench | not_needed | `logo_avoid` | none | Batch007 対象。ベンチマーク項目として汎用評価図で説明し、ロゴや公式アイコンは使わない |
| `E-4` | HumanEval | not_needed | `logo_avoid` | none | Batch007 対象。ベンチマーク項目として汎用評価図で説明し、ロゴや公式アイコンは使わない |
| `E-20` | MMLU | not_needed | `logo_avoid` | none | Batch007 対象。知識・推論ベンチマークの汎用評価図で説明し、ロゴや公式アイコンは使わない |
| `E-21` | MMLU-Pro | not_needed | `logo_avoid` | none | Batch007 対象。知識・推論ベンチマークの汎用評価図で説明し、ロゴや公式アイコンは使わない |
| `E-22` | GPQA | not_needed | `logo_avoid` | none | Batch007 対象。専門問題ベンチマークの汎用評価図で説明し、ロゴや公式アイコンは使わない |
| `E-23` | GSM8K | not_needed | `logo_avoid` | none | Batch007 対象。算数推論ベンチマークの汎用評価図で説明し、ロゴや公式アイコンは使わない |
| `E-24` | MATH | not_needed | `logo_avoid` | none | Batch007 対象。数学推論ベンチマークの汎用評価図で説明し、ロゴや公式アイコンは使わない |
| `E-25` | AIME | not_needed | `logo_avoid` | none | Batch007 対象。競技数学ベンチマークの汎用評価図で説明し、ロゴや公式アイコンは使わない |
| `E-26` | Humanity's Last Exam | not_needed | `logo_avoid` | none | Batch007 対象。総合難問ベンチマークの汎用評価図で説明し、ロゴや公式アイコンは使わない |
| `E-27` | IQ Bench | not_needed | `logo_avoid` | none | Batch007 対象。知能評価ベンチマークの汎用評価図で説明し、ロゴや公式アイコンは使わない |
| `E-30` | TAU-Bench | not_needed | `logo_avoid` | none | Batch007 対象。エージェント評価の汎用図で説明し、ロゴや公式アイコンは使わない |
| `E-31` | WebArena | not_needed | `logo_avoid` | none | Batch007 対象。Web 操作評価の汎用図で説明し、ロゴや公式アイコンは使わない |
| `E-32` | GAIA | not_needed | `logo_avoid` | none | Batch007 対象。複合タスク評価の汎用図で説明し、ロゴや公式アイコンは使わない |
| `E-33` | AgentBench | not_needed | `logo_avoid` | none | Batch007 対象。エージェント評価の汎用図で説明し、ロゴや公式アイコンは使わない |
| `E-34` | OSWorld | not_needed | `logo_avoid` | none | Batch007 対象。OS 操作評価の汎用図で説明し、ロゴや公式アイコンは使わない |
| `E-50` | Chatbot Arena | not_needed | `logo_avoid` | none | Batch007 対象。モデル比較・投票評価の汎用図で説明し、ロゴや公式アイコンは使わない |
| `E-51` | LMSYS Arena | not_needed | `logo_avoid` | none | Batch007 対象。モデル比較・投票評価の汎用図で説明し、ロゴや公式アイコンは使わない |
| `F-1` | JavaScript | not_needed | `logo_avoid` | none | JS, TypeScript, React, Node.js などのロゴを使わない。汎用ファイル、ブラウザ、サーバ記号だけにする |
| `F-2` | TypeScript | not_needed | `logo_avoid` | none | TypeScript ロゴを使わない。Before/After の汎用型チェック表現で説明する |
| `F-3` | Python | not_needed | `logo_avoid` | none | Batch007 対象。Python ロゴや蛇のマスコット表現を使わず、汎用コード・実行・データ処理の図で説明する |
| `F-4` | HTML | not_needed | `logo_avoid` | none | Batch008 対象。HTML5 ロゴは使わず、文書構造とブラウザ表示の汎用図で説明する |
| `F-5` | CSS | not_needed | `logo_avoid` | none | Batch008 対象。CSS3 ロゴは使わず、スタイル適用の汎用図で説明する |
| `F-6` | Markdown | not_needed | `logo_avoid` | none | Batch008 対象。Markdown ロゴは使わず、原稿からプレビューへの変換図で説明する |
| `F-7` | YAML | not_needed | `logo_avoid` | none | Batch008 対象。ロゴ不要。設定ファイルと構造化データの汎用図で説明する |
| `F-8` | JSON | not_needed | `logo_avoid` | none | Batch008 対象。ロゴ不要。API データと構造化オブジェクトの汎用図で説明する |
| `F-9` | SVG | not_needed | `logo_avoid` | none | Batch008 対象。SVG ロゴは使わず、ベクター図形と拡大縮小の汎用図で説明する |
| `F-10` | React | required | `official_logo_source_review_required` | none | Batch008 対象。公式素材と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `F-11` | Next.js | required | `official_logo_source_review_required` | none | Batch008 対象。公式素材と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `F-12` | Electron | required | `official_logo_source_review_required` | none | Batch008 対象。公式素材と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `F-13` | Tauri | required | `official_logo_source_review_required` | none | Batch008 対象。公式素材と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `F-14` | three.js | required | `official_logo_source_review_required` | none | Batch008 対象。公式素材と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `F-15` | shadcn/ui | required | `official_logo_source_review_required` | none | Batch008 対象。公式素材と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `F-16` | Tailwind CSS | required | `official_logo_source_review_required` | none | Batch008 対象。公式素材と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `F-17` | Astro | required | `official_logo_source_review_required` | none | Batch008 対象。公式素材と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `F-20` | ESLint | required | `official_logo_source_review_required` | none | Batch008 対象。公式素材と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `F-21` | Prettier | required | `official_logo_source_review_required` | none | Batch008 対象。公式素材と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `F-30` | VS Code | required | `official_logo_source_review_required` | none | Batch008 対象。Microsoft / VS Code の公式素材と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `F-34` | VS Code 拡張機能 | required | `official_logo_source_review_required` | none | Batch008 対象。VS Code 関連の公式素材と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `F-35` | Markdown Preview Enhanced | required | `official_logo_source_review_required` | none | Batch008 対象。拡張機能の公式素材と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `F-36` | Git Graph | required | `official_logo_source_review_required` | none | Batch008 対象。拡張機能の公式素材と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `F-37` | Japanese Language Pack for VS Code | required | `official_logo_source_review_required` | none | Batch009 対象。VS Code 拡張機能の公式素材と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `F-38` | Markdown All in One | required | `official_logo_source_review_required` | none | Batch009 対象。拡張機能の公式素材と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `F-40` | npm | required | `official_logo_source_review_required` | none | Batch009 対象。npm 公式素材と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `F-41` | Vite | required | `official_logo_source_review_required` | none | Batch009 対象。Vite 公式素材と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `F-42` | ビルド | not_needed | `logo_avoid` | none | Batch009 対象。概念図。ロゴ不要 |
| `F-44` | pnpm | required | `official_logo_source_review_required` | none | Batch009 対象。pnpm 公式素材と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `F-50` | git | required | `official_logo_source_review_required` | none | Batch009 対象。Git 公式素材と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `F-51` | git push | not_needed | `logo_avoid` | none | Batch009 対象。Git 操作の概念図として扱い、ロゴや公式アイコンは使わない |
| `F-52` | git pull | not_needed | `logo_avoid` | none | Batch009 対象。Git 操作の概念図として扱い、ロゴや公式アイコンは使わない |
| `F-53` | branch | not_needed | `logo_avoid` | none | Batch009 対象。Git 分岐概念図として扱い、ロゴや公式アイコンは使わない |
| `F-54` | commit | not_needed | `logo_avoid` | none | Batch009 対象。Git 履歴概念図として扱い、ロゴや公式アイコンは使わない |
| `F-55` | merge | not_needed | `logo_avoid` | none | Batch009 対象。Git 統合概念図として扱い、ロゴや公式アイコンは使わない |
| `F-56` | .gitignore | not_needed | `logo_avoid` | none | Batch009 対象。ファイル除外概念図として扱い、ロゴや公式アイコンは使わない |
| `F-57` | リポジトリ | not_needed | `logo_avoid` | none | Batch009 対象。リポジトリ概念図として扱い、ロゴや公式アイコンは使わない |
| `F-58` | git stash | not_needed | `logo_avoid` | none | Batch009 対象。一時退避概念図として扱い、ロゴや公式アイコンは使わない |
| `F-59` | README.md | not_needed | `logo_avoid` | none | Batch009 対象。ドキュメント概念図として扱い、ロゴや公式アイコンは使わない |
| `F-60` | GitHub | required | `official_logo_applied` | `assets/logos/github/GitHub_Logos/GitHub Logos/PNG/GitHub_Lockup_Black_Clearspace.png` | 本番 `assets/ponchi/final/F-60.webp` に公式 lockup 合成済み |
| `F-61` | Pull Request | required | `official_logo_source_review_required` | none | Batch009 対象。GitHub 関連項目として公式素材と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `F-62` | GitHub Actions | required | `official_logo_source_review_required` | none | Batch009 対象。GitHub 関連項目として公式素材と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `F-71` | ripgrep (rg) | not_needed | `logo_avoid` | none | Batch009 対象。検索ツール概念図として扱い、ロゴや公式アイコンは使わない |
| `F-80` | Node.js | required | `official_logo_source_review_required` | none | Batch010 対象。Node.js 公式素材と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `F-81` | bash | not_needed | `logo_avoid` | none | Batch010 対象。シェル概念図として扱い、ロゴや公式アイコンは使わない |
| `F-82` | WSL | required | `official_logo_source_review_required` | none | Batch010 対象。Microsoft/WSL 関連素材と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `F-83` | PowerShell | required | `official_logo_source_review_required` | none | Batch010 対象。PowerShell 公式素材と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `F-84` | Ghostty | required | `official_logo_source_review_required` | none | Batch010 対象。公式素材と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `F-85` | SuperClaude Framework | required | `official_logo_source_review_required` | none | Batch010 対象。公式素材や利用条件が不明なため、確認まで AI 生成ロゴは禁止してベースだけ作る |
| `F-86` | ollama | required | `official_logo_source_review_required` | none | Batch010 対象。Ollama 公式素材と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `F-87` | sudo | not_needed | `logo_avoid` | none | Batch010 対象。権限昇格の概念図として扱い、ロゴや公式アイコンは使わない |
| `F-90` | Docker | required | `official_logo_source_review_required` | none | Batch010 対象。Docker 公式素材と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `F-91` | .env | not_needed | `logo_avoid` | none | Batch010 対象。環境変数ファイルの概念図として扱い、ロゴや公式アイコンは使わない |
| `F-100` | 拡張子早見表 | not_needed | `logo_avoid` | none | Batch010 対象。ファイル形式の概念図として扱い、ロゴや公式アイコンは使わない |
| `F-101` | .ico | not_needed | `logo_avoid` | none | Batch010 対象。アイコンファイル形式の概念図として扱い、ロゴや公式アイコンは使わない |
| `F-102` | .mp4 | not_needed | `logo_avoid` | none | Batch010 対象。動画ファイル形式の概念図として扱い、ロゴや公式アイコンは使わない |
| `F-103` | .mp3 | not_needed | `logo_avoid` | none | Batch010 対象。音声ファイル形式の概念図として扱い、ロゴや公式アイコンは使わない |
| `F-104` | .webp | not_needed | `logo_avoid` | none | Batch010 対象。画像ファイル形式の概念図として扱い、ロゴや公式アイコンは使わない |
| `F-110` | Lighthouse | required | `official_logo_source_review_required` | none | Batch010 対象。Google/Chrome Lighthouse の公式素材と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `F-111` | a11y | not_needed | `logo_avoid` | none | Batch010 対象。アクセシビリティ概念図として扱い、ロゴや公式アイコンは使わない |
| `F-120` | PostgreSQL | required | `official_logo_source_review_required` | none | Batch010 対象。PostgreSQL 公式素材と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `F-121` | SQLite | required | `official_logo_source_review_required` | none | Batch010 対象。SQLite 公式素材と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `F-122` | Prisma | required | `official_logo_source_review_required` | none | Batch010 対象。Prisma 公式素材と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `F-123` | ORM | not_needed | `logo_avoid` | none | Batch011 対象。概念図として表現し、DB/製品ロゴは使わない |
| `F-130` | OAuth | not_needed | `logo_avoid` | none | Batch011 対象。認可フローの概念図。プロバイダロゴ不要 |
| `F-140` | Mermaid | required | `official_logo_source_review_required` | none | Batch011 対象。Mermaid 公式素材と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `F-141` | PlantUML | required | `official_logo_source_review_required` | none | Batch011 対象。PlantUML 公式素材と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `F-150` | MIT ライセンス | not_needed | `logo_avoid` | none | Batch011 対象。一般的な許諾条件の図解で表現する |
| `F-151` | Apache 2.0 | not_needed | `logo_avoid` | none | Batch011 対象。ライセンス条項の図解で表現し、Apache マークは使わない |
| `F-152` | GPL | not_needed | `logo_avoid` | none | Batch011 対象。コピーレフトの図解で表現し、GNU/FSF マークは使わない |
| `F-153` | Creative Commons | required | `official_logo_source_review_required` | none | Batch011 対象。CC 公式アイコンと利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `F-154` | OSS | not_needed | `logo_avoid` | none | Batch011 対象。オープンソース協働の概念図。財団ロゴ不要 |
| `F-160` | DOM | not_needed | `logo_avoid` | none | Batch011 対象。文書ツリーの概念図。ブラウザ/フレームワークロゴ不要 |
| `F-161` | SSR | not_needed | `logo_avoid` | none | Batch011 対象。サーバーからブラウザへの描画フロー。フレームワークロゴ不要 |
| `F-162` | SSG | not_needed | `logo_avoid` | none | Batch011 対象。ビルド時の静的ページ生成フロー。フレームワークロゴ不要 |
| `F-170` | EC2 | required | `official_logo_source_review_required` | none | Batch011 対象。AWS EC2 公式アイコンと利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `F-171` | S3 | required | `official_logo_source_review_required` | none | Batch011 対象。AWS S3 公式アイコンと利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `F-172` | IAM | required | `official_logo_source_review_required` | none | Batch011 対象。AWS IAM 公式アイコンと利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `F-180` | OpenGL | required | `official_logo_source_review_required` | none | Batch011 対象。OpenGL 公式ロゴと利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `F-181` | WebGL | required | `official_logo_source_review_required` | none | Batch011 対象。WebGL 公式ロゴと利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `F-190` | サブルーチン | not_needed | `logo_avoid` | none | Batch011 対象。関数呼び出しと再利用の概念図。言語ロゴ不要 |
| `F-200` | Rust | required | `official_logo_source_review_required` | none | Batch011 対象。Rust 公式ロゴと利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `G-1` | Context | not_needed | `logo_avoid` | none | 概念図。ロゴ不要 |
| `G-2` | Token | not_needed | `logo_avoid` | none | Batch012 対象。トークン化の概念図。AI 企業ロゴ不要 |
| `G-3` | Dictation | not_needed | `logo_avoid` | none | Batch012 対象。音声入力から文字化の概念図。アプリロゴ不要 |
| `G-4` | System Prompt | not_needed | `logo_avoid` | none | Batch012 対象。指示階層の概念図。モデル/プロバイダロゴ不要 |
| `G-5` | Context Window | not_needed | `logo_avoid` | none | Batch012 対象。文脈容量の概念図。モデル/プロバイダロゴ不要 |
| `G-6` | One-shot | not_needed | `logo_avoid` | none | Batch012 対象。1例からの学習/誘導の概念図。モデル/プロバイダロゴ不要 |
| `G-7` | 指示追従性 | not_needed | `logo_avoid` | none | Batch012 対象。指示と出力の照合図。モデル/プロバイダロゴ不要 |
| `G-8` | 決定論的／非決定論的 | not_needed | `logo_avoid` | none | Batch012 対象。同じ入力からの安定/ゆらぎ比較。モデル/プロバイダロゴ不要 |
| `G-9` | effort レベル | not_needed | `logo_avoid` | none | Batch012 対象。推論労力の調整図。モデル/プロバイダロゴ不要 |
| `G-10` | Prompt Engineering | not_needed | `logo_avoid` | none | Batch012 対象。プロンプト改善の概念図。モデル/プロバイダロゴ不要 |
| `G-11` | Context Engineering | not_needed | `logo_avoid` | none | Batch012 対象。文脈組み立ての概念図。モデル/プロバイダロゴ不要 |
| `G-12` | Agent Design | not_needed | `logo_avoid` | none | Batch012 対象。エージェント設計の概念図。モデル/プロバイダロゴ不要 |
| `G-13` | Few-shot Learning | not_needed | `logo_avoid` | none | Batch012 対象。複数例による誘導の概念図。モデル/プロバイダロゴ不要 |
| `G-14` | Thinking モデル | not_needed | `logo_avoid` | none | Batch012 対象。内部作業領域の概念図。モデル/プロバイダロゴ不要 |
| `G-15` | RAG | not_needed | `logo_avoid` | none | Batch012 対象。検索拡張生成の概念図。モデル/プロバイダロゴ不要 |
| `G-16` | Embedding | not_needed | `logo_avoid` | none | Batch012 対象。ベクトル化の概念図。モデル/プロバイダロゴ不要 |
| `G-17` | ベクトル DB | not_needed | `logo_avoid` | none | Batch012 対象。ベクトル検索の概念図。DB/製品ロゴ不要 |
| `G-18` | Chain of Thought | not_needed | `logo_avoid` | none | Batch012 対象。段階的推論の概念図。モデル/プロバイダロゴ不要 |
| `G-19` | Prompt Caching | not_needed | `logo_avoid` | none | Batch012 対象。再利用される文脈キャッシュの概念図。モデル/プロバイダロゴ不要 |
| `G-20` | CLAUDE.md | not_needed | `logo_avoid` | none | Batch012 対象。エージェント指示ファイルの汎用図解。Claude/Anthropic ロゴ不要 |
| `G-21` | AGENTS.md | not_needed | `logo_avoid` | none | Batch012 対象。複数エージェント指示ファイルの汎用図解。製品ロゴ不要 |
| `J-14` | LLM | not_needed | `logo_avoid` | none | 概念図。ロゴ不要 |

## ローカル公式素材あり

現時点で、この台帳内で後合成に使える公式素材は GitHub 系、Claude 系、Cursor、v0、Vercel、Netlify、Cloudflare、Render、Supabase。

| brand | asset | entries |
| :-- | :-- | :-- |
| GitHub Copilot | `assets/logos/github/GitHub_Logos/GitHub Logos/PNG/GitHub_Copilot_Lockup_Black_Clearspace.png` | `B-5` |
| GitHub | `assets/logos/github/GitHub_Logos/GitHub Logos/PNG/GitHub_Lockup_Black_Clearspace.png` | `F-60` |
| Claude | `assets/logos/anthropic/anthropic-media-resources/Anthropic media resources/Anthropic logos/Claude logos/1 Claude logo/PNG/Claude logo - Slate.png` | `B-2` |
| Claude Code | `assets/logos/anthropic/anthropic-media-resources/Anthropic media resources/Anthropic logos/Claude logos/2 Claude Code logo/PNG/Claude Code logo - Slate.png` | `B-7` |
| Cursor | `assets/logos/cursor/cursor-brand-assets/General Logos/Lockup Horizontal/PNG/LOCKUP_HORIZONTAL_2D_LIGHT.png` | `B-4` |
| v0 | `assets/logos/vercel/v0-assets/v0/Light/v0-logo-light.png` | `B-9` |
| Vercel | `assets/logos/vercel/vercel-assets/Vercel/logotype/light/vercel-logotype-light.png` | `B-20` |
| Netlify | `assets/logos/netlify/netlify-logo-full/netlify-logo-full/large/lightmode/logo-netlify-large-monochrome-lightmode.png` | `B-21` |
| Cloudflare | `assets/logos/cloudflare/Cloudflare_logo_kit/Cloudflare_logo_kit/Cloudflare_logo_kit/Cloudflare logo/png/CF_logo_horizontal_singlecolor_blk.png` | `B-22` |
| Render | `assets/logos/render/render-wordmark-from-press.png` | `B-28` |
| Supabase | `assets/logos/supabase/brand-assets/supabase-logo-wordmark--light.png` | `B-29` |

AWS Architecture Icons はローカルにあるが、B-23 にそのまま使うブランド lockup とは別扱いにする。B-23 は公式ロゴ/利用条件を確認するまで `official_logo_source_review_required` のまま止める。Ruby の素材は今回の対象には直接該当しない。

## 次の処理

1. この台帳を先にコミットする。
2. `official_logo_applied` は目視と寸法監査だけ行い、追加のロゴ生成はしない。
3. `official_logo_source_available_needs_import` は、公式素材の取得、`docs/brand_usage_audit.md` への記録、ローカル PNG/SVG 参照化、合成監査の順に進める。
4. `official_logo_source_review_required` は、具体ロゴ・取得経路・許諾条件を確認するまで本番ロゴ合成と本番差し替えを進めない。
5. `base_2to1_ready_logo_blocked` は、公式素材の取得・利用条件確認ができるまで、本番ロゴ合成と本番差し替えを進めない。
6. `logo_avoid` は、汎用図解として本番候補を進めてよい。

## 適用監査

`official_logo_applied` の確認結果は `docs/ponchi_logo_application_audit_2026-06-01.md` に記録する。

## 2:1 ベース再生成

ブランド系の元絵 2:1 ベース再生成結果は `docs/ponchi_brand_base_regeneration_2026-06-01.md` に記録する。
