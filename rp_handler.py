import runpod
import time
import spacy

def handler(event):
    input = event['input']
    nlp = spacy.load("en_core_web_lg")
    doc = nlp(input['prompt'])
    ents = []
    for ent in doc.ents:
        ents.append({"text": ent.text, "label_": ent.label_})
    return ents

if __name__ == '__main__':
    runpod.serverless.start({'handler': handler})
