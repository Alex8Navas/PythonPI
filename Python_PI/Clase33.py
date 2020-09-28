# Clase 33. Curso Píldoras Informáticas.

# Control de Flujo. Métodos de Cadenas.


# upper(): todo a mayúsculas. 
# lower(): todo a minúsculas. 
# capitalize(): Primera letra a mayúscula. 
# count(): conteo de x.
# find(): índice de un carácter o grupo de caracteres.
# idigit(): pregunta si es dígito. 
# isalnum(): pregunta si es carácter alfanumérico. 
# isalpha(): pregunta si es carácter alfabético. 
# split(): separa usando espacios. 
# strip(): se carga los espacios sobrantes de inicio y final. 
# replace(): cambiar caracteres. 
# rfind(): es como find, pero comienza por el final de la cadena (reverse). 


# Recomendación: http://pyspanishdoc.sourceforge.net/


Nombre = input("Introduce tu nombre de usuario: ")

print("Su nombre es", Nombre)

print("Su nombre es", Nombre.upper())

print("Su nombre es", Nombre.lower())

print("Su nombre es", Nombre.capitalize())

Edad = input("Introduce tu edad: ")

print("¿Has introducido un número?", Edad.isdigit())

while Edad.isdigit() == False:
	
	print("Introduce un número, pillín...")

	Edad = input("Introduce tu edad: ")

if (int(Edad) < 18):

	print("No pasarás.")

else:

	print("Puede pasar, caballero.")

