from tkinter import *
import math
def leftClickbutton(event):
    print(float(textBoxWeight.get())/math.pow( float(textBoxHight.get())/100,2))
    Check()
def Check():
    checkBMI = float(textBoxWeight.get())/math.pow( float(textBoxHight.get())/100,2)
    if checkBMI>= 30:
        result = "อ้วนมาก"
        print(result)
    elif 25<=checkBMI<=29.9:
        result = "อ้วน"
        print(result)
    elif 23 <= checkBMI <= 24.9:
        result = "น้ำหนักเกิน"
        print(result)
    elif 18 <= checkBMI <= 22.9:
        result = "สมส่วน"
        print(result)
    elif checkBMI < 18:
        result = "ผอมเกินไป"
        print(result)
    labelResult.configure(text=float(textBoxWeight.get())/math.pow( float(textBoxHight.get())/100,2))
    labelCheckResult.configure(text= result)

Mainwindow = Tk()

textBoxHight = Entry(Mainwindow)
textBoxHight.grid(row=0,column=1)
labelWeight= Label(Mainwindow,text="น้ำหนัก(kg.)")
labelWeight.grid(row=1,column=0)
textBoxWeight=Entry(Mainwindow)
textBoxWeight.grid(row=1,column=1)
calculateButton=Button(Mainwindow,text="คำนวณ")
calculateButton.bind('<Button-1>', leftClickbutton)
calculateButton.grid(row=2,column=0)
labelResult= Label(Mainwindow,text="ผลลัพธ์")
labelResult.grid(row=2,column=1)
labelCheckResult= Label(Mainwindow,text="")
labelCheckResult.grid(row=3,column=1)
Mainwindow.mainloop()

