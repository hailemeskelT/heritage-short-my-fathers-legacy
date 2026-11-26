# Costs and measurements

## Runtime
- Environment: Google Colab.
- GPU: NVIDIA Tesla T4.
- Reported GPU memory: 14.56 GB.
- Idle GPU allocation with CPU offloading: 0.0 GB reported.
- First SSD-1B test generation: approximately 27 seconds.
- Peak GPU memory reported for that test: 3.32 GB.

## Models and services

| Stage | Tool/model | Cost record |
|---|---|---|
| Keyframes | Segmind SSD-1B / Diffusers | No per-image hosted API charge; Colab GPU quota applies. |
| Narration | Edge TTS, `am-ET-MekdesNeural` | Online service; no Gemini TTS API charge recorded. Verify service terms. |
| Music | Python-generated synthetic score | No external music API charge. |
| Assembly | FFmpeg | No per-export API charge. |
| Gemini image API | Not used for final generation | Paid billing was required; no successful image call cost is claimed. |

## Measurements still to enter

| Stage | Actual total latency | GPU minutes | Notes |
|---|---:|---:|---|
| Model loading | [MEASURE] | [MEASURE] | Include download separately if relevant. |
| Ten keyframes | [MEASURE] | [MEASURE] | Use actual generation logs. |
| Narration | [MEASURE] | N/A or measured | Record actual TTS time. |
| Music | [MEASURE] | N/A | Local Python generation. |
| Assembly 9:16 | [MEASURE] | N/A | Record FFmpeg wall time. |
| Assembly 16:9 | [MEASURE] | N/A | Record FFmpeg wall time. |

Do not estimate missing measurements as if they were observed.
State separately whether any cash payment was actually made.
