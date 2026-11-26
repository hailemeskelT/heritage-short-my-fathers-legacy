# Repository Audit — 27 November 2026

## Snapshot and scope
- Repository: `hailemeskelT/heritage-short-my-fathers-legacy`
- Audited branch: `main`
- Head commit: `2c4a5250c7bb43224c4aa91e209be1296e27920b` — “Add final vertical and horizontal film exports”.
- Scope: recursive Git tree, source code, storyboard/schema, README, architecture, design/experiment/failure/cost/ethics documentation, run log, timing JSON, subtitles, requirements and asset paths.
- Limitation: binary MP4/PNG files were confirmed by Git tree metadata and byte sizes but were not decoded or played.

## Asset inventory
| Asset | Finding |
|---|---|
| Ten keyframes | `outputs/keyframes/shot_01.png` … `shot_10.png` present. |
| Test keyframe | `outputs/keyframes_test/shot_04_test.jpg` present, 316,729 bytes. |
| Vertical MP4 | Present, 4,834,885 bytes. |
| Horizontal MP4 | Present, 5,354,795 bytes. |
| Titlecards | Both orientation PNG files present. |
| Review image | Keyframe contact sheet present. |
| Narration timing/SRT | Present; end at 54.996 seconds. |
| Narration WAV | Not present; only .gitkeep in folder. |
| Music WAV | Not present; only .gitkeep in folder. |
| Motion clips | Not present; only .gitkeep in outputs/shots. |
| Run log | Exactly one SSD-1B test row. |

## Source implementation
1. `main.py run` calls validation, planning and still-image assembly only; it does not call image, motion, narration or music generation.
2. `pipeline/assemble.py` requires ten keyframes, narration WAV, score WAV and SRT. It concatenates stills, burns subtitles, sidechain-compresses the music under narration, mixes and encodes two aspect ratios.
3. The assembler explicitly describes the sequence as a still-image sequence without Ken Burns movement.
4. `pipeline/cache.py` has hash helpers, but stage-level cache reuse/invalidation is not integrated into CLI execution.
5. `pipeline/logger.py` supports structured records, but the current `runs.jsonl` contains one SSD-1B test record rather than all model calls.
6. `requirements.txt` includes only jsonschema and python-dotenv; FFmpeg and generation dependencies/model revisions are not fully captured.
7. Storyboard shots remain marked pending native-speaker review and asset generation despite ten keyframes being in the tree.
8. Storyboard target is 68.000 seconds; narration timing and final SRT cue end at 54.996 seconds, a 13.004-second difference.
9. Two final MP4 file objects exist, but codec, dimensions, runtime, audio, subtitle readability and AI end-card presence are not independently verified in this audit.
10. Detailed dates, participant counts, feedback and design changes from both audience tests are not contained in the public repository.
11. The repository does not contain a family permission record/scope for public release, nor complete pinned licence/service-version records.

## Conclusion
The current repository contains more completed media assets than the earlier inspection indicated: ten final keyframe files and both MP4 file objects are present. The source code and evidence still show a partial pipeline and several final verification/documentation gaps. The revised report records both the confirmed progress and these limitations.