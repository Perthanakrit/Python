x = int(input('Enter number :'))
groupN = int(input('number of classification'))
dictD = {}
for i in range(groupN):
    f, t, className = input('valve1 :').split()
    f, t = int(f), int(t)
    dictD[className] = f, t
for j, k in dictD.items():
    if k[0] <= x <= k[1]:
        print(j)
