'''
 12345-> 1+2+3+4+5=15 67896789678967896879678967896789678967896789678969
 15->1+5
'''
numI = int(input('Enter numbers :'))
numI = str(numI)
lenNumm = 1000
strNum =''
while lenNumm > 1 :
    numDefault = 0
    for x in numI:
        digitX = int(x)
        numDefault += digitX
    strNum = str(numDefault)
    lenNumm = len(strNum)
    numI = strNum

print(strNum)