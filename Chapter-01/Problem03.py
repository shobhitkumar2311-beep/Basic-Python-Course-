# Install an external module and use it to perform an operation of your interest.

import pyttsx3
engine = pyttsx3.init()
engine.say("Hello, I am a text to speech engine. I can convert text to speech. My first line is my name is John.")
engine.runAndWait()  