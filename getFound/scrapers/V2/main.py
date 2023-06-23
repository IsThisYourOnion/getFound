from linkedinJobSkimmer_V2 import LinkedinJobLinkSkimmer
import chromedriver_autoinstaller
from utils import ProcessJobIds
import os
import params
from jobDetailExtractor import LinkedinJobScraper

def main():

    #### HREF COLLECTION ####
    print('Beginning Href collection....')
    chromedriver_autoinstaller.install()
    search_items = params.search_terms
    scraper = LinkedinJobLinkSkimmer(search_items)
    scraper.perform_search()
    print("The scraper has finished collecting hrefs. All links have been successfully stored.")

    #### Extract Job Ids ####
    print('Beginning job id extraction...')
    # Construct the directory path relative to the current script's location
    relative_directory_path = 'data/linkedin_hrefs'
    script_directory = os.path.dirname(os.path.abspath(__file__))
    directory_path = os.path.join(script_directory, relative_directory_path)
    # Using the class
    processor = ProcessJobIds(directory_path)
    processor.process()
    print('Finished extracting jobs')


    #### JOB DESCRIPTION EXTRACTION ####
    print('Beginning job data collection...')
    # Get the script's current directory
    current_directory = os.path.dirname(os.path.abspath(__file__))
    # Construct the input and output directory paths
    input_directory_path = os.path.join(current_directory, 'data/linkedin_hrefs/job_ids')
    output_directory_path = os.path.join(current_directory, 'data/linkedin_job_response_raw')
    # Instantiate the scraper with the constructed paths
    scraper = LinkedinJobScraper(params.email, params.password, input_directory_path, output_directory_path)
    job_ids = scraper.get_job_ids()
    scraper.get_jobs(job_ids)
    print('Finished job data collection...')
    print("Job's done :D")


if __name__ == "__main__":
    main()