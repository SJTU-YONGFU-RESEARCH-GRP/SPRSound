# An example for IEEE BioCAS 2023 Grand Challenge on Respiratory Sound Classification


# model training
python3 train.py --task 11 --wav_path ./wav --json_path ./json --model_path  ./models

# model validation
python3 mian.py --task            11
                --wav             ./wav
                --out             ./output/output.json

# Note that the output format and command line of the submitted model for model validation should be consistent with the example
