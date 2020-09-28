# Clase 42. Curso Píldoras Informáticas.

# Control de Flujo. Interfaces Gráficas 1.

# Interfaz gráfica (GUI): ventana con la que el usuario interacciona. 

# Librería Tkinter. Otras opciones: WxPython, PyQT, PyGTK. 

# Tkinter es una librería puente entre Python y la librería TCL/TK de otros lenguajes como Perl, Rubi, etc.

# Raíz: Es la ventana. 
# Frame: Aglutinador de elementos o widgets. El propio frame es también un widget de la ventana.


from tkinter import *


root = Tk() # Se construye la raíz. 

root.title("Ventana de Moria")

root.resizable(1,1) # resizable(width, height): Fijas la ventana si pones 0,0 (el usuario no puede manipular el ancho y el alto de ésta). 
# Esta función toma ancho y alto cpmo booleanos, admiten 1 ó 0, donde 1 es True y permite redimensionar, y 0 es False y bloquea esto. 

root.iconbitmap("GOT.ico") # Cambias el icono de la ventana (por defecto es una pluma).

root.geometry("650x350") # Cambia el tamaño de la ventana que sale por defecto.

root.config(bg="darkgray") # Cambia el color del fondo de la ventana (por defecto es blanco). 

root.mainloop() # Ejecución de la ventana (mainloop es un bucle infinito par mantener la app corriendo).

# Hay que cambiar la extensión del archivo a .pyw para que no se abra la consola al abrir la aplicación. 