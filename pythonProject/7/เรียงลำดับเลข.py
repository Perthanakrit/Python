numberList = []
for i in range(5): #0,1,2,3,4
    userN = input("Enter number:")
    if i == 5:
        break
    else:
        numberList.append(userN)

numberList.sort()
numberList.reverse()
print(numberList)
for j in range(len(numberList)):
    print(numberList[j])

