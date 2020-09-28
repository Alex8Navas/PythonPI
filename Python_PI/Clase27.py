# Clase 27. Curso Píldoras Informáticas.

# Control de Flujo. POO4.

class Coche():

	# Propiedades
	LargoChasis = 300
	AnchoChasis = 100
	Ruedas = 4
	EnCircula = False

	# Comportamientos
	def Arranca(self):

		self.EnCircula = True
	
	def Estado(self):
		
		if self.EnCircula == True:
		
			return "El coche se encuentra en circulación."
		
		else:
		
			return "El coche se halla en punto muerto." 

CocheUno = Coche()

print("El largo del chasis del coche es:", CocheUno.LargoChasis)
print("El coche tiene", CocheUno.Ruedas, "ruedas")

# Cambiar el estado del objeto. Llamar a un método. 
print(CocheUno.Estado())

CocheUno.Arranca()

print(CocheUno.Estado())

print("----Creación del Segundo Coche----")

CocheDos = Coche()
print("El largo del chasis del coche dos es:", CocheDos.LargoChasis)
print("El coche dos tiene", CocheDos.Ruedas, "ruedas")
print(CocheDos.Estado())


print("----Nueva Factoría de Coches----")
class NewFactory():

	# Propiedades
	LargoChasis = 300
	AnchoChasis = 100
	Ruedas = 4
	EnCircula = False

	# Comportamientos: Reducir los dos comportamientos a uno. 
	def Arranca(self, arrancad):

		self.EnCircula = arrancad
		
		if self.EnCircula == True:
		
			return "El coche se encuentra en circulación."
		
		else:
		
			return "El coche se halla en punto muerto." 
	
	def Propiedades(self):

		print("El coche tiene", self.Ruedas, "ruedas.")

		print("Presenta un ancho de", self.AnchoChasis, "y un largo de chasis de", self.LargoChasis, ".")

print("----Coche Nuevo Uno----")
NewCar = NewFactory()
print(NewCar.Arranca(True))
NewCar.Propiedades()

print("----Coche Nuevo Dos----")
NewCar2 = NewFactory()
print(NewCar2.Arranca(False))
NewCar2.Propiedades()

# Es habitual que las características comunes de los objetos
# pertenezcan a un estado inicial. Para ello se emplea un método especial
# denominado constructor. 

print("----Remodelación de la Nueva Factoría de Coches----")
class NewFactory():

	def __init__(self): # Constructor. 
		# Propiedades
		self.LargoChasis = 300
		self.AnchoChasis = 100
		self.Ruedas = 4
		self.EnCircula = False

	# Comportamientos: Reducir los dos comportamientos a uno. 
	def Arranca(self, arrancad):

		self.EnCircula = arrancad
		
		if self.EnCircula == True:
		
			return "El coche se encuentra en circulación."
		
		else:
		
			return "El coche se halla en punto muerto." 
	
	def Propiedades(self):

		print("El coche tiene", self.Ruedas, "ruedas.")

		print("Presenta un ancho de", self.AnchoChasis, "y un largo de chasis de", self.LargoChasis, ".")

print("----Coche Remodelado Uno----")
NewCar = NewFactory()
print(NewCar.Arranca(True))
NewCar.Propiedades()

print("----Coche Remodelado Dos----")
NewCar2 = NewFactory()
NewCar2.Ruedas = 3 # Se cambia el valor de una de las propiedades. 
print(NewCar2.Arranca(False))
NewCar2.Propiedades()

# Para evitar cambios extraños de una calse como poner tres ruedas a un coche se recurre
# a la encapsulación, que hace inaccesible aquello que se encapsula. 

print("----Remodelación de la Nueva Factoría de Coches----")
class NewFactory():

	def __init__(self): # Constructor. 
		# Propiedades. Encapsulación. 
		self.__LargoChasis = 300
		self.__AnchoChasis = 100
		self.__Ruedas = 4 
		self.__EnCircula = False # Solo accesible a través del método Arranca. 

	# Comportamientos: Reducir los dos comportamientos a uno. 
	def Arranca(self, arrancad):

		self.__EnCircula = arrancad
		
		if self.__EnCircula == True:
		
			return "El coche se encuentra en circulación."
		
		else:
		
			return "El coche se halla en punto muerto." 
	
	def Propiedades(self):

		print("El coche tiene", self.__Ruedas, "ruedas.")

		print("Presenta un ancho de", self.__AnchoChasis, "y un largo de chasis de", self.__LargoChasis, ".")

print("----Coche Remodelado Uno----")
NewCar = NewFactory()
print(NewCar.Arranca(True))
NewCar.Propiedades()

print("----Coche Remodelado Dos----")
NewCar2 = NewFactory()
NewCar2.__Ruedas = 3 # Ya no hay cambios al haber encapsulación. 
print(NewCar2.Arranca(False))
NewCar2.Propiedades()
