def recursive_func(num):
    if num > 0:
        return num * recursive_func(num - 1)

    else:
        return 1

print(recursive_func(5))


def display_student(name, age):
    print(name, age)


