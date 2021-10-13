from PersonalAss import Assistant
from PersonalAss.FacePics import CheckKnownFace

def rememberMyFace():

    Assistant.speak("Okay, what is your name")

    my_name = Assistant.takeCommand()

    CheckKnownFace.rememberMe(my_name)

    Assistant.speak("Done " + my_name)
    return "Done " + my_name