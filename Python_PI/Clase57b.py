# Clase 57b. Curso Píldoras Informáticas.

# Control de Flujo. Bases de Datos 3. 

# Creación de Tablas Clave-Valor.

import sqlite3

conexion = sqlite3.connect("BBDD/Fallen in Battle")

puntero = conexion.cursor()

# La clave primaria se puede poner con un entero automático autoincrementable. 

conexion.execute("""

CREATE TABLE FallenAutoID (
IDGoblin INTEGER PRIMARY KEY AUTOINCREMENT, 
Name VARCHAR(20),
Kills INTEGER,
State VARCHAR(10))

	""")


goblinslist = [

("Horian", 4, "Dead"),
("Kroaz", 14, "Alive"),
("Lerk", 2, "Alive"),
("Irisk", 9, "Alive"),
("Péristan", 0, "Dead")

]

# Al ser el ID automático se ha de poner NULL. 
puntero.executemany("INSERT INTO FallenAutoID VALUES (NULL,?,?,?)", goblinslist)

conexion.commit()

conexion.close()
