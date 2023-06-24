import datetime
import os
import nltk

from nltk.corpus import stopwords
from pathlib import Path
import glob
import json
import re

nltk.download('stopwords')

stopwords_list = set(stopwords.words('english'))

class DataManager:
    def __init__(self):
        self.root_dir = self.get_project_root()

    def get_project_root(self) -> Path:
        """Return the root directory of your project."""
        return Path(__file__).parent.parent.parent

    def read_data(self, input_path: str, input_file_extension: str, as_list=False):
        # read all files from root/data/{input_path} with the extension {input_file_extension}
        files_pattern = str(self.root_dir / 'data' / input_path / f'*.{input_file_extension}')
        files = glob.glob(files_pattern)
        data = []
        for file_path in files:
            with open(file_path, 'r') as f:
                if input_file_extension == 'json':
                    file_data = json.load(f)
                elif as_list:
                    file_data = f.read().splitlines()
                else:
                    file_data = f.read()
                data.append(file_data)
        return data

    def write_data(self, output_path: str, filename: str, output_file_extension: str, data):
        # write to root/data/{output_path}/{filename}.{output_file_extension}
        output_dir_path = self.root_dir / 'data' / output_path
        output_dir_path.mkdir(parents=True, exist_ok=True)

        output_file_path = output_dir_path / f'{filename}.{output_file_extension}'
        with open(output_file_path, 'w') as f:
            if output_file_extension == 'json':
                json.dump(data, f)
            elif isinstance(data, list):
                f.write('\n'.join(data))
            else:
                f.write(data)



def clean_text(input_text):
    # Convert to lowercase
    lower_text = input_text.lower()
    # Remove URLs
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    no_url_text = url_pattern.sub('', lower_text)
    # Remove punctuation
    no_punct_text = re.sub(r'[^\w\s]', '', no_url_text)
    # Remove alphanumeric sequences (sequences that include both letters and numbers)
    no_alnum_text = re.sub(r'\b(?=\w*\d)\w+\b', '', no_punct_text)
    # Remove stopwords
    no_stopwords_text = ' '.join([word for word in no_alnum_text.split() if word not in stopwords_list])
    # Minimize unnecessary spaces and remove newline characters
    cleaned_text = re.sub(r'\s+', ' ', no_stopwords_text).strip().replace('\n', '')
    return cleaned_text

def remove_duplicates(input_list):
    return list(dict.fromkeys(input_list))
