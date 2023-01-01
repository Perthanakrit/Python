runF = True


def running(runNow):
    x = 0
    while runNow:
        x += 1
        print(x)
        if (x == 10): 
            runNow = False
    print(runNow)

running(runF)
print(runF)