from PersonalAss import Assistant
from PersonalAss import Run
import datetime
import simpleaudio as sa  # exclusively for windows only,


# if you are on any other system you can use 'playsound' or 'simpleaudio' module.
def alarm():
    # alarm_hour = int(input("Set hour: "))
    # alarm_minutes = int(input("Set minutes: "))
    # am_pm = input("am or pm? ")

    Assistant.speak("Enter hours")
    alarm_hour = int(Assistant.takeCommand())
    Assistant.speak("Enter minutes")
    alarm_minutes = int(Assistant.takeCommand())
    Assistant.speak("Beforenoon or Afternoon")
    am_pm = Assistant.takeCommand()

    print(f"Waiting for time: {alarm_hour}:{alarm_minutes} {am_pm}")

    # time conversion
    # because datetime module returns time in military form i.e. 24 hrs format
    if am_pm == 'afternoon':  # to convert pm to military time
        alarm_hour += 12

    elif alarm_hour == 12 and am_pm == 'beforenoon':  # to convert 12am to military time
        alarm_hour -= 12

    else:
        pass

    while True:  # infinite loop starts to make the program running until time matches alarm time

        # ringing alarm + execution condition for alarm
        if alarm_hour == datetime.datetime.now().hour and alarm_minutes == datetime.datetime.now().minute:
            print("wake up")

            # winsound.Beep(9999,9999)

            wave_obj = sa.WaveObject.from_wave_file("file1.wav")
            play_obj = wave_obj.play()
            play_obj.wait_done()
            break