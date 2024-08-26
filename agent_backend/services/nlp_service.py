from typing import List
import spacy

nlp = spacy.load("en_core_web_sm")


def tokenize(text: str) -> List[str]:
    doc = nlp(text)
    return [token.text for token in doc]


def named_entity_recognition(text: str) -> List[dict]:
    doc = nlp(text)
    return [{"text": ent.text, "label": ent.label_} for ent in doc.ents]


def sentiment_analysis(text: str) -> float:
    # This is a simplified example. You might want to use a dedicated sentiment analysis library.
    doc = nlp(text)
    return sum(token.sentiment for token in doc) / len(doc)
