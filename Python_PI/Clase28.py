# Clase 28. Curso Píldoras Informáticas.

# Control de Flujo. POO5.

# La Encapsulación de Métodos. 

print("----Segunda Remodelación de la Nueva Factoría de Coches----")
class NewFactory():

	def __init__(self): # Constructor. 
		# Propiedades. Encapsulación. 
		self.__LargoChasis = 300
		self.__AnchoChasis = 100
		self.__Ruedas = 4 
		self.__EnCircula = False # Solo accesible a través del método Arranca. 
 
	def Arranca(self, arrancad):

		self.__EnCircula = arrancad
		
		if self.__EnCircula:

			Chequeo = self.__Chequeo_Interno(int(input("Gasolina del coche (Litros): ")),
			 input("Estado del Aceite (Ok): "),
			 input("Estado de las puertas (Cerradas): ")) 

		if self.__EnCircula == True and Chequeo == True:
		
			return "El coche se encuentra en circulación."

		elif self.__EnCircula == True and Chequeo == False:

			return "Existe un problema detectado en el chequeo interno."
		
		else:
		
			return "El coche se halla en punto muerto." 
	
	def Propiedades(self):

		print("El coche tiene", self.__Ruedas, "ruedas.")

		print("Presenta un ancho de", self.__AnchoChasis, "y un largo de chasis de", self.__LargoChasis, ".")
	
	# Encapsulación de métodos.Sólo se puede acceder al método desde la clase
	# Esto sirve para que solamente funcione de forma interna. 
	def __Chequeo_Interno(self, gasolina, aceite, puertas):
		
		print("Chequeo de parámetros antes de arrancar.")
		
		self.gasolina = gasolina
		self.aceite = aceite
		self.puertas = puertas

		if self.gasolina >= 40 and self.aceite == "Ok" and self.puertas == "Cerradas":

			return True

		else:

			return False


print("----Coche Remodelado Uno----")
NewCar = NewFactory()
print(NewCar.Arranca(True))
NewCar.Propiedades()

print("----Coche Remodelado Dos----")
NewCar2 = NewFactory()
NewCar2.__Ruedas = 3 # Ya no hay cambios al haber encapsulación. 
print(NewCar2.Arranca(True))
NewCar2.Propiedades()

