from linkedin_api import Linkedin
from getFound.src.utils.utils import DataManager
import re
from getFound.src.config import params
from concurrent.futures import ThreadPoolExecutor
import time

class JobManager:
    def __init__(self, email, password, max_workers=10):
        self.manager = DataManager()
        self.api = Linkedin(email, password)
        self.max_workers = max_workers

    def clean_job_ids(self, job_links):
        pattern = re.compile(r'-?(\d{10})\?')
        flattened_list = [element for sublist in job_links for element in sublist]
        job_ids = []
        for url in flattened_list:
            match = pattern.search(url)
            if match:
                job_ids.append(match.group(1))
        return job_ids

    def _get_and_write_job_data(self, job):
        profile = self.api.get_job(job)
        file_name = f'job_{job}'
        self.manager.write_data('linked_job_data', file_name, 'json', profile)

    def pull_linkedin_data(self, job_ids):
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            executor.map(self._get_and_write_job_data, job_ids)

def runJobManager():
    # Usage example:
    email = params.email
    password = params.password
    linkedin_manager = JobManager(email, password)
    job_links = linkedin_manager.manager.read_data('linkedin_hrefs', 'txt', True)
    cleaned_ids = linkedin_manager.clean_job_ids(job_links)
    linkedin_manager.pull_linkedin_data(cleaned_ids)

