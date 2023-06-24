# params.py

# List of search terms
search_terms = ['deep learning',
                'AI engineer',
                'AI Researcher',
                'Applied Scientist',
                'data scientist']


# goal here is to add you original search terms + any other terms you want to add to finetune your kwds.
# example:
similarity_search = search_terms + ["programming", 'leader']

# User's email
email = "EMAIL"

# User's password
# WARNING: Storing passwords in plain text is not secure.
password = "PASSWORD"

num_jobs = 50

gpt_prompt = 'can you first extract keyphrases, produce attractive resume bullet points, output in a json format with Keyphrases and Bullet points being the keys based on the text:'
open_ai_key = 'API KEY'