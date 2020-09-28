# Clase 35. Curso Píldoras Informáticas.

# Control de Flujo. Paquetes.

# Paquete: Directorios donde se almacenan módulos relacionados entre sí. 
# Esto sirve para organizar y reutilizar los módulos.
# Crear un paquete es tan sencillo como crear una carpeta en cuyo interior
# se halle un archivo denominado __init__.py

from KalPak.KalGeneric import divis
from KalPak.KalGeneric import potencia


divis(8, 10)

potencia(8,3)


from KalPak.KalGeneric import *

sumar(2,4)

from KalPak.KalSubPak.BasicsKal import *

producto2(8,9)

from KalPak.PotSubPak.PotKal import *

potencia2(2, 5)

