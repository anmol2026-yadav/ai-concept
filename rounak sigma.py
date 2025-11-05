import streamlit as st
from openai import OpenAI
import os
client = OpenAI("api_key=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")

st.title("AI Concept Explainer 🧠")
st.write("Understand any topic easily — explained like you're 12!")

topic = st.text_input("Enter a topic or concept you want to understand:")
language = st.selectbox("Choose explanation language:", ["English", "Hindi"])

if st.button("Explain"):
    prompt = f"Explain the concept '{topic}' in very simple {language}. Use real-life examples and short sentences. Avoid jargon."
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    
    st.subheader("Explanation 👇")
    st.write(response.choices[0].message.content)
