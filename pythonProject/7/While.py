correctNumber=17
userGuess =0
while userGuess!=correctNumber:
    userGuess = int(input("Please guess a number :"))
    if userGuess > correctNumber:
        print("Too large")
    elif userGuess < correctNumber:
        print("Too small")
    elif userGuess == correctNumber:
        print("Correct !!")