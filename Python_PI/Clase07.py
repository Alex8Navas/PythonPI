# Clase 7. Curso Píldoras Informáticas.

# Listas 

# Pueden almacenar distintas clases de valores. 
# Se pueden expandir de forma dinámica. 
# Primer elemento: Posición cero. 

Razas = ["Elfos", "Enanos", "Humanos", "Orcos"]
print(Razas[:])
print(Razas[2])
# print(Razas[7]) <- Esto dará error por estar fuera de rango. 
print(Razas[-1]) # Lee al revés, partiendo de -1, no de cero. 
print(Razas[-3])
print(Razas[0:3]) # Extremo superior excluido. 
print(Razas[:2]) # Posición cero por defecto. 
print(Razas[2:]) # Accede hasta el final. 

# Agregar elemento al final de la lista. 
Razas.append("Hadas")
print(Razas[:])

# Agregar elemento en la posicióon deseada de la lista.
Razas.insert(2, "Ninfas")
print(Razas[:])

# Agregar varios elementos. 
Razas.extend(["Cíclopes", "Goblins", "Vampiros", "Vampiros"])
print(Razas[:])

# Dar índice del elemento deseado. 
print(Razas.index("Cíclopes"))
# Si se repite el elemento devuelve el primero. 
print(Razas.index("Vampiros"))

# Saber si se encuentra un elemento en la lista. 
print("Vampiros" in Razas)
print("Licántropos" in Razas)

# Las listas pueden almacenar distintos valores. 
Mix = [4, 5.6, True, "Mark"]
print(Mix[:])

# Eliminación de elementos. 
Mix.remove(5.6)
print(Mix[:])

# Eliminar el último elemento. 
Mix.pop()
print(Mix[:])

# Unir listas. Operador suma para concatenar.  
Mix2 = ["Michael", 7.8]
SuperMix = Mix + Mix2
print(SuperMix)

# El * funciona a modo de replicador. 
SuperMix2 = SuperMix * 3
print(SuperMix2)
