# Clase 44. Curso Píldoras Informáticas.

# Control de Flujo. Interfaces Gráficas 3.

# Label: sirev tanto para mostrar texto como para mostrar imágenes. 

from tkinter import *

root = Tk()

root.iconbitmap("GOT.ico")

root.config(bg = "#373737",
 relief = "groove",
 bd = 35,
 cursor = "Trek")

root.resizable(True, True)


FrameMoria = Frame(root,
 width = "1000",
 height= "700")

FrameMoria.pack()

FrameMoria.config(bg = "#EEEEEE",  
	relief = "groove",
	bd = 25,
	cursor = "pirate")

LabelMoria = Label(FrameMoria, text = """Han tomado el puente y la segunda sala. Hemos atrancado las puertas, pero no
podremos detenerlos por mucho tiempo. ¡El suelo tiembla!. Tambores… Tambores
en lo profundo. No podemos salir. Una sombra se mueve en la oscuridad.
No podemos salir. Ya vienen...""", fg = "#373737", font = ("Stencil", 12))

# LabelMoria.pack() # Adapta el contenedor a las dimensiones del lable por defecto. Por ello se usa place. 

LabelMoria.place(x = 100, y = 100) 

GIFMoria = PhotoImage(file = "Images/Eowyn.gif")

Label(FrameMoria, image = GIFMoria).place(x = 200, y = 200)

root.mainloop()
