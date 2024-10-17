
![logo](https://i.ibb.co/3S4STkq/ft-1.png)

# Introduction
Welcome to [**FacTube**](https://truedetective.com), In today's digital age, extracting valuable information from YouTube videos efficiently is crucial. This web application empowers you to accomplish a range of tasks related to YouTube videos, all in one convenient place.

## Key Features
* Reliable Fact-Checking: Navigate the information landscape with confidence. This web application incorporates fact-checking capabilities to help you verify the accuracy of claims made in YouTube videos. Identify potential misinformation and make informed decisions based on reliable sources.

## Benefits
* Save Time and Effort: Eliminate the need for multiple tools or manual processes. This web app streamlines your workflow and allows you to achieve your goals quickly and easily.
* Boost Efficiency: Get more out of YouTube videos with this comprehensive toolkit. Extract audio, translate content, and generate PDFs, all within a single platform.
* Enhance Understanding: Overcome language barriers and ensure you're getting accurate information from YouTube videos.


## Installation
* Clone this repository: `git clone "https://github.com/meedouazane/FacTube.git"`
* Access TrueDetective directory: `cd FacTube`
* Run pip to install dependence : `pip3 install -r requirements.txt`
* Sign up at [**Groq**](https://groq.com/) to obtain an API key for Free.
* You can either set the environment variable in your terminal  `export GROQ_API_KEY="YOUR_KEY"` or store it in a .env file.
* Run setup to install ffmpeg for Linux: `bash setup.sh` for Windows you can download and install it from [**ffmpeg**](https://www.ffmpeg.org/download.html) 
* Run app.py: `streamlit run FacTube.py`
* web app will be running on http://localhost:8501/

# Technologies:

Front-end Technologies:

Streamlit: an open-source Python framework for data scientists and AI/ML engineers to deliver interactive data apps.

Back-end Technologies:

Python:  high-level, general-purpose programming language known for its readability and simplicity.  
FastApi:  web framework for building HTTP-based service APIs in Python 3.8+. It uses Pydantic and type hints to validate, serialize and deserialize data.  
llama-3.1-70b-versatile: openly available model that rivals the top AI models when it comes to state-of-the-art capabilities in general knowledge, steerability, math, tool use, and multilingual translation.  
whisper-large-v3: general-purpose speech recognition model. It is trained on a large dataset of diverse audio and is also a multitasking model.  
Pytube: a lightweight, Pythonic, dependency-free, library (and command-line utility) for downloading YouTube Videos.

# Usage
Welcome to our user-friendly platform! Let's walk through the seamless process of optimizing your video with our features.

Misinformation Check
1. Copy and Paste the YouTube Video URL: Locate the URL of the YouTube video you want to check for misinformation. Paste the URL into the designated field on the True Detective website.
2. Submit the URL: Once you've pasted the URL, click the "Submit" button. True Detective will then initiate the fact-checking process.
3. Review the Results: FacTube will analyze the video and provide you with a report on any potential misinformation it detects.
![check](https://i.ibb.co/VtWHymS/1.png)
![check](https://i.ibb.co/6F8xr2c/2.png)


# Deployment
This code was tested and deployed on [Render](https://dashboard.render.com/) using Apache as a web server.

## The Team
Mohamed Ouazane - Back-end developer and Project manager [Github](https://github.com/meedouazane)  

# Related projects

* [Tomato Disease Detection](https://github.com/meedouazane/Tomato_Disease_Detection): A deep learning-based model designed to accurately identify and classify various tomato diseases from images of infected leaves. Leveraging advanced techniques like convolutional neural networks (CNNs).

* [Suggesti](https://github.com/meedouazane/Suggesti): Suggesti is a chatbot that provides movie and TV series recommendations based on a user-provided title. It uses cosine similarity to compare various attributes (genres, ratings, etc.) and is powered by Dialogflow to manage the conversational interface.

# Contributing
[ALX](https://intranet.alxswe.com/) and [Holberton School](https://www.holbertonschool.com/) (Staff and Students)

# License

MIT License
