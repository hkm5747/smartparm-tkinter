import tkinter as tk
import serial
import time
import codecs

ser = serial.Serial('COM12', 9600)

humi_temp = []
ver = []

#온도와 습도 읽어오는 함수
def read_current_Temperature():
    if ser.readable():
        humi_temp = ser.readable.decode()
        val = humi_temp.readlines()#리스트로 결과값을 반환한 것을 val에 저장
        return val[0]

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