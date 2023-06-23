# LinkedIn Job Scraper

This Python application uses Selenium and BeautifulSoup to automate job searching in LinkedIn. It searches for job listings based on certain keywords, extracts the links of these listings, and then scrapes the job descriptions from these links.

## Files
The application consists of the following files:

1. `linkedinJobSkimmer.py`: This file contains the main logic for searching LinkedIn job listings and extracting their URLs.

2. `linkedInScraper.py`: This file scrapes job descriptions from LinkedIn job listing URLs obtained from the previous script.

3. `main.py`: This is the driver script that invokes the previous two scripts and coordinates the flow of the application.

## How it works

### Part 1: LinkedIn Job Skimmer

The `linkedinJobSkimmer.py` script starts a Selenium webdriver, goes to LinkedIn's job search page, and enters your desired job keywords into the search bar. It uses Selenium's functionality to scroll down and 'click' the 'load more' button in order to load more job listings. 

From each loaded job listing, it extracts the URL and saves it in a list. Once all job listings have been loaded and all URLs extracted, the list of URLs is dumped to a JSON file.

### Part 2: LinkedIn Job Scraper

The `linkedInScraper.py` script takes as input the list of job listing URLs obtained from the previous script. For each URL, it makes a GET request to the webpage, parses the HTML to extract the job description, and then writes the description to a separate JSON file.

## Usage

1. Clone the repository.

2. Install the necessary Python packages using pip:

    ```
    pip install -r requirements.txt
    ```

3. In `main.py`, replace `'deep learning scientist', 'data scientist', 'AI engineer'` with your desired job keywords.

4. Run the application:

    ```
    python main.py
    ```

## Dependencies
This script requires the following Python packages:

- `selenium`
- `beautifulsoup4`
- `requests`
- `concurrent.futures`
- `multiprocessing`
- `json`
- `os`
- `chromedriver_autoinstaller`

These packages can be installed using pip:

```
pip install selenium beautifulsoup4 requests futures multiprocessing json os chromedriver_autoinstaller
```

## Caution
Use this tool responsibly and make sure you are not violating LinkedIn's Terms of Service by using this tool too aggressively.

## Contact
For any questions or issues, please open an issue in the GitHub repository or contact the repository owner directly.