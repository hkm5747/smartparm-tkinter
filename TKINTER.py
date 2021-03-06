import tkinter as tk
import serial
import time
import codecs

ser = serial.Serial('COM12', 9600)

humi_temp = []

#온도와 습도 읽어오는 함수
def read_current_Temperature():
    val = ser.readline()
    humi_temp = val.decode()
    return humi_temp[0:5], humi_temp[0:4]

def update():
    aktTemp.config(text=str(read_current_Temperature()))
    aktTemp.after(1000, update)

HEIGHT = 300
WIDTH = 500
root = tk.Tk()
canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

aktTemp = tk.Label(root, text=str(read_current_Temperature())+"°C", fg="black") 
aktTemp.pack()

aktHumi = tk.Label(root, text=str(read_current_Temperature())+"%", fg="black") 
aktHumi.pack()

update()
root.mainloop()