import pickle

class Vehiculos(object):
	"""docstring for Vehiculos"""
	def __init__(self,marca,modelo):
		
		self.marca=marca
		self.modelo=modelo
		self.enmarcha=False
		self.acelera=False
		self.frena=False
		

	def arrancar(self):
		self.enmarcha=True

	def acelerar(self):
		self.acelera=True

	def frenar(self):
		self.frena=True

	def estado(self):
		print("Marca: ",self.marca, "\n")
		print("Modelo: ",self.modelo, "\n")
		print("En Marcha : ",self.enmarcha, "\n")
		print("Acelerando: ",self.acelera, "\n")
		print("Frena: ",self.frena, "\n")


coche1=Vehiculos("Mazda","RX8")
coche2=Vehiculos("SEAT","A2")
coche3=Vehiculos("RENAULT","KANGOO")

coches=[coche1, coche2, coche3]


fichero = open("losCoches","wb")

pickle.dump(coches, fichero)

fichero.close()

del (fichero)

