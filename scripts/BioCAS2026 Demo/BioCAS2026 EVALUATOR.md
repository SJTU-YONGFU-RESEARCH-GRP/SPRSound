# Lung Sound Denoising Evaluator

## Submission

All individuals, teams and each member should submit the data use agreement in advance. (If not, your submissions will not be accepted.)

Multiple submissions are allowed. Please limit your submission to **1 per day**.

All submitted files must be compressed in **ZIP** format. The submission package must include the following components:

### 1. Training Script (optional)

Filename: `train.py`

This script is **optional**. Include it if your method needs training or fine-tuning; otherwise you may omit `train.py` and ship a static model file for `-m` in testing.

Execution command:

```bash
python3 train.py -i <input_dir> -o <model_path>
```

Input directory structure:

```text
<input_dir>/
├── xxx.wav
└── xxx.wav
```

Output: trained model file (e.g., `models/model.pkl`)

### 2. Testing Script

Filename: `test.py`

Execution command:

```bash
python3 test.py -i <input_dir> -o <output_dir> -m <model_path>
```

Input directory structure:

```text
<input_dir>/
├── xxx.wav
└── xxx.wav
```

Output directory structure:

```text
<output_dir>/
├── xxx.wav
└── xxx.wav
```

### 3. Dependencies File

Filename: `requirements.txt`

Content: list all Python dependencies with version specifications.

### 4. Documentation

Filename: `README.md`

Content requirements:

- Detailed model architecture description
- Training procedure
- Testing procedure
- Usage examples

A reference package is provided in `demo/`.

---

## Evaluation metric

No-reference metric: score a pair **(original, processed)** WAV at **8 kHz**.  
Final score:

\[
S = 0.40\,D + 0.35\,H + 0.25\,R,\qquad D,H,R\in[0,1]
\]

**D**, **H**, and **R** are each a single scalar in \([0,1]\) summarising the quantities below. Frequency bands, STFT settings, and the definitions of those quantities are fixed for all teams. Because the evaluation dataset is public, internal mapping scales and sub-weights are held by the organisers (identical for all submissions) to limit metric gaming and overfitting.

---

## Frequency bands

| Used in | Band (Hz) | Role |
|---------|-----------|------|
| **D** | 50–2500 | Full lung band for prominence |
| **D** | 5–20 and >2500 | Edge noise floor (outside lung) |
| **H** | 20–150 | Heart band |
| **H** | 150–800 | Mid-band lung energy to form heart/lung **ratio** (avoids overlapping 20–150) |
| **R** | 150–2500 | Lung naturalness (starts at 150 to exclude heart) |
| **H** rhythm | 0.6–4 | Heartbeat rate on heart-band envelope |
| **R** envelope | ~0.1–1 | Breathing rate on lung-band envelope |

---

## Shared analysis

- Length-align, remove DC.  
- STFT: Hann, **250 ms**, 50% overlap; power \(P=|Z|^2\);  
  \(L_{\mathrm{dB}}=10\log_{10}(\max(P,\varepsilon))\).  
- Aggregate with **median over active frames** of the original.  
- Positive dB improvements are mapped into \([0,1)\) before weighting.

---

## D — Denoising

**Meaning:** after processing, lung energy should stand out more clearly above the noise floor (pseudo-SNR / spectral prominence; **not** clean-reference SNR).

- Lung level: 95th percentile power in 50–2500 Hz → dB.  
- Edge noise: median dB in 5–20 Hz and >2500 Hz.  
- In-band noise: 25th percentile power in 50–2500 Hz → dB.  
- Prominence: \(L_{\mathrm{lung}}-L_{\mathrm{noise}}\).  

**D** rises with prominence gain and noise-floor drop; identity (no change) → \(D\approx 0\).

---

## H — Heart suppression

**Meaning:** heart-related content should weaken **relative to** lung, and heartbeat rhythm on the heart-band envelope should weaken.

- Band ratio (dB): \(L_{20\text{–}150}-L_{150\text{–}800}\) (lower after processing is better).  
- Rhythm: band-pass 20–150 Hz → Hilbert envelope → peak in 0.6–4 Hz.  
- If the original shows little heart periodicity, the rhythm term is down-weighted.

**H** does not measure broadband denoising strength.

---

## R — Naturalness

**Meaning:** breathing should still look natural above the heart band. **R is not fidelity to the original** (identity need not give \(R=1\)).

Evaluated from **150 Hz** upward:

- Envelope modulation depth \(\mathrm{MD}=\mathrm{IQR}/\mathrm{median}\) on ~0.1–1 Hz respiratory modulation.  
- Spectral texture and overall spectral shape in the lung band.

Scores both (a) preservation vs original and (b) absolute plausibility of the processed signal.
