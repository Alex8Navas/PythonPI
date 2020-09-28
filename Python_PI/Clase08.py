# Clase 8. Curso Píldoras Informáticas.

# Las Tuplas. 

# Son listas inmutables. 
# No permiten búsquedas ni movimientos de elementos, su eliminación o añadirlos. 
# Son de más rápida ejecución. Está más optimizada. 
# Se pueden usar de claves en un diccionario. 
# Las últimas versiones de Python permiten obtener los índices. 

RazasTupla = ("Elfos", "Enanos", "Humanos", "Orcos")
print(RazasTupla)
print(RazasTupla[2])

# Transformar tupla en lista y lista en tupla. 
RazasLista = list(RazasTupla)
print(RazasLista)
RazasTupla2 = tuple(RazasLista)
print(RazasTupla2)

# Comprobar si se encuentra elemento. 
print("Elfos" in RazasTupla)
print("Vampiros" in RazasTupla)

# Cuántos elementos de un mismo tipo se encuentran en una tupla. 
print(RazasTupla.count("Elfos"))
RazasTupla3 = ("Elfos", "Enanos", "Humanos", "Orcos", "Elfos")
print(RazasTupla3.count("Elfos"))

# Saber la longitud de una tupla.
print(len(RazasTupla))

# Tupla unitaria. 
RazaEspecial = ("Dragon", ) # Hay que añadir la coma al final. 
print(len(RazaEspecial))

# Se puede crear una tupla sin paréntesis. Se dice empaquetado de tupla. 
MixTupla = 93, "Elfos", 1990, 4.56
print(MixTupla)
# Se desaconseja su uso al poder confunirse con funciones que usan parámetros.   

# Desempaquetado de Tupla.
MixTupla2 = (14, "Gárgolas", 2004, 8.57)
Number, Species, Year, Power = MixTupla2
print(MixTupla2)
print(Species)
print(Power)
print(Year)
print(Number)

