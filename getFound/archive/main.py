from getFound.archive.linkedinJobSkimmer_V2 import LinkedinJobLinkSkimmer
from getFound.archive.jobDetailExtractor import LinkedinJobScraper
from utils import ProcessJobIds, run_JsonProcessor
import chromedriver_autoinstaller
import params
import os
from utils import loadFiles
from textProcessor import KeyphraseExtractionPipeline


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
    print('[Phase 3] Starting job data collection. Grab a drink and relax for a while...')
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

        # Define output directory
        output_dir = 'data/keywords'
        # Create output directory if it does not exist
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        text = loadFiles()
        # Load pipeline
        model_name = "ml6team/keyphrase-extraction-kbir-inspec"
        extractor = KeyphraseExtractionPipeline(model=model_name)

        # Divide text into 400-character chunks
        chunks = [text[i:i + 400] for i in range(0, len(text), 400)]

        # Open file before starting the loop
        with open(f'{output_dir}/keywords.txt', 'w') as f:
            for idx, chunk in enumerate(chunks):
                keyphrases = extractor(chunk)

                # Write keyphrases to file
                for phrase in keyphrases:
                    f.write("%s\n" % phrase)


if __name__ == "__main__":
    main()
