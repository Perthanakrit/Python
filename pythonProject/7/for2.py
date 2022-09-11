result=""
inputRound = int(input("Number1 :"))
Num=int(input("Number2 :"))
print(list(range(5)))
for i in range(5):
    result += str(inputRound+Num*i+1) #result = result + str(inputRound+Num*i+1)
    print(result)