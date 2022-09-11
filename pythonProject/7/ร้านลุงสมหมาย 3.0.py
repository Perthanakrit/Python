def inputnumbers():
    for i in range(len(nameList)):
        print(nameList[i],'(age :',str(ageLsit[i])+')')

nameList = []
ageLsit = []
genderLsit = []
nbcm = int(input('Enter number  of customer:')) #4
for i in range(nbcm): #0,1,2,3
    userName = input("Enter name:")
    yearofBrith = int(input('Your birth year :'))
    ageP  = 2017 - yearofBrith
    genDer = str(input())
    if i == nbcm:
        break
    else:
        nameList.append(userName)
        ageLsit.append(ageP)
        genderLsit.append(genDer)

print("--Customers Information--")
inputnumbers()

