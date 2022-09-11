usermaneInput=input("Username :")
passwordInput=input("Password :")
if usermaneInput == "admin" and passwordInput == "1234" :
    print("Succeed")
    print("-----ishop----")
    print("1.Vat calulator")
    print("2. Price Calcutor")
    GoodsInput = int(input("Add"))
    if GoodsInput == 1:
        price = int(input("Price (THB) :"))
        vat = 7
        result = price + (price * vat / 100)
        print(result)
    elif GoodsInput ==2:
        price1 = int(input("First Profduct Price : "))
        price2 = int(input("Second Profduct Price : "))
        print(price1+price2)