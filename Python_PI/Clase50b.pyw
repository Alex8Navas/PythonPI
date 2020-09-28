# Clase 50b. Curso Píldoras Informáticas.

# Control de Flujo. Interfaces Gráficas 9.

# Los Radio Buttons


from tkinter import *

root = Tk()

root.iconbitmap("GOT.ico")

root.title("La Radio de Moria")

root.config(bg = "#373737",
 relief = "groove",
 bd = 35,
 cursor = "Trek")

root.resizable(True, True)

FrameRadio = Frame(root)

FrameRadio.pack(fill = "both", expand = 1)

FrameRadio.config(bg = "#EEEEEE",  relief = "groove", bd = 25, cursor = "Trek")

def imprimir(): 

	print(varOption.get()) # Muestra en consola el valor elegido (1 o 2)

	if varOption.get() == 1:

		elegido.config(text = "Es usted un caballero.", fg = "#373737")

	elif varOption.get() == 2:

		elegido.config(text = "Es usted una dama.", fg = "#373737")

	elif varOption.get() == 3:

		elegido.config(text = "Es usted un alien.", fg = "#373737")

Label(FrameRadio, text = "Género: ").grid(row = 0, column = 0, padx = 0, pady = 5, sticky = W)

varOption = IntVar() # Para que se pueda moificar el estado del botón (encendido o apagado). 

RB1 = Radiobutton(FrameRadio, text = "Varón", variable = varOption, value = 1, command = imprimir)
RB1.grid(row = 1, column = 1, padx = 5, pady = 5, sticky = W)
RB1.config(justify="right")

RB2 = Radiobutton(FrameRadio, text = "Hembra", variable = varOption, value = 2, command = imprimir)
RB2.grid(row = 2, column = 1, padx = 5, pady = 5, sticky = W)
RB2.config(justify="right")

RB3 = Radiobutton(FrameRadio, text = "Otros", variable = varOption, value = 3, command = imprimir)
RB3.grid(row = 3, column = 1, padx = 5, pady = 5, sticky = W)
RB3.config(justify="right")

elegido = Label(FrameRadio)
elegido.grid(row = 4, column = 0, padx = 0, pady = 5, sticky = W, columnspan = 2)

root.mainloop()

