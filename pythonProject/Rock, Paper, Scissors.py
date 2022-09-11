import random

chiocelist_main = ['rock', 'paper', 'scissors']
pointU = 0
pointC = 0
def com_select(chiocelist):
    x = random.choice(chiocelist)
    return x

def determine_winner(user, com):
    print('User selected', user)
    print('Com selected', com)
    user_point = 0
    com_point = 0
    if user == com:
        print('Lies')
    elif com == 'rock':
        if user == 'paper':
            user_point += 1
            print('You\'ve added 1 point.')
        elif user == 'scissors':
            com_point += 1

    elif com == 'paper':
        if user == 'scissors':
            user_point += 1
            print('You\'ve added 1 point.')
        elif user == 'rock':
            com_point += 1

    elif com == 'scissors':
        if user == 'rock':
            user_point += 1
            print('You\'ve added 1 point.')
        elif user == 'paper':
            com_point += 1
    return user_point, com_point


while True:
    user_sel = int(input('Enter a choice (rock[0], paper[1], scissors[2]):'))
    f_value = determine_winner(chiocelist_main[user_sel], com_select(chiocelist_main))#Arrument: use_sel , x from com_select()

    pointU += f_value[0]
    pointC += f_value[1]
    print(pointU, pointC)
    print('---------------------')
    play_again = input("Play again? (Y/N): ")
    if play_again.lower() != 'y':
        break
if pointU > pointC:
    print('User gets victory.')
else:
    print('Com is got victory.')
