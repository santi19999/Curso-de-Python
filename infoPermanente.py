import pickle

class Persona:
	def __init__(self, nombre, genero, edad):
		self.nombre=nombre
		self.genero=genero
		self.edad=edad
		print("Se a creado una persona con el nombre de ", self.nombre)



persona1=Persona("juan","masculino",26)