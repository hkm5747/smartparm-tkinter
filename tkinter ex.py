from tkinter import *
import tkinter.font
import numpy as np
import pigpio
win = Tk()
myFont = tkinter.font.Font(family = 'Verdana', size = 20, weight = 'bold')
win.geometry('800x480')
win.configure(background='#CD5C5C')
#------------------------------------------------------main program ----------------------------------#
def readSensors():
    #function body
    # output is a list with name measuredValues
    #measuredValues contains total 4 values as I have 4 sensors
    win.after(1000, readSensors)     #calling the function every second
#label names variable
output_1= StringVar()
output_2 = StringVar()
output_3 = StringVar()
output_4 = StringVar()
value0 = str(measuredValues[0])
value1= str(measuredValues[1])
value2 = str(measuredValues[2])
value3 = str(measuredValues[3])
output_1.set (value0)
output_2.set (value1)
output_3.set (value2)
output_4.set(value3)
#Labels
# i used textvariable to to measured values. but doesn't work so far
#display values
output_1_label = Label(win, textvariable = output_1,height =2, width = 12)
output_1_label.place(x=200, y=100)
output_2_label = Label(win, textvariable = output_2, height =2, width = 12)
output_2_label.place(x=200, y=200)
output_3_label = Label(win, textvariable = output_3,height =2, width = 12)
output_3_label.place(x=200, y=300)
output_4_label = Label(win, textvariable = output_4, height =2, width = 12)
output_4_label.place(x=200, y=400)
#how to update the window with new data?
win.after(1000, readSensor)
win.mainloop()