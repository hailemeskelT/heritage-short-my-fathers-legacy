# Failure and recovery log

## 1. Paid image-generation API
- Problem: Gemini image generation required paid billing.
- Response: Switched to local open-weight SSD-1B inference.
- Outcome: First test image generated on a Tesla T4.

## 2. Image MIME type
- Problem: PNG response format was rejected by the selected image endpoint.
- Response: JPEG was used for the local test output.
- Outcome: Local SSD-1B output saved as JPEG.

## 3. VAE method AttributeError
- Problem: `StableDiffusionXLPipeline` did not expose `enable_vae_slicing()`.
- Response: Used `pipe.vae.enable_slicing()` and `pipe.vae.enable_tiling()`.
- Outcome: Both optimizations enabled.

## 4. Notebook NameError
- Problem: `storyboard` was not defined after the notebook state changed.
- Response: Reloaded `storyboard.json` into Python.

## 5. Google Drive path error
- Problem: The project was not found in the expected Drive folder after changing accounts.
- Response: Uploaded the ZIP to the new account and extracted it.
- Outcome: Storyboard restored; generated media had to be recreated because it was absent.

## 6. CLIP prompt truncation
- Problem: A 231-token prompt exceeded the CLIP tokenizer limit of 77.
- Response: Replaced verbose prompts with shorter scene-specific prompts.
- Outcome: Reduced prompt truncation risk.

Record any further actual failures and their evidence here.
