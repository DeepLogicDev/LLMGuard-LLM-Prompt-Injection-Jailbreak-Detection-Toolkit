import re

JAILBREAK_PATTERNS = [
    r"(?i)ignore previous instructions",
    r"(?i)disregard all prior prompts",
    r"(?i)pretend to be",
    r"(?i)as an AI developed by",
    r"(?i)you are not an AI"
]

def analyze_prompt(prompt):
    matches = [pattern for pattern in JAILBREAK_PATTERNS if re.search(pattern, prompt)]
    return {
        "malicious": bool(matches),
        "matched_patterns": matches
    }
