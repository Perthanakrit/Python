'''if True:
    print("hello!")
    print("hi")
elif False:
    print("wait")
else:
    print("Bye")'''

'''input_1 =input("1:")
input_2 =input("2:")
input_3 =input("3:")
input_4 =input("4:")
input_5 =input("5:")'''

number = []
for i in range(5):
    x = input('input:')
    number.append(x)

number.sort()
number.reverse()
print(number)

