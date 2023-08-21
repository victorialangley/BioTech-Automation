"""
keyword_extraction.py
Author: Victoria Langley
Description: This script extracts and ranks keywords from essay text.
"""

from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

class KeywordExtractor:
    def __init__(self, text):
        self.text = text

    def extract_keywords(self, num_keywords=5):
        # Tokenize and preprocess the text
        tokens = word_tokenize(self.text)
        tokens = [token.lower() for token in tokens if token.isalnum()]

        # Remove stopwords and punctuation
        stop_words = set(stopwords.words("english"))
        tokens = [token for token in tokens if token not in stop_words]

        # Calculate term frequency
        term_frequency = Counter(tokens)

        # Get the top N keywords
        keywords = [keyword for keyword, _ in term_frequency.most_common(num_keywords)]
        return keywords

if __name__ == "__main__":
    essay_text = """
    Biotechnology has made significant contributions to medicine and agriculture.
    Genetic engineering, bioremediation, and drug discovery are key areas.
    Ethical considerations arise due to potential misuse of biotech advancements.
    """

    extractor = KeywordExtractor(essay_text)
    extracted_keywords = extractor.extract_keywords(num_keywords=5)

    print("Extracted Keywords:")
    for rank, keyword in enumerate(extracted_keywords, start=1):
        print(f"{rank}. {keyword}")
