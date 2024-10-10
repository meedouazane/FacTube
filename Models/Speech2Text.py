#!/usr/bin/python3
"""
Speech to text module
"""
import io
from pytubefix import YouTube
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq()


def extract_audio_from_youtube(url):
    """
    Extracting audio from YouTube videos
    :param url: url of the video
    :return: the path of audio file
    """
    yt = YouTube(url, use_po_token=True)
    stream = yt.streams.filter(only_audio=True).first()
    audio_buffer = io.BytesIO()
    stream.stream_to_buffer(audio_buffer)
    audio_buffer.seek(0)
    return audio_buffer, yt.title



def speech_to_text(url):
    audio_buffer, title = extract_audio_from_youtube(url)
    transcription = client.audio.transcriptions.create(
        file=("audio.mp4", audio_buffer.read()),
        model="whisper-large-v3",
        response_format="verbose_json",
    )
    return transcription.text, title
