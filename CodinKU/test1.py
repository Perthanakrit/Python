import matplotlib.pyplot as plt
import numpy as np

listI = []
numof = int(input())

for i in range(numof):
    pos = int(input())
    listI.append(pos)

def plotGarph(listG):
    listPoint = []
    colorlist = ['red', 'green', 'blue', 'yellow','pink','olive']
    posP = len(listG) + 2
    for n in range(len(listG)):
        posP -= 1
        m1, c1 = 0.1 * listI[n], posP
        x = np.linspace(0, 10)

        plt.plot(x, x * m1 + c1, color=colorlist[n])
        plt.xlim(0, 10)
        plt.ylim(0, 10)
         
    plt.show()


plotGarph(listI)