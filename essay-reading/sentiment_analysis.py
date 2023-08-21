"""
sentiment_analysis.py
Author: Victoria Langley
Description: This script performs sentiment analysis on extracted essay text.
"""

from textblob import TextBlob

class SentimentAnalyzer:
    def __init__(self, text):
        self.text = text

    def analyze_sentiment(self):
        analysis = TextBlob(self.text)
        sentiment_score = analysis.sentiment.polarity

        if sentiment_score > 0:
            sentiment = "Positive"
        elif sentiment_score < 0:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"

        return sentiment, sentiment_score

if __name__ == "__main__":
    essay_text = """
    The advancements in biotechnology have revolutionized medical research.
    However, there are also ethical concerns surrounding genetic manipulation.
    """

    analyzer = SentimentAnalyzer(essay_text)
    sentiment, sentiment_score = analyzer.analyze_sentiment()

    print(f"Sentiment: {sentiment}")
    print(f"Sentiment Score: {sentiment_score:.2f}")
