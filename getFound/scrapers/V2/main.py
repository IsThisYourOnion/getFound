from linkedinJobSkimmer_V2 import LinkedinJobLinkSkimmer
from jobDetailExtractor import LinkedinJobScraper
from utils import ProcessJobIds, run_JsonProcessor
import chromedriver_autoinstaller
import os
import params


def main():
    """
    Main function to handle LinkedIn job scraping operations
    """

    # Link collection phase
    print('\n[Phase 1] Initiating LinkedIn job link collection...')
    chromedriver_autoinstaller.install()
    search_items = params.search_terms
    link_skimmer = LinkedinJobLinkSkimmer(search_items)

    # Perform search
    try:
        link_skimmer.perform_search()
        print(f'Successfully finished collecting job links. Data stored.\n')
    except Exception as e:
        print(f'An error occurred while collecting links: {e}\n')

    # Job ID extraction phase
    print('[Phase 2] Starting job ID extraction...')
    relative_directory_path = 'data/linkedin_hrefs'
    script_directory = os.path.dirname(os.path.abspath(__file__))
    directory_path = os.path.join(script_directory, relative_directory_path)

    # Extract Job Ids
    try:
        job_id_processor = ProcessJobIds(directory_path)
        job_id_processor.process()
        print('Successfully finished extracting job IDs.\n')
    except Exception as e:
        print(f'An error occurred while extracting job IDs: {e}\n')

    # Job description extraction phase
    print('[Phase 3] Starting job data collection...')
    input_directory_path = os.path.join(script_directory, 'data/linkedin_hrefs/job_ids')
    output_directory_path = os.path.join(script_directory, 'data/linkedin_job_response_raw')

    # Collect Job Descriptions
    try:
        scraper = LinkedinJobScraper(params.email, params.password, input_directory_path, output_directory_path)
        job_ids = scraper.get_job_ids()
        scraper.get_jobs(job_ids)
        print('Successfully finished job data collection.\n')
    except Exception as e:
        print(f'An error occurred while collecting job data: {e}\n')

    # Extract job description to files
    print('[Phase 4] Extracting job data to files...')
    try:
        run_JsonProcessor()
        print('Successfully finished extracting job data to files. Job done! :D')
    except Exception as e:
        print(f'An error occurred while extracting job data to files: {e}\n')


if __name__ == "__main__":
    main()
