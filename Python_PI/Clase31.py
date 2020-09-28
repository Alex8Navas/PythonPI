# Clase 31. Curso Píldoras Informáticas.

# Control de Flujo. POO8.



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


class VElekt(FactoryV):

	def __init__(self, marca, modelo):

		super().__init__(marca, modelo)
		self.autonomous = 100

	def cargaEnergy(self):

		self.carga = True 


# Herencia Múltiple. 
class BiciElekt(VElekt):  
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

# Función super() para heredar Métodos. 

print("\n----Las Leyendas de la Noche----")
class Vampiro():

	def __init__(self, nombre, edad, residencia): 

		self.nombre = nombre
		self.edad = edad
		self.residencia = residencia

	def description(self):

		print("El nombre del vampiro es", self.nombre,
			"\nLa edad del vampiro es", self.edad,
			"\nEl vampiro habita la región de", self.residencia)

class ClaseVampiroDeseado(Vampiro):

	def __init__(self):

		super().__init__(input("Nombre del Vampiro: "),
			int(input("Edad del Vampiro: ")),
			input("Residencia del Vampiro: ")) 
		self.riqueza = int(input("Riqueza del Vampiro: "))
		self.poder= int(input("Poder del Vampiro: "))

	def description(self):

		super().description()

		print("La riqueza del Vampiro es", self.riqueza,
			"\nEl poder del vampiro es", self.poder)

class ClaseVampiroGeneric(Vampiro):

	def __init__(self, riqueza, poder, nombre_vampiro, edad_vampiro, residencia_vampiro):

		super().__init__(nombre_vampiro, edad_vampiro, residencia_vampiro) 
		self.riqueza = riqueza
		self.poder= poder

	def description(self):

		super().description()

		print("La riqueza del Vampiro es", self.riqueza,
			"\nEl poder del vampiro es", self.poder)


print("----El primer Ancestro de Kiev----")
VanHess = Vampiro("Van Hess", 583, "Kiev")

VanHess.description()

print("----El vampiro deseado----")
Wilhem = ClaseVampiroDeseado()

Wilhem.description()

print("----El señor de Minsk----")
Renaak = ClaseVampiroGeneric(876576, 999, "Renaak", 528, "Minsk")

Renaak.description()

# Principio de sustitución: Es siempre uno. Un objeto de la subclase es 
# siempre perteneciente a la superclase. 

print(isinstance(Renaak, ClaseVampiroGeneric))
print(isinstance(Renaak, Vampiro))
print(isinstance(Renaak, ClaseVampiroDeseado))
