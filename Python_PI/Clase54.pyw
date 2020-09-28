# Clase 54. Curso Píldoras Informáticas.

# Control de Flujo. Interfaces Gráficas 13.

# Abrir archivos desde ventanas.
# Se requiere de llamar a la librería filedialog. 

from tkinter import *
from tkinter import filedialog

# ----- Declaración y configuración de la raíz -----

root = Tk()

root.title("La Prueba de Moria")

root.iconbitmap("GOT.ico")

root.config(bg = "#373737", relief = "groove", bd = 35, cursor = "Trek",
	width = 500, height = 300)

root.resizable(True, True)


# ----- Declaración de la función de apertura de ficheros -----

def openFile():

	fichero = filedialog.askopenfilename(title = "Habla, amigo, y entra", initialdir = "C:", 
		filetypes = (("Ficheros de Excel", "*.xlsx"), ("Ficheros de texto", "*.txt"), ("Toda Extensión", "*.*"))) 
	# Con filetypes se filtra nombre de archivos y la extensión. Lo del nombre es un indicador en el directorio, puedes poner lo que quieras. Lo importante es la extensión. 
	print(fichero) # Muestra la ruta del archivo. 

# ---- Botón para la apertura de fichero ----

Button(root, text = "Abrid las puertas", command = openFile).pack()

root.mainloop()