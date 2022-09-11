from tkinter import *

def planPage (event):
    label_text = StringVar()
    label_P= Label(Mainwindow,text="Plans for(Date)")
    label_P.grid(row=1, column=0)
    label_entry = Entry(Mainwindow, textvariable= label_text)
    label_entry.grid(row=1, column=1)
    return
Mainwindow = Tk()
chioce = Button(Mainwindow,text="Plans for today")
chioce.bind('<Button-1>', planPage)
chioce.grid(row=0,column=0)

Mainwindow.title('Appication')
Mainwindow.geometry('300x600')


Mainwindow.mainloop()