# Clase 20. Curso Píldoras Informáticas.

# Control de Flujo. Generadores 2.

# Instrucción yield from: simplifica el código para bucles anidados. 

# El asterisco es un número indeterminado de elementos dados en forma de tupla. 
def Cities(*ciudades):
	for i in ciudades:
		yield i 

Ciudades = Cities("Madrid", "Barcelona", "Sevilla", "León")

print(next(Ciudades))
print(next(Ciudades))

# Acceder a los subelementos o letras. 


def Cities2(*ciudades):
	for i in ciudades:
		for j in i:
			yield j 

Ciudades2 = Cities2("Madrid", "Barcelona", "Sevilla", "León")

print(next(Ciudades2))
print(next(Ciudades2))
print(next(Ciudades2))
print(next(Ciudades2))
print(next(Ciudades2))
print(next(Ciudades2))

print("\nCon Yield From")
# Con yield from. 

def Cities2(*ciudades):
	for i in ciudades:
		yield from i

Ciudades2 = Cities2("Madrid", "Barcelona", "Sevilla", "León")

print(next(Ciudades2))
print(next(Ciudades2))
print(next(Ciudades2))
print(next(Ciudades2))
print(next(Ciudades2))
print(next(Ciudades2))

