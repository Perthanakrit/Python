import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 

df = pd.read_csv('data-firearm.csv')
# x axis values
x = [1,2,3]
# corresponding y axis values
y = [2,4,1]
  
# plotting the points 
plt.plot(x, y)
  
# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')
  
# giving a title to my graph
plt.title('My first graph!')
plt.legend()
# function to show the plot
# plt.show()
year = 9
for y in range(12):
    year += 1
    num = 0
    for n in range(12):      
        num += 1   
        if year == 21 and num > 6:
           break    
        if num > 9:
            print('20'+str(year)+'-'+str(num))
        else:
            print('20'+str(year)+'-0'+str(num))

