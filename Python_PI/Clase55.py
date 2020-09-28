# Clase 55. Curso Píldoras Informáticas.

# Control de Flujo. Bases de Datos 1. 


# SQLite: 
# - Es un sistema e gestión de bases de datos relacional. 
# - Se encuentra escrito en C. Es de código abierto. 
# - Forma parte integral del sistema (es lo que lo diferencia).
# - Se guarda como un único fichero en host (ocupa poco espacio en memoria y es eficiente y rápido). 

# Desventajas de SQLite:
# - No admite cláusulas anidadas tipo where.
# - No existen usuarios (no puede haber acceso simultáneo de usuarios)
# - Falta de clave foránea cuando se crea en la consola. 


# Pasos para la conexión
# 1. Abrir la conexión.
# 2. Crear un puntero: objeto que permite tanto ejecutar queries como manejar los resultados de las queries realizadas. 
# 3. Ejecutar una query o consulta SQL.
# 4. Manejar los resultados de la consulta (insertar, leer, actualizar, borrar (por sus iniciales en inglés, CRUD))
# 5. Cerrar el puntero.
# 6. Cerrar la conexión. 

import sqlite3

# ----- Establecimiento de la Conexión ------

# Si se hace una llamada a una base de datos que no existe, ésta se crea con la llamada. 
# Se crea sí una base de datos vacía. 
conexx = sqlite3.connect("BBDD/La Base de los Goblins")


# ----- Creación del Puntero o Cursor -----

# Se crea el puntero o cursor.
cursor = conexx.cursor()

# ------ Consultas ----------

# Creación de la tabla: CREATE TABLE "nombre de la tabla" (variables con su tipo)
# cursor.execute("CREATE TABLE Goblins (Nombre VARCHAR(30), Color VARCHAR(15), Edad INTEGER)")
# Se invalida la línea anterior porque la tabla ya existe al ejecutar el script la primera vez. 


cursor.execute("INSERT INTO Goblins VALUES ('Haydeck', 'White', 12)")
# Confirmar el cambio en la tabla:
conexx.commit()

conexx.close()