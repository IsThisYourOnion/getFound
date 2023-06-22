import requests
from bs4 import BeautifulSoup
import time
import json
import threading

class LinkedinUrlSkimmer:
    def __init__(self):
        self.base_url = 'https://www.linkedin.com/jobs/search/?currentJobId=3617085448&keywords={}&refresh=true'
        self.position_increment = 1
        self.page_increment = 1
        self.hrefs = set()
        self.lock = threading.Lock()

    def scrape(self, job_positions, iterations, num_threads):
        threads = []

        for position in job_positions:
            print(f"Scraping job position: {position}")

            self.base_url = self.base_url.format(position)

            for _ in range(iterations):
                if len(self.hrefs) >= 20000:
                    break

                url = self.generate_url()

                thread = threading.Thread(target=self.scrape_page, args=(url,))
                threads.append(thread)
                thread.start()

                self.increment_position()

            for thread in threads:
                thread.join()

            self.print_results()
            self.write_to_json(position)

            # Reset hrefs for the next job position
            self.hrefs.clear()

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

                if len(self.hrefs) % 1000 == 0:
                    print("1000th href captured:", href)

            if len(self.hrefs) >= 20000:
                break

    def print_results(self):
        print("Total unique hrefs captured:", len(self.hrefs))
        print("Last Position:", len(self.hrefs) % 25 + 1 - self.position_increment)
        print("Last Page Number:", len(self.hrefs) // 25)
        print("Last Href Added:", list(self.hrefs)[-1])

    def write_to_json(self, position):
        data = {
            'linkedin_urls': list(self.hrefs)
        }

        file_path = f'getFound/data/raw_data/linkedin_hrefs/{position.replace(" ", "_")}_linkedin_urls.json'

        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)

        print(f"URLs written to '{file_path}'.")


scraper = LinkedinUrlSkimmer()
job_positions = ['deep learning scientist', 'data scientist', 'machine learning engineer']
scraper.scrape(job_positions, 20000, 8)  # Specify the job positions, number of iterations, and number of threads
