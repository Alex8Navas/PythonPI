# Clase 37. Curso Píldoras Informáticas.

# Control de Flujo. Archivos Externos 1.

# Trabajar con archivos externos tiene como objetivo la persistencia de datos. 
# Es decir, evitar que la información no se pierda tras la ejecución del programa. 

# Para esto se trabaja con el módulo io stream. 

from io import open 

# El archivo se puede abrir en modo lectura, escritura o append (para agregar info al archivo). 
# Si el archivo no existe, la función open lo crea. 
AText = open("AText.txt", "w")

Frase = """Han tomado el puente y la segunda sala. Hemos atrancado las puertas, pero no
podremos detenerlos por mucho tiempo. ¡El suelo tiembla!. Tambores… Tambores
en lo profundo. No podemos salir. Una sombra se mueve en la oscuridad.
No podemos salir. Ya vienen..."""

AText.write(Frase)

AText.close()


# Lectura del archivo. 
AText = open("AText.txt", "r")

Contenido = AText.read()

AText.close()

print(Contenido)


# Creando una lista con las líneas del .txt.
AText = open("AText.txt", "r")

Lista = AText.readlines()

AText.close()

print(Lista)

print(Lista[0])

print(Lista[1])

print(Lista[2])

print(Lista[3])


# Apppend
AText = open("AText.txt", "a")

AText.write("\n\nLibro de la Cámara de Mazarbul, Tumba de Balin, Minas de Moria.")

AText.close()

