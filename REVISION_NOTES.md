# Revision Notes — 27 November 2026

This branch contains an evidence-based update after re-auditing the connected repository at main commit `2c4a5250c7bb43224c4aa91e209be1296e27920b`.

Updated: README.md, ARCHITECTURE.md, DESIGN.md, EXPERIMENTS.md, FAILURES.md, COSTS.md, ETHICS.md, REPORT.md, docs/SUBMISSION_CHECKLIST.md, docs/ASSET_MANIFEST.md, docs/WALKTHROUGH_SCRIPT.md, and docs/FINAL_SUBMISSION_AUDIT.md.

Key corrections:
- Ten numbered keyframe PNGs and both final MP4 file objects are in the repository.
- Narration and music WAV files and moving-shot MP4 clips are absent from the Git tree.
- The current CLI `run` command plans and assembles stills; it does not generate assets.
- Cache helpers are not integrated into stage execution.
- `runs.jsonl` contains one SSD-1B test record, not all model calls.
- Narration timing and SRT end at 54.996 seconds, while the storyboard target is 68 seconds.
- Final MP4 stream properties and AI-disclosure end frames were not decoded in the text-based GitHub audit.
- The owner reports both audience tests were completed, but participant findings are not present in the public documentation.
- Family consent scope, exact model/service versions and licensing terms require records/confirmation.

No participant feedback, stage-cost totals, permission records or unverified media properties have been invented. Main is left unchanged; the revised documents are on a separate review branch.