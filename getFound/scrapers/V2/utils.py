import os
import re
import os
import json
import datetime
import glob
import json

# Opens href files, extracts job IDs, and stores them as individual text files.
class ProcessJobIds:
    def __init__(self, directory_path):
        self.directory_path = directory_path
        self.job_ids = []
        self.pattern = re.compile(r'-?(\d{10})\?')

    def process(self):
        # Create the 'job_ids' subdirectory if it doesn't exist
        job_ids_directory = os.path.join(self.directory_path, 'job_ids')
        os.makedirs(job_ids_directory, exist_ok=True)

        file_names = os.listdir(self.directory_path)
        for file_name in file_names:
            if file_name != 'job_ids' and not os.path.isdir(file_name):
                file_path = os.path.join(self.directory_path, file_name)
                with open(file_path, 'r') as file:
                    urls = file.read().splitlines()

                job_ids = []
                for url in urls:
                    match = self.pattern.search(url)
                    if match:
                        job_ids.append(match.group(1))

                # Store the extracted job IDs in a text file with the same name as the input file
                output_file_path = os.path.join(job_ids_directory, f"{file_name}")
                with open(output_file_path, 'w') as output_file:
                    output_file.write('\n'.join(job_ids))

                self.job_ids.extend(job_ids)

        return self.job_ids


class JSONProcessor:
    def __init__(self, input_dir, output_dir):
        self.input_dir = input_dir
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)

    def read_json_files(self):
        json_files = glob.glob(self.input_dir + '/*.json')
        data = []

        for js in json_files:
            with open(js) as json_file:
                data.append(json.load(json_file))

        return data

    def extract_description_and_write(self, data):
        for i, item in enumerate(data):
            try:
                description_text = item['description']['text']
                timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')
                with open(f"{self.output_dir}/description_{timestamp}.txt", "w") as f:
                    f.write(description_text)
            except KeyError:
                print(f"KeyError: 'description' or 'text' not found in item {i}")

    def process(self):
        data = self.read_json_files()
        self.extract_description_and_write(data)

def run_JsonProcessor():
    # Use the class
    processor = JSONProcessor('data/linkedin_job_response_raw', 'data/raw_text_files')
    processor.process()
