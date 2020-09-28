# Clase 70. Curso Píldoras Informáticas.

# Control de Flujo. Expresiones Regulares 2.

# Metacaracteres o caracteres comodín

import re

# Las anclas:

listNames = ["Rexar Herz", "Maximiliam Stark", "Markus Vestegard", "Niklas Müller", "Niklas Stark", "Karen Krisñark"]

for name in listNames:

	if re.findall("^Niklas", name): # Acento circunflejo (^): sirve para encontrar coincidencias que comienzan por. 

		print(name)

for name in listNames:

	if re.findall("Stark$", name): # Dollar ($): sirve para encontrar coincidencias que terminen por. 

		print(name)


# Búsqueda de dominios (es un uso frecuente del símbolo dolar y del circunflejo) 
listDom = ["http://pildorasinformaticas.es",
			"ftp://pildorasinformaticas.es",
			"http://pildorasinformaticas.com",
			"ftp://pildorasinformaticas.com",
			"http://informaticaespañola.es"]

for dom in listDom:

	if re.findall("es$", dom): 

		print(dom)

for dom in listDom:

	if re.findall("^ftp", dom): 

		print(dom)

# Búsqueda de caracteres en algún lugar del texto: se hace con corchetes.
for name in listNames:

	if re.findall("[ñ]", name):

		print(name) 

# Para varias palabras con una parte en común (se recoge entre corchetes la variación en la posición):
listObjetos = ["Programa", "Programo", "Programación", "Ordenador"]

for word in listObjetos:

	if re.findall("Program[ao]", word):

		print(word)

# Esto es muy útil para búsquedas cuando quien suministra los datos comete faltas de ortografía.
# Por ejemplo, poner la vocal sin tilde y con tilde entre corchetes.  
