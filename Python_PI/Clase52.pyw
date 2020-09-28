# Clase 52. Curso Píldoras Informáticas.

# Control de Flujo. Interfaces Gráficas 11.

# Construcción de Menús

from tkinter import *

root = Tk()

root.title("La Prueba de Moria")

root.iconbitmap("GOT.ico")

root.config(bg = "#373737", relief = "groove", bd = 35, cursor = "Trek")

root.resizable(True, True)

# ------ Definición del objeto menú -----

barraMenu = Menu(root)

root.config(menu = barraMenu)

# ----- Configuración de los elementos del menú -----

archivoMenu = Menu(barraMenu, tearoff = 0) # Declaración de un elemento del menú. 
# tearoff sirve para quitar la lágrima, una línea discontinua que sale en la parte superior de cada elemento del menú.
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
archivoMenu.add_command(label = "Cerrar")
archivoMenu.add_command(label = "Salir")


archivoEdit.add_command(label = "Copiar")
archivoEdit.add_command(label = "Cortar")
archivoEdit.add_command(label = "Pegar")


archivoHelp.add_command(label = "Licencia")
archivoHelp.add_command(label = "Acerca de")

# ------ Foto de Cabecera -----
foto = PhotoImage(file = "Images/Steampunk-Art.png")
Label(root, image = foto).pack()


FrameCheck = Frame(root)

FrameCheck.pack(fill = "both", expand = 1)

FrameCheck.config(bg = "#EEEEEE",  relief = "groove", bd = 25, cursor = "Trek")

root.mainloop()
