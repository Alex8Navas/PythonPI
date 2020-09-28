# Clase 29. Curso Píldoras Informáticas.

# Control de Flujo. POO6.

# La Herencia. 

# Clase Padre: La primera clase de la que heredan el resto. 
# Superclase: Toda clase que da hernecia a otra.
# Subclase: Toda clase que recibe hernecia de otra. 
# Una clase puede ser superclase y subclase al mismo tiempo. 


# Objetivo: Reciclaje de código.


print("----	Creación de la Factoría de Vehículos----")
class FactoryV():

	def __init__(self, marca, modelo):

		self.marca = marca
		self. modelo = modelo
		self.enmarcha = False
		self.acelera = False
		self.decelera = False

	def arranca(self):

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
	pass

MotoUno = Moto("Honda", "CBR")

MotoUno.estado()

