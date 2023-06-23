import os
import re
import os
import json
import datetime

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




class JsonProcessor:
    def __init__(self, input_directory, output_directory):
        self.input_directory = input_directory
        self.output_directory = output_directory
        # Create output directory if it doesn't exist
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

    def read_json_files(self):
        all_data = []
        for filename in os.listdir(self.input_directory):
            if filename.endswith('.json'):
                with open(os.path.join(self.input_directory, filename), 'r') as f:
                    data = json.load(f)
                    all_data.append(data)
        return all_data

    def extract_description_and_write(self, all_data):
        for i, data in enumerate(all_data):
            description_text = data['description']['text']
            # Get the current timestamp
            timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
            # Create a unique filename using the timestamp
            output_file_name = f'linked_raw_text_file{timestamp}.txt'
            output_file_path = os.path.join(self.output_directory, output_file_name)
            with open(output_file_path, 'w') as f:
                f.write(f'Description from JSON {i+1}: {description_text}\n')

    def process_files(self):
        data = self.read_json_files()
        self.extract_description_and_write(data)


def run_JsonProcessor():
    # Get the current directory
    current_directory = os.getcwd()

    # Define input and output directory paths
    input_directory_path = os.path.join(current_directory, 'getFound/scrapers/V2/data/linkedin_job_response_raw')
    output_directory_path = os.path.join(current_directory, 'getFound/data/raw_text')

    # Create an instance of JsonProcessor and process the files
    processor = JsonProcessor(input_directory_path, output_directory_path)
    processor.process_files()


