nof = int(input())
numlist = []
for i in range(nof):
    numBer = int(input())
    numlist.append(str(numBer))
text = ''.join(numlist)
for j in text[::-1]:
    print(j)


