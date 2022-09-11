def mistake():
    for x in range(11):
        if x==0:
            for i in range(9):
                print(str(x)+str(i+1),end=' ')

        elif x >0 :
            print(' ')
            for j in range(10):
                print(str(x)+str(j),end=' ')

                if x==10 and j==0:
                    break
def new0():
    for x in range(10):
        for j in range(10):
            if j==9:
                print(str(x+1)+str(0), end=' ')
            else:
                print(str(x)+str(j+1),end=' ')

        print(' ')

def loopT():
    lenght = int(input())
    for i in range(lenght):
        if i == 0 or i == lenght - 1:
            for j in range(lenght):
                print('#', end='')
            print('')
        else:
            print('#' + ' ' * (lenght - 2) + '#')

rD = int(input())

num = 0
for i in range(rD):
    num = 2*i + 1
    rD -= 1
    print(rD*' '+'*'*num)
