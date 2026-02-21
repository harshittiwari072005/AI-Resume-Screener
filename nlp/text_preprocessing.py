import spacy
import re

# Load English NLP model
nlp = spacy.load("en_core_web_sm")

def clean_text(text: str) -> str:
    """
    Cleans and normalizes resume text for NLP similarity.
    Steps:
    - lowercase
    - remove emails
    - remove numbers & special characters
    - remove stopwords
    - lemmatize words
    """

    # 1. Lowercase
    text = text.lower()

    # 2. Remove email addresses
    text = re.sub(r"\S+@\S+", " ", text)

    # 3. Remove non-alphabet characters
    text = re.sub(r"[^a-z\s]", " ", text)

    # 4. NLP processing
    doc = nlp(text)

    tokens = []
    for token in doc:
        # remove stopwords and very short tokens
        if not token.is_stop and len(token.text) > 2:
            tokens.append(token.lemma_)

    return " ".join(tokens)
