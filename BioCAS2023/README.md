# BioCAS 2023 Challenge Test Set

This dataset contains the **test set** for the **IEEE BioCAS 2023 Grand Challenge on Respiratory Sound Classification**. This challenge uses the same tasks as BioCAS 2022, with a new test set provided for evaluation.

## Dataset Overview

- **Challenge Year**: 2023
- **Task Type**: Respiratory Sound Classification (same as 2022)
- **Test Set**: 871 recordings (WAV + JSON pairs)
- **Training Data**: Please use the training data from the BioCAS 2022 release

## Directory Structure

```
BioCAS2023/
├── test2023_wav/               # Test WAV files (871 files)
└── test2023_json/              # Test JSON annotations (871 files)
```

## Important Note

**This release contains only the test set for 2023.** For training, please use the training data from the BioCAS 2022 release. Each year's challenge provides a new test set while using previously released data for training.

## File Naming Rules

Each file is named using 5 elements separated by underscores:

**Format**: `patient_number_age_gender_location_recording_number`

1. **Patient number** (e.g., `00014365`)
   - Unique identifier for each patient

2. **Age** (e.g., `4.3`)
   - Patient age in years (decimal format)

3. **Gender**
   - `0` = Male
   - `1` = Female

4. **Recording location**
   - `p1` = Left posterior
   - `p2` = Left lateral
   - `p3` = Right posterior
   - `p4` = Right lateral

5. **Recording number** (e.g., `7545`)
   - Unique identifier for each recording

**Example**: `00014365_4.3_1_p4_7545.wav`
- Patient: 00014365
- Age: 4.3 years
- Gender: Female (1)
- Location: Right lateral (p4)
- Recording ID: 7545

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

The tasks for BioCAS 2023 are the same as BioCAS 2022:

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

## Citation

If you use this dataset, please cite:

```
[Data] Q. Zhang, et al. "SPRSound: Open-Source SJTU Paediatric Respiratory Sound Database", 
IEEE Transactions on Biomedical Circuits and Systems (TBioCAS), vol. 16, no. 5, 
pp. 867-881, Oct, 2022.

[Competition] Q. Zhang, et al. "Grand Challenge on Respiratory Sound Classification", 
IEEE Biomedical Circuits and Systems Conference (BioCAS), 2022, pp. 1-5.

[Competition] Q. Zhang, et al. "Grand Challenge on Respiratory Sound Classification for SPRSound Dataset II", 
IEEE Biomedical Circuits and Systems Conference (BioCAS), pp. 1-5, Oct, 2023.
```

## Contact

For more information about the challenge, please visit:
- Challenge Website: [Respiratory Sound Challenge](http://1.117.17.41/grand-challenge/)

## License

Please refer to the LICENSE file in the parent directory for licensing information.

