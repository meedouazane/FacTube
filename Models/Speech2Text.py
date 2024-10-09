#!/usr/bin/python3
"""
Speech to text module
"""
from pytubefix.cli import on_progress
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
    yt = YouTube(url, on_progress_callback = on_progress)
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
