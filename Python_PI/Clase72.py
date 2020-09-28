# Clase 72. Curso Píldoras Informáticas.

# Control de Flujo. Expresiones Regulares 4. 

# Funciones match y search. 

import re

name1 = "Rexar Herz"
name2 = "Maximiliam Stark"
name3 = "Markus Vestegaard"
name4 = "Niklas Stark"
name5 = "niklas Vestegaard"
name6 = "Nya Vistings"
name7 = "Sya Gardevoir"

# match: busca coincidencias al comienzo de un string. 
if re.match("Niklas", name1):

	print("Se ha encontrado al renegado.")

else:

	print("No se ha encontrado al renegado.")

if re.match("Niklas", name4):

	print("Se ha encontrado al renegado.")

else:

	print("No se ha encontrado al renegado.")


# Esta función tiene un tercer parámetro, el flag, que permite ignorar mayúsculas: 
if re.match("Niklas", name5):

	print("Se ha encontrado al renegado.")

else:

	print("No se ha encontrado al renegado.")

if re.match("Niklas", name5, re.IGNORECASE):

	print("Se ha encontrado al renegado.")

else:

	print("No se ha encontrado al renegado.")


# El punto se puede usar de comodín para sustituit cualquier letra: 
if re.match(".ya", name6):

	print("Se ha encontrado al renegado.")

else:

	print("No se ha encontrado al renegado.")

if re.match(".ya", name7):

	print("Se ha encontrado al renegado.")

else:

	print("No se ha encontrado al renegado.")


string1 = "Maximiliam Ferdinand"
string2 = "87634439274"
string3 = "K-63794927290"

# El carácter \d sirve para saber si la cadena empieza o no por un número (d es de digit):
if re.match("\d", string1):

	print("Se ha encontrado al renegado.")

else:

	print("No se ha encontrado al renegado.")

if re.match("\d", string2):

	print("Se ha encontrado al renegado.")

else:

	print("No se ha encontrado al renegado.")

if re.match("\d", string3):

	print("Se ha encontrado al renegado.")

else:

	print("No se ha encontrado al renegado.")

# Search: busca en cualquier punto de la cadena la existencia de coincidencias. También tiene flag. 

for surname in [name1, name2, name3, name4, name6, name7]:

	if re.search("Vestegaard", surname):

		print("Se ha encontrado a un miembro de la familia Vestegaard. Es {}.".format(surname))

	elif re.search("Stark", surname):

		print("Se ha encontrado a un miembro de la familia Stark. Es {}.".format(surname))


code1 = "79f5S95D22g071Vs5EWl"
code2 = "871f63e44s3ADH927Pk4"
code3 = "K63794927290YTR89832"

if re.search("71", code1):

	print("El código {} contiene el valor 71".format(code1))

else:

	print("El código {} no contiene el valor 71".format(code1))

if re.search("71", code2):

	print("El código {} contiene el valor 71".format(code2))

else:

	print("El código {} no contiene el valor 71".format(code2))

if re.search("71", code3):

	print("El código {} contiene el valor 71".format(code3))

else:

	print("El código {} no contiene el valor 71".format(code3))
