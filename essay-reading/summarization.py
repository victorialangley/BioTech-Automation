"""
summarization.py
Author: Victoria Langley
Description: This script generates a summary of extracted essay text.
"""

from gensim.summarization import summarize

class EssaySummarizer:
    def __init__(self, text):
        self.text = text

    def generate_summary(self, ratio=0.3):
        summary = summarize(self.text, ratio=ratio)
        return summary

if __name__ == "__main__":
    essay_text = """
    The advancements in biotechnology have led to breakthroughs in medicine and agriculture.
    Genetic engineering, bioremediation, and drug discovery are some of the key areas.
    However, ethical concerns arise due to the potential misuse of biotech innovations.
    This essay explores the impact and challenges of biotechnology on society.
    """

    summarizer = EssaySummarizer(essay_text)
    generated_summary = summarizer.generate_summary()

    print("Generated Summary:")
    print(generated_summary)
