import re
from flashtext import KeywordProcessor
import spacy

nlp = spacy.load("en_core_web_sm")

sensitive_words_db = ["example1", "example2", "example3"]

EMAIL_REGEX = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
URL_REGEX = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'


def filter_text_with_regex(input_text, sensitive_words):
    filtered_text = input_text
    for word in sensitive_words:
        filtered_text = re.sub(r'\b' + re.escape(word) + r'\b', '**Filtered**', filtered_text)
    filtered_text = re.sub(EMAIL_REGEX, '**Filtered Email**', filtered_text)
    filtered_text = re.sub(URL_REGEX, '**Filtered URL**', filtered_text)
    return filtered_text


def filter_text_with_flashtext(input_text, sensitive_words):
    keyword_processor = KeywordProcessor()
    for word in sensitive_words:
        keyword_processor.add_keyword(word, '**Filtered**')
    filtered_text = keyword_processor.replace_keywords(input_text)
    return filtered_text


def filter_text_with_nlp(input_text, sensitive_words):
    filtered_text = input_text
    doc = nlp(input_text)
    for ent in doc.ents:
        if ent.label_ in ["GPE", "ORG"]:
            filtered_text = filtered_text.replace(ent.text, '**Filtered**')
    return filtered_text
