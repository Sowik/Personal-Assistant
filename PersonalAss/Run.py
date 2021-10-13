import webbrowser
from PersonalAss import WikiSearch
from PersonalAss import Jokes
from PersonalAss import Assistant
from PersonalAss import SynonymAntonym
from PersonalAss import SearchGoogle
from PersonalAss.FacePics import takepic
from PersonalAss.FacePics import CheckKnownFace
from PersonalAss import rememberMe
from PersonalAss import sendEmail
from PersonalAss import CryptoPrices
from PersonalAss import TwitterApp
from PersonalAss import alarm
from PersonalAss import rss
from PersonalAss import WolframAlpha

def choose_function(whatisaid):
    botWords = ""

    if 'wikipedia' in whatisaid:  # if wikipedia found in the query then this block will be executed
        return WikiSearch.searchWikipedia()
    elif "set an alarm" in whatisaid:
        return alarm.alarm()
    elif "show me" and "news" in whatisaid:
        return rss.rssfeed()
    elif "what" and "weather" in whatisaid:
        return WolframAlpha.wolframQuestions()
    elif "twitter" and "post" in whatisaid:
        return TwitterApp.postTweet()
    elif "twitter" and "message" in whatisaid:
        return TwitterApp.sendDM()
    elif 'open youtube' in whatisaid:
        return webbrowser.open("youtube.com")
    elif 'open google' in whatisaid:
        return webbrowser.open("google.com")
    elif 'tell me a joke' in whatisaid:
        return Jokes.tellAjoke()
    elif 'synonym' in whatisaid:
        return SynonymAntonym.findSynonyms()
    elif 'antonym' in whatisaid:
        return SynonymAntonym.findAntonyms()
    elif 'search google for' in whatisaid:
        SearchGoogle.searchGoogle()
    elif 'take a picture of me' in whatisaid:
        takepic.takeApic()
    elif "who am i" in whatisaid:
        return Assistant.speak(CheckKnownFace.getKnownFace())
    elif "remember me" in whatisaid:
        return rememberMe.rememberMyFace()
    elif "send an email" in whatisaid:
        return sendEmail.sendEmail()
    elif "bitcoin" and "price" in whatisaid:
        return CryptoPrices.getBtcPrice()
    elif "ethereum" and "price" in whatisaid:
        return CryptoPrices.getEthPrice()




if __name__ == "__main__":
    Assistant.wishMe()
    while True:
        Assistant.query = Assistant.takeCommand().lower()  # Converting user query into lower case
        # Logic for executing tasks based on query
        choose_function(Assistant.query)