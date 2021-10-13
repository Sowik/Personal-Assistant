from PersonalAss import Assistant
from PersonalAss import Run
import wikipedia

def searchWikipedia():
    Assistant.speak('Searching Wikipedia...')
    Assistant.query = Assistant.query.replace("wikipedia", "")
    #Vzimame pyrvite 2 izrecheniq za tyrsenata duma ot wikipedia
    results = wikipedia.summary(Assistant.query, sentences=2)
    Assistant.speak("According to Wikipedia")
    print(results)
    Assistant.speak(results)