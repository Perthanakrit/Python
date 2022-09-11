try:
    input1 = int(input("A :"))
    input2 = int(input("B :"))
    print(input1 / input2)
except ValueError:
    print("Error ! Please Re-Enter Number")
except ZeroDivisionError:
    print("Error ! You Can’t Enter 0")
except:
    print("Error !")