# Clase 22. Curso Píldoras Informáticas.

# Control de Flujo. Excepciones 2.

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

# Este bucle está hecho para que no continúe el código si 
# los valores introducidos son erróneos. Ya que la captura 
# de excepción no evita que siga la ejecución del programa
# y al no haber variables dará error al ejecutar una operación.

while True:
	try: 
		op1 = int(input("Introduce el primer número: "))
		op2 = int(input("Introduce el segundo número: "))
		break
	except ValueError:
		print("Eso no es un valor numérico entero.")

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


# Otro ejemplo para ver capturas:
# Se pueden poner varios except de forma consecuetiva. 
print("Segundo Programa de Cálculo")
def divII():
	try:

		number1 = float(input("Introduce el primer número: "))

		number2 = float(input("Introduce el segundo número: "))

		print("La división de", number1, "entre", number2, "es " +  str(number1/number2))

	except ValueError:

		print("Se han introducido erróneamente los valores.")

	except ZeroDivisionError:

		print("No se puede realizar una división por cero.")

	except: # Captura general.

		print("Se ha cometido un error desconocido.")

	finally: # Código que se ejecuta siempre, se produzca o no excepción.
	# Esto se hace con bases de datos. 
		print("Cálculo Finalizado.")

divII()

