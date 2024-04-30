import speech_recognition as sr
import datetime

listen = sr.Recognizer()

# def take_command():
#     command = None  # Initialize command
print("Start...")
try:
    print("In try")
    with sr.Microphone() as source:

        print('listening...')
        voice = listen.listen(source)
        command = listen.recognize_google(voice)
        print(command)
        # command = command.lower()
        # if 'alexa' in command:
        #     command = command.replace('alexa', '')
except:
    pass
