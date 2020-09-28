# Clase 58. Curso Píldoras Informáticas.

# Control de Flujo. Bases de Datos 4. 

import sqlite3

conexion = sqlite3.connect("BBDD/Fallen in Battle")

puntero = conexion.cursor()

# Operaciones CRUD: create, read, update, delete. 

# Operación de Lectura. 
puntero.execute("SELECT * FROM FallenUnique WHERE State = 'Dead'")

deadGoblins = puntero.fetchall()

print(deadGoblins)

# Operación de Actualización. 

puntero.execute("UPDATE FallenUnique SET Kills = 86 WHERE Name = 'Naska'")

# Operación Eliminar. 

puntero.execute("DELETE FROM FallenUnique WHERE Kills < 10")

conexion.commit()

conexion.close()
