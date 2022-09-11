import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('data-firearm.csv')
df.fillna(0, inplace = True)

hglst, longg, other_g, mtp = [], [], [], []

year = 9
for i in range(7536):
    for y in range(12):
        h = l = o = m = 0
        year += 1
        num = 0
        for n in range(12):
            num += 1
            for i in range(55):
                if num > 9:
                    if df['month'].loc[i] == '20'+str(year)+'-'+str(num):
                       
                        h += df['handgun'].loc[i]
                        l += df['long_gun'].loc[i] 
                        o += df['other'].loc[i]
                        m += df['multiple'].loc[i]
                else:
                    if df['month'].loc[i] == '20'+str(year)+'-0'+str(num):
                        
                        h += df['handgun'].loc[i]
                        l += df['long_gun'].loc[i] 
                        o += df['other'].loc[i]
                        m += df['multiple'].loc[i]

    hglst.append(h)
    longg.append(l)
    other_g.append(o)
    mtp.append(m)

 # if df['month'].loc[i] == '2020-01' or '2020-02' or '2020-03' or '2020-04' or '2020-05' or '2020-06' or '2020-07' or '2020-08' or '2020-09' or '2020-10' or '2020-11' or '2020-12':

# รวมปืนแต่ชนิด
def tatol(gun):
    result = 0
    for g in gun:
        result += g
    return result

def graph_eachyear():
    y = np.array([tatol(hglst), tatol(longg), tatol(other_g),tatol(mtp)])
    plt.pie(y, labels = ['hand_gun', 'long_gun','other','multiple'])

def graph_years():
    x = ['2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021']
    
    plt.plot(x, tatol(hglst), label = "hand_gun")
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.legend()
    plt.show()

graph_years()

