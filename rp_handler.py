import runpod
import time
import spacy
from spacy.matcher import Matcher

def handler(event):
    input = event['input']
    nlp = spacy.load("en_core_web_sm")
    matcher = Matcher(nlp.vocab)
    # Add match ID "HelloWorld" with no callback and one pattern
    pattern = [{"LOWER": "hello"}, {"IS_PUNCT": True}, {"LOWER": "world"}]
    matcher.add("HelloWorld", [pattern])

    doc = nlp("Hello, world! Hello world!")
    matches = matcher(doc)

    return matches

if __name__ == '__main__':
    runpod.serverless.start({'handler': handler})
