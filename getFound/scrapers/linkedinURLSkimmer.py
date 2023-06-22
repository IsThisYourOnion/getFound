import requests
from bs4 import BeautifulSoup
import time
import json
import threading

class LinkedinUrlSkimmer:
    def __init__(self):
        self.base_url = 'https://www.linkedin.com/jobs/search/?currentJobId=3617085448&keywords=deep%20learning%20scientist&refresh=true'
        self.position_increment = 1
        self.page_increment = 1
        self.hrefs = set()
        self.lock = threading.Lock()

    def scrape(self, iterations, num_threads):
        threads = []

        for _ in range(iterations):
            url = self.generate_url()

            thread = threading.Thread(target=self.scrape_page, args=(url,))
            threads.append(thread)
            thread.start()

            self.increment_position()

            if len(threads) % 25 == 0:
                print("Total hrefs captured:", len(self.hrefs))

        for thread in threads:
            thread.join()

        self.print_results()
        self.write_to_json()

    def generate_url(self):
        position = len(self.hrefs) % 25 + 1
        page_num = len(self.hrefs) // 25

        return f'{self.base_url}&position={position}&pageNum={page_num}'

    def increment_position(self):
        if len(self.hrefs) % 25 == 0:
            self.page_increment += 1

        if len(self.hrefs) % (25 * self.page_increment) == 0:
            self.position_increment += 1

    def scrape_page(self, url):
        r = requests.get(url)
        r.encoding = 'utf-8'
        soup = BeautifulSoup(r.text, 'html.parser')

        links = soup.find_all('a', class_='base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2]')

        for link in links:
            href = link.get('href')
            if href not in self.hrefs:
                with self.lock:
                    self.hrefs.add(href)

    def print_results(self):
        print("Total unique hrefs captured:", len(self.hrefs))
        print("Last Position:", len(self.hrefs) % 25 + 1 - self.position_increment)
        print("Last Page Number:", len(self.hrefs) // 25)
        print("Last Href Added:", list(self.hrefs)[-1])

    def write_to_json(self):
        data = {
            'linkedin_urls': list(self.hrefs)
        }

        with open('/content/drive/MyDrive/linkedin_urls.json', 'w') as file:
            json.dump(data, file, indent=4)

        print("URLs written to 'linkedin_urls.json'.")


scraper = LinkedinUrlSkimmer()
scraper.scrape(20000, 8)  # Specify the number of iterations and number of threads
