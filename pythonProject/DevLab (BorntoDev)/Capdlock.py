text = str(input())
for x in text:
    if x.islower():
        print(x.upper(),end="")
    elif x ==" ":
        print(" ",end="")
    elif x.isupper():
        print(x.lower(),end="")
