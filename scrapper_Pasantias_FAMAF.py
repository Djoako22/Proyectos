from bs4 import BeautifulSoup
import requests
import pandas as pd
import random
from time import sleep

t_list = []
f_list = []
e_list = []

def scrap(url='https://www.famaf.unc.edu.ar/search/?query=Pasant%C3%ADa', i=0):
    if(i==2):
    	return
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    lista = soup.select('div.card-content')
    for x in lista:
	    titulo = x.select_one('h3.title')
	    fecha = list(x.stripped_strings)
	    enlace = x.select_one('h3.title > a')
	    t_list.append(titulo.text)
	    f_list.append(fecha[0])
	    e_list.append('https://www.famaf.unc.edu.ar' + str(enlace['href']))
    
    u = soup.select_one('a.pagination-next')
    url = 'https://www.famaf.unc.edu.ar/search/' + str(u['href'])
    i=i+1
    
    sleep(random.uniform(2.0, 4.0))
    return scrap(url,i)

scrap()

df = pd.DataFrame({'Titulos': t_list, 'Fechas': f_list, 'Enlaces': e_list})
df = df.set_index('Titulos')
print(df)
#df.to_csv('Lista.csv')
