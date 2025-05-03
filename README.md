# LLMGuard-LLM-Prompt-Injection-Jailbreak-Detection-Toolkit

LLMGuard is an AI-powered toolkit for detecting prompt injection and jailbreak attempts in Large Language Model interactions. It combines rule-based analysis with ML classification to provide real-time protection.

## Features
- Regex-based jailbreaking pattern detection
- Transformer-based prompt classification
- REST API with FastAPI
- Interactive dashboard with Streamlit

## Run Instructions
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the API:
   ```bash
   uvicorn api.main:app --reload
   ```

3. Run the dashboard:
   ```bash
   streamlit run dashboard/streamlit_app.py
   ```
```

## Next Steps
- Add more patterns
- Fine-tune a classifier specifically for prompt injection
- Expand sanitization logic
- Save logs of detected threats
