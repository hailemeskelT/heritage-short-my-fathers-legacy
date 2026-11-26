# Architecture

## 1. Design

`storyboard.json` is the central production contract. It holds the
project information and ten shot descriptions, durations, narration,
English subtitles, image prompts and motion prompts.

## 2. Production stages

1. Story and storyboard — source account, audience, intent and shots.
2. Validation and planning — Python validation and production plan.
3. Keyframes — SSD-1B image generation through Diffusers on a Colab T4.
4. Narration — Amharic speech generation through Edge TTS.
5. Music — original programmatically synthesized instrumental score.
6. Assembly — FFmpeg applies slow camera movement, subtitles, audio mix
   and the AI disclosure end card.
7. Delivery — 9:16 and 16:9 MP4 exports.

## 3. Data contracts

The storyboard JSON is the input shared across stages. The schema is
stored in `schema/storyboard.schema.json`.

## 4. Caching

Document the actual cache key and invalidation behavior implemented
in `pipeline/cache.py` here. Do not claim per-shot cache invalidation
unless a prompt change was tested and only the changed shot regenerated.

## 5. Failure handling

Observed failures and their resolutions are in `FAILURES.md`.
Model calls and resource measurements belong in `runs.jsonl` and
`COSTS.md`.

## 6. Reproducibility limitation

The notebook executed image generation, narration, music and assembly.
The starter CLI's validation and planning commands were tested.
A clean-clone, single-command end-to-end pipeline is a separate
requirement and must not be claimed unless it has actually been tested.
