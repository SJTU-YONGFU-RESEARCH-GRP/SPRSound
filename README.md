# SPRSound: Open-Source SJTU Paediatric Respiratory Sound Database

This repository contains the released respiratory sound database for IEEE BioCAS 2022 Grand Challenge on Respiratory Sound Classification. Please refer to this link (http://1.117.17.41:9999/) for more information about the challenge.

<!-- TABLE OF CONTENTS -->
## Table of Contents

* [Database](#database)
* [Main Tasks](#maintask)
* [Evaluation Metrics](#evaluation)
* [Publication](#publication)


## <span id="database">Database</span>
Our database is the first open access respiratory sound database in the pediatric population, aging from 1 month to 18 years old. The respiratory sounds contained in the dataset were recorded at the pediatric respiratory department at Shanghai Children’s Medical Center (SCMC) using Yunting model II Stethoscopes. 

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

The annotations at the record and event level are provided in this database. At the record level, each recording with poor signal quality was annotated as Poor Quality, while the recordings with high signal quality were annotated as Normal, CAS, DAS, or CAS & DAS according to the presence/absence of continuous/discontinuous adventitious respiratory sounds. At the event level, each recording was segmented into multiple respiratory event and annotated as Normal, Rhonchi, Wheeze, Stridor, Coarse Crackle, Fine Crackle, or Wheeze+Crackle. 

The annotation information of each recording is saved in .json format with the same filename, which contains the annotation at record level and event level. The annotation at record level is Normal, CAS, DAS, CAS & DAS or Poor Quality. The annotation at event level consists of the start (ms) and the end (ms) of respiratory events, and the corresponding type of respiratory events (Normal, Rhonchi, Wheeze, Stridor, Coarse Crackle, Fine Crackle, Wheeze+Crackle).

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


## <span id="maintask">Main Tasks</span>

### Task 1 (Respiratory Sound Classification at event Level)

Task 1-1 is a binary class classification challenge (Normal and Adventitious).

Task 1-2 is a multiclass classification challenge (Normal (N), Rhonchi (R), Wheeze (W), Stridor (S), Coarse Crackle (CC), Fine Crackle (FC), Wheeze & Crackle (WC)).

### Task 2 (Respiratory Sound Classification at Record Level)

Task 2-1 is a ternary class classification challenge (Normal, Adventitious, and Poor Quality records).

Task 2-2 is a multiclass clasification challenge (Normal (N), CAS (C), DAS (D), CAS & DAS (CD), or Poor Quality (PQ) records).

## <span id="evaluation">Evaluation Metrics</span>
### Sensitivity (SE)
### Specificity (SP)
### Average Score (AS)
### Harmonic Score (HS)


## <span id="publication">Publication</span>

For use in publications and presentations please cite this data collection as follows:
```
Q. Zhang, et al. “SPRSound: Open-Source SJTU Paediatric Respiratory Sound Database”, IEEE Transactions on Biomedical Circuits and Systems (TBioCAS), pp. 1-13, 2022, early access.
Q. Zhang, et al. “Grand Challenge on Respiratory Sound Classification”, IEEE Biomedical Circuits and Systems Conference (BioCAS), 2022, pp. 1-5.
```
