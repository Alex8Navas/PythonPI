# Clase 13. Curso Píldoras Informáticas.

# Control de Flujo. Condicionales 4. 

print("Programa de Concesión de Becas del Estado.\n")

print("Concesión de Beca General.")

Distancia = int(input("¿A qué distancia vives del colegio? \n"))
print("La distancia a la escuela del alumno es", Distancia, ".")
Hermanos = int(input("¿Cuántos hermanos tienes? \n"))
print("El alumno tiene", Hermanos, "hermanos.")
SalarioFamiliar = int(input("¿Cuál es el salario neto de tu familia? \n"))
print("El salario familiar es de", SalarioFamiliar, "euros.\n")

if Distancia > 40 and Hermanos > 2 and SalarioFamiliar <= 10000:
	print("Se le ha concedido la beca general.")
else: 
	print("Beca general denegada.")

print("\nConcesión de Beca Especial.\n")
if Distancia > 40 and Hermanos > 2 or SalarioFamiliar <= 10000:
	print("Se le ha concedido la beca especial.")
else: 
	print("Beca especial denegada.")

print("\nAsignaturas optativas del año 2020.\n")
print("""Optativas disponibles:

	- Software.
	- Usabilidad y Accesibilidad.
	- Informática Gráfica.

	""")
Asignatura = input("Optativa a seleccionar: ")
Asignatura = Asignatura.lower()
if Asignatura in ("software", "usabilidad y accesibilidad", "informática gráfica"):
	print("Se ha seleccionado " + Asignatura)
else:
	print("Tal asignatura no está en el programa")
