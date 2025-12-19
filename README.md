# SPRSound: Open-Source SJTU Paediatric Respiratory Sound Database

This repository contains the released respiratory sound database for IEEE BioCAS Respiratory Sound Track Challenges. Please refer to this link ([Respiratory Sound Challenge](http://1.117.17.41/grand-challenge/)) for more information about the challenges.

<!-- TABLE OF CONTENTS -->

## Table of Contents

* [Database](#database)
* [Dataset Versions](#dataset-versions)
* [Challenge 2022 & 2023](#past-challenges)
  * [Main Tasks](#maintask)
  * [Evaluation Metrics](#evaluation1)

* [Challenge 2024](#challenge2024)
* [Challenge 2025](#challenge2025)
  * [Main Tracks](#maintracks)
  * [Evaluation Metrics](#evaluation2)

* [Publication](#publication)


## <span id="database">Database</span>
Our database is the first open-access respiratory sound database in the pediatric population, aged from 1 month to 18 years old. The respiratory sounds contained in the dataset were recorded at the pediatric respiratory department at Shanghai Children’s Medical Center (SCMC) using Yunting model II Stethoscopes. 

The recordings are saved in .wav format with naming rules as follows: Each name is composed of 5 elements separated with underscores, including the patient number, age, gender, the recording location, and the recording number of the participants.
1. Patient number (e.g., 65101170)
2. Age (e.g., 0.4)
3. Gender
    a. Male (0)
    b. Female (1)
4. Recording location 
    a. left posterior (p1)
    b. left lateral (p2)
    c. right posterior (p3)
    d. right lateral (p4)
5. Recording number (e.g., 3246)

The annotations at the record and event level are provided in this database. At the record level, each recording with poor signal quality was annotated as Poor Quality, while the recordings with high signal quality were annotated as Normal, CAS, DAS, or CAS & DAS according to the presence/absence of continuous/discontinuous adventitious respiratory sounds. At the event level, each recording was segmented into multiple respiratory events and annotated as Normal, Rhonchi, Wheeze, Stridor, Coarse Crackle, Fine Crackle, or Wheeze+Crackle. 

The annotation information of each recording is saved in .json format with the same filename, which contains the annotation at the record level and event level. The annotation at the record level is Normal, CAS, DAS, CAS & DAS, or Poor Quality. The annotation at event level consists of the start (ms) and the end (ms) of respiratory events, and the corresponding type of respiratory events (Normal, Rhonchi, Wheeze, Stridor, Coarse Crackle, Fine Crackle, Wheeze+Crackle).

An example of annotation file is as follow:

```json
{
    "recording_annotation": "Normal",
    "event_annotation": [
        {
            "start": 342, 
         	"end": 2515, 
            "type": "Normal"
        }, {
            "start": 2557, 
            "end": 3776, 
            "type": "Normal"
        }, {
            "start": 4547, 
            "end": 5651, 
            "type": "Normal"
        }, {
            "start": 6439, 
            "end": 8065, 
            "type": "Normal"
        }, {
            "start": 8363, 
            "end": 9201, 
            "type": "Normal"
        }
	]
}
```

## <span id="dataset-versions">Dataset Versions</span>

The SPRSound dataset is organized into different versions corresponding to each challenge year (2022, 2023, 2024, 2025). Each version contains the appropriate train/test splits for that year's challenge.

### Available Versions

- **Version 2022**: Initial release for BioCAS 2022 Challenge (Classification tasks)
- **Version 2023**: BioCAS 2023 Challenge release (Classification tasks)
- **Version 2024**: BioCAS 2024 Challenge release (Compression & Detection tracks)
- **Version 2025**: BioCAS 2025 Challenge release (Compression & Detection tracks)

### Creating a Release

To create a release package for a specific version, use the release creation script:

```bash
# Create a release for version 2024
python3 scripts/create_release.py --version 2024 --output_dir ./releases
```

This will create an organized release directory containing:
- All relevant train/validation/test splits for the specified version
- README.md, LICENSE, and other documentation
- Patient summary files
- Example files and scripts
- `version_info.json` with dataset statistics

### Directory Structure

The dataset is organized as follows:

```
SPRSound/
├── Classification/
│   ├── train_classification_wav/          # Training WAV files (all versions)
│   ├── train_classification_json/         # Training JSON annotations (all versions)
│   ├── valid_classification_wav/
│   │   ├── 2022/                          # 2022 validation set
│   │   └── 2023/                          # 2023 validation set
│   └── valid_classification_json/
│       ├── 2022/                          # 2022 validation annotations
│       └── 2023/                          # 2023 validation annotations
├── Detection/
│   ├── train_detection_wav/               # Training data
│   ├── train_detection_json/
│   ├── valid_detection_wav/               # Validation data
│   ├── valid_detection_json/
│   ├── test2024_detection_wav/            # 2024 test set
│   └── test2024_detection_json/
├── Compression/
│   ├── train_compression_wav/
│   ├── valid_compression_wav/
│   └── test2024_compression_wav/          # 2024 test set
└── ...
```

**Note**: You should organize your 2022 and 2023 validation splits manually in the `Classification/valid_classification_*/` directories before creating releases.

## <span id="past-challenges">Challenge 2022 & 2023</span>

### <span id="maintask">Main Tasks</span>

#### Task 1 (Respiratory Sound Classification at event Level)

Task 1-1 is a binary class classification challenge (Normal and Adventitious).

Task 1-2 is a multiclass classification challenge (Normal (N), Rhonchi (R), Wheeze (W), Stridor (S), Coarse Crackle (CC), Fine Crackle (FC), Wheeze & Crackle (WC)).

#### Task 2 (Respiratory Sound Classification at Record Level)

Task 2-1 is a ternary class classification challenge (Normal, Adventitious, and Poor Quality records).

Task 2-2 is a multiclass classification challenge (Normal (N), CAS (C), DAS (D), CAS & DAS (CD), or Poor Quality (PQ) records).

### <span id="evaluation1">Evaluation Metrics</span>

#### Sensitivity (SE)
#### Specificity (SP)
#### Average Score (AS)
#### Harmonic Score (HS)

## <span id="challenge2024">Challenge 2024</span>

### <span id="maintracks">Main Tracks</span>

#### Track 1 (Respiratory Recording Compression)

This track deals with respiratory recordings compression using compressive sensing-based compression methods.

#### Track 2 (Respiratory Event Detection)

This track deals with the detection of onsets and offsets in addition to the assignment of event labels of respiratory events in respiratory recordings using sound event detection methods.

### <span id="evaluation2">Evaluation Metrics</span>

#### Track1

##### Compression Ratio (CR)

##### Percent Root Mean Square Difference (PRD)

##### Correlation Coefficient (CC)

#### Track2

##### Event-based F-score (F)

##### Event-based Error Rate (ER)

## <span id="challenge2025">Challenge 2025</span>

### <span id="maintracks">Main Tracks</span>

#### Track 1 (Respiratory Recording Compression)

This track deals with respiratory recordings compression using compressive sensing-based compression methods.

#### Track 2 (Respiratory Event Detection)

This track deals with the detection of onsets and offsets in addition to the assignment of event labels of respiratory events in respiratory recordings using sound event detection methods.

### <span id="evaluation2">Evaluation Metrics</span>

#### Track1

##### Compression Ratio (CR)

##### Percent Root Mean Square Difference (PRD)

##### Correlation Coefficient (CC)

#### Track2

##### Event-based F-score (F)

##### Event-based Error Rate (ER)


## <span id="publication">Publication</span>

For use in publications and presentations, please cite this data collection as follows:
```
[Data] Q. Zhang, et al. “SPRSound: Open-Source SJTU Paediatric Respiratory Sound Database”, IEEE Transactions on Biomedical Circuits and Systems (TBioCAS), vol. 16, no. 5, pp. 867-881, Oct, 2022.
[Competition] Q. Zhang, et al. “Meta: Data Compression and Event Detection Grand Challenge 2024 With SPRSound Dataset”, IEEE Data Descriptions (DD), vol. 1, no. 1, pp. 1-8, Dec, 2024
[Competition] Q. Zhang, et al. “Grand Challenge on Respiratory Sound Classification for SPRSound Dataset II”, IEEE Biomedical Circuits and Systems Conference (BioCAS), pp. 1-5, Oct, 2023. 
[Competition] Q. Zhang, et al. “Grand Challenge on Respiratory Sound Classification”, IEEE Biomedical Circuits and Systems Conference (BioCAS), 2022, pp. 1-5.
```
