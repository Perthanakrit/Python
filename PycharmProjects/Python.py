# I = 1 , V = 5 , X = 10 , L = 50 , C = 100 , D = 500 , M = 1000
m = d = c = L = x = v = i = 0
number = int(input('Number: '))
romanAl = ''

while number > 0:
    if 4000 > number >= 1000:
        number -= 1000
        romanAl += 'M'
    elif 500 <= number < 1000:
        if 899 < number:
            romanAl += 'CM'
            number -= 900
        else:
            number -= 500
            romanAl += 'D'
    elif 100 <= number < 500:
        if 400 <= number:
            number -= 400
            romanAl += 'CD'
        else:
            number -= 100
            romanAl += 'C'
    elif 50 <= number < 100:
        if 89 < number:
            romanAl += 'XC'
            number -= 90
        else:
            number -= 50
            romanAl += 'L'
    elif 10 <= number < 50:
        if 40 <= number:
            number -= 40
            romanAl += 'XL'
        else:
            number -= 10
            romanAl += 'X'
    elif 5 <= number < 10:
        if number == 9:
            romanAl += 'IX'
            number -= 9
        else:
            number -= 5
            romanAl += 'V'
    elif 1 <= number < 5:
        if number == 4:
            number -= 4
            romanAl += 'IV'
        else:
            number -= 1
            romanAl += 'I'


print(romanAl)
