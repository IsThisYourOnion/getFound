from linkedInScraper import LinkedInScraper
from linkedinURLSkimmer import LinkedinUrlSkimmer
from utils import JSONDataProcessor
import os
from itertools import chain


def main():
    ## Collect URLs (HREFS) for jobs from specified positions
    scraper = LinkedinUrlSkimmer()
    job_positions = ['deep learning scientist', 'data scientist', 'machine learning engineer']
    scraper.scrape(job_positions, 100, 8)  # Specify the job positions, number of iterations, and number of threads
    # will stop at 20k hrefs per job item

    # Read in hrefs to extract job descriptions from Utils functions
    processor = JSONDataProcessor('/Users/adamkirstein/Code/getFound/getFound/data/raw_data/href_data/linkedin/')
    all_data = processor.read_json_files()

    href_list = list(chain.from_iterable(all_data))

    scraper = LinkedInScraper(href_list)
    scraper.scrape_all()


if __name__ == "__main__":
    main()
