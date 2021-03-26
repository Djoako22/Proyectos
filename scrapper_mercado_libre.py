from bs4 import BeautifulSoup
import requests
import pandas as pd
import random
from time import sleep

pro_list = [];
pre_list = [];

def scrap(url='https://computacion.mercadolibre.com.ar/laptops/notebooks/', i=0):
    n=8
    print("Scraping... ",int((i/n)*100),"%")
    if(i==n):
    	print("Listo!")
    	return
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    lista = soup.select('li.ui-search-layout__item')
    for x in lista:
	    producto = x.select_one('h2.ui-search-item__title')
	    precio = x.select_one('span.price-tag.ui-search-price__part > span.price-tag-fraction')
	    pro_list.append(producto.text)
	    pre_list.append(str(precio.text))
    
    u = soup.select_one('li.andes-pagination__button.andes-pagination__button--next > a')
    url=str(u['href'])
    i=i+1
    if(i%4==0):
    	sleep(random.uniform(8.0, 12.0))
    return scrap(url,i)


n = int(input('Desea Scrapear:\n1) Si\n2) No\n'))
while(n!=1):
	n = int(input('Desea Scrapear:\n1) Si\n2) No\n'))

if(n==1):
	scrap()
	df = pd.DataFrame({'Productos': pro_list, 'Precios': pre_list})
	
	
m = int(input('Que desea hacer:\n1) Imprimir la lista por consola\n2) Convertir la lista a csv\n'))
while(m!=1 and m!=2):
	m = int(input('Que desea hacer:\n1) Imprimir la lista por consola\n2) Convertir la lista a csv\n'))

if(m==1):
    print(df)
if(m==2):
	nombre = input('Ingrese nombre para el archivo:\n')
	df.to_csv(str(nombre)+'.csv')
