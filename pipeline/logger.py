from pathlib import Path
from datetime import datetime, timezone
import json

ROOT = Path(__file__).resolve().parents[1]
LOG_PATH = ROOT / 'runs.jsonl'


def log_event(stage, model, parameters=None, seed=None, latency_seconds=None, cost_estimate=None,
              status='success', output_path=None, details=None):
    record = {
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "stage": stage,
        "model": model,
        "parameters": parameters or {},
        "seed": seed,
        "latency_seconds": latency_seconds,
        "cost_estimate": cost_estimate,
        "status": status,
        "output_path": str(output_path) if output_path else None,
        "details": details or {}
    }
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    with LOG_PATH.open('a', encoding='utf-8') as f:
        f.write(json.dumps(record, ensure_ascii=False) + '\n')
    return record
