'''
5
1
2
1
3
1
pass:1
print=> 1,3,5
'''

nofg = int(input('Enter number of goods: '))
passwordLsit = []
for i in range(nofg):
    password_G = int(input('password:'))
    passwordLsit.append(password_G)
print(passwordLsit)
g_P = int(input('Enter Product code: '))


def finding_G():
    listX = []
    for j in range(len(passwordLsit)):
        if passwordLsit[j] == g_P:
            listX.append(str(j+1))
        text = ','.join(listX)
    print('Position:',text)



if g_P in passwordLsit :
    finding_G()
else:
    print("Not Found")