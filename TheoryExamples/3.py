from gtts import gTTS
from io import BytesIO
import pygame

class TextToSpeech:
    def __init__(self):
        pygame.mixer.init()

    def speak(self, text):
        tts = gTTS(text)
        fp = BytesIO()
        tts.save(fp)
        fp.seek(0)
        pygame.mixer.music.load(fp)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue