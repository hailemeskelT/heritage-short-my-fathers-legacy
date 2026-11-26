# ARCHITECTURE.md

## Overview
The system is a storyboard-driven, multi-stage content-generation pipeline. `storyboard.json` is the shared contract. Each stage reads only the fields it needs and writes explicit, inspectable outputs.

## Stage boundaries

1. **Script/story:** establish the real story, narration, shot descriptions, and cues.
2. **Keyframes:** generate still images from visual prompts and character/style references.
3. **Moving shots:** animate approved keyframes using image-to-video; use a controlled still-animation fallback where needed.
4. **Music:** generate and select an original instrumental score.
5. **Narration:** synthesize Amharic narration and validate pronunciation/timing.
6. **Assembly:** synchronize picture, narration, score, subtitles, end card, and aspect ratios with FFmpeg.

## Contract and validation

`schema/storyboard.schema.json` validates the shape and required fields. `pipeline/validate.py` also checks that shot durations total 60–90 seconds. Validation runs before planning or assembly.

## Caching

`pipeline/cache.py` calculates a deterministic SHA-256 input hash. Include the stage's prompt, model identifier/revision, parameters, seed, reference-image hashes, and relevant upstream asset hashes in each stage's cache key. If a key is unchanged, reuse the previous output. If a key changes, regenerate only that stage and downstream dependants.

## Failure handling

Use bounded retries for transient errors, preserve completed outputs, record failures, and select documented fallbacks. Do not repeat non-retryable authentication/invalid-request errors. A still keyframe with a Ken Burns pan/zoom is an acceptable fallback when video inference is unavailable.

## Secrets and privacy

Load API credentials from environment variables or secret stores. Never commit `.env`. Record consent and provider data-use/licence decisions in `ETHICS.md`.

## Reproducibility

Record actual model, revision, parameters, seed, latency, cost estimate, status, and output path in `runs.jsonl`. The README documents the end-to-end command. Test from a clean clone and a clean environment; no hidden notebook state should be required.

## Current starter-kit limitations

The repository supplies validation, stage planning, logging/cache primitives, and still-image FFmpeg assembly. Provider-specific image, video, TTS, and music adapters must be implemented and tested against the current official provider interfaces. Colab guide is operational guidance, not a preconfigured GPU notebook. Do not describe this starter kit alone as a completed AI-generation pipeline.
