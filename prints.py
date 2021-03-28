from cfonts import *
import random

palabras = ["Hello","My name is","Joako"]
estilos = ["block","slick","tiny","grid","pallet","shade","chrome","simple","simpleBlock","3d","simple3d","huge","console"]
colores = ["cyan","red","green","yellow","#00f"]

for p in palabras:
	print(render(p,font=estilos[random.randint(0,len(estilos)-1)],colors=[colores[random.randint(0,len(colores)-1)],colores[random.randint(0,len(colores)-1)]],align='left'))