import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 

df = pd.read_csv('data-firearm.csv')
df.fillna(0, inplace = True)

c = ['#00FF44','#FF0000','#FF00F7','#266FFF','#EAFF26']

statelst = []
for s in range(7536):
 statelst.append(df['state'].loc[s])
statelst = list(set(statelst))
statelst.sort()

hglst, longg, other_g, mtp = [], [], [], []

for st in statelst:
    h = l = o = m = 0
    for i in range(7536):
        if st == df['state'].loc[i]:
              h += df['handgun'].loc[i]
              l += df['long_gun'].loc[i] 
              o += df['other'].loc[i]
              m += df['multiple'].loc[i]
    hglst.append(h)
    longg.append(l)
    other_g.append(o)
    mtp.append(m)

hg = np.array(hglst)
longgun = np.array(longg)
other = np.array(other_g)
multiple = np.array(mtp)

plt.barh(statelst, hg, color = 'b')
plt.barh(statelst, longgun, left=hg, color = 'g')
plt.barh(statelst, other, left=hg+longgun, color = 'y')
plt.barh(statelst, multiple, left=hg+longgun+other, color = 'r')

plt.xlabel("Guns")
plt.ylabel("Number")
plt.legend(['handgun','long_gun','other','multiple'])
plt.show()