# Clase 76. Curso Píldoras Informáticas.

# Control de Flujo. Documentación y Pruebas 1. 

# Módulo doctest: Sirve para hacer pruebas

import doctest

def areaTriang(base, altura):

	""" Calcula el área de un triángulo dados su base y su altura
dados como parámetros. Se ponen varias pruebas a continuación: 

>>> areaTriang(3,6)
'La altura del triángulo de base 3 y altura 6 es: 9.0'

>>> areaTriang(4,5)
'La altura del triángulo de base 4 y altura 5 es: 10.0'

>>> areaTriang(9,3)
'La altura del triángulo de base 9 y altura 3 es: 13.5'

	 """

	return "La altura del triángulo de base {} y altura {} es: ".format(base, altura) + str(base*altura/2)

# Otro ejemplo: 
def mailverif(mail):

	""" Verifica si una cadena contiene un @.
Es incorrecto si la @ está al final de la cadena o
si existe más de una @ en el string.

>>> mailverif("Alex@gmail.com")
True

>>> mailverif("Alex@gmail.@com")
False

>>> mailverif("Alexgmail.com")
False

>>> mailverif("Alexgmail.com@")
False

	 """
	arroba = mail.count("@")

	if arroba!=1 or mail.rfind("@") == (len(mail) -1):

		return False

	else:

		return True


doctest.testmod() # Evalúa si existen problemas en la función al hacer las pruebas escritas. 

