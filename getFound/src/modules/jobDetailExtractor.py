from linkedin_api import Linkedin
from getFound.src.utils.utils import DataManager
import re
from getFound.src.config import params

class JobManager:
    def __init__(self, email, password, manager=None):
        self.api = Linkedin(email, password)
        self.manager = DataManager() if manager is None else manager
        self.job_ids = []
        self.pattern = re.compile(r'-?(\d{10})\?')

    def read_data(self, filename, filetype, data_has_header=False):
        job_links = self.manager.read_data(filename, filetype, data_has_header)
        for url in job_links:
            match = self.pattern.search(url)
            if match:
                self.job_ids.append(match.group(1))

    def fetch_and_write_job_data(self, dirname):
        for job in self.job_ids:
            profile = self.api.get_job(job)
            file_name = f'job_{job}'
            self.manager.write_data(dirname, file_name, 'json', profile)

def runJobManager():
    job_manager = JobManager(params.email, params.password)
    job_manager.read_data('linkedin_hrefs', 'txt', True)
    job_manager.fetch_and_write_job_data('linked_job_data')
