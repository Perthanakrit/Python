def test1():
    print("Number Pattern ")

    # Decide the row count. (above pattern contains 5 rows)
    row = 5
    # start: 1
    # stop: row+1 (range never include stop number in result)
    # step: 1
    # run loop 5 times
    for i in range(1,row + 1):
        for j in range(1, row-i+1):
            print(end=" ")
        for j in range(i,0,-1):
            print(j,end="")
        for j in range(2,i+1):
            print(j ,end="")
        print("")


def test_stringandinteger(string):
    groups = []
    newword = string[0]
    for x, i in enumerate(string[0:]):
        if i.isalpha():
            pass
    return groups

#HE 45 L 32 LO 458 T 6 H 359 ISIS1BO 589 RNT 34 ODEVN 80 AJA
def test_string(text):
    for i in text:
        if i.isalpha():
            pass





test_string('HE45L32LO458T6H359ISIS1BO589RNT34ODEVN80AJA')



def result_Goods():

    nofg = int(input())
    num = 0
    for i in range(nofg):
        price_G = int(input())
        num += price_G
    print(num,'THB')

def sumNum ():
    numI = int(input('Enter numbers :'))
    numI = str(numI)
    numDefault = 0
    for x in numI:
        digitX = int(x)
        print(type(digitX))

        numDefault += digitX
    numDefault = str(numDefault)
    strNum = str(numDefault)
    numI = strNum
    return type(numDefault)
def listtest():
    list = [14,33,27,35,10,60]
    for x in range(len(list)):
        for i in range(len(list)-1):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]

    print(list)

listtest()
