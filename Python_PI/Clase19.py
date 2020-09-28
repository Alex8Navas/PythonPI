# Clase 19. Curso Píldoras Informáticas.

# Control de Flujo. Generadores 1.

# Más eficientes que las funciones tradicionales. Ahorra memoria y trabajo. 
# Útiles para trabajar con listas de valores infinitos como una lista que devuelva IPs random. 
# Además de yield puede llevar el método return. 


# Funcióm tradicional par crear una lista de números pares. 
def genpares(limit):
	num = 1
	Pares = []
	while num <= limit:
		Pares.append(num*2)
		num += 1

	return Pares

print(genpares(10))

# Con un generador. 
def genparesGenerator(limit):
	num = 1

	while num <= limit:
		yield num*2
		num += 1

# Se guarda el generador en un objeto. 
ParesGenerator = genparesGenerator(10) 

# Se puede recorrer todo el generador con un bucle for.
# Lo pongo como comentario porque si no la siguiente parte del código 
# no se podría ejecutar al estar sobrepasando el límite de iteraciones. 

# for i in ParesGenerator:
#	print(i)

# Devuelve el primer valor del generador. 
print("El primer elemento del generador es: " +  str(next(ParesGenerator)))
# Ahora entra en suspensión, lo cual es la mayor ventaja en eficiencia frente a la función. 

# Se llama al segundo elemento. 
print("El segundo elemento del generador es: " +  str(next(ParesGenerator)))

print("El tercer elemento del generador es: " +  str(next(ParesGenerator)))
