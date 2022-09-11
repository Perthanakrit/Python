numR = int(input('numbers of input:'))
numberList = []
for i in range(numR):
    userN = int(input('number:'))
    if i == numR :
        break
    else:
        numberList.append(userN)

numberList.sort()
numberList.reverse()
for j in range(len(numberList)):
    print(numberList[j])
