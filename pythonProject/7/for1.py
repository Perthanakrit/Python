def basic_for():
    print(list(range(10)))
    for x in range(10): #นำสมาชิกตัวแรก(0)เข้าx
        print("hello",x+1)

def one_for():
    numbers = []
    for i in range(50):
        numbers.append(i+1)
    print(numbers)

one_for()


