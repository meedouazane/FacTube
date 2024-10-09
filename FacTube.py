import streamlit as st
from Models.llama import llama_check


# Streamlit app
st.title("YouTube Fact Checker")

# User input
youtube_url = st.text_input("Enter YouTube URL:")

if st.button("Check Facts"):
    if youtube_url:
        # Call the fact-checking function
        result, description = llama_check(youtube_url)
        st.write("Video Title:", description)
        st.write("Fact-Check Result:", result)
    else:
        st.write("Please enter a valid YouTube URL.")