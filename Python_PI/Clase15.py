# Clase 15. Curso Píldoras Informáticas.

# Control de Flujo. Bucles 2. 


for i in ["Markus", "John", "Clarck"]:
	print("Sieg")

for i in ["Markus", "John", "Clarck"]:
	print("Sieg", end = " ")

for i in ["Markus", "John", "Clarck"]:
	print("Sieg", end = ". ")

print("\n")

# También puede recorrer un string.
for i in "alex@gamil.com":
	print(i, end = " ")

# Revisar si es un mail: 
print("\n\nEvaluación del mail")
email = False 
for i in "alex@gamil.com":
	if i == "@":
		email = True

if email == True: # No hace falta poner el == porque por defecto se considera real. Valdría con "if email"
	print("El mail alex@gamil.com es correcto.")
else: 
	print("El mail es incorrecto.")

print("\n\nEvaluación del email de Usuario.")
EmailUsuario = input("Introduzca su email: ")
email = False 
for i in EmailUsuario:
	if i == "@":
		email = True

if email == True:
	print("El mail es correcto.")
else: 
	print("El mail es incorrecto.")


# Que el mail tenga @ y punto. 
print("\nEvaluación exhaustiva del email de Usuario.")
email = False 
contador = 0
for i in EmailUsuario:
	if i == "@" or i == ".":
		contador += 1

if contador == 2:
	print("El mail es correcto.")
else: 
	print("El mail es incorrecto.")

print("\nHaciendo Rangos.")
for i in range(5):
	print(i)
	
