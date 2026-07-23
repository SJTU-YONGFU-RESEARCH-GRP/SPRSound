# BioCAS2026 Demo

Minimal reference submission under `BioCAS2026 Demo/`.
It shows the required I/O only; the algorithm is a fixed bandpass (no learning).

## Directory layout

```text
<input_dir>/
├── xxx.wav
└── yyy.wav
```

Output keeps the **same filenames** in `<output_dir>/`.

## Commands

Optional (this demo only writes a parameter file):

```bash
python3 train.py -i <input_dir> -o <model_path>
```

Required for evaluation:

```bash
python3 test.py -i <input_dir> -o <output_dir> -m <model_path>
```

`<model_path>` is a JSON file (e.g. `model.json`).

## Algorithm

- Butterworth **bandpass 50–2500 Hz**, order 4, zero-phase (`sosfiltfilt`)
- Optional resample to **8 kHz** if set in the model
- This demo’s `train.py` only **exports** default parameters (no real training)

You can **fine-tune or train by yourself** (any method, any private proxy metric).  
Replace or extend `train.py` so it writes your own `<model_path>`; `test.py` must still load that model with `-m`. The official evaluator is not released for local score chasing — official scores come from organisers’ submission pipeline.

## Dependencies

`numpy`, `scipy`

## Notes for your own method

- Everyone must provide `test.py` with the same CLI: `-i`, `-o`, `-m`
- `train.py` is optional in this demo; for learnable methods, use it (or your own script) to produce `<model_path>`
