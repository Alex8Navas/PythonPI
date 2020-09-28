# Clase 71. Curso Píldoras Informáticas.

# Control de Flujo. Expresiones Regulares 3. 

# La búsqueda por rangos. 

import re

listNames = ["Rexar Herz", "Maximiliam Stark", "Markus Vestegard", "Niklas Müller", "Niklas Stark", "Karen Krisñark"]

# Búsqueda de nombres que contengan letras comprendidas entre la o y la t. 
print("----- Nombres que contienen letras comprendidas entre la O y la T -----")
for name in listNames:

	if re.findall("[o-t]", name):

		print(name)
print("----- Nombres que comienzan con letras comprendidas entre la O y la T -----")
for name in listNames:

	if re.findall("^[O-T]", name): # Acento circunflejo (^): cabe recordar que Python es case sensitive. 

		print(name)

print("----- Nombres que terminan por letras comprendidas entre la O y la T -----")
for name in listNames:

	if re.findall("[o-t]$", name):  

		print(name)

# Los rangos son útiles cuando se trabaja con códigos (ciudades de procedencia del producto):

listCode = ["MAD1", "SEV::1", "BCN1", "MAD2", "SEV::2", "BCN2", "MAD3", "SEV-3", "BCN3", "MAD4", "SEV-4", "BCN4",
 "MADA", "SEV.A", "BCNA",  "MADB", "SEV.B", "BCNB",  "MADC", "SEV.C", "BCNC"]

print("----- Madrid rango de cero a tres -----")
for code in listCode:

	if re.findall("MAD[0-3]", code):

		print(code)

# Un acento circunflejo delante del rango sirve para la negación de los valores del rango: 
print("----- Madrid rango fuera de cero a tres -----")
for code in listCode:

	if re.findall("MAD[^0-3]", code):

		print(code)


print("----- Madrid rango de cero a tres y de A a B -----")
for code in listCode:

	if re.findall("MAD[0-3A-B]", code):

		print(code)


print("----- Sevilla rango con guión o con punto -----")
for code in listCode:

	if re.findall("SEV[-.]", code):

		print(code)
