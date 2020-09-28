# Clase 73. Curso Píldoras Informáticas.

# Control de Flujo. Decoradores 1.

# Decorador: son funciones que añaden elementos (decoraciones) a otras funciones.
# Un decorador se compone de tres funciones (A,B,C) donde A recibe como parámetro a B y devuelve C. 
# Esto quiere decir que el dcorador devuelve una función. 

# La sintaxis sería así:
# def funciónA(Función B):
#	def FunciónC():
#		lo que hagga la función C
#	return FunciónC

# La función A es el decorador, la B es la función que se decora y la C es la función interna del decorador. 

def decorador(funcionB):

	def funcInterna():
		# Acciones decoradoras: 
		print("Se ejecutará el siguiente cálculo:")

		funcionB() # Lo que devuelva la función a decorar.

		print("Cálculo finalizado.\n")

	return funcInterna

@decorador # Así se especifica la llamada al decorador. 
def suma():

	print("8 + 8 =",8+8 )

@decorador
def resta():

	print("8 - 8 =", 8-8)

suma()

resta()

# Estas funciones decoradoras tienen mucha utilidad para llamar a bases de datos. 
# Esto es, en lugar de llamar a la base de datos dentro de cada función, se la llama
# dentro de la función decoradora y se añade el decorador a cada función. 