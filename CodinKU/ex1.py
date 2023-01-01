from time import process_time

t1_start = process_time()

N, T = map(int, input().split())
listNum =[]

for i in range(N):
    numInput = int(input())
    listNum.append(numInput)
print(listNum)
print(" ")

def fun1(nums, fistNum):
    #print(nums)
    currN = fistNum
    for n in nums:
        if (currN - 1 == n):
            print("0")
        elif (currN + 1 == n):
            print("1")
        currN = n

def fun2(nums2, fistNum2):
    prenumY = fistNum2;
    currNY = nums2[0]
    numZ = currNY; #Y=Z (1)
    for z in range(len(nums2)):
        if(z==0): 
            currNY = nums2[z]
            if (currNY - 1 == prenumY):
                print("1")
            elif (prenumY - 1 == currNY):
                print("0")
        else:
            if (currNY - 1 == prenumY):
                print("1") 
                prenumY = currNY
                currNY = nums2[z] - (2*prenumY)
            elif (prenumY - 1 == currNY):
                print("0")
                prenumY = currNY
                currNY = nums2[z] - prenumY
        
                         
if(T==1):
    fun1(listNum, N)
elif(T==2):
    fun2(listNum, N)

t1_stop = process_time()

print(t1_stop-t1_start)
