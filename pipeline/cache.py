import hashlib
import json
from pathlib import Path


def file_sha256(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for block in iter(lambda: f.read(1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()


def stable_hash(payload):
    encoded = json.dumps(payload, sort_keys=True, ensure_ascii=False, separators=(',', ':')).encode('utf-8')
    return hashlib.sha256(encoded).hexdigest()


def stage_cache_key(stage, inputs, model=None, parameters=None, seed=None, reference_files=None):
    refs = {}
    for p in reference_files or []:
        path = Path(p)
        refs[str(path)] = file_sha256(path) if path.exists() and path.is_file() else 'MISSING'
    return stable_hash({"stage":stage,"inputs":inputs,"model":model,"parameters":parameters or {},"seed":seed,"references":refs})
