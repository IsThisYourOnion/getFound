# LinkedIn Job Scraper

This project automates the process of searching, skimming, and extracting job data from LinkedIn. It also includes functionality to extract keywords from the job data for better understanding of job requirements.

## Features

1. Collects job links from LinkedIn based on given search terms.
2. Extracts job data from the collected links.
3. Stores job descriptions in text files.
4. Extracts keywords from the job data.

## Dependencies

The script is built in Python and uses a number of libraries. Install the dependencies with the following command:

```bash
pip install selenium joblib transformers linkedin_api
```

You also need to have a Google Chrome browser installed as the Selenium webdriver used in this script is Chrome-based.

## Quick Start

1. Configure your parameters in the `getFound/src/config.py` file. The parameters include the number of jobs you want to search, search terms, and your LinkedIn login credentials (email and password).

2. To run the script, navigate to the project directory and run:

```bash
python3 main.py
```

## How It Works

The script works in four main phases:

- **Phase 1** - LinkedIn job link collection: It collects job links from LinkedIn based on your search terms.
- **Phase 2** - Job data extraction: It extracts job data from the collected LinkedIn job links.
- **Phase 3** - Extracting job descriptions: The job descriptions are extracted and stored in text files for further processing.
- **Phase 4** - Extracting keywords: The script then extracts keywords from the job data, giving you a clear picture of the key requirements across different jobs.

The output of the script includes the links to the jobs collected, extracted job data in JSON format, job descriptions stored in text files, and extracted keywords.

## Output

The output data will be stored in the `data` directory. This includes job links from LinkedIn, job data in JSON format, job descriptions in text files, and extracted keywords.

## Troubleshooting

Make sure the parameters in `getFound/src/config.py` are set correctly. If the script is not running, check for error messages in the console. If you see an error about Selenium not being able to open the browser, check your Chrome version and make sure it's compatible with the webdriver version.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.