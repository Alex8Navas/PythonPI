# Clase 61. Curso Píldoras Informáticas.

# Control de Flujo. Práctica Guiada 3. 

# Etiquetas y Segundo Frame para los botones inferiores. 

from tkinter import *
from tkinter import messagebox
import sqlite3

root = Tk()

root.title("La Guarida del Goblin")

root.iconbitmap("GOT.ico")

root.config(bg = "#373737",
 relief = "groove",
 bd = 12,
 cursor = "Trek")

root.resizable(True, True)

# ------------ Configuración del Menú ------------

barraMenu = Menu()

root.config(menu = barraMenu, width = 300, height = 200)

# Definir los elementos del menú: 
BDMenu = Menu(barraMenu, tearoff = 0)
DelMenu = Menu(barraMenu, tearoff = 0)
CRUDMenu = Menu(barraMenu, tearoff = 0)
HelpMenu = Menu(barraMenu, tearoff = 0)

# Definir etiquetas de cada subelemento del menú: 
BDMenu.add_command(label = "Establish Connection")
BDMenu.add_command(label = "Exit")

DelMenu.add_command(label = "Delete Fields")

CRUDMenu.add_command(label = "Create")
CRUDMenu.add_command(label = "Read")
CRUDMenu.add_command(label = "Update")
CRUDMenu.add_command(label = "Delete")

HelpMenu.add_command(label = "License")
HelpMenu.add_command(label = "About...")

# Agregar los subelementos a cada elemento del menú y poner las etiquetas a los elementos:
barraMenu.add_cascade(label = "Base", menu = BDMenu)
barraMenu.add_cascade(label = "Delete", menu = DelMenu)
barraMenu.add_cascade(label = "CRUD", menu = CRUDMenu)
barraMenu.add_cascade(label = "Help", menu = HelpMenu) 


# ------------ Definición del Marco  ------------

FrameBD = Frame(root)

FrameBD.config(bg = "#EEEEEE", relief = "groove", bd = 6, cursor = "Trek")

FrameBD.pack()


# ------------ Definición de los Campos de Entrada  ------------

textID = Entry(FrameBD)
textID.grid(row = 0, column = 1, padx = 10, pady = 10)

textName = Entry(FrameBD)
textName.grid(row = 1, column = 1, padx = 10, pady = 10)
textName.config(fg = "darkgreen", justify = "left")

textRace = Entry(FrameBD)
textRace.grid(row = 2, column = 1, padx = 10, pady = 10)

textVillage = Entry(FrameBD)
textVillage.grid(row = 3, column = 1, padx = 10, pady = 10)

textPassword = Entry(FrameBD)
textPassword.grid(row = 4, column = 1, padx = 10, pady = 10)
textPassword.config(show = "*")

textDescription =  Text(FrameBD, width = 16, height = 7) # Cuadro de Texto. 
textDescription.grid(row = 5, column = 1, padx = 10, pady = 10)


# ------------ Scrollbar del Campo 5 ------------

scrollvertix = Scrollbar(FrameBD, command = textDescription.yview)
scrollvertix.grid(row = 5, column = 2, sticky = "nsew")
textDescription.config(yscrollcommand = scrollvertix.set)


# ------------  Etiquetas ------------

labelId = Label(FrameBD, text = "Id of the Goblin:")
labelId.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = W)

labelName = Label(FrameBD, text = "Name:")
labelName.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = W)

labelRace = Label(FrameBD, text = "Race:")
labelRace.grid(row = 2, column = 0, padx = 10, pady = 10, sticky = W)

labelVillage = Label(FrameBD, text = "Village:")
labelVillage.grid(row = 3, column = 0, padx = 10, pady = 10, sticky = W)

labelPassword = Label(FrameBD, text = "Password:")
labelPassword.grid(row = 4, column = 0, padx = 10, pady = 10, sticky = W)

labelDescription = Label(FrameBD, text = "Description:")
labelDescription.grid(row = 5, column = 0, padx = 10, pady = 10, sticky = NW)


# ------------ Frame 2 para Botones inferiores ------------

FrameButt = Frame(root)

FrameButt.config(bg = "#EEEEEE", relief = "groove", bd = 6, cursor = "Spider")

FrameButt.pack()

buttonCreate = Button(FrameButt, text = "Create")
buttonCreate.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "e")

buttonRead = Button(FrameButt, text = "Read")
buttonRead.grid(row = 0, column = 1, padx = 10, pady = 10, sticky = "e")

buttonUpdate = Button(FrameButt, text = "Update")
buttonUpdate.grid(row = 0, column = 2, padx = 10, pady = 10, sticky = "e")

buttonDelete = Button(FrameButt, text = "Delete")
buttonDelete.grid(row = 0, column = 3, padx = 10, pady = 10, sticky = "e")


root.mainloop()