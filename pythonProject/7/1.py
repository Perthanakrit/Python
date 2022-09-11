number = int(input("ความสูงพีระมิด: "))
hight = number
text = "*"
print(list(range(number)))
for i in range(number):
    y = 2*i+1
    number = number - 1 #number = number - 1
    print("."* number + y * text)
print(" ")
print(f"พีระมิดสูง: {hight} บล็อก")
