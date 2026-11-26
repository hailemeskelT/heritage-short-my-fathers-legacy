# Failure and recovery log

The following six incidents were documented by the project owner.

1. **Hosted image API required billing.** Gemini image endpoint required paid billing; the workflow switched to open-weight SSD-1B on Colab. Original billing response is not retained.
2. **Image format/MIME issue.** PNG response format was rejected by the selected endpoint; JPEG was used for the local test. The test JPEG is present.
3. **Diffusers VAE AttributeError.** The pipeline did not expose enable_vae_slicing(); the workflow used pipe.vae.enable_slicing() and pipe.vae.enable_tiling(). Runtime output is not retained.
4. **Notebook NameError.** storyboard was undefined after a notebook state change; storyboard.json was reloaded. Narrative record only.
5. **Google Drive account/path migration.** Project ZIP was uploaded and extracted in a second account; missing generated media was recreated according to the project notes. Narrative record only.
6. **CLIP prompt truncation.** A 231-token prompt exceeded the 77-token limit; prompts were shortened. Raw warning/prompt comparison is not retained.

## Current engineering risks
- main.py run plans and assembles only; it does not generate AI assets.
- Required narration and score WAV files are not in the Git tree.
- No moving-shot generation stage or clips are tracked.
- Cache helpers are not integrated into stage execution.
- runs.jsonl has one test record, not all model calls.
- No bounded generation retry framework is present.
- Storyboard statuses still mark generation/native-speaker review as pending although ten keyframe files exist.
- Narration/SRT timing ends at 54.996 seconds versus the 68-second storyboard target.

These code and evidence gaps do not imply that no work was done outside the repository. They indicate what the current public source snapshot does not prove.