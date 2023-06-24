from linkedin_api import Linkedin
from getFound.src.utils.utils import DataManager
import re
from getFound.src.config import params

class JobManager:
    def __init__(self, email, password):
        self.manager = DataManager()
        self.api = Linkedin(email, password)

    def clean_job_ids(self, job_links):
        pattern = re.compile(r'-?(\d{10})\?')
        flattened_list = [element for sublist in job_links for element in sublist]
        job_ids = []
        for url in flattened_list:
            match = pattern.search(url)
            if match:
                job_ids.append(match.group(1))
        return job_ids

    def pull_linkedin_data(self, job_ids):
        for job in job_ids:
            profile = self.api.get_job(job)
            file_name = f'job_{job}'
            self.manager.write_data('linked_job_data', file_name, 'json', profile)


def runJobManager():
    # Usage example:
    email = params.email
    password = params.password
    linkedin_manager = JobManager(email, password)
    job_links = linkedin_manager.manager.read_data('linkedin_hrefs', 'txt', True)
    cleaned_ids = linkedin_manager.clean_job_ids(job_links)
    linkedin_manager.pull_linkedin_data(cleaned_ids)

