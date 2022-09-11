import matplotlib.pyplot as plt
import pandas as pd

# Red CSV into pandas
data = pd.read_csv("Project_Anime_.csv")
data.head()
df = pd.DataFrame(data)

Name = df['Name'].head(10)
Score = df['Score'].head(10)
colors = ( "orange", "gold", "yellow","lawngreen", "lime", "cyan","deepskyblue","blueviolet","violet","magenta","hotpink","bisque")
fig, ax = plt.subplots(figsize=(12, 6))


ax.barh(Name, Score, color=colors)


# Add x, y gridlines
ax.grid(b=True, color='black',
        linestyle='-.', linewidth=0.5,
        alpha=0.2)

# Show top values
ax.invert_yaxis()

# Add annotation to bars
for i in ax.patches:
    plt.text(i.get_width()+0.2, i.get_y()+0.5,
             str(round((i.get_width()), 2)),
             fontsize=10, fontweight='bold',
             color='red')

# Add Plot Title
ax.set_title('Audiences favorite Top 10 Anime', color='black')
plt.xlabel("Score")
plt.ylabel("Name")
plt.style.use('seaborn-ticks')


# Show Plot
plt.show()