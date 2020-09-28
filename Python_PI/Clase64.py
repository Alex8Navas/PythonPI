# Clase 64. Curso Píldoras Informáticas.

# Control de Flujo. Práctica Guiada 6. 

# Leer y actualizar registros. 

from tkinter import *
from tkinter import messagebox
import sqlite3


# ---------------------- FUNCIONES --------------------------

def connectBD(): # Creación de la base de Datos. 

	conexion = sqlite3.connect("BBDD/GoblinsBase")

	puntero = conexion.cursor()

	try: 
		puntero.execute("""

			CREATE Table GoblinsData(
			ID INTEGER PRIMARY KEY AUTOINCREMENT,
			NAME VARCHAR(50),
			RACE VARCHAR(50),
			VILLAGE VARCHAR(20),
			PASSWORD VARCHAR (16),
			DESCRIPTION VARCHAR(10000)
			)

		""")
		
		messagebox.showinfo("Goblins Base", "Base de datos de Goblins creada con éxito")

	except: 

		messagebox.showwarning("¡Cuidado!", "La Base de Goblins ya fue creada")


def exitApp(): # Salida de la aplicación. 

	value = messagebox.askquestion("Salida de Moria", "¿Desea salir de la aplicación, noble goblin?")

	if value == "yes":

		root.destroy()


def cleanVar(): # Resetear todos los campos. 

	SID.set("")
	SName.set("")
	SRace.set("")
	SVillage.set("")
	SPassword.set("")

	# Para el Cuadro de Texto es diferente: 
	textDescription.delete(1.0, END) # Borrar desde el primer carácter hasta el final. 


def createGoblin(): # Crear un registro. 

	conexion = sqlite3.connect("BBDD/GoblinsBase")

	puntero = conexion.cursor()

	# Son mejores las consultas paramétricas: se verá en el curso de MySQL. 
	puntero.execute("INSERT INTO GoblinsData VALUES(NULL, '" + SName.get() + # Comillas anidadas para concatenar. 
		"','" + SRace.get() +
		"','" + SVillage.get() +
		"','" + SPassword.get() +
		"','" + textDescription.get("1.0", END) + "')") 

	conexion.commit()

	messagebox.showinfo("Goblin´s Base", "Ha nacido un goblin, hermanos")


def readGoblin(): # Lectura de registro. 

	conexion = sqlite3.connect("BBDD/GoblinsBase")

	puntero = conexion.cursor()

	# Se selecciona la información por el ID. 
	puntero.execute("SELECT * FROM GoblinsData WHERE ID =" + SID.get())
	# Se toma y guarda dicha información en una variable. 
	goblinread = puntero.fetchall()
	# Se recorren los campos y se muestra:
	for field in goblinread:

		SID.set(field[0])
		SName.set(field[1])
		SRace.set(field[2])
		SVillage.set(field[3])
		SPassword.set(field[4])
		textDescription.insert(1.0, field[5])

def updateGoblin():

	conexion = sqlite3.connect("BBDD/GoblinsBase")

	puntero = conexion.cursor()

	puntero.execute("UPDATE GoblinsData SET NAME='" + SName.get() +
		"', RACE='" + SRace.get() + 
		"', VILLAGE='" + SVillage.get() +
		"', PASSWORD='" + SPassword.get() +
		"', DESCRIPTION='" + textDescription.get("1.0", END) + 
		"' WHERE ID=" + SID.get())

	conexion.commit()

	messagebox.showinfo("Goblin´s Base", "Su goblin ha experimentado una transformación") 



# ---------------------- INTERFAZ --------------------------

root = Tk()

root.title("La Guarida del Goblin")

root.iconbitmap("goblin.ico")

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
BDMenu.add_command(label = "Establish Connection", command = connectBD)
BDMenu.add_command(label = "Exit", command = exitApp)

DelMenu.add_command(label = "Delete Fields", command = cleanVar)

CRUDMenu.add_command(label = "Create", command = createGoblin)
CRUDMenu.add_command(label = "Read", command = readGoblin)
CRUDMenu.add_command(label = "Update", command = updateGoblin)
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

# ------------ Variables String de los Campos de Entrada  ------------

SID = StringVar()
SName = StringVar()
SRace = StringVar()
SVillage = StringVar()
SPassword = StringVar()
# SDescription = StringVar() // con los textos no es necesario definir estas variables. 

# ------------ Definición de los Campos de Entrada  ------------

textID = Entry(FrameBD, textvariable = SID)
textID.grid(row = 0, column = 1, padx = 10, pady = 10)

textName = Entry(FrameBD, textvariable = SName)
textName.grid(row = 1, column = 1, padx = 10, pady = 10)
textName.config(fg = "darkgreen", justify = "left")

textRace = Entry(FrameBD, textvariable = SRace)
textRace.grid(row = 2, column = 1, padx = 10, pady = 10)

textVillage = Entry(FrameBD, textvariable = SVillage)
textVillage.grid(row = 3, column = 1, padx = 10, pady = 10)

textPassword = Entry(FrameBD, textvariable = SPassword)
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

buttonCreate = Button(FrameButt, text = "Create", command = createGoblin)
buttonCreate.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "e")

buttonRead = Button(FrameButt, text = "Read", command = readGoblin)
buttonRead.grid(row = 0, column = 1, padx = 10, pady = 10, sticky = "e")

buttonUpdate = Button(FrameButt, text = "Update", command = updateGoblin)
buttonUpdate.grid(row = 0, column = 2, padx = 10, pady = 10, sticky = "e")

buttonDelete = Button(FrameButt, text = "Delete")
buttonDelete.grid(row = 0, column = 3, padx = 10, pady = 10, sticky = "e")


# ------------  ------------

root.mainloop()
