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

 while True:
    current_time = time.localtime(time.time())
    hour_in_min = current_time[3] * 60
    minute= current_time[4]
    sec_in_min= (localtime[5])/60
    current_time_in_minute = hour_in_min + minute + sec_in_min
   #print("a",Alarm_time,"c",current_time_in_minute )
    if(Alarm_time == current_time_in_minute ):
        winsound.Beep(frequency, duration)
        break
 



#---click function defination-------
def click():
    txt = text_entry.get() # collect text from variable text_entry to txt
    print(txt)
#----------------------------------

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
# click is a  user defined function
b= Button(window,text="Start-50",width=6,command=alarm_clock)
b.grid(row=4,column=0,sticky=S)

window.mainloop()
