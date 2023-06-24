from getFound.src.utils.utils import DataManager
import time


class JobProcessor:
    def __init__(self):
        self.manager = DataManager()

    def read_job_data(self, file_type='json', is_path=False):
        self.job_data = self.manager.read_data('linked_job_data', file_type, is_path)
        return self.job_data

    def write_job_description(self, data_dir='raw_job_text', file_type='txt'):
        for job_json in self.job_data:
            description = job_json['description']['text']
            # Just choosing timestamp as placeholder file names
            file_name = str(time.time())
            self.manager.write_data(data_dir, file_name, file_type, description)


def runJobProcessor():
    # Using the class
    job_processor = JobProcessor()
    job_processor.read_job_data()
    job_processor.write_job_description()

