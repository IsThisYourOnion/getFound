from linkedInScraper import LinkedInScraper
from utils import JSONDataProcessor
import os
from itertools import chain


def main():
    # ## Collect URLs (HREFS) for jobs from specified positions
    # scraper = LinkedinUrlSkimmer()
    # job_positions = ['deep learning scientist', 'data scientist', 'machine learning engineer']
    # scraper.scrape(job_positions, 20000, 8)  # Specify the job positions, number of iterations, and number of threads
    # # will stop at 20k hrefs per job item

    # Read in hrefs to extract job descriptions from Utils functions
    base_project_dir = JSONDataProcessor.get_root_path()
    directory_path = os.path.join(base_project_dir, 'data', 'raw_data', 'linkedin_hrefs')
    processor = JSONDataProcessor(directory_path)
    all_data = processor.read_json_files()
    href_list = list(chain.from_iterable(all_data))

    scraper = LinkedInScraper(href_list)
    scraper.scrape_all()


if __name__ == "__main__":
    main()
