import requests
from bs4 import BeautifulSoup
import json
import os
from concurrent.futures import ThreadPoolExecutor

def read_json_files(directory):
    json_data = []
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r') as file:
                try:
                    data = json.load(file)
                    json_data.append(data)
                except json.JSONDecodeError:
                    print(f"Error decoding JSON file: {file_path}")
    return json_data

class LinkedInScraper:
    def __init__(self, hrefs, directory='testdata/linkedin_descriptions'):
        self.hrefs = hrefs
        self.directory = directory
        os.makedirs(directory, exist_ok=True)

    def scrape_url(self, href):
        try:
            # Make a request to the website
            r = requests.get(href)
            r.encoding = 'utf-8'

            # Create an instance of the BeautifulSoup class to parse the page
            soup = BeautifulSoup(r.text, 'html.parser')
            element = soup.select_one('.show-more-less-html__markup.relative.overflow-hidden.show-more-less-html__markup--clamp-after-5')
            if element:
                text = element.get_text()

                # save the data to a json file
                filename = os.path.join(self.directory, f'linkedin_description_{self.hrefs.index(href)}.json')
                with open(filename, 'w', encoding='utf-8') as f:
                    json.dump({href: text}, f, ensure_ascii=False, indent=4)
            else:
                print(f'No element found for URL {href}')
        except Exception as e:
            print(f'Error occurred for URL {href}: {e}')

    def scrape_all(self):
        with ThreadPoolExecutor() as executor:
            executor.map(self.scrape_url, self.hrefs)


# list of hrefs
hrefs = read_json_files('getFound/data/raw_data/linkedin_hrefs')

scraper = LinkedInScraper(hrefs)
scraper.scrape_all()
