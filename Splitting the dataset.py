import os
import random
import shutil
source_folder = 'ExtremeCountixAV/ExtremeCountixAV/Videos/Scale variation'

dataset_folder = 'train_dataset/CAV'
train_folder = os.path.join(dataset_folder, 'train')
test_folder = os.path.join(dataset_folder, 'test')
val_folder = os.path.join(dataset_folder, 'val')

os.makedirs(train_folder, exist_ok=True)
os.makedirs(test_folder, exist_ok=True)
os.makedirs(val_folder, exist_ok=True)

file_names = os.listdir(source_folder)

num_files = len(file_names)
num_train_files = int(num_files * 0.8)
num_val_files = int(num_files * 0.1)
num_test_files = num_files - num_train_files - num_val_files

random.shuffle(file_names)
for i, file_name in enumerate(file_names):
    source_path = os.path.join(source_folder, file_name)
    if i < num_train_files:
        destination_path = os.path.join(train_folder, file_name)
    elif i < num_train_files + num_val_files:
        destination_path = os.path.join(val_folder, file_name)
    else:
        destination_path = os.path.join(test_folder, file_name)

    shutil.move(source_path, destination_path)

print(
    f'Successfully split the dataset into: {num_train_files} files for training, {num_val_files} files for validation, {num_test_files} files for testing.')