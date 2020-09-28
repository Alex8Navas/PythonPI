# Clase 17. Curso Píldoras Informáticas.

# Control de Flujo. Bucles 4. 

# Los bucles indeterminados: bucles While. 

i = 1

while i<=10:
	print("Ejecución " + str(i))
	i+=1
print("Se han completado las series de ejecuciones.")

edad = int(input("Introduzca su edad, caballero: "))

while edad < 0:
	print("Su edad es negativa. Eso no es posible.")
	edad = int(input("Introduzca su edad, caballero: "))

while edad < 18 or edad > 100:
	print("Es usted menor de edad o un octogenario. Eso no entra en nuestros planes.")
	edad = int(input("Introduzca su edad, caballero: "))

print("Gracias por colaborar, caballero.")
print(f"La edad del caballero es de {edad}")

print("\nLas Raíces Cuadradas")
number = int(input("Introduzca un número, caballero: "))
trynumber = 0
while number <0:
	print("No existe la raíz de un número negativo.")
	if trynumber > 2: # Dos inclusive y comenzando el contador en cero, esto es, tienes cuatro oportunidades.
		print("Has agotado tus oportunidades.")
		break;
	number = int(input("Introduzca un número, caballero: "))
	if number<0:
		trynumber+=1
import math
if trynumber <= 2:
	solution = math.sqrt(number)
	print("La raíz cuadrada de " +  str(number) + " es " + str(solution))
