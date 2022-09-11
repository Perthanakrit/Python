fishList = []
while True:
    numF = int(input('weight of fish :'))
    if numF == 0:
        break
    else:
        fishList.append(numF)
def stringMethon():
    strN = str(fishList)
    strN = strN.strip('[, ]')
    strN = strN.split(',')
    resultA = ''.join(strN)
    print(resultA)
def sorting_numbers():
    for num in fishList:
        print(num, end=' ')

text = str(input('Fuction:'))
text = text.capitalize()
if text == 'Min':
    fishList.sort()
    sorting_numbers()
elif text == 'Max':
    fishList.sort()
    fishList.reverse()
    sorting_numbers()

