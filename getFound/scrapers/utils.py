import os
import glob
import json
from itertools import chain


class JSONDataProcessor:
    def __init__(self, directory_path):
        self.directory_path = directory_path

    def read_json_files(self):
        file_path = os.path.join(self.directory_path, '*.json')
        json_files = glob.glob(file_path)

        all_data = []  # List to store all the data

        for file in json_files:
            with open(file, 'r') as f:
                data = json.load(f)
                json_values = list(data.values())  # Extract only the JSON values
                all_data.extend(json_values)  # Extend the list with the JSON values

        return all_data  # Return the collected JSON values list

#
#
# processor = JSONDataProcessor('/Users/adamkirstein/Code/getFound/getFound/data/raw_data/href_data/linkedin/')
# all_data = processor.read_json_files()
# flattened_list = list(chain.from_iterable(all_data))

