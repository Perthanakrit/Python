import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 
import ast

data = pd.read_csv('mal_top2000_anime.csv')
df = pd.DataFrame(data)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
explode = (0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05)
colors = ( "orange", "gold", "yellow","lawngreen", "lime", "cyan","deepskyblue","blueviolet","violet","magenta","hotpink","bisque")

'''def bar():
    for m in months:
        num = 0
        for j in range(10):
            lst = df['Air Date'].loc[j].split(' ')
            if m == lst[0]:
                num += 1
            elif m != lst[0]:
                num += 0 
        numofanime.append(num)'''

def histogram(): 
    numofanime = []
    for month in months:
        num = 0
        for j in range(len(df['Air Date'])):
                lst = df['Air Date'].loc[j].split(' ')
                if len(lst) > 1:
                    if month == lst[0]:
                        num += 1
        numofanime.append(num)
    return numofanime

plt.pie(histogram(), labels=months, autopct='%1.1f%%',pctdistance=0.85, explode=explode, colors=colors )
# draw circle
centre_circle = plt.Circle((0, 0), 0.75, fc='white')
fig = plt.gcf()
# Adding Circle in Pie chart
fig.gca().add_artist(centre_circle)

plt.show()