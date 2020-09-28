# Clase 26. Curso Píldoras Informáticas.

# Control de Flujo. POO3.

class Coche():

	# Propiedades
	LargoChasis = 300
	AnchoChasis = 100
	Ruedas = 4
	EnCircula = False

	# Comportamientos
	def Arranca(self): # Método: Función especial de la clase. Por eso el self (el objeto de la clase). 
		
		self.EnCircula = True
	
	def Estado(self):
		
		if self.EnCircula == True:
		
			return "El coche se encuentra en circulación."
		
		else:
		
			return "El coche se halla en punto muerto."

# El self es como el this de Java y C++. 

CocheUno = Coche() # Crear un objeto se denomina instanciar o ejemplarizar. 

print("El largo del chasis del coche es:", CocheUno.LargoChasis)
print("El coche tiene", CocheUno.Ruedas, "ruedas")

# Cambiar el estado del objeto. Llamar a un método. 
print(CocheUno.Estado())

CocheUno.Arranca()

print(CocheUno.Estado())

