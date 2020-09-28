# Clase 38. Curso Píldoras Informáticas.

# Control de Flujo. Archivos Externos 2.

from io import open

AText = open("AText.txt", "r")

print(AText.read())

# A la segunda llamada no queda nada por leer.
print(AText.read())

# Método seek para moverse por la lectura.
# Al poner cero regresa al comienzo y se vuelve a leer el texto. 

AText.seek(0)

print(AText.read())

# A la posición 76 del texto.
AText.seek(76)

print(AText.read())

# En la mitad del texto.
AText.seek(len(AText.read())/2)

print(AText.read())

# Al final de la primera línea. 
AText.seek(len(AText.readline()))

print(AText.read())

AText.close()

# Para la lectura y escritura se abre con r+. 

AText = open("AText.txt", "r+")

# AText.write("Leyendas de la Tierra Media\n")

Lista = AText.readlines()

Lista.append("\nLeyendas de la Tierra Media\n")

# Si se quisiera sustituir algún elemento:
# Lista[1] = "\nLeyendas de la Tierra Media\n"

print(Lista)

AText.seek(0)

# Sustituir con el texto que se ha guardado en Lista. 
AText.writelines(Lista)

AText.close()

