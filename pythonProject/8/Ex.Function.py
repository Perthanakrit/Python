def login():
    usermaneInput = input("Username :")
    passwordInput = input("Password :")
    if usermaneInput == "admin" and passwordInput == "1234":
        return  True
    else:
        return False#fsdf
def showMenu():
    print("-----ishop----")
    print("1.Vat Calulator")
    print("2. Price Calcutor")
def menuSelect():
    GoodsInput = int(input("Add-> "))
    return  GoodsInput
def VatCalulator(tolatPrice) :
    vat = 7
    result = tolatPrice+ (tolatPrice * vat / 100)
    return result
def PriceCalcutor():
    price1 = int(input("First Profduct Price : "))
    price2 = int(input("Second Profduct Price : "))
    return VatCalulator(price1 + price2)
if login():
    print(showMenu())
    Select = menuSelect()
    if Select == 1 :
       print(VatCalulator(int(input("Price :"))))
    elif Select == 2 :
        print("result >>",PriceCalcutor(),"THB")

