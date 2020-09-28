# Clase 12. Curso Píldoras Informáticas.

# Control de Flujo. Condicionales 3. 

# Switch. Se usa cuando se evalúan muchas decisiones concatenadas. No es muy útil en Python, por lo que no está. 
# Motivo: En Python se pueden concatenar operadores de comparación en condicionales.

Edad = 8

if 0 < Edad < 100:
	print("Edad humana.")
else:
	print("Edad inhumana.")

print("\n\nPrograma de Evaluación de Salarios.")
Salario_Presidente = int(input("Introduzca el Salario del Presidente: "))
print("El salario del Presidente es " + str(Salario_Presidente))

Salario_Director = int(input("Introduzca el Salario del Director: "))
print("El salario del Director es " + str(Salario_Director))

Salario_JefeLocal = int(input("Introduzca el Salario del Jefe de Área: "))
print("El salario del Jefe de Área es " + str(Salario_JefeLocal))

Salario_Administrativo = int(input("Introduzca el Salario del Administrativo: "))
print("El salario del Administrativo es " + str(Salario_Administrativo))

if Salario_Administrativo < Salario_JefeLocal < Salario_Director < Salario_Presidente:
	print("Los sueldos tienen sentido.")
else: 
	print("Algo falla con los salarios. Se recomienda realizar una investigación.")
