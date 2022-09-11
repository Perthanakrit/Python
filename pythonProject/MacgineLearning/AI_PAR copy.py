import pandas as pd
import matplotlib.pyplot as plt
from sklearn import svm 

df = pd.read_csv("pythonProject\MacgineLearning\dtrainDataTest.csv")

markers=['o','o','o','o','o','o']
colors=['g','g','g','g','g','g']

x1_yes = df[df.par_state == 'par'][['x1']]
y1_yes = df[df.par_state == 'par'][['y1']] #weight,price & profit=='y'
z1_yes = df[df.par_state == 'par'][['z1']]
x2_yes = df[df.par_state == 'par'][['x2']]
y2_yes = df[df.par_state == 'par'][['y2']]  #weight,price & profit=='n'
z2_yes = df[df.par_state == 'par'][['z2']]
x1_no = df[df.par_state == 'normal'][['x1']]
y1_no = df[df.par_state == 'normal'][['y1']] #weight,price & profit=='y'
z1_no = df[df.par_state == 'normal'][['z1']]
x2_no = df[df.par_state == 'normal'][['x2']]
y2_no = df[df.par_state == 'normal'][['y2']]  #weight,price & profit=='n'
z2_no = df[df.par_state == 'normal'][['z2']]



#plot
plt.scatter(x1_yes,y1_yes,z1_yes, marker='o', color='g')
plt.scatter(x2_yes,y2_yes,z2_yes, marker='o', color='g')
plt.scatter(x1_no,y1_no,z1_no, marker='*', color='r')
plt.scatter(x2_no,y2_no,z2_no, marker='*', color='r')
#plt.scatter(a1_no, a2_no, marker='o', color='r')
plt.xlabel("a1")
plt.ylabel("a2")

plt.show()
