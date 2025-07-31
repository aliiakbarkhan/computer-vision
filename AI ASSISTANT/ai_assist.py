import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia

r = sr.Recognizer()

def speak(command):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(command)
    engine.runAndWait()

def commands():
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print('Listening.......Ask now.......')
            audioin = r.listen(source)
            my_text = r.recognize_google(audioin)
            my_text = my_text.lower()
            print(my_text)
    except:
        print('Error in caturing audio..........')

speak("welcome ali")
commands()
'''this is incomplete'''
