# Clase 75. Curso Píldoras Informáticas.

# Control de Flujo. Documentación. 

# Documentar: incluir comentarios en clases, métodos, módulos...
# Esto sirve para facilitar el trabajo en equipo. 


def areaCuadrado(lado):

	"""Esta función sirve para calcular el área de un cuadrado del lado especificado como parámetro."""

	return "El área del cuadrado de lado {} es: ".format(lado) + str(lado*lado)

def areaTriang(base, altura):

	"""Esta función sirve para calcular el área de un triángulo de la base y altura
especificados como parámetros."""
	
	return "El área del triángulo de base {} y altura {} es: ".format(base, altura) + str(base*altura/2)

print(areaCuadrado(9))

print(areaTriang(8,7))


# Si se quiere mostrar la información de los comentarios de la función:
print("\n----- Documentación con print & __doc__ -----\n")
print(areaCuadrado.__doc__)
print(areaTriang.__doc__)
# Otra opción:
print("\n----- Documentación con la función help -----\n")
help(areaCuadrado)
help(areaTriang)

class Operaciones:

	"""Esta clase sirve para definir funciones aritméticas."""

	def suma(number1, number2):

		""" Esta función sirve para sumar."""

		return number1 + number2

	def resta(number1, number2):

		""" ESta función sirve para restar."""

		return number1 - number2
help(Operaciones)
help(Operaciones.suma)

# También se pueden incluir comentarios en los módulos. 
from Modules import MatFun
help(MatFun)
