# Asset Manifest and Naming Convention

| Asset | Expected path | Required status |
|---|---|---|
| Character reference sheet | `references/character_sheet.png` | Approved before keyframes |
| Style reference | `references/style_reference.png` | Approved before keyframes |
| Keyframes | `outputs/keyframes/shot_01.png` … `shot_10.png` | One per storyboard shot |
| Moving shot clips | `outputs/shots/shot_01.mp4` … | Generate where GPU/model budget allows; fallback still animation is acceptable |
| Amharic narration | `outputs/narration/narration.wav` | Required for final assembly |
| Original score | `outputs/music/score.wav` | Required for final assembly |
| English subtitles | `subtitles/narration.en.srt` | Required for final assembly |
| Vertical export | `outputs/final/Heritage_Short_9x16.mp4` | Required |
| Horizontal export | `outputs/final/Heritage_Short_16x9.mp4` | Required |

## Quality control

- Inspect every keyframe for facial/hand artifacts, unwanted text, and continuity.
- Compare character identity, clothing, setting, and lighting across shots.
- Check clip start/end frames and trim weak segments.
- Verify SRT timing against Amharic audio.
- Check vertical safe areas; keep subtitles clear of platform interface areas.
- Check audio mix on phone speakers and headphones.
- Preserve model provenance/watermarks when present.
