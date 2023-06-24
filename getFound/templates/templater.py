from getFound.src.utils.utils import DataManager, remove_duplicates
from jinja2 import Environment, FileSystemLoader
import textwrap
import pdfkit
from pathlib import Path


class PDFCreator:
    def __init__(self):
        self.manager = DataManager()

        # Adjusted paths
        self.base_path = Path(__file__).resolve().parents[2]  # Gets the absolute path of the root project folder
        self.template_path = self.base_path / 'getFound' / 'templates'  # Constructs path to the templates folder
        self.output_path = self.template_path / 'output.pdf'  # Constructs path to the output pdf file
        self.input_path = self.base_path / 'getFound' / 'data' / 'job_keywords' / 'staging_keywords' / 'keywords.txt'

        self.keywords = self.get_keywords()
        self.columns = self.get_columns()

    def get_keywords(self):
        with open(str(self.input_path), 'r') as file:
            content = file.readlines()
        kwds = [line.strip() for line in content]
        return kwds

    def get_columns(self):
        items_per_column, extra = divmod(len(self.keywords), 4)
        columns = []
        for i in range(4):
            start = i * items_per_column + min(i, extra)
            end = start + items_per_column + (i < extra)
            columns.append(self.keywords[start:end])
        return columns

    def create_pdf(self):
        file_loader = FileSystemLoader(str(self.template_path))  # Converts Path object to string for compatibility with FileSystemLoader
        env = Environment(loader=file_loader)
        template = env.get_template('template.html')
        output = template.render(columns=self.columns)
        pdfkit.from_string(output, str(self.output_path))  # Converts Path object to string for compatibility with pdfkit


def toPdf():
    pdf_creator = PDFCreator()
    pdf_creator.create_pdf()
