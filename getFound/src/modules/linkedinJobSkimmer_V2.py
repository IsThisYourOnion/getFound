from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotVisibleException
import time
import re
import os
from getFound.src.config import params
import chromedriver_autoinstaller
from multiprocessing import Pool
from joblib import Parallel, delayed

class LinkedinJobLinkSkimmer:
    def __init__(self, search_item):
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1024, 600)
        self.driver.maximize_window()
        self.search_item = search_item
        self.hrefs = set()
        self.duplicate_counter = 0

    def perform_search(self):
        self.search_position(self.search_item)
        self.save_hrefs_to_txt()
        self.hrefs.clear()

    def search_position(self, search_item):
        position = search_item.replace(' ', "%20")
        self.driver.get(
            f"https://www.linkedin.com/jobs/search?keywords={position}&location=United%20States&geoId=103644278&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0")
        time.sleep(2)

        while len(self.hrefs) < params.num_jobs: # change in params.py
            self.scroll_and_extract_links()
            if len(self.hrefs) >= params.num_jobs:
                break
            self.load_more_jobs()

    def scroll_and_extract_links(self):
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        while True:
            self.extract_links_from_panels()
            if len(self.hrefs) >= params.num_jobs:
                break
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height or self.duplicate_counter == 5:
                break
            last_height = new_height

    def load_more_jobs(self):
        try:
            load_more_button = self.driver.find_element(By.CLASS_NAME, 'infinite-scroller__show-more-button')
            if load_more_button.is_displayed():
                load_more_button.click()
                time.sleep(2)
        except ElementNotVisibleException:
            pass

    def extract_links_from_panels(self):
        panel_container = self.driver.find_element(By.XPATH, '//*[@id="main-content"]/section[2]')
        panels = panel_container.find_elements(By.TAG_NAME, 'a')
        for panel in panels:
            href = panel.get_attribute("href")
            if "https://www.linkedin.com/company/" not in href:
                initial_size = len(self.hrefs)
                self.hrefs.add(href)
                final_size = len(self.hrefs)
                if initial_size == final_size:
                    self.duplicate_counter += 1
                else:
                    self.duplicate_counter = 0
                if len(self.hrefs) >= params.num_jobs:
                    break

    def save_hrefs_to_txt(self):
        current_file_path = os.path.abspath(__file__)
        project_directory = os.path.dirname(os.path.dirname(current_file_path))
        data_directory = os.path.join(os.path.dirname(project_directory), "data")
        directory = os.path.join(data_directory, "linkedin_hrefs")

        # Create the directory if it doesn't exist
        if not os.path.exists(directory):
            os.makedirs(directory)

        filename = re.sub('[^a-zA-Z0-9 \n\.]', '', self.search_item)
        filename = f'{filename}_{int(time.time())}.txt'
        filepath = os.path.join(directory, filename)

        with open(filepath, 'w') as f:
            for href in self.hrefs:
                f.write("%s\n" % href)

def collect_job_links(search_item):
    chromedriver_autoinstaller.install()
    link_skimmer = LinkedinJobLinkSkimmer(search_item)

    try:
        link_skimmer.perform_search()
        print(f'Successfully finished collecting job links. Data stored.\n')
    except Exception as e:
        print(f'An error occurred while collecting links: {e}\n')

def main_job_links():
    search_items = params.search_terms
    Parallel(n_jobs=-1)(delayed(collect_job_links)(item) for item in search_items)

