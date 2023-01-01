'''x=0
blank = 6
for i in range(0,4):  
    x = 2*(i) + 1
    blank -= 1 
    print(blank*" "+"*"*x)

print(' '+9*'*')

for k in range(2):
    print(int(9//2)*' '+ '***')'''

for i in range(4):
    if i == 3:
        print('{:^{}}'.format('*'*9, 9))  # Center-align the middle of the tree
    else:
        print('{:^{}}'.format('*'*(2*i + 1), 9)) 