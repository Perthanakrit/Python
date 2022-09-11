import pandas as pd 
import ast
import random

data = pd.read_csv('mal_top2000_anime.csv')
df = pd.DataFrame(data)

def main():
    def loop(para_list):
        gen, anime_name = [], []
        for n in range(len(para_list)):
            for g in para_list[n]:
                gen.append(g)
        gen = list(set(gen))
        print('genre',gen)
        for a in gen:
            for d in range(len(data)):
                lst_year = data['Air Date'].loc[d]
                lst_year = lst_year.split(' ')
                if len(lst_year) >= 3:
                    if int(lst_year[2])  >= 2010:           
                            if a in data['Genres'].loc[d]:
                                anime_name.append(data['Name'].loc[d])
                elif len(lst_year) == 1:
                    if int(lst_year[0]) >= 2010:
                        if a in data['Genres'].loc[d]:
                            anime_name.append(data['Name'].loc[d])
                elif len(lst_year) == 2:
                    if int(lst_year[1]) >= 2010:
                        if a in data['Genres'].loc[d]:
                            anime_name.append(data['Name'].loc[d])
        name_lst = list(set(anime_name))           
        return name_lst

    name = str(input('anime name: '))
    genrelst = []
    for i in range(len(data)):
        if name in data['Name'].loc[i] :
            lst = ast.literal_eval(data['Genres'].loc[i])
            genrelst.append(lst)          
    name_random = loop(genrelst)
    for r in range(50):
        num_random = random.randint(0,99)
        print(name_random[num_random])

