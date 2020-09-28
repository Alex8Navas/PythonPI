# Clase 43. Curso Píldoras Informáticas.

# Control de Flujo. Interfaces Gráficas 2.

# Manejo de Frames. 

from tkinter import *

root = Tk()

root.title("La Ventana de Moria")

root.iconbitmap("GOT.ico")

# root.geometry("1000x700") # Esto lo contendrá el frame, luego no es necesario. La raíz se adapta al frame. 

root.resizable(True,True)

root.config(bg = "#373737")

root.config(bd = 35, relief = "sunken", cursor = "trek")

FrameMoria = Frame() # Creación del marco. Con esto solamente no vale. Es necesario empaquetarlo. 

FrameMoria.pack(side = "bottom", anchor="w") # Empaquetado del marco. 
# Opciones de empaquetado: 
# Con side se puede mover el marco dentro de la ventana. Las opciones son top, right, let y bottom. 
# Con anchor se complementa side. Toma por parámetros los puntos cardinales (n, s, e, w). 
# En este caso se ha puesto abajo (bottom) a la izquierda (west). 
# Con fill se puede hacer que al ampliar la ventana el marco se amplíe con ella. Si se pone fill = "x"
# se amplía a lo ancho, y si se hace fill = "y", expand = True se amplía a lo alto. Para que se haga en 
# sendas direcciones se ha de poner fill = "both", expand = True.

FrameMoria.config(bg = "ivory", width = "1000", height= "700")

FrameMoria.config(bd = 25, relief = "groove") # Configurar el borde. Con bd se da el ancho del borde y con relief la forma.
# Otra opción para el borde puede ser relief = "sunken".

FrameMoria.config(cursor = "spider") # Cmabia el cursor sobre el marco. Opciones: hand2, pirate, mouse, spider, trek...

root.mainloop()
