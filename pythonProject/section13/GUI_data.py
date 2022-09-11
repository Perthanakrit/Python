from tkinter import *
import pandas as pd
import ast
import random

app = Tk()
app.title('recommendation')
app.geometry('720x500')

def recommendation_anime(event):
    global app
    data = pd.read_csv('mal_top2000_anime.csv')

    def loop(para_list):
        gen, anime_name = [], []
        for n in range(len(para_list)):
            for g in para_list[n]:
                gen.append(g)
        gen = list(set(gen))

        for a in gen:
            for d in range(len(data)):
                lst_year = data['Air Date'].loc[d]
                lst_year = lst_year.split(' ')
                if len(lst_year) >= 3:
                    if int(lst_year[2]) >= 2010:
                        if a in data['Genres'].loc[d]:
                            anime_name.append(data['Name'].loc[d] + ' ' + data['Genres'].loc[d])
                elif len(lst_year) == 1:
                    if int(lst_year[0]) >= 2010:
                        if a in data['Genres'].loc[d]:
                            anime_name.append(data['Name'].loc[d] + ' ' + data['Genres'].loc[d])
                elif len(lst_year) == 2:
                    if int(lst_year[1]) >= 2010:
                        if a in data['Genres'].loc[d]:
                            anime_name.append(data['Name'].loc[d] + ' ' + data['Genres'].loc[d])
        name_lst = list(set(anime_name))
        return name_lst

    # input anime name
    name = textName.get()
    print('anime: ', name)
    genrelst = []
    for i in range(len(data)):
        if name in data['Name'].loc[i]:
            lst = ast.literal_eval(data['Genres'].loc[i])
            genrelst.append(lst)
    print(': ', genrelst)
    #
    name_random = loop(genrelst)
    print(len(name_random))
    #
    list_animename = []
    lstnum = []
    while True:
        if len(set(lstnum)) == 50:
            break
        num_random = random.randint(0, 99)
        lstnum.append(num_random)
    for r in set(lstnum):
        list_animename.append(name_random[r])
    return list_animename

def leftClick(event):
    txt.delete("1.0", "end")
    text_anime = "\n".join(recommendation_anime(event))
    # label_anime.configure(text=text_anime)
    # text
    txt.insert(END, text_anime)

# Anime name & search button
var = StringVar()
label = Label(app, text="Anime name", font='30', bg='#C6E2FF').pack()
textName = Entry(app, textvariable=var)
textName.pack()
searchButton = Button(app, text='search', bg="#FFFF99")
searchButton.pack(expand=True)
searchButton.bind('<Button-1>', leftClick)
searchButton.pack()
# text 'Recommended'
labelResult = Label(app, text="Recommended", font="40", bg='#C6E2FF')
labelResult.pack()

# Add a Scrollbar(horizontal)
scroll = Scrollbar(app, orient='vertical')
# scroll.pack(side=RIGHT, fill='y')
# text widget
txt = Text(app, height=50, width=120, font=("Georgia, 16"), yscrollcommand=scroll.set)
txt.pack()
# scroll.config(command=txt.yview)
# Background
app.configure(bg='#C6E2FF')

app.mainloop()

