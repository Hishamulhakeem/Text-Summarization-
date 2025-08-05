
import streamlit as st
from transformers import pipeline

st.title("Text Summarization App")
st.write("Enter a long paragraph or article and get a summary.")

text_input = st.text_area("Enter Text:", height=300)

if st.button("Summarize"):
    if text_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
        summary = summarizer(text_input, max_length=130, min_length=30, do_sample=False)
        st.subheader("Summary")
        st.success(summary[0]['summary_text'])
