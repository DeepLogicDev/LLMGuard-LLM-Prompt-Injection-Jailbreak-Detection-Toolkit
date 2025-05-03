
# 🚨 LLMGuard: LLM Prompt Injection & Jailbreak Detection Toolkit

[![GitHub last commit](https://img.shields.io/github/last-commit/DeepLogicDev/LLMGuard-LLM-Prompt-Injection-Jailbreak-Detection-Toolkit)](https://github.com/DeepLogicDev/LLMGuard-LLM-Prompt-Injection-Jailbreak-Detection-Toolkit)
[![GitHub stars](https://img.shields.io/github/stars/DeepLogicDev/LLMGuard-LLM-Prompt-Injection-Jailbreak-Detection-Toolkit?style=social)](https://github.com/DeepLogicDev/LLMGuard-LLM-Prompt-Injection-Jailbreak-Detection-Toolkit/stargazers)

LLMGuard is an AI-powered toolkit designed to detect prompt injection and jailbreak attempts in large language model (LLM) interactions. It combines rule-based analysis and transformer-based classification to ensure safer AI prompt usage.

---

## 🔍 Features

- ✅ Regex-based jailbreak and prompt injection pattern detection
- ✅ Transformer-based emotion classification using BERT
- ✅ RESTful API using FastAPI
- ✅ Interactive analysis dashboard using Streamlit
- ✅ Easily extendable modules for sanitization and logging

---

## 🧱 Project Structure

```
llmguard/
├── app/
│   ├── analyzer.py       # Regex & pattern-based checks
│   ├── classifier.py     # ML/NLP classification
│   ├── sanitizer.py      # Optional rewriting module
│   └── utils.py          # Logging and helper functions
├── data/
│   ├── jailbreak_samples.json
│   └── safe_prompts.json
├── models/
│   └── bert_finetuned_model/   # (Add fine-tuned model here)
├── dashboard/
│   └── streamlit_app.py
├── api/
│   └── main.py           # FastAPI wrapper
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the FastAPI Server
```bash
uvicorn api.main:app --reload
```

### 3. Launch the Streamlit Dashboard
```bash
streamlit run dashboard/streamlit_app.py
```

---

## 🔬 Future Enhancements

- [ ] Improve the sanitizer module with LLM-based rewriting
- [ ] Train and integrate a custom jailbreak classifier
- [ ] Add live WebSocket-based prompt monitoring
- [ ] Build real-time threat reporting analytics

---

## 📜 License

This project is open-source and available under the MIT License.  
© 2025 LLMGuard Contributors

---

🌐 [Explore on GitHub](https://github.com/DeepLogicDev/LLMGuard-LLM-Prompt-Injection-Jailbreak-Detection-Toolkit)
