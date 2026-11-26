# The Heritage Short — My Father's Legacy

An AI-assisted short documentary inspired by a family story rooted in
North Shewa, Ethiopia.

## Project purpose

The film remembers a father's diligence in agriculture, his love and
values in raising his family, and his contribution to community life
through customary mediation and reconciliation.

Narration: Amharic  
Subtitles: English  
Storyboard: 10 shots  
GPU tested: NVIDIA Tesla T4  
Image model: Segmind SSD-1B  
Assembly: Python and FFmpeg

## Repository structure

- `storyboard.json`: Shared production contract.
- `schema/`: Storyboard JSON Schema and validation.
- `pipeline/`: Validation, planning, media and generation stages.
- `outputs/keyframes/`: Generated scene images.
- `outputs/narration/`: Narration outputs.
- `outputs/music/`: Original synthetic score.
- `outputs/final/`: Final vertical and horizontal exports.
- `subtitles/`: English subtitle file.
- `runs.jsonl`: Model-call records.
- `DESIGN.md`: Audience, intent, shot rationale and user tests.
- `ARCHITECTURE.md`: Pipeline design and contracts.
- `EXPERIMENTS.md`: Hypothesis, change and result log.
- `FAILURES.md`: Troubleshooting evidence.
- `COSTS.md`: Measured resource use and costs.
- `ETHICS.md`: Consent, licences and AI disclosure.
- `REPORT.md`: Project report.

## Environment

The image-generation workflow was developed in Google Colab on an
NVIDIA Tesla T4 with 14.56 GB reported VRAM.

Image model: `segmind/SSD-1B`  
Image library: Hugging Face Diffusers  
Narration: Edge TTS, Amharic voice `am-ET-MekdesNeural`  
Music: Original programmatically synthesized instrumental score  
Editing: FFmpeg

## Setup

Use a Python environment with the dependencies in `requirements.txt`.
For image generation, use a compatible GPU runtime and install the
model dependencies:

```bash
pip install -r requirements.txt
```

The model weights are downloaded separately and are not stored in Git.

## Validation and planning

The starter CLI commands verified during development are:

```bash
python main.py validate
python main.py plan
```

The media-generation workflow was also executed in Google Colab.
Do not treat the two commands above as a complete end-to-end command:
the complete pipeline command must be verified from a clean clone
before claiming full CLI reproducibility.

## Outputs

The two final exports are:

- `outputs/final/Heritage_Short_9x16.mp4`
- `outputs/final/Heritage_Short_16x9.mp4`

Large media files may be shared separately through public view-only
links. Do not commit credentials, tokens, model weights or private
family material.

## Reproduction status

Before relying on this repository as fully reproducible, verify:
1. JSON Schema validation runs before generation.
2. Every stage has a callable script.
3. Unchanged outputs are reused through caching.
4. Failures and retries are logged.
5. `runs.jsonl` records every model call.
6. One documented command works from a fresh clone.

See `ARCHITECTURE.md` and `REPORT.md`.
