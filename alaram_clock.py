import datetime
from playsound import playsound
alarmHour = int(input("Enter Hour: "))
alarmMin = int(input("Enter the minutes: "))
alarmAM = input("am / pm:")

if (alarmAM == "pm"):
    alarmHour+=12 

while True:
    if alarmHour==datetime.datetime.now().hour and alarmMin==datetime.datetime.now().minute:
        print("Playing...")
        playsound("tune.mp3")
        break
