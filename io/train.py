'''
Author: Qing Zhang
Date: 2023-04-01 15:34:15
Copyright (c) 2023 by Qing Zhang, All Rights Reserved. 
'''
import argparse
import os
import numpy as np
import json
import scipy.io.wavfile as wav
import librosa
from sklearn.multiclass import OneVsRestClassifier
from sklearn import svm
import pickle


parser = argparse.ArgumentParser(description='Main')
parser.add_argument("--task", required=True, type=int, choices=[11, 12, 21, 22],
                    help="task")
parser.add_argument("--wav_path", default='./wav', type=str,
                    help="input wav path")
parser.add_argument("--json_path", default='./json', type=str,
                    help="input json dictionary")
parser.add_argument("--model_path", default='./models', type=str,
                    help="output model dictionary")
args = parser.parse_args()
if not os.path.exists(args.model_path):
    os.makedirs(args.model_path)

task_11_dict = {'Normal': 0,
                'Rhonchi': 1,
                'Wheeze': 1,
                'Stridor': 1,
                'Coarse Crackle': 1,
                'Fine Crackle': 1,
                'Wheeze+Crackle': 1}

task_12_dict = {'Normal': 0,
               'Rhonchi': 1,
               'Wheeze': 2,
               'Stridor': 3,
               'Coarse Crackle': 4,
               'Fine Crackle': 5,
               'Wheeze+Crackle': 6}

task_21_dict = {'Normal': 0,
                'Poor Quality': 1,
                'CAS': 2,
                'DAS': 2,
                'CAS & DAS': 2}

task_22_dict  = {'Normal': 0,
                'Poor Quality': 1,
                'CAS': 2,
                'DAS': 3,
                'CAS & DAS': 4}

def sparse_json(file_name, level):
    with open(file_name, 'r') as f:
        data = json.load(f)

    if level == "recording":
        record_label = data["record_annotation"]
        return record_label

    elif level == "event":
        events = data["event_annotation"]
        event_labels = []
        starts = []
        ends = []
        for event in events:
            label = event["type"]
            if int(event['end']) > int(event['start']):
                event_labels.append(label)
                starts.append(int(event['start']))
                ends.append(int(event['end']))
        return event_labels, starts, ends

def MFCC(fs, sig, num = 40):
    mfcc = librosa.feature.mfcc(sig, fs, n_mfcc = num)
    mfcc = np.mean(mfcc, axis=1)
    # print("mfcc", mfcc,mfcc.shape) 
    return mfcc

def load_recording_dataset(wav_path, json_path):
    datas = []
    labels = []
    json_files = os.listdir(json_path)
    for i in json_files:
        label = sparse_json(os.path.join(json_path, i), level = "recording")
        file_name = i.rsplit(".json", 1)[0]
        fs, sig = wav.read(os.path.join(wav_path, file_name + ".wav"))
        sig = sig.astype('float')
        feature = MFCC(fs, sig)
        datas.append(feature)
        labels.append(label)

    return datas, labels

def load_event_dataset(wav_path, json_path):
    datas = []
    labels = []
    json_files = os.listdir(json_path)
    for i in json_files:
        event_labels, starts, ends = sparse_json(os.path.join(json_path, i), level = "event")
        file_name = i.rsplit(".json", 1)[0]
        fs, sig = wav.read(os.path.join(wav_path, file_name + ".wav"))
        for j in range(len(event_labels)):
            event = sig [int(starts[j] * fs / 1000) : int(ends[j] * fs / 1000)]
            feature =MFCC(fs, event)
            labels.append(event_labels[j])
            datas.append(feature)
    return datas, labels

def dataset(wav_path, json_path, task):
    if task == 21:
        datas, labels = load_recording_dataset(wav_path, json_path)
        labels = [task_21_dict[x] for x in labels]
    elif task == 22:
        datas, labels = load_recording_dataset(wav_path, json_path)
        labels = [task_22_dict[x] for x in labels]
    elif task == 11:
        datas, labels = load_event_dataset(wav_path, json_path)
        labels = [task_11_dict[x] for x in labels]
    elif task == 12:
        datas, labels = load_event_dataset(wav_path, json_path)
        labels = [task_12_dict[x] for x in labels]

    labels = np.array(labels)
    datas = np.array(datas)
    return datas, labels

def save_model(model, model_name):
    s = pickle.dumps(model)
    f = open(model_name, "wb+")
    f.write(s)
    f.close()

if __name__ == "__main__":
    # load dataset
    X_train, y_train = dataset(args.wav_path, args.json_path, args.task)

    # train
    model = OneVsRestClassifier(svm.SVC(kernel='poly', C = 2, random_state=0))  
    model.fit(X_train, y_train)

    # save the model
    model_name = os.path.join(args.model_path , "task_" + str(args.task) + ".pkl")
    save_model(model, model_name)
