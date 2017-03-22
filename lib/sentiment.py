from nltk.sentiment.vader import SentimentIntensityAnalyzer


class SentimentService():
    def __init__(self):
        self.service = SentimentIntensityAnalyzer()

    def analyze(self, text):
        return self.format_polarity(self.service.polarity_scores(text))

    def format_polarity(self, polarity):
        return polarity
