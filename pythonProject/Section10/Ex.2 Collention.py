menuList = []
def showBill():
    print("----Per Shop----")
    for number in range(len(menuList)):
        print(menuList[number][0])

while True:
    menuName = input("Please Enter Menu :")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price :")
        menuList.append([menuName,menuPrice])
print(menuList)
showBill()