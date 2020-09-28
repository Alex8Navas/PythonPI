# Clase 40. Curso Píldoras Informáticas.

# Control de Flujo. Serialización 2.

import pickle

class FactoryV():

	def __init__(self, marca, modelo):

		self.marca = marca
		self. modelo = modelo
		self.enmarcha = False
		self.acelera = False
		self.decelera = False

	def arrancar(self):

		self.enmarcha = True 

	def acelerar(self):

		self.acelera = True

	def decelerar(self):

		self.decelera = True

	def estado(self):

		print("La marca del vehículo es", self.marca,
			"\nEl modelo del vehículo es", self.modelo,
			"\nEl vehículo se encuentra enmarcha:", self.enmarcha,
			"\nEl vehículo se encuentra acelerando:", self.acelera,
			"\nEl vehículo se encuentra decelerando:", self.decelera)



V1 = FactoryV("Mazda", "MX5")
V2 = FactoryV("Seat", "Leon")
V3 = FactoryV("Renault", "Megane")

VList = [V1, V2, V3]

# Exportar los objetos creados. 
FactoryExport = open("FactoryV", "wb")

pickle.dump(VList, FactoryExport)


FactoryExport.close()

del(FactoryExport)

# Importar los objetos creados. 

FactoryImport = open("FactoryV", "rb")

VImportList = pickle.load(FactoryImport)

FactoryImport.close()

# print(VImportList) <- Esto te imprime el nombre codificado del objeto. 

for i in VImportList:

	i.estado() # Si se importara en otro archivo .py sería necesario copiar y pegar la clase FactoryV para que reconociera el método estado(). 
