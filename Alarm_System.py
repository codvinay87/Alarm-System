# import required module
from playsound import playsound
from datetime import datetime as dt

# Getting current
# date and time
now = dt.now()
t=dt.time(now)
t=str(t)
# print(t)
# print(type(t))
hour=t[0]+t[1]
minute=t[3]+t[4]
print(hour)
print(minute)

h_user=int(input("enter the hour: "))
m_user=int(input("enter the minute: "))
if(h_user==int(hour) and m_user==int(minute)):
    # for playing note.wav file
    playsound('/Users/vinaysinghania/Downloads/alarm.wav')
