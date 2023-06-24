"""
Params.py
-----------------------
File to store parameters used for a job scraper and text similarity step
"""

#### Job Search Parameters #### 

# Terms for job search
# Example: search_terms = ['data engineer', 'machine learning researcher', 'deep learning']
search_terms = ['Enter your search terms here']


#### Text Similarity Parameters #### 

# Additional keywords used in the text similarity step 
# These are used to fine-comb through lists of keywords 
# An AI model will use them to evaluate text similarity
# Example: keywords = ['programming', 'python', 'pytorch']
keywords = ['Enter your keywords here']

# Combine original search terms and additional keywords for the text similarity evaluation
similarity_search = search_terms + keywords


#### Scraper Parameters #### 

# Number of items to scrape per keyword before stopping (adjust as desired)
num_jobs = 1000 


#### LinkedIn Credentials #### 

# User's Email
email = "EMAIL"

# User's Password
password = "Password"


#### OpenAI Parameters #### 

# GPT prompt for keyphrase extraction, resume bullet point generation, 
# and output formatting in JSON with 'Keyphrases' and 'Bullet points' as keys
gpt_prompt = 'can you first extract keyphrases, produce attractive resume bullet points, output in a json format with Keyphrases and Bullet points being the keys based on the text:'

# OpenAI API Key
open_ai_key = 'OpenAI API Key'
