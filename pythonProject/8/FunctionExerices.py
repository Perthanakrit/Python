def choice():
    print("Pyramin=1")
    print("Cylinder=2")
    print("Cone=3")

def Pyramin():
    D1 = int(input("D="))
    D2 = int(input("D="))
    H = int(input("height="))
    V=1/2*(D1*D2*H)
    print(V,"cm3")

def Cylinder():
    r = int(input("r="))
    H1 = int(input("height="))
    pi = 3.14
    V_Cylinder = 2 *pi*r*H1
    return V_Cylinder

def Cone():
    r_cone=int(input("r="))
    H_cone=int(input("height="))
    pi_cone=3.14
    V_cone = 1/3*pi_cone*r_cone*r_cone*H_cone
    return V_cone

def selecting():
    userSelect = int(input("select->"))
    return  userSelect

print(choice())
User = selecting()
if User == 1  :
    print(Pyramin())
elif User==2 :
    print(Cylinder())
elif User==3 :
    print(Cone())

