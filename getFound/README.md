# getFound

getFound is a comprehensive job search utility designed to help users search for jobs via LinkedIn, extract details from job descriptions, perform keyword analysis, and generate a PDF report. It uses various libraries like `openai`, `transformers`, `selenium`, and more to execute its tasks.

## Overview of modules

### TextProcessor

This class is used to process chunks of text with OpenAI's GPT-3. It is used in the `GPTKeywords` function to process raw job descriptions and extract relevant keywords. 

### GPTKeywords
```Note this is not curerntly immplemmented```

This function serves as a comprehensive process to utilize the `TextProcessor` class, read raw job text, process it, and save the processed results into a JSON file.

### JobManager

This class is used to interact with LinkedIn's API, clean job IDs from LinkedIn job links, and retrieve job data. The `pull_linkedin_data` function concurrently retrieves job data and writes it to JSON files.

### runJobManager

This function serves as a comprehensive process to utilize the `JobManager` class, read LinkedIn hrefs, clean the hrefs into job IDs, and pull job data from LinkedIn.

### KeyphraseExtractionPipeline

This class is a pipeline for the extraction of key phrases from text. It's used in the `keywords` function to process job descriptions and extract relevant key phrases.

### keywords

This function reads raw job text, cleans the text, chunks it, and applies the `KeyphraseExtractionPipeline` to each chunk. The extracted keyphrases are then written to a text file.

### KeywordAnalyzer

This class is used to analyze the relevance of keywords with respect to predefined search terms. This is done by calculating the cosine similarity between the embeddings of keywords and search terms. Keywords with a cosine similarity score above a certain threshold are considered related.

### KeywordSim

This function uses the `KeywordAnalyzer` class to analyze extracted keywords and write related keywords to a text file.

### LinkedinJobLinkSkimmer

This class is used to automatically skim job links from LinkedIn. It opens a Chrome window, navigates to LinkedIn, and automatically scrolls through the page while extracting job links. The job links are then saved to a text file.

### collect_job_links

This function initiates a `LinkedinJobLinkSkimmer` instance and begins the job link collection process.

### main_job_links

This function parallelizes the job link collection process for multiple search terms.

### JobProcessor

This class reads job data (in JSON format) and writes the job descriptions to individual text files.

### runJobProcessor

This function initiates a `JobProcessor` instance and begins the job data reading and job description writing process.

### main

This is the main function that sequentially calls other functions and classes to perform the entire job search, data extraction, and keyword analysis process. The phases are:

1. Collect LinkedIn job links.
2. Extract job data from LinkedIn.
3. Extract job descriptions from the job data.
4. Extract keywords from job descriptions.
5. Analyze the similarity of the keywords.
6. Formulate a PDF report based on the results.

## Usage

To run the entire pipeline, just execute the Python script from the command line:

```
python script_name.py
```

Replace `script_name.py` with the name of the Python script file.

> Note: The script needs to have necessary parameters set in the `getFound.src.config.params` configuration file.