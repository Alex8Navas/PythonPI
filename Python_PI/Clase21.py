# Clase 21. Curso Píldoras Informáticas.

# Control de Flujo. Excepciones 1.

def suma(num1, num2):
	return num1 + num2 

def resta(num1, num2):
	return num1 - num2 

def multiplica(num1, num2):
	return num1 * num2 

# Capturas de Excepción: ZeroDivisionError
def divide(num1, num2):
	try:
		return num1 / num2 
	except ZeroDivisionError:
		print("La división entre cero no es aplicable.")
		return "Operación Errónea."

op1 = int(input("Introduce el primer número: "))
op2 = int(input("Introduce el segundo número: "))
operacion = input("""Introduce una operación entre: 
	1. Suma. 
	2. Resta.
	3. Divide.
	4. Multipllica.

	""")

if operacion == "Suma":
	print(suma(op1, op2))
elif operacion == "Resta":
	print(resta(op1, op2))
elif operacion == "Multiplica":
	print(multiplica(op1, op2))
elif operacion == "Divide":
	print(divide(op1, op2))
else: 
	print("Se ha producido un error inesperado.")
