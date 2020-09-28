# Clase 77. Curso Píldoras Informáticas.

# Control de Flujo. Documentación y Pruebas 2. 

# Pruebas con expresiones anidadas. 

import math
import doctest 

# Para anidar en las pruebas se ponen los puntos suspensivos.
# Si se quiere incluir un error o excepción, como la raíz cuadrada de un número negativo,
# se añaden la primera y última filas del error y entre medias puntos suspensivos. 
def root(listNumbers):

	""" Esta función revcibe una lista de números como input 
	y devuelve una lista con la raíces cuadradas de dichos 
	valores suministrados.  

>>> lista = []
>>> for i in [4,9,16]:
...		lista.append(i)
>>> root(lista)
[2.0, 3.0, 4.0]


>>> lista = []
>>> for i in [4,-9,16]:
...		lista.append(i)
>>> root(lista)
Traceback (most recent call last):
...
ValueError: math domain error
	 """
	return [math.sqrt(n) for n in listNumbers]


doctest.testmod()
