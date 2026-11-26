from pathlib import Path
import json
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]


def validate_storyboard(storyboard_path=None, schema_path=None):
    storyboard_path = Path(storyboard_path or ROOT / 'storyboard.json')
    schema_path = Path(schema_path or ROOT / 'schema' / 'storyboard.schema.json')
    if not storyboard_path.exists():
        raise FileNotFoundError(f'Storyboard not found: {storyboard_path}')
    if not schema_path.exists():
        raise FileNotFoundError(f'JSON Schema not found: {schema_path}')
    data = json.loads(storyboard_path.read_text(encoding='utf-8'))
    schema = json.loads(schema_path.read_text(encoding='utf-8'))
    errors = sorted(Draft202012Validator(schema).iter_errors(data), key=lambda e: list(e.path))
    if errors:
        formatted = '\n'.join(f"- {'/'.join(map(str, e.path)) or '<root>'}: {e.message}" for e in errors)
        raise ValueError('Storyboard schema validation failed:\n' + formatted)
    total = sum(float(s['duration_seconds']) for s in data['shots'])
    if not 60 <= total <= 90:
        raise ValueError(f'Shot durations total {total:.2f}s; challenge requires 60–90 seconds.')
    target = float(data['project']['target_duration_seconds'])
    if abs(total - target) > 0.05:
        raise ValueError(f'Shot total ({total:.2f}s) does not match project.target_duration_seconds ({target:.2f}s).')
    print(f'VALID: {storyboard_path.name}; {len(data["shots"])} shots; {total:.1f} seconds.')
    return data
