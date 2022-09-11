from tkinter import *

def sayhelloworld():
    print("hello world")
Mainwindow = Tk()
button = Button(Mainwindow,text = "Click", command = sayhelloworld)
button.place(x=50 ,y=20)

Mainwindow2 = Tk()
button2 = Button(Mainwindow2,text = "Click", command = sayhelloworld)
button2.place(x=50 ,y=20)
Mainwindow2.mainloop()
