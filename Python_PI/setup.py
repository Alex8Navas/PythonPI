# Archivo imprescindible para la configuración de un paquete distribuible en Python.
# Se va a aplicar a la función de potencia y redondeo del archivo .py del subpaquete PotSubKal. 
from setuptools import setup 


setup(

	name = "NurekPR",
	version = "1.0",
	description = "Paquete con las funciones de redondeo y de potencia.",
	author = "Nurek",
	author_email = "alex8srvc@gmail.com",
	url = "",
	packages = ["KalPak", "KalPak.PotSubPak"]
	
	)

