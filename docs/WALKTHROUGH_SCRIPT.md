# Walkthrough Video Script (maximum 5 minutes)

Target duration: approximately 4 minutes.

## 0:00–0:30 — Introduce the project

Show the finished Heritage Short and state its audience, story purpose, and language.

## 0:30–1:30 — Explain the architecture

Show `storyboard.json`, schema validation, and the stage sequence: keyframes, moving shots, music, narration, assembly. Explain caching, retries, and where Colab fits.

## 1:30–2:15 — Show evidence

Show a real `runs.jsonl` entry and one experiment with its hypothesis, change, and measured result. Mention one failure and how you handled it.

## 2:15–3:15 — Demonstrate selective regeneration

1. Open `storyboard.json`.
2. Change one shot's visual prompt or narration line.
3. Run the pipeline.
4. Show that only the affected stage output is regenerated and unaffected outputs are reused.
5. Show the new log entry.

You do not need to rerun Wan 2.2 live; the brief accepts showing the single new model call in the logs and allows pausing during generation.

## 3:15–4:00 — Close

Show the two exported aspect ratios, the AI disclosure end card, and summarize one lesson learned.

## Recording checklist

- [ ] Screen text is readable.
- [ ] No API keys, access tokens, private family details, or unapproved faces/voices are shown.
- [ ] Actual outputs and logs are used; do not stage fake evidence.
- [ ] Total duration is no more than five minutes.
