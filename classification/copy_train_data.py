import csv

import os
import shutil
import sys

source_directory = 'fairface_original/fairface-img-margin125-trainval'
destination_directory = 'fairface_clean/train'

race_list = ['east_asian', 'indian', 'black', 'white', 'middle_eastern', 'latino_hispanic', 'southeast_asian']

new_dict = {race: [] for race in race_list}
#print(str(new_dict))

with open('fairface_original/fairface_label_train.csv') as f:
    csvreader = csv.reader(f, delimiter=',')
    line_count = 0
    for line in csvreader:
        file_name = line[0]
        race = line[3].lower().replace(' ','_')
        if line_count < 10:
            print(f"detected line from labels file. {file_name=}, {race=}")
        if race in new_dict:
            new_dict[race].append(file_name)
        line_count += 1
    
    for race, list_of_files in new_dict.items():
        print(f"{race=}, size of the list = {len(list_of_files)}")
        file_count = 0

        for file_info in new_dict[race]:
            destination_race_directory = os.path.join(destination_directory, race)
            os.makedirs(destination_race_directory, exist_ok=True) 
            if file_count <= 100:
                print(f"{file_info=}")
                only_filename = file_info.split('/')[1]
                source_file = os.path.join(source_directory, file_info)
                destination_file = os.path.join(destination_race_directory, only_filename)
                # print(f"will try to copy from: {source_file}")
                # print(f"to:                    {destination_file}")
                shutil.copyfile(source_file, destination_file)
                file_count += 1
                # print("Train images copied.")
            else:
                break
        print(f"Done with {race} class")


# print(str(new_dict))