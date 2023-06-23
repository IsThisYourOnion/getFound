from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import ElementNotVisibleException
from bs4 import BeautifulSoup
from multiprocessing import Pool, Manager
import time
import chromedriver_autoinstaller
import json

class LinkedinJobLinkSkimmer:
    def __init__(self, search_item, hrefs):
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1024, 600)
        self.driver.maximize_window()
        self.search_item = search_item
        self.hrefs = hrefs
        self.duplicate_counter = 0

    def perform_search(self):
        self.search_position(self.search_item)
        print(f'Total HREFs collected: {len(self.hrefs)}')

    def search_position(self, search_item):
        position = search_item.replace(' ', "%20")
        self.driver.get(f"https://www.linkedin.com/jobs/search/?currentJobId=3642304035&keywords={position}&refresh=true&position=1&pageNum=0")
        time.sleep(2)

        while True:
            last_height = self.driver.execute_script("return document.body.scrollHeight")

            self.extract_links_from_panels()

            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)  # throttle
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
                if href not in self.hrefs:
                    self.hrefs.append(href)
                    self.duplicate_counter = 0
                else:
                    self.duplicate_counter += 1
                    if self.duplicate_counter == 5:
                        break

                if len(self.hrefs) % 100 == 0:
                    print(f'Total HREFs collected so far: {len(self.hrefs)}')

def worker(search_item, hrefs):
    scraper = LinkedinJobLinkSkimmer(search_item, hrefs)
    scraper.perform_search()

if __name__ == "__main__":
    chromedriver_autoinstaller.install()
    search_items = ['deep learning scientist', 'data scientist', 'AI engineer', 'machine learning engineer']

    manager = Manager()
    hrefs = manager.list()  # shared list across processes

    with Pool() as pool:
        pool.starmap(worker, [(item, hrefs) for item in search_items])

    # Save hrefs to json

    # Save hrefs to json
    with open('/getFound/data/raw_data/href_data/linkedin/linkedin_hrefs.json', 'w') as f:
        json.dump(list(hrefs), f)
