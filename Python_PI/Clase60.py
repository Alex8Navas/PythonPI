# Clase 60. Curso Píldoras Informáticas.

# Control de Flujo. Práctica Guiada 2. 

# Crear el Menú & Cuadros de Texto. 

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


root.mainloop()