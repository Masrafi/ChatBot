import speech_recognition as sr
from spech import text_to_speech
from text import take_command

recognizer = sr.Recognizer()
text_to_speech('How can I help you?')
# Capture audio input from the microphone
take_command()

while True:
    take_command()