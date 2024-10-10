import streamlit as st
from Models.llama import llama_check

st.set_page_config(
    page_title="FactTube",
    page_icon='img/ft_1.png',
)

# Streamlit app
st.image('img/ft_1.png', width=500)


# User input
youtube_url = st.text_input(label="Enter YouTube URL:", placeholder="https://www.youtube.com/watch?v=dQw4w9WgXcQ")

if st.button("Check Facts"):
    if youtube_url:
    # Call the fact-checking function
        result, description = llama_check(youtube_url)
        st.write("Video Title:", description)
        st.write("Fact-Check Result:", result)
    else:
        st.write("Please enter a valid YouTube URL.")