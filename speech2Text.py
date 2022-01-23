# This code converts your real time voice into text

import speech_recognition as sr
#import yagmail

recognizer = sr.Recognizer()
with sr.Microphone() as source:
    print("Clearing the background Noise....")
    recognizer.adjust_for_ambient_noise(source,duration=1)
    print("Waiting for your message....")
    recorderaudio = recognizer.listen(source)
    print("Done recording!")
try:
    print("Printing the message....")
    text = recognizer.recognize_google(recorderaudio,language='en-US')

    print('Your message:{}'.format(text))
except Exception as ex:
    print(ex)
