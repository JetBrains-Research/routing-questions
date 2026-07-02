#!/usr/bin/env python3
"""Download the SWE-Chat parquet tables needed for filtering.

Requires access to https://huggingface.co/datasets/SALT-NLP/SWE-chat.
Set HF_TOKEN or log in with the Hugging Face Hub before running.
"""

from __future__ import annotations

import argparse
import os
import shutil
from pathlib import Path

from huggingface_hub import hf_hub_download


REPO_ID = "SALT-NLP/SWE-chat"
DEFAULT_OUT_DIR = Path(__file__).resolve().parents[1] / "data" / "raw"
FILES = ["conversations.parquet", "sessions.parquet", "repositories.parquet"]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out-dir", type=Path, default=DEFAULT_OUT_DIR)
    parser.add_argument("--repo-id", default=REPO_ID)
    parser.add_argument("--skip-repositories", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)

    token = os.environ.get("HF_TOKEN") or os.environ.get("HUGGINGFACE_TOKEN")
    files = FILES if not args.skip_repositories else FILES[:2]

    for filename in files:
        print(f"Downloading {filename}...")
        downloaded = hf_hub_download(
            repo_id=args.repo_id,
            repo_type="dataset",
            filename=filename,
            token=token,
        )
        destination = args.out_dir / filename
        shutil.copyfile(downloaded, destination)
        print(f"Wrote {destination}")


if __name__ == "__main__":
    main()
