import pyttsx3
import speech_recognition as sr
import datetime
from PersonalAss.FacePics import CheckKnownFace

query = ''

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()  # Without this command, speech will not be audible to us.
    return audio


def wishme():
    hour = int(datetime.datetime.now().hour)


def wishMe():
    #v zavisimost ot dadeniqt chas (24h format) pri startirane asistentyt ni pozdravqva
    hour = int(datetime.datetime.now().hour)

    name = CheckKnownFace.getKnownFace()
    if name == "I don't know you.":
        name = ""

    if hour >= 0 and hour < 12:
        speak("Good Morning " + name)
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon " + name)
    else:
        speak("Good Evening " + name)
    speak("Welcome! Please tell me how may I help you")


def takeCommand():
    # It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')  # Using google for voice recognition.
        print(f"User said: {query}\n")  # User query will be printed.
    except Exception as e:
        # print(e)  use only if you want to print the error!
        print("Say that again please...")  # Say that again will be printed in case of improper voice
        return "None"  # None string will be returned
    return query
