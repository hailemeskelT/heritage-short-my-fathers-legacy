from pathlib import Path
import subprocess
import shutil

ROOT = Path(__file__).resolve().parents[1]


def _escape_filter_path(path: Path) -> str:
    # FFmpeg filtergraph path escaping for common special characters.
    value = path.resolve().as_posix()
    value = value.replace('\\', r'\\').replace(':', r'\\:').replace("'", r"\\'").replace(',', r'\\,')
    return value


def _run(cmd):
    print('Running:', ' '.join(str(x) for x in cmd))
    proc = subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True)
    if proc.returncode != 0:
        raise RuntimeError(f"FFmpeg failed ({proc.returncode}).\nSTDOUT:\n{proc.stdout}\nSTDERR:\n{proc.stderr}")


def assemble_from_stills(storyboard, allow_missing_video=True):
    ffmpeg = shutil.which('ffmpeg')
    if not ffmpeg:
        raise RuntimeError('FFmpeg is not installed or not available on PATH.')

    shots = storyboard['shots']
    image_paths = [ROOT / 'outputs' / 'keyframes' / f"{s['id']}.png" for s in shots]
    missing = [p for p in image_paths if not p.exists()]
    if missing:
        raise FileNotFoundError('Missing keyframes:\n' + '\n'.join(str(p.relative_to(ROOT)) for p in missing))

    narration = ROOT / 'outputs' / 'narration' / 'narration.wav'
    music = ROOT / 'outputs' / 'music' / 'score.wav'
    subtitles = ROOT / 'subtitles' / 'narration.en.srt'
    for p, label in [(narration,'Amharic narration WAV'), (music,'original score WAV'), (subtitles,'English SRT subtitles')]:
        if not p.exists():
            raise FileNotFoundError(f'Missing {label}: {p.relative_to(ROOT)}')

    out_dir = ROOT / 'outputs' / 'final'
    out_dir.mkdir(parents=True, exist_ok=True)

    for label, width, height, filename in [
        ('vertical',1080,1920,'Heritage_Short_9x16.mp4'),
        ('horizontal',1920,1080,'Heritage_Short_16x9.mp4')
    ]:
        cmd = [ffmpeg, '-y']
        for p, shot in zip(image_paths, shots):
            cmd += ['-loop','1','-framerate','24','-t',str(shot['duration_seconds']),'-i',str(p)]
        narr_idx = len(image_paths)
        music_idx = narr_idx + 1
        cmd += ['-i',str(narration),'-i',str(music)]

        filters = []
        vlabels = []
        for i in range(len(image_paths)):
            tag = f'v{i}'
            filters.append(f'[{i}:v]scale={width}:{height}:force_original_aspect_ratio=increase,crop={width}:{height},fps=24,setsar=1,format=yuv420p,setpts=PTS-STARTPTS[{tag}]')
            vlabels.append(f'[{tag}]')
        filters.append(''.join(vlabels) + f'concat=n={len(vlabels)}:v=1:a=0[vbase]')
        srt_path = _escape_filter_path(subtitles)
        filters.append(f"[vbase]subtitles='{srt_path}':force_style='FontSize=34,Alignment=2,MarginV=150,Outline=2,Shadow=1'[vout]")
        # Sidechain compression lowers score while narration is active; mix then normalize.
        filters.append(f'[{music_idx}:a][{narr_idx}:a]sidechaincompress=threshold=0.02:ratio=6:attack=300:release=1500[ducked]')
        filters.append(f'[{narr_idx}:a][ducked]amix=inputs=2:duration=longest:dropout_transition=2,loudnorm=I=-14:TP=-1:LRA=11[aout]')
        cmd += ['-filter_complex',';'.join(filters),'-map','[vout]','-map','[aout]','-r','24','-c:v','libx264','-preset','medium','-crf','20','-pix_fmt','yuv420p','-c:a','aac','-b:a','192k','-movflags','+faststart','-shortest',str(out_dir / filename)]
        _run(cmd)
        print(f'{label} export created: outputs/final/{filename}')

    print('NOTE: This starter assembler creates a Ken Burns-free still-image sequence. Add approved moving clips or a pan/zoom stage if you use them; maintain the same documented one-command pipeline.')
