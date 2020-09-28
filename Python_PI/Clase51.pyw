# Clase 51. Curso Píldoras Informáticas.

# Control de Flujo. Interfaces Gráficas 10.

# Los Checkbuttons


from tkinter import *

root = Tk()

root.title("La Prueba de Moria")

root.iconbitmap("GOT.ico")

root.config(bg = "#373737",
 relief = "groove",
 bd = 35,
 cursor = "Trek")

root.resizable(True, True)

foto = PhotoImage(file = "Images/Steampunk-Art.png")
Label(root, image = foto).pack()

FrameCheck = Frame(root)

FrameCheck.pack(fill = "both", expand = 1)

FrameCheck.config(bg = "#EEEEEE",  relief = "groove", bd = 25, cursor = "Trek")

# Si se pone aquí la foto, es decir, tras la creación del marco, saldrá debajo de las opciones. 
# foto = PhotoImage(file = "Images/Steampunk-Art.png")
# Label(root, image = foto).pack()

Label(FrameCheck, text = "Elija su destino: ", width = 50).grid(row = 0, column = 0, padx = 5, pady = 5, sticky = W)

Norte = IntVar()
Sur = IntVar()
Este = IntVar()
Oeste = IntVar()


def rumbo():

	elegido = ""

	if Norte.get()==1:

		elegido += "No marches hacia el Norte, se ha iniciado una guerra.\n"

	if Sur.get()==1:

		elegido += "Oh, Dorne, es la elección idónea para descansar.\n" 

	if Este.get()==1:

		elegido += "La región del Este es tierra de malechores, no te aconsejo acudir.\n" 

	if Oeste.get()==1:

		elegido += "Acudirás a la tierra de los barbas grises.\n"  

	Description.config(text = elegido)


CB1 = Checkbutton(FrameCheck, text = "Al Norte", variable = Norte, onvalue = 1, offvalue = 0, command = rumbo) 
# Onvalue define el valor de la variable si está seleccionada. 
# Offvalue define el valor de la variable cuando no se encuentra el botón pulsado. 
CB1.grid(row = 1, column = 1, padx = 5, pady = 5, sticky = W)

CB2 = Checkbutton(FrameCheck, text = "Al Este", variable = Este, onvalue = 1, offvalue = 0, command = rumbo)
CB2.grid(row = 2, column = 1, padx = 5, pady = 5, sticky = W)

CB3 = Checkbutton(FrameCheck, text = "Al Sur", variable = Sur, onvalue = 1, offvalue = 0, command = rumbo)
CB3.grid(row = 3, column = 1, padx = 5, pady = 5, sticky = W)

CB4 = Checkbutton(FrameCheck, text = "Al Oeste", variable = Oeste, onvalue = 1, offvalue = 0, command = rumbo)
CB4.grid(row = 4, column = 1, padx = 5, pady = 5, sticky = W)

Description = Label(FrameCheck)
Description.grid(row = 5, column = 0, padx = 5, pady = 5, sticky = W, columnspan = 2)

root.mainloop()