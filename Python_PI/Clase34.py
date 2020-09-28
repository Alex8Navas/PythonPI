# Clase 34. Curso Píldoras Informáticas.

# Control de Flujo. Módulos.

# Un módulo es un archivo .py o .pyc (python compilado), o un archivo escrito en C
# para CPython, que posee su propio espacio de nombres y que puede contener variables, funciones,
# clases e incluso otros módulos. 

# Sirven para organizar y reciclar código (modularización y reutilización). 

from Modules import MatFun

print("----La Calculadora----")

MatFun.sumar(9,9)

MatFun.restar(9,7)

from Modules import MatFun as MF

MF.sumar(9,9)

MF.restar(9,7)

# También se puede importar una función de un módulo. 
from Modules.MatFun import sumar # Solo importa la suma.

sumar(2,3)

from Modules.MatFun import * # Importa todas las funciones. Consume más. 

restar(2,3)


# Importar clases. 
from Modules.FactoryV import *

print("----La Fábrica----")

CarOne = FactoryV("Mazda", "Mx5")

CarOne.estado()


