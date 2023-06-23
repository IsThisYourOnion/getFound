from linkedInScraper import LinkedInScraper
from linkedinJobSkimmer import LinkedinJobLinkSkimmer
from utils import JSONReader
from itertools import chain
from multiprocessing import Pool, Manager
import chromedriver_autoinstaller
import json
import os
from selenium import webdriver


def worker(search_item, hrefs):
    # Each process should have its own webdriver instance
    driver = webdriver.Chrome()
    driver.set_window_size(1024, 600)
    driver.maximize_window()

    scraper = LinkedinJobLinkSkimmer(search_item, hrefs, driver)
    scraper.perform_search()

    driver.quit()


def main():
    chromedriver_autoinstaller.install()
    search_items = ['deep learning scientist', 'data scientist', 'AI engineer', 'machine learning engineer']

    driver = webdriver.Chrome()
    driver.set_window_size(1024, 600)
    driver.maximize_window()

    hrefs = []  # just a regular list, no need for Manager

    for item in search_items:
        scraper = LinkedinJobLinkSkimmer(item, hrefs, driver)
        scraper.perform_search()

    # Save hrefs to json
    with open('/getFound/data/raw_data/href_data/linkedin/linkedin_hrefs.json', 'w') as f:
        json.dump(hrefs, f)

    driver.quit()

    # Directory path
    directory = '/Users/adamkirstein/Code/getFound/getFound/data/raw_data/href_data/linkedin/'

    # # Create an instance of JSONReader
    # json_reader = JSONReader(directory)
    #
    # # Call the read_json_files() method to obtain the flattened list of JSON data
    # json_data_list = json_reader.read_json_files()
    # scraper = LinkedInScraper(json_data_list)
    # scraper.scrape_all()


if __name__ == "__main__":
    main()
