'''
  *    2(0)+1          x=2, number=3
 ***   2(1)+1           y=5
*****                   number=3-1
                        " "*2+(5*"*")
'''
number = int(input("range : "))
text = "*"
for x in range(number):
    y = 2*x+1
    number = number-1
    print(" "*number+(y*text))



