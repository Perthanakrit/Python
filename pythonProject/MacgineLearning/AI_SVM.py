import pandas as pd
import matplotlib.pyplot as plt
from sklearn import svm 

df = pd.read_csv('pythonProject\MacgineLearning\dataset.csv')

w_yes = df[df.profit == 'y'][['weight']] #weight,price & profit=='y'
p_yes = df[df.profit == 'y'][['price']]
w_no = df[df.profit == 'n'][['weight']] #weight,price & profit=='n'
p_no = df[df.profit == 'n'][['price']]
y_yes = df[df.profit == 'y'][['weight']]
x_yes = df[df.profit == 'y'][['price']]

#svm 
x = df[['weight', 'price']]
y = df['profit']
model = svm.SVC(kernel='linear')
model.fit(x,y)
#svm predict
a = model.predict([[2500,600]])
b = model.predict([[2500,300]])
lst = list(a)
print(type(lst))
print(lst)
print(a,b, sep='\n', end='\n')

def foundPrice():
    numInput = input('price: ')
    numInput = int(numInput)
    while True:
        c = model.predict([[2500,numInput]])
        print(numInput,c, sep='\n')
        lst = list(c)
        numInput += 10
        if(lst[0] == 'n'):
            break

fdoundPrice()

#plot
'''plt.scatter(w_yes, p_yes, marker='o', color='g')
plt.scatter(w_no, p_no, marker='o', color='r')
plt.xlabel("Weight")
plt.ylabel("Price")

plt.show()'''
