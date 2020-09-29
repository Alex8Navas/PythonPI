# Clase 78. Curso Píldoras Informáticas.

# Control de Flujo. Fin del Curso. 

# Creación de Ejecutables. 

# Primero en la consola se hace: pip install pyinstaller

# Tras la instalación vas al directorio dond está el archivo .py
# que quieres transformar en un ejecutable. 
# Una vez en el directorio haces en consola:
# pyinstaller nombredelarchivo.py.

# Una vez hecho esto se crean muchos archivos. Interesa la carpeta dist, 
# en la cual se encuentra el archivo .exe. 

# Se hace: pyinstaller --windowed CalculadoraClase50.py
# Para que el exe no abra la consola de python al ejecutarse. 

# Se hace: pyinstaller --windowed -onefile CalculadoraClase50.py
# Para que sólo se cree el ejecutable y no todas las carpetas
# Esto sirve para que usuarios con otro sistema operativo o incluso
# sin Python puedan ejecutar el programa que se ha creado. 

# Para añadir un icono: pyinstaller --windowed --onefile --icon=./goblin.ico CalculadoraClase50.py