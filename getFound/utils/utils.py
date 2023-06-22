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

    @staticmethod
    def get_root_path():
        current_path = os.path.abspath(__file__)  # Get the absolute path of the current script
        root_path = os.path.dirname(current_path)  # Get the directory containing the current script
        base_project_dir = os.path.dirname(root_path)  # Get the directory one step above the root path
        return base_project_dir


# Usage
base_project_dir = JSONDataProcessor.get_root_path()
directory_path = os.path.join(base_project_dir, 'data', 'raw_data', 'linkedin_hrefs')

processor = JSONDataProcessor(directory_path)
all_data = processor.read_json_files()
flattened_list = list(chain.from_iterable(all_data))

