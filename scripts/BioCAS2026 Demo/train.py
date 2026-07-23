#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BioCAS2026 Demo — optional parameter export (no real training).

  python3 train.py -i <input_dir> -o <model_path>

<input_dir>/
  ├── xxx.wav
  └── yyy.wav

Writes a JSON model at <model_path> (file path, e.g. model.json).

This demo only dumps fixed bandpass parameters. You may replace train.py
with your own fine-tuning / training and still write a model file that
test.py can load via -m <model_path>. The official evaluator is not
released for local tuning.
"""

from __future__ import print_function

import argparse
import json
from pathlib import Path


DEFAULT_PARAMS = {
    "method": "bandpass",
    "fs_target": 8000,
    "low_hz": 50.0,
    "high_hz": 2500.0,
    "order": 4,
}


def main():
    parser = argparse.ArgumentParser(description="Export BioCAS2026 Demo parameters.")
    parser.add_argument("-i", "--input", required=True, help="Input WAV directory")
    parser.add_argument("-o", "--output", required=True, help="Output model path (JSON file)")
    args = parser.parse_args()

    input_dir = Path(args.input)
    if not input_dir.is_dir():
        raise SystemExit("Input directory not found: %s" % input_dir)

    wavs = sorted(input_dir.glob("*.wav"))
    if len(wavs) == 0:
        raise SystemExit("No .wav files in %s" % input_dir)

    model_path = Path(args.output)
    model_path.parent.mkdir(parents=True, exist_ok=True)

    params = dict(DEFAULT_PARAMS)
    params["n_train_files"] = len(wavs)

    with open(model_path, "w") as f:
        json.dump(params, f, indent=2)

    print("Saved model: %s  (%d wav files seen)" % (model_path, len(wavs)))


if __name__ == "__main__":
    main()
