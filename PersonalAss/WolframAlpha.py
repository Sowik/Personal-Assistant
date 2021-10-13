import wolframalpha  # pip install wolframalpha
from PersonalAss import Assistant


def wolframQuestions():
    question = Assistant.takeCommand()
    question = question.replace("check", "")
    app_id = "RQ89AE-6YWUWX4AT7"
    client = wolframalpha.Client(app_id)
    res = client.query(question)
    answer = next(res.results).text
    Assistant.speak(answer)
    return answer
