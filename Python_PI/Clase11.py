# Clase 11. Curso Píldoras Informáticas.

# Control de Flujo. Condicionales 2. 

print("Verificación de Acceso")

EdadUsuario = int(input("Introduzca su edad, caballero: "))

if EdadUsuario < 18 and EdadUsuario > 0:
	print("Usted no puede pasar.")
elif EdadUsuario > 100 or EdadUsuario < 0:
	print("Edad incorrecta, caballero.")
else:
	print("Pase, caballero.")

print("El programa de verificación ha finalizado.\n\n")

print("Inicialización del Programa de Evaluación del Sujeto")

NotaSujeto = int(input("Introduzca su nota: "))

if NotaSujeto < 5 and NotaSujeto >= 0: 
	print("Insuficiente, caballero.")
elif NotaSujeto > 5 and NotaSujeto <= 6: 
	print("Suficiente, caballero.")
elif NotaSujeto > 6 and NotaSujeto <= 7: 
	print("Bien, caballero.")
elif NotaSujeto > 7 and NotaSujeto <= 8: 
	print("Notable, caballero.")
elif NotaSujeto > 8 and NotaSujeto <= 9: 
	print("Notable Alto, caballero.")
elif NotaSujeto > 9 and NotaSujeto <= 10: 
	print("Sobresaliente, caballero.")
else:
	print("No haga trampas.")


