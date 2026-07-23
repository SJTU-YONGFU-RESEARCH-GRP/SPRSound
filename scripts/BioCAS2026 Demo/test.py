#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BioCAS2026 Demo — inference.

  python3 test.py -i <input_dir> -o <output_dir> -m <model_path>

<input_dir>/
  ├── xxx.wav
  └── yyy.wav

Writes denoised WAVs to <output_dir>/ with the same filenames.
"""

from __future__ import print_function

import argparse
import json
import wave
from pathlib import Path

import numpy as np
from scipy import signal
from scipy.io import wavfile


def _read_pcm_with_wave(path):
    """Read PCM WAVs whose redundant header fields fail SciPy validation."""
    with wave.open(str(path), "rb") as handle:
        if handle.getcomptype() != "NONE":
            raise ValueError("Compressed WAV is unsupported: %s" % path)
        fs = handle.getframerate()
        channels = handle.getnchannels()
        sample_width = handle.getsampwidth()
        frames = handle.readframes(handle.getnframes())

    if sample_width == 1:
        audio = np.frombuffer(frames, dtype=np.uint8)
    elif sample_width == 2:
        audio = np.frombuffer(frames, dtype="<i2")
    elif sample_width == 4:
        audio = np.frombuffer(frames, dtype="<i4")
    else:
        raise ValueError("Unsupported PCM sample width %d: %s" % (sample_width, path))

    if channels > 1:
        audio = audio.reshape(-1, channels)
    return int(fs), audio


def load_wav(path):
    try:
        fs, audio = wavfile.read(str(path))
    except ValueError as err:
        # Official SPRSound files often have inconsistent nAvgBytesPerSec /
        # nBlockAlign; payload is still valid PCM.
        if "WAV header is invalid" not in str(err):
            raise
        fs, audio = _read_pcm_with_wave(path)

    audio = np.asarray(audio)
    if audio.ndim > 1:
        audio = audio[:, 0]

    # keep original integer dtype for writing back when possible
    orig_dtype = audio.dtype
    if np.issubdtype(audio.dtype, np.integer):
        if audio.dtype == np.uint8:
            max_val = 128.0
            x = (audio.astype(np.float64) - 128.0) / max_val
        else:
            max_val = float(np.iinfo(audio.dtype).max)
            x = audio.astype(np.float64) / max_val
    else:
        max_val = 1.0
        x = audio.astype(np.float64)

    return x, int(fs), orig_dtype, max_val


def save_wav(path, fs, x, orig_dtype, max_val):
    x = np.asarray(x, dtype=np.float64)
    peak = np.max(np.abs(x)) + 1e-12
    if peak > 1.0:
        x = x / peak

    if np.issubdtype(orig_dtype, np.integer):
        y = np.clip(x * max_val, np.iinfo(orig_dtype).min, np.iinfo(orig_dtype).max)
        y = y.astype(orig_dtype)
    else:
        y = x.astype(np.float32)

    wavfile.write(str(path), fs, y)


def resample_if_needed(x, fs, fs_target):
    if fs == fs_target:
        return x, fs
    n_out = int(round(len(x) * float(fs_target) / float(fs)))
    if n_out < 1:
        return x, fs
    y = signal.resample(x, n_out)
    return np.asarray(y, dtype=np.float64), fs_target


def bandpass_denoise(x, fs, low_hz, high_hz, order=4):
    nyq = 0.5 * fs
    low = max(low_hz / nyq, 1e-6)
    high = min(high_hz / nyq, 0.999)
    if high <= low:
        return x

    sos = signal.butter(order, [low, high], btype="bandpass", output="sos")
    try:
        return signal.sosfiltfilt(sos, x)
    except ValueError:
        return x


def load_model(model_path):
    with open(model_path, "r") as f:
        return json.load(f)


def process_file(wav_path, out_path, params):
    x, fs, orig_dtype, max_val = load_wav(wav_path)
    n_orig = len(x)

    fs_target = int(params.get("fs_target", fs))
    x_work, fs_work = resample_if_needed(x, fs, fs_target)

    y = bandpass_denoise(
        x_work,
        fs_work,
        float(params.get("low_hz", 50.0)),
        float(params.get("high_hz", 2500.0)),
        int(params.get("order", 4)),
    )

    if fs_work != fs:
        y, _ = resample_if_needed(y, fs_work, fs)

    if len(y) > n_orig:
        y = y[:n_orig]
    elif len(y) < n_orig:
        y = np.pad(y, (0, n_orig - len(y)))

    save_wav(out_path, fs, y, orig_dtype, max_val)


def main():
    parser = argparse.ArgumentParser(description="Run BioCAS2026 Demo bandpass denoiser.")
    parser.add_argument("-i", "--input", required=True, help="Input WAV directory")
    parser.add_argument("-o", "--output", required=True, help="Output WAV directory")
    parser.add_argument("-m", "--model", required=True, help="Model path (JSON from train.py)")
    args = parser.parse_args()

    input_dir = Path(args.input)
    output_dir = Path(args.output)
    model_path = Path(args.model)

    if not input_dir.is_dir():
        raise SystemExit("Input directory not found: %s" % input_dir)
    if not model_path.is_file():
        raise SystemExit("Model not found: %s" % model_path)

    params = load_model(model_path)
    output_dir.mkdir(parents=True, exist_ok=True)

    wavs = sorted(input_dir.glob("*.wav"))
    if len(wavs) == 0:
        raise SystemExit("No .wav files in %s" % input_dir)

    for wav_path in wavs:
        out_path = output_dir / wav_path.name
        process_file(wav_path, out_path, params)
        print("Wrote %s" % out_path)

    print("Done: %d files -> %s" % (len(wavs), output_dir))


if __name__ == "__main__":
    main()
