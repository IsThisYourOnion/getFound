import os
import re

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


# # Construct the directory path relative to the current script's location
# relative_directory_path = 'data/linkedin_hrefs'
# script_directory = os.path.dirname(os.path.abspath(__file__))
# directory_path = os.path.join(script_directory, relative_directory_path)
#
# # Using the class
# processor = ProcessJobIds(directory_path)
# processor.process()

