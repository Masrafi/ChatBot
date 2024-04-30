import speech_recognition as sr
import wikipedia
from spech import text_to_speech
import pywhatkit
import pyjokes
import webbrowser


recognizer = sr.Recognizer()


def take_command():
    with sr.Microphone() as source:
        print("Speak something...")
        audio_data = recognizer.listen(source)

    # Perform speech recognition using Google Web Speech API
    try:
        text = recognizer.recognize_google(audio_data)
        print("You said:", text)
        if "your name" in text:
            text_to_speech('My name is Alexa')
        elif "play" in text:
            pywhatkit.playonyt(text)
        elif "thank you" in text:
            text_to_speech("You are welcome")
        elif 'about' in text:
            look_for = text.replace('tell me about', '')
            info = wikipedia.summary(look_for, 2)
            print(info)
        elif 'what' in text:
            info = wikipedia.summary(text, 2)
            text_to_speech(info)
        elif 'joke' in text:
            my_joke = pyjokes.get_joke(language="en", category="neutral")
            text_to_speech(my_joke)
        else:
            text_to_speech("Sorry, I am not understand")
    except sr.UnknownValueError:
        text_to_speech("Sorry")
    except sr.RequestError as e:
        print("Error: Could not request results from Google Speech Recognition service;")

