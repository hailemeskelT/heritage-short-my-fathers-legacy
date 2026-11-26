# Experiments and iteration

Each experiment records a hypothesis, change, result and evidence.

## E01 — Storyboard validation
- Hypothesis: A structured storyboard will make production stages consistent.
- Change: Validated the JSON storyboard.
- Result: Validation returned 10 shots and 68 seconds.
- Evidence: `storyboard.json` and validation output.

## E02 — Pipeline planning
- Hypothesis: A generated production plan will expose missing stages.
- Change: Ran the planning command.
- Result: `outputs/pipeline_plan.json` was created.
- Evidence: Pipeline plan file.

## E03 — Placeholder visual inspection
- Hypothesis: Existing keyframes may already represent the family story.
- Change: Inspected all ten generated starter images.
- Result: The images were geometric placeholder story cards, not documentary scenes.
- Evidence: Initial contact sheet.

## E04 — Existing export inspection
- Hypothesis: The existing MP4 files may be suitable for final delivery.
- Change: Inspected stream metadata and sample frames.
- Result: H.264/AAC exports were 68 seconds, but their visual content contained placeholders.
- Evidence: FFprobe output and visual review.

## E05 — Pipeline source inspection
- Hypothesis: The starter image-generation function creates prompt-based scenes.
- Change: Inspected `pipeline/generate_local_assets.py`.
- Result: Keyframes were drawn with Pillow geometric shapes and text.
- Evidence: Source code inspection.

## E06 — Paid image API route
- Hypothesis: A hosted image API could generate the first cinematic keyframe.
- Change: Tried the Gemini image API route.
- Result: The image endpoint required paid billing; it was not used for the final images.
- Evidence: API error and billing prompt.

## E07 — Open image model on T4
- Hypothesis: SSD-1B could generate test images on a Tesla T4.
- Change: Loaded `segmind/SSD-1B` with Diffusers and CPU offloading.
- Result: Model loaded successfully on the T4.
- Evidence: Colab model-loading output.

## E08 — VAE optimization API
- Hypothesis: Pipeline-level VAE optimization methods were supported.
- Change: Tried `pipe.enable_vae_slicing()`, then used `pipe.vae.enable_slicing()` and `pipe.vae.enable_tiling()`.
- Result: VAE optimization methods were enabled through the VAE object.
- Evidence: AttributeError and successful follow-up output.

## E09 — Prompt length
- Hypothesis: A detailed long prompt would improve scene fidelity.
- Change: Used a 231-token prompt.
- Result: CLIP truncated the prompt at its 77-token limit. Shorter prompts were adopted.
- Evidence: Transformers warning.

## E10 — First image generation
- Hypothesis: SSD-1B could produce a 1024x1024 test keyframe within T4 memory.
- Change: Generated Shot 04 using 30 steps, guidance 9.0 and seed 404.
- Result: JPEG saved successfully in approximately 27 seconds; peak allocated GPU memory reported as 3.32 GB.
- Evidence: `outputs/keyframes_test/shot_04_test.jpg` and Colab output.

Add any further experiments actually performed after E10. Preserve prompt versions,
seeds, output paths and timing evidence where available.
