# Clase 74. Curso Píldoras Informáticas.

# Control de Flujo. Decoradores 2. 

# Recepción de parámetros al decorador: 
def decorador(funcionB):

	def funcInterna(*k):
		# Acciones decoradoras: 
		print("Se ejecutará el siguiente cálculo:")

		funcionB(*k) # Lo que devuelva la función a decorar.

		print("Cálculo finalizado.\n")

	return funcInterna

# Que llame a pares clave, valor se hace con dos asteriscos. 
def decorador2(funcionB):

	def funcInterna(*k, **kw):
		# Acciones decoradoras: 
		print("Se ejecutará el siguiente cálculo:")

		funcionB(*k, **kw) # Lo que devuelva la función a decorar.

		print("Cálculo finalizado.\n")

	return funcInterna

@decorador # Así se especifica la llamada al decorador. 
def suma(number1, number2):

	print("{} + {}  =".format(number1, number2), number1 + number2)

@decorador
def resta(number1, number2):

	print("{} - {} =".format(number1, number2), number1 - number2)

@decorador2
def potencia(base, exponente):

	print(pow(base, exponente))

suma(5,5)

resta(6,7)

suma(8,13)

resta(76,43)

potencia (5, 3)

potencia(base = 5, exponente = 3) # Por esto importa poner **, puesto que se especifica clave:valor. 
