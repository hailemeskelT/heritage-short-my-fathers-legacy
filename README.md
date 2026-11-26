# The Heritage Short — My Father's Legacy

An AI-assisted short film based on a family account rooted in North Shewa, Ethiopia.

**Narration:** Amharic | **Subtitles:** English | **Storyboard:** 10 shots, 68-second target, 24 fps metadata

## Project outputs in this repository
- Ten keyframe PNG files: outputs/keyframes/shot_01.png through shot_10.png.
- Vertical MP4 file: outputs/final/Heritage_Short_9x16.mp4 (4,834,885 bytes).
- Horizontal MP4 file: outputs/final/Heritage_Short_16x9.mp4 (5,354,795 bytes).
- Titlecard images, contact sheet, English SRT, and outputs/audio_timing.json.
- Source code, storyboard schema, run log, and project documentation.

The MP4 file objects are present, but their streams and final frames were not decoded during the repository audit. The tracked narration and music folders contain only .gitkeep files; the WAV inputs required by the assembler are not in Git. outputs/shots/ also contains only .gitkeep; no moving-shot clips are tracked.

## Environment
Project notes document Segmind SSD-1B through Diffusers on Google Colab with an NVIDIA Tesla T4 (14.56 GB reported VRAM), Edge TTS voice am-ET-MekdesNeural, a programmatically synthesized score, and FFmpeg assembly. One SSD-1B test is logged: 1024x1024, 30 steps, guidance 9.0, seed 404, about 27 seconds, and 3.32 GB peak allocated GPU memory.

## Setup and commands
Install the requirements in requirements.txt and install FFmpeg separately. The file currently lists only jsonschema and python-dotenv; model-generation dependencies are not fully pinned.

Commands: python main.py validate; python main.py plan; python main.py assemble; python main.py run.

Important: run only validates, creates a plan, and assembles stills. It does not generate keyframes, motion clips, narration, or music. Assembly requires ten keyframes, narration.wav, score.wav, and the SRT. A clean clone therefore cannot rebuild the final film from the tracked assets alone.

## Engineering status
The cache module contains hashing helpers, but stage-level cache invalidation is not wired into the CLI. The run log has one SSD-1B test record, not a complete record for every model call. The current assembler concatenates stills, burns subtitles, uses sidechain compression for music ducking, and produces two aspect ratios; it does not make moving video clips.

The narration timing file and SRT end at 54.996 seconds, while the storyboard target is 68 seconds. Confirm this timing against both final exports. See FINAL_SUBMISSION_AUDIT.md and REPORT.md for the full evidence-based review.