import webbrowser
from PersonalAss import Assistant

def searchGoogle():
    Assistant.speak('Opening Google...')
    Assistant.query = Assistant.query.replace("search google for ", "")
    Assistant.query = Assistant.query.replace(" ", "+")
    webbrowser.open("google.com/search?q=" + Assistant.query) #otvarqme browser s link kym dadenoto tyrsene
