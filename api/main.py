from fastapi import FastAPI, Request
from pydantic import BaseModel
from app.analyzer import analyze_prompt
from app.classifier import classify_prompt

app = FastAPI()

class PromptInput(BaseModel):
    prompt: str

@app.post("/analyze")
def analyze(input: PromptInput):
    analysis = analyze_prompt(input.prompt)
    classification = classify_prompt(input.prompt)
    return {
        "regex_analysis": analysis,
        "ml_classification": classification
    }
