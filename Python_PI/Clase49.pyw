# Clase 49. Curso Píldoras Informáticas.

# Control de Flujo. Interfaces Gráficas 8.

# Proyecto Calculadora 3. 

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
	cursor = "exchange")

#-----------Variables Globales------------------

operation = "" # Cadena vacía
resultado = 0


#--------------Pantalla-----------------

NumberPantalla = StringVar()

Pantalla = Entry(FrameCalculadora, textvariable = NumberPantalla)
Pantalla.grid(row = 1, column = 1, padx = 10, pady = 10, columnspan = 4) # Con columnspan hacemos que la pantalla se estire a 4 columnas (en diseño web es colspan). 
Pantalla.config(bg = "#373737", fg = "#EEEEEE", justify = "right")

#-----------Pulsa el Teclado--------------


def NumberPulsado(number):

	global operation

	if operation != "": # Si se pulsa un comando de operación se ha de hacer que:

		NumberPantalla.set(number) # Deje de concatenar números y escriba uno nuevo. 

		operation = "" # Para que vuelva a concatenar números. 

	else:

		NumberPantalla.set(NumberPantalla.get() + number)


#--------------Suma------------

def suma(number):

	global operation

	global resultado

	resultado += int(number)

	operation = "suma"

	NumberPantalla.set(resultado)

#--------------Igual------------


def igual():

	global resultado

	NumberPantalla.set(resultado + int(NumberPantalla.get()))

	resultado = 0 # Se resetea tras dar a igual.  


#----------Fila Uno------------

Boton7 = Button(FrameCalculadora, text = "7", width = 3,  command = lambda:NumberPulsado("7")) # width para ajustar el tamaño del botón. 
Boton8 = Button(FrameCalculadora, text = "8", width = 3,  command = lambda:NumberPulsado("8"))
Boton9 = Button(FrameCalculadora, text = "9", width = 3,  command = lambda:NumberPulsado("9"))
BotonDivide = Button(FrameCalculadora, text = "%", width = 3)

# Ubicación de botones.
Boton7.grid(row = 2, column = 1)
Boton8.grid(row = 2, column = 2)
Boton9.grid(row = 2, column = 3)
BotonDivide.grid(row = 2, column = 4)


#----------Fila Dos------------

Boton4 = Button(FrameCalculadora, text = "4", width = 3,  command = lambda:NumberPulsado("4"))
Boton5 = Button(FrameCalculadora, text = "5", width = 3,  command = lambda:NumberPulsado("5"))
Boton6 = Button(FrameCalculadora, text = "6", width = 3,  command = lambda:NumberPulsado("6"))
BotonMultiplica = Button(FrameCalculadora, text = "x", width = 3)

# Ubicación de botones.
Boton4.grid(row = 3, column = 1)
Boton5.grid(row = 3, column = 2)
Boton6.grid(row = 3, column = 3)
BotonMultiplica.grid(row = 3, column = 4)

#----------Fila Tres------------

Boton1 = Button(FrameCalculadora, text = "1", width = 3,  command = lambda:NumberPulsado("1")) 
Boton2 = Button(FrameCalculadora, text = "2", width = 3,  command = lambda:NumberPulsado("2"))
Boton3 = Button(FrameCalculadora, text = "3", width = 3,  command = lambda:NumberPulsado("3"))
BotonResta = Button(FrameCalculadora, text = "-", width = 3)

# Ubicación de botones.
Boton1.grid(row = 4, column = 1)
Boton2.grid(row = 4, column = 2)
Boton3.grid(row = 4, column = 3)
BotonResta.grid(row = 4, column = 4)

#----------Fila Cuatro------------

BotonComa = Button(FrameCalculadora, text = ",", width = 3, command = lambda:NumberPulsado(".")) # width para ajustar el tamaño del botón. 
Boton0 = Button(FrameCalculadora, text = "0", width = 3, command = lambda:NumberPulsado("0"))
BotonIgual = Button(FrameCalculadora, text = "=", width = 3, command=lambda:igual())
BotonSuma = Button(FrameCalculadora, text = "+", width = 3, command=lambda:suma(NumberPantalla.get()))

# Ubicación de botones.
BotonComa.grid(row = 5, column = 1)
Boton0.grid(row = 5, column = 2)
BotonIgual.grid(row = 5, column = 3)
BotonSuma.grid(row = 5, column = 4)

root.mainloop()