from pathlib import Path
import json
from pipeline.logger import log_event

ROOT = Path(__file__).resolve().parents[1]


def create_plan(storyboard):
    ROOT.joinpath('outputs').mkdir(exist_ok=True)
    plan = {
        "project": storyboard['project'],
        "stages": ["storyboard_validation", "keyframes", "moving_shots", "music", "narration", "assembly"],
        "shots": []
    }
    for shot in storyboard['shots']:
        plan['shots'].append({
            "id": shot['id'],
            "duration_seconds": shot['duration_seconds'],
            "keyframe_path": f"outputs/keyframes/{shot['id']}.png",
            "video_path": f"outputs/shots/{shot['id']}.mp4",
            "visual_prompt": shot['visual_prompt'],
            "motion_prompt": shot['motion_prompt'],
            "seed": shot.get('seed'),
            "status": shot.get('status', 'draft')
        })
    out = ROOT / 'outputs' / 'pipeline_plan.json'
    out.write_text(json.dumps(plan, ensure_ascii=False, indent=2), encoding='utf-8')
    log_event('planning', 'local-pipeline', parameters={"shot_count":len(plan['shots'])}, output_path=out)
    print(f'Plan written: {out.relative_to(ROOT)}')
    return out
