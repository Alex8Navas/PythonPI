# Clase 53. Curso Píldoras Informáticas.

# Control de Flujo. Interfaces Gráficas 12.

# Ventanas emergentes. 

from tkinter import *
# Para crear ventanas emergentes hay que importar obligatoriamente la siguiente librería:
from tkinter import messagebox 

# ----- Declaración y configuración de la raíz -----
root = Tk()

root.title("La Prueba de Moria")

root.iconbitmap("GOT.ico")

root.config(bg = "#373737", relief = "groove", bd = 35, cursor = "Trek",
	width = 500, height = 300)

root.resizable(True, True)


# ----- Función para Ventanas Emergenetes -----

def aditionale():
	
	messagebox.showinfo("La Ventana de Moria", "No puedes pasar")

# Se puede cambiar el sonido y apariencia de la ventana emergente. 
def avisoLicencia():
	
	messagebox.showwarning("La Licencia de Moria", "Dominada por los Goblins") # Cambia el emoji de info por uno de adevertencia o peligro. 

def escape():

	valor = messagebox.askquestion("Salida de Moria", "¿Desea usted, noble goblin, salir de Moria?") # Saldrá un interrogante. 
	# valor = messagebox.askokcancel("Salida de Moria", "¿Cómo desea usted, noble goblin, salir de Moria?") # Para cambiar por Ok o Cancel
	if valor == "yes": # Si se hace con askokcancel se ha de poner True o False, no "yes" o "no". 
		root.destroy() # Salir de la ventana. 

# Por si se bloquea el documento y no deja salir. 
def cierreSeguro():

	valor = messagebox.askretrycancel("Salida de Moria", "La salida de Moria no es posible. Las puertas están cerradas. No se puede salir") 

	if valor == False:

		root.destroy()



# ------ Definición del objeto menú -----

barraMenu = Menu(root)

root.config(menu = barraMenu)

# ----- Configuración de los elementos del menú -----

archivoMenu = Menu(barraMenu, tearoff = 0) # Declaración de un elemento del menú. 
# tearoff = 0 sirve para quitar la lágrima, una línea discontinua que sale en la parte superior de cada elemento del menú.
archivoEdit = Menu(barraMenu, tearoff = 0)
archivoTools = Menu(barraMenu, tearoff = 0)
archivoHelp = Menu(barraMenu, tearoff = 0)

# ------ Texto elementos del Menu ------

barraMenu.add_cascade(label = "Archivos", menu = archivoMenu)
barraMenu.add_cascade(label = "Edición", menu = archivoEdit)
barraMenu.add_cascade(label = "Herramientas", menu = archivoTools)
barraMenu.add_cascade(label = "Ayuda", menu = archivoHelp)

# ----- Subelementos del Menu ------

archivoMenu.add_command(label = "Nuevo")
archivoMenu.add_command(label = "Abrir")
archivoMenu.add_command(label = "Guardar")
archivoMenu.add_separator() # Barra de separación. 
archivoMenu.add_command(label = "Cerrar", command = cierreSeguro)
archivoMenu.add_command(label = "Salir", command = escape)


archivoEdit.add_command(label = "Copiar")
archivoEdit.add_command(label = "Cortar")
archivoEdit.add_command(label = "Pegar")


archivoHelp.add_command(label = "Licencia", command = avisoLicencia)
archivoHelp.add_command(label = "Acerca de", command = aditionale)

root.mainloop()
