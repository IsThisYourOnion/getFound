import re

# opens href files and extracts job ids for scraper.
class ProcessJobIds:
    def __init__(self, filepath):
        self.filepath = filepath
        self.job_ids = []
        self.pattern = re.compile(r'-?(\d{10})\?')

    def process(self):
        with open(self.filepath, 'r') as file:
            urls = file.read().splitlines()

        for url in urls:
            match = self.pattern.search(url)
            if match:
                self.job_ids.append(match.group(1)) # Note the change here

        return self.job_ids


# Using the class
processor = ProcessJobIds('')
job_ids = processor.process()
print(job_ids)


