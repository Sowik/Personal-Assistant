import cryptocompare
from PersonalAss import Assistant

#Nastroivame API Key-a
cryptocompare.cryptocompare._set_api_key_parameter("2635bfc726455cceffe75db807c6c9d619a1122ea5d6e564c37c2992cac8dd7d")

def getBtcPrice():
    #Zarejdame cenata na Bitcoin v USD
    info = cryptocompare.get_price('BTC', currency='USD')
    #Vryshta ni nested dicts, ot tam vzimame cenata
    price = info['BTC']["USD"]
    print(price)

    Assistant.speak("Bitcoin's price is " + str(price) + " USD")
    return "Bitcoin's price is " + str(price) + " USD"

def getEthPrice():
    #Zarejdame cenata na Ethereum v USD
    info = cryptocompare.get_price('ETH', currency='USD')
    #Vryshta ni nested dicts, ot tam vzimame cenata
    price = info['ETH']["USD"]
    print(price)

    Assistant.speak("Ethereum's price is " + str(price) + " USD")
    return "Ethereum's price is " + str(price) + " USD"
