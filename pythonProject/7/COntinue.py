print(list(range(12)))
for X in range(12):
    break
    for Y in range(12):
        print(X+1,"x",Y+1," =",(X+1)*(Y+1))

for val in "hello":
    if val == "l":
        continue
    print(val)
print("The end")
