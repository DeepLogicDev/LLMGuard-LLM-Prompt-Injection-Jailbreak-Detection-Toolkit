from transformers import pipeline
import torch

classifier = pipeline("text-classification", model="bhadresh-savani/bert-base-uncased-emotion")

def classify_prompt(prompt):
    result = classifier(prompt)[0]
    label = result['label']
    score = result['score']
    return {
        "label": label,
        "confidence": score
    }
