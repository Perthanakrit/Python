text = str(input('text:'))
length = len(text)
num = 2 * length
for i in range(length):
    num -= 2
    print(' '*num, end='')
    for j in range(i, -1, -1):
        print(text[j]+' ', end="")
    for j in range(1, i+1):
        print(text[j], end=" ")

    print("")




