from serializar_objetos import Vehiculos

import pickle
ficheroApertura=open("losCoches","rb") #leemos los datos del archivo binario

misCoches=pickle.load(ficheroApertura)

ficheroApertura.close()

for a in misCoches:
	print (a.estado())