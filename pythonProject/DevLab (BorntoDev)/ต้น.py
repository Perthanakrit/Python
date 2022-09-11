'''
   *
  ***
   *
  ***
 *****
   *
  ***
 *****
*******
   |
===V===

'''

number = int(input("range : "))
text = "*"
for y in range(number):
    x = number+1
    for i in range(2+y):
        sTar = 2*i+1
        x -= 1
        print(' '*x+text*sTar)
print(' '*number+'|')
print(number*'='+'V'+number*'=')
