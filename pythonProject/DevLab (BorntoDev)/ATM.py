# HE45L32LO458T6H359ISIS1BO589RNT34ODEVN80AJA, 45+32+458+6+359+1+589+34+80 = 1604
text = input("your text :")
charD = ''
numbers = []
for pos,arf in enumerate(text):
    if arf.isdigit():
        charD += arf
        if pos == len(text) - 1:  #ตัวสุดท้าย
            if len(charD) >= 2:
                numbers.append(charD)
            else:
                numbers.append(charD)
                charD = ''
    elif arf.isalpha():
        if len(charD) >= 2:
            numbers.append(charD)
            charD = ''
        else:
            numbers.append(charD)
            charD = ''
        numbers.append(charD)

print(numbers)
numD = 0
for x in numbers:
    if x.isnumeric():
        y = int(x)
        numD+=y

if len(str(numD)) < 4:
    print('0'*(4-len(str(numD)))+str(numD))
else:
    print(numD)