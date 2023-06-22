from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import json
import chromedriver_autoinstaller
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LinkedInJobScraper:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.driver = None

    def setup_driver(self):
        options = Options()
        chromedriver_autoinstaller.install()
        # options.add_argument("--headless")  # Run Chrome in headless mode
        # options.add_argument("--disable-dev-shm-usage")
        # options.add_argument("--no-sandbox")
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()

    def login(self):
        self.driver.get('https://www.linkedin.com/login')
        time.sleep(2)
        self.driver.find_element(By.ID, 'username').send_keys(self.email)
        self.driver.find_element(By.ID, 'password').send_keys(self.password)
        self.driver.find_element(By.ID, 'password').send_keys(Keys.RETURN)
        time.sleep(60)

    def scroll_to_bottom(self):
        last_height = self.driver.execute_script('return document.body.scrollHeight')
        while True:
            self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'jobs-search-results__list-item')))
            new_height = self.driver.execute_script('return document.body.scrollHeight')
            if new_height == last_height:
                break
            last_height = new_height
            time.sleep(1)
        time.sleep(20)

    def scrape_jobs(self, positions):
        for search in positions:
            position = search.replace(' ', "%20")
            counter = 0

            self.driver.get(f"https://www.linkedin.com/jobs/search/?currentJobId=3535505410&keywords={position}&refresh=true")

            job_counter = 0
            while True:
                jobs_lists = self.driver.find_element(By.CLASS_NAME, 'scaffold-layout__list-container')
                jobs = jobs_lists.find_elements(By.CLASS_NAME, 'jobs-search-results__list-item')

                for job in jobs:
                    job_title = job.find_element(By.CLASS_NAME, 'job-card-list__title').text
                    job_title = job_title.replace(" ", "_")
                    job.click()
                    time.sleep(1)
                    job_desc = self.driver.find_element(By.ID, 'job-details')
                    job_soup = BeautifulSoup(job_desc.get_attribute('outerHTML'), 'html.parser')
                    soup_text = job_soup.get_text().strip()

                    output = {
                        'job_title': job_title,
                        'description': soup_text
                    }

                    json_output = json.dumps(output)
                    # Write JSON data to a file
                    filename = f"testdata/file_{counter}.json"
                    with open(filename, 'w') as file:
                        file.write(json_output)
                    counter += 1

                    job_counter += 1
                    if job_counter % 5 == 0:
                        self.scroll_a_bit()

                try:
                    next_page_button = self.driver.find_element(By.CLASS_NAME, 'artdeco-pagination__button--next')
                    next_page_button.click()
                    time.sleep(1)
                except:
                    break

    def scroll_a_bit(self):
        self.driver.execute_script("window.scrollBy(0, 200);")
        time.sleep(1)

    def close(self):
        self.driver.quit()


# Usage example:
params = {"email": "adkstein@gmail.com",
          "password": "RyEGrP3kVmPyCpH84HA"}

positions = ['deep learning scientist', 'data engineer', 'machine learning engineer']

scraper = LinkedInJobScraper(params['email'], params['password'])
scraper.setup_driver()
scraper.login()
scraper.scrape_jobs(positions)
scraper.close()
