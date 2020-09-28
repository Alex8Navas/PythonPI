# Clase 46. Curso Píldoras Informáticas.

# Control de Flujo. Interfaces Gráficas 5.

# Text: widget para la introducción de texto largo.
# Button: Botones para la interacción con la interfaz. 

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
	cursor = "spider")

Myname = StringVar() # Se define una variable vacía donde poner tu nombre. 
NombreMoria = Entry(FrameMoria, textvariable = Myname) # Se asocia la etiqueta a la variable creada. 
NombreMoria.grid(row = 0, column = 1, padx = 10, pady = 10)
NombreMoria.config(fg = "gray", justify = "right")

ApellidoMoria = Entry(FrameMoria)
ApellidoMoria.grid(row = 1, column = 1, padx = 10, pady = 10)
ApellidoMoria.config(fg = "gray", justify = "right")

LocMoria = Entry(FrameMoria)
LocMoria.grid(row = 2, column = 1, padx = 10, pady = 10)
LocMoria.config(fg = "gray", justify = "right")

PassMoria = Entry(FrameMoria)
PassMoria.grid(row = 3, column = 1, padx = 10, pady = 10)
PassMoria.config(fg = "gray", justify = "right")


ComentariosMoria = Text(FrameMoria, width = 15, height = 8) # Dimensiones del cuadro de texto creado. Por defecto es muy grande. 
ComentariosMoria.grid(row = 5, column = 1, padx = 10, pady = 10)

# Por defecto el cuadro de texto no tiene scroll-bar. Hay que crearla. 

ScrollMoria = Scrollbar(FrameMoria, command = ComentariosMoria.yview) # Con yview se pone vertical la barrita. 
ScrollMoria.grid(row = 5, column = 2, sticky = "nsew") # Se coloca la barrita. 
# Con sticky = "nsew" la barrita se adapta al cuadro de texto al que pertence. 

ComentariosMoria.config(yscrollcommand = ScrollMoria.set) # Para que el posicionador de la barrita se mueva con el texto. 

NombreLabel = Label(FrameMoria, text = "Nombre:")
NombreLabel.grid(row = 0, column = 0, sticky = "e", padx = 10, pady = 10)

ApellidoLabel = Label(FrameMoria, text = "Apellido:")
ApellidoLabel.grid(row = 1, column = 0, sticky = "e", padx = 10, pady = 10)

LocLabel = Label(FrameMoria, text = "Localización:")
LocLabel.grid(row = 2, column = 0, sticky = "e", padx = 10, pady = 10)

PassLabel = Label(FrameMoria, text = "Contraseña:")
PassLabel.grid(row = 3, column = 0, sticky = "e", padx = 10, pady = 10)


ComentariosLabel = Label(FrameMoria, text = "Comentarios:")
ComentariosLabel.grid(row = 5, column = 0, sticky = "e", padx = 10, pady = 10)

# Agregar un botón a la consola. 
def FunctionBoton():
	Myname.set("Escriba su nombre, caballero.") # Se da un valor a la variable. 



ButtMoria = Button(root, text = "Enviar", command = FunctionBoton)
ButtMoria.pack()

root.mainloop()

