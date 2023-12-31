from getFound.src.modules.linkedinJobSkimmer_V2 import main_job_links
from getFound.src.modules.jobDetailExtractor import runJobManager
from getFound.src.modules.textProcessor import runJobProcessor
from getFound.src.modules.keywordExtractor import keywords
from getFound.src.modules.gptExtractor import GPTKeywords
from getFound.templates.templater import toPdf
from getFound.src.modules.keywordSimilarity import KeywordSim

def main():
    """
    Main function to handle LinkedIn job scraping operations
    """

    print('\n[Phase 1] Initiating LinkedIn job link collection...')
    main_job_links()

    print('[Phase 2] Starting job data extraction...')
    runJobManager()

    print('[Phase 3] Extracting job descriptions to files...')
    runJobProcessor()

    print('[Phase 4] Extracting keywords from job data...')
    keywords()

    print('[Phase 5] Performing similarity extraction...')
    KeywordSim()

    print('[Phase 6] Formulating Pdf...')
    toPdf()


if __name__ == "__main__":
    main()
