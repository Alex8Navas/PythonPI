# Clase 10. Curso Píldoras Informáticas.

# Control de Flujo. Condicionales. 

def evaluacion(Nota):
	valoracion = "Aprobado"
	if Nota < 5:
		valoracion = "Suspenso"
	return valoracion

print(evaluacion(7))
print(evaluacion(3))

# Mejora del Proceso
print("Programa de Evaluación del Alumnado")

Nota_Alumno = int(input("Introduce la nota del alumno: "))
def evaluacion2(Nota):
	valoracion = "Aprobado"
	if Nota < 5:
		valoracion = "Suspenso"
	return valoracion
print(evaluacion2(Nota_Alumno))

