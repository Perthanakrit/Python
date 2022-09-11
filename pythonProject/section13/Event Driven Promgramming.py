from tkinter import *

def leftClickbutton(event):
    print("leftclick")

def rightClickbutton(event):
    print("rightclick")
def doubleClickbutton(event):
    print("doubleclick")
main=Tk()

def task():
    print("hello")
    main.after(2000, task)  # reschedule event in 2 seconds

main.after(2000, task)
main.mainloop()

