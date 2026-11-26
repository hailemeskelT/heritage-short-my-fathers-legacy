# AI-Content Generation — The Heritage Short
## Final Project Report: የአባቴ ውርስ — My Father's Legacy

**Participant:** Add the name used in the challenge portal.  
**Repository:** https://github.com/hailemeskelT/heritage-short-my-fathers-legacy  
**Audit basis:** main commit `2c4a5250c7bb43224c4aa91e209be1296e27920b`, reviewed 27 November 2026.  
**Creative target:** ten shots, 68 seconds, Amharic narration, English subtitles.

> **Evidence note:** This report is based on the connected GitHub repository, including its recursive file tree, source files, storyboard, schema, project documentation, timing metadata, subtitles and file inventory. The GitHub text interface confirmed that two MP4 file objects exist, but did not decode or play them. The filmmaker reports that both audience tests were completed; detailed participant notes are not present in the repository. Unverified facts are not invented.

## 1. Executive summary

*My Father's Legacy* is an AI-assisted short film based on a family account rooted in North Shewa, Ethiopia. It remembers a father known for diligence in farming, love and good values in raising his family, and service to the community through customary mediation (*shimgilna*) and reconciliation. The film's central message is that values and family memory continue across generations: “Our story is our identity.”

The repository contains a ten-shot storyboard with a 68-second target, ten keyframe PNG files, an English subtitle file, narration timing metadata, titlecard images and two final MP4 file objects: vertical 9:16 and horizontal 16:9. The documented production workflow uses Segmind SSD-1B through Diffusers on a Colab Tesla T4, Edge TTS for Amharic narration, a programmatically synthesized instrumental score, and FFmpeg for assembly.

The codebase is useful but partial. Storyboard validation and planning are implemented; the assembler concatenates still images, burns subtitles, mixes narration and sidechain-compressed music, and exports two aspect ratios. However, `main.py run` does not generate AI assets. It validates, plans and invokes the still-image assembler. Source WAV files are not committed, the moving-shot directory is empty, cache helpers are not integrated into stage execution, and only one model-call record appears in `runs.jsonl`. A clean-clone end-to-end rebuild is therefore not established by the current repository.

## 2. Purpose, audience and intended response

The project aims to preserve a meaningful family story in a short audiovisual format while demonstrating an AI-assisted creative workflow. The primary audience is the filmmaker's family. Secondary audiences are Ethiopian young people and viewers interested in family heritage and community values.

The intended response is appreciation of family memory, parental example, diligence, patience, respect and reconciliation. The creative tone is warm, reflective, respectful and culturally grounded.

## 3. Story and creative design

The supplied family account describes a family rooted in North Shewa; a father who was a diligent farmer; a parent who raised the family with love and good values; and a respected community member who participated in customary mediation and reconciliation. The source account does not identify an exact village, date, crop, dispute, quotation or named historical event. Accordingly, AI visuals are illustrative reconstructions and should not be presented as archival or documentary photographs.

The ten shots move from the preservation of family stories and the North Shewa setting, to the father's work, family values, community service and reconciliation, and finally the continuation of his lessons across generations. The father is intended to be a fictional, non-identifiable figure. The synthetic narrator is not represented as the father's real voice.

## 4. Technical workflow and implementation

### 4.1 Storyboard and validation

`storyboard.json` is the central production specification. It includes project metadata, audience and intent, ten shot descriptions, Amharic narration, English subtitles, visual and motion prompts, durations, seeds/status metadata and an AI-disclosure string. `schema/storyboard.schema.json` uses JSON Schema Draft 2020-12. `pipeline/validate.py` validates the schema and checks that the duration total is within 60–90 seconds and matches the storyboard target. The project owner previously reported: `VALID: storyboard.json; 10 shots; 68.0 seconds.`

### 4.2 Keyframe generation

The current Git tree contains ten files, `outputs/keyframes/shot_01.png` through `shot_10.png`, plus a Shot 04 test JPEG. Project notes identify Segmind SSD-1B through Hugging Face Diffusers on a Google Colab NVIDIA Tesla T4 with 14.56 GB reported VRAM. The only detailed model-call row records a 1024×1024 test image, 30 steps, guidance 9.0, seed 404, approximately 27 seconds, and 3.32 GB peak allocated GPU memory.

The ten final keyframe files are present, but `runs.jsonl` does not record an individual model call for each final image. Their exact prompts, model revision, seeds, generation times and per-image costs therefore cannot be reconstructed from the current log. The notebook files in the repository are setup skeletons, not an executable ten-image generation stage.

### 4.3 Narration and subtitles

The repository documents Edge TTS using the Amharic voice `am-ET-MekdesNeural`. `outputs/audio_timing.json` records a narration duration of 54,996 ms (54.996 seconds). The ten English subtitle cues in `subtitles/narration.en.srt` also end at 54.996 seconds. The source WAV is not present in the Git tree, so pronunciation and actual audio cannot be independently auditioned from the repository.

This creates a material timing discrepancy: the storyboard targets 68.000 seconds, while the narration/subtitle timeline ends at 54.996 seconds, a difference of 13.004 seconds. The per-shot audio timing also does not follow the storyboard shot durations exactly. The final edits should be checked against the actual video timeline, and the SRT, narration and storyboard should be reconciled before claiming synchronization.

### 4.4 Music and assembly

The project describes an original programmatically synthesized instrumental score. `pipeline/assemble.py` expects `outputs/narration/narration.wav`, `outputs/music/score.wav` and the English SRT, alongside all ten keyframes. It uses FFmpeg to concatenate still images, apply subtitle burn-in, sidechain-compress music using narration as the control signal, mix the audio and loudness-normalize the output. The score WAV is not present in the audited Git tree; thus the final score and ducking cannot be measured from source files in this repository.

The assembler explicitly describes its output as a still-image sequence without Ken Burns movement. `outputs/shots/` contains only a placeholder file; no moving-shot clips or motion generation stage are present in the tracked source.

### 4.5 Final video files

The Git tree contains:
- `outputs/final/Heritage_Short_9x16.mp4` — 4,834,885 bytes.
- `outputs/final/Heritage_Short_16x9.mp4` — 5,354,795 bytes.
- Vertical and horizontal titlecard PNG files.
- Ten keyframe PNGs, the English SRT and audio timing JSON.

The MP4 objects are confirmed to exist by their repository paths and byte sizes, but their binary streams and final frames were not decoded in this audit. Actual dimensions, duration, codecs, soundtrack, subtitle readability, music ducking and visible AI end card therefore remain to be verified by playback and FFprobe.

## 5. Software engineering and reproducibility

Implemented components include:
- JSON Schema validation and duration checks.
- Planning output that lists expected keyframe and shot paths.
- FFmpeg still-image assembly, subtitle burn-in, audio mixing and two aspect ratios.
- SHA-256 and stable JSON hashing helpers.
- A structured JSONL event logger.
- Missing-file and FFmpeg error reporting during assembly.

Limitations found in the tracked implementation:
- `main.py run` validates, plans and assembles stills; it does not invoke image, motion, narration or music generation.
- `pipeline/cache.py` provides hash functions, but no integrated stage runner uses them to invalidate or reuse outputs.
- `runs.jsonl` contains one SSD-1B test row, not a record for every model call.
- No bounded retry mechanism is implemented in the tracked production path.
- `requirements.txt` lists only `jsonschema` and `python-dotenv`; FFmpeg and generation dependencies/model revisions are not fully pinned.
- Required narration and music WAVs are not in the repository, so assembly cannot run from a clean clone without restoring these assets.
- The full one-command clean-clone production workflow is not demonstrated.

The repository should therefore be described as a storyboard-driven validation, planning and still-assembly scaffold with externally executed generation steps, not as a complete reproducible AI generation pipeline.

## 6. Experiments and troubleshooting

`EXPERIMENTS.md` documents ten experiments: storyboard validation, pipeline planning, inspection of earlier placeholder frames and exports, source inspection, a paid image API route, SSD-1B loading on a T4, VAE configuration, CLIP prompt truncation, and first image generation. The strongest retained quantitative experiment is the Shot 04 SSD-1B test, supported by its JPEG output and one log entry.

Several other experiment results are narrative records without raw output, before/after assets or reproducible logs. For example, a source file cited in the earlier generator inspection is not present in the current tree, and the historic FFprobe output cited in the earlier export inspection is not retained. These results are retained as project notes, not represented as independently reproduced tests.

The documented problems include hosted image API billing, image-format handling, a Diffusers VAE method mismatch, notebook state loss, Google Drive account/path migration and CLIP prompt truncation. Shortening a 231-token prompt addressed the documented 77-token CLIP context limit. Loading SSD-1B on the T4 provided a workable local test route under the available resource constraints.

## 7. Audience testing and design iteration

The filmmaker reports that both required audience activities were completed: the radio-cut test and the near-final film test. The radio cut was defined as narration plus placeholder music on a black screen. However, the current public repository's `DESIGN.md` contained placeholders for the dates, participant counts, anonymised feedback and resulting design changes. This report does not invent participants, quotations or observations.

For a complete assessment record, add the actual date and at least three anonymous participant summaries for each round, the feedback received, what was unclear or effective, and the specific narration, storyboard, subtitle or editing changes made. Keep participant names and contact information private. The owner's statement that testing was completed should be distinguished from the missing written evidence.

## 8. Costs and measurements

The retained measurements are limited to one SSD-1B test: approximately 27 seconds and 3.32 GB peak allocated GPU memory on a Tesla T4. The narration timing JSON records 54.996 seconds of speech. The current repository does not provide total model-loading time, total time/GPU minutes for the ten final keyframes, TTS generation time, music-generation time, either FFmpeg export time, or a complete list-price-equivalent project cost.

The USD 0.00 field in the test log refers only to direct API cost for that local SSD-1B test; it is not the total project cost. This report does not extrapolate the one test latency to ten images or estimate missing costs as measured values.

## 9. Ethics, consent and AI disclosure

The project documents state that the father is represented by a fictional, non-identifiable AI figure and that the narrator is synthetic rather than a cloned or imitated version of the father's voice. No identifiable face or replicated real voice should be used without informed consent.

The public repository does not contain a family permission record or the scope of permission for publication. Retain consent evidence privately and record whether it covers telling the story, public distribution and identifying details. Do not publish private signatures or contact information.

The project notes identify SSD-1B as Apache 2.0, but the exact model revision is not pinned. Diffusers package version, Edge TTS applicable service terms and FFmpeg build/licensing details also need versioned records. The storyboard contains the disclosure text “This film was made with AI”; the ethics note says the end card states “MADE WITH AI.” Since the final MP4 frames were not inspected, verify the visible end card in both exports and enable the publishing platform's AI disclosure label or retain the required screenshot.

## 10. Practices tested and lessons learned

**A practice that helped:** Maintaining `storyboard.json` as the central production contract made the ten scenes, narration, subtitles, prompts, durations and audience intent reviewable in one structured file. Schema validation also provided a quick way to catch invalid structure and duration mismatches.

**A practice that did not work as expected:** Longer image prompts were not necessarily better. The documented 231-token prompt exceeded the 77-token CLIP context and was truncated. The response was to shorten prompts and prioritize the most important scene details.

**Hardest problem:** Building a usable workflow under limited paid-service and GPU resources while dealing with model-library differences, notebook state and Drive storage migration. Switching from a paid hosted image endpoint to SSD-1B on a Colab T4 produced a successful test image. The remaining challenge is to preserve and document all generation stages, input audio and model-call evidence in a reproducible form.

## 11. Extension work and next steps

The project explored an open-weight image model after the paid hosted endpoint proved unsuitable, and documented prompt-token and GPU-memory constraints. No paid frontier-model benchmark, comparative audience preference study or additional-language benchmark is claimed because those results are not retained in the repository.

Recommended next steps:
1. Package image, motion, narration and music generation as callable, restartable stages with pinned dependencies and model revisions.
2. Integrate per-stage hash caching, bounded retries and one complete log record per model call.
3. Restore and document the source WAV assets in a controlled way; do not expose private or unlicensed material.
4. Reconcile the 68.000-second storyboard against the 54.996-second narration/subtitle timeline, then re-export and inspect both MP4s.
5. Add motion generation if moving shots are required; otherwise accurately label the delivered visual method as still-image assembly.
6. Add anonymised findings and changes from both audience tests to `DESIGN.md`.
7. Complete family-permission scope, model/service terms and AI disclosure evidence.
8. Test the documented commands from a clean clone with all required inputs present.

## 12. Evidence status summary

| Area | Evidence in repository | Status from this audit |
|---|---|---|
| Public source repository | Public GitHub repository | Available |
| Storyboard/schema | Ten-shot JSON and validator | Available; shot statuses need updating after native review/generation confirmation |
| Keyframes | Ten PNG files | Present; per-image logs incomplete |
| Vertical/horizontal videos | Two MP4 file objects | Present; streams not decoded |
| Narration/subtitles | Timing JSON and SRT | Present; WAV absent; timeline mismatch requires resolution |
| Original music/ducking | Documented method and sidechain-compression filter | WAV absent; final mix not verified |
| Moving shots | No clips or generation code in tracked outputs | Not demonstrated |
| Ten experiments | Ten written entries | Documented; evidence strength varies |
| Run log | One SSD-1B test record | Incomplete for all model calls |
| Cost | One test timing/memory record | Stage totals unavailable |
| Audience tests | Owner reports both completed | Detailed notes not in repository |
| Consent/licences | Ethics notes with pending confirmations | Publication permission and service/version records need completion |
| Clean-clone run | CLI plans and assembles; WAVs absent | End-to-end generation not demonstrated |
| Walkthrough/public post | Script/template only | Final walkthrough and post evidence not located |

## 13. Conclusion

The project has a defined family story, a structured ten-shot storyboard, ten committed keyframe images, two committed final MP4 file objects, English subtitle and timing assets, and a documented SSD-1B test on a Colab T4. Its creative message emphasizes family memory, diligence, respect and reconciliation.

The repository audit also establishes that the tracked code is a partial production scaffold, not a fully reproducible end-to-end AI pipeline. The revised documentation distinguishes generated assets that are present from stages and evidence that are not present or not verified. The project should be submitted with these distinctions made clear, and with the timing, consent and final-video checks completed.

## Appendix — Repository and final output links

- Repository: https://github.com/hailemeskelT/heritage-short-my-fathers-legacy
- Vertical MP4: https://github.com/hailemeskelT/heritage-short-my-fathers-legacy/blob/main/outputs/final/Heritage_Short_9x16.mp4
- Horizontal MP4: https://github.com/hailemeskelT/heritage-short-my-fathers-legacy/blob/main/outputs/final/Heritage_Short_16x9.mp4
- Storyboard: https://github.com/hailemeskelT/heritage-short-my-fathers-legacy/blob/main/storyboard.json
- English subtitles: https://github.com/hailemeskelT/heritage-short-my-fathers-legacy/blob/main/subtitles/narration.en.srt

**Submission timing:** The repository's original checklist states 26 November 2026, 23:59 EAT. This revision is dated 27 November 2026. Confirm that the submission portal still accepts entries.