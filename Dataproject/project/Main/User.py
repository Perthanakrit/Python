import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 
import ast

df = pd.read_csv('Project_Anime_.csv')
data = pd.read_csv('Project_Anime_V.2_-Current.csv')

colors = ("orange", "gold", "yellow","lawngreen", "lime", "cyan","deepskyblue","blueviolet","violet","magenta","hotpink","bisque")

def finding_genre():
    fig = plt.figure()
    fig.patch.set_facecolor('xkcd:mint green')
    genrelst = []
    for g in range(len(df)):
        lst_g = ast.literal_eval(df['Genre'].loc[g])
        for j in lst_g:
            genrelst.append(j)
    label = list(set(genrelst))   
    label.sort()
    numof = []
    for gen in label:
        num = 0
        for a in range(len(df['Genre'])):
            lst = ast.literal_eval(df['Genre'].loc[a]) 
            for i in lst:    
                if gen  == i: 
                    num += 1
        numof.append(num)
    npnumof = np.array(numof)
    # explode
    myexplode = []  
    for j in range(len(label)):
        myexplode.append(0)
    myexplode[0],myexplode[3], myexplode[4] = 0.15, 0.05, 0.05
    print(myexplode)
    #pie chart
    plt.style.use('_mpl-gallery')
    plt.pie(npnumof, autopct='%.1f%%', labels = label,explode = myexplode, colors = colors, startangle = 0)
    plt.show()

def finding_genre_v2():
    genrelst = []
    for g in range(len(df)):
        lst_g = ast.literal_eval(df['Genre'].loc[g])
        for j in lst_g:
            genrelst.append(j)
    label = list(set(genrelst))   
    label.sort()    
    numof = []
    print(label)
    for gen in label:
        num = 0
        for a in range(len(data['audience'])):
            tup = ast.literal_eval(data['Genre'].loc[a]) 
            for lst in tup:
                for ge in lst:   
                    if ge  == gen: 
                        num += 1
        numof.append(num)
    print(numof)
    npnumof = np.array(numof)
    # explode
    myexplode = []  
    for j in range(len(label)):
        myexplode.append(0)
    myexplode[3],myexplode[0], myexplode[8] = 0.15, 0.05, 0.075
    plt.pie(npnumof, autopct='%.1f%%', labels = label,explode = myexplode, colors = colors, startangle = 0)
    plt.show()

finding_genre_v2()




























'''txt = df['Genre'].loc[0]
txt = txt.replace("['",'')
txt = txt.replace("']",'')
txt = txt.replace("'",'')

print(txt.split(','))
print(type(txt))'''

'''str1 = df['Genre'].loc[0]
list1 = ast.literal_eval(str1) 
print(type(list1))
print(list1)'''


