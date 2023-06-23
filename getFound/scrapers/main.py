from linkedInScraper import LinkedInScraper
from linkedinJobSkimmer import worker
from utils import JSONReader
import os
from itertools import chain
from multiprocessing import Pool, Manager
import chromedriver_autoinstaller
import json


def main():
    chromedriver_autoinstaller.install()
    search_items = ['deep learning scientist', 'data scientist', 'AI engineer']
    manager = Manager()
    hrefs = manager.list()  # shared list across processes
    with Pool() as pool:
        pool.starmap(worker, [(item, hrefs) for item in search_items])
    # Save hrefs to json
    with open('/Users/adamkirstein/Code/getFound/getFound/data/raw_data/href_data/linkedin/linkedin_hrefs.json',
              'w') as f:
        json.dump(list(hrefs), f)

    # Directory path
    directory = '/Users/adamkirstein/Code/getFound/getFound/data/raw_data/href_data/linkedin/'

    # Create an instance of JSONReader
    json_reader = JSONReader(directory)

    # Call the read_json_files() method to obtain the flattened list of JSON data
    json_data_list = json_reader.read_json_files()
    scraper = LinkedInScraper(json_data_list)
    scraper.scrape_all()


if __name__ == "__main__":
    main()
