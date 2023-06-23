import requests
from bs4 import BeautifulSoup
import json
import threading
import os
import random
import string


class LinkedinUrlSkimmer:
    def __init__(self):
        self.base_url = 'https://www.linkedin.com/jobs/search/?currentJobId=3617085448&keywords={}&refresh=true'
        self.hrefs = set()
        self.lock = threading.Lock()

    def generate_random_filename(self, length=10):
        letters_and_digits = string.ascii_letters + string.digits
        return ''.join(random.choice(letters_and_digits) for i in range(length))

    def scrape(self, job_positions, iterations, num_threads):
        threads = []

        for position in job_positions:
            print(f"Scraping job position: {position}")

            current_base_url = self.base_url.format(position)

            for _ in range(iterations):
                if len(self.hrefs) >= 20000:
                    break

                url = self.generate_url(current_base_url)

                thread = threading.Thread(target=self.scrape_page, args=(url,))
                threads.append(thread)
                thread.start()

            for thread in threads:
                thread.join()

            self.print_results()
            self.write_to_json(position)

            # Reset hrefs for the next job position
            self.hrefs.clear()

    def generate_url(self, current_base_url):
        position = len(self.hrefs) % 25 + 1
        page_num = len(self.hrefs) // 25

        return f'{current_base_url}&start={page_num * 25}'

    def scrape_page(self, url):
        r = requests.get(url)
        r.encoding = 'utf-8'
        soup = BeautifulSoup(r.text, 'html.parser')

        links = soup.find_all('a', class_='base-card__full-link')

        for link in links:
            href = link.get('href')
            if href not in self.hrefs:
                with self.lock:
                    self.hrefs.add(href)

                if len(self.hrefs) % 1000 == 0:
                    print("1000th href captured:", href)

            if len(self.hrefs) >= 20000:
                break

    def print_results(self):
        print("Total unique hrefs captured:", len(self.hrefs))
        print("Last Position:", len(self.hrefs) % 25 + 1)
        print("Last Page Number:", len(self.hrefs) // 25)
        print("Last Href Added:", list(self.hrefs)[-1])

    def write_to_json(self, position):
        data = {
            'linkedin_urls': list(self.hrefs)
        }

        file_name = f'{self.generate_random_filename()}.json'
        write_dir = '/getFound/data/raw_data/href_data/linkedin/'

        with open(write_dir + file_name, 'w') as file:
            json.dump(data, file)


