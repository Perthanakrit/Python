from tkinter import *

def sayhelloworld():
    print("hello world")
Mainwindow = Tk()
button = Button(Mainwindow,text = "Click1", command = sayhelloworld).grid(row=0,column=1)
button2 = Button(Mainwindow,text = "Click2", command = sayhelloworld).grid(row=1,column=1)
button2 = Button(Mainwindow,text = "Click3", command = sayhelloworld).grid(row=0,column=2)

Mainwindow.mainloop()