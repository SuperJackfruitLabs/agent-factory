from typing import List
import nltk
from nltk.tokenize import word_tokenize
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.chunk import ne_chunk
from nltk.tag import pos_tag


def download_nltk_resources():
    resources = [
        "punkt",
        "averaged_perceptron_tagger",
        "maxent_ne_chunker",
        "words",
        "vader_lexicon",
    ]
    for resource in resources:
        try:
            nltk.data.find(f"tokenizers/{resource}")
        except LookupError:
            nltk.download(resource, quiet=True)


download_nltk_resources()


def tokenize(text: str) -> List[str]:
    """
    Tokenize the input text into words.
    """
    return word_tokenize(text)


def extract_entities(text: str) -> List[str]:
    """
    Extract named entities from the input text.
    """
    tokens = word_tokenize(text)
    pos_tags = pos_tag(tokens)
    named_entities = ne_chunk(pos_tags)

    entities = []
    for chunk in named_entities:
        if hasattr(chunk, "label"):
            entity = " ".join(c[0] for c in chunk)
            entities.append(entity)

    return entities


def analyze_sentiment(text: str) -> float:
    """
    Analyze the sentiment of the input text.
    Returns a float between -1 (very negative) and 1 (very positive).
    """
    sia = SentimentIntensityAnalyzer()
    sentiment_scores = sia.polarity_scores(text)
    return sentiment_scores["compound"]
