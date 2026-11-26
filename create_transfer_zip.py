from __future__ import annotations

import argparse
import zipfile
from pathlib import Path
from typing import Iterable


EXCLUDED_NAMES = {
    ".git",
    ".github",
    ".venv",
    "venv",
    "__pycache__",
    ".ipynb_checkpoints",
    ".env",
}
EXCLUDED_SUFFIXES = {".pyc", ".pyo"}


def iter_files(root: Path) -> Iterable[Path]:
    for path in sorted(root.rglob("*")):
        if not path.is_file():
            continue

        relative = path.relative_to(root)
        if any(part in EXCLUDED_NAMES for part in relative.parts):
            continue
        if path.name in EXCLUDED_NAMES or path.suffix.lower() in EXCLUDED_SUFFIXES:
            continue
        yield path


def create_transfer_zip(project: Path, output: Path) -> Path:
    project = project.resolve()
    output = output.resolve()

    if not project.is_dir():
        raise ValueError(f"Project directory does not exist: {project}")

    output.parent.mkdir(parents=True, exist_ok=True)
    if output.suffix.lower() != ".zip":
        output = output.with_suffix(".zip")

    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in iter_files(project):
            if path.resolve() == output:
                continue
            archive.write(path, path.relative_to(project).as_posix())

    return output


def main() -> None:
    script_directory = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(
        description="Create a ZIP that can be transferred to Google Drive or Colab."
    )
    parser.add_argument(
        "--project",
        type=Path,
        default=script_directory,
        help="Project directory to archive (default: the script directory)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="ZIP path (default: <project>/heritage_short_transfer.zip)",
    )
    args = parser.parse_args()

    project = args.project.resolve()
    output = (
        args.output.resolve()
        if args.output
        else project / "heritage_short_transfer.zip"
    )

    try:
        zip_path = create_transfer_zip(project, output)
    except (OSError, ValueError) as exc:
        parser.error(str(exc))

    print(f"Created: {zip_path}")
    print(f"Size: {zip_path.stat().st_size / 1024 / 1024:.2f} MB")


if __name__ == "__main__":
    main()
