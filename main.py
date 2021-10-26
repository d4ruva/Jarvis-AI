"""
Author: Dhruva Dhangar
Date: 26-10-21
"""
import speech_recognition as sr
from gtts import gTTS
import os, time, playsound


class main():
    def __init__(self, text):
        self.text = text
        self.tts = gTTS(text=self.text, lang="en")
        self.filename = "voice.mp3"

    def speak(self):
        self.tts.save(self.filename)
        playsound.playsound(self.filename)


obj = main("Hello World")

main.speak(obj)
