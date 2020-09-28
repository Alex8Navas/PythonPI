# Clase 69. Curso Píldoras Informáticas.

# Control de Flujo. Expresiones Regulares 1. 

# - Regex: son secuencias de caracteres que configuran patrones de búsqueda. 
# - Sirven para la manipulación y procesamiento de textos. 
# Ejemplos: - Buscar un formato determinado de texto (gmail). 
#			- Buscar la presencia o ausencia de una cadena de caracteres dentro de un texto. 
#			- Contar el número de coincidencia dentro de un texto. 

import re

string = "El ocaso de los goblins deviene inexorable, pero los goblins resurgirán de entre sus cenizas."


# search: sirve para la búsqueda de patrones: devuelve un objeto de tipo SRE_Match.
print(re.search("ocaso", string))
print(re.search("Ocaso", string)) # Devuelve None al no encontrar el texto. 

patrone = "ocaso"

if re.search(patrone, string) is not None:

	print("Se ha detectado la amenaza")

else:

	print("No se ha detectado ninguna amenaza")



patroneFound = re.search(patrone, string)

# Método Start: Da la posición del inicio del patrón encontrado en el texto (primera posición es cero).
print(patroneFound.start())

# Método End: Da la posición de finalización del patrón encontrado en el texto (primera posición es cero).
print(patroneFound.end())

# Método Span: Da el intervalo de posiciones del patrón encontrado en el texto (primera posición es cero).
print(patroneFound.span())

# Find all: Encontrar todos los matches que se corresponden con el patrón devolviendo una lista con éstos.
patrone = "goblins"
print(re.findall(patrone, string))
print(len(re.findall(patrone, string))) # Veces que se ha encontrado la coincidencia. 
