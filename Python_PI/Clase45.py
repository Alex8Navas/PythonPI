# Clase 45. Curso Píldoras Informáticas.

# Control de Flujo. Interfaces Gráficas 4.

# Widgets para introducir texto. 

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


# Intorducir cuadro de texto en la raíz:

TextoMoria = Entry(root) 

TextoMoria.pack()

# Se puede poner también en el marco. 

NombreMoria = Entry(FrameMoria)

# TextoMoria2.place(x = 500, y = 500)
NombreMoria.grid(row = 0, column = 1, padx = 10, pady = 10)
# Padx y Pady sirve para definir los límites de separación entre widgets en píxeles
NombreMoria.config(fg = "#4E0232") # Si pones justify = "center" se ajusta la alineación del texto al centro del cuadro (las otras opciones son right y left).


# Añadir texto para decir al usuario qué introducir en el cuadro. 
IndicaMoria1 = Label(FrameMoria, text = "Nombre:")

# IndicaMoria.place(x= 500, y = 500) 
# Si pones la misma coordenada x que en el cuadro de texto este widget empuja al cuadro de texto. Esta práctica no está recomendada. 
# Se puede soucionar esto con pack (pero eso lastra el resto de elementos) o con grid, que crea una grilla. 
# Otra opción es ajustar las coordenadas con place. 

IndicaMoria1.grid(row = 0, column = 0, sticky = "e", padx = 10, pady = 10)
# Sticky es un indicador para alinear texto. Admite los puntos cardinales y sus combianciones (se, ne, nw, sw).

# Otro cuadro de texto:
ApellidoMoria = Entry(FrameMoria)
ApellidoMoria.grid(row = 1, column = 1, padx = 10, pady = 10)
ApellidoMoria.config(fg = "#4E0232")
IndicaMoria2 = Label(FrameMoria, text = "Apellidos:")
IndicaMoria2.grid(row = 1, column = 0, sticky = "e", padx = 10, pady = 10)

# Otro cuadro de texto: 
DireccMoria = Entry(FrameMoria)
DireccMoria.grid(row = 2, column = 1, padx = 10, pady = 10)
DireccMoria.config(fg = "#4E0232")
IndicaMoria3 = Label(FrameMoria, text = "Dirección:")
IndicaMoria3.grid(row = 2, column = 0, sticky = "e", padx = 10, pady = 10)

# Otro cuadro de texto:
PassMoria = Entry(FrameMoria)
PassMoria.grid(row = 3, column = 1, padx = 10, pady = 10)
PassMoria.config(fg = "#4E0232", show = "*")
IndicaMoria4 = Label(FrameMoria, text = "Contraseña:")
IndicaMoria4.grid(row = 3, column = 0, sticky = "e", padx = 10, pady = 10)

root.mainloop()
