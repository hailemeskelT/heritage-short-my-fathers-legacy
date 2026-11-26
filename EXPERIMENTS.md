# Experiments and iteration

Ten experiments are documented. The evidence status is noted because not every historic run log or comparison is retained in the current repository.

| ID | Test | Recorded result | Evidence status |
|---|---|---|---|
| E01 | Storyboard validation | Ten shots; 68-second target accepted. | Validator/schema present; prior successful command output reported by owner. |
| E02 | Pipeline planning | Plan file reportedly created. | Planner source present; generated plan not tracked. |
| E03 | Initial keyframe inspection | Earlier starter images described as geometric placeholders. | Contact sheet present; original pre-revision set not clearly versioned. |
| E04 | Earlier export inspection | Earlier prototypes described as 68-second H.264/AAC with placeholder visuals. | Earlier FFprobe report not retained; current final MP4 objects now present. |
| E05 | Starter generator source inspection | Earlier local generator described as Pillow geometric cards. | Cited generator source is not present in current tree. |
| E06 | Gemini image API route | Billing was required; route not used for final images. | Narrative record; original API response absent. |
| E07 | SSD-1B on T4 | Model reportedly loaded with Diffusers and CPU offloading. | T4 environment documented; full loading log absent. |
| E08 | VAE API | Pipeline-level method failed; VAE object methods used successfully. | Error/workaround described; runtime log absent. |
| E09 | Prompt length | 231-token prompt exceeded CLIP's 77-token context; shorter prompts adopted. | Narrative warning record; raw output not retained. |
| E10 | First SSD-1B test image | 1024x1024, 30 steps, guidance 9.0, seed 404; ~27 seconds; 3.32 GB peak allocation. | Test JPEG and one runs.jsonl entry present. |

Ten final keyframe PNG files are now present, but runs.jsonl contains only one model-call record. It does not identify the prompt, seed, latency, and cost for every final image. No additional experiments or frontier-model comparisons are added without retained evidence.