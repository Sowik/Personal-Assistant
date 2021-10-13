from PersonalAss import Assistant
from PersonalAss.GUI import PyqtGui
import tweepy

global auth


def authenticateTwitter():
    try:
        auth = tweepy.OAuthHandler("f3CPjOpq0AKRLXZO09yG4zLYA", "D1BmUicrWHA5Iu7HCibvMIwuvgvugSRzGSYd8kw7zYI7CkTai7")

        auth.set_access_token("510541353-3Yea93VFNiDDMQx1Ejmpz24XQr4NWsRZljznk5QC",
                              "nVUGOuD9BS58yu6kLSWDKh25JcLzUYrb17imuiE82IQHv")

        # auth = tweepy.OAuthHandler(conKey, conSec)
        #
        # auth.set_access_token(accToken,
        #                       accSec)
        print("Auth Done")
        Assistant.speak("Authentication Done")

        print(auth)

    except:
        Assistant.speak("Authentication failed")
        print("Authentication failed")
        return 0

    return auth


def postTweet():
    auth1 = authenticateTwitter()
    try:
        api = tweepy.API(auth1)

        Assistant.speak("Tell me the message")

        api.update_status(Assistant.takeCommand())

        Assistant.speak("Tweet Posted")
        return "Tweet Posted"
    except:
        Assistant.speak("Cannot Login To Twitter")
        return "Cannot Login To Twitter"


def sendDM():
    auth1 = authenticateTwitter()

    api = tweepy.API(auth1)

    Assistant.speak("Tell me the user id")
    id = Assistant.takeCommand()

    Assistant.speak("Tell me the message")

    api.send_direct_message(id, Assistant.takeCommand())
