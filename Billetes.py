pesos5000 = "[⁵⁰⁰⁰($)   ]"
pesos1000 = "[¹⁰⁰⁰($)   ]"
pesos500 = "[⁵⁰⁰($)   ]"
pesos100 = "[¹⁰⁰($)   ]"
pesos50 = "[⁵⁰($)  ]"
pesos10 = "[¹⁰($)  ]"
pesos5 = "[⁵ ($)  ]"
pesos1 = "(1$)"

dinero = int(input("Cuanto dinero necesita?\n"))

while(dinero>0):
	if(dinero>=5000):
		print(pesos5000)
		dinero -= 5000
	elif(dinero>=1000):
		print(pesos1000)
		dinero -= 1000
	elif(dinero>=500):
		print(pesos500)
		dinero -= 500
	elif(dinero>=100):
		print(pesos100)
		dinero -= 100
	elif(dinero>=50):
		print(pesos50)
		dinero -= 50
	elif(dinero>=10):
		print(pesos10)
		dinero -= 10
	elif(dinero>=5):
		print(pesos5)
		dinero -= 5
	else:
		print(pesos1)
		dinero -= 1



