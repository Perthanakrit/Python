import matplotlib.pyplot as plt
import pandas as pd


data = pd.read_csv('Project_Anime_V.2_-Current.csv')

animename = []
scoretotal = []
for a in range(len(data['audience'])):
    name = data['Name'].loc[a]
    namelst = name.split(',')
    score = data['Score'].loc[a] 
    scorelst = score.split(',')   
    for n in namelst:
        animename.append(n)
    for s in scorelst:
        scoretotal.append(float(s))

colors = ( "orange", "gold", "yellow","lawngreen", "lime", "cyan","deepskyblue","blueviolet","violet","magenta","hotpink","bisque")
fig, ax = plt.subplots(figsize=(12, 6))

ax.barh(animename, scoretotal, color=colors)
ax.invert_yaxis()
for i in ax.patches:
    plt.text(i.get_width()+0.1, i.get_y()+0.5,
             str(round((i.get_width()), 2)),
             fontsize=10, fontweight='bold',
             color='black')
# Add Plot Title
ax.set_title('Audiences favorite Top 10 Anime', color='black')
plt.xlabel("Score")
plt.ylabel("Name")
plt.style.use('seaborn-ticks')

plt.show()
