"""This scraper pulls hrefs from all job postings on url and saves them. output is fed into BS$/requests
- based scraper to obtain job descriptions."""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import ElementNotVisibleException
from bs4 import BeautifulSoup
import time
import chromedriver_autoinstaller
import json

class LinkedinJobLinkSkimmer:
    def __init__(self, search_items):
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1024, 600)
        self.driver.maximize_window()
        self.search_items = search_items
        self.hrefs = set()
        self.duplicate_counter = 0

    def perform_search(self):
        for search_item in self.search_items:
            self.search_position(search_item)

        print(f'Total HREFs collected: {len(self.hrefs)}')
        self.save_hrefs_to_json()

    def search_position(self, search_item):
        position = search_item.replace(' ', "%20")
        self.driver.get(f"https://www.linkedin.com/jobs/search/?currentJobId=3642304035&keywords={position}&refresh=true&position=1&pageNum=0")
        time.sleep(2)

        while True:
            last_height = self.driver.execute_script("return document.body.scrollHeight")

            while True:
                self.extract_links_from_panels()

                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)
                new_height = self.driver.execute_script("return document.body.scrollHeight")

                if new_height == last_height or self.duplicate_counter == 5:
                    break

                last_height = new_height

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
                    if self.duplicate_counter == 5:
                        break
                else:
                    self.duplicate_counter = 0

                if len(self.hrefs) % 100 == 0:
                    print(f'Total HREFs collected so far: {len(self.hrefs)}')

    def save_hrefs_to_json(self):
        with open('linkedin_hrefs.json', 'w') as f:
            json.dump(list(self.hrefs), f)

if __name__ == "__main__":
    chromedriver_autoinstaller.install()
    search_items = ['deep learning scientist', 'data scientist', 'AI engineer']
    scraper = LinkedinJobLinkSkimmer(search_items)
    scraper.perform_search()