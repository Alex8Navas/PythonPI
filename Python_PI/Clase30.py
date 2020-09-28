# Clase 30. Curso Píldoras Informáticas.

# Control de Flujo. POO7.


print("----	Creación de la Factoría de Vehículos----")
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


class VElekt():

	def __init__(self):

		self.autonomous = 100

	def cargaEnergy(self):

		self.carga = True 


# Herencia Múltiple. 
class BiciElekt(FactoryV, VElekt): # Se hereda el constructor de la primera superclase especificada. 
# En este caso se hace con FactoryV para indicar marca y modelo y usar su constructor. 
	pass




print("--Motocicleta Uno--")

MotoUno = Moto("Honda", "CBR")

MotoUno.caballitoF()

MotoUno.estado()

print("--Motocicleta Dos--")

MotoDos = Moto("Yamaha", "CBR")

MotoDos.estado()



print("--Furgón Uno--")

FurgoUno = Furgo("Reanult", "Kangoo")

FurgoUno.arrancar()

FurgoUno.acelerar()

FurgoUno.estado()

print(FurgoUno.capacidadCarga(450))

print("--Furgón Dos--")

FurgoUno = Furgo("Chevrolet", "Kangoo")

FurgoUno.arrancar()

FurgoUno.decelerar()

FurgoUno.estado()

print(FurgoUno.capacidadCarga(800))



print("--Bici Eléctrica Uno--")

BiciElektUno = BiciElekt("Orbea", "HC130")

BiciElektUno.estado()

