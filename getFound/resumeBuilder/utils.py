import os
import glob
import numpy as np
import re
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

class TextFileLoader:
    def __init__(self, script_path, project_end='getFound', data_path='scrapers/V2/data/raw_text_files'):
        self.script_dir = os.path.abspath(script_path)
        self.project_end = project_end
        self.data_path = data_path
        self.project_root = self.get_project_root()
        self.data_dir = self.get_data_directory()
        self.stopwords = set(stopwords.words('english'))

    def get_project_root(self):
        project_root = self.script_dir
        for _ in range(10):  # Adjust this value as needed
            if project_root.endswith(self.project_end):
                return project_root
            project_root = os.path.dirname(project_root)
        else:
            raise ValueError(f"Project root directory '{self.project_end}' not found within 10 parent directories.")
        return None

    def get_data_directory(self):
        return os.path.join(self.project_root, self.data_path)

    def load_txt_files(self):
        txt_files = glob.glob(os.path.join(self.data_dir, '*.txt'))
        file_contents = []
        for filename in txt_files:
            try:
                with open(filename, 'r') as file:
                    content = file.read().replace('\n', '')  # Remove newline tags
                    file_contents.append(content)
            except IOError as e:
                print(f"Error reading file {filename}: {e}")
        return file_contents

    def clean_text(self, input_text):
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
        no_stopwords_text = ' '.join([word for word in no_alnum_text.split() if word not in self.stopwords])
        # Minimize unnecessary spaces
        cleaned_text = re.sub(r'\s+', ' ', no_stopwords_text).strip()
        return cleaned_text

    def get_file_contents_string(self):
        file_contents = self.load_txt_files()
        file_contents_string = ' '.join(file_contents)  # Combine into a single string
        cleaned_contents_string = self.clean_text(file_contents_string)
        return cleaned_contents_string


def loadFiles():
    # Usage:
    loader = TextFileLoader(__file__)
    file_contents_array = loader.get_file_contents_string()
    return file_contents_array


