import random
mylist = ['adult', 'agent', 'anger', 'apple', 'award', 'basis', 'beach', 'birth', 'block', 'blood', 'board', 'brain', 'bread', 'break', 'brown', 'buyer', 'cause', 'chain', 'chair', 'chest', 'chief', 'child', 'china', 'claim', 'class', 'clock', 'coach', 'coast', 'court', 'cover', 'cream', 'crime', 'cross','crowd', 'crown', 'cycle', 'dance', 'death', 'depth', 'doubt', 'draft', 'drama', 'dream', 'dress','drink', 'drive', 'earth', 'enemy', 'entry', 'error', 'event', 'faith', 'fault', 'field', 'fight',
      'final', 'floor', 'focus', 'force', 'frame', 'frank', 'front', 'fruit', 'glass', 'grant', 'grass','green', 'group', 'guide', 'heart', 'henry', 'horse', 'hotel', 'house', 'image', 'index', 'input', 'issue', 'japan', 'jones', 'judge', 'knife', 'laura', 'layer', 'level', 'lewis', 'light', 'limit','lunch', 'major', 'march', 'match', 'metal', 'model', 'money', 'month', 'motor', 'mouth', 'music', 'night', 'noise', 'north', 'novel', 'nurse', 'offer', 'order', 'other', 'owner', 'panel', 'paper', 'party', 'peace', 'peter', 'phase', 'phone', 'piece', 'pilot', 'pitch', 'place', 'plane', 'plant','plate', 'point', 'pound', 'power', 'press', 'price', 'pride', 'prize', 'proof', 'queen', 'radio','range', 'ratio', 'reply', 'right', 'river', 'round', 'route', 'rugby', 'scale', 'scene', 'scope','score', 'sense', 'shape', 'share', 'sheep', 'sheet', 'shift', 'shirt', 'shock', 'sight', 'simon',
          'skill', 'sleep', 'smile', 'smith', 'smoke', 'sound', 'south', 'space', 'speed', 'spite', 'sport','squad', 'staff', 'stage', 'start', 'state', 'steam', 'steel', 'stock', 'stone', 'store', 'study', 'stuff', 'style', 'sugar', 'table', 'taste', 'terry', 'theme', 'thing', 'title', 'total', 'touch','tower', 'track', 'trade', 'train', 'trend', 'trial', 'trust', 'truth', 'uncle', 'union', 'unity','value', 'video', 'visit', 'voice', 'waste', 'watch', 'water', 'while', 'white', 'whole', 'woman','world', 'youth']
blank = ['_', '_', '_', '_', '_']

def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]
def hanger(hangmanlist,hp,numinLst):
    human = ['O', 'I', '/', '\\', '/', ' ' + '\\']
    for h in range(len(human)):
        if h == hp:
            hangmanlist[numinLst+h] = human[hp]
    print(''.join(hangmanlist))

def play(listA):
    c_word = random.choice(listA)
    c_word = c_word.upper()
    word_lst = list(c_word)
    print(word_lst)
    incorrect = 6
    print("Let's start ")
    print(display_hangman(incorrect))
    for chk in range(6):
        letter = str(input('letter:'))
        letter = letter.upper()
        if letter in c_word:
            for i in range(len(c_word)):
                if letter == word_lst[i]:
                    blank[i] = letter
            print(' '.join(blank))
        else:
            incorrect -= 1
            print(display_hangman(incorrect))

play(mylist)
