systemMenu = {"chicken":40,"pork":50,"beef":60,"duck":40}
menuList = []
def showBill():
    print("----PER SHOP----")
    total = 0
    for number in range(len(menuList)):
        print(menuList[number][0],menuList[number][1])
        total +=int(menuList[number][1])
    print("Total Price : ", total)

while True:
    menuName = input("Please Enter Menu :")
    if(menuName.lower() == "exit"):
        break
    else:
        menuList.append([menuName,systemMenu[menuName]])
print(menuList)
showBill()