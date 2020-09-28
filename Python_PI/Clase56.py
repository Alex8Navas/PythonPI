# Clase 56. Curso Píldoras Informáticas.

# Control de Flujo. Bases de Datos 2. 

# Insertar lote de registros. 

import sqlite3

conexionst = sqlite3.connect("BBDD/La Base de los Goblins")

puntero = conexionst.cursor()

GoblinsList = [

("Gern", "Black", 15),
("Jussk", "White", 11),
("Drott", "Green", 19),
("Piriane", "Dark Green", 17),

]

# Se ponen en values tanto interrogantes como campos o columnas tenga la lista. 
puntero.executemany("INSERT INTO Goblins VALUES (?,?,?)", GoblinsList)
conexionst.commit()

conexionst.close()
