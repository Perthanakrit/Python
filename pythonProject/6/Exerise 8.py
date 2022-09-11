usernameInput = input("Username :")
passwordInput = input("Password :")
if usernameInput == "cooler" and passwordInput == "094258" :
    print("_________Welcome________")
    print("1.Pizza        30 THB")
    print("2.Burger       20 THB")
    print("3.Cocacola     10 THB")
    ProductList = int(input("Number : "))
    if ProductList == 1:
        priceP = 30
        print("-Pizza-")
        quantityP = int(input("quantity to buy : "))
        print("result =",priceP*quantityP,"THB")
    elif ProductList == 2 :
        priceB = 20
        print("-Burger-")
        quantityB = int(input("quantity to buy : "))
        print("result =",priceB*quantityB,"THB")
    elif ProductList == 3 :
        priceC = 10
        print("-Cocacola-")
        quantityC = int(input("quantity to buy : "))
        print("result =",priceC*quantityC,"THB")
    print("Thank you very much.")
else:
    print("------------Error-----------")
    print("Please try again,","Thank you.")