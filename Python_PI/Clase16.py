# Clase 16. Curso Píldoras Informáticas.

# Control de Flujo. Bucles 3. 

for i in range(5):
	print(f"EL valor de la vriable es {i}")

for i in range(0, 50, 5): # De 0 a 50 (excluido) de cinco en cinco
	print(f"EL valor de la vriable es {i}")

print(len("Markus"))

print("\nAutentificación del Correo")
Autoriza = False
email = input("Intruduza su mail, por favor: ")
for i in range(len(email)):
	if email[i] == "@":
		Autoriza = True
if Autoriza == True:
	print("El correo es correcto, caballero.")
else:
	print("El correo es incorrecto.")
