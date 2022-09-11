def E ():
    passwordInput = input("Password :")
    while  passwordInput!="Oak123":
        o="in"
        print(o)
        passwordInput = input("Password :")
def ElectricPower ():
    V= int(input("numerical value of voltage: "))
    I= int(input("numerical value of electric current: "))
    print("Electric Power (P)  =", V*I, "Watt")
E()
ElectricPower ()
while "y"or "e" != userselect  :
    userselect = input("Please select y(คำนวณอีกครั้ง) or e(จบการทำงาน) :")
    if userselect == "y":
        ElectricPower()
    elif userselect == "e":
        print("END")
        break