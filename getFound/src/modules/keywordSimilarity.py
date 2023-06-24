from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from getFound.src.utils.utils import DataManager, remove_duplicates
from getFound.src.config import params

class KeywordAnalyzer:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.manager = DataManager()

    def get_related_keywords(self, keywords, search_terms, threshold=0.7):
        keyword_embeddings = self.model.encode(keywords)
        search_term_embeddings = self.model.encode(search_terms)

        # Compute the cosine similarity between keywords and search terms
        cosine_scores = cosine_similarity(keyword_embeddings, search_term_embeddings)

        related_keywords = []

        for i in range(len(keywords)):
            # If the maximum similarity score for the keyword is above the threshold, add it to the related keywords
            if np.max(cosine_scores[i]) > threshold:
                related_keywords.append(keywords[i])

        return related_keywords

    def analyze_keywords(self):
        kwds = self.manager.read_data('job_keywords', 'txt', True)
        kwds = remove_duplicates(kwds[0])
        search_terms = params.similarity_search
        related_keywords = self.get_related_keywords(kwds, search_terms)
        self.manager.write_data('job_keywords/staging_keywords', 'keywords', 'txt', related_keywords)
def KeywordSim():
    analyzer = KeywordAnalyzer()
    analyzer.analyze_keywords()