# Architecture and implementation status

## Contract
storyboard.json is the central production specification. It contains project metadata, audience/intent, ten shots, Amharic narration, English subtitles, visual/motion prompts, durations, seeds/status fields, and the AI disclosure text. schema/storyboard.schema.json uses JSON Schema Draft 2020-12. pipeline/validate.py checks the schema and verifies a 60–90-second total matching the target duration.

## Implemented stages
1. Validation: main.py validate calls pipeline/validate.py.
2. Planning: main.py plan calls pipeline/plan.py and writes outputs/pipeline_plan.json.
3. Assembly: main.py assemble calls pipeline/assemble.py.

## Actual CLI behaviour
main.py run validates, creates a plan, and calls the still-image assembler only. It does not invoke image, motion, narration, or music generation. The assembler requires ten PNG keyframes, outputs/narration/narration.wav, outputs/music/score.wav, and subtitles/narration.en.srt. The WAV source files are absent from the audited Git tree.

## Assembly
The assembler uses FFmpeg to concatenate still images, burn in English subtitles, sidechain-compress the music using narration as the key signal, mix/normalize audio, and export 1080x1920 vertical and 1920x1080 horizontal H.264/AAC files at 24 fps. It explicitly describes the result as a Ken-Burns-free still-image sequence. No moving-shot clips or generation stage are present in outputs/shots/.

## Cache and logging
pipeline/cache.py provides file hashes, stable JSON hashes, and a stage-cache-key helper. The CLI does not integrate these helpers into stage execution, so automatic per-shot cache reuse/invalidation is not demonstrated. pipeline/logger.py can write structured event records, but runs.jsonl currently has one SSD-1B keyframe-test row and does not represent all production model calls.

## Reproducibility conclusion
Validation, planning, hashing helpers, logging utilities, and still-image assembly exist. The repository does not yet demonstrate a clean-clone, one-command end-to-end AI production pipeline. Add callable generation adapters, pinned model/dependency versions, source-audio provisioning, stage cache integration, bounded retries, and complete run logging before claiming full reproducibility.