def sanitize_prompt(prompt):
    return prompt.replace("ignore previous instructions", "[REDACTED]")
