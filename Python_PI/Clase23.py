# Clase 23. Curso Píldoras Informáticas.

# Control de Flujo. Excepciones 3.

# Excepciones propias: Raise. 

def evalEdad(edad):

	if edad < 0:
		raise TypeError("No se permiten edades negativas") # Mensaje personalizado. 

	if edad < 20:
		return "Joven."
	elif edad < 40:
		return "Joven Adulto."
	elif edad < 65:
		return "Adulto."
	elif edad < 100:
		return "Signore."

print(evalEdad(99))
# print(evalEdad(-66))

import math 

print("\nPrograma de Cálculo de Raíces")

def Calcularoot(number1):

	if number1 < 0:
		raise ValueError("No se puede calcular la raíz de un número negativo.")

	else: 
		return math.sqrt(number1)

numberint = int(input("Introduce un número: "))

try:
	
	print(Calcularoot(numberint))

except ValueError as RootNegativa:
	
	print(RootNegativa)


print("Programa Finalizado.")
