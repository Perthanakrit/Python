import random
import re
mylist = ['adult', 'agent', 'anger', 'apple', 'award', 'basis', 'beach', 'birth', 'block', 'blood', 'board', 'brain', 'bread', 'break', 'brown', 'buyer', 'cause', 'chain', 'chair', 'chest', 'chief', 'child',
              'china', 'claim', 'class', 'clock', 'coach', 'coast', 'court', 'cover', 'cream', 'crime', 'cross','crowd', 'crown', 'cycle', 'dance', 'death', 'depth', 'doubt', 'draft', 'drama', 'dream', 'dress','drink', 'drive', 'earth', 'enemy', 'entry', 'error', 'event', 'faith', 'fault', 'field', 'fight',
              'final', 'floor', 'focus', 'force', 'frame', 'frank', 'front', 'fruit', 'glass', 'grant', 'grass',
              'green', 'group', 'guide', 'heart', 'henry', 'horse', 'hotel', 'house', 'image', 'index', 'input',
              'issue', 'japan', 'jones', 'judge', 'knife', 'laura', 'layer', 'level', 'lewis', 'light', 'limit',
              'lunch', 'major', 'march', 'match', 'metal', 'model', 'money', 'month', 'motor', 'mouth', 'music',
              'night', 'noise', 'north', 'novel', 'nurse', 'offer', 'order', 'other', 'owner', 'panel', 'paper',
              'party', 'peace', 'peter', 'phase', 'phone', 'piece', 'pilot', 'pitch', 'place', 'plane', 'plant',
              'plate', 'point', 'pound', 'power', 'press', 'price', 'pride', 'prize', 'proof', 'queen', 'radio',
              'range', 'ratio', 'reply', 'right', 'river', 'round', 'route', 'rugby', 'scale', 'scene', 'scope',
              'score', 'sense', 'shape', 'share', 'sheep', 'sheet', 'shift', 'shirt', 'shock', 'sight', 'simon',
              'skill', 'sleep', 'smile', 'smith', 'smoke', 'sound', 'south', 'space', 'speed', 'spite', 'sport',
              'squad', 'staff', 'stage', 'start', 'state', 'steam', 'steel', 'stock', 'stone', 'store', 'study',
              'stuff', 'style', 'sugar', 'table', 'taste', 'terry', 'theme', 'thing', 'title', 'total', 'touch',
              'tower', 'track', 'trade', 'train', 'trend', 'trial', 'trust', 'truth', 'uncle', 'union', 'unity',
              'value', 'video', 'visit', 'voice', 'waste', 'watch', 'water', 'while', 'white', 'whole', 'woman',
              'world', 'youth']
correct = ['-','-','-','-','-']
#hang = ['  0', '\n/', '|', '', '\n/', ' /']
def hanger():
    print('------')
    for i in range(7):
        if i > 0:
            print('|')
        else:
            print('|',' '*3+'|')
def hangman():
    pass
def hangman_guess(list):
    print(list)
    wrong = 0
    word = random.choice(list)
    print(word)
    for i in range(5):
        x = input('char:')
        if re.findall(x, word):
            for j in range(5):
                if x == word[i]:
                    correct[j] = x
                    print(*correct, sep='')
        else:
            wrong += 1
            hangman()

hangman_guess(mylist)
