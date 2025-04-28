from gtts import gTTS
import os

def speak_text(text):
    tts = gTTS(text=text, lang='en')
    tts.save("static/speech.mp3")
    os.system("start static/speech.mp3")  # Windows
    # For Linux/Mac, use: os.system("afplay static/speech.mp3")
