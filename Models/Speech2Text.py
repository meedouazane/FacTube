#!/usr/bin/python3
"""
Speech to text module
"""
import io
import subprocess
import yt_dlp
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq()


def extract_audio_from_youtube(url):
    """
    Extract audio from YouTube video and load it into an in-memory buffer without saving to disk.
    :param url: URL of the video
    :return: A BytesIO buffer containing the audio and the video title
    """
    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': True,
        'noplaylist': True,
        'extractaudio': True,
    }

    # Create an in-memory buffer
    audio_buffer = io.BytesIO()

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        # Extract video info
        info = ydl.extract_info(url, download=False)
        title = info.get('title')
        audio_url = info['url']  # URL for the audio stream

        # Use ffmpeg to pipe the audio stream directly into the buffer
        ffmpeg_process = subprocess.Popen(
            ['ffmpeg', '-i', audio_url, '-f', 'mp3', 'pipe:1'],
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL
        )
        # Write audio data to buffer
        audio_buffer.write(ffmpeg_process.stdout.read())
        audio_buffer.seek(0)
    return audio_buffer, title

def speech_to_text(url):
    audio_buffer, title = extract_audio_from_youtube(url)
    transcription = client.audio.transcriptions.create(
        file=("audio.mp4", audio_buffer.read()),
        model="whisper-large-v3",
        response_format="verbose_json",
    )
    return transcription.text, title
