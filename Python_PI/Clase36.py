# Clase 36. Curso Píldoras Informáticas.

# Control de Flujo. Paquetes Distribuibles.

# Estos paquetes se pueden enviar y utilizar con independencia de la raíz.

# Se crea el archivo setup.

# Se va a la consola y desde el directorio del archivo se hace:
# python setup.py sdist

# Esto crea un carpeta llamada dist con un archivo .tar.gz
# Se tiene otra carpeta con el nombre especificado en el setup.py con info del paquete. 


# Para instalar el paquete creado (no tiene mucho sentido, es para instalar en general),
# vas con cd a la carpeta dist y haces:
# pip3 install (nombre del archivo .tar.gz)
# Nota: si pones la primera letra del paquete y le das al tabulador se completa el nombre automáticamente. 

# Ahora se puede usar el subpaquete potencia desde donde se quiera. Forma parte del SO. 

from KalPak.PotSubPak.PotKal import *

potencia2(8,9)


# Para desinstalar simplemente se va, desde donde se desee (no importa el directorio de la consola)
# y se hace: pip3 uninstall (nombre del paquete).
