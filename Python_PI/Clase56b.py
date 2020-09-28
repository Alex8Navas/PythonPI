# Clase 56b. Curso Píldoras Informáticas.

# Control de Flujo. Bases de Datos 2. 

# Leer tabla de registros. 

import sqlite3

conexionst = sqlite3.connect("BBDD/La Base de los Goblins")

puntero = conexionst.cursor()

puntero.execute("SELECT * FROM Goblins") # Seleccionar todos los registros. 

listGoblins = puntero.fetchall() # Coger todos los regitros.

print("Mi lista de Goblins:\n",listGoblins)
print("Lectura con un bucle:")
for i in listGoblins:

	print("Ha nacido un nuevo goblin en la aldea")
	print("Nombre del Goblin: ", i[0], "\n",
	"Raza del Goblin: ", i[1], "\n", 
	"Edad del Goblin: ", i[2], sep = "")

conexionst.close()