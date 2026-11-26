# Walkthrough script — evidence-aligned version

Maximum duration: five minutes. The current tracked CLI does not perform AI generation or selective per-shot regeneration. Do not demonstrate main.py run as though it does.

## Suggested four-minute structure
1. **0:00–0:35 — Film and purpose.** Show the two exports and explain the family story, audience, and AI-assisted approach.
2. **0:35–1:25 — Storyboard contract.** Open storyboard.json and the schema. Run python main.py validate and show the actual ten-shot, 68-second validation output.
3. **1:25–2:10 — Code.** Show validate.py, plan.py, assemble.py, cache.py, and logger.py. Explain accurately that run validates, plans, and assembles stills; cache helpers are not integrated; generation stages are external/not wired.
4. **2:10–3:10 — Experiment.** Show the actual Shot 04 SSD-1B test record: 1024x1024, 30 steps, guidance 9.0, seed 404, about 27 seconds, 3.32 GB peak memory. Explain the CLIP prompt truncation issue.
5. **3:10–4:00 — Outputs and lesson.** Show ten keyframes and both MP4s. Explain still-image assembly and the audio-timing verification still needed.

## Selective regeneration demonstration
If selective regeneration was completed in a separate Colab notebook, show the actual notebook, changed prompt, regenerated shot, and matching model-call log. The tracked CLI does not currently implement selective per-shot regeneration. Do not stage or fabricate the evidence.

## Recording checklist
- Runtime no more than five minutes.
- Show actual outputs and logs only.
- Hide API keys, tokens, private family information, and unapproved likeness/voice.
- State one technical limitation accurately.