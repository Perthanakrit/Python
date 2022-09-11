userInput = int(input("Enter Number of Your Favorite Fruits :"))
myFruits =set()
while(len(myFruits)<userInput):
    myFruits.add(input("Fruist :"))
    print(myFruits)