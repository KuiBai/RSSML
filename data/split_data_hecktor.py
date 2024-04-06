import pickle
import random
import pandas as pd
import json

bb_csv_path = r"../hecktor2022_clinical_info_training.csv"  # Introduce CSV files here
bb = pd.read_csv(bb_csv_path)
patientID_list = list(bb.PatientID)

# Divide the data set to a ratio of 7: 1: 2
train_ratio = 0.7
val_ratio = 0.1
test_ratio = 0.2

train_size = int(len(patientID_list) * train_ratio)
val_size = int(len(patientID_list) * val_ratio)
test_size = len(patientID_list) - train_size - val_size

random.shuffle(patientID_list)
train_patient_list = patientID_list[:train_size]
val_patient_list = patientID_list[train_size:train_size + val_size]
test_patient_list = patientID_list[train_size + val_size:]

dicts = {'train': train_patient_list, 'val': val_patient_list, 'test': test_patient_list}

save_split_path = r"../data/split_1.pkl"

with open(save_split_path, 'w', encoding='utf-8') as f:
    json.dump(dicts, f)

with open(save_split_path, 'r', encoding='utf-8') as f:
    out = json.load(f)

print(out)

