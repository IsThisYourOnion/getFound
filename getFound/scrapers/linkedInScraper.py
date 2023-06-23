import requests
from bs4 import BeautifulSoup
import json
import os
from concurrent.futures import ThreadPoolExecutor

class LinkedInScraper:
    def __init__(self, hrefs, directory='getFound/data/raw_data/linkedin_descriptions'):
        self.hrefs = hrefs
        self.directory = directory

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

                write_path = '/Users/adamkirstein/Code/getFound/getFound/data/raw_data/description_data/linkedin/'
                file_name = f'linkedin_description_{self.hrefs.index(href)}.json'

                with open(write_path + file_name, 'w', encoding='utf-8') as f:
                    json.dump({href: text}, f, ensure_ascii=False, indent=4)
            else:
                print(f'No element found for URL {href}')
        except Exception as e:
            print(f'Error occurred for URL {href}: {e}')

    def scrape_all(self):
        with ThreadPoolExecutor() as executor:
            executor.map(self.scrape_url, self.hrefs)



