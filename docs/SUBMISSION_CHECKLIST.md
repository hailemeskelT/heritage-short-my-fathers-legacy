# Final submission readiness checklist

**Audit date:** 27 November 2026. **Repository audit branch:** submission/revised-report-and-docs.

## Assignment 1 — Codebase and report
- Public repository: present.
- Storyboard JSON and schema validator: present.
- Ten experiment entries: documented, but several historic results lack retained logs/outputs.
- Ten keyframe PNG files: present; individual model-call records are incomplete.
- Final report: revised version in this branch.
- README/architecture: describe the actual source behaviour.
- Clean-clone one-command AI generation: not demonstrated; main.py run plans and assembles only.
- Per-stage caching/retries: not integrated/implemented.
- runs.jsonl: one SSD-1B test record, not every model call.
- Cost totals: incomplete; one test latency/memory record and narration duration retained.
- Ethics: family permission scope and service/model version records need confirmation.

## Assignment 2 — Film, walkthrough, and post
- Vertical and horizontal MP4 file objects are present in outputs/final/; streams were not independently decoded in this audit.
- Narration timing and English SRT are present; WAV is not in Git.
- Score WAV is not in Git; sidechain compression exists in assembler source, but final mix is not verified.
- No moving-shot clips are tracked; current assembler concatenates still images.
- AI disclosure string and titlecard images exist; final MP4 disclosure frame must be checked.
- Walkthrough template exists; final walkthrough evidence link was not found in the repository.
- Public-post template exists; final post URL/screenshot was not found in the repository.

## Critical checks
- [ ] Resolve 68-second storyboard vs 54.996-second narration/SRT timeline.
- [ ] FFprobe both MP4s for dimensions, frame rate, runtime, and audio streams.
- [ ] Watch both versions; verify captions, audio mix/ducking, and visible AI end card.
- [ ] Add anonymised findings from both audience tests.
- [ ] Retain family permission privately and record scope in ETHICS.md.
- [ ] Add walkthrough (≤5 minutes), public post URL/screenshot, and platform AI label proof.
- [ ] Test all reviewer links in a private browser.
- [ ] Confirm portal accepts late submission: the original checklist lists 26 November 2026, 23:59 EAT; this audit is 27 November 2026.