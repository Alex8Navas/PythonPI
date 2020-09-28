# Clase 9. Curso Píldoras Informáticas.

# Los Diccionarios. 

# Son arrays asociativos o tablas de Hash, es decir, pares de clave:valor. 
# Pueden almacenar listas, tuplas y otros diccionarios. 
# El orden no importa. 

RazasPoder = {
	"Elfos": 9.56,
	"Humanos" : 10.4,
	"Orcos" : 4.56,
	"Goblins" : 2.3,
	"Ninfas" : 7.8,
	"Licántropos" : 11,
}

print(RazasPoder["Elfos"])
print(RazasPoder["Ninfas"])
print(RazasPoder)

# Agregar elementos. 
RazasPoder["Enanos"] = 8.2
print(RazasPoder)

# Modificar valor por clave. Se sobreescribe. 
RazasPoder["Enanos"] = 8.7
print(RazasPoder)

# Eliminar elementos. 
del RazasPoder["Orcos"]
print(RazasPoder)

# Se pueden alternar distintos tipos de valores. 
Humanos = {
	"Héroe" : "Alduin",
	"Ataque" : 10.7,
	"Fundación" : 1876,
	"Efectivos" : 23489
}
print(Humanos)

# Definir diccionario con Lista. 
Lista = ["Ataque", "Defensa", "Efectivos", "Magia"]
Elfos = {
	Lista[0] : 12,
	Lista[1] : 3.4,
	Lista[2] : 478,
	Lista[3] : "Viento",
}
print(Elfos)

# Añadir como valor una lista. 
ElfosOscuros = {
	Lista[0] : 15,
	Lista[1] : 6,
	Lista[2] : 218,
	Lista[3] : "Fuego",
	"Héroes" : ["Malekith", "Malida", "Malus", "Morkaris", "Mortharor"]
}
print(ElfosOscuros)
print(ElfosOscuros["Magia"])
print(ElfosOscuros["Héroes"])

# Diccionarios dentro de diccionarios. 
RazasElficas = {
	"Altos Elfos" : Elfos,
	"Elfos Oscuros" : ElfosOscuros
}
print(RazasElficas)
print(RazasElficas["Altos Elfos"])
print(RazasElficas["Elfos Oscuros"])

# Funciones interesantes para los diccionarios. 
print(ElfosOscuros.keys())
print(ElfosOscuros.values())
print(len(ElfosOscuros))

