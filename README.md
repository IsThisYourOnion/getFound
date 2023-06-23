# GetFound: The Project Premise

The essence of this ongoing project is to gather job descriptions in a focused manner, parse them, and assemble the parsed information into a "Master Keyword Resume". 

This concept of a master keyword resume revolves around the idea of a resume rich in keywords relevant to the specific industry and role. This concept takes advantage of the algorithms used by many job posting services, which scan stored resumes for specific keywords to find suitable candidates. 

Through the use of this tool, you can streamline your job search process and increase your visibility to recruiters and employers by ensuring your resume contains the most relevant and sought-after keywords in your industry.

## How GetFound Works

This project has a twofold approach:

1. **Data Collection**: Leveraging powerful web scraping libraries in Python, it automates the process of collecting relevant job descriptions from LinkedIn. The script searches for job listings using specific keywords, fetches the job descriptions, and saves them for further processing.

2. **Keyword Extraction and Resume Building**: In the subsequent stage, the tool will parse through the gathered job descriptions, extracting common and essential keywords from these descriptions. These keywords will then be assembled into the master keyword resume, ensuring the resulting resume is highly relevant and attractive to job posting services.

GetFound is still under development, and future updates will include the keyword extraction and resume building functionalities. 

This project simplifies the labor-intensive process of customizing a resume for each job application, and it can dramatically enhance a candidate's visibility in job search engines and platforms. By automating these steps, GetFound aims to make the job hunting process more efficient and effective. 

Stay tuned for future updates and enhancements to the GetFound project.



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

## Contact
For any questions or issues, please open an issue in the GitHub repository or contact the repository owner directly.