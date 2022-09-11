'''
     *
    ***
   *****
  *******
   *****
    ***
     *
'''

number = int(input("range : "))
text = "*"
number2 = number-1
for x in range(number):
    y = 2*x+1
    number = number-1
    print(" "*number+(y*text))
    if x==number2:
        for i in range(number2):
            y-=2
            number = number + 1
            print(" " * number + (y * text))

