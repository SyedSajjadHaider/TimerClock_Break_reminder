from tkinter import *

import time;

import winsound

frequency = 2500  # Set Frequency To 2500 Hertz
duration = 5000  # Set Duration To 1000 ms == 1 second
#winsound.Beep(frequency, duration)

def alarm_clock():

 localtime = time.localtime(time.time())
 hour_in_min = localtime[3] * 60
 minute= localtime[4]
 sec_in_min= (localtime[5])/60

 start_time_in_minute = hour_in_min + minute + sec_in_min

 Alarm_time = start_time_in_minute + 50
 Alarm_time_in_sec = Alarm_time * 60
 time.sleep(Alarm_time_in_sec)
 winsound.Beep(frequency, duration)


#----------------main---------------
window = Tk()  # important line , it create a window
window.title("50 - 10 TOOL") # window title

#--------------LABLE 1 ----------
lb = Label(window,text="STUDY-50 min break-10 min",bg="yellow",fg="black",font="none 12 bold")
lb.grid(row=1,column=0,sticky=W)
#--------------LABLE 2 ----------
lb = Label(window,text="                        ",fg="black",font="none 12 bold")
lb.grid(row=2,column=0,sticky=W)

# add a start button
b= Button(window,text="Start-50",width=6,command=alarm_clock)
b.grid(row=4,column=0,sticky=S)

window.mainloop()
