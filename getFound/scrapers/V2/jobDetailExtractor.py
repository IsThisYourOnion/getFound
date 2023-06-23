import os
import glob
import json
from linkedin_api import Linkedin
import params
class LinkedinJobScraper:
    def __init__(self, username, password, input_directory, output_directory):
        self.api = Linkedin(username, password)
        self.input_directory = input_directory
        self.output_directory = output_directory

    def get_job_ids(self):
        job_ids = []
        for file_name in glob.glob(os.path.join(self.input_directory, '*.txt')):
            with open(file_name, 'r') as file:
                for line in file:
                    job_id = line.strip()
                    job_ids.append(job_id)
        return job_ids

    def get_jobs(self, job_ids):
        for job_id in job_ids:
            job_data = self.api.get_job(job_id)
            self.save_as_json(job_id, job_data)

    def save_as_json(self, job_id, data):
        if not os.path.exists(self.output_directory):
            os.makedirs(self.output_directory)

        with open(f'{self.output_directory}/job_{job_id}.json', 'w') as json_file:
            json.dump(data, json_file)

# # Get the script's current directory
# current_directory = os.path.dirname(os.path.abspath(__file__))
#
# # Construct the input and output directory paths
# input_directory_path = os.path.join(current_directory, 'data/linkedin_hrefs/job_ids')
# output_directory_path = os.path.join(current_directory, 'data/linkedin_job_response_raw')
#
# # Instantiate the scraper with the constructed paths
# scraper = LinkedinJobScraper(params.email, params.password, input_directory_path, output_directory_path)
# job_ids = scraper.get_job_ids()
# scraper.get_jobs(job_ids)
