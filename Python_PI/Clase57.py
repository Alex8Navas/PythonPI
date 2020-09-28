# Clase 57. Curso Píldoras Informáticas.

# Control de Flujo. Bases de Datos 3. 

# Creación de Tablas Clave-Valor.

import sqlite3

conexion = sqlite3.connect("BBDD/Fallen in Battle")

puntero = conexion.cursor()

conexion.execute("""

CREATE TABLE Fallen (
IDGoblin VARCHAR(7) PRIMARY KEY, 
Name VARCHAR(20),
Kills INTEGER,
State VARCHAR(10))

	""")
# PRIMARY KEY: es el campo clave. No se puede repetir, son únicos. Si se introduce un valor repetido da la clave dará error. 

goblinslist = [

("K34", "Horian", 4, "Dead"),
("K92", "Kroaz", 14, "Alive"),
("K75", "Lerk", 2, "Alive"),
("K28", "Irisk", 9, "Alive"),
("K42", "Péristan", 0, "Dead")

]

puntero.executemany("INSERT INTO Fallen VALUES (?,?,?,?)", goblinslist)

conexion.commit()

conexion.close()
