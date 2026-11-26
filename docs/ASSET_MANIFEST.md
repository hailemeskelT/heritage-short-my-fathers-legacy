# Asset manifest — audited repository

| Asset | Path | Finding |
|---|---|---|
| Storyboard/schema | storyboard.json; schema/storyboard.schema.json | Present; ten shots; 68-second target. |
| Keyframes | outputs/keyframes/shot_01.png … shot_10.png | All ten PNG files present; per-image logs incomplete. |
| Test frame | outputs/keyframes_test/shot_04_test.jpg | Present; one SSD-1B test log. |
| Motion clips | outputs/shots/ | .gitkeep only; no clips. |
| Narration | outputs/narration/narration.wav | Not present in Git; assembler requires it. |
| Music | outputs/music/score.wav | Not present in Git; assembler requires it. |
| Timing/SRT | outputs/audio_timing.json; subtitles/narration.en.srt | Present; narration and final subtitle cue end at 54.996 seconds. |
| Vertical MP4 | outputs/final/Heritage_Short_9x16.mp4 | Present as a Git binary object; 4,834,885 bytes. Stream not decoded. |
| Horizontal MP4 | outputs/final/Heritage_Short_16x9.mp4 | Present as a Git binary object; 5,354,795 bytes. Stream not decoded. |
| Title cards | outputs/final/titlecard_vertical.png; titlecard_horizontal.png | Present; check AI disclosure text. |

Before release, FFprobe and play both MP4s; check 60–90-second duration, dimensions, narration, score ducking, subtitle synchronisation, and end-card visibility. Resolve the 68.000 vs 54.996-second timing difference.