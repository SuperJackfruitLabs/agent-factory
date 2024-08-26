import pytest
from agent_backend.utils.nlp_processing import (
    tokenize,
    extract_entities,
    analyze_sentiment,
)


def test_tokenization():
    text = "This is a test sentence."
    tokens = tokenize(text)
    assert tokens == ["This", "is", "a", "test", "sentence", "."]


def test_entity_extraction():
    text = "John Doe works at Google in New York."
    entities = extract_entities(text)
    assert "John Doe" in entities
    assert "Google" in entities
    assert "New York" in entities


def test_sentiment_analysis():
    positive_text = "I love this product! It's amazing."
    negative_text = "This is terrible. I hate it."
    neutral_text = "The sky is blue."

    assert analyze_sentiment(positive_text) > 0
    assert analyze_sentiment(negative_text) < 0
    assert -0.1 < analyze_sentiment(neutral_text) < 0.1
