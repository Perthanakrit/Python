numbers =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
numbers.sort() # Number must be sorted first.

def binary_search(numbers_list, number, left, right):
    if left > right :
        return  -1

    mid = (left+right) // 2
    if number == numbers_list[mid]:
        return mid
    elif number < numbers_list[mid]:
        return binary_search(numbers_list,number,left, mid-1)
    else:
        return binary_search(numbers_list, number, mid+1,right)

print(binary_search(1, 2, 3, 4))