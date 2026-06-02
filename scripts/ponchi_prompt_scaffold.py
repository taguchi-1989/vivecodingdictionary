#!/usr/bin/env python3
"""Scaffold subject-stack ponchi prompt files from the batch ledger."""
from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
BATCH_LEDGER = REPO / "ledgers" / "ponchi_generation_batches.csv"
PROMPTS = REPO / "assets" / "ponchi" / "pipeline_prompts"


TYPE_BY_CATEGORY = {
    "common": "front_matter",
    "service": "brand_or_service",
    "model": "model_family",
    "benchmark": "benchmark_or_eval",
    "language": "tool_or_language",
    "person_org": "brand_or_service",
    "concept": "concept",
    "history": "history_or_event",
    "mcp": "tool_or_language",
}

BATCH_SCENE_OVERRIDES = {
    "B-30": {
        "visual_subject": "A neutral managed-AI gateway diagram: four unlabeled model tiles flow into a central service hub, then out to a generic application panel, with small security-key and region-shield symbols nearby.",
        "supporting_subjects": "An operations worker comparing model choices on a blank tablet; no real console, no provider names, no product UI.",
        "view_mode": "operation_flow",
    },
    "B-31": {
        "visual_subject": "A before-after whiteboard workflow: left side shows a person stuck with loose blank notes, right side shows the same idea organized into simple unlabeled boxes and arrows on a hand-drawn-style board.",
        "supporting_subjects": "A non-engineer designer using a plain pen and a blank board; no app logo, no readable handwriting.",
        "view_mode": "before_after",
    },
    "B-32": {
        "visual_subject": "A design-to-code bridge: a central blank layout canvas connects a designer on the left to a developer and small AI robot on the right, converting visual blocks into component blocks.",
        "supporting_subjects": "Designer, developer, and small assistant robot; all screens are generic with abstract blocks only.",
        "view_mode": "operation_flow",
    },
    "B-33": {
        "visual_subject": "A choice diagram between two creative workflows: one branch for product interface design blocks, one branch for marketing materials and presentation tiles, with a central decision arrow.",
        "supporting_subjects": "A non-engineer worker deciding between generic design paths with a laptop and phone shown only as blank devices.",
        "view_mode": "before_after",
    },
    "B-40": {
        "visual_subject": "A community-signal hub: a central anonymous discussion cluster connects to three unlabeled community circles, then to a verification checklist and sharing arrow.",
        "supporting_subjects": "A business reader scanning generic comment bubbles and weighing early reports; no community names, no mascot, no real social UI.",
        "view_mode": "structure_map",
    },
    "B-41": {
        "visual_subject": "A preprint flow: a researcher sends blank paper sheets into an open archive hub, then arrows carry the papers to an engineer, a business reader, and a small AI summary robot.",
        "supporting_subjects": "One researcher on the submission side and one non-engineer reader on the receiving side; documents have no text.",
        "view_mode": "operation_flow",
    },
    "B-50": {
        "visual_subject": "A pricing-plan ladder with six unlabeled tiers, usage bars, feature dots, and a person matching a workload card to the right tier.",
        "supporting_subjects": "A worker comparing cost, usage, and team needs with simple abstract plan cards only.",
        "view_mode": "structure_map",
    },
    "B-51": {
        "visual_subject": "A pricing-plan matrix with six unlabeled tiers, different usage bars, and feature-scope icons, shown as a decision aid rather than a real product table.",
        "supporting_subjects": "A worker choosing between personal, team, and enterprise usage levels using blank cards.",
        "view_mode": "structure_map",
    },
    "B-52": {
        "visual_subject": "A three-tier pricing ladder with model-access blocks and feature-range bars expanding from basic to advanced use.",
        "supporting_subjects": "A non-engineer comparing simple plan cards and selecting an appropriate usage level; no plan names.",
        "view_mode": "structure_map",
    },
    "B-60": {
        "visual_subject": "A music-generation flow: a prompt card and simple control knobs feed into waveform blocks, then into a finished song tile and a listener previewing the result.",
        "supporting_subjects": "A creator listening to generated audio through a plain device; no product UI, no album art text.",
        "view_mode": "operation_flow",
    },
    "B-61": {
        "visual_subject": "An open music model pipeline: lyric-like blank sheets, rhythm marks, and waveform conditioning blocks feed into a clean audio waveform output.",
        "supporting_subjects": "A researcher comparing two unlabeled audio clips and a small AI robot indicating the selected path.",
        "view_mode": "operation_flow",
    },
    "C-1": {
        "visual_subject": "An AI organization map: research lab, product workbench, API platform, and safety review desk connect around a neutral company building.",
        "supporting_subjects": "Researchers, product builders, and reviewers shown as small abstract roles; no real people or product UI.",
        "view_mode": "structure_map",
    },
    "C-2": {
        "visual_subject": "An AI safety lab map: research papers, a safety shield, assistant product blocks, and governance review connect around a neutral organization building.",
        "supporting_subjects": "Two abstract founder silhouettes and a research reviewer, with no real-person likeness.",
        "view_mode": "structure_map",
    },
    "C-3": {
        "visual_subject": "A research-organization structure: scientific discovery icons, model service blocks, and a lab-to-product path connect around a neutral research building.",
        "supporting_subjects": "One researcher and one business user looking at abstract science and AI-service blocks; no named achievements.",
        "view_mode": "structure_map",
    },
    "C-4": {
        "visual_subject": "An AI department ecosystem: open model boxes, research lab blocks, product chat bubbles, and mobile integration panels form a fan around a central hub.",
        "supporting_subjects": "A young engineer observing how research, open models, and products connect; no real app icons.",
        "view_mode": "structure_map",
    },
    "C-5": {
        "visual_subject": "A real-time AI company pipeline: compute racks feed model training, which feeds a generic live information stream and chat assistant panel.",
        "supporting_subjects": "A business user comparing a live feed and assistant output on blank devices; no social-media marks.",
        "view_mode": "operation_flow",
    },
    "C-6": {
        "visual_subject": "A two-path model company diagram: one path runs on a local laptop, another path calls a cloud API, both emerging from a shared neutral model hub.",
        "supporting_subjects": "One developer testing locally and one developer using a cloud connection; no cloud-provider logos.",
        "view_mode": "operation_flow",
    },
    "C-7": {
        "visual_subject": "An AI model-sharing hub: model boxes, dataset table, demo window, and library package pillars surround a central neutral platform hub.",
        "supporting_subjects": "A researcher searching and testing model cards on blank panels; no mascot, no emoji-like face, no product UI.",
        "view_mode": "structure_map",
    },
    "C-8": {
        "visual_subject": "A company AI-organization hub: coding assistant, office document assistant, cloud model API, and small-model lab panels radiate from a central governance block.",
        "supporting_subjects": "A business worker realizing these tools share one corporate AI organization; all panels are unlabeled.",
        "view_mode": "structure_map",
    },
    "C-9": {
        "visual_subject": "An AI infrastructure stack: GPU-like compute racks at the bottom, a software platform layer in the middle, and generic cloud AI services at the top.",
        "supporting_subjects": "A business person connecting AI-service latency and cost to underlying hardware demand; no chip model names or cloud logos.",
        "view_mode": "structure_map",
    },
    "C-10": {
        "visual_subject": "A company-to-model relationship map: a neutral AI startup building connects to a generic model family stack, with a comparison row of other unlabeled startup tiles.",
        "supporting_subjects": "A technical reader comparing blank benchmark sheets; no real company logos, model names, national flags, or leaderboard text.",
        "view_mode": "structure_map",
    },
    "C-11": {
        "visual_subject": "A model-company transition map: an open model release path, API service block, and enterprise adoption path connect around a neutral AI company hub.",
        "supporting_subjects": "A developer and business reader comparing blank model cards and deployment blocks; no product UI, flags, or real logos.",
        "view_mode": "operation_flow",
    },
    "C-12": {
        "visual_subject": "A semiconductor supply-chain map: design files flow to wafer fabrication, packaging, and AI accelerator demand, shown as stacked factory and chip layers.",
        "supporting_subjects": "A business reader tracing how AI model demand reaches generic chip manufacturing; no official logos, chip model names, or national flags.",
        "view_mode": "structure_map",
    },
    "C-13": {
        "visual_subject": "An AI inference accelerator flow: compute racks feed a low-latency inference lane, then generic application responses return quickly to users.",
        "supporting_subjects": "An engineer comparing blank latency gauges and throughput bars; no official logos, chip labels, or product UI.",
        "view_mode": "operation_flow",
    },
    "C-14": {
        "visual_subject": "An AI chip competitor stack: GPUs, CPUs, accelerator cards, and software layers connect to model training and inference workloads.",
        "supporting_subjects": "A technical buyer comparing blank hardware options and workload cards; no official logos, chip model names, or brand colors.",
        "view_mode": "structure_map",
    },
    "C-50": {
        "visual_subject": "A four-milestone AI industry timeline: product launch, leadership crisis and return, policy testimony, and future platform announcements shown as unlabeled event cards.",
        "supporting_subjects": "An abstract executive silhouette at a microphone connected to the event cards; no real-person likeness, quotes, dates, company logos, or readable text.",
        "view_mode": "before_after",
    },
    "C-51": {
        "visual_subject": "A safety-focused AI company leadership map: research paper stack, model product block, safety review gate, and company growth path connect around an abstract leader silhouette.",
        "supporting_subjects": "Generic researchers and reviewers around blank documents; no real-person likeness, official logos, or readable text.",
        "view_mode": "structure_map",
    },
    "C-52": {
        "visual_subject": "A research-to-product achievement map: scientific discovery blocks, game-solving milestone, lab leadership, and AI model platform path connect around an abstract researcher silhouette.",
        "supporting_subjects": "Generic lab workers and blank science cards; no real-person likeness, official logos, named achievements, or readable text.",
        "view_mode": "structure_map",
    },
    "C-53": {
        "visual_subject": "An educator-engineer career map: neural network teaching board, autonomous systems block, code notebook, and practical AI commentary lane connect around an abstract engineer silhouette.",
        "supporting_subjects": "A learner reading blank diagrams and code cards; no real-person likeness, company logos, product UI, or readable text.",
        "view_mode": "structure_map",
    },
    "C-54": {
        "visual_subject": "A research founder timeline: neural network breakthrough, lab founding, alignment debate, and independent research path shown as connected unlabeled milestone cards.",
        "supporting_subjects": "An abstract researcher silhouette reviewing blank papers; no real-person likeness, official logos, quotes, or readable text.",
        "view_mode": "before_after",
    },
    "C-55": {
        "visual_subject": "A product leader map: model research, product launch, multimodal demo, and independent lab path connect around an abstract product-builder silhouette.",
        "supporting_subjects": "Generic product team members reviewing blank launch cards; no real-person likeness, official logos, product UI, or readable text.",
        "view_mode": "structure_map",
    },
    "C-56": {
        "visual_subject": "A deep learning research lineage map: convolutional model blocks, academic lab, open research group, and industry AI organization connect around an abstract scientist silhouette.",
        "supporting_subjects": "Students and engineers studying blank network diagrams; no real-person likeness, official logos, or readable text.",
        "view_mode": "structure_map",
    },
    "C-57": {
        "visual_subject": "A neural network pioneer timeline: early research, deep learning breakthrough, public warning, and policy discussion shown as connected unlabeled cards.",
        "supporting_subjects": "An abstract elder researcher silhouette with blank papers and a generic lecture board; no real-person likeness, quotes, logos, or readable text.",
        "view_mode": "before_after",
    },
    "C-58": {
        "visual_subject": "A multi-company AI influence map: electric vehicles, rockets, social platform data, and AI assistant development connect around an abstract entrepreneur silhouette.",
        "supporting_subjects": "A business reader tracing cross-industry influence with blank company tiles; no real-person likeness, official logos, social-media marks, or readable text.",
        "view_mode": "structure_map",
    },
    "C-59": {
        "visual_subject": "A GPU-to-AI platform leadership map: graphics processors, data center racks, developer software, and AI model demand connect around an abstract CEO silhouette.",
        "supporting_subjects": "A technical buyer looking at blank hardware demand charts; no real-person likeness, official logos, chip model names, or readable text.",
        "view_mode": "structure_map",
    },
    "C-60": {
        "visual_subject": "A futurist prediction timeline: computing trends, AI assistants, health technology, and long-term forecast cards connect around an abstract author silhouette.",
        "supporting_subjects": "A reader comparing blank future scenarios on a horizontal timeline; no real-person likeness, book covers, logos, or readable text.",
        "view_mode": "before_after",
    },
    "C-80": {
        "visual_subject": "A learning-channel discovery flow: a viewer watches generic AI tool comparison videos, then turns the takeaways into a simple work checklist.",
        "supporting_subjects": "A business worker using a blank smartphone and notebook; video thumbnails are generic blocks with no channel icon, YouTube UI, or readable text.",
        "view_mode": "operation_flow",
    },
    "C-81": {
        "visual_subject": "A practical AI workflow channel map: office tasks, automation steps, and tool-selection cards connect from a generic creator desk to a business viewer.",
        "supporting_subjects": "A worker watching blank tutorial panels and applying them to a simple office workflow; no mascot, real channel icon, platform UI, or readable text.",
        "view_mode": "operation_flow",
    },
    "C-82": {
        "visual_subject": "A daily AI commentary channel map: news cards, essential-point filter, and viewer action notes flow from a generic presenter desk to a reader.",
        "supporting_subjects": "A viewer sorting blank AI news cards by importance; no real channel icon, platform UI, portrait likeness, or readable text.",
        "view_mode": "operation_flow",
    },
    "C-83": {
        "visual_subject": "A paper-explainer channel map: research paper stack, concept simplification board, and practical takeaway cards flow to a learner.",
        "supporting_subjects": "A learner watching blank explanation panels and extracting key ideas; no real channel icon, platform UI, mascot, or readable text.",
        "view_mode": "operation_flow",
    },
    "D-42": {
        "visual_subject": "An open model family map: compact open model cards connect to local laptop use, research fine-tuning, and cloud deployment lanes.",
        "supporting_subjects": "A developer comparing lightweight model cards; no Google colors, Gemma logo, product UI, or readable text.",
        "view_mode": "structure_map",
    },
    "D-43": {
        "visual_subject": "A multilingual open model family map: model cards flow to coding, math, long-context documents, and local deployment lanes.",
        "supporting_subjects": "A developer choosing between generic model sizes; no Qwen logo, Alibaba marks, product UI, or readable text.",
        "view_mode": "structure_map",
    },
    "D-44": {
        "visual_subject": "A long-context assistant model workflow: large document stacks and search cards feed a model hub, then answers become summarized action cards.",
        "supporting_subjects": "A reader tracing document evidence into answer cards; no Kimi or Moonshot logo, product UI, or readable text.",
        "view_mode": "operation_flow",
    },
    "D-45": {
        "visual_subject": "An open-weight language model stack: base model, chat tuning, tool use, and deployment cards connect into a neutral service hub.",
        "supporting_subjects": "An engineer comparing local and server deployment blocks; no GLM or Zhipu logo, product UI, or readable text.",
        "view_mode": "structure_map",
    },
    "D-46": {
        "visual_subject": "A large efficient model architecture diagram: training data blocks and compute lanes feed a model core, then coding and chat outputs branch out.",
        "supporting_subjects": "A technical reader comparing efficiency bars and output cards; no DeepSeek logo, product UI, or readable text.",
        "view_mode": "operation_flow",
    },
    "D-47": {
        "visual_subject": "A reasoning model pipeline: hard problem cards enter a search-and-verify loop, then produce checked solution cards.",
        "supporting_subjects": "A reader comparing normal answer flow with deeper reasoning flow; no DeepSeek logo, product UI, or readable text.",
        "view_mode": "before_after",
    },
    "D-50": {
        "visual_subject": "A text-to-image generation flow: prompt card and style controls feed an image model core, then produce several image candidate panels and a review step.",
        "supporting_subjects": "A creator selecting a generated image from blank thumbnails; no OpenAI logo, product UI, or readable text.",
        "view_mode": "operation_flow",
    },
    "D-51": {
        "visual_subject": "A text-to-image model comparison map: prompt, reference image, and safety review feed an image generator, then multiple polished output panels appear.",
        "supporting_subjects": "A designer comparing generic image candidates; no Google colors, Imagen logo, product UI, or readable text.",
        "view_mode": "operation_flow",
    },
    "D-52": {
        "visual_subject": "A text-to-video generation flow: prompt board and storyboard cards feed a video model, then timeline frames and motion review cards come out.",
        "supporting_subjects": "A video creator reviewing blank storyboard frames; no OpenAI logo, product UI, or readable text.",
        "view_mode": "operation_flow",
    },
    "D-53": {
        "visual_subject": "A video generation model workflow: storyboard, camera movement, and scene consistency cards flow into a video model and output a frame strip.",
        "supporting_subjects": "A creator comparing generated scene strips; no Google colors, Veo logo, product UI, or readable text.",
        "view_mode": "operation_flow",
    },
    "D-54": {
        "visual_subject": "An image diffusion model workflow: noise grid gradually denoises into image candidates, then tuning and safety review select the output.",
        "supporting_subjects": "A designer watching generic denoising steps; no Stability AI logo, Stable Diffusion logo, product UI, or readable text.",
        "view_mode": "operation_flow",
    },
    "D-55": {
        "visual_subject": "An image editing assistant workflow: reference image, prompt card, and masked edit region feed a model, producing before-after image panels.",
        "supporting_subjects": "A creator comparing edits on blank image cards; no product logo, banana mascot, product UI, or readable text.",
        "view_mode": "before_after",
    },
    "D-56": {
        "visual_subject": "A video generation model workflow: prompt, motion path, and scene cards feed a model, then a frame strip with temporal consistency checks comes out.",
        "supporting_subjects": "A video editor reviewing generic motion frames; no Seedance logo, ByteDance marks, product UI, or readable text.",
        "view_mode": "operation_flow",
    },
    "D-57": {
        "visual_subject": "A creative image/video tool workflow: concept board, prompt, and reference assets flow into a generation canvas, then variants and review cards appear.",
        "supporting_subjects": "A designer comparing generic creative outputs; no Flow logo, product UI, or readable text.",
        "view_mode": "operation_flow",
    },
    "D-58": {
        "visual_subject": "A visual remix workflow: reference images and prompt cards feed a model hub, then combined visual variants and style-transfer results appear.",
        "supporting_subjects": "A creator organizing reference cards; no Whisk logo, product UI, or readable text.",
        "view_mode": "operation_flow",
    },
    "D-60": {
        "visual_subject": "A historical game-AI achievement diagram: game board states feed a search tree and self-play training loop, then a strategy improvement chart appears.",
        "supporting_subjects": "A researcher observing the board and search tree; no DeepMind logo, AlphaGo logo, product UI, or readable text.",
        "view_mode": "structure_map",
    },
    "D-70": {
        "visual_subject": "An AI solution deployment workflow: customer problem cards feed requirements, model selection, integration, evaluation, and operational support blocks.",
        "supporting_subjects": "A consultant and business user reviewing generic workflow cards; no Amical logo, product UI, or readable text.",
        "view_mode": "operation_flow",
    },
    "D-71": {
        "visual_subject": "A speech recognition model workflow: audio waveform and microphone input feed a speech model, then transcript, timestamps, and translation cards come out.",
        "supporting_subjects": "A user reviewing audio-to-text cards; no OpenAI logo, product UI, or readable text.",
        "view_mode": "operation_flow",
    },
    "E-1": {
        "visual_subject": "A coding benchmark workflow: bug report and repository snapshot feed a coding agent, then patch, tests, and pass/fail evaluation cards appear.",
        "supporting_subjects": "A reviewer comparing benchmark cases; no official logos, product UI, or readable text.",
        "view_mode": "operation_flow",
    },
    "E-2": {
        "visual_subject": "A verified coding benchmark workflow: human-filtered task set, repository snapshot, patch attempt, and stricter pass/fail gate connect in sequence.",
        "supporting_subjects": "A reviewer marking verified cases with generic check cards; no official logos, product UI, or readable text.",
        "view_mode": "operation_flow",
    },
    "E-3": {
        "visual_subject": "A terminal-task benchmark workflow: command-line task card, repository files, shell execution panel, and scoring report connect in sequence.",
        "supporting_subjects": "A reviewer watches a coding agent use a generic terminal; no official logos, product UI, readable text, red/green status colors, or real command names.",
        "view_mode": "operation_flow",
    },
    "E-4": {
        "visual_subject": "A function-synthesis benchmark workflow: short coding problem card feeds a code-generation block, unit tests run, and a neutral score card appears.",
        "supporting_subjects": "A reviewer compares generated function blocks and test result dots; no official logos, product UI, readable text, or red/green marks.",
        "view_mode": "operation_flow",
    },
    "E-20": {
        "visual_subject": "A broad knowledge benchmark map: many subject cards from different domains feed a model answer block, then a scored evaluation panel summarizes coverage.",
        "supporting_subjects": "A reviewer sorting generic domain cards; no official logos, school names, product UI, readable text, or red/green marks.",
        "view_mode": "structure_map",
    },
    "E-21": {
        "visual_subject": "A harder knowledge benchmark map: ambiguous question cards, distractor choices, reasoning filter, and stricter scoring panel connect left to right.",
        "supporting_subjects": "A reviewer separating easy and hard cases using blank cards; no official logos, product UI, readable text, or red/green marks.",
        "view_mode": "before_after",
    },
    "E-22": {
        "visual_subject": "A graduate-level science question benchmark: expert question cards feed a reasoning model block, then evidence checks and answer scoring cards appear.",
        "supporting_subjects": "A reviewer with generic science symbols and blank answer cards; no institution logos, product UI, readable text, or red/green marks.",
        "view_mode": "operation_flow",
    },
    "E-23": {
        "visual_subject": "A grade-school math reasoning benchmark: word-problem cards become equation blocks, step-by-step reasoning tiles, and final answer scoring.",
        "supporting_subjects": "A reviewer checking arithmetic steps on blank cards; no official logos, classroom branding, readable text, or red/green marks.",
        "view_mode": "operation_flow",
    },
    "E-24": {
        "visual_subject": "A challenging math benchmark workflow: theorem-like problem cards feed scratchpad reasoning, symbolic transformation tiles, and a neutral scoring panel.",
        "supporting_subjects": "A reviewer comparing solution paths on blank math cards; no official logos, readable formulas, product UI, or red/green marks.",
        "view_mode": "operation_flow",
    },
    "E-25": {
        "visual_subject": "A contest math benchmark diagram: timed problem set, reasoning workspace, answer selection, and ranked score chart connect in a clean flow.",
        "supporting_subjects": "A reviewer monitoring generic competition-style math cards; no official logos, readable formulas, medals with text, or red/green marks.",
        "view_mode": "operation_flow",
    },
    "E-26": {
        "visual_subject": "A very hard multi-domain exam benchmark: expert-level question cards from science, humanities, coding, and logic feed a model and strict scoring gate.",
        "supporting_subjects": "A reviewer filtering many blank expert cards into a difficulty ladder; no official logos, product UI, readable text, or red/green marks.",
        "view_mode": "structure_map",
    },
    "E-27": {
        "visual_subject": "An intelligence-test benchmark map: pattern puzzles, sequence cards, spatial reasoning tiles, and answer-choice evaluation connect around a model block.",
        "supporting_subjects": "A reviewer comparing abstract puzzle cards; no official logos, readable text, product UI, or red/green marks.",
        "view_mode": "structure_map",
    },
    "E-30": {
        "visual_subject": "An agent benchmark workflow: user goal, tool calls, simulated environment state, and task success scoring connect in an evaluation loop.",
        "supporting_subjects": "A reviewer watches an agent choose tools on generic cards; no official logos, product UI, readable text, or red/green marks.",
        "view_mode": "operation_flow",
    },
    "E-31": {
        "visual_subject": "A web-task benchmark workflow: generic browser window, form-like panels, navigation choices, and completion scoring connect as an agent path.",
        "supporting_subjects": "A reviewer tracks an agent through blank web pages; no real website UI, browser logos, product logos, readable text, or red/green marks.",
        "view_mode": "operation_flow",
    },
    "E-32": {
        "visual_subject": "A general assistant benchmark workflow: file cards, web snippets, reasoning notes, and final answer evaluation combine into a multi-step task path.",
        "supporting_subjects": "A reviewer assembling evidence from generic sources; no official logos, real websites, product UI, readable text, or red/green marks.",
        "view_mode": "operation_flow",
    },
    "E-33": {
        "visual_subject": "An agent-suite benchmark map: multiple environment cards, tool-use lanes, memory block, and scoring dashboard surround a central agent evaluator.",
        "supporting_subjects": "A reviewer comparing agent behaviors across blank tasks; no official logos, product UI, readable text, or red/green marks.",
        "view_mode": "structure_map",
    },
    "E-34": {
        "visual_subject": "An operating-system task benchmark workflow: desktop-like generic panels, file operations, settings cards, and completion score connect along an agent path.",
        "supporting_subjects": "A reviewer watches an agent manipulate neutral OS panels; no real OS icons, app logos, readable text, or red/green marks.",
        "view_mode": "operation_flow",
    },
    "E-50": {
        "visual_subject": "A model comparison arena: two anonymous model answer cards face a blind user vote, then aggregate preference bars update on a neutral leaderboard.",
        "supporting_subjects": "A reviewer comparing answer quality without seeing model identities; no official logos, product UI, readable text, or red/green marks.",
        "view_mode": "operation_flow",
    },
    "E-51": {
        "visual_subject": "A community model-rating arena: many anonymous model cards enter pairwise comparisons, user preference votes flow into a ranking chart.",
        "supporting_subjects": "A reviewer studies generic ranking movement and uncertainty bars; no organization logos, product UI, readable text, or red/green marks.",
        "view_mode": "structure_map",
    },
    "F-3": {
        "visual_subject": "A programming language workflow: code file cards feed an interpreter, package blocks, data processing lane, and script automation output.",
        "supporting_subjects": "A developer connects generic code, data table, and automation blocks; no Python logo, snake shape, package logos, product UI, or readable code.",
        "view_mode": "operation_flow",
    },
    "F-4": {
        "visual_subject": "A web document structure workflow: nested content blocks feed a browser-like preview panel and accessibility outline.",
        "supporting_subjects": "A developer maps page sections to rendered layout blocks; no HTML5 shield logo, browser logos, product UI, or readable code.",
        "view_mode": "operation_flow",
    },
    "F-5": {
        "visual_subject": "A styling workflow: plain layout blocks pass through selector-like style cards, spacing controls, and responsive preview panels.",
        "supporting_subjects": "A designer and developer compare before and after visual styling; no CSS3 shield logo, product UI, or readable code.",
        "view_mode": "before_after",
    },
    "F-6": {
        "visual_subject": "A lightweight writing-to-preview workflow: plain manuscript cards become headings, lists, image placeholders, and a preview page.",
        "supporting_subjects": "A writer edits simple blank document cards; no Markdown logo, product UI, or readable text.",
        "view_mode": "operation_flow",
    },
    "F-7": {
        "visual_subject": "A configuration data workflow: nested setting cards feed deployment options, environment blocks, and validation checks.",
        "supporting_subjects": "A developer organizes structured configuration cards; no logos, product UI, or readable keys.",
        "view_mode": "structure_map",
    },
    "F-8": {
        "visual_subject": "A data exchange workflow: API response blocks become nested object cards, list arrays, and application state panels.",
        "supporting_subjects": "A developer traces structured data between server and client blocks; no logos, product UI, or readable keys.",
        "view_mode": "operation_flow",
    },
    "F-9": {
        "visual_subject": "A vector graphics workflow: shape primitives, paths, and style attributes combine into a scalable illustration preview.",
        "supporting_subjects": "A designer zooms from small icon to large poster without pixelation; no SVG logo, product UI, or readable code.",
        "view_mode": "before_after",
    },
    "F-10": {
        "visual_subject": "A component-based UI workflow: state block, component tree, reusable cards, and rendered interface panels connect in sequence.",
        "supporting_subjects": "A developer assembles generic UI components; no React atom logo, product UI, brand colors, or readable code.",
        "view_mode": "structure_map",
    },
    "F-11": {
        "visual_subject": "A full-stack web framework workflow: route cards, server rendering block, API lane, and deployed page preview connect together.",
        "supporting_subjects": "A developer reviews generic application architecture; no Next.js logo, Vercel marks, product UI, or readable code.",
        "view_mode": "operation_flow",
    },
    "F-12": {
        "visual_subject": "A desktop app packaging workflow: web UI blocks combine with native shell, file access, and desktop window output.",
        "supporting_subjects": "A developer compares web app and desktop app delivery; no Electron logo, app icons, product UI, or readable code.",
        "view_mode": "operation_flow",
    },
    "F-13": {
        "visual_subject": "A lightweight desktop app workflow: frontend panel, native command bridge, secure permission gate, and packaged app output.",
        "supporting_subjects": "A developer checks smaller desktop app architecture; no Tauri logo, app icons, product UI, or readable code.",
        "view_mode": "operation_flow",
    },
    "F-14": {
        "visual_subject": "A 3D web graphics workflow: geometry primitives, material cards, camera view, and interactive canvas output connect left to right.",
        "supporting_subjects": "A developer manipulates generic 3D scene blocks; no three.js logo, product UI, or readable code.",
        "view_mode": "operation_flow",
    },
    "F-15": {
        "visual_subject": "A component library workflow: accessible primitive blocks, theme tokens, copied component cards, and polished UI panels connect together.",
        "supporting_subjects": "A developer assembles generic design-system components; no shadcn/ui logo, product UI, or readable code.",
        "view_mode": "structure_map",
    },
    "F-16": {
        "visual_subject": "A utility-first styling workflow: small utility chips combine into layout, spacing, color, and responsive preview panels.",
        "supporting_subjects": "A developer builds a generic interface from utility blocks; no Tailwind logo, brand colors, product UI, or readable class names.",
        "view_mode": "operation_flow",
    },
    "F-17": {
        "visual_subject": "A content-site framework workflow: content collections, island components, static build output, and fast page preview connect in sequence.",
        "supporting_subjects": "A developer maps content and interactive islands; no Astro logo, product UI, or readable code.",
        "view_mode": "operation_flow",
    },
    "F-20": {
        "visual_subject": "A code linting workflow: source file cards feed rule checks, issue grouping, and neutral quality report panels.",
        "supporting_subjects": "A developer reviews abstract code-quality warnings; no ESLint logo, product UI, readable code, or red/green status colors.",
        "view_mode": "operation_flow",
    },
    "F-21": {
        "visual_subject": "A code formatting workflow: messy layout blocks transform into aligned clean blocks through an automatic formatting pass.",
        "supporting_subjects": "A developer compares before and after formatting; no Prettier logo, product UI, readable code, or red/green status colors.",
        "view_mode": "before_after",
    },
    "F-30": {
        "visual_subject": "A code editor workspace map: file explorer panel, editor panes, terminal panel, extension area, and debugging controls connect around a workspace.",
        "supporting_subjects": "A developer works in a generic editor interface; no VS Code logo, Microsoft marks, product UI, or readable code.",
        "view_mode": "structure_map",
    },
    "F-34": {
        "visual_subject": "An editor extension ecosystem map: marketplace-like cards, install flow, command palette block, and enhanced editor capability panels.",
        "supporting_subjects": "A developer adds generic extensions to a neutral editor; no VS Code logo, extension icons, marketplace UI, or readable text.",
        "view_mode": "operation_flow",
    },
    "F-35": {
        "visual_subject": "A document preview extension workflow: markdown document cards feed a preview pane with diagrams, table blocks, and export panel.",
        "supporting_subjects": "A writer reviews enhanced preview output in a neutral editor; no extension logo, product UI, or readable text.",
        "view_mode": "operation_flow",
    },
    "F-36": {
        "visual_subject": "A git history visualization workflow: commit nodes, branch lanes, merge path, and file-change cards form a graph inspection view.",
        "supporting_subjects": "A developer traces repository history in a neutral editor; no Git Graph logo, GitHub logo, product UI, or readable commit IDs.",
        "view_mode": "structure_map",
    },
    "F-37": {
        "visual_subject": "An editor localization extension workflow: language pack card, settings panel, translated interface blocks, and user preference controls connect together.",
        "supporting_subjects": "A developer switches a neutral editor interface into Japanese-friendly labels shown only as blank bars; no VS Code logo, extension logo, marketplace UI, or readable text.",
        "view_mode": "operation_flow",
    },
    "F-38": {
        "visual_subject": "A markdown editing extension workflow: document card, shortcut toolbar, table-of-contents block, preview pane, and export card connect in sequence.",
        "supporting_subjects": "A writer improves a neutral editor document; no Markdown All in One logo, marketplace UI, product UI, or readable text.",
        "view_mode": "operation_flow",
    },
    "F-40": {
        "visual_subject": "A package manager workflow: package registry block, dependency tree cards, install command panel, and project package folder connect left to right.",
        "supporting_subjects": "A developer traces dependency installation; no npm logo, package logos, product UI, or readable command text.",
        "view_mode": "operation_flow",
    },
    "F-41": {
        "visual_subject": "A fast development build workflow: source modules feed a dev server card, hot-update loop, bundled output, and browser preview panel.",
        "supporting_subjects": "A developer watches modules update quickly; no Vite logo, lightning brand mark, product UI, or readable code.",
        "view_mode": "operation_flow",
    },
    "F-42": {
        "visual_subject": "A build process workflow: source files, dependency blocks, transform steps, bundle output, and deployment artifact connect in a pipeline.",
        "supporting_subjects": "A developer checks an abstract build pipeline; no official logos, product UI, or readable command text.",
        "view_mode": "operation_flow",
    },
    "F-44": {
        "visual_subject": "A workspace package manager workflow: shared package store, project dependency links, lockfile card, and workspace folders connect as a graph.",
        "supporting_subjects": "A developer compares efficient dependency sharing; no pnpm logo, package logos, product UI, or readable command text.",
        "view_mode": "structure_map",
    },
    "F-50": {
        "visual_subject": "A version control system map: working tree, staging area, commit history, branch lanes, and remote repository block connect together.",
        "supporting_subjects": "A developer traces changes through abstract version-control stages; no Git logo, GitHub logo, product UI, or readable commit IDs.",
        "view_mode": "structure_map",
    },
    "F-51": {
        "visual_subject": "A push operation workflow: local commit stack sends changes through an upload arrow to a remote repository block and team sync panel.",
        "supporting_subjects": "A developer sends local history to a shared remote; no Git logo, GitHub logo, product UI, or readable command text.",
        "view_mode": "operation_flow",
    },
    "F-52": {
        "visual_subject": "A pull operation workflow: remote repository updates flow down to local working files, then conflict check and updated workspace panels appear.",
        "supporting_subjects": "A developer receives shared changes into a local workspace; no Git logo, GitHub logo, product UI, or readable command text.",
        "view_mode": "operation_flow",
    },
    "F-53": {
        "visual_subject": "A branch concept diagram: one commit line splits into parallel feature lanes and later returns toward the main lane.",
        "supporting_subjects": "A developer compares isolated feature work with shared history; no Git logo, GitHub logo, product UI, or readable branch names.",
        "view_mode": "structure_map",
    },
    "F-54": {
        "visual_subject": "A commit concept diagram: file changes are grouped into a snapshot card, then appended to a chronological history lane.",
        "supporting_subjects": "A developer packages a set of changes into one history point; no Git logo, GitHub logo, product UI, or readable commit IDs.",
        "view_mode": "operation_flow",
    },
    "F-55": {
        "visual_subject": "A merge concept diagram: two branch lanes converge through a merge gate into a single combined history lane.",
        "supporting_subjects": "A developer resolves two streams of work into one shared line; no Git logo, GitHub logo, product UI, or readable labels.",
        "view_mode": "operation_flow",
    },
    "F-56": {
        "visual_subject": "A file-ignore workflow: project files pass through a filter card that separates tracked files from ignored cache and build artifacts.",
        "supporting_subjects": "A developer keeps generated files out of version tracking; no Git logo, GitHub logo, product UI, or readable filenames.",
        "view_mode": "operation_flow",
    },
    "F-57": {
        "visual_subject": "A repository structure map: source folders, history lane, settings card, collaboration members, and remote storage block form one project container.",
        "supporting_subjects": "A developer explains what lives inside a repository; no Git logo, GitHub logo, product UI, or readable file names.",
        "view_mode": "structure_map",
    },
    "F-58": {
        "visual_subject": "A stash workflow: temporary change cards move into a holding shelf, the working area becomes clean, then the cards can return later.",
        "supporting_subjects": "A developer temporarily shelves unfinished changes; no Git logo, GitHub logo, product UI, or readable command text.",
        "view_mode": "before_after",
    },
    "F-59": {
        "visual_subject": "A project README workflow: project summary card, setup steps, architecture diagram, and usage notes become a front-page document for collaborators.",
        "supporting_subjects": "A developer turns project knowledge into a blank documentation page; no GitHub logo, product UI, or readable prose.",
        "view_mode": "operation_flow",
    },
    "F-60": {
        "visual_subject": "A code hosting platform map: remote repository block, collaboration lanes, issue cards, pull request gate, and automation panel connect together.",
        "supporting_subjects": "A developer coordinates project work on a generic hosting platform; no GitHub logo, Octocat, product UI, or readable text.",
        "view_mode": "structure_map",
    },
    "F-61": {
        "visual_subject": "A pull request review workflow: feature branch changes flow into review cards, comment bubbles, approval gate, and merge destination.",
        "supporting_subjects": "A developer and reviewer compare proposed changes; no GitHub logo, product UI, or readable comments.",
        "view_mode": "operation_flow",
    },
    "F-62": {
        "visual_subject": "An automation workflow map: repository event card triggers jobs, runner blocks, test panels, artifact box, and deployment gate.",
        "supporting_subjects": "A developer watches automated checks run after a code event; no GitHub logo, Actions logo, product UI, or readable job names.",
        "view_mode": "operation_flow",
    },
    "F-71": {
        "visual_subject": "A fast code search workflow: query card scans folders and files, filters matching lines, and returns grouped results to a developer.",
        "supporting_subjects": "A developer searches a project tree quickly; no ripgrep logo, product UI, or readable search text.",
        "view_mode": "operation_flow",
    },
    "F-80": {
        "visual_subject": "A server-side runtime workflow: script module cards feed an event loop, package blocks, API server, and response panels.",
        "supporting_subjects": "A developer runs generic backend JavaScript modules; no Node.js logo, hexagon mark, package logos, product UI, or readable code.",
        "view_mode": "operation_flow",
    },
    "F-81": {
        "visual_subject": "A shell command workflow: prompt-like blank command cards feed file operations, pipes, filters, and script automation output.",
        "supporting_subjects": "A developer chains generic terminal actions; no Bash logo, product UI, readable commands, or shell text.",
        "view_mode": "operation_flow",
    },
    "F-82": {
        "visual_subject": "A cross-platform shell environment workflow: one desktop block connects to a Linux-like terminal environment, file bridge, and toolchain panels.",
        "supporting_subjects": "A developer moves between host files and a generic Unix environment; no Windows logo, Linux mascot, Microsoft marks, product UI, or readable text.",
        "view_mode": "operation_flow",
    },
    "F-83": {
        "visual_subject": "A command shell automation workflow: command cards feed object-like output blocks, script pipeline, admin task panel, and report cards.",
        "supporting_subjects": "A developer automates system tasks in a generic shell; no PowerShell logo, Microsoft marks, product UI, or readable commands.",
        "view_mode": "operation_flow",
    },
    "F-84": {
        "visual_subject": "A modern terminal workspace workflow: terminal window blocks, tabs, split panes, shell session cards, and keyboard-driven navigation connect together.",
        "supporting_subjects": "A developer uses a generic terminal emulator; no Ghostty logo, ghost icon, product UI, or readable shell text.",
        "view_mode": "structure_map",
    },
    "F-85": {
        "visual_subject": "An assistant framework workflow: prompt command cards, role presets, tool routing, task plan, and generated assistance panels connect in sequence.",
        "supporting_subjects": "A developer coordinates a generic AI assistant framework; no Claude logo, SuperClaude logo, product UI, or readable prompt text.",
        "view_mode": "operation_flow",
    },
    "F-86": {
        "visual_subject": "A local model runtime workflow: model file cards feed local runtime block, chat panel, tool connection, and offline workstation output.",
        "supporting_subjects": "A developer runs generic local AI models; no Ollama logo, llama animal, product UI, or readable model names.",
        "view_mode": "operation_flow",
    },
    "F-87": {
        "visual_subject": "A permission escalation workflow: normal user task card passes through a privilege gate, approval shield, and protected system action panel.",
        "supporting_subjects": "A developer carefully performs an admin action; no logos, product UI, readable commands, or red warning color.",
        "view_mode": "operation_flow",
    },
    "F-90": {
        "visual_subject": "A container workflow: application files and dependency blocks are packed into a container box, then run across server and cloud-like environment panels.",
        "supporting_subjects": "A developer compares local and deployment runtime consistency; no Docker whale logo, product UI, container brand marks, or readable text.",
        "view_mode": "operation_flow",
    },
    "F-91": {
        "visual_subject": "An environment configuration workflow: secret setting cards and runtime configuration blocks feed app startup without exposing values.",
        "supporting_subjects": "A developer separates configuration from code; no logos, product UI, readable variable names, or key strings.",
        "view_mode": "operation_flow",
    },
    "F-100": {
        "visual_subject": "A file extension guide map: generic file cards sort into image, audio, video, document, code, and archive groups.",
        "supporting_subjects": "A learner compares file types by icons and usage blocks; no product logos, readable extensions, or brand icons.",
        "view_mode": "structure_map",
    },
    "F-101": {
        "visual_subject": "An icon file workflow: small app icon tiles become multi-size image slots and platform-ready icon cards.",
        "supporting_subjects": "A designer prepares generic icon assets; no OS logos, app logos, readable extension text, or product UI.",
        "view_mode": "operation_flow",
    },
    "F-102": {
        "visual_subject": "A video file workflow: frame strip, audio track, compression block, and playback device panels connect left to right.",
        "supporting_subjects": "A creator prepares a generic video asset; no media player logos, readable extension text, product UI, or brand icons.",
        "view_mode": "operation_flow",
    },
    "F-103": {
        "visual_subject": "An audio file workflow: waveform card, compression block, music-note icon, and playback device panel connect in sequence.",
        "supporting_subjects": "A creator prepares a generic audio asset; no platform logos, readable extension text, product UI, or brand icons.",
        "view_mode": "operation_flow",
    },
    "F-104": {
        "visual_subject": "A web image format workflow: source image card feeds compression, transparency/quality controls, and browser preview panels.",
        "supporting_subjects": "A designer chooses a lightweight image output; no browser logos, readable extension text, product UI, or brand icons.",
        "view_mode": "operation_flow",
    },
    "F-110": {
        "visual_subject": "A web quality audit workflow: page load panel feeds performance, accessibility, SEO-like, and best-practice score cards.",
        "supporting_subjects": "A developer reviews generic web quality metrics; no Lighthouse logo, Google/Chrome marks, product UI, readable scores, or red/green colors.",
        "view_mode": "structure_map",
    },
    "F-111": {
        "visual_subject": "An accessibility review workflow: interface panels pass through keyboard, contrast, screen-reader, and semantic-structure check cards.",
        "supporting_subjects": "A developer improves usability for many users; no official logos, product UI, readable text, or red/green colors.",
        "view_mode": "operation_flow",
    },
    "F-120": {
        "visual_subject": "A relational database workflow: table cards, relationships, query block, transaction shield, and application data panel connect together.",
        "supporting_subjects": "A developer models structured data; no PostgreSQL elephant logo, product UI, readable table names, or SQL text.",
        "view_mode": "structure_map",
    },
    "F-121": {
        "visual_subject": "An embedded database workflow: local app file connects to compact database card, query block, cache panel, and device storage.",
        "supporting_subjects": "A developer uses a lightweight local database; no SQLite logo, product UI, readable table names, or SQL text.",
        "view_mode": "operation_flow",
    },
    "F-122": {
        "visual_subject": "An ORM workflow: database schema cards connect to model layer, query builder blocks, generated client, and application code panel.",
        "supporting_subjects": "A developer maps database tables into typed application objects; no Prisma logo, product UI, readable schema, or code text.",
        "view_mode": "operation_flow",
    },
    "F-123": {
        "visual_subject": "An object-relational mapping workflow: database table cards connect to object model blocks, query builder tiles, and an application layer.",
        "supporting_subjects": "A developer translates stored records into application objects; no database logos, product UI, readable schema, SQL text, or code text.",
        "view_mode": "operation_flow",
    },
    "F-130": {
        "visual_subject": "An authorization handoff: user device, app server, consent gate, token card, and resource server connect through secure arrows.",
        "supporting_subjects": "A developer checks how access is delegated without sharing a password; no provider logos, real login UI, readable tokens, or brand colors.",
        "view_mode": "operation_flow",
    },
    "F-140": {
        "visual_subject": "A diagram-as-code workflow: plain text-like blocks feed into flowchart, sequence, and graph diagram panels.",
        "supporting_subjects": "A developer converts structured diagram instructions into visual documentation; no Mermaid logo, product UI, readable code, or animal imagery.",
        "view_mode": "operation_flow",
    },
    "F-141": {
        "visual_subject": "A UML diagram generation workflow: class blocks, sequence lifelines, component boxes, and documentation panels connect from a plain source card.",
        "supporting_subjects": "A developer turns architecture notes into UML-style diagrams; no PlantUML logo, product UI, readable code, or plant imagery.",
        "view_mode": "operation_flow",
    },
    "F-150": {
        "visual_subject": "A permissive license workflow: source package card, simple permission stamp, attribution note block, and reuse destination connect across a legal review lane.",
        "supporting_subjects": "A developer checks what can be reused with minimal restrictions; no institutional marks, readable license text, or legal-brand icons.",
        "view_mode": "structure_map",
    },
    "F-151": {
        "visual_subject": "A license obligations map: open source package card connects to notice, patent-grant, modification, and redistribution condition tiles.",
        "supporting_subjects": "A developer reviews responsibilities before shipping reused code; no Apache feather, foundation marks, readable license text, or legal-brand icons.",
        "view_mode": "structure_map",
    },
    "F-152": {
        "visual_subject": "A copyleft flow: original source package connects to modified source, redistribution package, and share-the-source obligation gate.",
        "supporting_subjects": "A developer checks how derivative distribution affects source release requirements; no GNU, FSF, animal marks, or readable license text.",
        "view_mode": "operation_flow",
    },
    "F-153": {
        "visual_subject": "A creative reuse license map: media asset card connects to attribution, share, remix, commercial-use, and no-derivatives condition tiles.",
        "supporting_subjects": "A creator decides how an image or document can be reused; no Creative Commons icons, readable license abbreviations, or platform UI.",
        "view_mode": "structure_map",
    },
    "F-154": {
        "visual_subject": "An open source collaboration loop: public code package, issue cards, review lane, contribution merge block, and shared release card connect around a community hub.",
        "supporting_subjects": "Developers collaborate on reusable software; no foundation logos, repository product UI, readable issue text, or red/green status colors.",
        "view_mode": "operation_flow",
    },
    "F-160": {
        "visual_subject": "A browser document tree: nested element nodes connect from a page shell to style, event, and script interaction panels.",
        "supporting_subjects": "A developer inspects how page structure is represented as a tree; no browser logos, framework marks, readable HTML, or product UI.",
        "view_mode": "structure_map",
    },
    "F-161": {
        "visual_subject": "A server-side rendering flow: request card goes to server render block, HTML-like page shell, hydration step, and browser display panel.",
        "supporting_subjects": "A developer compares response speed and client activation; no framework logos, browser logos, readable code, or real product UI.",
        "view_mode": "operation_flow",
    },
    "F-162": {
        "visual_subject": "A static site generation flow: content files and template blocks feed a build machine, producing prebuilt page cards served from a generic hosting box.",
        "supporting_subjects": "A developer prepares pages before deployment; no framework logos, host logos, readable code, or real product UI.",
        "view_mode": "operation_flow",
    },
    "F-170": {
        "visual_subject": "A cloud compute workflow: virtual server tiles, scaling lane, network boundary, storage connection, and application workload panel connect in a neutral cloud.",
        "supporting_subjects": "An operator provisions compute capacity; no AWS logo, EC2 icon, product console UI, readable instance names, or cloud-provider colors.",
        "view_mode": "structure_map",
    },
    "F-171": {
        "visual_subject": "An object storage workflow: files become bucket-like storage containers, then connect to backup, web asset, lifecycle, and access-control panels.",
        "supporting_subjects": "An operator organizes durable cloud files; no AWS logo, S3 icon, product console UI, readable bucket names, or cloud-provider colors.",
        "view_mode": "operation_flow",
    },
    "F-172": {
        "visual_subject": "An identity and permissions workflow: users, roles, policy cards, key vault, and protected resource panels connect through approval arrows.",
        "supporting_subjects": "An administrator grants least-privilege access; no AWS logo, IAM icon, product console UI, readable policy text, or cloud-provider colors.",
        "view_mode": "structure_map",
    },
    "F-180": {
        "visual_subject": "A graphics rendering pipeline: geometry data, shader-like processing blocks, texture panels, rasterization stage, and final 3D viewport connect left to right.",
        "supporting_subjects": "A graphics developer traces how shapes become pixels; no OpenGL logo, readable shader code, product UI, or game-brand imagery.",
        "view_mode": "operation_flow",
    },
    "F-181": {
        "visual_subject": "A browser graphics workflow: web page shell connects to graphics API blocks, shader-like stages, GPU tile, and interactive canvas panel.",
        "supporting_subjects": "A web developer renders 3D content inside a browser; no WebGL logo, browser logos, readable code, product UI, or game-brand imagery.",
        "view_mode": "operation_flow",
    },
    "F-190": {
        "visual_subject": "A reusable subroutine flow: main program card calls a shared function block, receives a result, and reuses the same block from multiple paths.",
        "supporting_subjects": "A beginner programmer sees repeated steps extracted into one callable unit; no language logos, readable code, or product UI.",
        "view_mode": "operation_flow",
    },
    "F-200": {
        "visual_subject": "A systems-programming safety map: memory ownership blocks, compiler check gate, performance meter, package build lane, and application binary card connect together.",
        "supporting_subjects": "A developer balances safety and speed; no Rust logo, readable code, package names, product UI, or gear-shaped brand marks.",
        "view_mode": "structure_map",
    },
    "G-1": {
        "visual_subject": "A context window concept map: user intent card, conversation history blocks, retrieved notes, and current model response panel connect into one working memory area.",
        "supporting_subjects": "A person shows how relevant background changes an assistant's answer; no AI-company logos, chat product UI, readable text, or brand icons.",
        "view_mode": "structure_map",
    },
    "G-2": {
        "visual_subject": "A tokenization workflow: a sentence-like blank strip breaks into small colored chunks, then flows into a compact model input meter and output panel.",
        "supporting_subjects": "A learner sees language split into countable pieces; no readable words, no letters, no tokenizer names, no model/provider logos.",
        "view_mode": "operation_flow",
    },
    "G-3": {
        "visual_subject": "A dictation workflow: microphone waveform blocks flow into speech recognition tiles, correction controls, and a blank document panel.",
        "supporting_subjects": "A person speaks into a plain microphone while a laptop turns audio into structured blank text rows; no app UI, no logos, no readable text.",
        "view_mode": "operation_flow",
    },
    "G-4": {
        "visual_subject": "An instruction hierarchy: top-level rule card, developer instruction card, user request card, and assistant response panel stack in priority order.",
        "supporting_subjects": "A developer arranges blank rule cards so an assistant follows the correct constraints; no model/provider logos, no chat UI, no readable text.",
        "view_mode": "structure_map",
    },
    "G-5": {
        "visual_subject": "A context capacity diagram: conversation cards, retrieved notes, and tool results fill a large window meter, with overflow cards waiting outside.",
        "supporting_subjects": "A person manages which blank notes fit into the working context; no model/provider logos, no chat UI, no readable text.",
        "view_mode": "structure_map",
    },
    "G-6": {
        "visual_subject": "A one-shot learning setup: one example card guides an assistant response path, with before and after output panels shown as blank layouts.",
        "supporting_subjects": "A learner gives one demonstration and sees the assistant follow the pattern; no model/provider logos, no readable text, no chat UI.",
        "view_mode": "operation_flow",
    },
    "G-7": {
        "visual_subject": "An instruction-following evaluation: a request card with checklist icons flows to an assistant panel, then to matching constraint tiles.",
        "supporting_subjects": "A reviewer checks whether the output obeys structure, tone, and constraints using abstract ticks and alignment marks; no text or logos.",
        "view_mode": "operation_flow",
    },
    "G-8": {
        "visual_subject": "A deterministic versus nondeterministic comparison: one identical input card splits into a stable repeated output path and a varied output path.",
        "supporting_subjects": "A person compares repeatability and variation with abstract dice-like randomness and lock-like stability symbols; no labels, no words, no logos.",
        "view_mode": "before_after",
    },
    "G-9": {
        "visual_subject": "A reasoning effort control panel: low, medium, and high effort lanes expand from quick answer cards to deeper planning and verification cards.",
        "supporting_subjects": "A user chooses how much invisible work the assistant spends before responding; no model/provider logos, no readable labels, no chat UI.",
        "view_mode": "structure_map",
    },
    "G-10": {
        "visual_subject": "A prompt refinement workflow: rough request card goes through constraint, example, format, and review blocks before becoming a cleaner instruction card.",
        "supporting_subjects": "A prompt writer iterates blank instruction cards and sees clearer output structure; no model/provider logos, no readable prompt text.",
        "view_mode": "operation_flow",
    },
    "G-11": {
        "visual_subject": "A context engineering workflow: goal card, background notes, retrieved facts, tool outputs, and memory cards assemble into one organized context pack.",
        "supporting_subjects": "A developer selects relevant blank materials before sending them to an assistant; no model/provider logos, no readable text, no chat UI.",
        "view_mode": "structure_map",
    },
    "G-12": {
        "visual_subject": "An agent design architecture: planner, memory, tool router, action executor, and feedback loop cards connect around a central assistant core.",
        "supporting_subjects": "A developer designs how an autonomous workflow decides, acts, observes, and revises; no model/provider logos, no readable labels, no product UI.",
        "view_mode": "structure_map",
    },
    "G-13": {
        "visual_subject": "A few-shot learning setup: several example input-output cards establish a pattern, then a new blank input follows the same output path.",
        "supporting_subjects": "A learner provides multiple demonstrations before the assistant generalizes; no model/provider logos, no readable words, no chat UI.",
        "view_mode": "operation_flow",
    },
    "G-14": {
        "visual_subject": "A thinking model workspace: hidden scratch area, planning cards, verification loop, and final answer panel are separated by a privacy boundary.",
        "supporting_subjects": "A user receives a concise result while abstract internal work happens behind a translucent boundary; no model/provider logos, no readable text.",
        "view_mode": "structure_map",
    },
    "G-15": {
        "visual_subject": "A retrieval-augmented generation workflow: user question goes to search index, retrieves document cards, then feeds an assistant answer panel.",
        "supporting_subjects": "A developer connects relevant knowledge to generation; no model/provider logos, no search-engine UI, no readable text.",
        "view_mode": "operation_flow",
    },
    "G-16": {
        "visual_subject": "An embedding workflow: text/image cards transform into numeric vector dots, then cluster by similarity in a coordinate-like space.",
        "supporting_subjects": "A learner sees different content mapped into nearby and distant positions; no model/provider logos, no readable text, no math labels.",
        "view_mode": "operation_flow",
    },
    "G-17": {
        "visual_subject": "A vector database search workflow: query vector enters a similarity index, finds nearest neighbor cards, and returns relevant knowledge tiles.",
        "supporting_subjects": "A developer searches by meaning rather than exact words; no database/product logos, no readable text, no SQL or code.",
        "view_mode": "operation_flow",
    },
    "G-18": {
        "visual_subject": "A reasoning chain diagram: a problem card flows through several intermediate thought-step tiles into a checked final answer panel.",
        "supporting_subjects": "A reviewer sees step-by-step structure without revealing readable reasoning text; no model/provider logos, no chat UI, no words.",
        "view_mode": "operation_flow",
    },
    "G-19": {
        "visual_subject": "A prompt caching workflow: reusable prefix cards are stored in a cache shelf, then combined with fresh request cards for faster response flow.",
        "supporting_subjects": "A developer reuses stable context while changing the latest task; no model/provider logos, no readable text, no product UI.",
        "view_mode": "operation_flow",
    },
    "G-20": {
        "visual_subject": "An agent instruction file workflow: a generic markdown-like file card defines project rules, tool preferences, and task boundaries for an assistant workspace.",
        "supporting_subjects": "A developer edits a blank configuration file beside an abstract assistant panel; no Claude or Anthropic logos, no readable filename or text.",
        "view_mode": "structure_map",
    },
    "G-21": {
        "visual_subject": "A multi-agent instruction file workflow: one generic markdown-like file card coordinates several assistant role cards, tools, and handoff arrows.",
        "supporting_subjects": "A developer sets shared operating rules for multiple abstract agents; no product logos, no readable filename or text, no chat UI.",
        "view_mode": "structure_map",
    },
}


def read_entry(path_value: str) -> str:
    if not path_value.strip():
        return ""
    path = REPO / path_value
    if not path.exists() or path.is_dir():
        return ""
    return path.read_text(encoding="utf-8")


def extract_section(text: str, heading: str) -> str:
    pattern = re.compile(
        rf"^##\s+{re.escape(heading)}\s*$\n(.*?)(?=^##\s+|\Z)",
        flags=re.MULTILINE | re.DOTALL,
    )
    match = pattern.search(text)
    return match.group(1).strip() if match else ""


def extract_bullets(section: str) -> dict[str, str]:
    result: dict[str, str] = {}
    for line in section.splitlines():
        line = line.strip()
        if not line.startswith("- "):
            continue
        body = line[2:]
        if ":" in body:
            key, value = body.split(":", 1)
            result[key.strip()] = value.strip()
    return result


def clean(value: str) -> str:
    value = re.sub(r"\s+", " ", value).strip()
    return value.replace("|", "/")


def remove_readable_text_hints(value: str) -> str:
    value = re.sub(r"「[^」]+」", "blank abstract marks", value)
    value = re.sub(r"『[^』]+』", "blank abstract marks", value)
    value = re.sub(r"(?:blank abstract marks){2,}", "unlabeled workflow stages", value)
    value = re.sub(r"blank abstract marks(?:の)?(?:ロゴ枠|ロゴノード)", "a neutral unlabeled service hub", value)
    value = value.replace("ロゴ枠", "neutral service hub")
    value = value.replace("ロゴノード", "neutral service hub")
    value = value.replace("blank abstract marks", "an unlabeled visual block")
    value = value.replace("v0 のチャット画面", "a generic UI-generation chat panel")
    value = value.replace("v0", "the service concept")
    return clean(value)


def neutralize_entry_name(value: str, title: str) -> str:
    if not title:
        return value
    escaped = re.escape(title)
    value = re.sub(rf"{escaped}\s*(?:アイコン|ロゴ|logo|icon)", "a neutral service symbol", value, flags=re.IGNORECASE)
    value = re.sub(rf"{escaped}\s*(?:画面|コンソール|UI)", "a generic service screen", value, flags=re.IGNORECASE)
    value = re.sub(escaped, "the service concept", value, flags=re.IGNORECASE)
    return clean(value)


def subject_type(row: dict[str, str]) -> str:
    if row.get("subtype") in {"person", "youtuber"}:
        return "person_or_creator"
    return TYPE_BY_CATEGORY.get(row.get("category", ""), "concept")


def brand_mode(row: dict[str, str]) -> str:
    stage = row.get("pipeline_stage", "")
    logo_need = row.get("logo_need", "")
    category = row.get("category", "")
    subtype = row.get("subtype", "")
    if stage == "blocked_brand_asset":
        return "blocked_brand_asset"
    if stage == "overlay_wait":
        return "official_overlay_required"
    if stage in {"overlay_ready", "overlay_audit"}:
        return "official_overlay_ready"
    if logo_need == "required":
        return "official_overlay_required"
    if logo_need in {"avoid", "none", "not_required"}:
        return "none"
    if category in {"service", "model"} or (category == "person_org" and subtype == "company"):
        return "official_overlay_required"
    return "none"


def role_balance(row: dict[str, str]) -> str:
    if row.get("category") == "common":
        return "both_review"
    if row.get("category") == "service":
        return "solo_female_works"
    return "diagram_first"


def composition_family(row: dict[str, str]) -> str:
    category = row.get("category", "")
    subtype = row.get("subtype", "")
    title = row.get("title", "")
    mode = brand_mode(row)
    if category == "common":
        return "concept_map"
    if mode in {"official_overlay_required", "official_overlay_ready", "blocked_brand_asset"}:
        return "brand_clearspace"
    if "assistant" in subtype or category == "service":
        return "process_flow"
    if "Context" in title or category == "concept":
        return "timeline_scale"
    return "process_flow"


def composition_type(row: dict[str, str]) -> str:
    if brand_mode(row) in {"official_overlay_required", "official_overlay_ready", "blocked_brand_asset"}:
        return "logo_clearspace"
    if row.get("category") == "common":
        return "diagram_first"
    return "diagram_first"


def has_before_after(memo: str) -> bool:
    return bool(re.search(r"Before\s*/\s*After|Before\s*／\s*After|対比|ビフォー|アフター", memo, re.IGNORECASE))


def view_mode(row: dict[str, str], memo: str, visual_subject_source: str, mode: str) -> str:
    if has_before_after(memo):
        return "before_after"
    if re.search(r"時系列|順番|流れ|フロー|Step|ステップ|push|deploy|デプロイ", visual_subject_source, re.IGNORECASE):
        return "operation_flow"
    if mode != "none":
        return "logo_clearspace"
    if row.get("category") == "common":
        return "structure_map"
    return "diagram_only"


def character_block(row: dict[str, str], memo: str) -> tuple[str, str, str]:
    if row.get("subtype") == "youtuber":
        return "use", "omit", "use"
    text = f"{row.get('title','')} {memo}"
    robot = "use" if re.search(r"ロボット|AI|assistant|アシスタント", text, re.IGNORECASE) else "omit"
    male = "use" if re.search(r"エンジニア|開発|男性|技術者", text) else "omit"
    female = "use" if re.search(r"人物|読者|担当者|ユーザー|非エンジニア|企画|デザイン", text) else "omit"
    if female == "omit" and male == "omit" and row.get("category") == "common":
        female = "use"
        male = "use"
    return female, male, robot


def temporary_people_block(memo: str) -> tuple[str, str, str, str]:
    text = memo
    multi = bool(re.search(r"複数|チーム|メンバー|全員|グループ|レビュアー|レビュー|ユーザー|担当者|3 人|3人|2 名|2名", text))
    if not multi:
        return "no", "", "", "temporary people are not needed"

    count = "2-4"
    match = re.search(r"([2-6])\s*(?:人|名)", text)
    if match:
        count = match.group(1)
    role = "background_team"
    if re.search(r"レビュアー|レビュー|確認", text):
        role = "reviewers"
    elif re.search(r"ユーザー|利用者|担当者", text):
        role = "users"
    return (
        "yes",
        count,
        role,
        "allowed only when the entry needs coordination; keep them smaller than Character A/B/C and do not turn them into the main cast",
    )


def make_prompt(row: dict[str, str]) -> str:
    override = BATCH_SCENE_OVERRIDES.get(row["entry_id"], {})
    entry_text = read_entry(row["md_path"])
    memo = extract_section(entry_text, "誌面ポンチ絵メモ")
    bullets = extract_bullets(memo)
    main_figure = extract_section(entry_text, "メイン図")
    main_figure_lines = [line.strip() for line in main_figure.splitlines() if line.strip()]
    visual_subject_source = (
        bullets.get("描く内容")
        or bullets.get("中心に置く概念")
        or bullets.get("中央キーワード")
        or (main_figure_lines[0] if main_figure_lines else "")
        or f"{row['title']} concept explained as a simple workflow"
    )
    visual_subject = neutralize_entry_name(remove_readable_text_hints(visual_subject_source), row["title"])
    visual_subject = override.get("visual_subject", visual_subject)
    supporting = clean(
        bullets.get("周辺の要素")
        or bullets.get("登場人物")
        or "generic cards, arrows, simple UI-neutral symbols"
    )
    supporting = neutralize_entry_name(remove_readable_text_hints(supporting), row["title"])
    supporting = override.get("supporting_subjects", supporting)
    avoid = "readable text, fake logos, official icons, brand colors, real product UI, watermarks"
    mode = brand_mode(row)
    logo_subject = "none"
    if mode != "none":
        logo_subject = f"official {row['title']} brand overlay after source review"
    female, male, robot = character_block(row, memo)
    clearspace = "no logo clearspace needed"
    if mode in {"official_overlay_ready", "official_overlay_required", "blocked_brand_asset"}:
        clearspace = f"rightmost 40% of top 25% kept completely blank for official {row['title']} logo"
    temp_allowed, temp_count, temp_role, temp_rule = temporary_people_block(memo)
    comparison_mode = "before_after" if has_before_after(memo) else "not_applicable"
    resolved_view_mode = override.get("view_mode", view_mode(row, memo, visual_subject_source, mode))
    if resolved_view_mode == "before_after":
        comparison_mode = "before_after"

    return f"""# {row['entry_id']} {row['title']} ponchi prompt

## Scene Brief

```yaml
entry_id: {row['entry_id']}
title: {row['title']}
subject_type: {subject_type(row)}
subject_stack:
  entry_subject: {row['title']}
  visual_subject: {visual_subject}
  supporting_subjects: {supporting}
  logo_subject: {logo_subject}
  excluded_subjects: {avoid}
brand_asset:
  mode: {mode}
  asset_name: {row.get('title', '') if mode != 'none' else ''}
  local_path: {row.get('official_asset', '')}
  source_url:
visual_references:
  character_a: assets/ponchi/references/character-a-reader-woman.png
  character_b: assets/ponchi/references/character-b-teacher-man.png
  character_c: assets/ponchi/references/character-c-pet-robot.png
role_balance: {role_balance(row)}
composition_family: {composition_family(row)}
composition_type: {composition_type(row)}
composition_density: balanced
comparison_mode: {comparison_mode}
view_mode: {resolved_view_mode}
characters:
  female: {female}
  male: {male}
  robot: {robot}
temporary_people:
  allowed: {temp_allowed}
  count: {temp_count}
  role: {temp_role}
  rule: {temp_rule}
hands_policy:
  visible_hands_max: 2
  gesture: simple pointing or operating gesture only if needed
canvas:
  ratio: 2:1
  standard_size: 1254x627
  main_subject_scale: main subject occupies more than half of canvas width
  density_gate: bbox coverage should be at least 0.50 unless visually justified
clearspace:
  required: {'yes' if mode != 'none' else 'no'}
  location: {clearspace}
  size_hint: controlled, not an empty half-page
  forbidden_under_clearspace: characters, faces, hands, cards, icons, arrows, dots, connectors, labels, borders, shadows, placeholders
scene_goal: make {row['title']} understandable as a simple book diagram
main_symbols: {visual_subject}
avoid: {avoid}
```

## Generation Prompt

Use case: infographic-diagram
Asset type: VibeCodingDictionary ponchi image
Primary request: Create a 2:1 horizontal technical-book ponchi illustration for {row['entry_id']} {row['title']}.

Subject: The entry subject is {row['title']}, but the visual subject is {visual_subject}. Show {supporting} only as supporting elements.

Composition: Use {composition_family(row)} / {composition_type(row)} with balanced density. The main subject must occupy more than half of the canvas width. Use 2-4 large visual blocks rather than many tiny cards.

Comparison: {comparison_mode}. If before_after, make the before and after states visibly different without relying on readable text.

Characters: female={female}, male={male}, robot={robot}. Use the recurring Character A/B/C visual references whenever those characters appear. Temporary people allowed={temp_allowed}; if used, keep them secondary and smaller than the recurring characters.

Logo and brand rule: {'Keep the upper-right logo clearspace completely blank white, about the rightmost 40% of the top 25% of the image. Do not generate, imitate, redraw, or approximate any company or service logo. Outside that clearspace, keep the main subject large and complete.' if mode != 'none' else 'No official logo is needed. Do not draw, imitate, or hint at any company or service logo, app icon, product UI, brand mark, or brand color scheme.'}

Color palette: strict white/black/gray plus approved blue accents only: #FFFFFF, #F7F9FC, #1A1A1A, #6B7280, #EAF1FB, #D6E6FA, #8DB7E8, #3F7FD1, #123E82.

Style: clean simple editorial line illustration, smooth uniform black lines, flat light gray fills, minimal shading, no hatching, no pencil sketch, no painterly texture.

Avoid: {avoid}. No readable text, no watermark.
"""


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("batch_id")
    parser.add_argument("--ledger", type=Path, default=BATCH_LEDGER)
    parser.add_argument("--out-dir", type=Path, default=None)
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args()

    with args.ledger.open("r", encoding="utf-8-sig", newline="") as handle:
        rows = [row for row in csv.DictReader(handle) if row["batch_id"] == args.batch_id]
    if not rows:
        raise SystemExit(f"batch not found: {args.batch_id}")

    out_dir = args.out_dir or PROMPTS / args.batch_id
    out_dir.mkdir(parents=True, exist_ok=True)
    wrote = 0
    skipped = 0
    for row in rows:
        if row["pipeline_stage"] not in {
            "brief_needed",
            "blocked_brand_asset",
            "overlay_wait",
            "overlay_ready",
            "overlay_audit",
            "prompt_review",
        }:
            continue
        path = out_dir / f"{row['entry_id']}.md"
        if path.exists() and not args.overwrite:
            skipped += 1
            continue
        path.write_text(make_prompt(row), encoding="utf-8")
        wrote += 1
    print(f"wrote={wrote} skipped={skipped} batch={args.batch_id}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
