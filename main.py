"""
Author: Dhruva Dhangar
Date: 26-10-21
"""
import os
import playsound

import speech_recognition as sr
from gtts import gTTS


class main():
    def __init__(self, text):
        self.text = text
        self.tts = gTTS(text=self.text, lang="en")
        self.filename = "output.mp3"

    def speak(self):
        self.tts.save(self.filename)
        playsound.playsound(os.path.join(os.getcwd(), self.filename))

    def recognize(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
            said = ""

            try:
                said = r.recognize_google(audio)
                print(said)
            except Exception as e:
                print("Error: " + str(e))


obj = main("Hello")
obj.recognize()
