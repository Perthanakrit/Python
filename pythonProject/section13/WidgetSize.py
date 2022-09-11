from tkinter import *

def sayhelloworld():
    print("hello world")
Mainwindow = Tk()
button = Button(Mainwindow,text = "Click1", command = sayhelloworld,width=20,height=1).grid(row=0,column=1)
button2 = Button(Mainwindow,text = "Click2", command = sayhelloworld).grid(row=1,column=1)
button2 = Button(Mainwindow,text = "Click3", command = sayhelloworld).grid(row=0,column=2)
label=Label(Mainwindow,text = "Hello",width=20).grid(row=2)
Mainwindow.mainloop()