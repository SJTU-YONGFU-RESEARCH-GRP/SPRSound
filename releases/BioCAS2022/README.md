# BioCAS 2022 Challenge Dataset

This dataset is released for the **IEEE BioCAS 2022 Grand Challenge on Respiratory Sound Classification**. It contains respiratory sound recordings from pediatric patients with corresponding annotations for classification tasks.

## Dataset Overview

- **Challenge Year**: 2022
- **Task Type**: Respiratory Sound Classification
- **Training Set**: 1,949 recordings (WAV + JSON pairs)
- **Test Set**: 734 recordings (WAV files)
  - **Inter-subject Test Set**: 355 recordings (with JSON annotations)
  - **Intra-subject Test Set**: 379 recordings (with JSON annotations)

## Directory Structure

```
BioCAS2022/
├── train2022_wav/              # Training WAV files (1,949 files)
├── train2022_json/             # Training JSON annotations (1,949 files)
├── test2022_wav/               # Test WAV files (734 files)
└── test2022_json/              # Test JSON annotations (734 files)
    ├── inter_test_json/        # Inter-subject test annotations (355 files)
    └── intra_test_json/       # Intra-subject test annotations (379 files)
```

## File Naming Rules

Each file is named using 5 elements separated by underscores:

**Format**: `patient_number_age_gender_location_recording_number`

1. **Patient number** (e.g., `65058931`)
   - Unique identifier for each patient

2. **Age** (e.g., `3.4`)
   - Patient age in years (decimal format)

3. **Gender**
   - `0` = Male
   - `1` = Female

4. **Recording location**
   - `p1` = Left posterior
   - `p2` = Left lateral
   - `p3` = Right posterior
   - `p4` = Right lateral

5. **Recording number** (e.g., `1086`)
   - Unique identifier for each recording

**Example**: `65058931_3.4_1_p2_1086.wav`
- Patient: 65058931
- Age: 3.4 years
- Gender: Female (1)
- Location: Left lateral (p2)
- Recording ID: 1086

## Annotation Format

Each WAV file has a corresponding JSON file with the same filename (except extension) containing annotations at two levels:

### Record Level Annotation
- `Normal`: High quality recording with normal respiratory sounds
- `CAS`: Continuous Adventitious Sounds
- `DAS`: Discontinuous Adventitious Sounds
- `CAS & DAS`: Both continuous and discontinuous adventitious sounds
- `Poor Quality`: Recording with poor signal quality

### Event Level Annotation
Each recording is segmented into multiple respiratory events with the following labels:
- `Normal`: Normal respiratory sound
- `Rhonchi`: Low-pitched continuous adventitious sound
- `Wheeze`: High-pitched continuous adventitious sound
- `Stridor`: High-pitched inspiratory sound
- `Coarse Crackle`: Low-pitched discontinuous adventitious sound
- `Fine Crackle`: High-pitched discontinuous adventitious sound
- `Wheeze+Crackle`: Combination of wheeze and crackle

### JSON File Structure

```json
{
    "record_annotation": "Normal",
    "event_annotation": [
        {
            "start": "2499",
            "end": "4277",
            "type": "Normal"
        },
        {
            "start": "5182",
            "end": "7542",
            "type": "Normal"
        },
        {
            "start": "8872",
            "end": "10480",
            "type": "Normal"
        }
    ]
}
```

**Fields**:
- `record_annotation`: Record-level label (string)
- `event_annotation`: Array of event-level annotations
  - `start`: Start time in milliseconds (string)
  - `end`: End time in milliseconds (string)
  - `type`: Event type (string)

## Challenge Tasks

### Task 1: Respiratory Sound Classification at Event Level

- **Task 1-1**: Binary classification (Normal vs. Adventitious)
- **Task 1-2**: Multi-class classification (Normal, Rhonchi, Wheeze, Stridor, Coarse Crackle, Fine Crackle, Wheeze+Crackle)

### Task 2: Respiratory Sound Classification at Record Level

- **Task 2-1**: Ternary classification (Normal, Adventitious, Poor Quality)
- **Task 2-2**: Multi-class classification (Normal, CAS, DAS, CAS & DAS, Poor Quality)

## Evaluation Metrics

- **Sensitivity (SE)**
- **Specificity (SP)**
- **Average Score (AS)**
- **Harmonic Score (HS)**

## Audio Format

- **Format**: WAV
- **Sampling Rate**: Standard audio format (please check individual files for specific parameters)
- **Duration**: Variable (typically several seconds per recording)

## Test Set Split

The test set is divided into two subsets:

1. **Inter-subject Test Set** (`inter_test_json/`): 355 recordings
   - Tests generalization across different patients
   
2. **Intra-subject Test Set** (`intra_test_json/`): 379 recordings
   - Tests generalization within the same patients

## Citation

If you use this dataset, please cite:

```
[Competition] Q. Zhang, et al. "Grand Challenge on Respiratory Sound Classification", 
IEEE Biomedical Circuits and Systems Conference (BioCAS), 2022, pp. 1-5.

[Data] Q. Zhang, et al. "SPRSound: Open-Source SJTU Paediatric Respiratory Sound Database", 
IEEE Transactions on Biomedical Circuits and Systems (TBioCAS), vol. 16, no. 5, 
pp. 867-881, Oct, 2022.
```

## Contact

For more information about the challenge, please visit:
- Challenge Website: [Respiratory Sound Challenge](http://1.117.17.41/grand-challenge/)

## License

Please refer to the LICENSE file in the parent directory for licensing information.

