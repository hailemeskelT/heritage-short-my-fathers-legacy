# Google Colab GPU Workflow

This guide sets up a repeatable GPU workspace. Colab availability and quotas vary; never assume a specific GPU type or session duration.

## 1. Start a runtime

1. Open Google Colab and create a notebook.
2. Select Runtime → Change runtime type → GPU, if available.
3. Run:

```python
!nvidia-smi
import torch
print('CUDA available:', torch.cuda.is_available())
if torch.cuda.is_available():
    print(torch.cuda.get_device_name(0))
```

Record the actual GPU model and runtime constraints in `COSTS.md`.

## 2. Mount persistent storage

```python
from google.colab import drive
drive.mount('/content/drive')
```

Use a project folder under Drive for checkpoints and outputs. Save generated assets after each completed shot/track. Do not depend on the Colab VM disk surviving a reset.

## 3. Load the project

```python
%cd /content
!git clone https://github.com/REPLACE_WITH_YOUR_USERNAME/heritage-short.git
%cd /content/heritage-short
!pip install -r requirements.txt
```

Replace the repository URL with your actual public repository. Keep credentials in Colab Secrets or environment variables, not in notebook cells that will be shared.

## 4. GPU generation stages

Use separate, restartable workflows for:

- Wan 2.2 TI2V-5B image-to-video generation.
- ACE-Step 1.5 instrumental music generation.

Before running, check the official model repository/model card and current inference instructions. Model repositories, dependencies, memory requirements, and notebook examples can change. Select a configuration that fits the actual GPU allocated to your runtime. Generate low-resolution/short drafts first, batch jobs, and save each result immediately.

## 5. Return assets to the project

Save files using the manifest in `ASSET_MANIFEST.md`, for example:

- `outputs/shots/shot_03.mp4`
- `outputs/music/score.wav`

Keep generated outputs and run metadata together so they can be inspected and reproduced.

## 6. Resource-management rules

- Load one large model at a time and unload it before loading the next if GPU memory is limited.
- Do not download model weights again when a persistent Drive copy is already available and permitted by the licence.
- Prefer low-resolution drafts and only render approved material at higher settings.
- Keep a retry limit and fallback plan for each shot.
- Log model, revision, parameters, seed, generation time, GPU model, GPU minutes, and estimated cost.
- Document session interruptions, quota exhaustion, out-of-memory errors, and workarounds in `FAILURES.md`.
