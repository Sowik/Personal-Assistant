import pyjokes
from PersonalAss import Assistant


def tellAjoke():
    #vzimame shega ot pyjokes
    joke = str(pyjokes.get_joke())
    print(joke)
    Assistant.speak(joke)
    return joke
