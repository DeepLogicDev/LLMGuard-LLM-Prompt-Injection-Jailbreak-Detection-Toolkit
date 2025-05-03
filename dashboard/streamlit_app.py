import streamlit as st
from app.analyzer import analyze_prompt
from app.classifier import classify_prompt

st.title("LLMGuard: Prompt Injection Detection")

prompt = st.text_area("Enter Prompt:")
if st.button("Analyze"):
    result_regex = analyze_prompt(prompt)
    result_ml = classify_prompt(prompt)

    st.subheader("Regex Analysis")
    st.write(result_regex)

    st.subheader("ML Classification")
    st.write(result_ml)
