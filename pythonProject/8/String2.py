name = input("Fristnamme :").capitalize()
lastName =input("Lastname :").capitalize()
print("Hello ! %s %s!"%(name,lastName))

text ="Per"
textFormatted="Welocme %s"%name
print(textFormatted.center(21,"-"))
print(len(name+lastName))