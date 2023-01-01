def func1():
    x=0
    star = 21
    blank = int(star/2)
    for i in range(0,3):  
        x = 2*(i) + 1
        blank -= 1 
        print(blank*" "+"*"*x)

    star_2 = star 
    for j in range(0,3):
        star_2 = star_2 - 1 *i  
        print((j)*" "+star_2*"*")
    star_2 = 5
    blank_2 = 3
    blank_3 = 5
    for k in range(3):     
        blank_2 -= 1    
        print(blank_2*" "+ star_2*"*"+blank_3*" "+ star_2*"*")
        star_2 -= 2
        blank_3 += 6

def func2():
    star = 21
    for i in range(star//2, star, 2):
        print(' '*(star//2 - i) + '*'*(i*2 + 1))

    # Print the base of the tree
    for i in range(star//2, -1, -2):
        print(' '*(star//2 - i) + '*'*(i*2 + 1))

    # Print the body of the tree
    for i in range(star//2):
        quotient, remainder = divmod(star - (i*2 + 1), 2)
        print(' '*i + '*'*(i*2 + 1) + ' '*quotient + '*'*(i*2 + 1))




func2()