import json
import os
from itertools import chain

class JSONReader:
    def __init__(self, directory):
        self.directory = directory

    def read_json_files(self):
        # Get a list of all files in the directory
        file_list = os.listdir(self.directory)

        # Filter JSON files
        json_files = [file for file in file_list if file.endswith('.json')]

        # Initialize an empty list to store JSON contents
        json_data = []

        # Iterate over each JSON file and read its contents
        for file_name in json_files:
            file_path = os.path.join(self.directory, file_name)
            with open(file_path, 'r') as json_file:
                data = json.load(json_file)
                json_data.append(data)

        # Flatten the list of JSON data
        flattened_data = list(chain.from_iterable(json_data))

        # Return the flattened list of JSON data
        return flattened_data

