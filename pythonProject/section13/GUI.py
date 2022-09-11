from tkinter import *

def login(event):
    usernameInput = BoxName.get()
    passwordInput = BoxPasword.get()
    if usernameInput == "cooler" or passwordInput == "094258":
        check = "Corrent"
        print(check)
    else:
        check="inCorrent"
        print(check)
    result.configure(text=check)
Mainwindow = Tk()
name= Label(Mainwindow,text="Username")
name.grid(row=0,column=0)
BoxName=Entry(Mainwindow)
BoxName.grid(row=0,column=1)
pasword= Label(Mainwindow,text="Password")
pasword.grid(row=1,column=0)
BoxPasword=Entry(Mainwindow)
BoxPasword.grid(row=1,column=1)
LoginButton=Button(Mainwindow,text="Login")
LoginButton.bind('<Button-1>',login)
LoginButton.grid(row=2,column=0)
result= Label(Mainwindow,text="")
result.grid(row=2,column=1)

Mainwindow.mainloop()