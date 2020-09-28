# Clase 58. Curso Píldoras Informáticas.

# Control de Flujo. Bases de Datos 4. 

import sqlite3

conexion = sqlite3.connect("BBDD/Fallen in Battle")

puntero = conexion.cursor()

# UNIQUE: instrucción para que no se puedan repetir valores en un campo. 

conexion.execute("""

CREATE TABLE FallenUnique (

IDGoblin INTEGER PRIMARY KEY AUTOINCREMENT,
Name VARCHAR(20) UNIQUE,
Kills INTEGER,
State VARCHAR(10))
	
	""")


goblinsNew = [

("Dorler", 7, "Dead"),
("Urik", 22, "Dead"),
("Naska", 56, "Alive"),
("Werony", 23, "Dead"),
("Creisial", 9, "Dead")

]

puntero.executemany("INSERT INTO FallenUnique VALUES (NULL,?,?,?)", goblinsNew)

conexion.commit()

conexion.close()
