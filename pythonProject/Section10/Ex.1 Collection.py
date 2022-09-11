menuList = []
priceList = []

def showBill():
    totalprice = 0
    print("---- Per Shop----")
    for number in range(len(menuList)):
        print(menuList[number], priceList[number])
        totalprice += int(priceList[number])
    print("Total : ",totalprice)

while True:
    menuName = input("Plese Enter Menu :")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price :")
        menuList.append(menuName)
        priceList.append(menuPrice)

showBill()