'''
  *
 ***
*****
'''

number = int(input())
for x in range(number):
    text = ""
    for y in range(x+1):
        text = text+"*"
    print(text)


