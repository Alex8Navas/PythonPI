# Clase 50. Curso Píldoras Informáticas.

# Control de Flujo. Interfaces Gráficas 9.

# Proyecto Calculadora 4. 

from tkinter import * 

root = Tk()

root.iconbitmap("GOT.ico")

root.title("Moria")

root.config(bg = "#373737",
 relief = "groove",
 bd = 35,
 cursor = "Trek")

root.resizable(False, False)

FrameCalculadora = Frame(root)

FrameCalculadora.pack()
# Conpack(fill="both", expand=1) se expande el frame con la raíz. 

FrameCalculadora.config(bg = "#EEEEEE",  
	relief = "groove",
	bd = 25,
	cursor = "exchange")

#-----------Variables Globales------------------

operation = "" # Cadena vacía
resultado = 0
resetea = False


#--------------Pantalla-----------------

NumberPantalla = StringVar()

Pantalla = Entry(FrameCalculadora, textvariable = NumberPantalla)
Pantalla.grid(row = 1, column = 1, padx = 10, pady = 10, columnspan = 4) # Con columnspan hacemos que la pantalla se estire a 4 columnas (en diseño web es colspan). 
Pantalla.config(bg = "#373737", fg = "#EEEEEE", justify = "right")

#-----------Pulsa el Teclado--------------


def NumberPulsado(number):

	global operation

	global resetea

	if resetea: # Si se pulsa un comando de operación se ha de hacer que:

		NumberPantalla.set(number) # Deje de concatenar números y escriba uno nuevo. 

		resetea = False 

	else:

		NumberPantalla.set(NumberPantalla.get() + number)


#--------------Suma------------

def suma(number):

	global operation

	global resultado

	global resetea

	resultado += float(number)

	operation = "Suma"

	resetea = True

	NumberPantalla.set(resultado)



#--------------Resta------------

number1 = 0

contador_resta = 0

def resta(number):

	global operation

	global resultado

	global number1

	global contador_resta

	global resetea

	if contador_resta == 0:

		number1 = float(number)

		resultado = number1

	else:

		if contador_resta == 1:

			resultado = number1 - float(number)

		else:

			resultado = float(resultado) - float(num)	

		numeroPantalla.set(resultado)

		resultado = numeroPantalla.get()


	contador_resta += 1

	operation = "Resta"

	resetea = True


#--------------Multiplicación------------

contador_mult = 0

def multiplica(number):

	global operation

	global resultado

	global contador_mult

	global number1

	global resetea

	if contador_mult == 0:

		number1 = float(number)

		resultado = number1

	else:

		if contador_mult == 1:

			resultado = number1 * float(number)

		else:

			resultado = float(resultado) *  float(number)

		NumberPantalla.set(resultado)

		resultado = NumberPantalla.get()

	contador_mult += 1

	operation = "Multiplicación"

	resetea = True



#--------------División------------

contador_div = 0

def divide(number):

	global resultado

	global resetea

	global number1

	global contador_div

	global operation

	if contador_div == 0:

		number1 = float(number)

		resultado = number1

	else:

		if contador_div == 1:

			resultado = number1/float(number)

		else:

			resultado = resultado/float(number)

		NumberPantalla.set(resultado)

		resultado = NumberPantalla.get()

	contador_div += 1

	operation = "División"

	resetea = True




#--------------Igual------------


def igual():

	global resultado

	global contador_resta

	global contador_mult

	global contador_div

	global operation

	if operation == "Suma":

		NumberPantalla.set(resultado + float(NumberPantalla.get()))

		resultado = 0 # Se resetea tras dar a igual.  

	elif operation == "Resta":

		NumberPantalla.set(resultado - float(NumberPantalla.get()))

		resultado = 0

		contador_resta = 0

	elif operation == "Multiplicación":

		NumberPantalla.set(resultado * float(NumberPantalla.get()))

		resultado = 0

		contador_mult = 0

	elif operation == "División":

	 	NumberPantalla.set(resultado / float(NumberPantalla.get()))

	 	resultado = 0

	 	contador_div = 0





#----------Fila Uno------------

Boton7 = Button(FrameCalculadora, text = "7", width = 3,  command = lambda:NumberPulsado("7")) # width para ajustar el tamaño del botón. 
Boton8 = Button(FrameCalculadora, text = "8", width = 3,  command = lambda:NumberPulsado("8"))
Boton9 = Button(FrameCalculadora, text = "9", width = 3,  command = lambda:NumberPulsado("9"))
BotonDivide = Button(FrameCalculadora, text = "%", width = 3, command = lambda:divide(NumberPantalla.get()))

# Ubicación de botones.
Boton7.grid(row = 2, column = 1)
Boton8.grid(row = 2, column = 2)
Boton9.grid(row = 2, column = 3)
BotonDivide.grid(row = 2, column = 4)


#----------Fila Dos------------

Boton4 = Button(FrameCalculadora, text = "4", width = 3,  command = lambda:NumberPulsado("4"))
Boton5 = Button(FrameCalculadora, text = "5", width = 3,  command = lambda:NumberPulsado("5"))
Boton6 = Button(FrameCalculadora, text = "6", width = 3,  command = lambda:NumberPulsado("6"))
BotonMultiplica = Button(FrameCalculadora, text = "x", width = 3, command = lambda:multiplica(NumberPantalla.get()))

# Ubicación de botones.

Boton4.grid(row = 3, column = 1)
Boton5.grid(row = 3, column = 2)
Boton6.grid(row = 3, column = 3)
BotonMultiplica.grid(row = 3, column = 4)

#----------Fila Tres------------

Boton1 = Button(FrameCalculadora, text = "1", width = 3,  command = lambda:NumberPulsado("1")) 
Boton2 = Button(FrameCalculadora, text = "2", width = 3,  command = lambda:NumberPulsado("2"))
Boton3 = Button(FrameCalculadora, text = "3", width = 3,  command = lambda:NumberPulsado("3"))
BotonResta = Button(FrameCalculadora, text = "-", width = 3, command = lambda:resta(NumberPantalla.get()))

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