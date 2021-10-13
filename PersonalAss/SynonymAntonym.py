import nltk
nltk.download('wordnet')
from nltk.corpus import wordnet
from PersonalAss import Assistant

def findSynonyms():
    Assistant.query = Assistant.query.replace("synonym", "")
    Assistant.query = Assistant.query.replace(" ", "")
    synonyms = []
    count = 0
    #izvajdame sinonimite za dadenata duma ot wordnet.synsets
    for syn in wordnet.synsets(Assistant.query):
        count += 1
        if count == 11:
            break
        for l in syn.lemmas():
            synonyms.append(l.name())

    #prevryshtame sinonimite v string
    synonyms = list(dict.fromkeys(synonyms))
    strsyn = ', '.join(map(str, synonyms))
    print(strsyn)
    Assistant.speak('Synonyms of the word ' + Assistant.query + " are")
    Assistant.speak(strsyn)
    return 'Synonyms of the word ' + Assistant.query + " are " + strsyn

def findAntonyms():
    Assistant.query = Assistant.query.replace("antonym", "")
    Assistant.query = Assistant.query.replace(" ", "")
    antonyms = []
    count = 0
    # izvajdame antonimite za dadenata duma ot wordnet.synsets
    for syn in wordnet.synsets(Assistant.query):
        if count == 11:
            break
        for l in syn.lemmas():
            if l.antonyms():
                count += 1
                antonyms.append(l.antonyms()[0].name())
    #prevryshtame antonimite v string
    antonyms = list(dict.fromkeys(antonyms))
    antsyn = ', '.join(map(str, antonyms))
    print(antsyn)
    Assistant.speak('Antonyms of the word ' + Assistant.query + " are")
    Assistant.speak(antsyn)
    return 'Antonyms of the word ' + Assistant.query + " are " + antsyn

