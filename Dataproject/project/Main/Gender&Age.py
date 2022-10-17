import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 

data = pd.read_csv("Project_Anime_V.2_-_Project_Anime__1.csv")

barWidth = 0.25


# set width of bar
barWidth = 0.25
fig = plt.subplots(figsize =(12, 8))
 
# set height of bar
age = ['15','16','17','18']
malelst, femalelst = [],[]

for a in age:
        male, female = 0, 0
        for i in range(len(data['audience'])):
                if a==str(data['Age'].loc[i]):
                        if data['Gender'].loc[i] == 'Male':
                                male += 1
                        elif data['Gender'].loc[i] == 'Female':
                                female += 1
        malelst.append(male)
        femalelst.append(female)
             
print(malelst,femalelst)
'''
# Set position of bar on X axis
br1 = np.arange()
br2 = [x + barWidth for x in br1]

# Make the plot
plt.bar(br1, Male, color ='#33CCFF', width = barWidth,
        edgecolor ='grey', label ='Male')
plt.bar(br2, Female, color ='#FF9966', width = barWidth,
        edgecolor ='grey', label ='Female')
 
# Adding Xticks
plt.xlabel('Age', fontweight ='bold', fontsize = 15)
plt.ylabel('count', fontweight ='bold', fontsize = 15)
plt.xticks([r + barWidth/2 for r in range(len(Male))],
        ['15', '16', '17', '18'],)
plt.title("Gender and Age")
plt.legend()
plt.show()'''
