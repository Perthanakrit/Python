from sympy import symbols, solve
def sloved_by_sympy():
    N, M, Y = int(input('ผลต่างอายุPersent:')), int(input('ต่างกันกี่Mเท่า:')), int(input('Y years ago:'))
    B_Persent = symbols('b')
    A_Past = M*(B_Persent-Y)+Y
    print(A_Past)
    b = A_Past-1-B_Persent
    sol_B = solve(b)
    a = sol_B[0]+N

    print(a, sol_B[0])

N, M, Y = [int(i) for i in input().split()]
def solveE(numN, numM, numY):
    b = (numY*(1-numM)-numN)/(1-numM)
    a = b + numN
    return int(a), int(b)

print(solveE(N, M, Y)[0],solveE(N, M, Y)[1])

