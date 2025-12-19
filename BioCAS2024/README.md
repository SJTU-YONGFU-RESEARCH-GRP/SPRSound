# BioCAS 2024 Challenge Test Set

This dataset contains the **test set** for the **IEEE BioCAS 2024 Grand Challenge on Respiratory Sound Compression and Event Detection**. This challenge introduces new tracks (Compression and Detection) while maintaining the same dataset format as previous years.

## Dataset Overview

- **Challenge Year**: 2024
- **Task Type**: Respiratory Recording Compression & Respiratory Event Detection
- **Test Set**: 1,704 recordings (WAV + JSON pairs)
- **Training Data**: Please use the training data from previous releases

## Directory Structure

```
BioCAS2024/
├── test2024_wav/               # Test WAV files (1,704 files)
└── test2024_json/              # Test JSON annotations (1,704 files)
```

## Important Note

**This release contains only the test set for 2024.** For training, please use the training data from previous releases. Each year's challenge provides a new test set while using previously released data for training.

## File Naming Rules

Each file is named using 5 elements separated by underscores:

**Format**: `patient_number_age_gender_location_recording_number`

1. **Patient number** (e.g., `00015105`)
   - Unique identifier for each patient

2. **Age** (e.g., `5.3`)
   - Patient age in years (decimal format)

3. **Gender**
   - `0` = Male
   - `1` = Female

4. **Recording location**
   - `p1` = Left posterior
   - `p2` = Left lateral
   - `p3` = Right posterior
   - `p4` = Right lateral
   - `p5` = Additional location (for 2024+)
   - `p6` = Additional location (for 2024+)
   - `p7` = Additional location (for 2024+)
   - `p8` = Additional location (for 2024+)

5. **Recording number** (e.g., `25271`)
   - Unique identifier for each recording

**Example**: `00015105_5.3_0_p1_25271.wav`
- Patient: 00015105
- Age: 5.3 years
- Gender: Male (0)
- Location: Left posterior (p1)
- Recording ID: 25271

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
    "event_annotation": [
        {
            "start": "553",
            "end": "2535",
            "type": "Normal"
        },
        {
            "start": "2587",
            "end": "4626",
            "type": "Normal"
        }
    ]
}
```

**Fields**:
- `event_annotation`: Array of event-level annotations
  - `start`: Start time in milliseconds (string)
  - `end`: End time in milliseconds (string)
  - `type`: Event type (string)

## Challenge Tracks

### Track 1: Respiratory Recording Compression

This track deals with respiratory recordings compression using compressive sensing-based compression methods.

**Evaluation Metrics**:
- **Compression Ratio (CR)**
- **Percent Root Mean Square Difference (PRD)**
- **Correlation Coefficient (CC)**

### Track 2: Respiratory Event Detection

This track deals with the detection of onsets and offsets in addition to the assignment of event labels of respiratory events in respiratory recordings using sound event detection methods.

**Evaluation Metrics**:
- **Event-based F-score (F)**
- **Event-based Error Rate (ER)**

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

[Competition] Q. Zhang, et al. "Meta: Data Compression and Event Detection Grand Challenge 2024 With SPRSound Dataset", 
IEEE Data Descriptions (DD), vol. 1, no. 1, pp. 1-8, Dec, 2024.
```

## Contact

For more information about the challenge, please visit:
- Challenge Website: [Respiratory Sound Challenge](http://1.117.17.41/grand-challenge/)

## License

Please refer to the LICENSE file in the parent directory for licensing information.

