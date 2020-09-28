# Clase 47. Curso Píldoras Informáticas.

# Control de Flujo. Interfaces Gráficas 6.

# Proyecto Calculadora. 

from tkinter import * 

root = Tk()

root.iconbitmap("GOT.ico")

root.config(bg = "#373737",
 relief = "groove",
 bd = 35,
 cursor = "Trek")

root.resizable(True, True)

FrameCalculadora = Frame(root)

FrameCalculadora.pack()

FrameCalculadora.config(bg = "#EEEEEE",  
	relief = "groove",
	bd = 25,
	cursor = "spider")

#--------------Pantalla-----------------

Pantalla = Entry(FrameCalculadora)
Pantalla.grid(row = 1, column = 1, padx = 10, pady = 10, columnspan = 4) # Con columnspan hacemos que la pantalla se estire a 4 columnas (en diseño web es colspan). 
Pantalla.config(bg = "#373737", fg = "#EEEEEE", justify = "right")

#----------Fila Uno------------

Boton7 = Button(FrameCalculadora, text = "7", width = 3) # width para ajustar el tamaño del botón. 
Boton8 = Button(FrameCalculadora, text = "8", width = 3)
Boton9 = Button(FrameCalculadora, text = "9", width = 3)
BotonDivide = Button(FrameCalculadora, text = "%", width = 3)

# Ubicación de botones.
Boton7.grid(row = 2, column = 1)
Boton8.grid(row = 2, column = 2)
Boton9.grid(row = 2, column = 3)
BotonDivide.grid(row = 2, column = 4)


#----------Fila Dos------------

Boton4 = Button(FrameCalculadora, text = "4", width = 3) # width para ajustar el tamaño del botón. 
Boton5 = Button(FrameCalculadora, text = "5", width = 3)
Boton6 = Button(FrameCalculadora, text = "6", width = 3)
BotonMultiplica = Button(FrameCalculadora, text = "x", width = 3)

# Ubicación de botones.
Boton4.grid(row = 3, column = 1)
Boton5.grid(row = 3, column = 2)
Boton6.grid(row = 3, column = 3)
BotonMultiplica.grid(row = 3, column = 4)

#----------Fila Tres------------

Boton1 = Button(FrameCalculadora, text = "1", width = 3) # width para ajustar el tamaño del botón. 
Boton2 = Button(FrameCalculadora, text = "2", width = 3)
Boton3 = Button(FrameCalculadora, text = "3", width = 3)
BotonResta = Button(FrameCalculadora, text = "-", width = 3)

# Ubicación de botones.
Boton1.grid(row = 4, column = 1)
Boton2.grid(row = 4, column = 2)
Boton3.grid(row = 4, column = 3)
BotonResta.grid(row = 4, column = 4)

#----------Fila Cuatro------------

BotonComa = Button(FrameCalculadora, text = ",", width = 3) # width para ajustar el tamaño del botón. 
Boton0 = Button(FrameCalculadora, text = "0", width = 3)
BotonIgual = Button(FrameCalculadora, text = "=", width = 3)
BotonSuma = Button(FrameCalculadora, text = "+", width = 3)

# Ubicación de botones.
BotonComa.grid(row = 5, column = 1)
Boton0.grid(row = 5, column = 2)
BotonIgual.grid(row = 5, column = 3)
BotonSuma.grid(row = 5, column = 4)

root.mainloop()

