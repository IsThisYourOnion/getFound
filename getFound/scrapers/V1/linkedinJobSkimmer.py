from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
import chromedriver_autoinstaller
import json

class LinkedinJobLinkSkimmer:
    def __init__(self, search_item, hrefs, driver):
        self.driver = driver
        self.search_item = search_item
        self.hrefs = hrefs
        self.duplicate_counter = 0

    def perform_search(self):
        self.search_position(self.search_item)
        print(f'Total HREFs collected: {len(self.hrefs)}')

    def search_position(self, search_item):
        position = search_item.replace(' ', "%20")
        self.driver.get(f"https://www.linkedin.com/jobs/search/?currentJobId=3642304035&keywords={position}&refresh=true&position=1&pageNum=0")

        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'main-content')))

        while True:
            last_height = self.driver.execute_script("return document.body.scrollHeight")

            self.extract_links_from_panels()

            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            WebDriverWait(self.driver, 10).until(lambda driver: self.driver.execute_script("return document.body.scrollHeight") > last_height)

            new_height = self.driver.execute_script("return document.body.scrollHeight")

            if new_height == last_height or self.duplicate_counter == 5:
                break

            last_height = new_height

            try:
                load_more_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'infinite-scroller__show-more-button')))
                load_more_button.click()
            except WebDriverException:
                pass

    def extract_links_from_panels(self):
        panel_container = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="main-content"]/section[2]')))
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
