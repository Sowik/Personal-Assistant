import smtplib
from PersonalAss import Assistant

def sendEmail():
    # speak('to whom to send the message')
    receiver = input()
    Assistant.speak('What is the subject?')
    subject = Assistant.takeCommand()
    Assistant.speak('What should I say?')
    message = Assistant.takeCommand()
    content = 'Subject: {}\n\n{}'.format(subject, message)

    # init gmail SMTP
    mail = smtplib.SMTP('smtp.gmail.com', 587)

    # identify to server
    mail.ehlo()

    # encrypt session
    mail.starttls()

    # login
    mail.login('nbupythonassistant@gmail.com', 'thecoolkid21')

    # send message
    mail.sendmail('nbupythonassistant@gmail.com', receiver, content)

    # end mail connection
    mail.close()

    Assistant.speak('Email sent.')