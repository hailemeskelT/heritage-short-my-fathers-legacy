# Master Requirements Checklist — The Heritage Short

This checklist follows the attached challenge brief. The items marked **Mandatory** are the baseline deliverables; optional extension work is listed separately.

## A. Film requirements — Assignment 2

- [ ] **Mandatory:** A 60–90-second short film about a meaningful person, place, or story.
- [ ] **Mandatory:** Narration in the selected language (project choice: Amharic).
- [ ] **Mandatory:** English subtitles that accurately match the narration.
- [ ] **Mandatory:** Original musical score.
- [ ] **Mandatory:** Music ducking under narration (score gets quieter while speech is present).
- [ ] **Mandatory:** Consistent character identity and visual style across shots.
- [ ] **Mandatory:** Vertical 9:16 MP4.
- [ ] **Mandatory:** Horizontal 16:9 MP4.
- [ ] **Mandatory:** Visible end card stating that the film was made with AI.
- [ ] **Mandatory:** Publish with the platform's AI label/disclosure enabled, or supply a screenshot if not posting publicly.

## B. Pipeline / software requirements — Assignment 1

- [ ] **Mandatory:** Public GitHub repository.
- [ ] **Mandatory:** `storyboard.json` is the contract shared by pipeline stages.
- [ ] **Mandatory:** JSON Schema validates storyboard before each run.
- [ ] **Mandatory:** Separate stage scripts for script/story, keyframes, moving shots, music, narration, and assembly.
- [ ] **Mandatory:** Re-runs regenerate only changed outputs (input hashing/cache).
- [ ] **Mandatory:** Retries and error handling.
- [ ] **Mandatory:** Secrets kept out of repository.
- [ ] **Mandatory:** One log line per model call in `runs.jsonl`, including model, parameters, seed, latency, and cost or cost estimate.
- [ ] **Mandatory:** A documented one-command run from a clean clone.
- [ ] **Mandatory:** `README.md` explains installation, execution, and cost.
- [ ] **Mandatory:** `ARCHITECTURE.md` explains stage boundaries, contracts, caching, and failure handling.

## C. Design thinking and user testing

- [ ] **Mandatory:** State intended audience and what they should feel/understand before generation.
- [ ] **Mandatory:** First prototype is a radio cut (narration plus placeholder music, black screen).
- [ ] **Mandatory:** Test radio cut with at least three people from intended audience.
- [ ] **Mandatory:** Record what participants said and what changed in `DESIGN.md`.
- [ ] **Mandatory:** Test near-final film with at least three people from intended audience.
- [ ] **Mandatory:** Record the second test and resulting changes in `DESIGN.md`.
- [ ] **Mandatory:** Give every shot a reason in the storyboard / design notes.

## D. Experiments, persistence, and measurement

- [ ] **Mandatory:** At least ten experiments, each documenting hypothesis → change → result.
- [ ] **Mandatory:** Comparisons supported by actual evidence (text, logs, outputs, or measurements).
- [ ] **Mandatory:** `FAILURES.md` records actual blockers, attempts, fixes or workarounds.
- [ ] **Mandatory:** `COSTS.md` reports measured latency and GPU minutes per stage and list-price-equivalent cost where it can be estimated.
- [ ] **Mandatory where available:** Frontier-model comparison if access is provided; do not claim a comparison not performed.

## E. Ethics, consent, and licences

- [ ] **Mandatory:** Record consent for every real person whose identifiable face/likeness or voice appears or is replicated.
- [ ] **Mandatory:** If a real person appears or is voiced without a consent record in `ETHICS.md`, the film scores zero under the brief.
- [ ] **Mandatory:** Record licence/terms for every model used and relevant output rights.
- [ ] **Mandatory:** State labelling/disclosure plan and enable AI disclosure on the publishing platform.
- [ ] **Mandatory:** Preserve available watermarks/provenance metadata.
- [ ] **Good practice:** Do not send sensitive private family information to free endpoints unless you have checked data-use terms and have permission.

## F. Report requirements — Assignment 1

- [ ] **Mandatory:** What you set out to make and for whom.
- [ ] **Mandatory:** What you learned from both audience tests.
- [ ] **Mandatory:** Hardest problem and how you solved or worked around it.
- [ ] **Mandatory:** One suggested practice that beat your instinct and one that did not, with evidence.
- [ ] **Mandatory:** Any ceiling/extension work performed.
- [ ] **Mandatory:** What you would build next.

## G. Walkthrough and public communication — Assignment 2

- [ ] **Mandatory:** Walkthrough video at most five minutes.
- [ ] **Mandatory:** Explain architecture and one hard decision.
- [ ] **Mandatory:** Change one keyframe prompt or narration line in `storyboard.json`.
- [ ] **Mandatory:** Re-run and show only the affected shot regenerating; logs with one new model call count as evidence. A full Wan rerun is not required on camera.
- [ ] **Mandatory:** Write your own public post explaining the story, why it matters, and one lesson learned.

## H. Optional ceiling work

These are extensions, not prerequisites for the baseline:

- Test another Ethiopian language (e.g. Afaan Oromo, Tigrinya, Somali) and document model performance.
- Generate a song with lyrics rather than an instrumental score.
- Benchmark an open model against a frontier model with measured cost/latency and blind preference testing.
- Package the pipeline as a CLI or MCP server for others.
- Build a simple web app for relatives to submit stories.
- Train a LoRA and measure character-consistency improvement.
- Measure audience response after publishing.

## Assessment weight summary

### Assignment 1 — Codebase and report (100 points)

| Criterion | Points |
|---|---:|
| Software engineering and reproducibility | 20 |
| Documentation | 10 |
| Design thinking and audience | 10 |
| Experimentation and iteration | 10 |
| Troubleshooting and persistence | 10 |
| Measurement | 5 |
| Consent, labelling and licences | 5 |
| Report: reflection and audience learning | 10 |
| Report: suggested practices tested honestly | 10 |
| Report: curiosity beyond the floor | 10 |
| **Total** | **100** |

### Assignment 2 — Film, walkthrough and post (100 points)

| Criterion | Points |
|---|---:|
| Film | 50 |
| Walkthrough video | 30 |
| Public post | 20 |
| **Total** | **100** |

## Deadline

Both assignments: **Thursday, 26 November 2026, 23:59 East Africa Time (EAT)**.
