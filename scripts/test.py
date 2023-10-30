'''
Author: Qing Zhang
Date: 2023-04-01 16:46:15
Copyright (c) 2023 by Qing Zhang, All Rights Reserved. 
'''
import os
import argparse
import json
import scipy.io.wavfile as wav
import numpy as np
import pickle
import librosa

parser = argparse.ArgumentParser(description='Main')
parser.add_argument("--task", required=True, type=int, choices=[11, 12, 21, 22],
                    help="task")
parser.add_argument("--wav", default='./wav', type=str,
                    help="test wav file dir")
parser.add_argument("--out", default='./output/output.json', type=str,
                    help="output json dir")
args = parser.parse_args()


task_11_dict = {
    0: "Normal",
    1: "Adventitious"
}

task_12_dict = {
    0: "Normal",
    1: "Rhonchi",
    2: "Wheeze",
    3: "Stridor",
    4: "Coarse Crackle",
    5: "Fine Crackle",
    6: "Wheeze & Crackle"
}

task_21_dict = {
    0: "Normal",
    1: "Poor Quality",
    2: "Adventitious"
}

task_22_dict = {
    0: "Normal",
    1: "Poor Quality",
    2: "CAS",
    3: "DAS",
    4: "CAS & DAS"
}

def MFCC(fs, sig, num = 40):
    mfcc = librosa.feature.mfcc(sig, fs, n_mfcc = num)
    mfcc = np.mean(mfcc, axis=1)
    # print("mfcc", mfcc,mfcc.shape) 
    return mfcc

def load_test_data(data_path):
    file_names = []
    for wav_file in os.listdir(data_path):
        if wav_file.endswith('.wav'):
            file_names.append(wav_file)
    
    datas = []
    for file in file_names:
        fs, sig = wav.read(os.path.join(data_path, file))
        sig = sig.astype('float')
        feature = MFCC(fs, sig)
        datas.append(feature)

    return datas, file_names

def write_to_json(predictions, names, path, task):

    if task == 11:
        task_dict = task_11_dict
    if task == 12:
        task_dict = task_12_dict
    if task == 21:
        task_dict = task_21_dict
    if task == 22:
        task_dict = task_22_dict
        
    with open(path, 'w') as outfile:
        json_string = {}
        for i in range(len(predictions)):
            text_result = task_dict[predictions[i]]
            json_string[names[i]] = text_result   
        json.dump(json_string, outfile, ensure_ascii=False, indent=4)

def eval(task, data):
    # load model
    model_name= "./models/task_" + str(task) + ".pkl"
    f = open(model_name, 'rb')
    s = f.read()
    model = pickle.loads(s)
    # prediction
    predictions = model.predict(data)
    return predictions


if __name__ == "__main__":
    # load test data
    data, file_names = load_test_data(args.wav)

    # prediction
    predictions = eval(args.task, data)

    # output
    write_to_json(predictions, file_names, args.out, args.task)



