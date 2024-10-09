from groq import Groq
from .Speech2Text import speech_to_text


client = Groq()

def llama_check(url):
    text, title = speech_to_text(url)
    completion = client.chat.completions.create(
        model="llama-3.1-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": f"You are an AI trained to identify and verify  factual information."
                           f" Please check the following text for any false information and provide corrections or confirmations :"
                           f" {text} "
            }
        ],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=True,
        stop=None,
    )
    result = ""
    for chunk in completion:
        content = chunk.choices[0].delta.content or ""
        result += content
    return result, title
