from pickle import TRUE
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import svm

df = pd.read_csv('pythonProject\MacgineLearning\dtrainDataTest(2).csv')
numof = len(df['x1'])
print('total',numof)

x = df[['x1', 'y1', 'z1', 'x2', 'y2', 'z2']]
y = df[['par_state']]

model = svm.SVC(kernel = 'linear')
#อย่าลืมแปลง y ให้เป็น n_shape
model.fit(x, y.values.ravel())

num = 1

for i in range(numof):
    
    x1,y1,z1,x2,y2,z2 = df['x1'].loc[i],df['y1'].loc[i],df['z1'].loc[i],df['x2'].loc[i],df['y2'].loc[i],df['z2'].loc[i]
    answer = model.predict([[x1,y1,z1,x2,y2,z2]])
    print(num,answer)
    num += 1


