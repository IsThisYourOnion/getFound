# getFound


## Usage

* `linkedinURLSkimmer.py`: pulls hrefs.
* `LinkedInScraper`: pulls descriptions

1. Clone the repository or download the source code.
2. Open the `getFound/scrapers/linkedinURLSkimmer.py` file in a text editor.
3. Modify the `job_positions` list in the `scrape` method to specify the job positions you want to scrape. For example: `job_positions = ['deep learning scientist', 'data scientist', 'machine learning engineer']`.
4. Adjust the number of iterations and the number of threads as per your requirements in the `scrape` method: `scraper.scrape(job_positions, iterations, num_threads)`.
5. Run the `getFound/scrapers/linkedinURLSkimmer.py` file using Python.

The scraper will start extracting job listings from LinkedIn for each specified job position. The captured LinkedIn URLs will be saved as separate JSON files in the `getFound/data/raw_data/linkedin_hrefs` directory.

## Customization

- If you want to change the output directory for JSON files, modify the `file_path` variable in the `write_to_json` method of the `LinkedinURLSkimmer` class.
- To customize the base LinkedIn URL or other parameters, modify the respective variables in the `LinkedinURLSkimmer` class.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
