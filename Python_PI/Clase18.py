# Clase 18. Curso Píldoras Informáticas.

# Control de Flujo. Bucles 5. 

for i in "Alejandro":
	print("La letra de la presente posición es " + i)

print("\n")

for i in "Alejandro":
	if i == "a" or i == "A":
		continue

	print("La letra de la presente posición es " + i)

print("\n")

Frase = "Nüremberg ist Sieg"

# Considerando los espacios como caracteres. 
print(len(Frase))

# Prescindir de espacios. 
contador = 0
for i in Frase:
	if i == " ":
		continue
	contador+=1
print(contador)

# El siguiente bucle permanece en activo hasta pulsar: Ctrl + C
# while True:
# 	pass

# Clase nula. 
class Bob:
	pass

# Función nula:
def BobFun():
	pass

# Uso de break para búsqueda de arroba. 
email = input("Introduzca su mail, caballero: ")

for i in email:
	if i == "@":
		arroba = True
		break;
else:
	arroba = False

print(arroba)

