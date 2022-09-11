from tkinter import *
from tkinter import ttk
Mainwindow = Tk()

Mainwindow.title('Tic-Tac-Toe')
labelTopic = ttk.Label(Mainwindow, text="Tic-Tac-Toe", font='30')
labelTopic.grid(row=0, column=0, padx=260, pady=10)




Mainwindow.geometry('620x400')
Mainwindow.mainloop()
