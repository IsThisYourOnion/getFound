# LinkedIn Job Scraper

This repository contains code for scraping job data from LinkedIn using Selenium and the LinkedIn API. The code allows you to collect job links, extract job IDs, and retrieve detailed job data from LinkedIn.

## Prerequisites

Before running the code, ensure that you have the following:

- Python 3.x installed on your system
- `selenium` package installed (`pip install selenium`)
- `chromedriver_autoinstaller` package installed (`pip install chromedriver_autoinstaller`)
- `linkedin-api` package installed (`pip install linkedin-api`)

Additionally, please make sure you have the following credentials:

- Your LinkedIn email address
- Your LinkedIn password

## Usage

1. Clone the repository to your local machine or download the source code.

2. Install the required packages using the following command:

   ```
   pip install -r requirements.txt
   ```

3. Open the `params.py` file and update the following variables with your LinkedIn credentials:

   - `email`: Your LinkedIn email address
   - `password`: Your LinkedIn password

4. Customize the list of search terms in the `search_terms` variable in the `params.py` file. Add or remove search terms based on your requirements.

5. Open a terminal or command prompt and navigate to the directory where the code is located.

6. Run the script by executing the following command:

   ```
   python main.py
   ```

   The script will perform the following actions:

   - Collect job links from LinkedIn based on the provided search terms.
   - Extract job IDs from the collected links.
   - Retrieve detailed job data for each job ID using the LinkedIn API.
   - Save the job data as JSON files in the specified output directory.

7. After the script finishes execution, you can find the scraped job data in the specified output directory.

## Customization

- If you want to change the output directory for the scraped job data, modify the `output_directory` variable in the `LinkedinJobScraper` class.

- You can adjust the number of job results to collect for each search term by modifying the `while len(self.hrefs) < 100` condition in the `search_position` method of the `LinkedinJobLinkSkimmer` class.

- Feel free to customize the code further to suit your specific needs. You can explore the different methods and classes to extend the functionality or make any necessary modifications.

## Disclaimer

Please note that web scraping may violate the terms of service of websites. Make sure to use this code responsibly and in accordance with the LinkedIn terms of service. The code provided here is for educational purposes only, and the developers are not responsible for any misuse or legal consequences arising from its usage.