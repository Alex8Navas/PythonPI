# Factoría de Vehículos
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


class Moto(FactoryV):

	caballito = "Ninguna."
	
	def caballitoF(self):

		self.caballito = "Esta moto tiene la capacidad de hacer el caballito."

	def estado(self):

		print("La marca de la moto es", self.marca,
			"\nEl modelo de la moto es", self.modelo,
			"\nLa moto se encuentra enmarcha:", self.enmarcha,
			"\nLa moto se encuentra acelerando:", self.acelera,
			"\nLa moto se encuentra decelerando:", self.decelera,
			"\nHabilidad Especial:", self.caballito)



class Furgo(FactoryV):

	def capacidadCarga(self, carga):

		self.capacidad = int(carga)

		if self.capacidad > 500:

			return "El furgón se encuentra cargado."

		else:

			return "Todavía se pueden cargar más bienes."


class VElekt(FactoryV):

	def __init__(self, marca, modelo):

		super().__init__(marca, modelo)
		self.autonomous = 100

	def cargaEnergy(self):

		self.carga = True 


# Herencia Múltiple. 
class BiciElekt(VElekt):  
	pass


