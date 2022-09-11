import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
df = pd.read_csv('Project_Anime_.csv')

df.set_index('Name', inplace =True)
colors = ( "orange", "gold", "yellow","lawngreen", "lime", "cyan","deepskyblue","blueviolet","violet","magenta","hotpink","bisque")


df[:10]["Score"].plot(kind="barh", title="Audiences favorite Top 10 Anime ")
df[:10]["Score"].plot(kind="barh",figsize=(10,5), color=colors)
plt.xlabel("Score")
plt.ylabel("Name")

plt.show()